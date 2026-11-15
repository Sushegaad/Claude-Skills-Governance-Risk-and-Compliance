"""
test_structure_guards.py
========================
Regression guards from the November 2026 two-round structural audit
(AUDIT-ROUND2-VERDICTS.md). Each entry is an invented ID, fabricated
structure, or inverted rule that was verified wrong against primary text
and fixed. None may ever reappear in the named skill's source tree.

Patterns are matched case-sensitively as plain substrings unless noted.
Scope is per-skill (plugins/<p>/skills/<p>/**/*.md) so identical strings
that are legitimate in other frameworks are not affected.
"""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent

# plugin -> list of forbidden substrings (verified-wrong content)
FORBIDDEN = {
    "dpdpa": [
        "Limitation for Filing Complaint",      # invented s.31
        "Section 7(e)) for employment",          # employment is 7(i)
        "TLS 1.2",                               # invented Rule 6 spec
        "AES-256",                               # invented Rule 6 spec
        "Section 17(g)",                         # exemptions end at 17(1)(f)/17(2)/(3)
        "Section 10(2)(d)",                      # s.10(2) has (a)-(c) only
    ],
    "vn-pdpl": [
        "Chapter IX",                            # law has 5 chapters
        "Chapter VI",                            # (covers VI/VII/VIII too via VI prefix? no; list each)
        "Chapter VII",
        "Chapter VIII",
    ],
    "dora": [
        "Art. 36 (Recommendations",              # 36 = powers outside the Union
        "Art. 38 (Fees",                         # fees = Art. 43
        "Art. 39 (Rights of defence",
        "EBA Lead for Banking",                  # invented Art. 54 gloss
        "5,000 clients",                         # threshold is 100,000
    ],
    "eu-cra": [
        "35 categories",                         # Class I has 19
        "industrial robots",                     # not in any CRA annex
        "EU database for products with digital elements",  # no such database
    ],
    "cmmc": [
        "17 practices",                          # Level 1 = 15 requirements
        "CMMC-AB",                               # The Cyber AB
        "max score = 17",                        # no L1 numeric score
    ],
    "lgpd": [
        "Protection of credit (LI prohibited",   # credit is Art. 7 X, never Art. 11
        "no adequacy decisions issued",          # Decision (EU) 2026/179 exists
        "Arts. 55-A to 55-L",                    # invented range
    ],
    "iso27701": [
        "A.7.5.5",                               # invented 2019 control
        "Annex A \u2014 28 controls", "Annex A - 28 controls",  # fabricated 2019 count
    ],
    "swift-csp": [
        "1.3A", "1.5A", "2.9A",                  # mandatory controls mis-marked advisory
        "23 mandatory",                          # stale count
    ],
    "tsa-compliance": [
        "Enhancing Surface Transportation Cybersecurity",  # invented NPRM title
        "1580-21-01E", "1582-21-01E",            # fabricated revisions
    ],
    "fedramp": [
        "LMR-GEN",                               # fabricated rule IDs
        "High = 421", "High | 421",              # Rev 4 count
    ],
    "gdpr-compliance": [
        "Senior Responsible Individual (SRI) must be designated",  # dead DPDI provision
    ],
    "saudi-arabia-grc": [
        "Levels 3-4 require in-Kingdom", "Levels 3\u20134 require in-Kingdom",  # repealed CCRF v2 scheme
    ],
    # Guards carried over from issues #62/#63 fix cycles
    "nist-ai-rmf": [
        "GOVERN 3.3", "GOVERN 5.3", "GOVERN 6.3",   # invented subcategories
        "RS.CO-P",                                   # Privacy Framework has no Respond fn
        "AI RMF Implementation Tiers",               # AI 100-1 defines no tiers
    ],
    "iso42001": [
        "A.2.5",                                 # Annex A.2 ends at A.2.4
        "A.10.5",                                # Annex A.10 ends at A.10.4
    ],
    "ear": [
        "ACE — Additional Permissive",           # exception symbol is APR
        "ACE - Additional Permissive",
    ],
    "itar": [
        "Form DV-1",                             # invented; real form is DSP-83
        "DV-1",
    ],
    "section-508": [
        "52.239-2",                              # no such FAR clause
    ],
}


def _skill_files(plugin):
    base = REPO_ROOT / "plugins" / plugin / "skills" / plugin
    return sorted(base.rglob("*.md"))


@pytest.mark.parametrize("plugin", sorted(FORBIDDEN))
def test_no_forbidden_structural_claims(plugin):
    hits = []
    for f in _skill_files(plugin):
        text = f.read_text(encoding="utf-8")
        for pat in FORBIDDEN[plugin]:
            if pat in text:
                hits.append((str(f.relative_to(REPO_ROOT)), pat))
    assert not hits, (
        "Audited-wrong content reappeared (see Claude Docs/AUDIT-ROUND2-"
        f"VERDICTS.md): {hits}")


def test_guard_covers_all_wave1_skills():
    for p in ("dpdpa", "vn-pdpl", "dora", "eu-cra", "cmmc", "lgpd"):
        assert p in FORBIDDEN and _skill_files(p), p
