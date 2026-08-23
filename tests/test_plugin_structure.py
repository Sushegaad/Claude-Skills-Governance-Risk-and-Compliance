"""
test_plugin_structure.py
========================
Validates that every plugin in the plugins/ directory is correctly structured
for the Claude Code plugin marketplace.

Expected layout for each plugin:
    plugins/<plugin-name>/
    ├── .claude-plugin/
    │   └── plugin.json          (valid JSON, required fields present)
    ├── skills/
    │   └── <skill-name>/
    │       ├── SKILL.md         (non-empty)
    │       └── references/      (optional)
    │           └── *.md
    └── <plugin-name>.skill      (valid ZIP — bundled for direct download)

Run with:
    pip install pytest
    pytest tests/test_plugin_structure.py -v
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
MARKETPLACE_JSON = REPO_ROOT / ".claude-plugin" / "marketplace.json"

PLUGIN_DIRS = sorted([p for p in PLUGINS_DIR.iterdir() if p.is_dir()])

# Single source of truth: all 30 expected plugin names derived from
# marketplace.json at test time (see test_marketplace_lists_all_plugins).
# Hardcoded set is used only as a cross-check — update this list whenever
# a new skill is added.
EXPECTED_PLUGINS = {
    "ccpa",
    "cis-controls",
    "eu-cra",
    "cmmc",
    "csrd",
    "dora",
    "dpdpa",
    "ear",
    "eu-ai-act",
    "fedramp",
    "gdpr-compliance",
    "hipaa-compliance",
    "ism",
    "iso27001",
    "iso27701",
    "iso42001",
    "itar",
    "lgpd",
    "nis2",
    "nist-800-53",
    "nist-ai-rmf",
    "nist-csf",
    "nzism",
    "pci-compliance",
    "vn-pdpl",
    "section-508",
    "soc2",
    "swift-csp",
    "tsa-compliance",
    "wcag",
    "saudi-arabia-grc",
    "tisax",
    "uae-grc",
}

REQUIRED_PLUGIN_JSON_FIELDS = {"name", "version", "description"}


def pytest_generate_tests(metafunc):
    if "plugin_dir" in metafunc.fixturenames:
        ids = [p.name for p in PLUGIN_DIRS]
        metafunc.parametrize("plugin_dir", PLUGIN_DIRS, ids=ids)


# ---------------------------------------------------------------------------
# Per-plugin structural tests
# ---------------------------------------------------------------------------

class TestPluginDirectory:

    def test_plugin_json_exists(self, plugin_dir):
        """Every plugin must have .claude-plugin/plugin.json."""
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        assert plugin_json.exists(), (
            f"{plugin_dir.name}: missing .claude-plugin/plugin.json"
        )

    def test_plugin_json_is_valid(self, plugin_dir):
        """plugin.json must be valid JSON."""
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            pytest.skip("plugin.json missing — covered by test_plugin_json_exists")
        try:
            data = json.loads(plugin_json.read_text())
        except json.JSONDecodeError as e:
            pytest.fail(f"{plugin_dir.name}: plugin.json is invalid JSON: {e}")
        assert isinstance(data, dict), (
            f"{plugin_dir.name}: plugin.json must be a JSON object"
        )

    def test_plugin_json_required_fields(self, plugin_dir):
        """plugin.json must contain name, version, and description."""
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            pytest.skip("plugin.json missing")
        data = json.loads(plugin_json.read_text())
        missing = REQUIRED_PLUGIN_JSON_FIELDS - set(data.keys())
        assert not missing, (
            f"{plugin_dir.name}: plugin.json is missing required fields: {missing}"
        )

    def test_plugin_version_semver(self, plugin_dir):
        """version field must follow semver (MAJOR.MINOR.PATCH)."""
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            pytest.skip("plugin.json missing")
        data = json.loads(plugin_json.read_text())
        version = data.get("version", "")
        parts = version.split(".")
        assert len(parts) == 3 and all(p.isdigit() for p in parts), (
            f"{plugin_dir.name}: version '{version}' is not valid semver (expected X.Y.Z)"
        )

    def test_skills_directory_exists(self, plugin_dir):
        """Every plugin must have a skills/ subdirectory."""
        skills_dir = plugin_dir / "skills"
        assert skills_dir.is_dir(), (
            f"{plugin_dir.name}: missing skills/ directory"
        )

    def test_skills_directory_has_one_skill_folder(self, plugin_dir):
        """The skills/ directory must contain exactly one skill subfolder."""
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            pytest.skip("skills/ missing — covered by test_skills_directory_exists")
        subfolders = [p for p in skills_dir.iterdir() if p.is_dir()]
        assert len(subfolders) == 1, (
            f"{plugin_dir.name}: skills/ must contain exactly one skill folder, "
            f"found {len(subfolders)}: {[s.name for s in subfolders]}"
        )

    def test_skill_md_exists(self, plugin_dir):
        """Each skill folder must contain SKILL.md."""
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            pytest.skip("skills/ missing")
        subfolders = [p for p in skills_dir.iterdir() if p.is_dir()]
        if not subfolders:
            pytest.skip("no skill subfolder found")
        skill_folder = subfolders[0]
        skill_md = skill_folder / "SKILL.md"
        assert skill_md.exists(), (
            f"{plugin_dir.name}: SKILL.md not found at "
            f"skills/{skill_folder.name}/SKILL.md"
        )

    def test_skill_md_not_empty(self, plugin_dir):
        """SKILL.md must have content."""
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            pytest.skip("skills/ missing")
        subfolders = [p for p in skills_dir.iterdir() if p.is_dir()]
        if not subfolders:
            pytest.skip("no skill subfolder")
        skill_md = subfolders[0] / "SKILL.md"
        if not skill_md.exists():
            pytest.skip("SKILL.md missing — covered by test_skill_md_exists")
        assert skill_md.stat().st_size > 0, (
            f"{plugin_dir.name}: SKILL.md is empty (0 bytes)"
        )

    def test_skill_zip_exists(self, plugin_dir):
        """
        Every plugin must bundle a <plugin-name>.skill ZIP file at its root.
        This allows direct download without going through the marketplace.
        """
        expected = plugin_dir / f"{plugin_dir.name}.skill"
        assert expected.exists(), (
            f"{plugin_dir.name}: missing bundled skill ZIP at "
            f"plugins/{plugin_dir.name}/{plugin_dir.name}.skill — "
            "add it by copying the standalone .skill file into the plugin folder"
        )

    def test_skill_zip_is_valid(self, plugin_dir):
        """The bundled .skill file must be a valid ZIP archive."""
        skill_zip = plugin_dir / f"{plugin_dir.name}.skill"
        if not skill_zip.exists():
            pytest.skip("skill ZIP missing — covered by test_skill_zip_exists")
        assert zipfile.is_zipfile(skill_zip), (
            f"{plugin_dir.name}: {plugin_dir.name}.skill is not a valid ZIP file"
        )

    def test_skill_zip_contains_skill_md(self, plugin_dir):
        """The bundled .skill ZIP must contain exactly one SKILL.md one level deep."""
        skill_zip = plugin_dir / f"{plugin_dir.name}.skill"
        if not skill_zip.exists() or not zipfile.is_zipfile(skill_zip):
            pytest.skip("skill ZIP missing or invalid")
        with zipfile.ZipFile(skill_zip) as zf:
            names = zf.namelist()
        skill_mds = [n for n in names if n.upper().endswith("SKILL.MD")]
        assert len(skill_mds) == 1, (
            f"{plugin_dir.name}: expected 1 SKILL.md in ZIP, found {len(skill_mds)}: {skill_mds}"
        )
        depth = len(Path(skill_mds[0]).parts) - 1
        assert depth == 1, (
            f"{plugin_dir.name}: SKILL.md must be exactly one directory deep in the ZIP "
            f"(e.g. {plugin_dir.name}/SKILL.md), found at: {skill_mds[0]!r}"
        )

    def test_no_files_outside_skill_folder(self, plugin_dir):
        """No stray files should exist directly in the skills/ directory."""
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            pytest.skip("skills/ missing")
        stray_files = [p for p in skills_dir.iterdir() if p.is_file()]
        assert not stray_files, (
            f"{plugin_dir.name}: stray files found directly in skills/: "
            f"{[f.name for f in stray_files]}"
        )

    def test_references_are_markdown(self, plugin_dir):
        """All files in references/ must be .md files."""
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            pytest.skip("skills/ missing")
        subfolders = [p for p in skills_dir.iterdir() if p.is_dir()]
        if not subfolders:
            pytest.skip("no skill subfolder")
        refs_dir = subfolders[0] / "references"
        if not refs_dir.exists():
            return  # references/ is optional
        non_md = [
            f.name for f in refs_dir.iterdir()
            if f.is_file() and f.suffix.lower() != ".md"
        ]
        assert not non_md, (
            f"{plugin_dir.name}: non-.md files found in references/: {non_md}"
        )

    def test_plugin_json_author_is_object(self, plugin_dir):
        """
        author in plugin.json must be an object with 'name' and 'email' keys,
        not a plain string.  A bare string causes 'Invalid input: expected object,
        received string' from claude plugin validate.
        """
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            pytest.skip("plugin.json missing — covered by test_plugin_json_exists")
        data = json.loads(plugin_json.read_text())
        author = data.get("author")
        if author is None:
            return  # author is optional at the plugin.json level
        assert isinstance(author, dict), (
            f"{plugin_dir.name}: plugin.json 'author' must be an object "
            f"{{\"name\": ..., \"email\": ...}}, got string: {author!r}"
        )
        for key in ("name", "email"):
            assert key in author, (
                f"{plugin_dir.name}: plugin.json 'author' object is missing '{key}' key"
            )

    def test_plugin_json_skills_key_absent_or_omitted(self, plugin_dir):
        """
        plugin.json must NOT contain a 'skills' key.  Claude Code auto-discovers
        skills from the skills/ subdirectory; an explicit 'skills' array (especially
        one containing objects with 'name'/'path' keys) causes schema validation
        errors: 'skills: Invalid input'.
        """
        plugin_json = plugin_dir / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            pytest.skip("plugin.json missing — covered by test_plugin_json_exists")
        data = json.loads(plugin_json.read_text())
        assert "skills" not in data, (
            f"{plugin_dir.name}: plugin.json must not contain a 'skills' key — "
            "Claude Code auto-discovers skills from the skills/ directory. "
            "Remove the 'skills' array entirely."
        )


# ---------------------------------------------------------------------------
# Inventory sanity checks
# ---------------------------------------------------------------------------

def test_all_expected_plugins_present():
    """All 30 expected plugin directories must exist under plugins/."""
    found = {p.name for p in PLUGIN_DIRS}
    missing = EXPECTED_PLUGINS - found
    assert not missing, (
        f"Expected plugin directories not found: {missing}"
    )


def test_no_unexpected_plugins():
    """
    Flag any plugin directories not in the expected set.
    When adding a new skill, update EXPECTED_PLUGINS in this file.
    """
    found = {p.name for p in PLUGIN_DIRS}
    extra = found - EXPECTED_PLUGINS
    assert not extra, (
        f"Found plugin directories not listed in EXPECTED_PLUGINS — "
        f"add them to the set at the top of this test file: {extra}"
    )


def test_marketplace_json_exists():
    """marketplace.json must exist at .claude-plugin/marketplace.json."""
    assert MARKETPLACE_JSON.exists(), (
        "marketplace.json not found at .claude-plugin/marketplace.json"
    )


def test_marketplace_json_valid():
    """marketplace.json must be valid JSON."""
    if not MARKETPLACE_JSON.exists():
        pytest.skip("marketplace.json missing")
    try:
        data = json.loads(MARKETPLACE_JSON.read_text())
    except json.JSONDecodeError as e:
        pytest.fail(f"marketplace.json is invalid JSON: {e}")
    assert isinstance(data, (dict, list)), "marketplace.json must be a JSON object or array"


def test_marketplace_lists_all_plugins():
    """Every plugin in plugins/ must be referenced in marketplace.json."""
    if not MARKETPLACE_JSON.exists():
        pytest.skip("marketplace.json missing")
    data = json.loads(MARKETPLACE_JSON.read_text())

    if isinstance(data, list):
        entries = data
    elif isinstance(data, dict):
        entries = data.get("plugins", [])
    else:
        pytest.fail("marketplace.json has unexpected structure")

    referenced = set()
    for entry in entries:
        for key in ("name", "id", "plugin_id", "path"):
            val = entry.get(key, "")
            if val:
                referenced.add(str(val).strip("/").split("/")[-1])

    found_plugin_names = {p.name for p in PLUGIN_DIRS}
    unlisted = found_plugin_names - referenced
    assert not unlisted, (
        f"These plugins exist in plugins/ but are not referenced in marketplace.json: {unlisted}"
    )


def test_all_marketplace_plugins_have_directories():
    """Every plugin named in marketplace.json must have a directory in plugins/."""
    if not MARKETPLACE_JSON.exists():
        pytest.skip("marketplace.json missing")
    data = json.loads(MARKETPLACE_JSON.read_text())
    entries = data.get("plugins", []) if isinstance(data, dict) else data

    found_plugin_names = {p.name for p in PLUGIN_DIRS}
    for entry in entries:
        name = entry.get("name", "")
        assert name in found_plugin_names, (
            f"marketplace.json references plugin '{name}' but plugins/{name}/ does not exist"
        )


def test_marketplace_entry_author_is_object():
    """
    Every entry in marketplace.json that has an 'author' field must set it to
    an object {\"name\": ..., \"email\": ...}, not a plain string.

    A bare string causes the misleading error
    'This plugin uses a source type your Claude Code version does not support'
    during `claude plugin install`, and is flagged as
    'Invalid input: expected object, received string' by `claude plugin validate`.
    """
    if not MARKETPLACE_JSON.exists():
        pytest.skip("marketplace.json missing")
    data = json.loads(MARKETPLACE_JSON.read_text())
    entries = data.get("plugins", []) if isinstance(data, dict) else data

    bad = []
    for entry in entries:
        name = entry.get("name", "<unknown>")
        author = entry.get("author")
        if author is None:
            continue  # author is optional in a marketplace entry
        if not isinstance(author, dict):
            bad.append(
                f"  {name}: 'author' is {type(author).__name__} {author!r} "
                f"— must be {{\"name\": ..., \"email\": ...}}"
            )
        else:
            for key in ("name", "email"):
                if key not in author:
                    bad.append(
                        f"  {name}: 'author' object is missing '{key}' key"
                    )

    assert not bad, (
        "marketplace.json entries have invalid 'author' fields "
        "(fix: replace string values with {{\"name\": ..., \"email\": ...}} objects):\n"
        + "\n".join(bad)
    )
