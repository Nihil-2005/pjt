# Version 1 — DefectDojo substrate (DevSecOps CI/CD)

Runs the shared risk pipeline and pushes the **deduplicated + enriched**
results into DefectDojo (your dashboard / history / reporting layer) over
its REST API. This is the "industry-standard" version: scanners run in CI,
DefectDojo stores and displays everything, and its own dedup engine adds a
second layer on top of our pipeline's.

## Components

| File | Purpose |
|---|---|
| `core/` | vendored copy of the shared 8-stage engine (normalize → dedup → filter → enrich → attack paths → score → remediate → rank). Makes this folder **self-contained** — copy it anywhere and it runs. |
| `run_pipeline.py` | orchestrator: shared core → push to DefectDojo |
| `defectdojo_client.py` | DefectDojo API v2 client (products, engagements, tests, findings) |
| `import_payloads.py` | maps findings → DefectDojo payloads (score breakdown, threat intel, remediation) |
| `config.json` | product context (owner, asset criticality, business impact, exposure, controls) |
| `pipeline.sh` | bash orchestrator (scan → pipeline → push) |
| `.github/workflows/pipeline.yml` | GitHub Actions CI/CD |
| `test_version1.py` | unit tests (client mocked, payloads asserted) |

## What gets pushed per finding

DefectDojo natively stores everything we enrich (verified against
3.2.100):

- `title` — `[P1] <title> (<product>)` (ticket-ready)
- `severity`, `cwe`, `cve`, `cvssv3` / `cvssv3_score`
- `epss_score`, `epss_percentile`, `known_exploited`, `kev_date`
- `description` — full score-card: 0–100 score, component breakdown,
  threat intel, attack-path context, scanner provenance, remediation
- `found_by`, `numerical_severity`, `deduplication_on_engagement`

## Running

```bash
# 1) DefectDojo must be up (your docker-compose stack, API on :8080)
# 2) get an API token (admin user):
#    docker exec django-defectdojo-uwsgi-1 bash -lc "cd /app && ./manage.py shell -c \
#      \"from rest_framework.authtoken.models import Token; \
#       from django.contrib.auth.models import User; \
#       t,_=Token.objects.get_or_create(user=User.objects.get(username='admin')); print(t.key)\""

export DD_API_TOKEN=<token>
export DD_BASE_URL=http://localhost:8080
export PUSH_DD=1
./pipeline.sh
```

Or directly:

```bash
python run_pipeline.py --reports ../sample_reports --config config.json \
    --out ../outputs/v1 --push-defectdojo
```

Open DefectDojo → the `juice_shop` / `nodegoat` / `bwapp` products → the
engagement → test → findings. Each finding carries its full risk score-card.

## GitHub Actions

`.github/workflows/pipeline.yml` runs the pipeline weekly (or on demand) and
uploads the ranked CSV/JSON, top actions, tickets, metrics and dashboard as
artifacts. Configure two repo secrets:

- `DD_API_TOKEN` — DefectDojo API token
- `DD_BASE_URL` — e.g. `https://defectdojo.example.com`

## Tests

```bash
python test_version1.py
```
