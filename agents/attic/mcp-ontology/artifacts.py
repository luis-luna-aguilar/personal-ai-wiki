from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
import json
import re

from .extractor import PROMPT_VERSION
from .markdown import MarkdownDocument
from .schema import ExtractedSection, coerce_extracted_section


ARTIFACT_SCHEMA_VERSION = 1


def safe_artifact_name(path: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "__", path).strip("_") + ".json"


def build_work_packet(document: MarkdownDocument, extractor_model: str) -> dict:
    return {
        "schema_version": ARTIFACT_SCHEMA_VERSION,
        "path": document.path,
        "title": document.title,
        "content_hash": document.content_hash,
        "extractor_prompt_version": PROMPT_VERSION,
        "extractor_model": extractor_model,
        "instructions": (
            "Read each section and fill extracted.entities, extracted.relationships, "
            "extracted.actions, and extracted.workflows. Treat wiki content as true. "
            "Use open-ended kinds/properties/relationship types. Do not add citations, "
            "confidence, evidence spans, or as_of data."
        ),
        "sections": [
            {
                "heading": section.heading,
                "start_line": section.start_line,
                "end_line": section.end_line,
                "text": section.text,
                "extracted": {
                    "entities": [],
                    "relationships": [],
                    "actions": [],
                    "workflows": [],
                },
            }
            for section in document.sections
            if section.text.strip()
        ],
    }


def write_work_packet(work_dir: Path, document: MarkdownDocument, extractor_model: str) -> Path:
    work_dir.mkdir(parents=True, exist_ok=True)
    target = work_dir / safe_artifact_name(document.path)
    target.write_text(
        json.dumps(build_work_packet(document, extractor_model), indent=2) + "\n",
        encoding="utf-8",
    )
    return target


def load_extraction_artifact(path: Path) -> tuple[dict, list[ExtractedSection]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != ARTIFACT_SCHEMA_VERSION:
        raise ValueError(f"Unsupported extraction artifact schema_version in {path}")
    sections = [
        coerce_extracted_section(section.get("extracted", {}))
        for section in data.get("sections", [])
        if isinstance(section, dict)
    ]
    return data, sections


def artifact_preview(section: ExtractedSection) -> dict:
    return asdict(section)
