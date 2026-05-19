#!/usr/bin/env python3
"""
index_check.py — verify wiki/index.md lists every page under wiki/

Reports:
  - Pages on disk that are NOT in index.md (missing from index)
  - Pages in index.md that do NOT exist on disk (stale/broken index entries)

Ignores: wiki/index.md itself, wiki/log.md, wiki/history/, wiki/_schema/,
         wiki/sources/ (sources are intentionally not indexed).
"""

import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent / "wiki"
INDEX_FILE = WIKI_ROOT / "index.md"

IGNORED_DIRS = {"history", "_schema", "sources"}
IGNORED_FILES = {"index.md", "log.md"}


def collect_disk_pages():
    pages = set()
    for path in WIKI_ROOT.rglob("*.md"):
        rel = path.relative_to(WIKI_ROOT)
        parts = rel.parts
        if parts[0] in IGNORED_DIRS:
            continue
        if len(parts) == 1 and parts[0] in IGNORED_FILES:
            continue
        pages.add(str(rel))
    return pages


def collect_index_pages():
    """Extract all relative .md links from index.md."""
    pages = set()
    text = INDEX_FILE.read_text(encoding="utf-8")
    for match in re.finditer(r"\[.*?\]\(([^)]+\.md)\)", text):
        href = match.group(1)
        # Normalise: strip leading ./ if present
        href = href.lstrip("./")
        pages.add(href)
    return pages


def main():
    disk = collect_disk_pages()
    indexed = collect_index_pages()

    missing_from_index = sorted(disk - indexed)
    stale_in_index = sorted(indexed - disk)

    ok = True

    if missing_from_index:
        ok = False
        print(f"\n[MISSING FROM INDEX] {len(missing_from_index)} page(s) on disk not in wiki/index.md:")
        for p in missing_from_index:
            print(f"  - {p}")

    if stale_in_index:
        ok = False
        print(f"\n[STALE INDEX ENTRIES] {len(stale_in_index)} entry(ies) in index.md with no matching file:")
        for p in stale_in_index:
            print(f"  - {p}")

    if ok:
        print(f"[OK] index.md accounts for all {len(disk)} wiki pages.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
