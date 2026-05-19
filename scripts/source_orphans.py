#!/usr/bin/env python3
"""
source_orphans.py — find wiki/sources/ pages whose slug appears in no wiki page's
                    `sources:` frontmatter field.

A source orphan means the source summary page exists but no wiki page claims it
as a backing source. This can happen when a source is created but the derived wiki
pages are not updated, or when a wiki page's frontmatter is missing the reference.

Reports:
  - Orphaned source files (slug not referenced anywhere in wiki/ frontmatter)
  - Also reports sources referenced in frontmatter with no matching source file
    (reverse: broken source references)
"""

import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent / "wiki"
SOURCES_DIR = WIKI_ROOT / "sources"


def slug_from_path(path: Path) -> str:
    """Return the stem (filename without .md) as the source slug."""
    return path.stem


def collect_source_slugs() -> set[str]:
    slugs = set()
    for path in SOURCES_DIR.rglob("*.md"):
        slugs.add(slug_from_path(path))
    return slugs


def collect_referenced_slugs() -> set[str]:
    """Scan all wiki pages (excluding sources/) for `sources: [...]` frontmatter."""
    referenced = set()
    frontmatter_re = re.compile(r"^sources:\s*\[([^\]]*)\]", re.MULTILINE)
    inline_source_re = re.compile(r"[\w-]+")

    for path in WIKI_ROOT.rglob("*.md"):
        # Skip source pages themselves and history
        rel = path.relative_to(WIKI_ROOT)
        if rel.parts[0] in ("sources", "history", "_schema"):
            continue

        text = path.read_text(encoding="utf-8")
        for match in frontmatter_re.finditer(text):
            for slug in inline_source_re.findall(match.group(1)):
                referenced.add(slug)

    return referenced


def main():
    source_slugs = collect_source_slugs()
    referenced_slugs = collect_referenced_slugs()

    orphaned = sorted(source_slugs - referenced_slugs)
    broken_refs = sorted(referenced_slugs - source_slugs)

    ok = True

    if orphaned:
        ok = False
        print(f"\n[ORPHANED SOURCES] {len(orphaned)} source file(s) not referenced by any wiki page:")
        for slug in orphaned:
            # Find the actual path for context
            matches = list(SOURCES_DIR.rglob(f"{slug}.md"))
            path_str = str(matches[0].relative_to(WIKI_ROOT)) if matches else slug
            print(f"  - {path_str}")

    if broken_refs:
        ok = False
        print(f"\n[BROKEN SOURCE REFS] {len(broken_refs)} slug(s) in wiki frontmatter with no source file:")
        for slug in broken_refs:
            print(f"  - {slug}")

    if ok:
        print(f"[OK] All {len(source_slugs)} source files are referenced; all {len(referenced_slugs)} frontmatter slugs have matching files.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
