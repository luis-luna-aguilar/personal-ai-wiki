#!/usr/bin/env python3
"""Report wiki pages with no inbound internal links.

Scan and exempt paths live in config.yml under `orphans`.

A page is an orphan if:
  - It lives under a scan_paths directory, AND
  - It is NOT under an exempt_paths directory, AND
  - No other page (also under scan_paths) links to it via a relative Markdown link

Usage:
    python scripts/orphans.py           # human report
    python scripts/orphans.py --json    # machine-readable
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

from _lib import (  # type: ignore
    WIKI_ROOT,
    extract_markdown_links,
    iter_pages,
    load_config,
    resolve_path,
)


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
    return rel.with_suffix("").as_posix()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    cfg = load_config()
    orphan_cfg: dict = cfg.get("orphans") or {}
    scan_roots = [resolve_path(p) for p in (orphan_cfg.get("scan_paths") or ["wiki"])]
    exempt = [resolve_path(p).resolve() for p in (orphan_cfg.get("exempt_paths") or [])]

    all_pages = iter_pages(scan_roots)

    wiki_root = WIKI_ROOT

    # Collect all internal link targets used anywhere.
    link_counts: dict[str, int] = defaultdict(int)
    for page in all_pages:
        for target in extract_markdown_links(page.body):
            key = _markdown_target_key(page.path, target, wiki_root)
            if key:
                link_counts[key.lower()] += 1

    # Determine which pages are exempt.
    def is_exempt(p: Path) -> bool:
        resolved = p.resolve()
        for ex in exempt:
            if resolved == ex or ex in resolved.parents:
                return True
        return False

    # For each non-exempt page, check if any of its candidate link-names was used.
    orphans = []
    for page in all_pages:
        if is_exempt(page.path):
            continue
        try:
            candidate = page.path.relative_to(wiki_root).with_suffix("").as_posix().lower()
        except ValueError:
            continue
        if link_counts.get(candidate, 0) > 0:
            continue
        orphans.append(page.rel)

    orphans.sort()

    if args.json:
        json.dump({"orphans": orphans, "scanned": len(all_pages)}, sys.stdout, indent=2)
        print()
        return 0

    print(f"Orphan report")
    print(f"Scanned: {len(all_pages)} pages")
    print(f"Orphans: {len(orphans)}")
    print()
    if orphans:
        for path in orphans:
            print(f"  {path}")
    else:
        print("No orphans.")
    return 0 if not orphans else 1


if __name__ == "__main__":
    sys.exit(main())
