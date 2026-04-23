from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tomllib


@dataclass
class PathConfig:
    repo_root: Path
    index_path: Path
    personal_root: Path
    wiki_root: Path
    log_path: Path
    proposals_root: Path
    runtime_logs_dir: Path
    runtime_log_file: Path
    query_history_dir: Path


@dataclass
class TransportConfig:
    enable_local_mcp: bool
    enable_remote_mcp: bool


@dataclass
class PersonalWikiConfig:
    provider: str
    model: str
    max_steps: int
    max_files: int
    max_search_results: int
    include_personal_by_default: bool
    require_index_first: bool
    stale_after_days: int
    hard_stale_after_days: int
    return_consulted_pages: bool
    return_gaps: bool
    answer_style: str
    log_level: str
    log_tool_calls: bool
    log_model_io: bool
    persist_query_history: bool
    transport: TransportConfig
    paths: PathConfig


def _deep_merge(base: dict, override: dict) -> dict:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _load_toml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("rb") as handle:
        return tomllib.load(handle)


def load_config(base_dir: Path | None = None) -> PersonalWikiConfig:
    base_dir = (base_dir or Path(__file__).resolve().parent).resolve()
    default_path = base_dir / "config.default.toml"
    local_path = base_dir / "config.local.toml"

    raw = _deep_merge(_load_toml(default_path), _load_toml(local_path))
    app = raw["personal_wiki_agent"]
    transport = app["transport"]
    paths = app["paths"]

    def resolve(path_value: str) -> Path:
        return (base_dir / path_value).resolve()

    return PersonalWikiConfig(
        provider=app["provider"],
        model=app["model"],
        max_steps=int(app["max_steps"]),
        max_files=int(app["max_files"]),
        max_search_results=int(app["max_search_results"]),
        include_personal_by_default=bool(app["include_personal_by_default"]),
        require_index_first=bool(app["require_index_first"]),
        stale_after_days=int(app["stale_after_days"]),
        hard_stale_after_days=int(app["hard_stale_after_days"]),
        return_consulted_pages=bool(app["return_consulted_pages"]),
        return_gaps=bool(app["return_gaps"]),
        answer_style=app["answer_style"],
        log_level=app["log_level"],
        log_tool_calls=bool(app["log_tool_calls"]),
        log_model_io=bool(app["log_model_io"]),
        persist_query_history=bool(app["persist_query_history"]),
        transport=TransportConfig(
            enable_local_mcp=bool(transport["enable_local_mcp"]),
            enable_remote_mcp=bool(transport["enable_remote_mcp"]),
        ),
        paths=PathConfig(
            repo_root=resolve(paths["repo_root"]),
            index_path=resolve(paths["index_path"]),
            personal_root=resolve(paths["personal_root"]),
            wiki_root=resolve(paths["wiki_root"]),
            log_path=resolve(paths["log_path"]),
            proposals_root=resolve(paths["proposals_root"]),
            runtime_logs_dir=resolve(paths["runtime_logs_dir"]),
            runtime_log_file=resolve(paths["runtime_log_file"]),
            query_history_dir=resolve(paths["query_history_dir"]),
        ),
    )
