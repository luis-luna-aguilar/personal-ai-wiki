from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExtractedEntity:
    name: str
    kind: str = "Thing"
    aliases: list[str] = field(default_factory=list)
    properties: dict[str, Any] = field(default_factory=dict)
    summary: str = ""


@dataclass
class ExtractedRelationship:
    source: str
    rel_type: str
    target: str
    properties: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExtractedAction:
    name: str
    kind: str = "Action"
    properties: dict[str, Any] = field(default_factory=dict)
    requires: list[str] = field(default_factory=list)
    produces: list[str] = field(default_factory=list)


@dataclass
class ExtractedWorkflow:
    name: str
    kind: str = "Workflow"
    properties: dict[str, Any] = field(default_factory=dict)
    steps: list[str] = field(default_factory=list)


@dataclass
class ExtractedSection:
    entities: list[ExtractedEntity] = field(default_factory=list)
    relationships: list[ExtractedRelationship] = field(default_factory=list)
    actions: list[ExtractedAction] = field(default_factory=list)
    workflows: list[ExtractedWorkflow] = field(default_factory=list)


def coerce_extracted_section(data: dict[str, Any]) -> ExtractedSection:
    return ExtractedSection(
        entities=[
            ExtractedEntity(
                name=str(item.get("name", "")).strip(),
                kind=str(item.get("kind") or item.get("type") or "Thing").strip() or "Thing",
                aliases=[str(alias).strip() for alias in item.get("aliases", []) if str(alias).strip()],
                properties=dict(item.get("properties", {})) if isinstance(item.get("properties", {}), dict) else {},
                summary=str(item.get("summary", "")).strip(),
            )
            for item in data.get("entities", [])
            if isinstance(item, dict) and str(item.get("name", "")).strip()
        ],
        relationships=[
            ExtractedRelationship(
                source=str(item.get("source", "")).strip(),
                rel_type=str(item.get("type") or item.get("rel_type") or item.get("relationship", "RELATED_TO")).strip()
                or "RELATED_TO",
                target=str(item.get("target", "")).strip(),
                properties=dict(item.get("properties", {})) if isinstance(item.get("properties", {}), dict) else {},
            )
            for item in data.get("relationships", [])
            if isinstance(item, dict)
            and str(item.get("source", "")).strip()
            and str(item.get("target", "")).strip()
        ],
        actions=[
            ExtractedAction(
                name=str(item.get("name", "")).strip(),
                kind=str(item.get("kind") or item.get("type") or "Action").strip() or "Action",
                properties=dict(item.get("properties", {})) if isinstance(item.get("properties", {}), dict) else {},
                requires=[str(value).strip() for value in item.get("requires", []) if str(value).strip()],
                produces=[str(value).strip() for value in item.get("produces", []) if str(value).strip()],
            )
            for item in data.get("actions", [])
            if isinstance(item, dict) and str(item.get("name", "")).strip()
        ],
        workflows=[
            ExtractedWorkflow(
                name=str(item.get("name", "")).strip(),
                kind=str(item.get("kind") or item.get("type") or "Workflow").strip() or "Workflow",
                properties=dict(item.get("properties", {})) if isinstance(item.get("properties", {}), dict) else {},
                steps=[str(value).strip() for value in item.get("steps", []) if str(value).strip()],
            )
            for item in data.get("workflows", [])
            if isinstance(item, dict) and str(item.get("name", "")).strip()
        ],
    )
