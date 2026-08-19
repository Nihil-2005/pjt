"""Unit tests for core/ai_enrich.py.

All Claude API calls are mocked — no real API key needed to run tests.
"""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

from core.models import Finding


# ─────────────────────── fixtures ─────────────────────────────────

def _make_finding(title="XSS in login", severity="high",
                  scanner="zap", cve=None, cwe="CWE-79",
                  score=75.0) -> Finding:
    f = Finding(
        scanner=scanner, product="juice_shop",
        title=title, severity=severity, cwe=cwe, cve=cve,
        description="Reflected XSS on the login endpoint.",
        evidence='<script>alert(1)</script>',
        endpoint="/login",
    )
    f.status = "active"
    f.score = score
    f.score_breakdown = {}
    f.remediation_suggestions = []
    return f


# ─────────────────── _call_claude mock ────────────────────────────

def _mock_claude(system, user, api_key, retries=2):
    """Return plausible JSON depending on the system prompt."""
    if "false-positive" in system.lower() or "fp" in system.lower():
        count = user.count("\n") + 1  # rough finding count
        results = [
            {"fp_probability": 0.1, "fp_reason": "Confirmed by active scanner test."}
        ] * min(count, 10)
        return json.dumps(results)
    if "remediation" in system.lower():
        count = user.count("\n") + 1
        results = [
            "Immediately apply a WAF rule to block the payload pattern. "
            "Fix the root cause by encoding all user-supplied output using contextual escaping."
        ] * min(count, 10)
        return json.dumps(results)
    if "executive" in system.lower() or "ciso" in system.lower():
        return ("The application presents a high-risk posture with multiple "
                "exploitable web vulnerabilities. The most critical finding "
                "is a SQL injection on the login endpoint allowing full "
                "authentication bypass. Immediate action: patch the login "
                "handler and deploy WAF rules before the next business day.")
    return json.dumps([])


# ─────────────────────── tests ────────────────────────────────────

class TestAiEnrich:

    def test_no_api_key_skips_gracefully(self):
        from core import ai_enrich as ai_mod
        findings = [_make_finding()]
        with patch.dict("os.environ", {}, clear=True):
            # Remove both key names from env
            import os
            os.environ.pop("ANTHROPIC_API_KEY", None)
            os.environ.pop("CLAUDE_API_KEY", None)
            result = ai_mod.ai_enrich(findings)
        assert result["used"] is False
        assert result["executive_brief"] == ""
        # Findings untouched
        assert findings[0].score == 75.0

    @patch("core.ai_enrich._call_claude", side_effect=_mock_claude)
    def test_fp_classification_applied(self, mock_call):
        from core import ai_enrich as ai_mod
        findings = [_make_finding()]
        result = ai_mod.ai_enrich(
            findings, api_key="test-key", skip_remediation=True)
        assert result["used"] is True
        assert result["counts"]["fp_classified"] == 1
        assert "ai_fp_probability" in findings[0].score_breakdown
        assert findings[0].score_breakdown["ai_fp_probability"] == 0.1

    @patch("core.ai_enrich._call_claude", side_effect=_mock_claude)
    def test_high_fp_reduces_score(self, mock_call):
        """fp_probability > 0.6 should apply a score penalty."""
        from core import ai_enrich as ai_mod

        def _high_fp_claude(system, user, api_key, retries=2):
            if "false-positive" in system.lower():
                return json.dumps([
                    {"fp_probability": 0.9,
                     "fp_reason": "Scanner-generated noise pattern."}
                ])
            return json.dumps(["some remediation text"])

        findings = [_make_finding(score=70.0)]
        with patch("core.ai_enrich._call_claude",
                   side_effect=_high_fp_claude):
            ai_mod.ai_enrich(findings, api_key="test-key",
                             skip_remediation=True)

        # fp=0.9 → penalty = (0.9 - 0.6) * 25 = 7.5 → score = 70 - 7.5 = 62.5
        assert findings[0].score == pytest.approx(62.5, abs=0.1)
        assert "ai_fp_penalty" in findings[0].score_breakdown

    @patch("core.ai_enrich._call_claude", side_effect=_mock_claude)
    def test_ai_remediation_prepended(self, mock_call):
        from core import ai_enrich as ai_mod
        findings = [_make_finding()]
        ai_mod.ai_enrich(findings, api_key="test-key")
        assert len(findings[0].remediation_suggestions) >= 1
        first = findings[0].remediation_suggestions[0]
        assert first["kind"] == "ai_remediation"
        assert "ai_enrich" in first["source"] or "claude" in first["source"]

    @patch("core.ai_enrich._call_claude", side_effect=_mock_claude)
    def test_executive_brief_generated(self, mock_call):
        from core import ai_enrich as ai_mod
        findings = [_make_finding()]
        result = ai_mod.ai_enrich(
            findings,
            summary_stats={
                "raw_findings": 100, "unique_findings": 60,
                "final_findings": 50,
                "p1": 2, "p2": 5, "p3": 10, "p4": 33,
            },
            api_key="test-key",
        )
        assert len(result["executive_brief"]) > 20

    @patch("core.ai_enrich._call_claude", side_effect=_mock_claude)
    def test_batch_size_respected(self, mock_call):
        """12 findings → at least 2 API calls for FP classification."""
        from core import ai_enrich as ai_mod
        findings = [_make_finding(title=f"Finding {i}") for i in range(12)]
        ai_mod.ai_enrich(findings, api_key="test-key",
                         skip_remediation=True)
        # BATCH_SIZE=10 → 2 FP calls + 1 brief = 3 total
        assert mock_call.call_count >= 2

    @patch("core.ai_enrich._call_claude", side_effect=Exception("network error"))
    def test_api_failure_does_not_crash_pipeline(self, mock_call):
        """If every API call fails, pipeline continues without AI enrichment."""
        from core import ai_enrich as ai_mod
        findings = [_make_finding()]
        result = ai_mod.ai_enrich(findings, api_key="test-key")
        # used=True because api_key was set, but counts are 0
        assert result["counts"]["fp_classified"] == 0
        # Finding score unchanged
        assert findings[0].score == 75.0

    def test_no_active_findings_returns_early(self):
        from core import ai_enrich as ai_mod
        f = _make_finding()
        f.status = "quarantined"
        result = ai_mod.ai_enrich([f], api_key="test-key")
        assert result["used"] is False

    @patch("core.ai_enrich._call_claude", side_effect=_mock_claude)
    def test_remediation_only_top_50(self, mock_call):
        """Only the top 50 by score get AI remediation, not all 60."""
        from core import ai_enrich as ai_mod
        findings = [
            _make_finding(title=f"F{i}", score=float(i))
            for i in range(60)
        ]
        ai_mod.ai_enrich(findings, api_key="test-key")
        remediation_count = sum(
            1 for f in findings
            if any(s["kind"] == "ai_remediation"
                   for s in f.remediation_suggestions)
        )
        assert remediation_count <= 50
