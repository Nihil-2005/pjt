"""End-to-end pipeline orchestration.

Stages (mapped to the activity's solution approach):

  1. INGEST & NORMALIZE  parse_reports_dir -> unified Finding schema
  2. DEDUPLICATION       cross-scanner dedup (CVE / endpoint+CWE / title)
  3. FILTERING           auditable quarantine (severity / FP / risk-accept)
  4. ENRICHMENT          CISA KEV, FIRST.org EPSS (+trend), NVD, exploit-db
  5. ATTACK PATH MAPPING CAPEC-inspired CWE chains + escalation probability
  6. RISK SCORING        8-factor 0-100 contextual score (explainable)
  7. REMEDIATION         first-aid + full remediation + scanner guidance
  8. RANKING & OUTPUT    top action list, CSV/JSON/markdown, dashboard

Both version1_defectdojo and version2_custom import this same core.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
from typing import Any, Dict, List, Optional

from . import attackpath, dashboard, dedup, enrich, filter as filt, history, normalize, output, rank as rank_mod, remediation, score as score_mod
from .config import Config
from .models import Finding, RunSummary


def run(reports_dir: str, config: Config, out_dir: str,
        products: Optional[List[str]] = None,
        skip_enrich: bool = False,
        use_searchsploit: Optional[bool] = None,
        fetcher: Optional[enrich.Fetcher] = None) -> Dict[str, Any]:
    """Run the full pipeline and write all outputs under ``out_dir``.

    Returns a dict with findings, ranked, summary, attack_paths, metrics.
    """
    os.makedirs(out_dir, exist_ok=True)
    run_date = dt.datetime.now().isoformat(timespec="seconds")
    products = products or config.product_names()

    # ---- Stage 1: ingest & normalize ------------------------------------
    print("== [1/8] INGEST & NORMALIZE ==")
    findings = normalize.parse_reports_dir(reports_dir, products)
    print(f"  parsed {len(findings)} raw findings from {reports_dir}")

    # ---- Stage 2: deduplication ------------------------------------------
    print("== [2/8] DEDUPLICATION ==")
    dedup_result = dedup.deduplicate(findings, fuzzy=config.dedup_cfg.get("fuzzy_title", False))
    findings = dedup_result["findings"]
    dedup_metrics = dedup_result["metrics"]
    print(f"  raw={dedup_metrics['raw']} unique={dedup_metrics['unique']} "
          f"dedup%={dedup_metrics['dedup_pct']}")

    # ---- Stage 3: filtering (auditable quarantine) ------------------------
    print("== [3/8] FILTERING (auditable) ==")
    uniques = [f for f in findings if not f.is_duplicate]
    filter_result = filt.filter_findings(uniques, config.filter_cfg, config.products)
    findings = filter_result["findings"]
    filter_metrics = filter_result["metrics"]
    print(f"  active={filter_metrics['active']} quarantined={filter_metrics['quarantined']}")

    # ---- Stage 4: enrichment ----------------------------------------------
    print("== [4/8] ENRICHMENT (KEV / EPSS / NVD / exploit-db) ==")
    enricher = enrich.Enricher(config.enrich_cfg, fetcher=fetcher)
    if not skip_enrich:
        enricher.enrich(findings, use_searchsploit=use_searchsploit)
        print(f"  enriched: {enricher.counts_dict()}")

    # ---- Stage 5: attack path mapping --------------------------------------
    print("== [5/8] ATTACK PATH MAPPING ==")
    all_paths: Dict[str, List[Any]] = {}
    for product in products:
        if not any(f.product == product for f in findings):
            continue
        paths = attackpath.build_attack_paths(findings, product, config.product(product))
        all_paths[product] = [p.to_dict() for p in paths]
        attackpath.attach_escalation_potential(findings, paths)
    total_paths = sum(len(v) for v in all_paths.values())
    print(f"  {total_paths} attack paths across {len(all_paths)} products")

    # ---- Stage 6: risk scoring ---------------------------------------------
    print("== [6/8] RISK SCORING (8-factor, explainable) ==")
    for f in findings:
        if f.status == "active":
            score_mod.compute_score(f, config.product(f.product), config.weights)

    # ---- Stage 7: remediation ----------------------------------------------
    print("== [7/8] REMEDIATION SUGGESTIONS ==")
    for f in findings:
        if f.status == "active":
            f.remediation_suggestions = remediation.suggest_remediation(f)

    # ---- Stage 8: ranking + outputs ----------------------------------------
    print("== [8/8] RANKING & OUTPUT ==")
    ranked = rank_mod.rank_findings(findings, config)

    active = [f for f in findings if f.status == "active"]
    scores = [f.score or 0 for f in active]
    summary = RunSummary(
        run_date=run_date,
        products=[p for p in products if any(f.product == p for f in findings)],
        raw_findings=dedup_metrics["raw"],
        unique_findings=dedup_metrics["unique"],
        quarantined=filter_metrics["quarantined"],
        final_findings=filter_metrics["active"],
        dedup_pct=dedup_metrics["dedup_pct"],
        avg_score=round(sum(scores) / len(scores), 1) if scores else 0.0,
        top_score=max(scores) if scores else 0.0,
        p1=sum(1 for f in active if f.priority == "P1"),
        p2=sum(1 for f in active if f.priority == "P2"),
        p3=sum(1 for f in active if f.priority == "P3"),
        p4=sum(1 for f in active if f.priority == "P4"),
        enrich_counts=enricher.counts_dict() if not skip_enrich else {},
        quarantine_by_rule=filter_metrics.get("quarantine_by_rule", {}),
        attack_paths=total_paths,
    )

    output.write_ranked_csv(os.path.join(out_dir, "ranked_findings.csv"), ranked)
    output.write_ranked_json(os.path.join(out_dir, "ranked_findings.json"), ranked)
    output.write_top_actions_md(os.path.join(out_dir, "top_actions.md"), ranked, summary)
    output.write_tickets_md(os.path.join(out_dir, "tickets_ready.md"), ranked,
                            config.reporting.get("ticket_threshold", 60))

    noise = {
        "run_date": run_date,
        "raw_findings": summary.raw_findings,
        "unique_findings": summary.unique_findings,
        "quarantined": summary.quarantined,
        "final_findings": summary.final_findings,
        "dedup_pct": summary.dedup_pct,
        "noise_removed_pct": round(
            (summary.raw_findings - summary.final_findings) / max(summary.raw_findings, 1) * 100, 2),
        "dedup_by_pass": dedup_metrics["by_pass"],
        "quarantine_by_rule": summary.quarantine_by_rule,
        "enrich_counts": summary.enrich_counts,
        "attack_paths": total_paths,
        "avg_score": summary.avg_score,
        "top_score": summary.top_score,
        "p1_p2": summary.p1 + summary.p2,
    }
    output.write_metrics_json(os.path.join(out_dir, "noise_reduction.json"), noise)

    # history (risk reduction over time)
    hist = history.History(os.path.join(out_dir, "history.db"))
    for product in summary.products:
        pf = [f for f in active if f.product == product]
        pscores = [f.score or 0 for f in pf]
        hist.add_run(run_date[:10], product, {
            "raw": summary.raw_findings,
            "unique": summary.unique_findings,
            "quarantined": summary.quarantined,
            "final": len(pf),
            "dedup_pct": summary.dedup_pct,
            "avg_score": round(sum(pscores) / len(pscores), 1) if pscores else 0.0,
            "top_score": max(pscores) if pscores else 0.0,
            "p1": sum(1 for f in pf if f.priority == "P1"),
            "p2": sum(1 for f in pf if f.priority == "P2"),
            "p3": sum(1 for f in pf if f.priority == "P3"),
            "p4": sum(1 for f in pf if f.priority == "P4"),
            "enrich_counts": summary.enrich_counts,
        })
    history_map = hist.all_history()
    hist.close()

    quarantine_list = [f for f in findings if f.status == "quarantined"]
    dashboard.build_dashboard(os.path.join(out_dir, "risk_dashboard.html"), findings,
                              ranked, summary, all_paths, history_map, quarantine_list)

    print("\n[OK] pipeline complete - outputs in", out_dir)
    print(f"   ranked_findings.csv/json · top_actions.md · tickets_ready.md · "
          f"noise_reduction.json · risk_dashboard.html · history.db")

    return {
        "findings": findings,
        "ranked": ranked,
        "summary": summary,
        "attack_paths": all_paths,
        "metrics": noise,
    }


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="Risk Prioritization & Deduplication pipeline (shared core)")
    parser.add_argument("--reports", required=True, help="directory with <product>_<scanner>.json reports")
    parser.add_argument("--config", default=None, help="path to config.json")
    parser.add_argument("--out", default="out", help="output directory")
    parser.add_argument("--products", default=None, help="comma-separated product filter")
    parser.add_argument("--skip-enrich", action="store_true", help="skip live threat-intel lookups")
    parser.add_argument("--searchsploit", action="store_true", help="use exploitdb docker image for exploit lookups")
    args = parser.parse_args(argv)

    config = Config.load(args.config)
    products = args.products.split(",") if args.products else None
    run(args.reports, config, args.out, products=products,
        skip_enrich=args.skip_enrich, use_searchsploit=True if args.searchsploit else None)


if __name__ == "__main__":
    main()
