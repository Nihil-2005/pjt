import json
import os
import sys
import tempfile
import unittest
from unittest.mock import patch

# resolve the vendored `core/` shipped inside this version folder (folder is self-contained)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import Config  # noqa: E402
from core.models import Finding  # noqa: E402
from core.score import compute_score  # noqa: E402

from github_issues import GitHubIssues, write_tickets_md, _issue_body  # noqa: E402
from storage import Storage  # noqa: E402


def mk_finding(score_seed=None, priority="P1", title="XSS", status="active",
               product="app", score=None):
    f = Finding(scanner="zap", product=product, title=title, severity="high",
                cwe="CWE-79", endpoint="http://app/x", status=status,
                cve="CVE-2021-44228", description="xss found")
    f.kev = True
    f.kev_date = "2021-12-10"
    f.epss_score = 0.95
    f.epss_percentile = 0.99
    f.exploit_available = True
    f.exploit_source = "cisa-kev"
    f.score = score if score is not None else 88.0
    f.priority = priority
    f.sla_hours = 24
    f.owner = "appsec-web"
    f.score_breakdown = {"components": {"cvss": 25, "epss": 15, "kev": 20},
                         "total": 88.0, "drivers": ["in CISA KEV"]}
    f.remediation_suggestions = [
        {"kind": "first_aid", "text": "Block JNDI lookups"},
        {"kind": "full_remediation", "text": "Upgrade log4j-core to 2.17.1"},
    ]
    return f


CFG = Config({"products": {"app": {"owner": "appsec-web", "asset_criticality": 8,
                                   "business_impact": 8, "exposure": 9,
                                   "control_effectiveness": 2}}})


class TestStorage(unittest.TestCase):
    def test_roundtrip(self):
        td = tempfile.mkdtemp()
        try:
            db = Storage(os.path.join(td, "v2.db"))
            fs = [mk_finding(1), mk_finding(2, priority="P4", title="low", score=10.0)]
            db.save_run("2026-08-16T10:00:00", "app", {"raw": 5, "unique": 2, "quarantined": 1,
                                              "final": 2, "dedup_pct": 60.0,
                                              "avg_score": 49.0, "top_score": 88.0,
                                              "p1": 1, "p2": 0, "p3": 0, "p4": 1})
            db.save_findings("2026-08-16T10:00:00", fs)
            self.assertEqual(db.latest_run_date(), "2026-08-16T10:00:00")
            hist = db.history()
            self.assertEqual(len(hist), 1)
            self.assertEqual(hist[0]["p1"], 1)
            rows = db.findings_for_run("2026-08-16T10:00:00")
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["cve"], "CVE-2021-44228")
            summ = db.summary()
            self.assertEqual(summ["total_active_findings"], 2)
            db.close()
        finally:
            import shutil
            shutil.rmtree(td, ignore_errors=True)


class TestGitHubIssues(unittest.TestCase):
    def test_dry_run_counts_and_filters(self):
        fs = [mk_finding(1, priority="P1", score=88.0),
              mk_finding(2, priority="P4", title="low", score=10.0),
              mk_finding(3, priority="P2", title="med", score=65.0)]
        gh = GitHubIssues("owner/repo", "tok", dry_run=True)
        stats = gh.file_issues(fs, threshold=60.0)
        self.assertEqual(stats["created"], 2)   # P1 + P2 (P4 below threshold)
        self.assertEqual(stats["below_threshold"], 1)

    @patch("github_issues.GitHubIssues._open_issue_titles",
           return_value={"[P1] XSS (app)"})
    @patch("github_issues.GitHubIssues._request")
    def test_skips_duplicate_titles(self, mock_req, mock_titles):
        fs = [mk_finding(1, priority="P1", score=88.0)]
        gh = GitHubIssues("owner/repo", "tok", dry_run=False)
        stats = gh.file_issues(fs, threshold=60.0)
        self.assertEqual(stats["skipped_duplicate"], 1)
        self.assertEqual(stats["created"], 0)
        mock_req.assert_not_called()

    def test_issue_body_explainable(self):
        body = _issue_body(mk_finding(1))
        self.assertIn("88.0", body)
        self.assertIn("CVE-2021-44228", body)
        self.assertIn("first_aid", body)
        self.assertIn("Upgrade log4j-core", body)

    def test_tickets_md(self):
        with tempfile.TemporaryDirectory() as td:
            path = os.path.join(td, "tickets.md")
            n = write_tickets_md([mk_finding(1, score=88.0),
                                  mk_finding(2, priority="P4", title="low", score=10.0)],
                                 path, threshold=60.0)
            self.assertEqual(n, 1)
            content = open(path, encoding="utf-8").read()
            self.assertIn("P1", content)
            self.assertNotIn("low", content)


if __name__ == "__main__":
    unittest.main()
