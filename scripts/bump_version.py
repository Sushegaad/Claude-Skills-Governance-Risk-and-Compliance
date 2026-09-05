#!/usr/bin/env python3
"""
bump_version.py — bump the canonical version everywhere in one command.

Usage:
    python scripts/bump_version.py 1.10.0 "October 2026"

Updates (all previously hand-edited on every release):
  • plugins/*/.claude-plugin/plugin.json      (33 version strings)
  • .claude-plugin/marketplace.json           (33 version strings)
  • tests/test_version_consistency.py         (CANONICAL_VERSION + KNOWN_OLD_VERSIONS)
  • index.html                                (release badge + "Latest release" text)
  • README.md                                 (release badge + tag link)
  • "* - Claude Skill/*.md"                   (33 "Skill version:" footers)
  • ai-catalog.json                           (via build_docs.py, run automatically)

It does NOT write the release-notes entry in index.html (that is content, not
mechanics) — it prints a checklist of the remaining manual steps instead.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    new, monthyear = sys.argv[1], sys.argv[2]
    if not re.fullmatch(r"\d+\.\d+\.\d+", new):
        print(f"ERROR: '{new}' is not a semver version")
        return 2

    tv = REPO / "tests" / "test_version_consistency.py"
    m = re.search(r'CANONICAL_VERSION = "(\d+\.\d+\.\d+)"', tv.read_text())
    old = m.group(1)
    if old == new:
        print(f"Already at {new}")
        return 0
    print(f"Bumping {old} -> {new} ({monthyear})")

    n = 0
    for f in sorted(REPO.glob("plugins/*/.claude-plugin/plugin.json")):
        c = f.read_text(encoding="utf-8")
        assert f'"version": "{old}"' in c, f"{f}: expected version {old}"
        f.write_text(c.replace(f'"version": "{old}"', f'"version": "{new}"', 1), encoding="utf-8")
        n += 1
    print(f"  plugin.json: {n}")

    mk = REPO / ".claude-plugin" / "marketplace.json"
    c = mk.read_text(encoding="utf-8")
    count = c.count(f'"version": "{old}"')
    assert count == n, f"marketplace.json has {count} version strings, expected {n}"
    mk.write_text(c.replace(f'"version": "{old}"', f'"version": "{new}"'), encoding="utf-8")
    print(f"  marketplace.json: {count}")

    c = tv.read_text(encoding="utf-8")
    c = c.replace(f'CANONICAL_VERSION = "{old}"', f'CANONICAL_VERSION = "{new}"', 1)
    c = re.sub(r'(KNOWN_OLD_VERSIONS = \{[^}]*)"\}', rf'\1", "{old}"}}', c, count=1) \
        if f'"{old}"' not in re.search(r"KNOWN_OLD_VERSIONS = \{[^}]*\}", c).group(0) else c
    tv.write_text(c, encoding="utf-8")
    print("  test_version_consistency.py: canonical + denylist")

    idx = REPO / "index.html"
    c = idx.read_text(encoding="utf-8")
    c = c.replace(f'alt="Release v{old}"', f'alt="Release v{new}"', 1)
    c = c.replace(f"Release-v{old}-brightgreen.svg", f"Release-v{new}-brightgreen.svg", 1)
    c = c.replace(f"Latest release: <strong>v{old}</strong>", f"Latest release: <strong>v{new}</strong>", 1)
    idx.write_text(c, encoding="utf-8")
    print("  index.html: badge + latest-release text")

    rd = REPO / "README.md"
    c = rd.read_text(encoding="utf-8")
    c = c.replace(f"Release: v{old}", f"Release: v{new}", 1)
    c = c.replace(f"Release-v{old}-brightgreen.svg", f"Release-v{new}-brightgreen.svg", 1)
    c = c.replace(f"releases/tag/v{old}", f"releases/tag/v{new}", 1)
    rd.write_text(c, encoding="utf-8")
    print("  README.md: badge")

    n = 0
    for f in sorted(REPO.glob("* - Claude Skill/*.md")):
        c = f.read_text(encoding="utf-8")
        c2 = re.sub(r"Skill version: \d+\.\d+\.\d+ — \w+ \d{4}", f"Skill version: {new} — {monthyear}", c)
        c2 = c2.replace(f"**Skill version:** {old}", f"**Skill version:** {new}")
        if c2 != c:
            f.write_text(c2, encoding="utf-8")
            n += 1
    print(f"  standalone README footers: {n}")

    print("  regenerating derived files (ai-catalog.json)...")
    subprocess.run([sys.executable, str(REPO / "scripts" / "build_docs.py")], check=True)

    print(f"""
Done. Remaining MANUAL steps for v{new}:
  1. Write the v{new} release-notes entry in index.html (current block, demote
     previous, archive the one before; keep exactly two visible).
  2. Update Claude Docs/CHANGELOG.md.
  3. Update the GitHub 'About' blurb if headline stats changed.
  4. Run: pytest tests/ -q  &&  python scripts/build_docs.py --check
  5. Commit, push, then: git tag v{new} && git push --tags
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
