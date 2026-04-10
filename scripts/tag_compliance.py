#!/usr/bin/env python3
"""Check that tags, domains, and subcategories used in wiki pages are declared
in wiki/_schema/.

This is a loose text-based check: any backticked slug (`like-this`) in the
schema file counts as declared. That matches how the schema files are written.

Usage:
    python scripts/tag_compliance.py          # human report
    python scripts/tag_compliance.py --json   # machine-readable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from _lib import (  # type: ignore
    VAULT_ROOT,
    iter_pages,
)

SCHEMA_DIR = VAULT_ROOT / "wiki" / "_schema"

BACKTICKED_SLUG_RE = re.compile(r"`([a-z][a-z0-9\-]*)`")


def _declared_slugs(file: Path) -> set[str]:
    if not file.exists():
        return set()
    text = file.read_text(encoding="utf-8")
    return set(BACKTICKED_SLUG_RE.findall(text))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    declared_tags = _declared_slugs(SCHEMA_DIR / "tags.md")
    declared_domains = _declared_slugs(SCHEMA_DIR / "domains.md")
    declared_subcats = _declared_slugs(SCHEMA_DIR / "subcategories.md")

    tag_violations: dict[str, list[str]] = defaultdict(list)
    domain_violations: dict[str, list[str]] = defaultdict(list)
    subcat_violations: dict[str, list[str]] = defaultdict(list)

    for page in iter_pages([VAULT_ROOT / "wiki"]):
        rel = page.rel
        if "_schema" in rel:
            continue
        for tag in page.tags:
            if tag and tag not in declared_tags:
                tag_violations[tag].append(rel)
        for domain in page.domains:
            if domain and domain not in declared_domains:
                domain_violations[domain].append(rel)
        subcat = page.subcategory
        if subcat and subcat not in declared_subcats:
            subcat_violations[subcat].append(rel)

    result = {
        "undeclared_tags": dict(tag_violations),
        "undeclared_domains": dict(domain_violations),
        "undeclared_subcategories": dict(subcat_violations),
    }

    if args.json:
        json.dump(result, sys.stdout, indent=2)
        print()
        return 0

    total_violations = (
        len(tag_violations) + len(domain_violations) + len(subcat_violations)
    )
    print("Tag / domain / subcategory compliance")
    print(
        f"declared: {len(declared_tags)} tags, "
        f"{len(declared_domains)} domains, "
        f"{len(declared_subcats)} subcategories"
    )
    print(f"undeclared terms in use: {total_violations}")
    print()

    def _report(label: str, violations: dict[str, list[str]]):
        if not violations:
            return
        print(f"Undeclared {label}:")
        for term, pages in sorted(violations.items()):
            print(f"  {term}")
            for pg in pages:
                print(f"      used in {pg}")
        print()

    _report("tags", tag_violations)
    _report("domains", domain_violations)
    _report("subcategories", subcat_violations)

    if total_violations == 0:
        print("All tags, domains, and subcategories are declared.")

    return 0 if total_violations == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
