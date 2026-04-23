from __future__ import annotations

from pathlib import Path


def collect_recent_changes(log_path: Path, proposals_root: Path, limit: int) -> dict[str, list[str]]:
    log_items: list[str] = []
    proposal_items: list[str] = []

    if log_path.exists():
        try:
            log_lines = [line.strip() for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
            log_items = log_lines[-limit:]
        except UnicodeDecodeError:
            log_items = []

    applied_root = proposals_root / "applied"
    if applied_root.exists():
        proposal_items = sorted(
            [path.name for path in applied_root.glob("*.md")],
            reverse=True,
        )[:limit]

    return {
        "wiki_log": log_items,
        "applied_proposals": proposal_items,
    }

