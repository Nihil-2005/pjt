# Version 2 — fully custom substrate (no DefectDojo)

Everything built ourselves: the same shared risk engine plus our **own**
persistence (SQLite), our **own** ticketing (GitHub Issues), our **own**
dashboard (standalone HTML/SVG) and our **own** Docker deployment.
Stdlib-only Python — no third-party packages at runtime.

## Components

| File | Purpose |
|---|---|
| `core/` | vendored copy of the shared 8-stage engine (normalize → dedup → filter → enrich → attack paths → score → remediate → rank). Makes this folder **self-contained** — copy it anywhere and it runs. |
| `run_pipeline.py` | orchestrator: shared core → SQLite → tickets |
| `storage.py` | SQLite store (findings per run + run-history for risk-over-time) |
| `github_issues.py` | auto-file GitHub Issues for findings ≥ threshold (dedup-guard against open duplicates) |
| `config.json` | product context + ticket threshold |
| `pipeline.sh` | bash orchestrator |
| `Dockerfile` / `docker-compose.yml` | containerized deployment |
| `test_version2.py` | unit tests (storage round-trip, GitHub mocked, tickets) |

## Running locally

```bash
python run_pipeline.py --reports ../sample_reports --config config.json \
    --out ../outputs/v2 --file-tickets
```

Outputs: `ranked_findings.csv/json`, `top_actions.md`, `tickets_ready.md`,
`noise_reduction.json`, `risk_dashboard.html`, `history.db`, `v2.db`.

Open `../outputs/v2/risk_dashboard.html` — it includes the before/after noise
reduction, the attack-path graph per product, the risk-reduction-over-time
chart and the ranked table.

## Auto-ticketing (GitHub Issues)

```bash
export GH_REPO=your-org/your-repo
export GH_TOKEN=<github-pat>     # needs "issues: write"
TICKETS=github ./pipeline.sh     # or TICKETS=both for file + GitHub
```

Findings with `score >= ticket_threshold` (default 40, see `config.json`)
become issues titled `[P1] <title> (<product>)` with labels
`security, priority:P1`, an explainable body (score breakdown, threat
intel, attack-path context, remediation) and the SLA/owner. The de-dup
guard skips titles that already have an open issue.

```bash
# dry-run (no API calls):
python run_pipeline.py --reports ../sample_reports --config config.json \
    --out ../outputs/v2 --github-tickets --dry-run --github-repo org/repo --github-token x
```

## Docker

```bash
docker build -f Dockerfile -t risk-pipeline-v2 ..
docker run --rm -v "$(pwd)/outputs/v2:/out" risk-pipeline-v2 \
    --reports /app/sample_reports --config config.json --out /out --file-tickets

# or with compose:
docker compose run --rm pipeline
```

## Tests

```bash
python test_version2.py
```
