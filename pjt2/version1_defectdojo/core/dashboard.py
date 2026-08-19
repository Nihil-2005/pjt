"""Self-contained HTML risk dashboard.

Everything is inline (CSS + SVG generated in Python) so the dashboard works
offline / from file:// — no CDN dependencies.  Sections:

  - summary cards (raw / unique / quarantined / final, dedup %, score stats)
  - before/after bar chart (noise reduction)
  - attack-path graph (SVG, per product)
  - risk-reduction-over-time line chart (from the run history)
  - ranked findings table with expandable score breakdown + remediation
  - quarantine log (proves nothing was silently dropped)
"""
from __future__ import annotations

import html
import os
from typing import Any, Dict, List

from .models import Finding, RunSummary

_SEV_COLORS = {"critical": "#d32f2f", "high": "#f57c00", "medium": "#fbc02d",
               "low": "#7cb342", "info": "#90a4ae"}


def _esc(v: Any) -> str:
    return html.escape("" if v is None else str(v))


# ---------------------------------------------------------------------------
# SVG helpers
# ---------------------------------------------------------------------------
def svg_before_after(raw: int, unique: int, final: int, quarantined: int) -> str:
    width, height = 460, 190
    bars = [("Raw findings", raw, "#546e7a"),
            ("After dedup", unique, "#1976d2"),
            ("After filter", final, "#388e3c"),
            ("Quarantined", quarantined, "#e64a19")]
    maxv = max(raw, unique, final, quarantined, 1)
    bw, gap, x0, y0 = 80, 24, 30, 150
    parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    for i, (label, val, color) in enumerate(bars):
        h = max(6, int(val / maxv * 120))
        x = x0 + i * (bw + gap)
        parts.append(f'<rect x="{x}" y="{y0 - h}" width="{bw}" height="{h}" '
                     f'fill="{color}" rx="4"><title>{label}: {val}</title></rect>')
        parts.append(f'<text x="{x + bw / 2}" y="{y0 - h - 6}" text-anchor="middle" '
                     f'font-size="13" font-weight="bold" fill="#333">{val}</text>')
        parts.append(f'<text x="{x + bw / 2}" y="{y0 + 18}" text-anchor="middle" '
                     f'font-size="11" fill="#555">{label}</text>')
    parts.append(f'<text x="{x0}" y="{y0 + 40}" font-size="10" fill="#888">'
                 f'dedup+filter removed {max(0, raw - final)} of {raw} raw alerts '
                 f'({round((raw - final) / max(raw, 1) * 100)}%)</text>')
    parts.append("</svg>")
    return "".join(parts)


def svg_attack_path(paths: List[Dict[str, Any]], product: str) -> str:
    if not paths:
        return '<p style="color:#888">No attack paths — no chainable CWE pairs found on this product.</p>'
    nodes: Dict[str, int] = {}
    for p in paths:
        nodes.setdefault(p["from_cwe"], 0)
        nodes.setdefault(p["to_cwe"], 0)
    n = len(nodes)
    width, height = 620, max(220, n * 56 + 60)
    x_from, x_to = 120, 480
    ys = {cwe: 50 + i * 56 for i, cwe in enumerate(sorted(nodes))}

    parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append(f'<text x="{10}" y="{16}" font-size="12" fill="#666">Attack paths — {_esc(product)} '
                 f'(CAPEC-inspired CWE chains, escalation probability)</text>')
    # edges
    for p in paths:
        y1, y2 = ys[p["from_cwe"]], ys[p["to_cwe"]]
        mid = (y1 + y2) / 2
        col = "#c62828" if p["probability"] >= 0.6 else ("#ef6c00" if p["probability"] >= 0.4 else "#7cb342")
        parts.append(f'<path d="M {x_from} {y1} C {(x_from + x_to) / 2} {y1}, '
                     f'{(x_from + x_to) / 2} {y2}, {x_to} {y2}" fill="none" '
                     f'stroke="{col}" stroke-width="2" opacity="0.75" '
                     f'stroke-dasharray="6 3"><title>{_esc(p["description"])} '
                     f'-> {p["probability"]}</title></path>')
        parts.append(f'<text x="{(x_from + x_to) / 2}" y="{mid - 4}" text-anchor="middle" '
                     f'font-size="10" fill="{col}">p={p["probability"]}</text>')
    # nodes
    for cwe, y in ys.items():
        impact = cwe in ("CWE-94", "CWE-78", "CWE-434", "CWE-502", "CWE-89", "CWE-918")
        fill = "#b71c1c" if impact else "#1565c0"
        parts.append(f'<rect x="{x_from - 96}" y="{y - 16}" width="92" height="32" rx="16" '
                     f'fill="{fill}"><title>{_esc(cwe)}</title></rect>')
        parts.append(f'<text x="{x_from - 50}" y="{y + 4}" text-anchor="middle" font-size="11" '
                     f'fill="#fff" font-weight="bold">{_esc(cwe)}</text>')
        parts.append(f'<rect x="{x_to}" y="{y - 16}" width="92" height="32" rx="16" '
                     f'fill="{fill}"><title>{_esc(cwe)}</title></rect>')
        parts.append(f'<text x="{x_to + 46}" y="{y + 4}" text-anchor="middle" font-size="11" '
                     f'fill="#fff" font-weight="bold">{_esc(cwe)}</text>')
    parts.append(f'<text x="{x_from - 96}" y="{height - 8}" font-size="10" fill="#888">'
                 f'red = high-impact escalation target</text>')
    parts.append("</svg>")
    return "".join(parts)


def svg_risk_over_time(history: List[Dict[str, Any]]) -> str:
    if len(history) < 2:
        return '<p style="color:#888">Need 2+ runs to plot risk reduction over time.</p>'
    width, height, pad_l, pad_b = 620, 200, 46, 30
    dates = [h["run_date"][:16] for h in history]
    scores = [h["avg_score"] or 0 for h in history]
    finals = [h["final"] or 0 for h in history]
    maxv = max(max(scores), max(finals), 1)
    step = (width - pad_l - 20) / max(len(history) - 1, 1)
    parts = [f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">']

    def pts(vals, yscale):
        return " ".join(
            f"{pad_l + i * step},{height - pad_b - (v / maxv) * yscale}"
            for i, v in enumerate(vals))

    parts.append(f'<polyline points="{pts(scores, 120)}" fill="none" stroke="#d32f2f" '
                 f'stroke-width="2.5"><title>avg score</title></polyline>')
    parts.append(f'<polyline points="{pts(finals, 120)}" fill="none" stroke="#1976d2" '
                 f'stroke-width="2.5"><title>final findings</title></polyline>')
    for i, d in enumerate(dates):
        parts.append(f'<text x="{pad_l + i * step}" y="{height - pad_b + 16}" text-anchor="middle" '
                     f'font-size="9" fill="#777">{_esc(d)}</text>')
    for i, s in enumerate(scores):
        parts.append(f'<circle cx="{pad_l + i * step}" cy="{height - pad_b - (s / maxv) * 120}" '
                     f'r="3" fill="#d32f2f"/>')
    parts.append(f'<text x="{pad_l}" y="{14}" font-size="11" fill="#d32f2f">avg risk score</text>')
    parts.append(f'<text x="{pad_l + 110}" y="{14}" font-size="11" fill="#1976d2">final findings</text>')
    parts.append("</svg>")
    return "".join(parts)


# ---------------------------------------------------------------------------
# Main dashboard
# ---------------------------------------------------------------------------
def _finding_row(f: Finding) -> str:
    sb = f.score_breakdown.get("components", {})
    comps = ", ".join(f"{k}={v}" for k, v in sb.items())
    drivers = "; ".join(f.score_breakdown.get("drivers", [])) or "no intel drivers"
    rem = "".join(
        f'<li><b>{_esc(s["kind"])}:</b> {_esc(s["text"])}</li>' for s in f.remediation_suggestions)
    color = _SEV_COLORS.get(f.severity, "#999")
    return f"""<tr>
      <td>{_esc(f.score_breakdown.get('rank', ''))}</td>
      <td><b>{f.score}</b></td>
      <td>{_esc(f.priority)}</td>
      <td>{_esc(f.sla_hours)}h</td>
      <td>{_esc(f.owner)}</td>
      <td>{_esc(f.product)}</td>
      <td>{_esc(f.scanner)}</td>
      <td><span style="color:{color}">{_esc(f.severity)}</span></td>
      <td>{_esc(f.title[:70])}</td>
      <td>{_esc(f.cve or '-')}</td>
      <td>{_esc(f.cwe or '-')}</td>
      <td>{_esc((f.endpoint or '-')[:44])}</td>
      <td><details><summary>view</summary>
        <p><b>Score breakdown:</b> {_esc(comps)}</p>
        <p><b>Drivers:</b> {_esc(drivers)}</p>
        <p><b>EPSS:</b> {f.epss_score or '-'} (pct {f.epss_percentile or '-'})
           · <b>KEV:</b> {'yes ' + _esc(f.kev_date) if f.kev else 'no'}
           · <b>Exploit:</b> {'yes (' + _esc(f.exploit_source) + ')' if f.exploit_available else 'no'}
           · <b>Escalation:</b> {f.escalation_potential or 0.0}</p>
        <p><b>Description:</b> {_esc(f.description[:300])}</p>
        <ul>{rem}</ul>
      </details></td>
    </tr>"""


def _quarantine_rows(findings: List[Finding]) -> str:
    rows = [f for f in findings if f.status == "quarantined"]
    if not rows:
        return '<tr><td colspan="4">No findings quarantined this run.</td></tr>'
    return "".join(
        f"<tr><td>{_esc(f.product)}</td><td>{_esc(f.scanner)}</td>"
        f"<td>{_esc(f.title[:60])}</td><td>{_esc(f.quarantine_reason)}</td></tr>"
        for f in rows[:50])


def build_dashboard(path: str, findings: List[Finding], ranked: List[Finding],
                    summary: RunSummary, attack_paths: Dict[str, List[Dict[str, Any]]],
                    history: Dict[str, List[Dict[str, Any]]],
                    quarantine: List[Finding]) -> None:
    ba = svg_before_after(summary.raw_findings, summary.unique_findings,
                          summary.final_findings, summary.quarantined)
    ap_svgs = "".join(
        f'<div class="card"><h2>Attack paths — {_esc(product)}</h2>{svg_attack_path(paths, product)}</div>'
        for product, paths in attack_paths.items())
    ro_svg = svg_risk_over_time(history.get(summary.products[0], []) if summary.products else [])

    rows = "".join(_finding_row(f) for f in ranked[: int(summary.final_findings) or 50])
    qrows = _quarantine_rows(quarantine)

    html_doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Risk Dashboard — {_esc(summary.run_date)}</title>
<style>
 body {{ font-family: Arial, sans-serif; margin: 24px; background: #f4f6f8; color: #222; }}
 h1 {{ color: #0d47a1; }} h2 {{ color: #1565c0; font-size: 17px; }}
 .cards {{ display: flex; flex-wrap: wrap; gap: 12px; margin: 16px 0; }}
 .card {{ background: #fff; border-radius: 10px; padding: 16px; box-shadow: 0 1px 3px rgba(0,0,0,.12); margin-bottom: 16px; }}
 .stat {{ background: #fff; border-radius: 10px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(0,0,0,.12); min-width: 130px; }}
 .stat .n {{ font-size: 26px; font-weight: bold; color: #0d47a1; }}
 .stat .l {{ font-size: 12px; color: #666; }}
 table {{ width: 100%; border-collapse: collapse; background: #fff; font-size: 12.5px; }}
 th, td {{ padding: 7px 8px; text-align: left; border-bottom: 1px solid #e3e6ea; }}
 th {{ background: #1565c0; color: #fff; position: sticky; top: 0; }}
 tr:hover {{ background: #f0f5fa; }}
 details summary {{ cursor: pointer; color: #1565c0; }}
 .pill {{ padding: 2px 8px; border-radius: 10px; color: #fff; font-size: 11px; }}
</style></head><body>
<h1>🛡️ Vulnerability Risk Dashboard</h1>
<p>Run: <b>{_esc(summary.run_date)}</b> · Products: {', '.join(_esc(p) for p in summary.products)}</p>

<div class="cards">
  <div class="stat"><div class="n">{summary.raw_findings}</div><div class="l">raw findings</div></div>
  <div class="stat"><div class="n">{summary.unique_findings}</div><div class="l">after dedup ({summary.dedup_pct}%)</div></div>
  <div class="stat"><div class="n">{summary.quarantined}</div><div class="l">quarantined (auditable)</div></div>
  <div class="stat"><div class="n">{summary.final_findings}</div><div class="l">final active findings</div></div>
  <div class="stat"><div class="n">{summary.avg_score}</div><div class="l">avg risk score</div></div>
  <div class="stat"><div class="n">{summary.top_score}</div><div class="l">top risk score</div></div>
  <div class="stat"><div class="n">{summary.p1 + summary.p2}</div><div class="l">P1+P2 tickets</div></div>
</div>

<div class="card"><h2>Noise reduction (before / after)</h2>{ba}</div>

<div class="card"><h2>Risk reduction over time</h2>{ro_svg}</div>

{ap_svgs}

<div class="card"><h2>Ranked findings ({summary.final_findings})</h2>
<table><thead><tr><th>#</th><th>Score</th><th>Pri</th><th>SLA</th><th>Owner</th><th>Product</th>
<th>Scanner</th><th>Sev</th><th>Title</th><th>CVE</th><th>CWE</th><th>Endpoint</th><th>Details</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<div class="card"><h2>Quarantine log ({summary.quarantined} — nothing silently dropped)</h2>
<table><thead><tr><th>Product</th><th>Scanner</th><th>Title</th><th>Reason</th></tr></thead>
<tbody>{qrows}</tbody></table></div>

<p style="color:#888;font-size:11px">Generated by the shared risk-pipeline core · all charts are inline SVG (offline-friendly).</p>
</body></html>"""

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html_doc)
