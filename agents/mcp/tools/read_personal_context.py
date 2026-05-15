from __future__ import annotations

from pathlib import Path

from .search_repo import search_markdown_paths


def search_personal_context(personal_root: Path, query: str, limit: int) -> list[dict[str, str | int]]:
    return search_markdown_paths(personal_root, query, limit)

