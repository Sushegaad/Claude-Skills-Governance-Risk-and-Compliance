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

Two sets of .skill files are tested:
  - Standalone: the <Name> - Claude Skill/<name>.skill files for direct download
  - Plugin-bundled: plugins/<name>/<name>.skill files shipped with each plugin

Run with:
    pip install pytest
    pytest tests/test_skill_installability.py -v
"""

import json
import zipfile
from pathlib import Path
import pytest

# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"

# Standalone .skill files: live in "<Name> - Claude Skill/" folders
STANDALONE_SKILL_FILES = sorted([
    p for p in REPO_ROOT.rglob("*.skill")
    if "plugins" not in p.parts and ".claude" not in p.parts
])

# Plugin-bundled .skill files: live at plugins/<name>/<name>.skill
PLUGIN_SKILL_FILES = sorted([
    p for p in PLUGINS_DIR.rglob("*.skill")
    if p.parent.name == p.stem  # e.g. plugins/iso27001/iso27001.skill
])

ALL_SKILL_FILES = sorted(set(STANDALONE_SKILL_FILES) | set(PLUGIN_SKILL_FILES))

# ---------------------------------------------------------------------------
# Expected inventory — update when adding a new skill
# ---------------------------------------------------------------------------


# Standalone filenames as they actually appear on disk (some legacy names differ)
# Derived from skills.json — the single source of truth for the inventory.
EXPECTED_STANDALONE_FILENAMES = {
    s["skill_file"]
    for s in json.loads((REPO_ROOT / "skills.json").read_text(encoding="utf-8"))["skills"]
}


def pytest_generate_tests(metafunc):
    """Parametrise every test that accepts a skill_path fixture."""
    if "skill_path" in metafunc.fixturenames:
        ids = [
            f"{'plugin' if 'plugins' in p.parts else 'standalone'}::{p.name}"
            for p in ALL_SKILL_FILES
        ]
        metafunc.parametrize("skill_path", ALL_SKILL_FILES, ids=ids)


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
# Archive structure tests (parametrised over all .skill files)
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
        parts = Path(skill_md_path).parts
        depth = len(parts) - 1

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
        Prevents partially-nested archives where some files escaped the skill folder.
        """
        entries = _entries(skill_path)
        skill_md_path = _skill_md_entries(entries)[0]
        top_folder = Path(skill_md_path).parts[0]

        bad = [
            name for name, _ in entries
            if not name.startswith(top_folder + "/")
            and name != top_folder + "/"
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
# Standalone folder hygiene tests
# ---------------------------------------------------------------------------

STANDALONE_DIRS = sorted([
    d for d in REPO_ROOT.iterdir()
    if d.is_dir() and d.name.endswith(" - Claude Skill")
])


def test_standalone_dirs_contain_no_unexpected_file_types():
    """
    Every '<Name> - Claude Skill' folder may contain .skill files and README/
    markdown files, but nothing else (e.g. no binaries, scripts, or config files).
    """
    ALLOWED_SUFFIXES = {".skill", ".md", ".txt"}
    violations = {}
    for skill_dir in STANDALONE_DIRS:
        unexpected = [
            f.name for f in skill_dir.iterdir()
            if f.is_file() and f.suffix.lower() not in ALLOWED_SUFFIXES
        ]
        if unexpected:
            violations[skill_dir.name] = unexpected

    assert not violations, (
        "Unexpected file types found in standalone skill folders:\n"
        + "\n".join(f"  {folder}: {files}" for folder, files in violations.items())
    )


def test_standalone_dirs_contain_exactly_one_skill_file():
    """Each '<Name> - Claude Skill' folder must contain exactly one .skill file."""
    violations = {}
    for skill_dir in STANDALONE_DIRS:
        skill_files = [f for f in skill_dir.iterdir() if f.suffix.lower() == ".skill"]
        if len(skill_files) != 1:
            violations[skill_dir.name] = [f.name for f in skill_files]

    assert not violations, (
        "Expected exactly one .skill file per standalone folder:\n"
        + "\n".join(f"  {folder}: {files}" for folder, files in violations.items())
    )


# ---------------------------------------------------------------------------
# Plugin .skill completeness check
# ---------------------------------------------------------------------------

def test_every_plugin_has_bundled_skill_zip():
    """
    Every plugin directory must contain a <plugin-name>.skill ZIP file.
    This is the bundled copy for direct download alongside the plugin source.
    """
    plugin_dirs = sorted([p for p in PLUGINS_DIR.iterdir() if p.is_dir()])
    missing = []
    for plugin_dir in plugin_dirs:
        expected = plugin_dir / f"{plugin_dir.name}.skill"
        if not expected.exists():
            missing.append(f"plugins/{plugin_dir.name}/{plugin_dir.name}.skill")

    assert not missing, (
        "The following plugins are missing their bundled .skill ZIP.\n"
        "Copy the standalone .skill file into the plugin folder to fix:\n"
        + "\n".join(f"  {m}" for m in missing)
    )


# ---------------------------------------------------------------------------
# Inventory sanity checks
# ---------------------------------------------------------------------------

def test_all_expected_standalone_skills_present():
    """
    All 27 expected standalone .skill files must exist.
    When adding a new skill, add its filename to EXPECTED_STANDALONE_FILENAMES.
    """
    found = {p.name for p in STANDALONE_SKILL_FILES}
    missing = EXPECTED_STANDALONE_FILENAMES - found
    assert not missing, (
        f"Expected standalone .skill files not found: {missing}"
    )


def test_no_unexpected_standalone_skills():
    """
    Warn if standalone .skill files appear that are not in the expected set.
    This catches new skills added without updating the test inventory.
    When adding a new skill, update EXPECTED_STANDALONE_FILENAMES above.
    """
    found = {p.name for p in STANDALONE_SKILL_FILES}
    extra = found - EXPECTED_STANDALONE_FILENAMES
    assert not extra, (
        f"Found standalone .skill files not listed in EXPECTED_STANDALONE_FILENAMES — "
        f"add them to the set at the top of this test file: {extra}"
    )


def test_plugin_skill_names_match_canonical():
    """
    Every plugin-bundled .skill file must use the canonical lowercase kebab-case
    name matching its plugin directory name.
    """
    wrong = []
    for skill_file in PLUGIN_SKILL_FILES:
        plugin_name = skill_file.parent.name
        if skill_file.stem != plugin_name:
            wrong.append(
                f"plugins/{plugin_name}/{skill_file.name} "
                f"(expected: {plugin_name}.skill)"
            )
    assert not wrong, (
        "Plugin-bundled .skill files with incorrect names:\n"
        + "\n".join(f"  {w}" for w in wrong)
    )


# ---------------------------------------------------------------------------
# Installer-constraint checks (added v1.6.x)
#
# The claude.ai skill installer rejects archives for reasons beyond nesting:
# frontmatter name format/length, description length, junk archive entries.
# Users have reported "SKILL.md file must be in the top-level folder, not
# nested deeper" — the nesting rule is covered above; these tests pin down
# every other known rejection cause so no artifact can ship that fails
# installation.
# ---------------------------------------------------------------------------

import json
import re as _re

try:
    import yaml as _yaml
except ImportError:  # pragma: no cover
    _yaml = None

_NAME_PATTERN = _re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
_MAX_NAME_LEN = 64
_MAX_DESC_LEN = 1024
_JUNK_MARKERS = ("__MACOSX", ".DS_Store", "Thumbs.db")


def _all_skill_zips():
    zips = sorted(REPO_ROOT.glob("plugins/*/*.skill"))
    zips += [p for p in sorted(REPO_ROOT.glob("*/*.skill"))
             if "plugins" not in p.parts]
    return zips


def _frontmatter_of(zip_path):
    import zipfile
    with zipfile.ZipFile(zip_path) as zf:
        skill_md = [n for n in zf.namelist()
                    if n.endswith("SKILL.md") and n.count("/") == 1][0]
        text = zf.read(skill_md).decode("utf-8")
    m = _re.match(r"^---\n(.*?)\n---\n", text, _re.DOTALL)
    assert m, f"{zip_path.name}: SKILL.md has no YAML frontmatter"
    assert _yaml is not None, "pyyaml required for installability tests"
    return _yaml.safe_load(m.group(1)), skill_md.split("/")[0]


class TestInstallerConstraints:
    @pytest.mark.parametrize("zip_path", _all_skill_zips(), ids=lambda p: p.name)
    def test_no_junk_archive_entries(self, zip_path):
        """__MACOSX/.DS_Store entries break or pollute installs (a re-zip on
        macOS Finder adds them); our build pipeline must never ship them."""
        import zipfile
        with zipfile.ZipFile(zip_path) as zf:
            junk = [n for n in zf.namelist()
                    if any(j in n for j in _JUNK_MARKERS) or n.startswith(".")]
        assert not junk, f"{zip_path.name}: junk entries {junk}"

    @pytest.mark.parametrize("zip_path", _all_skill_zips(), ids=lambda p: p.name)
    def test_frontmatter_name_valid(self, zip_path):
        """Installer requires: name present, lowercase alphanumeric+hyphens,
        ≤64 chars, and matching the archive's top-level folder."""
        fm, top = _frontmatter_of(zip_path)
        name = fm.get("name", "")
        assert name, f"{zip_path.name}: frontmatter 'name' missing"
        assert _NAME_PATTERN.fullmatch(name), (
            f"{zip_path.name}: name {name!r} is not lowercase-hyphen format"
        )
        assert len(name) <= _MAX_NAME_LEN, f"{zip_path.name}: name >64 chars"
        assert name == top, (
            f"{zip_path.name}: top-level folder {top!r} != frontmatter name {name!r}"
        )

    @pytest.mark.parametrize("zip_path", _all_skill_zips(), ids=lambda p: p.name)
    def test_frontmatter_description_within_limit(self, zip_path):
        """Installer rejects descriptions over 1024 characters."""
        fm, _ = _frontmatter_of(zip_path)
        desc = fm.get("description", "") or ""
        assert desc, f"{zip_path.name}: frontmatter 'description' missing"
        assert len(desc) <= _MAX_DESC_LEN, (
            f"{zip_path.name}: description is {len(desc)} chars "
            f"(installer limit {_MAX_DESC_LEN}). Trim the trigger text."
        )

    @pytest.mark.parametrize("zip_path", _all_skill_zips(), ids=lambda p: p.name)
    def test_zip_matches_source_skill_md(self, zip_path):
        """The bundled SKILL.md must be byte-identical to the source tree —
        a stale ZIP is the classic way an already-fixed install bug returns."""
        import zipfile
        with zipfile.ZipFile(zip_path) as zf:
            inner = [n for n in zf.namelist()
                     if n.endswith("SKILL.md") and n.count("/") == 1][0]
            bundled = zf.read(inner)
        name = inner.split("/")[0]
        source = REPO_ROOT / "plugins" / name / "skills" / name / "SKILL.md"
        assert source.exists(), f"{zip_path.name}: no source at {source}"
        assert bundled == source.read_bytes(), (
            f"{zip_path.name}: bundled SKILL.md differs from source — rebuild the ZIP"
        )

    @pytest.mark.parametrize("zip_path", _all_skill_zips(), ids=lambda p: p.name)
    def test_zip_reference_files_match_source(self, zip_path):
        """Every references/*.md bundled in the ZIP must be byte-identical to the
        source tree, and every source reference file must be bundled. SKILL.md
        alone being checked left a silent-staleness channel for reference docs."""
        import zipfile
        with zipfile.ZipFile(zip_path) as zf:
            inner_skill = [n for n in zf.namelist()
                           if n.endswith("SKILL.md") and n.count("/") == 1][0]
            name = inner_skill.split("/")[0]
            bundled_refs = {
                n.split("/", 1)[1]: zf.read(n)
                for n in zf.namelist()
                if n.startswith(f"{name}/references/") and n.endswith(".md")
            }
        src_dir = REPO_ROOT / "plugins" / name / "skills" / name
        source_refs = {
            f"references/{p.name}": p.read_bytes()
            for p in sorted((src_dir / "references").glob("*.md"))
        } if (src_dir / "references").exists() else {}
        missing = sorted(set(source_refs) - set(bundled_refs))
        extra = sorted(set(bundled_refs) - set(source_refs))
        assert not missing, (
            f"{zip_path.name}: source reference files not bundled: {missing} — rebuild the ZIP"
        )
        assert not extra, (
            f"{zip_path.name}: ZIP bundles reference files with no source: {extra}"
        )
        stale = sorted(k for k in source_refs if bundled_refs[k] != source_refs[k])
        assert not stale, (
            f"{zip_path.name}: bundled reference files differ from source: {stale} — rebuild the ZIP"
        )
