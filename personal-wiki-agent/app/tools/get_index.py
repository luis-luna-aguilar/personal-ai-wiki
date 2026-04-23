from __future__ import annotations

from pathlib import Path

from .read_file import read_text_excerpt


def get_index_content(index_path: Path) -> str:
    return read_text_excerpt(index_path, 1, 260)

