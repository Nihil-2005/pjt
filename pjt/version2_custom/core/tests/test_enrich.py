import json
import os
import tempfile
import unittest

from core.enrich import Enricher, Fetcher
from core.models import Finding


class FakeFetcher(Fetcher):
    """Serves canned KEV/EPSS/NVD responses."""

    def __init__(self):
        self.calls = []

    def get_json(self, url, headers=None, timeout=20):
        self.calls.append(url)
        if "kev" in url:
            return {"vulnerabilities": [
                {"cveID": "CVE-2021-44228", "dateAdded": "2021-12-10",
                 "vendorProject": "Apache", "product": "Log4j"}]}
        if "epss" in url and "date=" in url:
            return {"data": [{"cve": "CVE-2021-44228", "epss": "0.800000000"}]}
        if "epss" in url:
            return {"data": [{"cve": "CVE-2021-44228", "epss": "0.999990000",
                              "percentile": "1.000000000"}]}
        if "nvd" in url:
            return {"vulnerabilities": [{"cve": {"metrics": {
                "cvssMetricV31": [{"cvssData": {"baseScore": 10.0}}]}}}]}
        return {}


class TestEnrich(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.cfg = {"cache_dir": os.path.join(self.tmp, "cache"),
                    "use_nvd": True, "use_searchsploit": False,
                    "kev_url": "https://x/kev.json", "epss_url": "https://x/epss",
                    "nvd_url": "https://x/nvd", "cache_ttl_days": 1}
        self.fetcher = FakeFetcher()

    def test_full_enrichment(self):
        f = Finding(scanner="trivy", product="app", title="Log4Shell",
                    severity="critical", cve="CVE-2021-44228")
        e = Enricher(self.cfg, fetcher=self.fetcher)
        e.enrich([f], use_searchsploit=False)
        self.assertTrue(f.kev)
        self.assertEqual(f.kev_date, "2021-12-10")
        self.assertAlmostEqual(f.epss_score, 0.99999)
        self.assertEqual(f.epss_percentile, 1.0)
        self.assertEqual(f.nvd_cvss, 10.0)
        self.assertTrue(f.exploit_available)          # KEV doubles as exploit
        self.assertEqual(f.exploit_source, "cisa-kev")
        self.assertGreater(f.epss_trend, 0)           # rising vs 7d ago

    def test_no_cve_findings_untouched(self):
        f = Finding(scanner="zap", product="app", title="XSS", severity="medium")
        e = Enricher(self.cfg, fetcher=self.fetcher)
        e.enrich([f], use_searchsploit=False)
        self.assertFalse(f.kev)
        self.assertIsNone(f.epss_score)

    def test_cache_used_on_second_run(self):
        f = Finding(scanner="trivy", product="app", title="Log4Shell",
                    severity="critical", cve="CVE-2021-44228")
        e1 = Enricher(self.cfg, fetcher=self.fetcher)
        e1.enrich([f], use_searchsploit=False)
        calls_after_first = len(self.fetcher.calls)
        e2 = Enricher(self.cfg, fetcher=self.fetcher)
        e2.enrich([f], use_searchsploit=False)
        self.assertLess(len(self.fetcher.calls), calls_after_first + 10)


if __name__ == "__main__":
    unittest.main()
