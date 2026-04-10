#!/usr/bin/env python3
"""Report wiki pages whose `as_of` date has exceeded the staleness threshold.

Thresholds per page type live in config.yml under `stale_thresholds_days`.
Include/exclude paths live in config.yml under `stale`.

Usage:
    python scripts/stale.py            # full report
    python scripts/stale.py --json     # machine-readable
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from _lib import (  # type: ignore
    VAULT_ROOT,
    iter_pages,
    load_config,
    relativize,
    resolve_path,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    cfg = load_config()
    thresholds: dict = cfg.get("stale_thresholds_days") or {}
    default_days = int(thresholds.get("default", 30))
    stale_cfg: dict = cfg.get("stale") or {}
    include = [resolve_path(p) for p in (stale_cfg.get("include_paths") or ["wiki"])]
    exclude = [resolve_path(p) for p in (stale_cfg.get("exclude_paths") or [])]

    today = date.today()
    pages = iter_pages(include, exclude=exclude)

    results = []
    for page in pages:
        page_type = page.type or "default"
        threshold = int(thresholds.get(page_type, default_days))
        as_of = page.as_of
        if as_of is None:
            results.append(
                {
                    "path": page.rel,
                    "type": page_type,
                    "as_of": None,
                    "age_days": None,
                    "threshold": threshold,
                    "status": "missing_as_of",
                }
            )
            continue
        age = (today - as_of).days
        if age > threshold * 2:
            status = "stale"
        elif age > threshold:
            status = "aging"
        else:
            status = "fresh"
        results.append(
            {
                "path": page.rel,
                "type": page_type,
                "as_of": as_of.isoformat(),
                "age_days": age,
                "threshold": threshold,
                "status": status,
            }
        )

    if args.json:
        json.dump(results, sys.stdout, indent=2)
        print()
        return 0

    # Human report: group by status.
    def _by_status(s: str):
        return sorted(
            (r for r in results if r["status"] == s),
            key=lambda r: (r["age_days"] is None, -(r["age_days"] or 0)),
        )

    stale_rows = _by_status("stale")
    aging_rows = _by_status("aging")
    missing_rows = _by_status("missing_as_of")
    fresh_count = sum(1 for r in results if r["status"] == "fresh")

    total = len(results)
    print(f"Stale report  ({today.isoformat()})")
    print(f"Scanned: {total} pages")
    print(
        f"  stale: {len(stale_rows)}   aging: {len(aging_rows)}   "
        f"missing_as_of: {len(missing_rows)}   fresh: {fresh_count}"
    )
    print()

    if stale_rows:
        print("STALE (age > 2x threshold — verify before trusting)")
        for r in stale_rows:
            print(
                f"  {r['path']:<55} "
                f"type={r['type']:<10} "
                f"age={r['age_days']}d  threshold={r['threshold']}d"
            )
        print()

    if aging_rows:
        print("AGING (age > threshold — may be outdated)")
        for r in aging_rows:
            print(
                f"  {r['path']:<55} "
                f"type={r['type']:<10} "
                f"age={r['age_days']}d  threshold={r['threshold']}d"
            )
        print()

    if missing_rows:
        print("MISSING `as_of` (frontmatter needs attention)")
        for r in missing_rows:
            print(f"  {r['path']}  (type={r['type']})")
        print()

    if not stale_rows and not aging_rows and not missing_rows:
        print("All scanned pages are fresh.")

    return 0 if not stale_rows else 1


if __name__ == "__main__":
    sys.exit(main())
