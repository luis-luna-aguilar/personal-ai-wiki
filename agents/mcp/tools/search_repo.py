from __future__ import annotations

from pathlib import Path


def search_markdown_paths(root: Path, query: str, limit: int) -> list[dict[str, str | int]]:
    query_terms = [term.lower() for term in query.split() if term.strip()]
    results: list[dict[str, str | int]] = []

    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        score = 0
        rel_text = rel.as_posix().lower()

        for term in query_terms:
            if term in rel_text:
                score += 5

        try:
            preview = path.read_text(encoding="utf-8")[:4000]
        except UnicodeDecodeError:
            continue

        lowered = preview.lower()
        for term in query_terms:
            if term in lowered:
                score += 2

        if score > 0:
            snippet = preview[:300].replace("\n", " ").strip()
            results.append(
                {
                    "path": path.as_posix(),
                    "score": score,
                    "snippet": snippet,
                }
            )

    results.sort(key=lambda item: int(item["score"]), reverse=True)
    return results[:limit]

