#!/usr/bin/env python3
"""Convert scanner JSON reports (nuclei | wapiti | trivy) into a standalone HTML report.

Usage: python3 json_to_html.py <nuclei|wapiti|trivy> <input.json> <output.html> <title>
"""
import json
import sys
from html import escape

SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4, "unknown": 5}


def esc(v):
    return escape("" if v is None else str(v))


def severity_rank(sev):
    return SEV_ORDER.get(str(sev).lower(), SEV_ORDER["unknown"])


def rows_for(kind, data):
    """Return (headers, rows) for the given scanner JSON kind."""
    if kind == "nuclei":
        headers = ["Severity", "Name", "Template", "Matched At", "Description"]
        rows = []
        for f in data or []:
            info = f.get("info") or {}
            rows.append([
                esc(info.get("severity", "")),
                esc(info.get("name", "")),
                esc(f.get("template-id", "")),
                esc(f.get("matched-at", "")),
                esc((info.get("description") or "")[:300]),
            ])
        return headers, rows

    if kind == "wapiti":
        headers = ["Severity", "Category", "Path", "Parameter", "Info"]
        level_map = {3: "high", 2: "medium", 1: "low", 0: "info"}
        rows = []
        for cat, findings in (data.get("vulnerabilities") or {}).items():
            for f in findings or []:
                rows.append([
                    esc(level_map.get(f.get("level"), "info")),
                    esc(cat),
                    esc(f.get("path", "")),
                    esc(f.get("parameter", "")),
                    esc((f.get("info") or "")[:300]),
                ])
        return headers, rows

    if kind == "trivy":
        headers = ["Severity", "Target", "CVE", "Package", "Installed", "Fixed"]
        rows = []
        for r in data.get("Results") or []:
            for v in r.get("Vulnerabilities") or []:
                rows.append([
                    esc(v.get("Severity", "")),
                    esc(r.get("Target", "")),
                    esc(v.get("VulnerabilityID", "")),
                    esc(v.get("PkgName", "")),
                    esc(v.get("InstalledVersion", "")),
                    esc(v.get("FixedVersion", "")),
                ])
        return headers, rows

    raise SystemExit(f"Unknown report kind: {kind}")


def main():
    if len(sys.argv) != 5:
        raise SystemExit(
            "Usage: json_to_html.py <nuclei|wapiti|trivy> <input.json> <output.html> <title>"
        )
    kind, src, dst, title = sys.argv[1:5]

    with open(src, encoding="utf-8") as fh:
        data = json.load(fh)

    headers, rows = rows_for(kind, data)
    rows.sort(key=lambda r: severity_rank(r[0]))

    counts = {}
    for r in rows:
        counts[r[0]] = counts.get(r[0], 0) + 1
    summary = " ".join(
        f'<span class="sev sev-{s}">{s}: {counts[s]}</span>' for s in sorted(counts, key=severity_rank)
    ) or "<span>no findings</span>"

    table_rows = "\n".join(
        f"<tr>{''.join(f'<td>{c}</td>' for c in row)}</tr>" for row in rows
    )
    header_cells = "".join(f"<th>{h}</th>" for h in headers)

    html_doc = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<style>
    body {{ font-family: Arial, sans-serif; margin: 30px; background: #f5f5f5; }}
    h1 {{ color: #333; }}
    .meta {{ color: #666; margin-bottom: 15px; }}
    .sev {{ padding: 3px 8px; border-radius: 4px; margin-right: 6px; font-size: 13px; }}
    .sev-critical {{ background: #d32f2f; color: white; }}
    .sev-high {{ background: #f57c00; color: white; }}
    .sev-medium {{ background: #fbc02d; color: #333; }}
    .sev-low {{ background: #7cb342; color: white; }}
    .sev-info {{ background: #90a4ae; color: white; }}
    table {{ width: 100%; border-collapse: collapse; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
    th, td {{ padding: 8px 10px; text-align: left; border-bottom: 1px solid #ddd; font-size: 13px; }}
    th {{ background: #2196F3; color: white; position: sticky; top: 0; }}
    tr:hover {{ background: #f5f5f5; }}
</style>
</head>
<body>
    <h1>{esc(title)}</h1>
    <div class="meta">Generated {esc(__import__('datetime').datetime.now().isoformat(timespec='seconds'))} · {len(rows)} findings</div>
    <div class="meta">{summary}</div>
    <table>
        <thead><tr>{header_cells}</tr></thead>
        <tbody>
{table_rows}
        </tbody>
    </table>
</body>
</html>
"""
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(html_doc)
    print(f"   📄 HTML report written: {dst} ({len(rows)} findings)")


if __name__ == "__main__":
    main()
