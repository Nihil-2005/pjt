# ─────────────────────────────────────────────────────────────────
#  Risk Prioritization & Deduplication pipeline — Makefile
# ─────────────────────────────────────────────────────────────────

.PHONY: help sync-core check-core-sync test run-v1 run-v2 clean install

# ── Primary targets ───────────────────────────────────────────────

help:
	@echo "Targets:"
	@echo "  make install         Install Python dependencies"
	@echo "  make sync-core       Sync root core/ into both version folders"
	@echo "  make check-core-sync Fail if any core copy is out of sync"
	@echo "  make test            Run all unit tests"
	@echo "  make run-v2          Run the full pipeline (v2 custom substrate)"
	@echo "  make run-v1          Run the full pipeline (v1 DefectDojo)"
	@echo "  make clean           Remove __pycache__ and .pyc files"

# ── Dependency install ────────────────────────────────────────────

install:
	pip install -r requirements.txt

# ── Core sync ─────────────────────────────────────────────────────

sync-core:
	rsync -av --delete \
	    --exclude='*.pyc' --exclude='__pycache__' \
	    core/ version1_defectdojo/core/
	rsync -av --delete \
	    --exclude='*.pyc' --exclude='__pycache__' \
	    core/ version2_custom/core/
	@echo "[OK] core/ synced to version1_defectdojo/core/ and version2_custom/core/"

check-core-sync:
	@echo "Checking core copies are in sync..."
	@diff -rq \
	    --exclude='*.pyc' --exclude='__pycache__' \
	    core/ version1_defectdojo/core/ \
	    && diff -rq \
	    --exclude='*.pyc' --exclude='__pycache__' \
	    core/ version2_custom/core/ \
	    && echo "[OK] All core copies in sync" \
	    || (echo "" && \
	        echo "ERROR: core copies are out of sync." && \
	        echo "       Run:  make sync-core" && \
	        echo "" && exit 1)

# ── Tests ─────────────────────────────────────────────────────────

test:
	python -m pytest core/tests/ -v --tb=short

test-v1:
	python -m pytest version1_defectdojo/core/tests/ -v --tb=short

test-v2:
	python -m pytest version2_custom/core/tests/ -v --tb=short

test-all: test test-v1 test-v2

# ── Pipeline runs ─────────────────────────────────────────────────

run-v2:
	python version2_custom/run_pipeline.py \
	    --reports sample_reports \
	    --config  version2_custom/config.json \
	    --out     outputs/v2 \
	    --file-tickets

run-v2-ai:
	ANTHROPIC_API_KEY=$${ANTHROPIC_API_KEY} \
	NVD_API_KEY=$${NVD_API_KEY} \
	python version2_custom/run_pipeline.py \
	    --reports sample_reports \
	    --config  version2_custom/config.json \
	    --out     outputs/v2 \
	    --file-tickets

run-v2-skip-enrich:
	python version2_custom/run_pipeline.py \
	    --reports     sample_reports \
	    --config      version2_custom/config.json \
	    --out         outputs/v2-fast \
	    --skip-enrich \
	    --skip-ai

run-v1:
	python version1_defectdojo/run_pipeline.py \
	    --reports sample_reports \
	    --config  version1_defectdojo/config.json \
	    --out     outputs/v1

# ── Clean ─────────────────────────────────────────────────────────

clean:
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; true
	@find . -name '*.pyc' -delete 2>/dev/null; true
	@echo "[OK] cleaned __pycache__ and .pyc files"

clean-outputs:
	rm -rf outputs/
	@echo "[OK] outputs/ removed"

clean-cache:
	rm -rf .threat_cache/
	@echo "[OK] threat intel cache cleared"
