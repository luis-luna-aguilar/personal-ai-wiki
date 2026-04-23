from __future__ import annotations

import os

from .config import PersonalWikiConfig


def prepare_provider_environment(config: PersonalWikiConfig) -> None:
    """Map product-specific env vars to provider-standard names."""
    if config.provider == "openrouter":
        personal_key = os.getenv("PERSONAL_WIKI_OPENROUTER_API_KEY")
        if personal_key and not os.getenv("OPENROUTER_API_KEY"):
            os.environ["OPENROUTER_API_KEY"] = personal_key


def ensure_required_credentials(config: PersonalWikiConfig) -> None:
    if config.provider == "openrouter" and not os.getenv("OPENROUTER_API_KEY"):
        raise RuntimeError(
            "Missing OpenRouter credentials. Set PERSONAL_WIKI_OPENROUTER_API_KEY "
            "or OPENROUTER_API_KEY before running the Personal Wiki Agent."
        )

