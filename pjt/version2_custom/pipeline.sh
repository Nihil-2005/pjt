#!/usr/bin/env bash
# ============================================================================
# pipeline.sh (version 2) — fully custom substrate, no DefectDojo.
#
#   1. shared core: normalize -> dedup -> filter -> enrich -> attack paths
#      -> score -> remediate -> rank   (same brain as version 1)
#   2. persist findings + history to SQLite (v2.db)
#   3. file GitHub Issues for findings >= ticket threshold (optional)
#
# Env overrides:
#   REPORTS_DIR   directory with <product>_<scanner>.json  (default ../sample_reports)
#   OUT_DIR       pipeline outputs                          (default ../outputs/v2)
#   CONFIG        config.json path                          (default ./config.json)
#   PRODUCTS      comma-separated subset, e.g. "juice_shop"
#   GH_REPO       GitHub "owner/name" (required for --github-tickets)
#   GH_TOKEN      GitHub token (required for --github-tickets)
#   TICKETS=file|github|both|none   (default file)
#   SKIP_ENRICH=1 offline run (skip live threat-intel lookups)
# ============================================================================
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

REPORTS_DIR="${REPORTS_DIR:-$ROOT_DIR/sample_reports}"
OUT_DIR="${OUT_DIR:-$ROOT_DIR/outputs/v2}"
CONFIG="${CONFIG:-$SCRIPT_DIR/config.json}"
PRODUCTS="${PRODUCTS:-}"
TICKETS="${TICKETS:-file}"
SKIP_ENRICH="${SKIP_ENRICH:-0}"
GH_REPO="${GH_REPO:-}"
GH_TOKEN="${GH_TOKEN:-}"

echo "== [v2] risk pipeline (custom substrate) =="
echo "   reports : $REPORTS_DIR"
echo "   out     : $OUT_DIR"
echo "   config  : $CONFIG"

ARGS=(--reports "$REPORTS_DIR" --config "$CONFIG" --out "$OUT_DIR" --file-tickets)
[ -n "$PRODUCTS" ] && ARGS+=(--products "$PRODUCTS")
[ "$SKIP_ENRICH" = "1" ] && ARGS+=(--skip-enrich)

case "$TICKETS" in
  github|both)
    if [ -z "$GH_REPO" ] || [ -z "$GH_TOKEN" ]; then
        echo "ERROR: TICKETS=$TICKETS requires GH_REPO and GH_TOKEN" >&2
        exit 1
    fi
    ARGS+=(--github-tickets --github-repo "$GH_REPO" --github-token "$GH_TOKEN")
    ;;
esac

cd "$SCRIPT_DIR"
python run_pipeline.py "${ARGS[@]}"

echo
echo "== [v2] done. Dashboard: $OUT_DIR/risk_dashboard.html =="
