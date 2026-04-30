#!/usr/bin/env python3
"""Report broken internal links across the wiki.

A Markdown link is broken if its relative .md path does not resolve inside wiki/.
Editor-specific wiki link syntax is invalid in wiki page bodies.

Usage:
    python scripts/link_check.py          # human report
    python scripts/link_check.py --json   # machine-readable
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _lib import (  # type: ignore
    WIKILINK_RE,
    WIKI_ROOT,
    extract_markdown_links,
    iter_pages,
)


def _build_target_index(wiki_root: Path) -> set[str]:
    """Return the set of valid lowercase wiki-relative Markdown targets."""
    return {
        p.relative_to(wiki_root).with_suffix("").as_posix().lower()
        for p in wiki_root.rglob("*.md")
    }


def _markdown_target_key(source_path: Path, target: str, wiki_root: Path) -> str | None:
    """Return a wiki-relative key for an internal Markdown link target."""
    if not target or target.startswith("#"):
        return None
    if "://" in target or target.startswith(("mailto:", "tel:")):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target.endswith(".md"):
        return None

    resolved = (source_path.parent / target).resolve()
    try:
        rel = resolved.relative_to(wiki_root.resolve())
    except ValueError:
        return None
    return rel.with_suffix("").as_posix().lower()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    wiki_root = WIKI_ROOT
    valid_targets = _build_target_index(wiki_root)

    broken: list[dict] = []
    invalid_syntax: list[dict] = []
    pages = iter_pages([wiki_root])
    for page in pages:
        for match in WIKILINK_RE.finditer(page.body):
            invalid_syntax.append({"source": page.rel, "target": match.group(0)})
        for target in extract_markdown_links(page.body):
            key = _markdown_target_key(page.path, target, wiki_root)
            if not key:
                continue
            if key not in valid_targets:
                broken.append({"source": page.rel, "target": target.strip()})

    if args.json:
        json.dump(
            {
                "broken": broken,
                "invalid_syntax": invalid_syntax,
                "scanned": len(pages),
            },
            sys.stdout,
            indent=2,
        )
        print()
        return 0

    print(f"Link check")
    print(f"Scanned: {len(pages)} pages")
    print(f"Broken: {len(broken)}")
    print(f"Invalid syntax: {len(invalid_syntax)}")
    print()
    if broken:
        print("Broken Markdown links:")
        for b in broken:
            print(f"  {b['source']:<55} -> {b['target']}")
    if invalid_syntax:
        print("Invalid editor-specific links:")
        for b in invalid_syntax:
            print(f"  {b['source']:<55} -> {b['target']}")
    if not broken and not invalid_syntax:
        print("All internal links resolve.")
    return 0 if not broken and not invalid_syntax else 1


if __name__ == "__main__":
    sys.exit(main())
