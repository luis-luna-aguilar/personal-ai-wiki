from __future__ import annotations

import os
from typing import Any

from ..ontology.compiler import build_store_from_env


def ontology_search(query: str, limit: int = 10) -> list[dict[str, Any]]:
    store = build_store_from_env()
    try:
        return store.search(query, limit=limit)
    finally:
        store.close()


def ontology_expand(entity: str, depth: int = 2, limit: int = 30) -> list[dict[str, Any]]:
    store = build_store_from_env()
    try:
        return store.expand(entity, depth=depth, limit=limit)
    finally:
        store.close()


def ontology_actions(goal: str, limit: int = 10) -> list[dict[str, Any]]:
    store = build_store_from_env()
    try:
        return store.actions(goal, limit=limit)
    finally:
        store.close()


def ontology_configured() -> bool:
    return bool(os.getenv("AGENTS_NEO4J_PASSWORD") or os.getenv("PERSONAL_WIKI_NEO4J_PASSWORD"))
