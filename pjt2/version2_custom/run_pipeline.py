"""Version 2 pipeline: shared core + fully custom substrate.

The same 8-stage brain as version 1, but the substrate is 100% ours:

  - SQLite database stores every run's findings + history (risk reduction
    over time) — no DefectDojo,
  - auto-ticketing files GitHub Issues for P1/P2 findings,
  - the dashboard is the standalone HTML/SVG report from the shared core.

Usage:
    python run_pipeline.py --reports ../sample_reports --config config.json \
        --out ../outputs/v2 [--file-tickets] [--github-tickets]
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import sys
from typing import List, Optional

# resolve the vendored `core/` shipped inside this version folder (folder is self-contained)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import Config  # noqa: E402
from core.pipeline import run as run_core  # noqa: E402
from core.models import Finding  # noqa: E402

from github_issues import GitHubIssues, write_tickets_md  # noqa: E402
from storage import Storage  # noqa: E402


def persist(db_path: str, run_date: str, result: dict, config: Config) -> dict:
    """Write findings + run history into SQLite. Returns the DB summary."""
    storage = Storage(db_path)
    findings = result["findings"]
    summary = result["summary"]
    active = [f for f in findings if f.status == "active"]
    by_product: dict = {}
    for f in active:
        by_product.setdefault(f.product, []).append(f)
    for product, pf in by_product.items():
        scores = [f.score or 0 for f in pf]
        storage.save_run(run_date[:10], product, {
            "raw": summary.raw_findings,
            "unique": summary.unique_findings,
            "quarantined": summary.quarantined,
            "final": len(pf),
            "dedup_pct": summary.dedup_pct,
            "avg_score": round(sum(scores) / len(scores), 1) if scores else 0.0,
            "top_score": max(scores) if scores else 0.0,
            "p1": sum(1 for f in pf if f.priority == "P1"),
            "p2": sum(1 for f in pf if f.priority == "P2"),
            "p3": sum(1 for f in pf if f.priority == "P3"),
            "p4": sum(1 for f in pf if f.priority == "P4"),
        })
    storage.save_findings(run_date, findings)
    db_summary = storage.summary()
    storage.close()
    return db_summary


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Version 2: custom risk pipeline")
    parser.add_argument("--reports", required=True, help="dir with <product>_<scanner>.json")
    parser.add_argument("--config", default=None, help="config.json path")
    parser.add_argument("--out", default="outputs/v2", help="output dir")
    parser.add_argument("--products", default=None, help="comma-separated product filter")
    parser.add_argument("--skip-enrich", action="store_true", help="skip live threat-intel lookups")
    parser.add_argument("--db", default=None, help="SQLite db path (default <out>/v2.db)")
    parser.add_argument("--file-tickets", action="store_true",
                        help="write tickets_ready.md for findings >= threshold")
    parser.add_argument("--github-tickets", action="store_true",
                        help="file GitHub Issues for findings >= threshold")
    parser.add_argument("--github-repo", default=None, help="owner/name (or env GH_REPO)")
    parser.add_argument("--github-token", default=None, help="or env GH_TOKEN")
    parser.add_argument("--dry-run", action="store_true", help="don't call the GitHub API")
    args = parser.parse_args(argv)

    config = Config.load(args.config)
    products = args.products.split(",") if args.products else None
    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    result = run_core(args.reports, config, out_dir, products=products,
                      skip_enrich=args.skip_enrich)
    ranked = result["ranked"]
    run_date = dt.datetime.now().isoformat(timespec="seconds")

    # 1) SQLite persistence (our custom database)
    db_path = args.db or os.path.join(out_dir, "v2.db")
    db_summary = persist(db_path, run_date, result, config)
    print(f"  [v2-db] stored run in {db_path}: {db_summary}")

    # 2) ticket file (offline artifact)
    threshold = config.reporting.get("ticket_threshold", 60)
    if args.file_tickets:
        n = write_tickets_md(ranked, os.path.join(out_dir, "tickets_ready.md"), threshold)
        print(f"  [v2-tickets] {n} ticket-ready finding(s) written to tickets_ready.md")

    # 3) GitHub Issues (real ticketing)
    if args.github_tickets:
        repo = args.github_repo or os.environ.get("GH_REPO", "")
        token = args.github_token or os.environ.get("GH_TOKEN", "")
        gh = GitHubIssues(repo, token, dry_run=args.dry_run)
        stats = gh.file_issues(ranked, threshold=threshold, label="security")
        print(f"  [v2-github] {stats}")
        if stats.get("errors") and not args.dry_run:
            sys.exit(2)

    print("\n[OK] v2 pipeline complete - outputs in", out_dir)
    print("   ranked_findings.csv/json · top_actions.md · tickets_ready.md ·")
    print("   noise_reduction.json · risk_dashboard.html · history.db · v2.db")


if __name__ == "__main__":
    main()
