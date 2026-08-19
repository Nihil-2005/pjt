#!/usr/bin/env bash
# ============================================================================
# scan.sh — Full-potential multi-scanner web vulnerability pipeline
# ----------------------------------------------------------------------------
# Scanners : Nuclei · Wapiti · OWASP ZAP (full/active) · Trivy   [Docker]
# Targets  : OWASP Juice Shop · NodeGoat · bWAPP                 [Docker]
# Auth     : Automatic login per target (form/API) → cookies/headers
#            injected into every scanner.
# Reports  : JSON + HTML per scanner (json_to_html.py), ZAP XML/HTML,
#            scan.log + summary.html with a findings matrix.
#
# Env overrides:
#   RESUME=0|1            Resume unfinished scan        (default 1)
#   PARALLEL=0|1          Run 4 scanners concurrently    (default 0)
#   SCAN_MODE=quick|deep  Deep = full templates + active (default quick)
#   TARGETS_ONLY=a,b      Subset, e.g. "bwapp,nodegoat"  (default: all)
#   ZAP_MAX_MINUTES=15    WAPITI_MAX_TIME=30  NUCLEI_TIMEOUT=900
#   ZAP_TIMEOUT=1800      TRIVY_TIMEOUT=900   WAPITI_TIMEOUT=1800
#   MAX_DEPTH=10          SKIP_TRIVY=1        NETWORK=vulnlab
# ============================================================================

# ── Auto re-launch inside WSL when started from Windows ──────────────────────
if [ -z "${WSL_DISTRO_NAME:-}" ] && command -v wsl >/dev/null 2>&1; then
    script_dir="$(cd "$(dirname "$0")" && pwd)"
    wsl_dir="$(printf '%s' "$script_dir" | sed -E 's|^/([a-zA-Z])/|/mnt/\L\1/|')"
    script_name="$(basename "$0")"
    echo "🪟 Detected Windows shell — re-launching inside WSL..."
    exec wsl bash -lc "cd '$wsl_dir' && bash '$script_name'"
fi

set -euo pipefail

# ── Globals ──────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NETWORK="${NETWORK:-vulnlab}"
COMPOSE_FILE="${COMPOSE_FILE:-$SCRIPT_DIR/docker-compose.yml}"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
SCAN_TIME="$(date)"
CONTAINER_PREFIX="vlscan"
AUTH_DIR="$(mktemp -d /tmp/vulnlab-auth.XXXXXX)"
declare -A SCAN_STATUS

# ── Configurable knobs ───────────────────────────────────────────────────────
RESUME="${RESUME:-1}"
PARALLEL="${PARALLEL:-0}"
SCAN_MODE="${SCAN_MODE:-quick}"          # quick | deep
ZAP_MAX_MINUTES="${ZAP_MAX_MINUTES:-15}"
WAPITI_MAX_TIME="${WAPITI_MAX_TIME:-30}"
NUCLEI_TIMEOUT="${NUCLEI_TIMEOUT:-900}"
WAPITI_TIMEOUT="${WAPITI_TIMEOUT:-1800}"
ZAP_TIMEOUT="${ZAP_TIMEOUT:-1800}"
TRIVY_TIMEOUT="${TRIVY_TIMEOUT:-900}"
SKIP_TRIVY="${SKIP_TRIVY:-0}"
MAX_DEPTH="${MAX_DEPTH:-10}"

# deep mode: longer budgets, full template assault
if [ "$SCAN_MODE" = "deep" ]; then
    ZAP_MAX_MINUTES=30; WAPITI_MAX_TIME=60
    NUCLEI_TIMEOUT=1800; ZAP_TIMEOUT=3600
fi

# ── Targets: docker_url | host_url(readiness) | image | auth_type ────────────
declare -A TARGETS=(
    ["juice_shop"]="http://juice-shop:3000|http://localhost:3000|bkimminich/juice-shop:latest|api"
    ["nodegoat"]="http://nodegoat:4000|http://localhost:4000|nodegoat-web:latest|form"
    ["bwapp"]="http://bwapp:80|http://localhost:8080|raesene/bwapp:latest|form"
)
ORDER=(juice_shop nodegoat bwapp)

# ── Default credentials (override via credentials/<target>.json) ─────────────
declare -A DEFAULT_AUTH=(
    ["bwapp"]='{"login_url":"/login.php","auth_url":"/login.php","username":"bee","password":"bug","extra_fields":{"security_level":"0"}}'
    ["nodegoat"]='{"register_url":"/signup","register_fields":{"firstName":"Sec","lastName":"Test","userName":"sectest","password":"Test123!","verify":"Test123!"},"login_url":"/login","auth_url":"/login","username":"sectest","password":"Test123!","login_field":"userName","password_field":"password"}'
    ["juice_shop"]='{"register_email":"scanner@test.local","register_password":"Scanner123!","login_api":"/rest/user/login"}'
)

# ── Logging & traps ──────────────────────────────────────────────────────────
trap 'echo "❌ Error at line $LINENO (exit $?)"' ERR
trap 'echo "🛑 Interrupted — cleaning up..."; jobs -p | xargs -r kill 2>/dev/null; exit 130' INT TERM

die()  { echo "❌ $*" >&2; exit 1; }
info() { echo "ℹ️  $*"; }
warn() { echo "⚠️  $*" >&2; }

# ── Pre-flight checks ────────────────────────────────────────────────────────
preflight() {
    for tool in docker jq curl timeout; do
        command -v "$tool" >/dev/null 2>&1 || die "Required tool missing: $tool"
    done
    docker info >/dev/null 2>&1 || die "Docker daemon is not running or not accessible"
    info "Pre-flight checks passed"
}

# ── Report directory (resume-aware; raw scans archive under ../scan_reports/) ──
SCAN_ARCHIVE="${SCAN_ARCHIVE:-$SCRIPT_DIR/../scan_reports}"
mkdir -p "$SCAN_ARCHIVE"
REPORT_DIR="$SCAN_ARCHIVE/scan_reports_$TIMESTAMP"
if [ "$RESUME" = "1" ]; then
    # trailing slash restricts the glob to directories (ignores *.zip copies)
    LATEST="$(ls -d "$SCAN_ARCHIVE"/scan_reports_*/ 2>/dev/null | sort | tail -1 || true)"
    LATEST="${LATEST%/}"
    if [ -n "${LATEST:-}" ] && [ -d "$LATEST" ] && [ ! -f "$LATEST/summary.html" ]; then
        REPORT_DIR="$LATEST"
        info "Resuming previous scan in: $REPORT_DIR"
    fi
fi
mkdir -p "$REPORT_DIR"
REPORT_PATH="$(realpath "$REPORT_DIR")"
LOG_FILE="$REPORT_DIR/scan.log"

# tee all output to the log from this point on
exec > >(tee -a "$LOG_FILE") 2>&1

echo "==========================================================================="
echo "🚀 FULL-POTENTIAL VULNERABILITY SCAN SUITE"
echo "   Mode: $SCAN_MODE | Parallel: $PARALLEL | Resume: $RESUME"
echo "==========================================================================="
info "Reports: $REPORT_PATH"

# ── Helper: wait for HTTP endpoint ───────────────────────────────────────────
wait_for_http() {
    local name=$1 url=$2 timeout=${3:-180} elapsed=0
    until curl -s -o /dev/null --max-time 3 "$url" 2>/dev/null; do
        if [ "$elapsed" -ge "$timeout" ]; then
            warn "$name not ready after ${timeout}s (scanning anyway)"
            return 1
        fi
        sleep 5; elapsed=$((elapsed + 5))
    done
    echo "   ✅ $name is up"
}

# ── Ensure target stack is running ───────────────────────────────────────────
ensure_targets_up() {
    local need_start=0 c
    if ! docker network inspect "$NETWORK" >/dev/null 2>&1; then
        need_start=1
    else
        for c in vulnlab-juice-shop vulnlab-nodegoat vulnlab-bwapp vulnlab-mongo; do
            docker ps --format '{{.Names}}' | grep -qx "$c" || { need_start=1; break; }
        done
    fi

    if [ "$need_start" -eq 1 ]; then
        info "Target containers not running — starting via docker compose..."
        if [ -f "$COMPOSE_FILE" ]; then
            docker compose -f "$COMPOSE_FILE" up -d
        else
            docker compose up -d
        fi
    fi

    echo "⏳ Waiting for targets..."
    local name url
    for name in "${ORDER[@]}"; do
        url="$(cut -d'|' -f2 <<< "${TARGETS[$name]}")"
        wait_for_http "$name" "$url" 180 || true
    done
}

# ── Ensure Wapiti image exists ───────────────────────────────────────────────
ensure_wapiti_image() {
    if ! docker image inspect vulnlab/wapiti:latest >/dev/null 2>&1; then
        info "Building Wapiti scanner image (first run)..."
        [ -f "$SCRIPT_DIR/Dockerfile.wapiti" ] || die "Dockerfile.wapiti not found"
        docker build -f "$SCRIPT_DIR/Dockerfile.wapiti" -t vulnlab/wapiti:latest "$SCRIPT_DIR"
    fi
}

# ── Build the credentials file for a target (merged with defaults) ───────────
build_creds() {
    local target=$1
    local custom="$SCRIPT_DIR/credentials/$target.json"
    mkdir -p "$SCRIPT_DIR/credentials"
    if [ -f "$custom" ]; then
        jq -s '.[0] * .[1]' <(printf '%s' "${DEFAULT_AUTH[$target]}") "$custom" > "$AUTH_DIR/$target.json" \
            || { warn "Invalid credentials file $custom — using defaults"; \
                 printf '%s' "${DEFAULT_AUTH[$target]}" > "$AUTH_DIR/$target.json"; }
    else
        printf '%s' "${DEFAULT_AUTH[$target]}" > "$AUTH_DIR/$target.json"
    fi
}

# ── URL-encode a value for form posts (never fails the scan on jq hiccups) ────
urlenc() { printf '%s' "$1" | jq -sRr @uri 2>/dev/null || printf '%s' "$1"; }

# ── Login & capture session artifacts ────────────────────────────────────────
# Sets globals: AUTH_HEADER (Cookie:/Authorization: line) | AUTH_TYPE
login_target() {
    local target=$1 auth_type=$2
    AUTH_HEADER="" ; AUTH_TYPE="none"
    [ "$auth_type" = "none" ] && return 0

    build_creds "$target"
    # Login curls run on the host, so use the published localhost URL; the
    # in-network hostname (e.g. juice-shop:3000) only resolves inside containers.
    IFS='|' read -r _ host_url _ <<< "${TARGETS[$target]}"
    local jar="$AUTH_DIR/$target.cookies"

    case "$auth_type" in
        form)
            local login_url username password extra_fields reg_url reg_fields
            login_url="$(jq -r '.login_url' "$AUTH_DIR/$target.json")"
            username="$(jq -r '.username' "$AUTH_DIR/$target.json")"
            password="$(jq -r '.password' "$AUTH_DIR/$target.json")"
            extra_fields="$(jq -r '.extra_fields // {} | to_entries | map("\(.key)=\(.value|@uri)") | join("&")' "$AUTH_DIR/$target.json" 2>/dev/null || true)"
            reg_url="$(jq -r '.register_url // empty' "$AUTH_DIR/$target.json")"

            # Optional registration first (NodeGoat needs signup)
            if [ -n "$reg_url" ]; then
                reg_fields="$(jq -r '.register_fields // {} | to_entries | map("\(.key)=\(.value|@uri)") | join("&")' "$AUTH_DIR/$target.json" 2>/dev/null || true)"
                curl -s -o /dev/null -c "$jar" -b "$jar" -L \
                    -d "$reg_fields" "$host_url$reg_url" || true
            fi

            local lf pf
            lf="$(jq -r '.login_field // "login"' "$AUTH_DIR/$target.json")"
            pf="$(jq -r '.password_field // "password"' "$AUTH_DIR/$target.json")"
            local form
            form="$(urlenc "$lf")=$(urlenc "$username")&$(urlenc "$pf")=$(urlenc "$password")"
            [ -n "$extra_fields" ] && form="$form&$extra_fields"

            curl -s -o /dev/null -c "$jar" -b "$jar" -L \
                -d "$form" "$host_url$login_url" || warn "Login POST failed for $target"

            if [ -s "$jar" ]; then
                local cookie_str
                cookie_str="$(awk 'NF>=7 && $6!~/^#/ {printf "%s%s=%s", sep, $6, $7; sep="; "}' "$jar")"
                if [ -n "$cookie_str" ]; then
                    AUTH_HEADER="Cookie: $cookie_str"
                    AUTH_TYPE="form"
                fi
            fi
            ;;
        api)   # Juice Shop: register then login via REST → JWT Bearer
            local email pass login_api token
            email="$(jq -r '.register_email' "$AUTH_DIR/$target.json")"
            pass="$(jq -r '.register_password' "$AUTH_DIR/$target.json")"
            login_api="$(jq -r '.login_api' "$AUTH_DIR/$target.json")"

            # best-effort registration (ignore if already exists); Juice Shop
            # requires passwordRepeat, without it the account is never created
            curl -s -o /dev/null -H 'Content-Type: application/json' \
                -d "{\"email\":\"$email\",\"password\":\"$pass\",\"passwordRepeat\":\"$pass\"}" \
                "$host_url/api/Users" || true

            token="$(curl -s -H 'Content-Type: application/json' \
                -d "{\"email\":\"$email\",\"password\":\"$pass\"}" \
                "$host_url$login_api" | jq -r '.authentication.token // empty' 2>/dev/null || true)"

            if [ -n "$token" ]; then
                AUTH_HEADER="Authorization: Bearer $token"
                AUTH_TYPE="api"
            else
                warn "API login failed for $target (falling back to unauthenticated)"
            fi
            ;;
    esac

    if [ -n "$AUTH_HEADER" ]; then
        info "Authenticated to $target via $AUTH_TYPE"
    else
        warn "No auth obtained for $target — scanning unauthenticated"
    fi
}

# ── Write ZAP hook that injects the auth header into every request ───────────
# zap-full-scan.py has no -H option (baseline-only), so we add a Replacer rule
# from a python hook instead: it swaps in the session header for the whole run.
write_zap_hook() {
    local target=$1 hdr_name hdr_val
    hdr_name="${AUTH_HEADER%%:*}"
    hdr_val="${AUTH_HEADER#*: }"
    cat > "$AUTH_DIR/$target.hook" << PYEOF
# Replaces the session header value on every request ZAP sends.
def zap_started(zap, target):
    zap.replacer.add_rule(
        description="auth", enabled="true", matchtype="REQ_HEADER",
        matchregex="false", matchstring="$hdr_name",
        replacement="$hdr_val", initiators="")
PYEOF
}

# ── Helper: docker run wrapper with timeout + named container ────────────────
run_docker() {
    local name=$1 tmo=$2; shift 2
    timeout "$tmo" docker run --rm --name "$name" "$@" \
        && return 0 || {
            local rc=$?
            [ $rc -eq 124 ] && warn "$name timed out after ${tmo}s"
            return $rc
        }
}

# ── Helper: count findings in a scanner JSON report ──────────────────────────
count_findings() {
    local scanner=$1 json=$2
    case "$scanner" in
        nuclei) jq 'length' "$json" 2>/dev/null || echo 0 ;;
        wapiti) jq '[.vulnerabilities[] | length] | add // 0' "$json" 2>/dev/null || echo 0 ;;
        zap)    jq '[.site[]?.alerts[]?] | length' "$json" 2>/dev/null || echo 0 ;;
        trivy)  jq '[.Results[]? | .Vulnerabilities? // [] | length] | add // 0' "$json" 2>/dev/null || echo 0 ;;
    esac
}

# ── Helper: resume-skip a scanner but keep its count in the summary matrix ───
resume_skip() {
    local target=$1 scanner=$2
    local json="$REPORT_DIR/${target}_$scanner.json"
    echo "   ⏭️  Skipping (resume — $json exists)"
    [ -s "$json" ] && printf '%s' "$(count_findings "$scanner" "$json")" > "$AUTH_DIR/$target-$scanner.count"
    return 0
}

# ── Scanner 1: Nuclei (full template power + auth) ───────────────────────────
scan_nuclei() {
    local target=$1 url=$2
    echo "[1/4] Nuclei → $target"

    if [ "$RESUME" = "1" ] && { [ -s "$REPORT_DIR/${target}_nuclei.json" ] \
        || docker ps -q --filter "name=${CONTAINER_PREFIX}-nuclei-$target" | grep -q .; }; then
        resume_skip "$target" nuclei; return 0
    fi

    local -a cmd=( projectdiscovery/nuclei:latest -u "$url"
        -json-export "/reports/${target}_nuclei.json"
        -o "/reports/${target}_nuclei.txt"
        -timeout 10 -retries 1 )

    if [ "$SCAN_MODE" = "deep" ]; then
        cmd+=( -t http/ -t javascript/ )       # full template set
    else
        cmd+=( -etags dos fuzz )               # quick: skip noisy categories
    fi
    [ -n "$AUTH_HEADER" ] && cmd+=( -H "$AUTH_HEADER" )

    run_docker "${CONTAINER_PREFIX}-nuclei-$target" "$NUCLEI_TIMEOUT" \
        -v "$REPORT_PATH:/reports" -v nuclei-templates:/root/nuclei-templates \
        --network "$NETWORK" "${cmd[@]}" || true

    if [ -s "$REPORT_DIR/${target}_nuclei.json" ]; then
        local n; n="$(count_findings nuclei "$REPORT_DIR/${target}_nuclei.json")"
        echo "   ✅ Nuclei: $n findings"
        python3 "$SCRIPT_DIR/json_to_html.py" nuclei "$REPORT_DIR/${target}_nuclei.json" \
            "$REPORT_DIR/${target}_nuclei.html" "Nuclei — $target" 2>/dev/null || true
        printf '%s' "$n" > "$AUTH_DIR/$target-nuclei.count"
    else
        echo "   ⚠️  Nuclei produced no JSON"; printf '0/err' > "$AUTH_DIR/$target-nuclei.count"
    fi
}

# ── Scanner 2: Wapiti (full modules, domain scope, POST auth) ────────────────
scan_wapiti() {
    local target=$1 url=$2
    echo "[2/4] Wapiti → $target"

    if [ "$RESUME" = "1" ] && { [ -s "$REPORT_DIR/${target}_wapiti.json" ] \
        || docker ps -q --filter "name=${CONTAINER_PREFIX}-wapiti-$target" | grep -q .; }; then
        resume_skip "$target" wapiti; return 0
    fi

    local -a cmd=( -u "$url" -f json -o "/reports/${target}_wapiti.json"
        --scope domain -d "$MAX_DEPTH" --max-files-per-dir 50
        --flush-session --max-scan-time "$WAPITI_MAX_TIME" )

    if [ "$AUTH_TYPE" = "form" ]; then
        local auth_url username password
        auth_url="$(jq -r '.auth_url // .login_url' "$AUTH_DIR/$target.json")"
        username="$(jq -r '.username' "$AUTH_DIR/$target.json")"
        password="$(jq -r '.password' "$AUTH_DIR/$target.json")"
        IFS='|' read -r docker_url _ _ <<< "${TARGETS[$target]}"
        # wapiti3 fetches the login page and fills the username/password fields itself
        cmd+=( --form-user "$username" --form-password "$password" --form-url "$docker_url$auth_url" )
    fi

    run_docker "${CONTAINER_PREFIX}-wapiti-$target" "$WAPITI_TIMEOUT" \
        -v "$REPORT_PATH:/reports" -v "$AUTH_DIR:/creds:ro" \
        --network "$NETWORK" vulnlab/wapiti:latest "${cmd[@]}" || true

    if [ -s "$REPORT_DIR/${target}_wapiti.json" ]; then
        local n; n="$(count_findings wapiti "$REPORT_DIR/${target}_wapiti.json")"
        echo "   ✅ Wapiti: $n findings"
        python3 "$SCRIPT_DIR/json_to_html.py" wapiti "$REPORT_DIR/${target}_wapiti.json" \
            "$REPORT_DIR/${target}_wapiti.html" "Wapiti — $target" 2>/dev/null || true
        printf '%s' "$n" > "$AUTH_DIR/$target-wapiti.count"
    else
        echo "   ⚠️  Wapiti produced no JSON"; printf '0/err' > "$AUTH_DIR/$target-wapiti.count"
    fi
}

# ── Scanner 3: OWASP ZAP — FULL active scan with auth context ────────────────
write_zap_context() {
    local target=$1 url=$2 ctx="$REPORT_DIR/$target.context"
    cat > "$ctx" << XML
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <context>
    <name>$target</name>
    <inscope>true</inscope>
    <includeRegexs><regex>$url.*</regex></includeRegexs>
  </context>
</configuration>
XML
}

scan_zap() {
    local target=$1 url=$2
    echo "[3/4] OWASP ZAP (full/active) → $target"

    if [ "$RESUME" = "1" ] && { [ -s "$REPORT_DIR/${target}_zap.json" ] \
        || docker ps -q --filter "name=${CONTAINER_PREFIX}-zap-$target" | grep -q .; }; then
        resume_skip "$target" zap; return 0
    fi

    # Prefer full (active) scan; fall back to baseline if unavailable
    local script="zap-full-scan.py"
    if ! docker run --rm ghcr.io/zaproxy/zaproxy:stable which "$script" >/dev/null 2>&1; then
        warn "zap-full-scan.py not found — falling back to baseline"
        script="zap-baseline.py"
    fi

    write_zap_context "$target" "$url"

    local -a cmd=( "$script" -t "$url" -m "$ZAP_MAX_MINUTES"
        -J "${target}_zap.json" -x "${target}_zap.xml" -r "${target}_zap.html"
        -n "/zap/wrk/${target}.context" )
    if [ -f "$SCRIPT_DIR/zap.conf" ]; then
        cmd+=( -c "/zap/wrk/zap.conf" )
    fi
    if [ -n "$AUTH_HEADER" ]; then
        write_zap_hook "$target"
        cmd+=( --hook "/zap/auth/$target.hook" )
    fi

    run_docker "${CONTAINER_PREFIX}-zap-$target" "$ZAP_TIMEOUT" \
        -u zap -v "$REPORT_PATH:/zap/wrk/:rw" -v "$AUTH_DIR:/zap/auth:ro" \
        --network "$NETWORK" ghcr.io/zaproxy/zaproxy:stable "${cmd[@]}" || true

    if [ -s "$REPORT_DIR/${target}_zap.json" ]; then
        local n; n="$(count_findings zap "$REPORT_DIR/${target}_zap.json")"
        echo "   ✅ ZAP: $n alerts"
        printf '%s' "$n" > "$AUTH_DIR/$target-zap.count"
    else
        echo "   ⚠️  ZAP produced no JSON"; printf '0/err' > "$AUTH_DIR/$target-zap.count"
    fi
}

# ── Scanner 4: Trivy — image scanning ────────────────────────────────────────
scan_trivy() {
    local target=$1 image=$2
    echo "[4/4] Trivy → $image"
    [ "$SKIP_TRIVY" = "1" ] && { echo "   ⏭️  Skipped (SKIP_TRIVY=1)"; return 0; }

    if [ "$RESUME" = "1" ] && { [ -s "$REPORT_DIR/${target}_trivy.json" ] \
        || docker ps -q --filter "name=${CONTAINER_PREFIX}-trivy-$target" | grep -q .; }; then
        resume_skip "$target" trivy; return 0
    fi

    run_docker "${CONTAINER_PREFIX}-trivy-$target" "$TRIVY_TIMEOUT" \
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v trivy-cache:/root/.cache/trivy \
        -v "$REPORT_PATH:/reports" \
        --network "$NETWORK" \
        aquasec/trivy:latest image \
        --format json -o "/reports/${target}_trivy.json" \
        --severity CRITICAL,HIGH,MEDIUM,LOW "$image" || true

    if [ -s "$REPORT_DIR/${target}_trivy.json" ]; then
        local n; n="$(count_findings trivy "$REPORT_DIR/${target}_trivy.json")"
        echo "   ✅ Trivy: $n vulns"
        python3 "$SCRIPT_DIR/json_to_html.py" trivy "$REPORT_DIR/${target}_trivy.json" \
            "$REPORT_DIR/${target}_trivy.html" "Trivy — $target" 2>/dev/null || true
        printf '%s' "$n" > "$AUTH_DIR/$target-trivy.count"
    else
        echo "   ⚠️  Trivy produced no JSON"; printf '0/err' > "$AUTH_DIR/$target-trivy.count"
    fi
}

# ── Run all scanners for one target (sequential or parallel) ─────────────────
scan_target() {
    local target=$1 docker_url=$2 image=$3 auth_type=$4
    local -a scanners=(nuclei wapiti zap trivy)
    local s

    login_target "$target" "$auth_type"
    echo ""

    if [ "$PARALLEL" = "1" ]; then
        scan_nuclei "$target" "$docker_url" &  local p1=$!
        scan_wapiti "$target" "$docker_url" &  local p2=$!
        scan_zap    "$target" "$docker_url" &  local p3=$!
        scan_trivy  "$target" "$image"      &  local p4=$!
        wait $p1 $p2 $p3 $p4 || warn "One or more scanners for $target reported errors"
    else
        scan_nuclei "$target" "$docker_url"; echo ""
        scan_wapiti "$target" "$docker_url"; echo ""
        scan_zap    "$target" "$docker_url"; echo ""
        scan_trivy  "$target" "$image";      echo ""
    fi

    # Collect counts written by each scanner (background subshells cannot
    # update SCAN_STATUS directly, so every mode funnels through count files).
    for s in "${scanners[@]}"; do
        if [ -f "$AUTH_DIR/$target-$s.count" ]; then
            SCAN_STATUS["$target-$s"]="$(cat "$AUTH_DIR/$target-$s.count")"
        fi
    done
}

# ── Summary HTML ──────────────────────────────────────────────────────────────
generate_summary() {
    local html="$REPORT_DIR/summary.html"
    cat > "$html" << HTML
<!DOCTYPE html>
<html><head><title>Vulnerability Scan Summary</title>
<style>
body{font-family:Arial,sans-serif;margin:40px;background:#f5f5f5}
.card{background:#fff;padding:20px;border-radius:10px;box-shadow:0 2px 4px rgba(0,0,0,.1);margin-bottom:20px}
table{width:100%;border-collapse:collapse}
th,td{padding:10px;text-align:left;border-bottom:1px solid #ddd}
th{background:#2196F3;color:#fff}
tr:hover{background:#f0f0f0}
.err{color:#c00}.ok{color:#080}
</style></head><body>
<h1>🔒 Full-Potential Scan Summary</h1>
<div class="card">
<p><strong>Time:</strong> $SCAN_TIME</p>
<p><strong>Mode:</strong> $SCAN_MODE | <strong>Parallel:</strong> $PARALLEL</p>
<p><strong>Targets:</strong> ${#ORDER[@]} · <strong>Scanners:</strong> Nuclei, Wapiti, ZAP (full), Trivy</p>
</div>
<div class="card"><h2>Findings Matrix</h2>
<table><tr><th>Target</th><th>Nuclei</th><th>Wapiti</th><th>ZAP</th><th>Trivy</th></tr>
HTML

    local t nuc wap zap tri
    for t in "${ORDER[@]}"; do
        nuc="${SCAN_STATUS[$t-nuclei]:-—}"; wap="${SCAN_STATUS[$t-wapiti]:-—}"
        zap="${SCAN_STATUS[$t-zap]:-—}";    tri="${SCAN_STATUS[$t-trivy]:-—}"
        echo "<tr><td>$t</td><td>$nuc</td><td>$wap</td><td>$zap</td><td>$tri</td></tr>" >> "$html"
    done

    cat >> "$html" << HTML
</table></div>
<div class="card"><h2>📁 Report Files</h2><ul>
HTML
    local f
    for f in "$REPORT_DIR"/*; do
        [ -f "$f" ] && echo "<li><code>$(basename "$f")</code> ($(du -h "$f" | cut -f1))</li>" >> "$html"
    done
    cat >> "$html" << HTML
</ul></div>
<p style="color:#666">📍 $REPORT_PATH · Log: scan.log</p>
</body></html>
HTML
    echo "✅ Summary: $html"
}

# ── Main ──────────────────────────────────────────────────────────────────────
main() {
    preflight
    ensure_wapiti_image
    ensure_targets_up

    local target docker_url host_url image auth_type
    for target in "${ORDER[@]}"; do
        # optional subset filter: TARGETS_ONLY="bwapp,nodegoat"
        if [ -n "${TARGETS_ONLY:-}" ]; then
            case ",$TARGETS_ONLY," in *",$target,"*) ;; *) continue ;; esac
        fi

        IFS='|' read -r docker_url host_url image auth_type <<< "${TARGETS[$target]}"

        echo "==========================================================================="
        echo "🔍 SCANNING: $target  ($docker_url)"
        echo "==========================================================================="
        scan_target "$target" "$docker_url" "$image" "$auth_type"
    done

    generate_summary

    # best-effort ownership fix (never prompt)
    if command -v sudo >/dev/null 2>&1; then
        sudo -n chown -R "${SUDO_USER:-$USER}" "$REPORT_DIR" 2>/dev/null || true
    fi
    rm -rf "$AUTH_DIR"

    echo ""
    echo "==========================================================================="
    echo "✅ ALL SCANS COMPLETE"
    echo "📁 Reports : $REPORT_PATH"
    echo "📋 Log     : $LOG_FILE"
    echo "🌐 Open    : $REPORT_DIR/summary.html"
    echo "==========================================================================="
}

main "$@"
