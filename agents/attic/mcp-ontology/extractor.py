from __future__ import annotations

from dataclasses import asdict
import json
import os
import re
import urllib.error
import urllib.request

from .markdown import MarkdownSection
from .schema import ExtractedSection, coerce_extracted_section


PROMPT_VERSION = "ontology-extractor-v1"


SYSTEM_PROMPT = """You compile an open ontology from Luis's curated AI wiki.

Treat the wiki section as true knowledge. Extract structured knowledge, not claims.
Be open-ended: create new entity kinds, action kinds, workflow kinds, relationship
types, and property keys when the text supports them.

Return only JSON with this shape:
{
  "entities": [
    {
      "name": "Claude Code",
      "kind": "Tool",
      "aliases": ["Anthropic Claude Code"],
      "summary": "Terminal-first AI coding agent",
      "properties": {"capabilities": ["agent loop"], "constraints": []}
    }
  ],
  "relationships": [
    {"source": "Claude Code", "type": "USES_MODEL", "target": "Claude Opus 4.7", "properties": {}}
  ],
  "actions": [
    {"name": "run browser verification", "kind": "VerificationAction", "properties": {}, "requires": ["browser automation"], "produces": ["visual proof"]}
  ],
  "workflows": [
    {"name": "agentic infrastructure operations", "kind": "OperationalWorkflow", "properties": {}, "steps": ["read-only diagnosis", "approval-gated mutation"]}
  ]
}

Guidelines:
- Extract knowledge that would help answer future questions.
- Prefer compact properties over long prose.
- Do not create evidence spans, citations, confidence scores, or as_of fields.
- Do not classify the page; classify concepts/entities from the content.
- Use stable names. Put alternate spellings in aliases.
- Use uppercase snake case for relationship types when possible, but invent new ones when useful.
"""


class OntologyExtractor:
    def __init__(self, model: str, api_key: str | None = None, base_url: str | None = None) -> None:
        self.model = model
        self.api_key = (
            api_key
            or os.getenv("AGENTS_OPENROUTER_API_KEY")
            or os.getenv("PERSONAL_WIKI_OPENROUTER_API_KEY")
            or os.getenv("OPENROUTER_API_KEY")
        )
        self.base_url = base_url or os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1/chat/completions")

    def extract(self, section: MarkdownSection) -> ExtractedSection:
        if not self.api_key:
            raise RuntimeError(
                "Missing OpenRouter credentials for ontology extraction. "
                "Set AGENTS_OPENROUTER_API_KEY, PERSONAL_WIKI_OPENROUTER_API_KEY, or OPENROUTER_API_KEY."
            )

        payload = {
            "model": self._provider_model(),
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": (
                        f"File: {section.path}\n"
                        f"Page title: {section.title}\n"
                        f"Section heading: {section.heading}\n\n"
                        f"{section.text}"
                    ),
                },
            ],
            "temperature": 0.1,
            "response_format": {"type": "json_object"},
        }
        request = urllib.request.Request(
            self.base_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://local.agents",
                "X-Title": "Personal Wiki Ontology Compiler",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenRouter extraction failed: HTTP {exc.code}: {body[:1000]}") from exc

        data = json.loads(raw)
        content = data["choices"][0]["message"]["content"]
        parsed = _parse_json_object(content)
        return coerce_extracted_section(parsed)

    def _provider_model(self) -> str:
        return self.model.removeprefix("openrouter:")


class HeuristicExtractor:
    """Offline development extractor.

    This is intentionally simple and exists for smoke tests and local plumbing
    checks. Production ontology quality should come from OntologyExtractor.
    """

    def __init__(self) -> None:
        self.model = "heuristic"

    def extract(self, section: MarkdownSection) -> ExtractedSection:
        entities = []
        for name in sorted(set(re.findall(r"\b[A-Z][A-Za-z0-9.+/-]*(?:\s+[A-Z][A-Za-z0-9.+/-]*){0,4}", section.text))):
            if len(name) < 3 or name.lower() in {"current", "sources", "recent changes"}:
                continue
            entities.append({"name": name, "kind": "Thing", "aliases": [], "summary": "", "properties": {}})
            if len(entities) >= 20:
                break
        return coerce_extracted_section({"entities": entities, "relationships": [], "actions": [], "workflows": []})


class ManualExtractor:
    """Marker extractor for Codex/manual artifact workflows."""

    model = "codex-manual"

    def extract(self, section: MarkdownSection) -> ExtractedSection:
        raise RuntimeError(
            "Manual extraction does not run inside the CLI. Use `prepare` to create "
            "work packets, fill extraction JSON, then use `import`."
        )


def _parse_json_object(content: str) -> dict:
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", content, re.DOTALL)
        if not match:
            raise
        data = json.loads(match.group(0))
    if not isinstance(data, dict):
        raise ValueError("Extractor returned JSON that is not an object.")
    return data


def extracted_to_dict(section: ExtractedSection) -> dict:
    return asdict(section)
