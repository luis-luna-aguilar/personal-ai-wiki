from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mcp.ontology.graph import canonical_id
from mcp.ontology.artifacts import build_work_packet, load_extraction_artifact
from mcp.ontology.manifest import OntologyManifest
from mcp.ontology.markdown import eligible_wiki_files, parse_markdown_document
from mcp.ontology.schema import coerce_extracted_section


class OntologyMarkdownTests(unittest.TestCase):
    def test_eligible_files_excludes_history(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            wiki = root / "wiki"
            (wiki / "concepts").mkdir(parents=True)
            (wiki / "history" / "concepts").mkdir(parents=True)
            current = wiki / "concepts" / "mcp.md"
            history = wiki / "history" / "concepts" / "old.md"
            current.write_text("# MCP\n\nCurrent.", encoding="utf-8")
            history.write_text("# Old\n\nArchived.", encoding="utf-8")

            files = [path.relative_to(wiki).as_posix() for path in eligible_wiki_files(wiki)]

            self.assertEqual(files, ["concepts/mcp.md"])

    def test_parse_document_sections_and_title(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            path = root / "wiki" / "concepts" / "mcp.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                "---\ntitle: MCP\ntype: concept\n---\n\n# MCP\n\nIntro.\n\n## Tools\n\nTool use.",
                encoding="utf-8",
            )

            document = parse_markdown_document(path, root)

            self.assertEqual(document.title, "MCP")
            self.assertEqual(document.path, "wiki/concepts/mcp.md")
            self.assertEqual([section.heading for section in document.sections], ["MCP", "Tools"])


class OntologyManifestTests(unittest.TestCase):
    def test_dirty_reasons(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            manifest = OntologyManifest(Path(temp_dir) / "manifest.json")

            self.assertEqual(
                manifest.dirty_reason("wiki/a.md", "hash1", "prompt1", "model1"),
                "unprocessed",
            )
            manifest.mark_clean("wiki/a.md", "hash1", "prompt1", "model1", "batch1")
            self.assertIsNone(manifest.dirty_reason("wiki/a.md", "hash1", "prompt1", "model1"))
            self.assertEqual(
                manifest.dirty_reason("wiki/a.md", "hash2", "prompt1", "model1"),
                "content_changed",
            )
            self.assertEqual(
                manifest.dirty_reason("wiki/a.md", "hash1", "prompt2", "model1"),
                "prompt_version_changed",
            )


class OntologySchemaTests(unittest.TestCase):
    def test_coerce_open_extraction(self) -> None:
        extracted = coerce_extracted_section(
            {
                "entities": [{"name": "MCP", "kind": "Protocol", "properties": {"open": True}}],
                "relationships": [{"source": "MCP", "type": "ENABLES", "target": "Tool use"}],
                "actions": [{"name": "use MCP tool", "kind": "ToolAction", "requires": ["MCP server"]}],
                "workflows": [{"name": "agent tool routing", "steps": ["select tool"]}],
            }
        )

        self.assertEqual(extracted.entities[0].kind, "Protocol")
        self.assertEqual(extracted.relationships[0].rel_type, "ENABLES")
        self.assertEqual(extracted.actions[0].requires, ["MCP server"])
        self.assertEqual(extracted.workflows[0].steps, ["select tool"])

    def test_canonical_id_merges_kind_variants(self) -> None:
        self.assertEqual(canonical_id("Claude Code", "Tool"), canonical_id("Claude Code", "Thing"))

    def test_manual_work_packet_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            path = root / "wiki" / "concepts" / "mcp.md"
            path.parent.mkdir(parents=True)
            path.write_text("# MCP\n\nMCP connects agents to tools.", encoding="utf-8")
            document = parse_markdown_document(path, root)
            packet = build_work_packet(document, "codex-manual")
            packet["sections"][0]["extracted"]["entities"].append(
                {"name": "MCP", "kind": "Protocol", "properties": {}}
            )
            packet["sections"][0]["extracted"]["relationships"].append(
                {"source": "MCP", "type": "CONNECTS_TO", "target": "Tools"}
            )
            artifact = root / "artifact.json"
            artifact.write_text(__import__("json").dumps(packet), encoding="utf-8")

            data, sections = load_extraction_artifact(artifact)

            self.assertEqual(data["extractor_model"], "codex-manual")
            self.assertEqual(sections[0].entities[0].name, "MCP")
            self.assertEqual(sections[0].relationships[0].rel_type, "CONNECTS_TO")


if __name__ == "__main__":
    unittest.main()
