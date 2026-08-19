import unittest

from core.attackpath import build_attack_paths, attach_escalation_potential
from core.models import Finding


def mk(cwe, product="app", severity="high", exploit=False, trend=None):
    f = Finding(scanner="zap", product=product, title=f"{cwe} finding",
                severity=severity, cwe=cwe, endpoint=f"/{cwe}")
    f.exploit_available = exploit
    f.epss_trend = trend
    return f


PRODUCT = {"exposure": 8}


class TestAttackPath(unittest.TestCase):
    def test_chain_detected_between_present_cwes(self):
        fs = [mk("CWE-200"), mk("CWE-287"), mk("CWE-94")]
        paths = build_attack_paths(fs, "app", PRODUCT)
        edges = {(p.from_cwe, p.to_cwe) for p in paths}
        self.assertIn(("CWE-200", "CWE-287"), edges)
        self.assertIn(("CWE-287", "CWE-94"), edges)

    def test_missing_cwe_breaks_chain(self):
        fs = [mk("CWE-200")]  # no CWE-287 -> no chain
        paths = build_attack_paths(fs, "app", PRODUCT)
        self.assertEqual(paths, [])

    def test_probability_bounded_and_boosted(self):
        fs = [mk("CWE-434", exploit=True), mk("CWE-94")]
        paths = build_attack_paths(fs, "app", PRODUCT)
        p = paths[0]
        self.assertLessEqual(p.probability, 0.95)
        # chainability 0.75 * exploit 1.3 * exposure boost > base
        self.assertGreater(p.probability, p.chainability)
        self.assertIn("exploit-available", " ".join(p.factors))

    def test_escalation_potential_attached(self):
        fs = [mk("CWE-200"), mk("CWE-287")]
        paths = build_attack_paths(fs, "app", PRODUCT)
        attach_escalation_potential(fs, paths)
        f200 = next(f for f in fs if f.cwe == "CWE-200")
        self.assertGreater(f200.escalation_potential, 0)
        self.assertLessEqual(f200.escalation_potential, 0.95)


if __name__ == "__main__":
    unittest.main()
