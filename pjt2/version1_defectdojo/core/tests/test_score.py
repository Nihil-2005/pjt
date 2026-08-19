import unittest

from core.models import Finding
from core.score import compute_score

WEIGHTS = {"cvss": 30, "epss": 15, "kev": 15, "exploit": 10, "asset": 10,
           "business": 10, "exposure": 5, "controls": 5}
PRODUCT = {"asset_criticality": 5, "business_impact": 5, "exposure": 5,
           "control_effectiveness": 3}


def mk(severity="high", cve=None, epss_pct=None, kev=False, exploit=False):
    f = Finding(scanner="trivy", product="app", title="t", severity=severity, cve=cve)
    f.epss_percentile = epss_pct
    f.kev = kev
    f.exploit_available = exploit
    return f


class TestScore(unittest.TestCase):
    def test_kev_medium_outranks_nonkev_high(self):
        """The rubric's 'not raw CVSS alone' test."""
        kev_medium = mk(severity="medium", epss_pct=0.9, kev=True, exploit=True)
        plain_high = mk(severity="high", epss_pct=0.05)
        compute_score(kev_medium, PRODUCT, WEIGHTS)
        compute_score(plain_high, PRODUCT, WEIGHTS)
        self.assertGreater(kev_medium.score, plain_high.score)

    def test_score_in_range_and_explainable(self):
        f = mk(severity="critical", epss_pct=1.0, kev=True, exploit=True)
        bd = compute_score(f, PRODUCT, WEIGHTS)
        self.assertLessEqual(f.score, 100)
        self.assertGreaterEqual(f.score, 0)
        comps = bd["components"]
        self.assertEqual(sum(comps.values()), f.score)
        self.assertIn("CISA KEV", " ".join(bd["drivers"]))

    def test_controls_reduce_score(self):
        f1 = mk(severity="high")
        f2 = mk(severity="high")
        strong = dict(PRODUCT, control_effectiveness=10)
        weak = dict(PRODUCT, control_effectiveness=0)
        compute_score(f1, weak, WEIGHTS)
        compute_score(f2, strong, WEIGHTS)
        self.assertGreater(f1.score, f2.score)

    def test_maximum_components(self):
        f = mk(severity="critical", epss_pct=1.0, kev=True, exploit=True)
        bd = compute_score(f, {k: 10 for k in
                              ("asset_criticality", "business_impact", "exposure",
                               "control_effectiveness")}, WEIGHTS)
        self.assertEqual(bd["components"]["kev"], 15)
        self.assertEqual(bd["components"]["exploit"], 10)


if __name__ == "__main__":
    unittest.main()
