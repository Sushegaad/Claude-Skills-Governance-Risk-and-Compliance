#!/usr/bin/env python3
"""
build_docs.py — generate all derived skill tables from skills.json + grading data.

Single source of truth:
  • skills.json                    — the skill inventory (names, files, categories,
                                     eval descriptions). Edit THIS when adding a skill.
  • grc-workspace/**/grading.json  — eval ground truth. Stats (with %, baseline %,
                                     delta) are COMPUTED from these, never typed.

Generated blocks (between  <!-- GEN:<name> -->  /  <!-- /GEN:<name> -->  markers):
  index.html       install-table, eval-table
  README.md        readme-eval-table
  INSTALLATION.md  install-commands, install-all, plugin-tables

Usage:
  python scripts/build_docs.py          # regenerate blocks in place
  python scripts/build_docs.py --check  # exit 1 if any generated block is stale
                                        # (wired into CI as the drift gate)

Stat aggregation is imported from tests/test_eval_consistency.py so the
generator and the test suite can never disagree about how grading.json
files are counted.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

REPO = Path(__file__).resolve().parent.parent
RAW = "https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance/raw/main/"

# Category display order = order of each category's first (lowest-numbered) skill.
CATEGORY_INSTALL_HEADERS = {
    "Information Security & Risk Management": "Information Security & Risk",
}


def _load_eval_module():
    spec = importlib.util.spec_from_file_location(
        "tec", REPO / "tests" / "test_eval_consistency.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _delta_disp(with_pct: int, base_pct: int) -> str:
    d = with_pct - base_pct
    return "±0%" if d == 0 else (f"+{d}%" if d > 0 else f"{d}%")


def compute_stats(skills, tec):
    """Per-skill (with%, base%, passed_cell) computed from grading.json files."""
    stats = {}
    for s in skills:
        agg = tec._aggregate_skill_grading(s["plugin"])
        if agg is None:
            raise SystemExit(f"ERROR: no grading data found for {s['plugin']}")
        wp, wt, bp, bt = agg
        stats[s["plugin"]] = {
            "with": round(100 * wp / wt),
            "base": round(100 * bp / bt),
            "passed": f"{wp}/{wt}",
        }
    return stats


# ── Renderers ────────────────────────────────────────────────────────────────

def render_install_table(skills):
    rows = []
    for s in skills:
        href = RAW + quote(s["standalone_dir"]) + "/" + quote(s["skill_file"])
        rows.append(
            f'<tr><td>{s["num"]}. {s["install_html"]}</td>'
            f'<td><a href="{href}">{s["skill_file"]}</a></td></tr>'
        )
    return "\n".join(rows)


def render_eval_table(skills, stats):
    rows = []
    for s in skills:
        st = stats[s["plugin"]]
        rows.append(
            '<tr><td style="text-align:center;font-weight:600;color:#64748b">'
            f'{s["num"]}</td><td>{s["eval_html"]}</td><td>{s["eval"]["cases"]}</td>'
            f'<td><strong>{st["with"]}%</strong></td><td>{st["base"]}%</td>'
            f'<td>{_delta_disp(st["with"], st["base"])}</td>'
            f'<td style="white-space:nowrap">{s["eval"]["last_updated"]}</td>'
            f'<td>{s["eval"]["tested"]}</td></tr>'
        )
    return "\n".join(rows)


def render_readme_eval_table(skills, stats):
    rows = []
    for s in skills:
        st = stats[s["plugin"]]
        rows.append(
            f'| {s["readme_name"]} | {s["eval"]["cases"]} | **{st["with"]}%** '
            f'| {st["base"]}% | {_delta_disp(st["with"], st["base"])} '
            f'| {s["eval"]["readme_tested"]} |'
        )
    return "\n".join(rows)


def _categories_in_order(skills):
    seen = []
    for s in skills:  # skills are in num order
        if s["category"] not in seen:
            seen.append(s["category"])
    return seen


def render_install_commands(skills):
    out = []
    for cat in _categories_in_order(skills):
        header = CATEGORY_INSTALL_HEADERS.get(cat, cat)
        members = [s for s in skills if s["category"] == cat]
        out.append(f"### {header}\n")
        out.append("```shell")
        out.extend(f'/plugin install {s["plugin"]}@grc-skills' for s in members)
        out.append("```\n")
    return "\n".join(out).rstrip()


def render_install_all(skills):
    names = " ".join(
        f'{s["plugin"]}@grc-skills'
        for cat in _categories_in_order(skills)
        for s in skills
        if s["category"] == cat
    )
    return f"```shell\n/plugin install {names}\n```"


def render_plugin_tables(skills):
    out = []
    for cat in _categories_in_order(skills):
        members = [s for s in skills if s["category"] == cat]
        out.append(f"### {cat}\n")
        out.append("| Plugin name | Framework | What it does |")
        out.append("|---|---|---|")
        out.extend(
            f'| `{s["plugin"]}` | {s["install_framework"]} | {s["install_desc"]} |'
            for s in members
        )
        out.append("")
    return "\n".join(out).rstrip()


# ── Block replacement ────────────────────────────────────────────────────────

def replace_block(content: str, name: str, body: str, path: Path):
    begin, end = f"<!-- GEN:{name} -->", f"<!-- /GEN:{name} -->"
    pattern = re.compile(re.escape(begin) + r"\n.*?" + re.escape(end), re.DOTALL)
    if not pattern.search(content):
        raise SystemExit(f"ERROR: markers for '{name}' not found in {path.name}")
    return pattern.sub(begin + "\n" + body + "\n" + end, content)


def main():
    check = "--check" in sys.argv
    manifest = json.loads((REPO / "skills.json").read_text(encoding="utf-8"))
    skills = sorted(manifest["skills"], key=lambda s: s["num"])
    tec = _load_eval_module()
    stats = compute_stats(skills, tec)

    targets = {
        REPO / "index.html": {
            "install-table": render_install_table(skills),
            "eval-table": render_eval_table(skills, stats),
        },
        REPO / "README.md": {
            "readme-eval-table": render_readme_eval_table(skills, stats),
        },
        REPO / "INSTALLATION.md": {
            "install-commands": render_install_commands(skills),
            "install-all": render_install_all(skills),
            "plugin-tables": render_plugin_tables(skills),
        },
    }

    stale = []
    for path, blocks in targets.items():
        original = path.read_text(encoding="utf-8")
        updated = original
        for name, body in blocks.items():
            updated = replace_block(updated, name, body, path)
        if updated != original:
            if check:
                stale.append(path.name)
            else:
                path.write_text(updated, encoding="utf-8")
                print(f"regenerated blocks in {path.name}")

    if check:
        if stale:
            print(f"DRIFT: generated blocks stale in: {', '.join(stale)} — "
                  f"run: python scripts/build_docs.py")
            return 1
        print("docs generator: all generated blocks up to date")
    else:
        print("done — verify with: pytest tests/ -q")
    return 0


if __name__ == "__main__":
    sys.exit(main())
