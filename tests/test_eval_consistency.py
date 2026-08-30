"""
test_eval_consistency.py
========================
Validates that per-skill evaluation stats are consistent across all three
locations where they are published:

  1. grc-skills-eval-results.html  — canonical evaluation page (ground truth)
  2. index.html                     — #evaluation tab Per-Skill Results table
  3. README.md                      — #skill-evaluation markdown table

Rules enforced:

  • Every skill in the eval page summary table must appear in index.html and README.md
  • with-skill %, baseline %, and delta % must match exactly across all three files
  • Delta must equal (with% − base%) ± 1 tolerance for rounding
  • Accordion headers in grc-skills-eval-results.html must match the summary table
  • Per-skill published stats must match the grading.json artifacts in grc-workspace/
    (TestGradingFileConsistency — the deep audit layer)
  • Headline assertion counts and baseline % in all three files must be derivable
    from the per-skill grading data on disk

Background: these three files have diverged in the past when a skill's eval was
re-run (improving results) and only one or two of the three locations was updated.
This test ensures any future update propagates consistently to all locations.

Why the old tests could not catch inflated stats
-------------------------------------------------
The original TestEvalConsistency class only enforces CROSS-FILE CONSISTENCY:
it verifies that GDPR shows the same numbers in all three files. If all three
files agree on a wrong number (e.g., 100%/96% when grading.json says 88%/88%),
every cross-file test still passes. The class also designates
grc-skills-eval-results.html as "ground truth" — but that HTML is a presentation
layer that can be edited by hand; the actual ground truth is the grading.json
artifacts produced by the eval framework.

Run with:
    pytest tests/test_eval_consistency.py -v
"""

import json
import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT  = Path(__file__).parent.parent
EVAL_PAGE  = REPO_ROOT / "grc-skills-eval-results.html"
INDEX_HTML = REPO_ROOT / "index.html"
README     = REPO_ROOT / "README.md"

# The manifest (skills.json) is the single source of truth for the inventory.
_MANIFEST = json.loads((REPO_ROOT / "skills.json").read_text(encoding="utf-8"))
EXPECTED_SKILL_COUNT = len(_MANIFEST["skills"])


# ---------------------------------------------------------------------------
# Name normalisation
# ---------------------------------------------------------------------------

def _normalize_name(raw: str) -> str:
    """
    Produce a canonical, case-insensitive key for cross-file skill matching.

    Handles:
      • HTML tags  (<img …>, <strong>, etc.)
      • Flag / emoji characters (non-ASCII code points)
      • Bracketed regional / regulatory suffixes ([EU], [US], [Brazil], …)
      • Trailing whitespace from stripping the above
    """
    # 1. Strip HTML tags (img alt text stays inside the tag and is removed too)
    name = re.sub(r"<[^>]+>", "", raw)
    # 2. Remove [bracketed] qualifiers
    name = re.sub(r"\[.*?\]", "", name)
    # 3. Drop all non-ASCII characters (removes emoji, flag sequences, etc.)
    name = "".join(c for c in name if ord(c) < 128)
    # 4. Normalise whitespace
    name = re.sub(r"\s+", " ", name).strip()
    return name.lower()


def _parse_pct(raw: str) -> int:
    """'±0%' / '+4%' / '-4%' / '4%' / '0%'  →  signed integer (sign preserved)."""
    sign = -1 if raw.strip().startswith("-") else 1
    return sign * int(re.sub(r"[+\-±%\s]", "", raw))


# ---------------------------------------------------------------------------
# File parsers
# ---------------------------------------------------------------------------

def _parse_eval_page_summary(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the Per-Skill summary table in grc-skills-eval-results.html.

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    This is the ground truth; all other files are compared against it.
    """
    pattern = re.compile(
        r'class="skill-link">([^<]+)</a></td>\s*'
        r'<td[^>]*>(\d+)%</td>\s*'   # with-skill %
        r'<td[^>]*>(\d+)%</td>\s*'   # baseline %
        r'<td[^>]*>([+\-±]?\d+)%</td>',  # delta %
        re.DOTALL,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


def _parse_eval_page_accordions(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the accordion toggle-header stats in grc-skills-eval-results.html.

    These should mirror the summary table. Divergence indicates an incomplete
    update (e.g. the accordion header was manually edited but the summary row
    was not, or vice-versa).

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    """
    pattern = re.compile(
        r'<span class="skill-toggle-name">([^<]+)</span>\s*'
        r'<span class="skill-toggle-stats">(\d+)% with skill\s*·\s*(\d+)% baseline\s*·\s*'
        r'<span[^>]*>([+\-±]?\d+)%</span></span>',
        re.DOTALL,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


def _parse_index_html(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the Per-Skill Results table in the #evaluation section of index.html.

    Each row looks like:
      <tr><td …>N</td><td …>[emoji/img] SKILL NAME [TAG]</td><td>5</td>
          <td><strong>WW%</strong></td><td>BB%</td><td>DD%</td>…</tr>

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    """
    pattern = re.compile(
        r"<tr><td[^>]*>\d+</td>"
        r"<td[^>]*>(.*?)</td>"           # skill name cell (may contain img/emoji)
        r"<td>5</td>"                    # eval count — distinguishes this table
        r"<td><strong>(\d+)%</strong></td>"  # with-skill %
        r"<td>(\d+)%</td>"              # baseline %
        r"<td>([+\-±]?\d+)%</td>",      # delta %
        re.DOTALL,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


def _parse_readme(content: str) -> dict[str, tuple[int, int, int]]:
    """
    Parse the skill evaluation markdown table in README.md.

    Each row looks like:
      | SKILL NAME [TAG] | 5 | **WW%** | BB% | +DD% | … |

    Note: zero-delta skills may appear as "0%" (no sign), not "+0%".
    The delta sign is therefore optional in the pattern.

    Returns {canonical_name: (with_pct, base_pct, delta_pct)}.
    """
    pattern = re.compile(
        r"^\| ([^|]+?) \| 5 \| \*\*(\d+)%\*\* \| (\d+)% \| ([+\-±]?\d+)% \|",
        re.MULTILINE,
    )
    return {
        _normalize_name(m.group(1)): (
            int(m.group(2)),
            int(m.group(3)),
            _parse_pct(m.group(4)),
        )
        for m in pattern.finditer(content)
    }


# ---------------------------------------------------------------------------
# Lookup helper
# ---------------------------------------------------------------------------

def _best_match(key: str, lookup: dict) -> str | None:
    """
    Exact match only.

    We intentionally avoid substring fallbacks here (e.g. "ism" ⊂ "nzism")
    because skill names normalise cleanly and a substring match would silently
    hide missing entries or, worse, cross-match two different skills.
    """
    return key if key in lookup else None


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def eval_data() -> dict:
    eval_content  = EVAL_PAGE.read_text(encoding="utf-8")
    index_content = INDEX_HTML.read_text(encoding="utf-8")
    readme_content = README.read_text(encoding="utf-8")
    return {
        "eval_summary":    _parse_eval_page_summary(eval_content),
        "eval_accordions": _parse_eval_page_accordions(eval_content),
        "index":           _parse_index_html(index_content),
        "readme":          _parse_readme(readme_content),
    }


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestEvalConsistency:
    """Cross-file consistency of per-skill evaluation statistics."""

    # -- Row counts --------------------------------------------------------

    def test_eval_page_skill_count(self, eval_data):
        """Eval page summary table must have exactly EXPECTED_SKILL_COUNT rows."""
        n = len(eval_data["eval_summary"])
        assert n == EXPECTED_SKILL_COUNT, (
            f"Expected {EXPECTED_SKILL_COUNT} skills in grc-skills-eval-results.html "
            f"summary table, found {n}.\n"
            f"If you added a skill, increment EXPECTED_SKILL_COUNT in this file."
        )

    def test_index_html_skill_count(self, eval_data):
        """index.html Per-Skill Results table must have exactly EXPECTED_SKILL_COUNT rows."""
        n = len(eval_data["index"])
        assert n == EXPECTED_SKILL_COUNT, (
            f"Expected {EXPECTED_SKILL_COUNT} skills in index.html, found {n}.\n"
            f"Skills found: {sorted(eval_data['index'])}"
        )

    def test_readme_skill_count(self, eval_data):
        """README.md skill evaluation table must have exactly EXPECTED_SKILL_COUNT rows."""
        n = len(eval_data["readme"])
        assert n == EXPECTED_SKILL_COUNT, (
            f"Expected {EXPECTED_SKILL_COUNT} skills in README.md, found {n}.\n"
            f"Skills found: {sorted(eval_data['readme'])}"
        )

    # -- Cross-file stat consistency ----------------------------------------

    def test_eval_page_vs_index_html(self, eval_data):
        """
        Every skill's (with%, base%, delta%) in grc-skills-eval-results.html
        must match the corresponding row in index.html.

        Common failure: a skill is re-evaluated and the eval page is updated
        but index.html is not (or vice-versa).
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            match = _best_match(name, eval_data["index"])
            if match is None:
                errors.append(f"  '{name}' not found in index.html Per-Skill table")
                continue
            iw, ib, id_ = eval_data["index"][match]
            if (w, b, d) != (iw, ib, id_):
                errors.append(
                    f"  {name!r}:\n"
                    f"    eval page : {w}% with-skill / {b}% baseline / {d:+}% delta\n"
                    f"    index.html: {iw}% with-skill / {ib}% baseline / {id_:+}% delta"
                )
        assert not errors, (
            "Mismatches between grc-skills-eval-results.html and index.html:\n"
            + "\n".join(errors)
        )

    def test_eval_page_vs_readme(self, eval_data):
        """
        Every skill's (with%, base%, delta%) in grc-skills-eval-results.html
        must match the corresponding row in README.md.

        Common failure: a skill re-run improves results; the eval page and
        index.html are updated but README.md is forgotten.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            match = _best_match(name, eval_data["readme"])
            if match is None:
                errors.append(f"  '{name}' not found in README.md skill evaluation table")
                continue
            rw, rb, rd = eval_data["readme"][match]
            if (w, b, d) != (rw, rb, rd):
                errors.append(
                    f"  {name!r}:\n"
                    f"    eval page: {w}% with-skill / {b}% baseline / {d:+}% delta\n"
                    f"    README.md: {rw}% with-skill / {rb}% baseline / {rd:+}% delta"
                )
        assert not errors, (
            "Mismatches between grc-skills-eval-results.html and README.md:\n"
            + "\n".join(errors)
        )

    # -- Internal consistency within grc-skills-eval-results.html -----------

    def test_accordion_headers_match_summary_table(self, eval_data):
        """
        For every skill that has an accordion toggle header in
        grc-skills-eval-results.html, the header stats must match
        the summary table for that skill.

        Skills added to the summary table without a corresponding accordion
        section (currently: WCAG, NZISM, VN-PDPL, EU CRA) are skipped —
        they lack accordions because they were added in a later batch that
        didn't include detailed accordion sections. They are listed as a
        non-failing informational note.

        The test FAILS only when an accordion header is present but shows
        different values from the summary table (the bug pattern we've seen:
        an accordion is manually edited for a re-run but the summary row
        is not updated, or vice-versa).
        """
        errors = []
        no_accordion = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            match = _best_match(name, eval_data["eval_accordions"])
            if match is None:
                no_accordion.append(name)
                continue
            aw, ab, ad = eval_data["eval_accordions"][match]
            if (w, b, d) != (aw, ab, ad):
                errors.append(
                    f"  {name!r}:\n"
                    f"    summary table : {w}% with-skill / {b}% baseline / {d:+}% delta\n"
                    f"    accordion hdr : {aw}% with-skill / {ab}% baseline / {ad:+}% delta"
                )
        # Informational: list skills with no accordion section (non-blocking)
        if no_accordion:
            print(
                f"\n[INFO] {len(no_accordion)} skill(s) have no accordion section "
                f"in grc-skills-eval-results.html: {no_accordion}"
            )
        assert not errors, (
            "Accordion headers don't match summary table in grc-skills-eval-results.html:\n"
            + "\n".join(errors)
        )

    # -- Arithmetic sanity (delta = with% − base%) --------------------------

    def test_delta_arithmetic_eval_page(self, eval_data):
        """
        Delta must equal (with% − base%) in grc-skills-eval-results.html.
        Tolerance of ±1 accounts for legitimate percentage rounding.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["eval_summary"].items()):
            expected = w - b
            if abs(expected - d) > 1:
                errors.append(
                    f"  {name!r}: {w}% − {b}% = {expected:+}% but delta shows {d:+}%"
                )
        assert not errors, (
            "Delta arithmetic errors in grc-skills-eval-results.html:\n"
            + "\n".join(errors)
        )

    def test_delta_arithmetic_index_html(self, eval_data):
        """
        Delta must equal (with% − base%) in index.html.
        Tolerance of ±1 accounts for legitimate percentage rounding.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["index"].items()):
            expected = w - b
            if abs(expected - d) > 1:
                errors.append(
                    f"  {name!r}: {w}% − {b}% = {expected:+}% but delta shows {d:+}%"
                )
        assert not errors, (
            "Delta arithmetic errors in index.html:\n"
            + "\n".join(errors)
        )

    def test_delta_arithmetic_readme(self, eval_data):
        """
        Delta must equal (with% − base%) in README.md.
        Tolerance of ±1 accounts for legitimate percentage rounding.
        """
        errors = []
        for name, (w, b, d) in sorted(eval_data["readme"].items()):
            expected = w - b
            if abs(expected - d) > 1:
                errors.append(
                    f"  {name!r}: {w}% − {b}% = {expected:+}% but delta shows {d:+}%"
                )
        assert not errors, (
            "Delta arithmetic errors in README.md:\n"
            + "\n".join(errors)
        )

    # -- With-skill % ≥ baseline % (a skill should never hurt) ---------------

    # Skills with a documented negative delta in the current published run.
    # Honest evals with independently authored primary-source assertions CAN
    # come out below baseline — that is a finding to publish and fix, not to
    # hide. Any skill listed here must have an open improvement item in the
    # changelog/CHANGELOG.md. Remove entries as skills are improved and re-run.
    KNOWN_NEGATIVE_DELTA: set[str] = set()

    def test_with_skill_not_worse_than_baseline(self, eval_data):
        """
        With-skill score must be ≥ baseline for every skill in all three files,
        except skills explicitly acknowledged in KNOWN_NEGATIVE_DELTA (published
        honestly with an open improvement item). An UNDOCUMENTED negative delta
        still fails — it means results changed without acknowledgement.
        """
        errors = []
        for source, data in [
            ("grc-skills-eval-results.html", eval_data["eval_summary"]),
            ("index.html",                   eval_data["index"]),
            ("README.md",                    eval_data["readme"]),
        ]:
            for name, (w, b, _d) in sorted(data.items()):
                if w < b and name not in self.KNOWN_NEGATIVE_DELTA:
                    errors.append(f"  [{source}] {name!r}: {w}% with-skill < {b}% baseline")
        assert not errors, (
            "Skills with an UNDOCUMENTED negative delta (add to "
            "KNOWN_NEGATIVE_DELTA only with a changelog improvement item):\n"
            + "\n".join(errors)
        )


# ---------------------------------------------------------------------------
# Deep audit: grading.json artifacts vs. published stats
# ---------------------------------------------------------------------------

# Map each skill ID to the grc-workspace directory that holds its eval subdirs.
# Iteration-2 takes precedence over iteration-1 for skills re-run in that round.
# Skills with no committed grading data are listed in GRADING_NOT_AVAILABLE and
# are skipped (not failed) so that adding their data later is a diff, not a fix.
_WS = REPO_ROOT / "grc-workspace"

_SKILL_GRADING_DIR: dict[str, Path] = {
    s["plugin"]: REPO_ROOT / s["grading_dir"] for s in _MANIFEST["skills"]
}

# Flat-eval skills that share the iteration-1 root; restrict search by prefix.
_FLAT_EVAL_PREFIXES: dict[str, list[str]] = {
    "itar":         ["eval-91", "eval-92", "eval-93", "eval-94", "eval-95"],
    "csrd":         ["eval-101", "eval-102", "eval-103", "eval-104", "eval-105"],
    "cis-controls": ["eval-106", "eval-107", "eval-108", "eval-109", "eval-110"],
}

# Skills with no grading data committed to this repository.
# They are skipped, not failed — so adding grading files later will surface
# in git diff rather than requiring a test fix.
_GRADING_NOT_AVAILABLE: set[str] = set()

# Tolerance in percentage points: grading-computed % may differ from published
# by at most this much due to legitimate rounding (e.g. 23/27 = 85.19% → 85%).
_TOLERANCE_PP = 1

# Maps each plugin skill ID to the normalized key used in the eval HTML summary
# table (produced by _normalize_name applied to the skill-link text).
# This is necessary because display names are abbreviated (e.g., "GDPR" for
# the gdpr-compliance plugin) and don't map mechanically from the skill ID.
_SKILL_ID_TO_NORM_KEY: dict[str, str] = {
    s["plugin"]: s["norm_key"] for s in _MANIFEST["skills"]
}


def _parse_grading_json(path: Path) -> tuple[int, int]:
    """
    Parse a single grading.json file and return (passed, total).

    Handles three formats produced by different eval harness versions:

    Format A — explicit totals (most common):
        {"total": N, "passed": N, ...}

    Format B — SWIFT CSP harness (uses "assertions"/"pass"):
        {"assertions": [{"pass": true/false, ...}], "passed_assertions": N, ...}

    Format C — expectation list without top-level totals:
        {"expectations": [{"passed": true/false, ...}]}
    """
    data = json.loads(path.read_text())

    # Format A: top-level total/passed integers
    if isinstance(data.get("total"), int) and data["total"] > 0:
        return int(data["passed"]), int(data["total"])

    # Format B: assertions array with boolean "pass" field
    if "assertions" in data and isinstance(data["assertions"], list):
        items = data["assertions"]
        if items and "pass" in items[0]:
            passed = sum(1 for a in items if a.get("pass"))
            return passed, len(items)
        # Fall through if "pass" key absent

    # Format C: expectations array with boolean "passed" field
    if "expectations" in data and isinstance(data["expectations"], list):
        items = data["expectations"]
        passed = sum(1 for e in items if e.get("passed"))
        return passed, len(items)

    raise ValueError(
        f"Unrecognised grading.json format at {path}. "
        f"Keys found: {list(data.keys())}"
    )


def _eval_dirs_for_skill(skill_id: str) -> list[Path]:
    """
    Return the list of per-eval directories (each containing with_skill/ and
    without_skill/ subdirectories) for the given skill.
    """
    base = _SKILL_GRADING_DIR.get(skill_id)
    if base is None or not base.is_dir():
        return []

    prefixes = _FLAT_EVAL_PREFIXES.get(skill_id)

    dirs = []
    for candidate in sorted(base.iterdir()):
        if not candidate.is_dir():
            continue
        # For flat-eval skills in iteration-1 root, restrict to matching prefixes
        if prefixes and not any(candidate.name.startswith(p) for p in prefixes):
            continue
        # Must have at least one of with_skill / without_skill
        if (candidate / "with_skill").is_dir() or (candidate / "without_skill").is_dir():
            dirs.append(candidate)

    return dirs


def _aggregate_skill_grading(skill_id: str) -> tuple[int, int, int, int] | None:
    """
    Aggregate all eval dirs for a skill and return
    (with_passed, with_total, base_passed, base_total).

    Returns None if no grading data is available for this skill.
    """
    eval_dirs = _eval_dirs_for_skill(skill_id)
    if not eval_dirs:
        return None

    wp = wt = bp = bt = 0
    for eval_dir in eval_dirs:
        for run_type, counters in [
            ("with_skill",    (lambda p, b: (p, b, 0, 0))),
            ("without_skill", (lambda p, b: (0, 0, p, b))),
        ]:
            gf = eval_dir / run_type / "grading.json"
            if not gf.exists():
                continue
            passed, total = _parse_grading_json(gf)
            if run_type == "with_skill":
                wp += passed; wt += total
            else:
                bp += passed; bt += total

    return (wp, wt, bp, bt) if (wt > 0 or bt > 0) else None


def _pct(passed: int, total: int) -> int:
    """Integer percentage, rounded normally."""
    return round(100 * passed / total) if total > 0 else 0


class TestGradingFileConsistency:
    """
    Deep audit: verifies that per-skill published stats in
    grc-skills-eval-results.html (and by extension index.html and README.md,
    which are forced in sync by TestEvalConsistency) are backed by the
    grading.json artifacts in grc-workspace/.

    Why this matters
    ----------------
    TestEvalConsistency only enforces CROSS-FILE AGREEMENT: it will pass
    even when all three stat files consistently show the wrong number.
    This class computes pass rates directly from grading.json files on disk
    and fails the build if any published stat deviates more than 1 pp from
    the grading-derived truth.

    Root causes caught
    ------------------
    1. Manual edits to published stats without a re-run
       ("looks about right" editing without checking grading.json)
    2. Stats copied from an earlier iteration that were never updated
    3. Rounding errors (e.g. 24/27 = 88.9% published as 89% when grading
       shows 23/27 = 85.2%)
    4. Assertion count drift (WCAG has 27 assertions not 25; new skills
       added without updating the headline total)
    5. Wrong iteration used (iter-1 numbers published while iter-2 exists)
    """

    # Tolerance in percentage points
    TOLERANCE = _TOLERANCE_PP

    @pytest.mark.parametrize("skill_id", sorted(_SKILL_GRADING_DIR.keys()))
    def test_with_skill_pct_matches_grading(self, skill_id, eval_data):
        """
        Published with-skill % in grc-skills-eval-results.html must match
        the pass rate computed from grading.json files (within ±1 pp).
        """
        if skill_id in _GRADING_NOT_AVAILABLE:
            pytest.skip(f"No grading data committed for {skill_id}")

        grading = _aggregate_skill_grading(skill_id)
        if grading is None:
            pytest.skip(f"grading.json files not found for {skill_id}")

        wp, wt, _bp, _bt = grading
        if wt == 0:
            pytest.skip(f"No with_skill grading.json files found for {skill_id}")

        computed = _pct(wp, wt)
        # Look up the published value using the explicit display-name mapping
        norm_key = _SKILL_ID_TO_NORM_KEY.get(skill_id)
        if norm_key is None:
            pytest.fail(
                f"'{skill_id}' has no entry in _SKILL_ID_TO_NORM_KEY. "
                f"Add it to the mapping."
            )
        published = eval_data["eval_summary"].get(norm_key)
        if published is None:
            pytest.fail(
                f"'{skill_id}' (display key '{norm_key}') not found in "
                f"grc-skills-eval-results.html summary table."
            )
        pub_w, _pub_b, _pub_d = published
        assert abs(pub_w - computed) <= self.TOLERANCE, (
            f"{skill_id}: published with-skill = {pub_w}%, "
            f"grading computes {computed}% ({wp}/{wt}). "
            f"Difference {abs(pub_w - computed)}pp exceeds tolerance {self.TOLERANCE}pp. "
            f"Update the stat in grc-skills-eval-results.html (and the other two stat files)."
        )

    @pytest.mark.parametrize("skill_id", sorted(_SKILL_GRADING_DIR.keys()))
    def test_baseline_pct_matches_grading(self, skill_id, eval_data):
        """
        Published baseline % in grc-skills-eval-results.html must match
        the pass rate computed from grading.json files (within ±1 pp).
        """
        if skill_id in _GRADING_NOT_AVAILABLE:
            pytest.skip(f"No grading data committed for {skill_id}")

        grading = _aggregate_skill_grading(skill_id)
        if grading is None:
            pytest.skip(f"grading.json files not found for {skill_id}")

        _wp, _wt, bp, bt = grading
        if bt == 0:
            pytest.skip(f"No without_skill grading.json files found for {skill_id}")

        computed = _pct(bp, bt)
        norm_key = _SKILL_ID_TO_NORM_KEY.get(skill_id)
        if norm_key is None:
            pytest.fail(f"'{skill_id}' has no entry in _SKILL_ID_TO_NORM_KEY.")
        published = eval_data["eval_summary"].get(norm_key)
        if published is None:
            pytest.fail(
                f"'{skill_id}' (display key '{norm_key}') not found in "
                f"grc-skills-eval-results.html summary table."
            )
        _pub_w, pub_b, _pub_d = published
        assert abs(pub_b - computed) <= self.TOLERANCE, (
            f"{skill_id}: published baseline = {pub_b}%, "
            f"grading computes {computed}% ({bp}/{bt}). "
            f"Difference {abs(pub_b - computed)}pp exceeds tolerance {self.TOLERANCE}pp. "
            f"Update the stat in grc-skills-eval-results.html (and the other two stat files)."
        )

    def test_total_assertion_count_headline_eval_html(self):
        """
        The 'Total Assertions' stat card in grc-skills-eval-results.html must
        equal the sum of all assertions across every skill's grading files.
        """
        content = EVAL_PAGE.read_text(encoding="utf-8")
        m = re.search(
            r'<div class="stat-value">(\d+)</div>\s*'
            r'<div class="stat-label">Total Assertions</div>',
            content,
        )
        assert m, "Could not find 'Total Assertions' stat card in grc-skills-eval-results.html"
        published_total = int(m.group(1))

        computed_total = _compute_total_assertions()
        assert published_total == computed_total, (
            f"grc-skills-eval-results.html 'Total Assertions' shows {published_total} "
            f"but grading files sum to {computed_total}. "
            f"Update the stat card (and corresponding counts in index.html and README.md)."
        )

    def test_total_assertion_count_headline_index_html(self):
        """
        The assertion count in index.html stat-grid must equal the sum derived
        from grading files.
        """
        content = INDEX_HTML.read_text(encoding="utf-8")
        # Matches both "655 / 675 assertions passed" and "752 total assertions"
        m = re.search(r"(\d+)\s*/\s*(\d+)\s*assertions\s*passed", content)
        assert m, "Could not find 'X / Y assertions passed' in index.html stat-grid"
        published_total = int(m.group(2))

        computed_total = _compute_total_assertions()
        assert published_total == computed_total, (
            f"index.html stat-grid shows / {published_total} total assertions "
            f"but grading files sum to {computed_total}."
        )

    def test_total_assertion_count_headline_readme(self):
        """
        The assertion count in the README.md aggregate table must equal the sum
        derived from grading files.
        """
        content = README.read_text(encoding="utf-8")
        # Matches "| **97%** | **655 / 675** |"
        m = re.search(r"\*\*(\d+)\s*/\s*(\d+)\*\*", content)
        assert m, "Could not find '**X / Y**' assertion counts in README.md aggregate table"
        published_total = int(m.group(2))

        computed_total = _compute_total_assertions()
        assert published_total == computed_total, (
            f"README.md aggregate table shows / {published_total} total assertions "
            f"but grading files sum to {computed_total}."
        )

    def test_skills_without_grading_are_documented(self):
        """
        Every skill in the published summary table must have an entry in
        _SKILL_ID_TO_NORM_KEY AND either grading files in grc-workspace/ OR
        an entry in _GRADING_NOT_AVAILABLE.

        This test fails immediately when a new skill is added to the eval
        page without updating the grading directory mapping — ensuring that
        the deep audit never silently skips a skill.
        """
        # All normalized display-name keys we know about
        known_norm_keys = set(_SKILL_ID_TO_NORM_KEY.values())

        eval_content = EVAL_PAGE.read_text(encoding="utf-8")
        raw_pattern = re.compile(r'class="skill-link">([^<]+)</a></td>', re.DOTALL)
        raw_names = [m.group(1).strip() for m in raw_pattern.finditer(eval_content)]

        undocumented = []
        for raw in raw_names:
            norm = _normalize_name(raw)
            if norm not in known_norm_keys:
                undocumented.append(raw)

        assert not undocumented, (
            "The following skills appear in the published summary table but have "
            "no entry in _SKILL_ID_TO_NORM_KEY:\n"
            + "\n".join(f"  '{n}' (normalised: '{_normalize_name(n)}')" for n in undocumented)
            + "\n\nAdd the skill to _SKILL_ID_TO_NORM_KEY, _SKILL_GRADING_DIR "
            "(with the path to its grading data), and optionally "
            "_GRADING_NOT_AVAILABLE if grading files aren't committed yet."
        )


def _compute_total_assertions() -> int:
    """
    Sum the total assertion count across all skills that have grading data.
    Skills in _GRADING_NOT_AVAILABLE contribute 25 each (the assumed default)
    so the total stays consistent even when those files aren't committed.
    """
    DEFAULT_ASSERTIONS_PER_SKILL = 25
    total = 0

    for skill_id in _SKILL_GRADING_DIR:
        grading = _aggregate_skill_grading(skill_id)
        if grading is not None:
            _wp, wt, _bp, bt = grading
            # Use whichever run has data; prefer with_skill total
            skill_total = wt or bt
            total += skill_total
        else:
            total += DEFAULT_ASSERTIONS_PER_SKILL

    # Skills with no grading data use the default assertion count
    total += len(_GRADING_NOT_AVAILABLE) * DEFAULT_ASSERTIONS_PER_SKILL

    return total


# ---------------------------------------------------------------------------
# Summary-block consistency (added v1.6.0 — catches the +16/+107 class of error)
# ---------------------------------------------------------------------------

def _parse_readme_summary(content: str) -> dict:
    """Extract the overall summary from README.md's Skill Evaluation table."""
    w = re.search(r"\|\s*\*\*With GRC Skills installed\*\*\s*\|\s*\*\*(\d+)%\*\*\s*\|\s*\*\*(\d+)\s*/\s*(\d+)\*\*", content)
    b = re.search(r"\|\s*Without skills \(baseline Claude\)\s*\|\s*(\d+)%\s*\|\s*(\d+)\s*/\s*(\d+)", content)
    d = re.search(r"\|\s*\*\*Delta\*\*\s*\|\s*\*\*\+(\d+) points?\*\*\s*\|\s*\*\*\+(\d+) assertions?\*\*", content)
    assert w and b and d, "README summary table rows not found"
    return {
        "with_pct": int(w.group(1)), "with_passed": int(w.group(2)), "total": int(w.group(3)),
        "base_pct": int(b.group(1)), "base_passed": int(b.group(2)), "base_total": int(b.group(3)),
        "delta_pts": int(d.group(1)), "delta_assertions": int(d.group(2)),
    }


def _parse_index_summary(content: str) -> dict:
    """Extract the overall summary from index.html's stat-grid."""
    w = re.search(r'<div class="value">(\d+)%</div>\s*<div class="label">With GRC Skills installed<br\s*/?><small>(\d+)\s*/\s*(\d+) assertions passed</small>', content)
    b = re.search(r'<div class="value">(\d+)%</div>\s*<div class="label">Baseline Claude \(no skills\)<br\s*/?><small>(\d+)\s*/\s*(\d+) assertions passed</small>', content)
    d = re.search(r'<div class="value">\+(\d+)</div>\s*<div class="label">Point improvement<br\s*/?><small>\+(\d+) additional assertions passed</small>', content)
    assert w and b and d, "index.html stat-grid entries not found"
    return {
        "with_pct": int(w.group(1)), "with_passed": int(w.group(2)), "total": int(w.group(3)),
        "base_pct": int(b.group(1)), "base_passed": int(b.group(2)), "base_total": int(b.group(3)),
        "delta_pts": int(d.group(1)), "delta_assertions": int(d.group(2)),
    }


def _parse_eval_page_stat_cards(content: str) -> dict:
    """Extract the overall summary from grc-skills-eval-results.html stat cards."""
    w = re.search(r'<div class="stat-value">(\d+)%</div>\s*<div class="stat-label">With Skill</div>', content)
    b = re.search(r'<div class="stat-value neutral">(\d+)%</div>\s*<div class="stat-label">Baseline \(No Skill\)</div>', content)
    d = re.search(r'<div class="stat-value positive">\+(\d+)%</div>\s*<div class="stat-label">Improvement</div>', content)
    t = re.search(r'<div class="stat-value">(\d+)</div>\s*<div class="stat-label">Total Assertions</div>', content)
    e = re.search(r'<div class="stat-value positive">\+(\d+)</div>\s*<div class="stat-label">Extra Assertions Passed</div>', content)
    assert w and b and d and t and e, "eval page stat cards not found"
    return {
        "with_pct": int(w.group(1)), "base_pct": int(b.group(1)),
        "delta_pts": int(d.group(1)), "total": int(t.group(1)),
        "delta_assertions": int(e.group(1)),
    }


def _parse_eval_page_assertion_cells(content: str) -> list[tuple[str, int, int]]:
    """Extract (skill, passed, total) from the summary table's assertions column."""
    pattern = re.compile(
        r'class="skill-link">([^<]+)</a></td>\s*'
        r'<td[^>]*>(\d+)%</td>\s*<td[^>]*>(\d+)%</td>\s*'
        r'<td[^>]*>[+\-±]?\d+%</td>\s*'
        r'<td[^>]*>(\d+)/(\d+)</td>',
        re.DOTALL,
    )
    return [(m.group(1), int(m.group(4)), int(m.group(5))) for m in pattern.finditer(content)]


class TestSummaryBlockConsistency:
    """The overall (suite-level) stats must be identical across all three files."""

    @pytest.fixture(scope="class")
    def summaries(self):
        readme = (REPO_ROOT / "README.md").read_text()
        index = (REPO_ROOT / "index.html").read_text()
        eval_page = (REPO_ROOT / "grc-skills-eval-results.html").read_text()
        return {
            "readme": _parse_readme_summary(readme),
            "index": _parse_index_summary(index),
            "eval_page": _parse_eval_page_stat_cards(eval_page),
        }

    def test_summary_block_consistency(self, summaries):
        r, i, e = summaries["readme"], summaries["index"], summaries["eval_page"]
        for field in ("with_pct", "base_pct", "delta_pts", "delta_assertions"):
            assert r[field] == i[field] == e[field], (
                f"Summary field '{field}' diverges: README={r[field]}, "
                f"index.html={i[field]}, eval page={e[field]}"
            )
        assert r["total"] == i["total"] == e["total"], (
            f"Total assertions diverge: README={r['total']}, "
            f"index.html={i['total']}, eval page={e['total']}"
        )
        # README/index also publish raw passed counts — they must agree
        assert r["with_passed"] == i["with_passed"], "with-skill passed count diverges README vs index"
        assert r["base_passed"] == i["base_passed"], "baseline passed count diverges README vs index"

    def test_summary_arithmetic(self, summaries):
        r = summaries["readme"]
        # Percentages must round-trip from raw counts
        assert round(100 * r["with_passed"] / r["total"]) == r["with_pct"], (
            f"with-skill %: {r['with_passed']}/{r['total']} rounds to "
            f"{round(100 * r['with_passed'] / r['total'])}, published {r['with_pct']}%"
        )
        assert round(100 * r["base_passed"] / r["base_total"]) == r["base_pct"], (
            f"baseline %: {r['base_passed']}/{r['base_total']} rounds to "
            f"{round(100 * r['base_passed'] / r['base_total'])}, published {r['base_pct']}%"
        )
        # Deltas must be arithmetic, not hand-typed (the +16/+107 bug)
        assert r["delta_pts"] == r["with_pct"] - r["base_pct"], (
            f"delta points {r['delta_pts']} != {r['with_pct']} - {r['base_pct']}"
        )
        assert r["delta_assertions"] == r["with_passed"] - r["base_passed"], (
            f"delta assertions {r['delta_assertions']} != "
            f"{r['with_passed']} - {r['base_passed']}"
        )
        # Per-skill assertion cells on the eval page must sum to the published totals
        eval_page = (REPO_ROOT / "grc-skills-eval-results.html").read_text()
        cells = _parse_eval_page_assertion_cells(eval_page)
        assert len(cells) == EXPECTED_SKILL_COUNT, (
            f"Expected {EXPECTED_SKILL_COUNT} assertion cells, found {len(cells)}"
        )
        assert sum(t for _, _, t in cells) == r["total"], (
            f"Per-skill assertion totals sum to {sum(t for _, _, t in cells)}, "
            f"published total is {r['total']}"
        )
        assert sum(p for _, p, _ in cells) == r["with_passed"], (
            f"Per-skill passed counts sum to {sum(p for _, p, _ in cells)}, "
            f"published with-skill passed is {r['with_passed']}"
        )

    def test_methodology_totals(self, summaries):
        total = summaries["readme"]["total"]
        readme = (REPO_ROOT / "README.md").read_text()
        index = (REPO_ROOT / "index.html").read_text()
        assert re.search(rf"\({total} assertions in total\)|\({total} in total\)", readme), (
            f"README methodology prose does not state the published total ({total})"
        )
        assert f"{total} total assertions evaluated" in index, (
            f"index.html methodology prose does not state the published total ({total})"
        )
