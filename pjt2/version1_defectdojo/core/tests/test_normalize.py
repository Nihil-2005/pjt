import json
import os
import tempfile
import unittest

from core.models import Finding
from core.normalize import (parse_zap, parse_nuclei, parse_wapiti, parse_trivy,
                            parse_report_file, parse_reports_dir)


class TestNormalize(unittest.TestCase):
    def test_zap_parses_alerts(self):
        data = {"site": [{"@name": "http://app:3000", "alerts": [
            {"name": "SQL Injection", "riskdesc": "High (Medium)", "cweid": 89,
             "url": "http://app:3000/login", "param": "user",
             "desc": "SQLi possible", "solution": "Use prepared statements",
             "evidence": "error in response", "reference": "CVE-2021-1234"},
        ]}]}
        fs = parse_zap(data, "juice_shop")
        self.assertEqual(len(fs), 1)
        f = fs[0]
        self.assertEqual(f.scanner, "zap")
        self.assertEqual(f.severity, "high")
        self.assertEqual(f.cwe, "CWE-89")
        self.assertEqual(f.cve, "CVE-2021-1234")
        self.assertEqual(f.endpoint, "http://app:3000/login")
        self.assertEqual(f.parameter, "user")

    def test_nuclei_parses_cve_and_cwe(self):
        data = [{
            "template-id": "cve-2021-44228", "info": {
                "name": "Log4Shell RCE", "severity": "critical",
                "description": "Log4j JNDI injection",
                "classification": {"cve-id": ["CVE-2021-44228"], "cwe-id": ["CWE-502"]},
            },
            "matched-at": "http://app:3000/", "url": "http://app:3000/",
        }]
        fs = parse_nuclei(data, "juice_shop")
        self.assertEqual(len(fs), 1)
        f = fs[0]
        self.assertEqual(f.severity, "critical")
        self.assertEqual(f.cve, "CVE-2021-44228")
        self.assertEqual(f.cwe, "CWE-502")
        self.assertEqual(f.endpoint, "http://app:3000/")

    def test_wapiti_parses_levels_and_solutions(self):
        data = {
            "vulnerabilities": {"SQL Injection": [{
                "level": 2, "path": "/products?id=1", "parameter": "id",
                "info": "SQLi in id param"}]},
            "classifications": {"SQL Injection": {
                "desc": "SQLi", "sol": "Use parameterized queries",
                "ref": {"CWE-89: SQL Injection": "https://cwe.mitre.org/89"}}},
        }
        fs = parse_wapiti(data, "bwapp")
        self.assertEqual(len(fs), 1)
        f = fs[0]
        self.assertEqual(f.severity, "medium")
        self.assertEqual(f.cwe, "CWE-89")
        self.assertIn("parameterized queries", f.remediation)
        self.assertEqual(f.parameter, "id")

    def test_trivy_parses_cve_and_fixed_version(self):
        data = {"Results": [{"Target": "juice-shop:latest (node 20.x)",
                             "Vulnerabilities": [{
                                 "VulnerabilityID": "CVE-2021-44228",
                                 "Severity": "CRITICAL", "PkgName": "log4j-core",
                                 "InstalledVersion": "2.14.0", "FixedVersion": "2.17.1",
                                 "Title": "Log4Shell", "Description": "JNDI RCE",
                                 "CVSS": {"nvd": {"v3": {"V3Score": 10.0}}}}]}]}
        fs = parse_trivy(data, "nodegoat")
        self.assertEqual(len(fs), 1)
        f = fs[0]
        self.assertEqual(f.cve, "CVE-2021-44228")
        self.assertEqual(f.fixed_version, "2.17.1")
        self.assertIn("2.17.1", f.remediation)
        self.assertEqual(f.raw["cvss_score"], 10.0)

    def test_report_file_dispatch_and_dir(self):
        with tempfile.TemporaryDirectory() as td:
            zap = {"site": [{"@name": "http://x", "alerts": [
                {"name": "A", "riskdesc": "Medium", "url": "http://x/"}]}]}
            with open(os.path.join(td, "app_zap.json"), "w") as fh:
                json.dump(zap, fh)
            fs = parse_report_file(os.path.join(td, "app_zap.json"), "app")
            self.assertEqual(fs[0].scanner, "zap")
            fs2 = parse_reports_dir(td, product_names=["app"])
            self.assertEqual(len(fs2), 1)

    def test_nmap_xml(self):
        from core.normalize import parse_nmap_xml
        xml = ('<nmaprun><host><address addr="10.0.0.5"/>'
               '<ports><port portid="22" protocol="tcp"><state state="open"/>'
               '<service name="ssh"/></port></ports></host></nmaprun>')
        fs = parse_nmap_xml(xml, "app")
        self.assertEqual(len(fs), 1)
        self.assertEqual(fs[0].endpoint, "10.0.0.5:22")


if __name__ == "__main__":
    unittest.main()
