#!/usr/bin/env bash
# ============================================================================
# pipeline.sh (version 1) — DevSecOps CI/CD: scanners -> risk pipeline ->
# DefectDojo dashboard.
#
# Stages:
#   0. [optional] run ../scans/scan.sh to produce fresh reports
#   1. shared core: normalize -> dedup -> filter -> enrich -> attack paths
#      -> score -> remediate -> rank   (same brain as version 2)
#   2. push deduplicated + enriched findings into DefectDojo via REST API
#
# Env overrides:
#   REPORTS_DIR   directory with <product>_<scanner>.json   (default ../sample_reports)
#   OUT_DIR       pipeline outputs                           (default ../outputs/v1)
#   CONFIG        config.json path                           (default ./config.json)
#   PRODUCTS      comma-separated subset, e.g. "juice_shop"
#   DD_BASE_URL   DefectDojo API base                        (default http://localhost:8080)
#   DD_API_TOKEN  DefectDojo API token                       (required to push)
#   PUSH_DD=1     push to DefectDojo after the pipeline      (default 0)
#   SKIP_ENRICH=1 offline run (skip live threat-intel lookups)
# ============================================================================
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

REPORTS_DIR="${REPORTS_DIR:-$ROOT_DIR/sample_reports}"
OUT_DIR="${OUT_DIR:-$ROOT_DIR/outputs/v1}"
CONFIG="${CONFIG:-$SCRIPT_DIR/config.json}"
PRODUCTS="${PRODUCTS:-}"
PUSH_DD="${PUSH_DD:-0}"
SKIP_ENRICH="${SKIP_ENRICH:-0}"
DD_BASE_URL="${DD_BASE_URL:-http://localhost:8080}"
DD_API_TOKEN="${DD_API_TOKEN:-}"

echo "== [v1] risk pipeline (DefectDojo substrate) =="
echo "   reports : $REPORTS_DIR"
echo "   out     : $OUT_DIR"
echo "   config  : $CONFIG"

ARGS=(--reports "$REPORTS_DIR" --config "$CONFIG" --out "$OUT_DIR")
[ -n "$PRODUCTS" ] && ARGS+=(--products "$PRODUCTS")
[ "$SKIP_ENRICH" = "1" ] && ARGS+=(--skip-enrich)
if [ "$PUSH_DD" = "1" ]; then
    if [ -z "$DD_API_TOKEN" ]; then
        echo "ERROR: PUSH_DD=1 requires DD_API_TOKEN" >&2
        exit 1
    fi
    ARGS+=(--push-defectdojo --dd-base-url "$DD_BASE_URL" --dd-token "$DD_API_TOKEN")
fi

cd "$SCRIPT_DIR"
python run_pipeline.py "${ARGS[@]}"

echo
echo "== [v1] done. Open DefectDojo ($DD_BASE_URL) for the dashboard. =="
