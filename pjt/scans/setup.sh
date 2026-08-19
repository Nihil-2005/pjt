#!/bin/bash

# ── Auto re-launch inside WSL when started from Windows (Git Bash / CMD) ──
if [ -z "${WSL_DISTRO_NAME:-}" ] && command -v wsl >/dev/null 2>&1; then
    script_dir="$(cd "$(dirname "$0")" && pwd)"
    wsl_dir="$(printf '%s' "$script_dir" | sed -E 's|^/([a-zA-Z])/|/mnt/\L\1/|')"
    script_name="$(basename "$0")"
    echo "🪟 Detected Windows shell — re-launching inside WSL..."
    exec wsl bash -lc "cd '$wsl_dir' && bash '$script_name'"
fi

set -e

wait_for_http() {
    local name=$1 url=$2 timeout=$3 elapsed=0
    until curl -s -o /dev/null --max-time 3 "$url" 2>/dev/null; do
        if [ "$elapsed" -ge "$timeout" ]; then
            echo "   ⚠️  $name not ready after ${timeout}s — check 'docker compose ps'"
            return 1
        fi
        sleep 5
        elapsed=$((elapsed + 5))
    done
    echo "   ✅ $name is up"
}

echo "==========================================================================="
echo "🔧 SETTING UP VULNERABILITY LAB (all in Docker, inside WSL)"
echo "==========================================================================="
echo ""

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "== [1/3] Building Wapiti scanner image =="
docker build -f "$SCRIPT_DIR/Dockerfile.wapiti" -t vulnlab/wapiti:latest "$SCRIPT_DIR"
echo ""

echo "== [2/3] Starting vulnerable target containers =="
docker compose -f "$SCRIPT_DIR/docker-compose.yml" up -d
echo ""

echo "== [3/3] Waiting for targets to become ready =="
wait_for_http "juice-shop" "http://localhost:3000" 180 || true
wait_for_http "nodegoat"  "http://localhost:4000" 180 || true
wait_for_http "bwapp"     "http://localhost:8080" 240 || true

echo ""
echo "==========================================================================="
echo "✅ LAB READY!"
echo "   Juice Shop : http://localhost:3000"
echo "   NodeGoat   : http://localhost:4000"
echo "   bWAPP      : http://localhost:8080"
echo ""
echo "   Next step  : bash scan.sh"
echo "   Stop lab   : docker compose down"
echo "==========================================================================="
