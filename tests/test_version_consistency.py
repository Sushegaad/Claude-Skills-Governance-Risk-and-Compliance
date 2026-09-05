"""
test_version_consistency.py
============================
Enforces that every skill plugin and the repository itself carry exactly one
version — the current canonical release version — across all locations:

  - plugins/*/. claude-plugin/plugin.json   (each plugin's own manifest)
  - .claude-plugin/marketplace.json         (marketplace catalog)
  - index.html badge                        (GitHub Pages site header)
  - README.md badge                         (repository readme)

If any of these disagrees with CANONICAL_VERSION, the test fails and names
the offending file so it can be corrected before merging.

Run with:
    pytest tests/test_version_consistency.py -v
"""

import json
import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Ground truth — bump this when cutting a new release
# ---------------------------------------------------------------------------
CANONICAL_VERSION = "1.9.0"

REPO = Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _plugin_dirs():
    return sorted((REPO / "plugins").iterdir())


def _load_plugin_json(plugin_dir: Path) -> dict:
    return json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text())


# ---------------------------------------------------------------------------
# Tests: plugin manifests
# ---------------------------------------------------------------------------

class TestPluginVersions:
    """Every plugins/*/. claude-plugin/plugin.json must declare CANONICAL_VERSION."""

    @pytest.mark.parametrize("plugin_dir", _plugin_dirs(), ids=lambda p: p.name)
    def test_plugin_json_version(self, plugin_dir: Path):
        data = _load_plugin_json(plugin_dir)
        assert "version" in data, (
            f"{plugin_dir.name}/plugin.json is missing the 'version' field"
        )
        assert data["version"] == CANONICAL_VERSION, (
            f"{plugin_dir.name}/plugin.json has version {data['version']!r}, "
            f"expected {CANONICAL_VERSION!r}"
        )


# ---------------------------------------------------------------------------
# Tests: marketplace catalog
# ---------------------------------------------------------------------------

class TestMarketplaceVersions:
    """Every entry in marketplace.json must declare CANONICAL_VERSION."""

    def _load_marketplace(self) -> dict:
        return json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text())

    def test_all_marketplace_entries_versioned(self):
        data = self._load_marketplace()
        bad = [
            p["name"]
            for p in data.get("plugins", [])
            if p.get("version") != CANONICAL_VERSION
        ]
        assert not bad, (
            f"marketplace.json entries with wrong version "
            f"(expected {CANONICAL_VERSION!r}): {bad}"
        )

    def test_marketplace_plugin_count_matches_plugins_dir(self):
        data = self._load_marketplace()
        mp_names = {p["name"] for p in data.get("plugins", [])}
        dir_names = {d.name for d in _plugin_dirs()}
        missing_from_mp = dir_names - mp_names
        missing_from_dir = mp_names - dir_names
        assert not missing_from_mp, (
            f"Plugins in plugins/ but not in marketplace.json: {sorted(missing_from_mp)}"
        )
        assert not missing_from_dir, (
            f"Plugins in marketplace.json but not in plugins/: {sorted(missing_from_dir)}"
        )


# ---------------------------------------------------------------------------
# Tests: repository-level version markers
# ---------------------------------------------------------------------------

class TestRepositoryVersion:
    """The GitHub Pages site and README must display CANONICAL_VERSION."""

    def test_index_html_badge(self):
        html = (REPO / "index.html").read_text()
        pattern = re.compile(r"Release-v([\d]+\.[\d]+\.[\d]+)")
        matches = pattern.findall(html)
        assert matches, "No Release-vX.Y.Z badge found in index.html"
        bad = [v for v in matches if v != CANONICAL_VERSION]
        assert not bad, (
            f"index.html badge(s) show version(s) {bad}, "
            f"expected {CANONICAL_VERSION!r}"
        )

    def test_index_html_latest_release_text(self):
        html = (REPO / "index.html").read_text()
        pattern = re.compile(r"Latest release:.*?v([\d]+\.[\d]+\.[\d]+)", re.DOTALL)
        match = pattern.search(html)
        assert match, "Could not find 'Latest release: vX.Y.Z' text in index.html"
        found = match.group(1)
        assert found == CANONICAL_VERSION, (
            f"index.html 'Latest release' shows v{found}, "
            f"expected v{CANONICAL_VERSION}"
        )

    def test_readme_badge(self):
        readme = (REPO / "README.md").read_text()
        pattern = re.compile(r"Release-v([\d]+\.[\d]+\.[\d]+)")
        matches = pattern.findall(readme)
        assert matches, "No Release-vX.Y.Z badge found in README.md"
        bad = [v for v in matches if v != CANONICAL_VERSION]
        assert not bad, (
            f"README.md badge(s) show version(s) {bad}, "
            f"expected {CANONICAL_VERSION!r}"
        )


# ---------------------------------------------------------------------------
# Tests: version uniqueness (no stale version strings in key files)
# ---------------------------------------------------------------------------

class TestVersionUniqueness:
    """No old version strings should appear in plugin manifests or the catalog."""

    KNOWN_OLD_VERSIONS = {"0.8.0", "1.0.0", "1.1.0", "1.2.0", "1.3.0", "1.4.0", "1.5.0", "1.6.0", "1.6.1", "1.6.2", "1.7.1", "1.8.0"}

    @pytest.mark.parametrize("plugin_dir", _plugin_dirs(), ids=lambda p: p.name)
    def test_no_stale_version_in_plugin_json(self, plugin_dir: Path):
        data = _load_plugin_json(plugin_dir)
        version = data.get("version", "")
        assert version not in self.KNOWN_OLD_VERSIONS, (
            f"{plugin_dir.name}/plugin.json still carries stale version {version!r}; "
            f"update it to {CANONICAL_VERSION!r}"
        )

    def test_no_stale_version_in_marketplace(self):
        data = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text())
        bad = [
            (p["name"], p.get("version"))
            for p in data.get("plugins", [])
            if p.get("version") in self.KNOWN_OLD_VERSIONS
        ]
        assert not bad, (
            f"marketplace.json entries with stale versions: {bad}"
        )


# ---------------------------------------------------------------------------
# Tests: _config.yml Jekyll exclusions
# ---------------------------------------------------------------------------

class TestJekyllConfig:
    """
    Every standalone skill folder must appear in _config.yml's exclude list
    so Jekyll never tries to process binary .skill ZIP files — which bloats
    the Pages artifact and can cause deployment failures.
    """

    def _load_excluded(self) -> set:
        import yaml  # PyYAML is available in the test env
        with open(REPO / "_config.yml") as f:
            config = yaml.safe_load(f)
        return set(config.get("exclude", []))

    def _standalone_skill_dirs(self) -> list:
        """Return folder names that contain a .skill ZIP (standalone skill dirs)."""
        skip = {"plugins", "tests", "grc-workspace", "assets", ".github", ".git",
                "__pycache__", "_site"}
        dirs = []
        for d in REPO.iterdir():
            if d.is_dir() and d.name not in skip and not d.name.startswith("."):
                if list(d.glob("*.skill")):
                    dirs.append(d.name)
        return sorted(dirs)

    @pytest.mark.parametrize("folder", _standalone_skill_dirs(None), ids=lambda f: f)
    def test_standalone_skill_folder_excluded_from_jekyll(self, folder: str):
        excluded = self._load_excluded()
        assert folder in excluded, (
            f"'{folder}' contains .skill ZIP files but is NOT in _config.yml exclude list. "
            f"Jekyll will try to process its binary files, bloating the Pages artifact. "
            f"Add  - \"{folder}\"  to the exclude list in _config.yml."
        )

    def test_plugins_dir_excluded_from_jekyll(self):
        excluded = self._load_excluded()
        assert "plugins" in excluded, (
            "The 'plugins' directory is not excluded in _config.yml. "
            "Jekyll will crawl all SKILL.md files and reference docs unnecessarily."
        )
