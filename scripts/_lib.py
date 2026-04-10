"""Shared helpers for AI Wiki maintenance scripts.

Zero external dependencies by default — plain stdlib. YAML is parsed with a
minimal frontmatter parser rather than pyyaml so nothing breaks on a clean
machine. Scripts that need fancy features can import pyyaml themselves.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# All scripts assume they live at <vault>/scripts/<name>.py and compute the
# vault root from __file__. No cwd assumptions.
VAULT_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = VAULT_ROOT / "wiki"
CONFIG_PATH = VAULT_ROOT / "config.yml"


# ---------------------------------------------------------------------------
# Minimal YAML reader
# ---------------------------------------------------------------------------
#
# Supports the subset of YAML we actually use in this wiki:
#   key: value
#   key: [a, b, c]
#   key:
#     - a
#     - b
#   nested:
#     key: value
#
# That's enough for config.yml and all frontmatter. If this ever needs to
# handle quoted strings with colons or multi-line blocks, switch to pyyaml.


def _parse_scalar(value: str):
    value = value.strip()
    if not value:
        return ""
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(v) for v in inner.split(",")]
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    if value.lower() in ("null", "~", ""):
        return None
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        pass
    # Date: YYYY-MM-DD
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    return value


def parse_yaml(text: str) -> dict:
    """Minimal YAML parser for the subset we actually use.

    Handles:
      key: value
      key: [inline, list]
      key:
        nested: value
      key:
        - list
        - items

    Not supported (and not used by this wiki):
      - list of dicts
      - multi-line strings
      - anchors / aliases
      - flow-style mappings

    If you hit a config that needs more, switch to pyyaml.
    """
    # Strip comments outside of strings, drop empty lines.
    lines: list[str] = []
    for raw in text.splitlines():
        in_str = False
        out: list[str] = []
        for ch in raw:
            if ch in ('"', "'"):
                in_str = not in_str
            if ch == "#" and not in_str:
                break
            out.append(ch)
        line = "".join(out).rstrip()
        if line.strip():
            lines.append(line)

    def indent_of(line: str) -> int:
        return len(line) - len(line.lstrip(" "))

    def parse_block(i: int) -> tuple[object, int]:
        """Parse the block starting at lines[i]. Returns (value, next_index)."""
        if i >= len(lines):
            return {}, i
        base_indent = indent_of(lines[i])
        first_content = lines[i].strip()
        is_list = first_content.startswith("- ")

        if is_list:
            result_list: list = []
            while i < len(lines):
                line = lines[i]
                indent = indent_of(line)
                if indent < base_indent:
                    break
                if indent > base_indent:
                    i += 1
                    continue
                content = line.strip()
                if not content.startswith("- "):
                    break
                item = content[2:].strip()
                if item == "":
                    nested, i = parse_block(i + 1)
                    result_list.append(nested)
                else:
                    result_list.append(_parse_scalar(item))
                    i += 1
            return result_list, i

        result_dict: dict = {}
        while i < len(lines):
            line = lines[i]
            indent = indent_of(line)
            if indent < base_indent:
                break
            if indent > base_indent:
                i += 1
                continue
            content = line.strip()
            if content.startswith("- "):
                break
            if ":" not in content:
                i += 1
                continue
            key, _, value = content.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                nested, i = parse_block(i + 1)
                result_dict[key] = nested
            else:
                result_dict[key] = _parse_scalar(value)
                i += 1
        return result_dict, i

    root, _ = parse_block(0)
    return root if isinstance(root, dict) else {}


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class Page:
    path: Path
    frontmatter: dict
    body: str

    @property
    def rel(self) -> str:
        return str(self.path.relative_to(VAULT_ROOT))

    @property
    def slug(self) -> str:
        return self.path.stem

    @property
    def type(self) -> str | None:
        return self.frontmatter.get("type")

    @property
    def as_of(self) -> date | None:
        value = self.frontmatter.get("as_of")
        if isinstance(value, date):
            return value
        if isinstance(value, str):
            try:
                return date.fromisoformat(value)
            except ValueError:
                return None
        return None

    @property
    def tags(self) -> list[str]:
        return list(self.frontmatter.get("tags") or [])

    @property
    def domains(self) -> list[str]:
        return list(self.frontmatter.get("domains") or [])

    @property
    def subcategory(self) -> str | None:
        return self.frontmatter.get("subcategory")


def read_page(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if m:
        fm = parse_yaml(m.group(1))
        body = text[m.end():]
    else:
        fm = {}
        body = text
    return Page(path=path, frontmatter=fm or {}, body=body)


def iter_pages(roots: list[Path], exclude: list[Path] | None = None) -> list[Page]:
    """Walk one or more directories and return all *.md pages."""
    exclude = [e.resolve() for e in (exclude or [])]
    pages: list[Page] = []
    for root in roots:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.md")):
            resolved = p.resolve()
            if any(
                resolved == ex or ex in resolved.parents for ex in exclude
            ):
                continue
            try:
                pages.append(read_page(p))
            except Exception as e:  # noqa: BLE001
                print(f"warn: failed to parse {p}: {e}", file=sys.stderr)
    return pages


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    return parse_yaml(CONFIG_PATH.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Wikilink extraction
# ---------------------------------------------------------------------------


WIKILINK_RE = re.compile(r"\[\[([^\[\]\|]+?)(?:\|[^\[\]]+)?\]\]")


def extract_wikilinks(text: str) -> list[str]:
    """Return all [[wikilink]] targets in the text (without pipe aliases)."""
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]


# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------


def resolve_path(path_like: str) -> Path:
    p = Path(path_like)
    if not p.is_absolute():
        p = VAULT_ROOT / p
    return p


def relativize(path: Path) -> str:
    try:
        return str(path.relative_to(VAULT_ROOT))
    except ValueError:
        return str(path)
