#!/usr/bin/env python3
"""Run every cheap maintenance script and print a combined report.

Chains: stale.py, orphans.py, link_check.py, tag_compliance.py.

Usage:
    python scripts/lint_all.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
SCRIPTS = ["stale.py", "orphans.py", "link_check.py", "tag_compliance.py"]


def main() -> int:
    exit_codes = []
    for name in SCRIPTS:
        print("=" * 70)
        print(f"  {name}")
        print("=" * 70, flush=True)
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / name)],
            check=False,
        )
        exit_codes.append(result.returncode)
        print(flush=True)

    print("=" * 70)
    print("  lint summary")
    print("=" * 70)
    any_issues = any(code != 0 for code in exit_codes)
    for name, code in zip(SCRIPTS, exit_codes):
        status = "OK" if code == 0 else "issues"
        print(f"  {name:<22} {status}")
    return 1 if any_issues else 0


if __name__ == "__main__":
    sys.exit(main())
