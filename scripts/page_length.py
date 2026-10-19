#!/usr/bin/env python3
"""
page_length.py — find wiki pages that have outgrown their type's body-word
                 ceiling, or that carry the structural signals of a page that
                 should be split (see AGENTS.md → "Page length and splitting").

Checks, all configured in config.yml → page_length:

  1. body ceiling      body words (excluding frontmatter and the sections in
                       `exclude_sections`) above `body_word_ceiling.<type>`;
                       within `warn_tolerance` it is a warning only, above
                       `split_required_ratio` it is marked "split required"
  2. flat section      a single `##` section above `flat_section_max_words`
                       with no `###` subheads
  3. dated heading     a `##`/`###` heading that names a month-and-year
                       ("(August 2026)") or a "cluster" — an ingest batch
                       rather than a concept. The schema-mandated
                       "(as of YYYY-MM-DD)" status stamp is not a trigger.
  4. state-of bullets  a leader bullet on a state-of page longer than
                       `state_of_bullet_max_chars`

Usage:
    python3 scripts/page_length.py           # human report
    python3 scripts/page_length.py --json    # machine-readable

Exit code 1 if any finding other than a warning.
"""

from __future__ import annotations

import argparse
import json
import re
import sys

from _lib import WIKI_ROOT, iter_pages, load_config, require_config  # type: ignore

IGNORED_DIRS = {"history", "_schema", "sources"}
IGNORED_FILES = {"index.md", "log.md"}

H2_RE = re.compile(r"^## (.+?)\s*$", re.MULTILINE)
H3_RE = re.compile(r"^### ", re.MULTILINE)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
MONTHS = (
    "january|february|march|april|may|june|july|august|september|october|"
    "november|december"
)
# "(as of YYYY-MM-DD)" is the schema-mandated status stamp and is NOT a
# trigger; "(August 2026)", "August 2026 …", and "… cluster" are.
DATED_HEADING_RE = re.compile(
    rf"\((?:{MONTHS})\s+20\d\d\)|\b(?:{MONTHS})\s+20\d\d\b|\bcluster\b",
    re.IGNORECASE,
)
AS_OF_RE = re.compile(r"\bas of\b", re.IGNORECASE)


def _words(text: str) -> int:
    return len(FENCE_RE.sub(" ", text).split())


def _sections(body: str) -> list[tuple[str, str]]:
    """Split a page body into (heading, text) pairs for each `##` section.
    Text before the first `##` is returned under heading ''."""
    out: list[tuple[str, str]] = []
    matches = list(H2_RE.finditer(body))
    if not matches:
        return [("", body)]
    out.append(("", body[: matches[0].start()]))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out.append((m.group(1).strip(), body[m.end() : end]))
    return out


def check_page(page, cfg: dict) -> list[dict]:
    findings: list[dict] = []
    ceilings = cfg["body_word_ceiling"]
    excluded = {s.lower() for s in cfg["exclude_sections"]}
    flat_max = int(cfg["flat_section_max_words"])
    bullet_max = int(cfg["state_of_bullet_max_chars"])
    ptype = page.type or "default"
    ceiling = int(ceilings.get(ptype, ceilings["default"]))

    sections = _sections(page.body)
    body_words = sum(
        _words(text) for heading, text in sections if heading.lower() not in excluded
    )
    if body_words > ceiling:
        ratio = body_words / ceiling
        detail = f"{body_words} body words > {ceiling} ceiling for type {ptype} ({ratio:.0%})"
        if ratio > float(cfg["split_required_ratio"]):
            detail += " — split required"
        findings.append(
            {
                "check": "body-ceiling",
                "detail": detail,
                "warn": ratio <= float(cfg["warn_tolerance"]),
            }
        )

    for heading, text in sections:
        if not heading or heading.lower() in excluded:
            continue
        w = _words(text)
        if w > flat_max and not H3_RE.search(text):
            findings.append(
                {
                    "check": "flat-section",
                    "detail": f"'## {heading}' is {w} words with no ### subheads (max {flat_max})",
                }
            )

    for m in re.finditer(r"^#{2,3} (.+?)\s*$", page.body, re.MULTILINE):
        heading = m.group(1)
        if heading.lower() in excluded or AS_OF_RE.search(heading):
            continue
        if DATED_HEADING_RE.search(heading):
            findings.append(
                {
                    "check": "dated-heading",
                    "detail": f"heading names a date or cluster, not an idea: '{heading}'",
                }
            )

    if ptype == "state-of":
        for heading, text in sections:
            if heading.lower() in excluded or not heading:
                continue
            for line in text.splitlines():
                if line.startswith("- ") and len(line) > bullet_max:
                    findings.append(
                        {
                            "check": "state-of-bullet",
                            "detail": f"{len(line)}-char leader bullet under '## {heading}': "
                            f"{line[:70].rstrip()}…",
                        }
                    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    cfg = require_config(load_config(), "page_length")
    for key in (
        "body_word_ceiling",
        "flat_section_max_words",
        "state_of_bullet_max_chars",
        "exclude_sections",
        "warn_tolerance",
        "split_required_ratio",
    ):
        require_config({"page_length": cfg}, f"page_length.{key}")

    results: dict[str, list[dict]] = {}
    pages = iter_pages(
        [WIKI_ROOT], exclude=[WIKI_ROOT / d for d in IGNORED_DIRS]
    )
    for page in pages:
        if page.path.name in IGNORED_FILES and page.path.parent == WIKI_ROOT:
            continue
        findings = check_page(page, cfg)
        if findings:
            results[page.rel] = findings

    if args.json:
        json.dump(results, sys.stdout, indent=2)
        print()
        return 1 if failing(results) else 0

    print("Page length and split triggers")
    print(f"pages scanned: {len(pages)}")
    print(f"pages with findings: {len(results)}")
    print()
    by_check: dict[str, int] = {}
    for rel, findings in sorted(results.items()):
        print(rel)
        for f in findings:
            by_check[f["check"]] = by_check.get(f["check"], 0) + 1
            tag = f"warn: {f['check']}" if f.get("warn") else f["check"]
            print(f"  [{tag}] {f['detail']}")
        print()
    if by_check:
        print("by check: " + ", ".join(f"{k}={v}" for k, v in sorted(by_check.items())))
    else:
        print("No page exceeds its ceiling or shows a split trigger.")
    return 1 if failing(results) else 0


def failing(results: dict[str, list[dict]]) -> bool:
    """Warnings (body within warn_tolerance) never fail the lint."""
    return any(not f.get("warn") for fs in results.values() for f in fs)


if __name__ == "__main__":
    sys.exit(main())
