"""Version 1 pipeline: shared core + DefectDojo substrate.

Runs the same 8-stage brain as version 2 (normalize -> dedup -> filter ->
enrich -> attack paths -> score -> remediation -> rank), then *pushes the
deduplicated, enriched results into DefectDojo* (your dashboard / history /
reporting layer) over its REST API.

Usage:
    python run_pipeline.py --reports ../sample_reports --config config.json \
        --out ../outputs/v1 --push-defectdojo
"""
from __future__ import annotations

import argparse
import os
import sys
from typing import List, Optional

# resolve the vendored `core/` shipped inside this version folder (folder is self-contained)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import Config  # noqa: E402
from core.pipeline import run as run_core  # noqa: E402
from core.models import Finding  # noqa: E402

from defectdojo_client import DefectDojoClient, DefectDojoError  # noqa: E402
from import_payloads import finding_to_payload, build_engagement_summary, dump_payloads  # noqa: E402


def push_to_defectdojo(ranked: List[Finding], config: Config,
                       engagement_name: Optional[str] = None,
                       base_url: Optional[str] = None,
                       api_token: Optional[str] = None) -> dict:
    """Push every active finding into DefectDojo. Returns push stats."""
    client = DefectDojoClient(base_url=base_url, api_token=api_token)
    stats = {"products": 0, "findings": 0, "skipped": 0, "errors": []}
    run_id = os.environ.get("GITHUB_RUN_ID") or "local"

    for product in config.product_names():
        pf = [f for f in ranked if f.product == product and f.status == "active"]
        if not pf:
            continue
        prod = client.upsert_product(
            product,
            description=config.product(product).get("display_name", product),
        )
        stats["products"] += 1
        eng_name = engagement_name or f"risk-pipeline-{run_id}-{product}"
        eng = client.upsert_engagement(prod["id"], eng_name,
                                       description=build_engagement_summary(pf))
        test = client.upsert_test(eng["id"], "Manual Finding")
        for f in pf:
            try:
                payload = finding_to_payload(f, config.product(product).get("display_name", ""))
                client.push_finding(test["id"], payload, product_id=prod["id"])
                stats["findings"] += 1
            except DefectDojoError as exc:
                stats["errors"].append(f"{f.title[:50]}: {exc}")
                stats["skipped"] += 1
    return stats


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Version 1: risk pipeline + DefectDojo")
    parser.add_argument("--reports", required=True, help="dir with <product>_<scanner>.json")
    parser.add_argument("--config", default=None, help="config.json path")
    parser.add_argument("--out", default="outputs/v1", help="output dir (also holds payloads)")
    parser.add_argument("--products", default=None, help="comma-separated product filter")
    parser.add_argument("--skip-enrich", action="store_true", help="skip live threat-intel lookups")
    parser.add_argument("--push-defectdojo", action="store_true",
                        help="push results into DefectDojo (v1 substrate)")
    parser.add_argument("--dd-base-url", default=None, help="overrides DD_BASE_URL")
    parser.add_argument("--dd-token", default=None, help="overrides DD_API_TOKEN")
    parser.add_argument("--engagement-name", default=None, help="DefectDojo engagement name")
    args = parser.parse_args(argv)

    config = Config.load(args.config)
    products = args.products.split(",") if args.products else None

    result = run_core(args.reports, config, args.out, products=products,
                      skip_enrich=args.skip_enrich)
    ranked = result["ranked"]

    # always write the DefectDojo import payloads as an auditable artifact
    payload_path = os.path.join(args.out, "defectdojo_payloads.json")
    dump_payloads(ranked, payload_path)
    print(f"  wrote DefectDojo payloads -> {payload_path}")

    if args.push_defectdojo:
        stats = push_to_defectdojo(ranked, config,
                                   engagement_name=args.engagement_name,
                                   base_url=args.dd_base_url, api_token=args.dd_token)
        print(f"  [DefectDojo] pushed {stats['findings']} findings across "
              f"{stats['products']} products; errors={len(stats['errors'])}")
        for err in stats["errors"][:5]:
            print(f"    ! {err}")
        if stats["errors"]:
            sys.exit(2)
    else:
        print("  (not pushing to DefectDojo; pass --push-defectdojo to import)")


if __name__ == "__main__":
    main()
