"""Shared core engine for the Risk Prioritization & Deduplication pipeline.

This package is version-agnostic: both version1_defectdojo (DefectDojo
substrate) and version2_custom (fully custom substrate) import it.  The core
implements normalize -> dedup -> filter -> enrich -> attack-path -> score ->
rank -> outputs; the two versions only differ in how they persist, display
and ticket the results.
"""

__version__ = "1.0.0"
