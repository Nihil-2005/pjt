"""SQLite persistence layer for version 2 (fully custom substrate).

Stores:
  - every run's findings (the normalized + enriched + scored rows),
  - run summaries (before/after metrics, priority counts, avg score),
  - the risk-reduction-over-time history (queried by the dashboard).

The core ``history.py`` already keeps a small SQLite history store for the
risk-over-time chart; this module is the *full* finding store so version 2
has a real database behind its dashboard (no DefectDojo dependency).
"""
from __future__ import annotations

import json
import os
import sqlite3
from typing import Any, Dict, List, Optional

from core.models import Finding

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_date TEXT NOT NULL,
    product TEXT NOT NULL,
    raw_findings INTEGER DEFAULT 0,
    unique_findings INTEGER DEFAULT 0,
    quarantined INTEGER DEFAULT 0,
    final_findings INTEGER DEFAULT 0,
    dedup_pct REAL DEFAULT 0,
    avg_score REAL DEFAULT 0,
    top_score REAL DEFAULT 0,
    p1 INTEGER DEFAULT 0,
    p2 INTEGER DEFAULT 0,
    p3 INTEGER DEFAULT 0,
    p4 INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS findings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_date TEXT NOT NULL,
    product TEXT NOT NULL,
    scanner TEXT,
    title TEXT,
    severity TEXT,
    status TEXT,
    cve TEXT,
    cwe TEXT,
    endpoint TEXT,
    parameter TEXT,
    score REAL,
    priority TEXT,
    sla_hours INTEGER,
    owner TEXT,
    epss_score REAL,
    epss_percentile REAL,
    epss_trend REAL,
    kev INTEGER DEFAULT 0,
    kev_date TEXT,
    exploit_available INTEGER DEFAULT 0,
    exploit_source TEXT,
    escalation_potential REAL,
    dedup_key TEXT,
    is_duplicate INTEGER DEFAULT 0,
    payload TEXT
);
CREATE INDEX IF NOT EXISTS idx_findings_run ON findings(run_date, product);
CREATE INDEX IF NOT EXISTS idx_findings_prio ON findings(product, priority);
"""


class Storage:
    def __init__(self, db_path: str):
        self.db_path = db_path
        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.conn.executescript(SCHEMA)

    def close(self) -> None:
        self.conn.close()

    # ------------------------------------------------------------- writers
    def save_run(self, run_date: str, product: str, summary: Dict[str, Any]) -> int:
        cur = self.conn.execute(
            """INSERT INTO runs (run_date, product, raw_findings, unique_findings,
               quarantined, final_findings, dedup_pct, avg_score, top_score,
               p1, p2, p3, p4)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (run_date, product, summary.get("raw", 0), summary.get("unique", 0),
             summary.get("quarantined", 0), summary.get("final", 0),
             summary.get("dedup_pct", 0.0), summary.get("avg_score", 0.0),
             summary.get("top_score", 0.0), summary.get("p1", 0),
             summary.get("p2", 0), summary.get("p3", 0), summary.get("p4", 0)))
        self.conn.commit()
        return cur.lastrowid

    def save_findings(self, run_date: str, findings: List[Finding]) -> None:
        # keep the findings table as "latest run only": remove the previous
        # run's rows, then insert the new ones.  Run summaries stay for the
        # risk-reduction-over-time history.
        self.conn.execute("DELETE FROM findings WHERE run_date != ?", (run_date,))
        rows = []
        for f in findings:
            rows.append((
                run_date, f.product, f.scanner, f.title, f.severity, f.status,
                f.cve, f.cwe, f.endpoint, f.parameter, f.score, f.priority,
                f.sla_hours, f.owner, f.epss_score, f.epss_percentile,
                f.epss_trend, 1 if f.kev else 0, f.kev_date,
                1 if f.exploit_available else 0, f.exploit_source,
                f.escalation_potential, f.dedup_key, 1 if f.is_duplicate else 0,
                json.dumps(f.to_dict(), default=str)))
        self.conn.executemany(
            """INSERT INTO findings (run_date, product, scanner, title, severity,
               status, cve, cwe, endpoint, parameter, score, priority, sla_hours,
               owner, epss_score, epss_percentile, epss_trend, kev, kev_date,
               exploit_available, exploit_source, escalation_potential, dedup_key,
               is_duplicate, payload)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", rows)
        self.conn.commit()

    # ------------------------------------------------------------- readers
    def latest_run_date(self) -> Optional[str]:
        row = self.conn.execute("SELECT MAX(run_date) FROM runs").fetchone()
        return row[0] if row and row[0] else None

    def history(self, product: Optional[str] = None) -> List[Dict[str, Any]]:
        q = ("SELECT run_date, product, raw_findings, unique_findings, quarantined,"
             " final_findings, dedup_pct, avg_score, top_score, p1, p2, p3, p4"
             " FROM runs")
        args: tuple = ()
        if product:
            q += " WHERE product = ?"
            args = (product,)
        q += " ORDER BY run_date, product"
        cols = ["run_date", "product", "raw", "unique", "quarantined", "final",
                "dedup_pct", "avg_score", "top_score", "p1", "p2", "p3", "p4"]
        return [dict(zip(cols, row)) for row in self.conn.execute(q, args).fetchall()]

    def findings_for_run(self, run_date: str, product: Optional[str] = None,
                         status: str = "active") -> List[Dict[str, Any]]:
        q = "SELECT payload FROM findings WHERE run_date = ? AND status = ?"
        args: list = [run_date, status]
        if product:
            q += " AND product = ?"
            args.append(product)
        return [json.loads(r[0]) for r in self.conn.execute(q, args).fetchall()]

    def summary(self) -> Dict[str, Any]:
        """Aggregate stats across all runs (for the dashboard header)."""
        total_findings = self.conn.execute(
            "SELECT COUNT(*) FROM findings WHERE status='active'").fetchone()[0]
        runs = self.conn.execute("SELECT COUNT(DISTINCT run_date) FROM runs").fetchone()[0]
        top = self.conn.execute("SELECT MAX(score) FROM findings").fetchone()[0]
        return {"total_active_findings": total_findings, "runs": runs,
                "top_score": top}
