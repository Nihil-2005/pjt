# Version 2 — fully custom substrate (no DefectDojo dependency).
# The shared core + v2 orchestrator are stdlib-only, so the image is tiny.
FROM python:3.12-slim

WORKDIR /app

# copy the whole repo (core + version2)
COPY . .

WORKDIR /app/version2_custom

# the pipeline writes outputs to /out (mounted volume)
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "run_pipeline.py"]
CMD ["--reports", "/app/sample_reports", "--config", "config.json", "--out", "/out", "--file-tickets"]
