#!/usr/bin/env python3
"""
raw_orphans.py — find raw/ source files that no triage, proposal, or wiki page
                 accounts for.

Every file in raw/ should be traceable to a decision: a source page under
wiki/sources/, a proposal (pending, applied, or rejected), or a triage file that
listed it (ingested or skipped). A raw file matching none of these was fetched
and then dropped, so its content may be missing from the wiki.

A raw file counts as accounted for when any of these appear anywhere in
proposals/ or wiki/:
  - its path (raw/...)
  - its `url:` value
  - for X/Twitter URLs, the status/article id
Raw files whose URL matches another raw file that is accounted for are reported
separately as duplicates (safe to delete).

Usage:
    python3 scripts/raw_orphans.py

Exit code 1 if any unaccounted raw file exists (duplicates alone don't fail).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"^url:\s*(\S+)", re.MULTILINE)
X_ID_RE = re.compile(r"/(?:status|article)/(\d+)")


def keys_for(path: Path) -> tuple[str, list[str]]:
    rel = path.relative_to(ROOT).as_posix()
    m = URL_RE.search(path.read_text(encoding="utf-8", errors="ignore")[:3000])
    keys = []
    if m:
        url = m.group(1).rstrip("/")
        keys.append(url)
        x = X_ID_RE.search(url)
        if x:
            keys.append(x.group(1))
    return rel, keys


def main() -> int:
    corpus = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for d in ("proposals", "wiki")
        for p in (ROOT / d).rglob("*.md")
    )
    raws = [p for p in (ROOT / "raw").rglob("*.md") if "assets" not in p.parts]
    unaccounted, by_key = [], {}
    for p in raws:
        rel, keys = keys_for(p)
        if rel in corpus or any(k in corpus for k in keys):
            for k in keys:
                by_key.setdefault(k, rel)
            continue
        unaccounted.append((rel, keys))

    dupes = [(r, by_key[k[0]]) for r, k in unaccounted if k and k[0] in by_key]
    orphans = [r for r, k in unaccounted if not (k and k[0] in by_key)]

    print(f"Raw files scanned: {len(raws)}")
    print(f"Duplicates of an accounted-for raw file: {len(dupes)}")
    for r, other in sorted(dupes):
        print(f"  - {r}  (same URL as {other})")
    print(f"Unaccounted (never triaged, proposed, or summarized): {len(orphans)}")
    for r in sorted(orphans):
        print(f"  - {r}")
    if not orphans:
        print("\nEvery raw file is accounted for.")
    # Duplicates are reported for cleanup but don't fail the lint.
    return 1 if orphans else 0


if __name__ == "__main__":
    sys.exit(main())
