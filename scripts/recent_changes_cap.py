#!/usr/bin/env python3
"""
recent_changes_cap.py — find wiki pages whose `## Recent changes` section
                         exceeds the cap configured in config.yml
                         (history.recent_changes_cap).

Reports each violating page, the current count, and the entries that need to
be spilled to wiki/history/.

Exit code 1 if any violations found.
"""

import re
import sys
from pathlib import Path

from _lib import load_config, require_config  # type: ignore

WIKI_ROOT = Path(__file__).parent.parent / "wiki"

IGNORED_DIRS = {"history", "_schema", "sources"}
IGNORED_FILES = {"index.md", "log.md"}

RECENT_CHANGES_RE = re.compile(
    r"^## Recent changes\s*\n((?:.*\n)*?)(?=^##|\Z)",
    re.MULTILINE,
)
ENTRY_RE = re.compile(r"^\s*- \[", re.MULTILINE)


def check_page(path: Path, cap: int):
    text = path.read_text(encoding="utf-8")
    match = RECENT_CHANGES_RE.search(text)
    if not match:
        return None
    section = match.group(1)
    entries = ENTRY_RE.findall(section)
    count = len(entries)
    if count > cap:
        # Extract the actual entry lines for reporting
        entry_lines = [
            line.strip()
            for line in section.splitlines()
            if line.strip().startswith("- [")
        ]
        return count, entry_lines
    return None


def main():
    cap = int(require_config(load_config(), "history.recent_changes_cap"))
    violations = []

    for path in sorted(WIKI_ROOT.rglob("*.md")):
        rel = path.relative_to(WIKI_ROOT)
        parts = rel.parts
        if parts[0] in IGNORED_DIRS:
            continue
        if len(parts) == 1 and parts[0] in IGNORED_FILES:
            continue

        result = check_page(path, cap)
        if result:
            count, entry_lines = result
            violations.append((rel, count, entry_lines))

    if not violations:
        print(f"[OK] No pages exceed the {cap}-entry recent-changes cap.")
        return

    print(f"\n[CAP EXCEEDED] {len(violations)} page(s) have more than {cap} recent-changes entries:\n")
    for rel, count, entries in violations:
        excess = count - cap
        print(f"  {rel}  ({count} entries, {excess} to spill)")
        for i, entry in enumerate(entries):
            marker = "  SPILL →" if i >= cap else "         "
            # Truncate long lines for readability
            display = entry[:100] + "…" if len(entry) > 100 else entry
            print(f"    {marker} {display}")
        print()

    sys.exit(1)


if __name__ == "__main__":
    main()
