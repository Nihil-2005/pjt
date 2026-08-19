import unittest

from core.dedup import deduplicate
from core.models import Finding


def mk(scanner, product="app", title="X", severity="high", cve=None, cwe=None,
       endpoint=None, parameter=None):
    return Finding(scanner=scanner, product=product, title=title, severity=severity,
                   cve=cve, cwe=cwe, endpoint=endpoint, parameter=parameter)


class TestDedup(unittest.TestCase):
    def test_cve_dedup_across_scanners(self):
        fs = [
            mk("nuclei", cve="CVE-2021-44228", title="Log4Shell via HTTP"),
            mk("trivy", cve="CVE-2021-44228", title="Log4Shell in image"),
            mk("zap", cve="CVE-2021-44228", title="Log4j JNDI"),
        ]
        out = deduplicate(fs)
        uniques = [f for f in out["findings"] if not f.is_duplicate]
        self.assertEqual(len(uniques), 1)
        self.assertEqual(out["metrics"]["unique"], 1)
        self.assertEqual(out["metrics"]["dedup_pct"], round(2 / 3 * 100, 2))

    def test_endpoint_cwe_dedup(self):
        fs = [
            mk("zap", cwe="CWE-79", endpoint="http://app/x", parameter="q",
               title="Reflected XSS"),
            mk("wapiti", cwe="CWE-79", endpoint="http://app/x", parameter="q",
               title="Cross Site Scripting"),
        ]
        out = deduplicate(fs)
        uniques = [f for f in out["findings"] if not f.is_duplicate]
        self.assertEqual(len(uniques), 1)
        self.assertEqual(out["metrics"]["by_pass"]["endpoint"], 1)

    def test_distinct_findings_stay(self):
        fs = [
            mk("zap", cwe="CWE-89", endpoint="/a", severity="high"),
            mk("zap", cwe="CWE-79", endpoint="/b", severity="medium"),
        ]
        out = deduplicate(fs)
        self.assertEqual(out["metrics"]["unique"], 2)
        self.assertEqual(out["metrics"]["dedup_pct"], 0.0)

    def test_title_dedup_when_enabled(self):
        fs = [
            mk("zap", severity="medium", title="Information Disclosure - Backup File Found"),
            mk("wapiti", severity="medium", title="Backup File Found - Information Disclosure"),
        ]
        out = deduplicate(fs, fuzzy=True)
        self.assertEqual(out["metrics"]["unique"], 1)

    def test_empty(self):
        out = deduplicate([])
        self.assertEqual(out["metrics"]["raw"], 0)
        self.assertEqual(out["metrics"]["unique"], 0)


if __name__ == "__main__":
    unittest.main()
