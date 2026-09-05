"""
test_skill_freshness.py
=======================
Every SKILL.md must carry a "Last verified" date, and that date must be
recent. GRC skills embed fast-moving regulatory facts (deadlines, control
counts, adequacy decisions); a skill that hasn't been re-verified within
the review window (120 days ≈ one quarter + buffer) is presumed stale and
must be re-checked against primary sources before release.

The quarterly review process and per-framework source list live in
the maintainer review cadence (monthly whats-new cycle; content re-verification at most every 120 days).

Run with:
    pytest tests/test_skill_freshness.py -v
"""

import re
from datetime import date, timedelta
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
MAX_AGE_DAYS = 120

_LAST_VERIFIED = re.compile(r"\*\*Last verified:\*\*\s*(\d{4})-(\d{2})-(\d{2})")


def _skill_files():
    return sorted(REPO_ROOT.glob("plugins/*/skills/*/SKILL.md"))


@pytest.mark.parametrize("skill_md", _skill_files(), ids=lambda p: p.parent.name)
def test_has_last_verified_date(skill_md: Path):
    """SKILL.md body must contain a '**Last verified:** YYYY-MM-DD' line."""
    m = _LAST_VERIFIED.search(skill_md.read_text())
    assert m, (
        f"{skill_md.parent.name}: no '**Last verified:** YYYY-MM-DD' line found. "
        "Add one directly below the top-level heading."
    )


@pytest.mark.parametrize("skill_md", _skill_files(), ids=lambda p: p.parent.name)
def test_last_verified_is_fresh(skill_md: Path):
    """The Last-verified date must be within MAX_AGE_DAYS of today."""
    m = _LAST_VERIFIED.search(skill_md.read_text())
    if not m:
        pytest.skip("covered by test_has_last_verified_date")
    verified = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    age = (date.today() - verified).days
    assert age <= MAX_AGE_DAYS, (
        f"{skill_md.parent.name}: last verified {verified} ({age} days ago, "
        f"limit {MAX_AGE_DAYS}). Re-verify the skill against primary sources "
        "(re-verify the skill content against primary sources) and update the date."
    )
    assert age >= 0, (
        f"{skill_md.parent.name}: last-verified date {verified} is in the future"
    )


@pytest.mark.parametrize("skill_md", _skill_files(), ids=lambda p: p.parent.name)
def test_no_relative_time_language(skill_md: Path):
    """
    Skill content must use absolute dates, not relative-time phrasing that
    rots ('one month away', 'activates next month'). Deadlines expressed as
    dates stay correct; deadlines expressed relative to an unstated 'now'
    become silently wrong.
    """
    text = skill_md.read_text()
    bad = re.findall(r"(?i)\b(?:one |1 |a )?month[s]? away\b|\bnext month\b|\bnext week\b|\bin a few (?:weeks|months)\b", text)
    assert not bad, (
        f"{skill_md.parent.name}: relative-time phrasing found: {bad}. "
        "Replace with absolute dates."
    )
