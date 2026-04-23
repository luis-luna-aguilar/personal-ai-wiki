from __future__ import annotations

import json
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any

from .config import PersonalWikiConfig


def configure_logging(config: PersonalWikiConfig) -> logging.Logger:
    logger = logging.getLogger("personal_wiki_agent")
    if logger.handlers:
        return logger

    config.paths.runtime_logs_dir.mkdir(parents=True, exist_ok=True)
    handler = RotatingFileHandler(
        config.paths.runtime_log_file,
        maxBytes=2_000_000,
        backupCount=5,
        encoding="utf-8",
    )
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging, config.log_level.upper(), logging.INFO))
    logger.propagate = False
    return logger


def write_query_artifact(config: PersonalWikiConfig, filename: str, payload: dict[str, Any]) -> Path:
    config.paths.query_history_dir.mkdir(parents=True, exist_ok=True)
    path = config.paths.query_history_dir / filename
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return path


def write_error_artifact(config: PersonalWikiConfig, filename: str, payload: dict[str, Any]) -> Path:
    config.paths.query_history_dir.mkdir(parents=True, exist_ok=True)
    path = config.paths.query_history_dir / filename
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return path

