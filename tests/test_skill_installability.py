"""
test_skill_installability.py
============================
Validates that every .skill file in the repository can be installed
by Claude without errors.

Rules enforced (mirrors the Claude skill installer):
  1. The archive must contain at least one entry.
  2. Exactly one SKILL.md must exist inside the archive.
  3. SKILL.md must live exactly ONE directory level deep:
       <skill-name>/SKILL.md   ✅
       skills/<skill-name>/SKILL.md  ❌  (two levels — triggers installer error)
       SKILL.md                ❌  (top-level — no wrapping folder)
  4. All reference files (if any) must sit under the same top-level folder
     as SKILL.md, e.g. <skill-name>/references/*.md
  5. The archive must not contain any path that escapes the top-level folder
     (path-traversal guard: no entry may start with / or contain ..)
  6. SKILL.md must not be empty (> 0 bytes).

Run with:
    pip install pytest
    pytest tests/test_skill_installability.py -v
"""

import zipfile
from pathlib import Path
import pytest

# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent

SKILL_FILES = sorted(REPO_ROOT.rglob("*.skill"))

# Exclude any .skill files that live inside the plugins/ tree — those are
# source directories, not the distributable ZIP archives.
SKILL_FILES = [
    p for p in SKILL_FILES
    if "plugins" not in p.parts
]


def pytest_generate_tests(metafunc):
    """Parameterise every test that accepts a `skill_path` fixture."""
    if "skill_path" in metafunc.fixturenames:
        ids = [p.name for p in SKILL_FILES]
        metafunc.parametrize("skill_path", SKILL_FILES, ids=ids)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _entries(skill_path: Path):
    """Return list of (name, file_size) for every entry in the archive."""
    with zipfile.ZipFile(skill_path) as zf:
        return [(info.filename, info.file_size) for info in zf.infolist()]


def _skill_md_entries(entries):
    return [name for name, _ in entries if name.upper().endswith("SKILL.MD")]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestSkillArchiveStructure:

    def test_is_valid_zip(self, skill_path):
        """File must be a valid ZIP archive."""
        assert zipfile.is_zipfile(skill_path), (
            f"{skill_path.name} is not a valid ZIP file"
        )

    def test_archive_not_empty(self, skill_path):
        """Archive must contain at least one entry."""
        entries = _entries(skill_path)
        assert len(entries) > 0, f"{skill_path.name} is an empty archive"

    def test_exactly_one_skill_md(self, skill_path):
        """There must be exactly one SKILL.md in the archive."""
        entries = _entries(skill_path)
        skill_mds = _skill_md_entries(entries)
        assert len(skill_mds) == 1, (
            f"{skill_path.name}: expected 1 SKILL.md, found {len(skill_mds)}: {skill_mds}"
        )

    def test_skill_md_exactly_one_level_deep(self, skill_path):
        """
        SKILL.md must be exactly one directory level deep.

        Accepted:   <skill-name>/SKILL.md
        Rejected:   SKILL.md                       (top-level, depth 0)
                    skills/<skill-name>/SKILL.md   (two levels, depth 2+)
        """
        entries = _entries(skill_path)
        skill_md_path = _skill_md_entries(entries)[0]

        parts = Path(skill_md_path).parts  # e.g. ('iso27001', 'SKILL.md')
        depth = len(parts) - 1  # number of parent directories

        assert depth == 1, (
            f"{skill_path.name}: SKILL.md must be exactly one directory deep "
            f"(e.g. <skill-name>/SKILL.md), but found it at: {skill_md_path!r} "
            f"(depth={depth}). "
            "This causes the installer error: 'SKILL.md file must be in the "
            "top-level folder, not nested deeper.'"
        )

    def test_no_path_traversal(self, skill_path):
        """No entry may use absolute paths or .. components (security guard)."""
        entries = _entries(skill_path)
        bad = [
            name for name, _ in entries
            if name.startswith("/") or ".." in Path(name).parts
        ]
        assert not bad, (
            f"{skill_path.name}: archive contains unsafe paths: {bad}"
        )

    def test_all_files_under_top_level_folder(self, skill_path):
        """
        Every file entry must live under the same top-level folder as SKILL.md.
        This prevents partially-nested archives where some files escaped the
        skill folder.
        """
        entries = _entries(skill_path)
        skill_md_path = _skill_md_entries(entries)[0]
        top_folder = Path(skill_md_path).parts[0]  # e.g. 'iso27001'

        bad = [
            name for name, _ in entries
            if not name.startswith(top_folder + "/") and name != top_folder + "/"
            and name != top_folder
        ]
        assert not bad, (
            f"{skill_path.name}: these entries sit outside the expected top-level "
            f"folder '{top_folder}/': {bad}"
        )

    def test_skill_md_not_empty(self, skill_path):
        """SKILL.md must have content (> 0 bytes)."""
        entries = _entries(skill_path)
        skill_md_name = _skill_md_entries(entries)[0]

        size = next(sz for name, sz in entries if name == skill_md_name)
        assert size > 0, (
            f"{skill_path.name}: SKILL.md exists but is empty (0 bytes)"
        )

    def test_references_under_skill_folder(self, skill_path):
        """
        If a references/ directory exists, all its contents must be under
        <skill-name>/references/, not at a different path.
        """
        entries = _entries(skill_path)
        skill_md_path = _skill_md_entries(entries)[0]
        top_folder = Path(skill_md_path).parts[0]

        ref_entries = [
            name for name, _ in entries
            if "reference" in name.lower() and not name.endswith("/")
        ]
        bad = [
            name for name in ref_entries
            if not name.startswith(f"{top_folder}/references/")
        ]
        assert not bad, (
            f"{skill_path.name}: reference files found outside "
            f"'{top_folder}/references/': {bad}"
        )


# ---------------------------------------------------------------------------
# Inventory sanity check
# ---------------------------------------------------------------------------

EXPECTED_SKILLS = {
    "eu-ai-act.skill",
    "fedramp.skill",
    "gdpr-compliance.skill",
    "govramp.skill",
    "hipaa-compliance.skill",
    "iso13485.skill",
    "hitrust.skill",
    "iso22301.skill",
    "iso27001.skill",
    "iso27701.skill",
    "iso27017.skill",
    "iso27018.skill",
    "iso31000.skill",
    "ISO-42001.skill",
    "ISO-9001.skill",
    "NIST Cybersecurity.skill",
    "PCI-Compliance.skill",
    "soc2.skill",
    "TSA-Compliance.skill",
    "cmmc.skill",
    "uk-nis-csrb.skill",
}


def test_all_expected_skills_present():
    """All expected .skill files must exist in the repository."""
    found = {p.name for p in SKILL_FILES}
    missing = EXPECTED_SKILLS - found
    assert not missing, (
        f"The following expected .skill files were not found in the repo: {missing}"
    )


def test_no_unexpected_skills():
    """Warn if there are .skill files not in the expected set (new skill added without updating tests)."""
    found = {p.name for p in SKILL_FILES}
    extra = found - EXPECTED_SKILLS
    assert not extra, (
        f"Found .skill files not listed in EXPECTED_SKILLS — "
        f"please add them to the test: {extra}"
    )
