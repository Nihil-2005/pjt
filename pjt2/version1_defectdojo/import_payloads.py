"""Map shared-core findings into DefectDojo finding payloads.

Each payload carries the full evidence trail so DefectDojo (the v1
dashboard) shows *why* a finding is ranked the way it is:

  - the 0-100 contextual score + breakdown,
  - threat intel (KEV date, EPSS score/percentile, exploit source),
  - remediation: first-aid + full suggestions,
  - SLA band + owner (ticket-ready),
  - the scanner provenance list (which scanners reported it).
"""
from __future__ import annotations

import datetime as dt
import json
from typing import Any, Dict, List

from core.models import Finding


def finding_to_payload(f: Finding, product_display: str = "") -> Dict[str, Any]:
    sev = f.severity
    desc_parts: List[str] = [
        f"**Risk score: {f.score:.1f}/100**  (priority {f.priority}, "
        f"SLA {f.sla_hours}h, owner {f.owner})",
        "",
        "### Score breakdown",
        _score_table(f),
        "",
        "### Threat intelligence",
        *_threat_intel_lines(f),
        "",
        "### Attack-path context",
        *_attack_path_lines(f),
        "",
        "### Evidence",
        f"Scanners: {_scanners(f)}",
        f"Endpoint: {f.endpoint or '-'}",
        f"Parameter: {f.parameter or '-'}",
        f"Package: {f.package or '-'} {f.installed_version or ''}"
        f"{' -> ' + f.fixed_version if f.fixed_version else ''}",
        "",
        f"### Scanner description\n{f.description or 'n/a'}",
        "",
        "### Remediation",
        _remediation_lines(f),
    ]
    return {
        "title": f"[{f.priority}] {f.title} ({product_display or f.product})",
        "severity": sev,
        "description": "\n".join(desc_parts),
        "mitigation": _remediation_lines(f),
        "references": f.raw.get("reference") or f.exploit_source or "",
        "cwe": _cwe_id(f.cwe),
        "cve": f.cve,
        "cvssv3": f.effective_cvss,
        "epss_score": f.epss_score,
        "epss_percentile": f.epss_percentile,
        "known_exploited": f.kev,
        "kev_date": f.kev_date,
        "active": True,
        "verified": True,
        "endpoint": f.endpoint,
        "impact": f"Exploitation likelihood: EPSS {f.epss_score or 0:.4f} "
                  f"(pct {f.epss_percentile or 0:.3f}); "
                  f"KEV: {'yes' if f.kev else 'no'}; "
                  f"escalation potential: {f.escalation_potential or 0.0:.2f}",
        "sla_hours": f.sla_hours,
        "owner": f.owner,
    }


def _score_table(f: Finding) -> str:
    comps = (f.score_breakdown or {}).get("components", {})
    rows = "\n".join(f"| {k} | {v} |" for k, v in sorted(comps.items()))
    return f"| factor | points |\n|---|---|\n{rows}"


def _threat_intel_lines(f: Finding) -> List[str]:
    lines = [
        f"- CVE: {f.cve or '-'}  (CWE: {f.cwe or '-'})",
        f"- EPSS: {f.epss_score or 0:.4f}  percentile {f.epss_percentile or 0:.3f}"
        f"  trend {f.epss_trend or 0:+.4f}/7d",
        f"- CISA KEV: {'yes (' + (f.kev_date or '') + ')' if f.kev else 'no'}",
        f"- Public exploit: {'yes (' + (f.exploit_source or '?') + ')' if f.exploit_available else 'no'}",
    ]
    return lines


def _attack_path_lines(f: Finding) -> List[str]:
    if f.escalation_potential:
        return [f"- Escalation potential: {f.escalation_potential:.2f} "
                f"(max chain probability originating at {f.cwe})"]
    return ["- No chainable CAPEC path from this finding's CWE."]


def _scanners(f: Finding) -> str:
    prov = f.raw.get("scanners") if isinstance(f.raw, dict) else None
    if prov:
        return ", ".join(prov)
    return f.scanner


def _remediation_lines(f: Finding) -> str:
    suggestions = f.remediation_suggestions or []
    lines = [f"- [{s.get('kind')}] {s.get('text', '')}" for s in suggestions]
    if f.remediation and f.remediation not in lines:
        lines.append(f"- [scanner] {f.remediation}")
    return "\n".join(lines) or "No remediation guidance provided."


def _cwe_id(cwe: str) -> int | None:
    if not cwe:
        return None
    digits = "".join(ch for ch in str(cwe) if ch.isdigit())
    return int(digits) if digits else None


def build_engagement_summary(findings: List[Finding]) -> str:
    """Markdown block appended to the DefectDojo engagement description."""
    from core.models import RunSummary  # noqa: F401  (kept simple below)
    active = [f for f in findings if f.status == "active"]
    p1 = sum(1 for f in active if f.priority == "P1")
    p2 = sum(1 for f in active if f.priority == "P2")
    return (
        f"Run {dt.datetime.now().isoformat(timespec='seconds')}: "
        f"{len(active)} active findings "
        f"(P1={p1}, P2={p2}, avg score "
        f"{sum((f.score or 0) for f in active) / max(len(active), 1):.1f}). "
        f"Full ranked list in the test's findings."
    )


def dump_payloads(findings: List[Finding], path: str) -> None:
    """Write the import payloads to disk (debug/audit artifact)."""
    with open(path, "w", encoding="utf-8") as fh:
        json.dump([finding_to_payload(f) for f in findings], fh, indent=2)
