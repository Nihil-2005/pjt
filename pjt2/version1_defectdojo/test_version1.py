import os
import sys
import unittest
from unittest.mock import patch

# resolve the vendored `core/` shipped inside this version folder (folder is self-contained)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config import Config  # noqa: E402
from core.models import Finding  # noqa: E402
from core.score import compute_score  # noqa: E402

from defectdojo_client import DefectDojoClient, _split_url  # noqa: E402
from import_payloads import finding_to_payload, _cwe_id  # noqa: E402


def mk_finding(**kw):
    f = Finding(scanner="zap", product="app", title="Reflected XSS",
                severity="high", cwe="CWE-79", endpoint="http://app/search",
                parameter="q", description="xss found", **kw)
    f.kev = True
    f.kev_date = "2021-12-10"
    f.epss_score = 0.95
    f.epss_percentile = 0.99
    f.exploit_available = True
    f.exploit_source = "cisa-kev"
    f.escalation_potential = 0.4
    f.raw = {"scanners": ["zap", "wapiti"]}
    return f


CFG = Config({"products": {"app": {"owner": "appsec-web", "asset_criticality": 8,
                                   "business_impact": 8, "exposure": 9,
                                   "control_effectiveness": 2}}})


class TestPayloads(unittest.TestCase):
    def test_payload_maps_all_intel(self):
        f = mk_finding()
        compute_score(f, CFG.product("app"), CFG.weights)
        f.priority = "P1"
        f.sla_hours = 24
        f.owner = "appsec-web"
        p = finding_to_payload(f, "My App")
        self.assertEqual(p["severity"], "high")
        self.assertEqual(p["cwe"], 79)
        self.assertEqual(p["cve"], None)
        self.assertAlmostEqual(p["cvssv3"], 8.0)
        self.assertEqual(p["epss_score"], 0.95)
        self.assertEqual(p["epss_percentile"], 0.99)
        self.assertTrue(p["known_exploited"])
        self.assertEqual(p["kev_date"], "2021-12-10")
        self.assertEqual(p["endpoint"], "http://app/search")
        self.assertIn("Risk score", p["description"])
        self.assertIn("appsec-web", p["description"])
        self.assertIn("scanner", p["description"].lower())

    def test_cwe_id_parsing(self):
        self.assertEqual(_cwe_id("CWE-79"), 79)
        self.assertEqual(_cwe_id("CWE-200"), 200)
        self.assertIsNone(_cwe_id(None))
        self.assertIsNone(_cwe_id(""))

    def test_url_split(self):
        host, path = _split_url("http://app:3000/search?q=1")
        self.assertEqual(host, "app:3000")
        self.assertEqual(path, "/search")


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = DefectDojoClient(base_url="http://dd.test", api_token="tok")
        self.client.session = unittest.mock.MagicMock()

    def _resp(self, payload, status=200):
        r = unittest.mock.MagicMock()
        r.status_code = status
        r.json.return_value = payload
        r.text = ""
        return r

    def test_upsert_product_creates_when_missing(self):
        self.client.session.request.side_effect = [
            self._resp({"results": []}),            # product lookup
            self._resp({"id": 7}),                  # product type lookup (missing -> create path)
            self._resp({"id": 7}),                  # product type create
            self._resp({"id": 42}),                 # product create
        ]
        prod = self.client.upsert_product("app", prod_type="Research & Development")
        self.assertEqual(prod["id"], 42)
        calls = [c.args for c in self.client.session.request.call_args_list]
        # POSTs go to product_types/ and products/
        self.assertTrue(any("products/" in str(a) for a in calls))
        self.assertTrue(any("product_types/" in str(a) for a in calls))

    def test_push_finding_posts_with_dedup_flags(self):
        payload = {"title": "t", "severity": "high", "description": "d",
                   "cwe": 79, "cve": "CVE-1", "cvssv3": 8.0, "endpoint": "http://h/p",
                   "epss_score": 0.9, "epss_percentile": 0.9,
                   "known_exploited": True, "kev_date": "2021-01-01"}
        self.client.session.request.side_effect = [self._resp({"id": 99})]
        out = self.client.push_finding(test_id=3, payload=payload, product_id=2)
        self.assertEqual(out["id"], 99)
        body = self.client.session.request.call_args_list[-1].kwargs["json"]
        self.assertEqual(body["test"], 3)
        self.assertTrue(body["deduplication_on_engagement"])
        self.assertEqual(body["epss_score"], 0.9)
        self.assertTrue(body["known_exploited"])


if __name__ == "__main__":
    unittest.main()
