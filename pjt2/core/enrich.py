"""Threat-intelligence enrichment.

For every CVE found in the normalized dataset we fetch:

  - CISA KEV      : known-exploited status + date added   (free JSON feed)
  - FIRST.org EPSS: exploit-prediction score + percentile + 7-day trend
                    (public API; trend via the ``date`` query param)
  - NVD           : CVSS v3 fallback when the scanner didn't provide one
  - Exploit-DB    : searchsploit via the exploitdb Docker image (optional;
                    when disabled, CISA KEV doubles as the exploit signal)

All lookups are cached on disk (``cache_dir``) so demo re-runs are instant
and offline after the first run.  ``Fetcher`` is injectable for tests.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

from .models import Finding

USER_AGENT = "vulnlab-risk-pipeline/1.0 (+hackathon)"


class Fetcher:
    """Thin urllib wrapper; tests inject a fake."""

    def get_json(self, url: str, timeout: int = 20) -> Any:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))


def _load_cache(path: str) -> Optional[Any]:
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as fh:
                return json.load(fh)
        except Exception:
            return None
    return None


def _save_cache(path: str, data: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


class Enricher:
    def __init__(self, cfg: Dict, cache_dir: Optional[str] = None, fetcher: Optional[Fetcher] = None):
        self.cfg = cfg
        self.cache_dir = cache_dir or cfg.get("cache_dir", ".threat_cache")
        self.fetcher = fetcher or Fetcher()
        self.kev_map: Dict[str, Dict[str, Any]] = {}
        self.epss_map: Dict[str, Dict[str, Any]] = {}
        self.nvd_map: Dict[str, Dict[str, Any]] = {}
        self.exploit_map: Dict[str, List[str]] = {}
        self.counts: Dict[str, int] = {"kev": 0, "epss": 0, "nvd": 0, "exploit": 0}

    # ------------------------------------------------------------- KEV
    def load_kev(self) -> None:
        cache = os.path.join(self.cache_dir, "kev.json")
        data = _load_cache(cache)
        fresh = False
        if data and (dt.datetime.now() - dt.datetime.fromisoformat(data["fetched"])).days \
                < int(self.cfg.get("cache_ttl_days", 1)):
            self.kev_map = {v["cveID"]: v for v in data["vulnerabilities"]}
            return
        try:
            data = self.fetcher.get_json(self.cfg["kev_url"])
            vulns = data.get("vulnerabilities", [])
            self.kev_map = {v["cveID"]: v for v in vulns}
            _save_cache(cache, {"fetched": dt.datetime.now().isoformat(), "vulnerabilities": vulns})
            fresh = True
        except Exception as exc:
            print(f"  ! KEV fetch failed ({exc}); using cache if present")
            if data:
                self.kev_map = {v["cveID"]: v for v in data["vulnerabilities"]}
        if fresh:
            print(f"  [OK] KEV: {len(self.kev_map)} known-exploited CVEs loaded")

    # ------------------------------------------------------------- EPSS
    def load_epss(self, cves: List[str]) -> None:
        cves = sorted({c.upper() for c in cves if c})
        cache_path = os.path.join(self.cache_dir, "epss.json")
        cache = _load_cache(cache_path) or {}
        # refresh cache if stale
        if (dt.datetime.now() - dt.datetime.fromisoformat(cache.get("fetched", "2000-01-01"))).days \
                >= int(self.cfg.get("cache_ttl_days", 1)):
            cache = {"fetched": dt.datetime.now().isoformat(), "data": {}}
        missing = [c for c in cves if c not in cache["data"]]
        if missing:
            # EPSS API takes one `cve` param with comma-separated IDs
            # (max ~2000 chars) -> chunk so the URL stays under the limit
            for chunk in _chunks(missing, 60):
                try:
                    q = urllib.parse.urlencode({"cve": ",".join(chunk)})
                    data = self.fetcher.get_json(f"{self.cfg['epss_url']}?{q}")
                    for entry in data.get("data", []):
                        cve = entry.get("cve", "").upper()
                        cache["data"][cve] = {
                            "epss": float(entry.get("epss", 0) or 0),
                            "percentile": float(entry.get("percentile", 0) or 0),
                        }
                except Exception as exc:
                    print(f"  ! EPSS fetch failed ({exc}); continuing with cache")
            _save_cache(cache_path, cache)
        self.epss_map = cache.get("data", {})

    def load_epss_trend(self, cves: List[str]) -> None:
        """7-day EPSS delta: + rising / - falling / None when unavailable."""
        past = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=7)).date().isoformat()
        cache_path = os.path.join(self.cache_dir, "epss_trend.json")
        cache = _load_cache(cache_path) or {}
        missing = [c for c in sorted({c.upper() for c in cves if c}) if c not in cache]
        if missing:
            for chunk in _chunks(missing, 60):
                try:
                    q = urllib.parse.urlencode({"cve": ",".join(chunk), "date": past})
                    data = self.fetcher.get_json(f"{self.cfg['epss_url']}?{q}")
                    for entry in data.get("data", []):
                        cache[entry.get("cve", "").upper()] = float(entry.get("epss", 0) or 0)
                except Exception:
                    pass  # trend is best-effort
            _save_cache(cache_path, cache)
        self.trend_map = cache

    # ------------------------------------------------------------- NVD
    def load_nvd(self, cves: List[str]) -> None:
        cache_path = os.path.join(self.cache_dir, "nvd.json")
        cache = _load_cache(cache_path) or {}
        missing = [c for c in sorted({c.upper() for c in cves if c}) if c not in cache]
        for i, cve in enumerate(missing):
            try:
                url = f"{self.cfg['nvd_url']}?cveId={urllib.parse.quote(cve)}"
                data = self.fetcher.get_json(url)
                vulns = data.get("vulnerabilities", [])
                if vulns:
                    metrics = vulns[0].get("cve", {}).get("metrics", {})
                    for key in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
                        if key in metrics and metrics[key]:
                            base = metrics[key][0].get("cvssData", {}).get("baseScore")
                            cache[cve] = {"cvss": base}
                            break
            except Exception:
                pass
            if i % 4 == 3:  # public API: 5 req / 30s
                import time
                time.sleep(6)
        self.nvd_map = cache
        _save_cache(cache_path, cache)

    # ------------------------------------------------------------- Exploit-DB
    def load_exploits(self, cves: List[str], docker_available: bool = True) -> None:
        cache_path = os.path.join(self.cache_dir, "exploits.json")
        cache = _load_cache(cache_path) or {}
        missing = [c for c in sorted({c.upper() for c in cves if c}) if c not in cache]
        for cve in missing:
            try:
                proc = subprocess.run(
                    ["docker", "run", "--rm", "exploitdb/exploitdb:latest",
                     "searchsploit", "--cve", cve, "-j"],
                    capture_output=True, text=True, timeout=120)
                ids = []
                if proc.returncode == 0 and proc.stdout.strip():
                    data = json.loads(proc.stdout)
                    for exp in data.get("RESULTS_EXPLOIT", []):
                        ids.append(str(exp.get("Exploit Unique ID", "")))
                cache[cve] = ids
            except Exception:
                cache[cve] = []
        self.exploit_map = cache
        _save_cache(cache_path, cache)

    # ------------------------------------------------------------- apply
    def enrich(self, findings: List[Finding], use_searchsploit: Optional[bool] = None) -> None:
        use_searchsploit = self.cfg.get("use_searchsploit", False) if use_searchsploit is None \
            else use_searchsploit
        cves = sorted({f.cve.upper() for f in findings if f.cve})
        self.load_kev()
        if cves:
            self.load_epss(cves)
            self.load_epss_trend(cves)
            if self.cfg.get("use_nvd", True):
                # only fetch NVD for CVEs that actually lack a scanner CVSS
                # (NVD is the fallback source; rate-limited to 5 req/30s)
                needs_nvd = {
                    f.cve.upper() for f in findings
                    if f.cve and not _has_scanner_cvss(f)
                }
                needs_nvd = [c for c in sorted(needs_nvd) if c not in self.nvd_map]
                if needs_nvd:
                    self.load_nvd(needs_nvd)
            if use_searchsploit:
                self.load_exploits(cves)

        for f in findings:
            if not f.cve:
                continue
            cve = f.cve.upper()
            kev = self.kev_map.get(cve)
            if kev:
                f.kev = True
                f.kev_date = kev.get("dateAdded")
                self.counts["kev"] += 1
            epss = self.epss_map.get(cve)
            if epss:
                f.epss_score = epss["epss"]
                f.epss_percentile = epss["percentile"]
                self.counts["epss"] += 1
            trend = getattr(self, "trend_map", {}).get(cve)
            if trend is not None and f.epss_score is not None:
                f.epss_trend = round(f.epss_score - trend, 4)
            nvd = self.nvd_map.get(cve)
            if nvd and nvd.get("cvss") is not None:
                f.nvd_cvss = float(nvd["cvss"])
                self.counts["nvd"] += 1
            if use_searchsploit:
                exps = self.exploit_map.get(cve, [])
                if exps:
                    f.exploit_available = True
                    f.exploit_source = "exploit-db:" + ",".join(exps[:3])
                    self.counts["exploit"] += 1
            elif f.kev:
                f.exploit_available = True
                f.exploit_source = "cisa-kev"

    def counts_dict(self) -> Dict[str, int]:
        return dict(self.counts)


def _chunks(items: List[str], size: int) -> List[List[str]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def _has_scanner_cvss(f: Finding) -> bool:
    """True when the scanner report itself carried a CVSS score."""
    cv = f.raw.get("cvss_score") if isinstance(f.raw, dict) else None
    return isinstance(cv, (int, float)) and 0 <= cv <= 10
