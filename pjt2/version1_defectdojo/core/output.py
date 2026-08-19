"""Output writers: ranked dataset (CSV/JSON), noise-reduction metrics,
ticket-ready markdown, and an executive summary."""
from __future__ import annotations

import csv
import json
import os
from typing import Any, Dict, List

from .models import Finding, RunSummary

CSV_COLUMNS = [
    "rank", "score", "priority", "sla_hours", "owner", "product", "scanner",
    "title", "severity", "cve", "cwe", "endpoint", "parameter",
    "epss_score", "epss_percentile", "epss_trend", "kev", "kev_date",
    "exploit_available", "exploit_source", "escalation_potential",
    "package", "fixed_version", "description", "remediation_summary",
]


def write_ranked_csv(path: str, ranked: List[Finding]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for f in ranked:
            row = f.to_row()
            row["rank"] = f.score_breakdown.get("rank", "")
            writer.writerow({c: row.get(c, "") for c in CSV_COLUMNS})


def write_ranked_json(path: str, ranked: List[Finding]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump([f.to_dict() for f in ranked], fh, indent=2)


def write_metrics_json(path: str, metrics: Dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(metrics, fh, indent=2)


def write_top_actions_md(path: str, ranked: List[Finding], summary: RunSummary) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    lines = [
        "# Top Action List — Risk Prioritized Findings",
        "",
        f"Run: {summary.run_date}  ·  Products: {', '.join(summary.products)}",
        "",
        f"Raw findings: **{summary.raw_findings}** → unique: **{summary.unique_findings}** "
        f"→ after filtering: **{summary.final_findings}** (dedup **{summary.dedup_pct}%**)",
        "",
        "| Rank | Score | Pri | SLA | Owner | Product | Title | CVE | CWE | Endpoint |",
        "|-----:|------:|-----|----:|-------|---------|-------|-----|-----|----------|",
    ]
    for f in ranked:
        lines.append(
            f"| {f.score_breakdown.get('rank', '')} | {f.score} | {f.priority} | "
            f"{f.sla_hours}h | {f.owner} | {f.product} | {f.title[:60]} | "
            f"{f.cve or ''} | {f.cwe or ''} | {f.endpoint or ''} |")
    lines += ["", "## Score breakdown (top 10)", ""]
    for f in ranked[:10]:
        sb = f.score_breakdown.get("components", {})
        lines.append(f"**#{f.score_breakdown.get('rank')} · {f.score} — {f.title[:70]}**")
        lines.append(f"- {', '.join(f'{k}={v}' for k, v in sb.items())}")
        lines.append(f"- Drivers: {', '.join(f.score_breakdown.get('drivers', [])) or 'none'}")
        lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def write_tickets_md(path: str, ranked: List[Finding], threshold: float) -> None:
    """Ticket-ready markdown for findings above the auto-ticket threshold."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    tickets = [f for f in ranked if (f.score or 0) >= threshold]
    lines = [
        "# Tickets Ready (auto-file candidates)",
        "",
        f"{len(tickets)} findings meet the auto-ticket threshold (score ≥ {threshold}).",
        "",
    ]
    for i, f in enumerate(tickets, start=1):
        lines += [
            f"## Ticket {i}: [{f.priority}] {f.title}",
            "",
            f"- **Score:** {f.score} / 100  ·  **Owner:** {f.owner}  ·  **SLA:** {f.sla_hours}h",
            f"- **Product:** {f.product}  ·  **Scanner:** {f.scanner}",
            f"- **CVE:** {f.cve or '-'}  ·  **CWE:** {f.cwe or '-'}",
            f"- **Endpoint:** {f.endpoint or '-'}{f'  (param: {f.parameter})' if f.parameter else ''}",
            f"- **Severity:** {f.severity}  ·  **EPSS:** {f.epss_score or '-'} "
            f"(pct {f.epss_percentile or '-'})  ·  **KEV:** {'yes ' + str(f.kev_date) if f.kev else 'no'}",
            f"- **Escalation potential:** {f.escalation_potential or 0.0}",
            "",
            "**Score breakdown:** " + ", ".join(
                f"{k}={v}" for k, v in f.score_breakdown.get("components", {}).items()),
            "",
            "**Remediation:**",
        ]
        for s in f.remediation_suggestions:
            lines.append(f"- *{s['kind']}:* {s['text']}")
        lines.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
