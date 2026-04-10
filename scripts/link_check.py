#!/usr/bin/env python3
"""Report broken [[wikilinks]] across the wiki.

A [[target]] is broken if no file in wiki/ has a matching slug or relative path.

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
    VAULT_ROOT,
    extract_wikilinks,
    iter_pages,
)


def _build_target_index(wiki_root: Path) -> set[str]:
    """Return the set of valid lowercase wikilink targets for all pages in wiki/."""
    targets: set[str] = set()
    for p in wiki_root.rglob("*.md"):
        rel = p.relative_to(wiki_root).with_suffix("")
        targets.add(rel.as_posix().lower())
        targets.add(p.stem.lower())
        parts = rel.parts
        for i in range(1, len(parts)):
            targets.add("/".join(parts[i:]).lower())
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    wiki_root = VAULT_ROOT / "wiki"
    valid_targets = _build_target_index(wiki_root)

    broken: list[dict] = []
    pages = iter_pages([wiki_root])
    for page in pages:
        for target in extract_wikilinks(page.body):
            t = target.strip().lower()
            # Strip heading anchors (e.g. page#heading).
            t_core = t.split("#", 1)[0]
            if not t_core:
                continue
            if t_core not in valid_targets:
                broken.append({"source": page.rel, "target": target.strip()})

    if args.json:
        json.dump({"broken": broken, "scanned": len(pages)}, sys.stdout, indent=2)
        print()
        return 0

    print(f"Link check")
    print(f"Scanned: {len(pages)} pages")
    print(f"Broken: {len(broken)}")
    print()
    if broken:
        for b in broken:
            print(f"  {b['source']:<55} -> [[{b['target']}]]")
    else:
        print("All wikilinks resolve.")
    return 0 if not broken else 1


if __name__ == "__main__":
    sys.exit(main())
