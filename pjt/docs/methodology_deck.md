# Hackathon Activity 4 — Methodology Deck

## Risk Prioritization & Deduplication

> **Problem**: teams drown in raw scanner output. This pipeline ingests
> findings from multiple open-source scanners, strips duplicates and noise,
> enriches each finding with public threat intelligence, and produces a
> ranked, ticket-ready action list so teams fix what is *genuinely
> exploitable* first.

---

## 1. Solution approach (the 8 stages)

| # | Stage | What it does | Where |
|---|---|---|---|
| 1 | **Ingest & Normalize** | 4–6 scanner JSON/XML → one schema (`scanner, product, title, severity, CVE, CWE, endpoint, param, remediation, evidence`) | `core/normalize.py` |
| 2 | **Deduplication** | 3 passes: CVE-centric → endpoint+CWE → fuzzy title; canonical keeps richest evidence | `core/dedup.py` |
| 3 | **Filtering** | severity floor + FP patterns + risk-accept list; **nothing deleted** — quarantined with the rule that dropped it | `core/filter.py` |
| 4 | **Enrichment** | CISA KEV, FIRST.org EPSS (+7-day trend), NVD CVSS fallback, Exploit-DB; disk-cached | `core/enrich.py` |
| 5 | **Attack Path Mapping** | CAPEC-inspired CWE→CWE chains + escalation probability per path | `core/attackpath.py` |
| 6 | **Risk Scoring** | explainable 0–100 score from 8 factors (below) | `core/score.py` |
| 7 | **Remediation** | first-aid + full remediation + scanner guidance | `core/remediation.py` |
| 8 | **Ranking & Output** | P1–P4 + SLA + owner; CSV/JSON/markdown, HTML dashboard, metrics, history | `core/rank.py` `core/output.py` `core/dashboard.py` |

## 2. Key criteria → how we meet them

| Criterion | Evidence |
|---|---|
| Ingest ≥ 2 scanners into one dataset | **4 scanners** (ZAP, Nuclei, Wapiti, Trivy) + Nmap/OpenVAS parsers |
| Measurable noise reduction | `noise_reduction.json`: **63.85% dedup**, 37 quarantined with rule-by-rule breakdown |
| Scoring driven by real threat intel | weights: CVSS ≤25, **EPSS ≤15, KEV ≤20**, exploit ≤10 — a KEV Medium outranks a plain High |
| Explainable ranking, ticket-ready | every finding has a score-card breakdown + owner + SLA band |
| Auto-tickets + dashboard + methodology | GitHub Issues / DefectDojo findings; HTML dashboard; this deck |

## 3. Scoring model (0–100, transparent)

```
score = CVSS(≤25) + EPSS percentile(≤15) + KEV(≤20) + exploit(≤10)
      + asset criticality(≤10) + business impact(≤10) + exposure(≤5)
      − control effectiveness(≤5)
```

Every finding ships `score_breakdown`: the per-factor points and the
drivers (e.g. "in CISA KEV", "EPSS percentile 0.990", "EPSS rising
+0.013/7d"). That is the explainability a judge can interrogate.

**SLA bands**: score ≥ 80 → P1 / 24h · ≥ 60 → P2 / 72h · ≥ 40 → P3 / 7d ·
else P4 / 30d.

## 4. Attack-path & escalation model

Built from the **CAPEC attack-pattern graph** (prerequisites/consequences)
rather than invented rules:

- findings grouped by CWE → edges kept where a known chain exists
  (`CWE-502 deserialization → CWE-94 RCE`, `CWE-79 XSS → CWE-287 auth
  bypass`, …)
- per-path escalation probability:

```
P(path) = chainability
        × exploit_available (×1.3 if exploit/KEV present)
        × exposure boost (1 + 0.2 × exposure/10)
        × EPSS-trend boost (×1.15 if rising)
        — capped at 0.95
```

- each finding gets an `escalation_potential` = best path originating at
  its CWE → feeds the dashboard's attack-path graph.

## 5. Results on the lab (Juice Shop · NodeGoat · bWAPP)

| Metric | Value |
|---|---|
| Raw scanner findings | **2,122** |
| Unique after dedup | **767** → dedup **63.85%** (1,355 duplicates removed) |
| Quarantined (info + known FPs) | **37** (rule-by-rule logged) |
| Final active findings | **730** → noise removed **65.6%** |
| Enriched with EPSS | **696 CVEs** |
| Attack paths mapped | **15** |
| Ticket-ready (score ≥ 40) | **304** |

Before/after: **2,122 raw alerts → 730 prioritized findings** — teams
triage 34% of the original output, sorted by genuine exploitability.

## 6. Two deployable versions (one brain, two bodies)

**Version 1 — DefectDojo (DevSecOps CI/CD)**: GitHub Actions runs the
scanners + pipeline; results push into DefectDojo via REST (products →
engagements → tests → findings with EPSS/KEV/CWE fields); DefectDojo adds
its own dedup engine and report builder. *Industry-standard story.*

**Version 2 — fully custom**: SQLite store, GitHub Issues auto-ticketing
(with open-duplicate guard), standalone HTML/SVG dashboard, Docker image.
*"We built it ourselves" story.*

Both consume the same shared core → identical numbers, zero drift.

## 7. Live demo script (≈5 min)

1. `python -m unittest discover -s core/tests` → **36 tests green**
2. Run version 2: `python version2_custom/run_pipeline.py --reports
   sample_reports --config version2_custom/config.json --out outputs/v2
   --file-tickets` (instant — threat-intel cache warm)
3. Show `noise_reduction.json` (dedup %, quarantine breakdown)
4. Show `risk_dashboard.html` (before/after, attack-path graph,
   risk-over-time) and `tickets_ready.md`
5. Run version 1 with `--push-defectdojo` → findings appear in DefectDojo
   with EPSS/KEV/CWE columns

## 8. Honest limitations & next steps

- Lab CVEs are not in CISA KEV → P1/P2 bands are empty on this dataset;
  the scoring still ranks by EPSS (the rubric's intent). Point at any
  KEV-listed CVE (e.g. `CVE-2021-44228`) to show the P1 path.
- Exploit-DB lookup is optional (needs the `exploitdb/exploitdb` image);
  KEV doubles as the exploit signal when disabled.
- NVD fallback only fetches CVEs lacking a scanner CVSS (rate-limit
  friendly).
- Next: OpenVAS/Nmap full templates, delta reports across CI runs,
  DefectDojo report-builder export as the executive artifact.
