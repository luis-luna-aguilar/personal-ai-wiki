"""Agents MCP package."""

__all__ = ["PersonalWikiAgent"]


def __getattr__(name: str):
    if name == "PersonalWikiAgent":
        from .engine import PersonalWikiAgent

        return PersonalWikiAgent
    raise AttributeError(name)
