import unittest

from core.filter import filter_findings
from core.models import Finding


def mk(severity="medium", title="Something", description="", product="app", cwe=None):
    return Finding(scanner="zap", product=product, title=title, severity=severity,
                   description=description, cwe=cwe)


CFG = {"drop_severity": ["info"], "fp_patterns": ["swagger", "backup file"],
       "risk_accept": [{"product": "app", "cwe": "CWE-200"}]}


class TestFilter(unittest.TestCase):
    def test_drops_info_severity(self):
        fs = [mk("info", "Noise"), mk("high", "Real")]
        out = filter_findings(fs, CFG, {})
        self.assertEqual(out["metrics"]["active"], 1)
        self.assertEqual(out["metrics"]["quarantined"], 1)
        q = [f for f in fs if f.status == "quarantined"][0]
        self.assertIn("severity", q.quarantine_reason)

    def test_fp_pattern(self):
        fs = [mk("medium", "Swagger UI Detected")]
        out = filter_findings(fs, CFG, {})
        self.assertEqual(out["metrics"]["active"], 0)
        self.assertIn("fp_pattern", fs[0].quarantine_reason)

    def test_risk_accept(self):
        fs = [mk("high", "Info Leak", cwe="CWE-200")]
        out = filter_findings(fs, CFG, {})
        self.assertEqual(fs[0].quarantine_reason, "risk_accept")

    def test_audit_log_never_silent(self):
        fs = [mk("info", "a"), mk("medium", "Backup File b"), mk("high", "c")]
        out = filter_findings(fs, CFG, {})
        rules = out["metrics"]["quarantine_by_rule"]
        self.assertEqual(sum(rules.values()), 2)
        self.assertEqual(set(rules.keys()) & {"risk_accept"}, set())


if __name__ == "__main__":
    unittest.main()
