"""
test_iso42001_crossrefs.py
==========================
Guards against ISO/IEC 42001 Annex A citation drift (GitHub issue #63).

Any A.x[.y[.z]] identifier cited in an ISO 42001 context anywhere under
plugins/ must exist in the repo's own control list,
plugins/iso42001/skills/iso42001/references/iso42001-controls-annex-a.md
(38 controls, domains A.2 to A.10, sub-objectives A.6.1 and A.6.2).

"ISO 42001 context" means: a markdown table whose nearest preceding heading
or whose header row mentions 42001, or any single line that mentions 42001.
Scoping matters because ISO 27001 Annex A uses the same A.x.y notation in
many other skills and must not be validated against the 42001 list.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ANNEX = (REPO_ROOT / "plugins" / "iso42001" / "skills" / "iso42001"
         / "references" / "iso42001-controls-annex-a.md")
AID = re.compile(r"\bA\.\d+(?:\.\d+){0,2}\b")


def _valid_ids():
    text = ANNEX.read_text(encoding="utf-8")
    controls = set(re.findall(r"^\| (A\.[\d.]+) \|", text, re.M))
    domains = {f"A.{i}" for i in range(2, 11)} | {"A.6.1", "A.6.2"}
    return controls, controls | domains


def _scan():
    """Return (violations, tables_scanned) across plugins/ markdown files."""
    violations, tables_scanned = [], 0
    for f in sorted((REPO_ROOT / "plugins").rglob("*.md")):
        if f.name == "iso42001-controls-annex-a.md":
            continue
        _, valid = _valid_ids()
        lines = f.read_text(encoding="utf-8").splitlines()
        last_heading = ""
        i = 0
        while i < len(lines):
            ln = lines[i]
            if ln.startswith("#"):
                last_heading = ln
            if ln.lstrip().startswith("|"):
                j = i
                block = []
                while j < len(lines) and lines[j].lstrip().startswith("|"):
                    block.append(lines[j])
                    j += 1
                if "42001" in last_heading or "42001" in block[0]:
                    tables_scanned += 1
                    for k, row in enumerate(block):
                        for cited in AID.findall(row):
                            if cited not in valid:
                                violations.append(
                                    (str(f.relative_to(REPO_ROOT)), i + k + 1, cited))
                i = j
                continue
            if "42001" in ln:
                for cited in AID.findall(ln):
                    if cited not in valid:
                        violations.append(
                            (str(f.relative_to(REPO_ROOT)), i + 1, cited))
            i += 1
    return violations, tables_scanned


class TestAnnexAList:
    def test_annex_file_has_38_controls(self):
        controls, _ = _valid_ids()
        assert len(controls) == 38, (
            f"iso42001-controls-annex-a.md lists {len(controls)} controls, expected 38")

    def test_known_nonexistent_ids_absent_from_list(self):
        """The IDs invented in issue #63 must never enter the control list."""
        controls, _ = _valid_ids()
        for bogus in ("A.2.5", "A.4.1", "A.10.1", "A.10.5"):
            assert bogus not in controls, f"{bogus} should not be a control"


class TestCrosswalkCitations:
    def test_no_invalid_annex_a_citations_in_42001_contexts(self):
        violations, _ = _scan()
        assert not violations, (
            "Invalid ISO 42001 Annex A citations (file, line, cited id): "
            + "; ".join(f"{f}:{ln} {cid}" for f, ln, cid in violations))

    def test_scanner_actually_covers_the_crosswalk_tables(self):
        """Guard the scoping: the known 42001 crosswalk tables (nist-ai-rmf
        SKILL.md and rmf-profiles.md, eu-ai-act gpai-governance.md, plus the
        iso42001 skill's own tables) must be inside the scanned set."""
        _, tables_scanned = _scan()
        assert tables_scanned >= 3, (
            f"only {tables_scanned} 42001-context tables scanned; "
            "scoping has regressed and the drift guard is blind")
