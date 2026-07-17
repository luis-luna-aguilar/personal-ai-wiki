from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
import re
import traceback
from time import time
from typing import Any
from uuid import uuid4

from deepagents import create_deep_agent

from .config import PersonalWikiConfig, load_config
from .models import ensure_required_credentials, prepare_provider_environment
from .output_schema import ConsultedPage, Gap, QueryResponse
from .runtime_logging import configure_logging, write_error_artifact, write_query_artifact
from .tools.get_index import get_index_content
from .tools.read_file import read_text_excerpt
from .tools.read_personal_context import search_personal_context
from .tools.recent_changes import collect_recent_changes
from .tools.search_repo import search_markdown_paths


def _parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    frontmatter_text = parts[1]
    result: dict[str, str] = {}
    for line in frontmatter_text.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def _extract_text_content(message_content: Any) -> str:
    if isinstance(message_content, str):
        return message_content
    if isinstance(message_content, list):
        parts: list[str] = []
        for item in message_content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                text = item.get("text")
                if isinstance(text, str):
                    parts.append(text)
        return "\n".join(parts).strip()
    return str(message_content)


def _strip_code_fences(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if len(lines) >= 3:
            return "\n".join(lines[1:-1]).strip()
    return stripped


def _extract_json_candidate(text: str) -> str | None:
    fenced_match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL | re.IGNORECASE)
    if fenced_match:
        return fenced_match.group(1).strip()

    start = text.find("{")
    if start == -1:
        return None

    depth = 0
    in_string = False
    escape = False
    for index, char in enumerate(text[start:], start=start):
        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1].strip()
    return None


class QuerySession:
    def __init__(self, config: PersonalWikiConfig, logger: logging.Logger) -> None:
        self.config = config
        self.logger = logger
        self._consulted: dict[str, ConsultedPage] = {}
        self._deep_read_paths: set[str] = set()

    def consulted_pages(self) -> list[ConsultedPage]:
        return list(self._consulted.values())

    def _resolve_repo_path(self, path: str) -> Path:
        raw = path.strip().strip('"').strip("'")
        candidate = Path(raw)
        if candidate.is_absolute():
            try:
                target = candidate.resolve()
                target.relative_to(self.config.paths.repo_root)
            except ValueError:
                # Models often emit repo-relative paths with a leading slash,
                # e.g. "/wiki/state-of/coding.md". Treat those as repo-relative.
                target = (self.config.paths.repo_root / raw.lstrip("/")).resolve()
        else:
            target = (self.config.paths.repo_root / candidate).resolve()

        try:
            target.relative_to(self.config.paths.repo_root)
        except ValueError as exc:
            raise ValueError("Path escapes the repository root.") from exc
        return target

    def _normalize_search_result(self, item: dict[str, Any]) -> dict[str, Any]:
        normalized = dict(item)
        raw_path = item.get("path")
        if isinstance(raw_path, str):
            try:
                normalized["path"] = Path(raw_path).resolve().relative_to(
                    self.config.paths.repo_root
                ).as_posix()
            except ValueError:
                normalized["path"] = raw_path
        return normalized

    def _maybe_track_page(self, path: Path, why_used: str) -> None:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return

        metadata = _parse_frontmatter(text)
        title = metadata.get("title") or path.stem.replace("-", " ").title()
        as_of = metadata.get("as_of", "")
        rel_path = path.relative_to(self.config.paths.repo_root).as_posix()
        self._consulted[rel_path] = ConsultedPage(
            path=rel_path,
            title=title,
            as_of=as_of,
            why_used=why_used,
        )

    def preload_index(self) -> str:
        index_path = self.config.paths.index_path
        self._maybe_track_page(index_path, "Repository index loaded before agent exploration")
        if self.config.log_tool_calls:
            self.logger.info("tool=preload_index path=%s", index_path)
        return get_index_content(index_path)

    def get_index(self) -> str:
        """Read the wiki index. Use this to orient yourself before deeper reads."""
        index_path = self.config.paths.index_path
        self._maybe_track_page(index_path, "Wiki index consulted for routing")
        if self.config.log_tool_calls:
            self.logger.info("tool=get_index path=%s", index_path)
        return get_index_content(index_path)

    def search_repo(self, query: str, scope: str = "wiki", limit: int = 8) -> list[dict[str, str | int]]:
        """Search markdown files by path and content. Use this to decide which files to read."""
        roots = []
        if scope in {"wiki", "all"}:
            roots.append(self.config.paths.wiki_root)
        if scope in {"personal", "all"}:
            roots.append(self.config.paths.personal_root)

        results: list[dict[str, str | int]] = []
        for root in roots:
            results.extend(search_markdown_paths(root, query, limit))
        results.sort(key=lambda item: int(item["score"]), reverse=True)
        if self.config.log_tool_calls:
            self.logger.info(
                "tool=search_repo scope=%s limit=%s query=%s results=%s",
                scope,
                limit,
                query,
                len(results[:limit]),
            )
        return [self._normalize_search_result(item) for item in results[:limit]]

    def read_file(self, path: str, start_line: int = 1, end_line: int = 220) -> dict[str, Any]:
        """Read a repository markdown file selectively. Prefer targeted file reads."""
        target = self._resolve_repo_path(path)
        if not target.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")

        rel_path = target.relative_to(self.config.paths.repo_root).as_posix()
        if rel_path not in self._deep_read_paths and len(self._deep_read_paths) >= self.config.max_files:
            raise ValueError(
                f"max_files limit reached ({self.config.max_files}). "
                f"Refine the search before reading additional files."
            )
        self._deep_read_paths.add(rel_path)

        self._maybe_track_page(target, f"Read during query: lines {start_line}-{end_line}")
        if self.config.log_tool_calls:
            self.logger.info(
                "tool=read_file path=%s start_line=%s end_line=%s deep_reads=%s max_files=%s",
                target,
                start_line,
                end_line,
                len(self._deep_read_paths),
                self.config.max_files,
            )
        excerpt = read_text_excerpt(target, start_line, end_line)
        metadata = _parse_frontmatter(target.read_text(encoding="utf-8"))
        return {
            "path": path,
            "title": metadata.get("title", target.stem.replace("-", " ").title()),
            "as_of": metadata.get("as_of", ""),
            "content": excerpt,
        }

    def read_personal_context(self, query: str, limit: int = 4) -> list[dict[str, str | int]]:
        """Search Luis's personal notes when the task requires opinion, judgment, or advice."""
        results = search_personal_context(self.config.paths.personal_root, query, limit)
        if self.config.log_tool_calls:
            self.logger.info(
                "tool=read_personal_context query=%s limit=%s results=%s",
                query,
                limit,
                len(results),
            )
        return [self._normalize_search_result(item) for item in results]

    def get_recent_changes(self, limit: int = 8) -> dict[str, list[str]]:
        """Summarize recent changes from wiki/log.md and recently applied proposals."""
        if self.config.log_tool_calls:
            self.logger.info("tool=get_recent_changes limit=%s", limit)
        return collect_recent_changes(
            self.config.paths.log_path,
            self.config.paths.proposals_root,
            limit,
        )

    def tools(self) -> list[Any]:
        return [
            self.get_index,
            self.search_repo,
            self.read_file,
            self.read_personal_context,
            self.get_recent_changes,
        ]


class PersonalWikiAgent:
    def __init__(self, base_dir: Path | None = None) -> None:
        self.base_dir = (base_dir or Path(__file__).resolve().parent).resolve()
        self.config = load_config(self.base_dir)
        self.logger = configure_logging(self.config)

    def _load_prompt_piece(self, relative_path: str) -> str:
        path = self.base_dir / relative_path
        return path.read_text(encoding="utf-8").strip()

    def _build_system_prompt(self) -> str:
        query_instructions = self._load_prompt_piece("query_instructions.md")
        system_prompt = self._load_prompt_piece("prompts/system.md")
        answer_format = self._load_prompt_piece("prompts/answer_format.md")
        return "\n\n".join([query_instructions, system_prompt, answer_format])

    def _build_user_prompt(self, prompt: str, context: str, include_personal_views: bool) -> str:
        parts = [f"User prompt:\n{prompt.strip()}"]
        if context.strip():
            parts.append(f"Additional context:\n{context.strip()}")
        parts.append(f"Include personal views: {'yes' if include_personal_views else 'no'}")
        parts.append(
            "Return a final answer grounded in the repository. "
            "Always provide meaningful gap analysis."
        )
        return "\n\n".join(parts)

    def _parse_agent_response(self, raw_text: str) -> tuple[str, list[Gap], list[str]]:
        cleaned = _strip_code_fences(raw_text)
        candidate = cleaned
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            extracted = _extract_json_candidate(raw_text)
            if extracted is not None:
                try:
                    data = json.loads(extracted)
                except json.JSONDecodeError:
                    data = None
                else:
                    self.logger.info("response_parser=recovered_json_from_wrapped_output")
            else:
                data = None

        if data is None:
            return (
                raw_text.strip(),
                [
                    Gap(
                        type="format_error",
                        message="The model did not return valid structured output. Review the answer manually.",
                        suggested_addition="Tighten output formatting prompts or add eval coverage for JSON compliance.",
                    )
                ],
                ["Response required fallback parsing."],
            )

        answer = str(data.get("answer", "")).strip()
        notes = [str(item) for item in data.get("notes", []) if str(item).strip()]
        gaps: list[Gap] = []
        for item in data.get("gaps", []):
            if not isinstance(item, dict):
                continue
            gaps.append(
                Gap(
                    type=str(item.get("type", "unspecified_gap")),
                    message=str(item.get("message", "")).strip(),
                    suggested_addition=str(item.get("suggested_addition", "")).strip(),
                )
            )
        if not gaps:
            gaps.append(
                Gap(
                    type="missing_gap_output",
                    message="The model did not provide explicit gap analysis.",
                    suggested_addition="Add eval coverage for mandatory Gaps behavior.",
                )
            )
        return answer, gaps, notes

    def answer(
        self,
        prompt: str,
        context: str = "",
        include_personal_views: bool | None = None,
    ) -> QueryResponse:
        include_personal = (
            self.config.include_personal_by_default
            if include_personal_views is None
            else include_personal_views
        )
        query_id = uuid4().hex[:12]
        started_at = time()
        started_at_iso = datetime.now(timezone.utc).isoformat()

        prepare_provider_environment(self.config)
        ensure_required_credentials(self.config)

        session = QuerySession(self.config, self.logger)
        preloaded_index = session.preload_index() if self.config.require_index_first else ""
        system_prompt = self._build_system_prompt()
        if preloaded_index:
            system_prompt = (
                f"{system_prompt}\n\n"
                "Preloaded wiki index for initial orientation:\n"
                f"{preloaded_index}"
            )
        user_prompt = self._build_user_prompt(prompt, context, include_personal)
        self.logger.info(
            "query_id=%s event=query_started include_personal_views=%s prompt=%s",
            query_id,
            include_personal,
            prompt,
        )
        if self.config.log_model_io:
            write_query_artifact(
                self.config,
                f"{query_id}-request.json",
                {
                    "query_id": query_id,
                    "started_at": started_at_iso,
                    "prompt": prompt,
                    "context": context,
                    "include_personal_views": include_personal,
                    "system_prompt": system_prompt,
                    "user_prompt": user_prompt,
                },
            )

        agent = create_deep_agent(
            model=self.config.model,
            tools=session.tools(),
            system_prompt=system_prompt,
        )
        try:
            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user_prompt,
                        }
                    ]
                },
            )
        except Exception as exc:
            duration_ms = int((time() - started_at) * 1000)
            tb = traceback.format_exc()
            self.logger.error(
                "query_id=%s event=query_failed duration_ms=%s error=%s",
                query_id,
                duration_ms,
                exc,
            )
            write_error_artifact(
                self.config,
                f"{query_id}-error.json",
                {
                    "query_id": query_id,
                    "started_at": started_at_iso,
                    "failed_at": datetime.now(timezone.utc).isoformat(),
                    "duration_ms": duration_ms,
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                    "traceback": tb,
                    "prompt": prompt,
                    "consulted_pages_before_failure": [p.__dict__ for p in session.consulted_pages()],
                },
            )
            raise

        raw_text = _extract_text_content(result["messages"][-1].content)
        finished_at_iso = datetime.now(timezone.utc).isoformat()
        if self.config.log_model_io:
            write_query_artifact(
                self.config,
                f"{query_id}-response-raw.json",
                {
                    "query_id": query_id,
                    "started_at": started_at_iso,
                    "finished_at": finished_at_iso,
                    "raw_response": raw_text,
                },
            )
        answer, gaps, notes = self._parse_agent_response(raw_text)
        response = QueryResponse(
            answer=answer,
            consulted_pages=session.consulted_pages(),
            gaps=gaps,
            notes=notes,
        )
        duration_ms = int((time() - started_at) * 1000)
        self.logger.info(
            "query_id=%s event=query_finished duration_ms=%s consulted_pages=%s gaps=%s",
            query_id,
            duration_ms,
            len(response.consulted_pages),
            len(response.gaps),
        )
        if self.config.persist_query_history:
            write_query_artifact(
                self.config,
                f"{query_id}-response-final.json",
                {**response.to_dict(), "started_at": started_at_iso, "finished_at": finished_at_iso, "duration_ms": duration_ms},
            )
        return response
