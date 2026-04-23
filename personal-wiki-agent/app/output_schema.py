from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class ConsultedPage:
    path: str
    title: str
    as_of: str
    why_used: str


@dataclass
class Gap:
    type: str
    message: str
    suggested_addition: str = ""


@dataclass
class QueryResponse:
    answer: str
    consulted_pages: list[ConsultedPage] = field(default_factory=list)
    gaps: list[Gap] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "answer": self.answer,
            "consulted_pages": [asdict(page) for page in self.consulted_pages],
            "gaps": [asdict(gap) for gap in self.gaps],
            "notes": self.notes,
        }

