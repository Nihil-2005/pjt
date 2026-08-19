"""Ranking: sort active findings into a ticket-ready action list.

Order: score desc, then KEV, then EPSS percentile (explainable tie-breaks).
Each ranked finding gets priority (P1..P4), SLA hours, and an owner from the
product config.
"""
from __future__ import annotations

from typing import Dict, List

from .models import Finding


def rank_findings(findings: List[Finding], config) -> List[Finding]:
    active = [f for f in findings if f.status == "active"]
    active.sort(key=lambda f: (
        f.score if f.score is not None else 0,
        1 if f.kev else 0,
        f.epss_percentile if f.epss_percentile is not None else 0,
    ), reverse=True)

    for i, f in enumerate(active, start=1):
        band = config.sla_for(f.score or 0)
        f.priority = band["priority"]
        f.sla_hours = band["sla_hours"]
        f.owner = config.product(f.product).get("owner", "appsec-team")
        f.score_breakdown["rank"] = i
    return active


def top_action_list(ranked: List[Finding], top_n: int = 25) -> List[Finding]:
    return ranked[:top_n]
