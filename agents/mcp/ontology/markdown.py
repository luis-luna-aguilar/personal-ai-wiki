from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import re


HISTORY_PART = "history"


@dataclass(frozen=True)
class MarkdownSection:
    path: str
    title: str
    heading: str
    start_line: int
    end_line: int
    text: str


@dataclass(frozen=True)
class MarkdownDocument:
    path: str
    title: str
    content_hash: str
    sections: list[MarkdownSection]


def eligible_wiki_files(wiki_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in wiki_root.rglob("*.md"):
        rel_parts = path.relative_to(wiki_root).parts
        if HISTORY_PART in rel_parts:
            continue
        files.append(path)
    return sorted(files)


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _strip_frontmatter(lines: list[str]) -> tuple[dict[str, str], int]:
    if not lines or lines[0].strip() != "---":
        return {}, 0

    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break
    if end_index is None:
        return {}, 0

    metadata: dict[str, str] = {}
    for line in lines[1:end_index]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, end_index + 1


def _section_title(line: str) -> str | None:
    match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
    if not match:
        return None
    return match.group(2).strip()


def parse_markdown_document(path: Path, repo_root: Path) -> MarkdownDocument:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    metadata, body_start = _strip_frontmatter(lines)
    title = metadata.get("title") or path.stem.replace("-", " ").title()
    rel_path = path.relative_to(repo_root).as_posix()

    section_starts: list[tuple[int, str]] = []
    for index in range(body_start, len(lines)):
        heading = _section_title(lines[index])
        if heading:
            section_starts.append((index, heading))

    if not section_starts:
        body = "\n".join(lines[body_start:]).strip()
        sections = [
            MarkdownSection(
                path=rel_path,
                title=title,
                heading=title,
                start_line=body_start + 1,
                end_line=len(lines),
                text=body,
            )
        ]
    else:
        sections = []
        for offset, (start, heading) in enumerate(section_starts):
            end = section_starts[offset + 1][0] if offset + 1 < len(section_starts) else len(lines)
            section_text = "\n".join(lines[start:end]).strip()
            if not section_text:
                continue
            sections.append(
                MarkdownSection(
                    path=rel_path,
                    title=title,
                    heading=heading,
                    start_line=start + 1,
                    end_line=end,
                    text=section_text,
                )
            )

    return MarkdownDocument(
        path=rel_path,
        title=title,
        content_hash=content_hash(text),
        sections=sections,
    )
