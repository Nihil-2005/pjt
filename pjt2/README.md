# Risk Prioritization & Deduplication Pipeline

**Hackathon Activity 4** — a pipeline that ingests raw findings from multiple
vulnerability scanners, strips out duplicate and noisy alerts, enriches each
finding with public threat intelligence, and produces a ranked, ticket-ready
action list so teams fix what is *genuinely exploitable* first.

Two deployable versions share **one brain** (the `core/` engine) and differ
only in their substrate:

| | **Version 1 — DefectDojo** (`version1_defectdojo/`) | **Version 2 — fully custom** (`version2_custom/`) |
|---|---|---|
| Storage / dashboard | DefectDojo (REST API, findings explorer, reports) | SQLite (`v2.db`) + standalone HTML/SVG dashboard |
| Dedup layer | pipeline dedup + DefectDojo's own dedup engine | pipeline dedup only |
| Ticketing | DefectDojo findings (Jira/GitHub via DefectDojo) + GitHub Issues | **GitHub Issues** (stdlib `urllib`) |
| CI/CD | GitHub Actions workflow + `pipeline.sh` | `pipeline.sh` + Docker image + compose |
| Dependency | `requests` (client only) | **stdlib-only** |

```
                    ┌──────────────────────────────────────────┐
                    │         SHARED CORE  (core/)             │
                    │  normalize → dedup → filter → enrich     │
                    │  → attack paths → score → remediate →    │
                    │  rank                                     │
                    └───────────────┬──────────────────────────┘
                                    │ same ranked dataset
                   ┌────────────────┴─────────────────┐
                   ▼                                  ▼
      VERSION 1: DefectDojo substrate         VERSION 2: custom substrate
      (dashboard + history + reports)         (SQLite + GitHub Issues +
                                               own dashboard)
```

## Pipeline stages (both versions)

1. **Ingest & Normalize** — parses ZAP, Nuclei, Wapiti, Trivy, Nmap, OpenVAS
   reports into one schema (`core/normalize.py`).
2. **Deduplication** — CVE-centric → endpoint+CWE → fuzzy-title passes; the
   canonical finding keeps the richest evidence from every duplicate
   (`core/dedup.py`).
3. **Filtering (auditable)** — severity floor + FP patterns + risk-accept
   list. Nothing is deleted: every dropped finding is *quarantined* with the
   rule that dropped it (`core/filter.py`).
4. **Enrichment** — CISA KEV (known-exploited + date), FIRST.org **EPSS**
   score/percentile + 7-day trend, NVD CVSS fallback, optional Exploit-DB.
   All lookups cached on disk (`core/enrich.py`).
5. **Attack Path Mapping** — CAPEC-inspired CWE→CWE chains with an
   escalation probability per path (`core/attackpath.py`).
6. **Risk Scoring (0–100, explainable)** — CVSS + EPSS percentile + KEV +
   exploit availability + asset criticality + business impact + exposure,
   reduced by control effectiveness. Every finding carries a score-card
   breakdown (`core/score.py`).
7. **Remediation** — first-aid + full remediation + scanner-provided
   guidance (`core/remediation.py`).
8. **Ranking & Output** — priority P1–P4 with SLA hours and owners; ranked
   CSV/JSON, top-actions markdown, ticket-ready list, noise-reduction
   metrics, HTML/SVG dashboard (before/after, attack-path graph,
   risk-over-time), run history (`core/rank.py`, `core/output.py`,
   `core/dashboard.py`, `core/history.py`).

## Quickstart

```bash
# 0) run scanners (optional — sample reports are already in sample_reports/)
./scans/scan.sh      # or bring your own <product>_<scanner>.json files

# 1) shared-core tests
python -m unittest discover -s core/tests

# 2) version 2 (fully custom, no external services)
python version2_custom/run_pipeline.py --reports sample_reports \
    --config version2_custom/config.json --out outputs/v2 --file-tickets
#   → open outputs/v2/risk_dashboard.html

# 3) version 1 (DefectDojo dashboard)
export DD_API_TOKEN=...      # your DefectDojo API token
version1_defectdojo/pipeline.sh   # or:
python version1_defectdojo/run_pipeline.py --reports sample_reports \
    --config version1_defectdojo/config.json --out outputs/v1 --push-defectdojo
#   → open http://localhost:8080 (DefectDojo)
```

> **Tip**: the first run hits the live threat-intel APIs (EPSS, KEV, NVD)
> and caches results; re-runs are instant and offline.

## Scoring model (why it's not "raw CVSS alone")

```
score (0–100) =
    CVSS          (≤25)  severity/CVSS base score
  + EPSS          (≤15)  FIRST.org exploit-prediction percentile
  + KEV           (≤20)  CISA known-exploited status
  + exploit       (≤10)  public exploit available (exploit-db / KEV)
  + asset         (≤10)  asset criticality (per product)
  + business      (≤10)  business impact (per product)
  + exposure      (≤ 5)  exposure level (per product)
  − controls      (≤ 5)  strong controls reduce the score
```

A KEV-listed **Medium** CVE outranks a non-KEV **High** CVE — the rubric's
"not raw CVSS alone" test (`core/tests/test_score.py`).

## Results on the sample lab (Juice Shop / NodeGoat / bWAPP)

| Metric | Value |
|---|---|
| Raw scanner findings | 2,122 |
| After dedup (unique) | 767 (**63.85% dedup**) |
| Quarantined (info-severity + known FPs) | 37 |
| Final active findings | 730 |
| Enriched with EPSS | 696 CVEs |
| Attack paths mapped | 15 |
| Ticket-ready findings (score ≥ 40) | 304 |

## Repo layout

```
core/                     canonical shared engine (stdlib-only) + tests
version1_defectdojo/      DefectDojo substrate — SELF-CONTAINED (has its own core/ copy)
version2_custom/          custom substrate — SELF-CONTAINED (has its own core/ copy)
sample_reports/           demo scanner reports (pipeline default input)
scans/                    scanner lab: scan.sh, setup.sh, docker-compose.yml, Dockerfile.wapiti, json_to_html.py, credentials/
scan_reports/             raw scan archives (dated folders + zip)
outputs/                  generated pipeline outputs (v1/ v1_enriched/ v2/)
logs/                     runtime logs
.threat_cache/            threat-intel cache (EPSS/KEV/NVD — warm, so re-runs are instant)
docs/                     methodology deck + activity reference image
```

Each version folder ships a **vendored copy of `core/`** and resolves it locally,
so `version1_defectdojo/` and `version2_custom/` are fully standalone — copy
either folder anywhere (a CI runner, a Docker host, a fresh checkout) and it
runs on its own, no shared root needed. The root `core/` remains the canonical
source the copies are taken from.
