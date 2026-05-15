from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from uuid import uuid4
import os

from .artifacts import load_extraction_artifact, write_work_packet
from .extractor import HeuristicExtractor, ManualExtractor, OntologyExtractor, PROMPT_VERSION, extracted_to_dict
from .graph import Neo4jOntologyStore
from .manifest import OntologyManifest
from .markdown import eligible_wiki_files, parse_markdown_document
from .schema import ExtractedSection


@dataclass
class OntologyPaths:
    repo_root: Path
    wiki_root: Path
    manifest_path: Path
    work_dir: Path


@dataclass
class OntologyStatus:
    clean: list[str]
    dirty: dict[str, str]
    deleted: list[str]
    failed: list[str]


class OntologyCompiler:
    def __init__(
        self,
        paths: OntologyPaths,
        model: str,
        extractor_mode: str = "llm",
        store: Neo4jOntologyStore | None = None,
    ) -> None:
        self.paths = paths
        self.model = model
        self.extractor_mode = extractor_mode
        self.manifest = OntologyManifest(paths.manifest_path)
        self._store = store
        if extractor_mode == "heuristic":
            self.extractor = HeuristicExtractor()
        elif extractor_mode == "manual":
            self.extractor = ManualExtractor()
        else:
            self.extractor = OntologyExtractor(model)

    @property
    def store(self) -> Neo4jOntologyStore:
        if self._store is None:
            self._store = build_store_from_env()
        return self._store

    def close(self) -> None:
        if self._store is not None:
            self._store.close()

    def status(self) -> OntologyStatus:
        documents = {
            path.relative_to(self.paths.repo_root).as_posix(): parse_markdown_document(path, self.paths.repo_root)
            for path in eligible_wiki_files(self.paths.wiki_root)
        }
        dirty: dict[str, str] = {}
        clean: list[str] = []
        failed: list[str] = []
        for rel_path, document in documents.items():
            reason = self.manifest.dirty_reason(
                rel_path,
                document.content_hash,
                PROMPT_VERSION,
                self.extractor.model,
            )
            if reason:
                dirty[rel_path] = reason
            else:
                clean.append(rel_path)
            record = self.manifest.records.get(rel_path)
            if record and record.status == "failed":
                failed.append(rel_path)

        deleted = [
            path for path in self.manifest.records
            if path not in documents and self.manifest.records[path].status != "deleted"
        ]
        return OntologyStatus(clean=clean, dirty=dirty, deleted=deleted, failed=failed)

    def rebuild(self) -> dict[str, int]:
        if self.extractor_mode == "manual":
            raise RuntimeError("Manual mode cannot rebuild directly. Use prepare, fill packets, then import.")
        self.store.verify()
        self.store.setup()
        self.store.clear_namespace()
        self.manifest.records = {}
        return self.sync(process_all=True)

    def sync(self, process_all: bool = False) -> dict[str, int]:
        if self.extractor_mode == "manual":
            raise RuntimeError("Manual mode cannot sync directly. Use prepare, fill packets, then import.")
        self.store.verify()
        self.store.setup()
        status = self.status()
        eligible_paths = eligible_wiki_files(self.paths.wiki_root)
        documents = {
            path.relative_to(self.paths.repo_root).as_posix(): parse_markdown_document(path, self.paths.repo_root)
            for path in eligible_paths
        }
        to_process = set(documents) if process_all else set(status.dirty)

        processed = 0
        failed = 0
        deleted = 0
        for rel_path in sorted(to_process):
            document = documents[rel_path]
            batch_id = uuid4().hex
            self.store.delete_file_output(rel_path)
            try:
                extracted_sections: list[ExtractedSection] = [
                    self.extractor.extract(section)
                    for section in document.sections
                    if section.text.strip()
                ]
                self.store.write_file_extraction(
                    path=rel_path,
                    title=document.title,
                    content_hash=document.content_hash,
                    batch_id=batch_id,
                    extracted_sections=extracted_sections,
                )
            except Exception as exc:
                failed += 1
                self.manifest.mark_failed(
                    rel_path,
                    document.content_hash,
                    PROMPT_VERSION,
                    self.extractor.model,
                    batch_id,
                    str(exc),
                )
            else:
                processed += 1
                self.manifest.mark_clean(
                    rel_path,
                    document.content_hash,
                    PROMPT_VERSION,
                    self.extractor.model,
                    batch_id,
                )

        for rel_path in status.deleted:
            self.store.delete_file_output(rel_path)
            self.manifest.mark_deleted(rel_path)
            deleted += 1

        self.manifest.save()
        return {"processed": processed, "failed": failed, "deleted": deleted}

    def prepare(self, limit: int | None = None, process_all: bool = False) -> dict[str, object]:
        status = self.status()
        eligible_paths = eligible_wiki_files(self.paths.wiki_root)
        documents = {
            path.relative_to(self.paths.repo_root).as_posix(): parse_markdown_document(path, self.paths.repo_root)
            for path in eligible_paths
        }
        to_prepare = sorted(documents) if process_all else sorted(status.dirty)
        if limit is not None:
            to_prepare = to_prepare[:limit]

        written: list[str] = []
        for rel_path in to_prepare:
            artifact_path = write_work_packet(
                self.paths.work_dir,
                documents[rel_path],
                self.extractor.model,
            )
            written.append(artifact_path.relative_to(self.paths.repo_root).as_posix())

        return {
            "prepared": len(written),
            "work_packets": written,
            "deleted_waiting_cleanup": status.deleted,
        }

    def import_artifact(self, artifact_path: Path) -> dict[str, object]:
        self.store.verify()
        self.store.setup()
        data, extracted_sections = load_extraction_artifact(artifact_path)
        rel_path = str(data["path"])
        content_hash = str(data["content_hash"])
        prompt_version = str(data.get("extractor_prompt_version") or PROMPT_VERSION)
        extractor_model = str(data.get("extractor_model") or self.extractor.model)
        title = str(data.get("title") or rel_path)
        batch_id = uuid4().hex

        current_path = (self.paths.repo_root / rel_path).resolve()
        if not current_path.exists():
            self.store.delete_file_output(rel_path)
            self.manifest.mark_deleted(rel_path)
            self.manifest.save()
            return {"path": rel_path, "status": "deleted"}

        current_document = parse_markdown_document(current_path, self.paths.repo_root)
        if current_document.content_hash != content_hash:
            self.manifest.mark_failed(
                rel_path,
                current_document.content_hash,
                prompt_version,
                extractor_model,
                batch_id,
                "Extraction artifact is stale: file content hash changed after packet creation.",
            )
            self.manifest.save()
            return {"path": rel_path, "status": "stale_artifact"}

        self.store.delete_file_output(rel_path)
        self.store.write_file_extraction(
            path=rel_path,
            title=title,
            content_hash=content_hash,
            batch_id=batch_id,
            extracted_sections=extracted_sections,
        )
        self.manifest.mark_clean(rel_path, content_hash, prompt_version, extractor_model, batch_id)
        self.manifest.save()
        return {"path": rel_path, "status": "imported", "sections": len(extracted_sections)}

    def import_artifacts(self, path: Path) -> dict[str, object]:
        paths = sorted(path.glob("*.json")) if path.is_dir() else [path]
        results = [self.import_artifact(item) for item in paths]
        return {
            "imported": sum(1 for item in results if item.get("status") == "imported"),
            "stale": sum(1 for item in results if item.get("status") == "stale_artifact"),
            "deleted": sum(1 for item in results if item.get("status") == "deleted"),
            "results": results,
        }

    def inspect_file(self, rel_path: str) -> dict:
        path = (self.paths.repo_root / rel_path).resolve()
        document = parse_markdown_document(path, self.paths.repo_root)
        return {
            "path": document.path,
            "title": document.title,
            "content_hash": document.content_hash,
            "sections": [
                {
                    "heading": section.heading,
                    "start_line": section.start_line,
                    "end_line": section.end_line,
                    "extracted": extracted_to_dict(self.extractor.extract(section)),
                }
                for section in document.sections
                if section.text.strip()
            ],
        }

    def query(self, text: str, limit: int = 10) -> list[dict]:
        return self.store.search(text, limit=limit)

    def expand(self, name: str, depth: int = 2, limit: int = 30) -> list[dict]:
        return self.store.expand(name, depth=depth, limit=limit)

    def actions(self, goal: str, limit: int = 10) -> list[dict]:
        return self.store.actions(goal, limit=limit)


def default_paths(base_dir: Path | None = None) -> OntologyPaths:
    base = (base_dir or Path(__file__).resolve().parents[3]).resolve()
    return OntologyPaths(
        repo_root=base,
        wiki_root=base / "wiki",
        manifest_path=base / "agents" / "ontology" / "manifest.json",
        work_dir=base / "agents" / "ontology" / "work",
    )


def build_store_from_env() -> Neo4jOntologyStore:
    uri = os.getenv("AGENTS_NEO4J_URI") or os.getenv("PERSONAL_WIKI_NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("AGENTS_NEO4J_USER") or os.getenv("PERSONAL_WIKI_NEO4J_USER", "neo4j")
    password = os.getenv("AGENTS_NEO4J_PASSWORD") or os.getenv("PERSONAL_WIKI_NEO4J_PASSWORD")
    database = os.getenv("AGENTS_NEO4J_DATABASE") or os.getenv("PERSONAL_WIKI_NEO4J_DATABASE", "neo4j")
    if not password:
        raise RuntimeError("Missing Neo4j password. Set AGENTS_NEO4J_PASSWORD or PERSONAL_WIKI_NEO4J_PASSWORD.")
    return Neo4jOntologyStore(uri=uri, user=user, password=password, database=database)
