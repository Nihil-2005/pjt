import unittest

from core.config import Config
from core.models import Finding
from core.rank import rank_findings, top_action_list
from core.score import compute_score

CFG = Config({"products": {"app": {"owner": "payments-team", "asset_criticality": 8,
                                   "business_impact": 8, "exposure": 9,
                                   "control_effectiveness": 2}}})


def mk(title, score_seed, kev=False, epss=0.0, status="active", cve=None,
       cvss=None, exploit=False):
    f = Finding(scanner="zap", product="app", title=title, severity="medium",
                status=status, cve=cve, raw={"cvss_score": cvss} if cvss else {})
    f.kev = kev
    f.epss_percentile = epss
    f.exploit_available = exploit
    compute_score(f, CFG.product("app"), CFG.weights)
    return f


class TestRank(unittest.TestCase):
    def test_ordering_and_owner(self):
        low = mk("low", 1, epss=0.01)
        high = mk("high", 1, kev=True, epss=0.99, cve="CVE-2021-44228",
                  cvss=9.8, exploit=True)
        ranked = rank_findings([low, high], CFG)
        self.assertEqual(ranked[0], high)
        self.assertEqual(ranked[0].owner, "payments-team")
        self.assertEqual(ranked[0].priority, "P1")
        self.assertGreater(ranked[0].score, 80)

    def test_sla_bands(self):
        for score, pri, sla in [(85, "P1", 24), (65, "P2", 72), (45, "P3", 168), (10, "P4", 720)]:
            band = CFG.sla_for(score)
            self.assertEqual(band["priority"], pri)
            self.assertEqual(band["sla_hours"], sla)

    def test_quarantined_excluded(self):
        q = mk("q", 1, status="quarantined")
        a = mk("a", 1)
        ranked = rank_findings([q, a], CFG)
        self.assertNotIn(q, ranked)

    def test_top_n(self):
        fs = [mk(f"f{i}", 1) for i in range(30)]
        ranked = rank_findings(fs, CFG)
        self.assertEqual(len(top_action_list(ranked, 25)), 25)


if __name__ == "__main__":
    unittest.main()
