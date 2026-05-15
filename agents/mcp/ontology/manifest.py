from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
import json


@dataclass
class ManifestRecord:
    path: str
    content_hash: str
    last_processed_at: str
    extractor_prompt_version: str
    extractor_model: str
    graph_batch_id: str
    status: str
    error: str = ""


class OntologyManifest:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.records: dict[str, ManifestRecord] = {}
        self.load()

    def load(self) -> None:
        if not self.path.exists():
            self.records = {}
            return
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self.records = {
            item["path"]: ManifestRecord(**item)
            for item in data.get("files", [])
        }

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": 1,
            "updated_at": utc_now(),
            "files": [asdict(record) for record in sorted(self.records.values(), key=lambda item: item.path)],
        }
        self.path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    def dirty_reason(
        self,
        path: str,
        current_hash: str,
        prompt_version: str,
        model: str,
    ) -> str | None:
        record = self.records.get(path)
        if record is None:
            return "unprocessed"
        if record.status == "failed":
            return "previous_failed"
        if record.content_hash != current_hash:
            return "content_changed"
        if record.extractor_prompt_version != prompt_version:
            return "prompt_version_changed"
        if record.extractor_model != model:
            return "model_changed"
        if record.status == "deleted":
            return "previous_deleted"
        return None

    def mark_clean(
        self,
        path: str,
        current_hash: str,
        prompt_version: str,
        model: str,
        batch_id: str,
    ) -> None:
        self.records[path] = ManifestRecord(
            path=path,
            content_hash=current_hash,
            last_processed_at=utc_now(),
            extractor_prompt_version=prompt_version,
            extractor_model=model,
            graph_batch_id=batch_id,
            status="clean",
        )

    def mark_failed(
        self,
        path: str,
        current_hash: str,
        prompt_version: str,
        model: str,
        batch_id: str,
        error: str,
    ) -> None:
        self.records[path] = ManifestRecord(
            path=path,
            content_hash=current_hash,
            last_processed_at=utc_now(),
            extractor_prompt_version=prompt_version,
            extractor_model=model,
            graph_batch_id=batch_id,
            status="failed",
            error=error[:1000],
        )

    def mark_deleted(self, path: str) -> None:
        record = self.records.get(path)
        if record is None:
            return
        record.status = "deleted"
        record.last_processed_at = utc_now()


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
