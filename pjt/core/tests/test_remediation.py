import unittest

from core.models import Finding
from core.remediation import suggest_remediation


class TestRemediation(unittest.TestCase):
    def test_two_to_three_suggestions(self):
        f = Finding(scanner="zap", product="app", title="SQLi", severity="high",
                    cwe="CWE-89", remediation="Use prepared statements")
        sugg = suggest_remediation(f)
        self.assertGreaterEqual(len(sugg), 2)
        self.assertLessEqual(len(sugg), 3)
        kinds = {s["kind"] for s in sugg}
        self.assertIn("first_aid", kinds)
        self.assertIn("full_remediation", kinds)

    def test_first_aid_differs_from_full(self):
        f = Finding(scanner="zap", product="app", title="SQLi", severity="high", cwe="CWE-89")
        sugg = {s["kind"]: s["text"] for s in suggest_remediation(f)}
        self.assertNotEqual(sugg["first_aid"], sugg["full_remediation"])
        self.assertIn("parameterized", sugg["full_remediation"].lower())

    def test_trivy_uses_fixed_version(self):
        f = Finding(scanner="trivy", product="app", title="t", severity="critical",
                    cve="CVE-2021-44228", package="log4j-core",
                    installed_version="2.14.0", fixed_version="2.17.1")
        sugg = {s["kind"]: s["text"] for s in suggest_remediation(f)}
        self.assertIn("2.17.1", sugg["full_remediation"])

    def test_scanner_guidance_included_when_present(self):
        f = Finding(scanner="zap", product="app", title="X", severity="low",
                    remediation="Disable the feature")
        sugg = suggest_remediation(f)
        self.assertTrue(any(s["kind"] == "scanner_guidance" for s in sugg))

    def test_generic_fallback(self):
        f = Finding(scanner="zap", product="app", title="Mystery", severity="low")
        sugg = {s["kind"]: s["text"] for s in suggest_remediation(f)}
        self.assertTrue(sugg["first_aid"])
        self.assertTrue(sugg["full_remediation"])


if __name__ == "__main__":
    unittest.main()
