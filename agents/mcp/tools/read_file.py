from __future__ import annotations

from pathlib import Path


def read_text_excerpt(path: Path, start_line: int = 1, end_line: int = 220) -> str:
    with path.open("r", encoding="utf-8") as handle:
        lines = handle.readlines()
    start = max(start_line - 1, 0)
    end = min(end_line, len(lines))
    excerpt = "".join(lines[start:end])
    return excerpt.strip()

