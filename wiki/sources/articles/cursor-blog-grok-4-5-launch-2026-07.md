---
title: Introducing Grok 4.5 (Cursor blog)
type: source
source_type: article
source_file: raw/articles/2026-08-25-cursorcom-blog-grok-4-5.md
url: https://cursor.com/blog/grok-4-5
published: 2026-07-08
ingested: 2026-08-25
domains: [coding, models]
---

# Introducing Grok 4.5 (Cursor blog)

Cursor's official announcement of Grok 4.5, trained jointly with SpaceXAI (xAI post-Cursor-acquisition). Positions it as Cursor's most powerful model yet and its first trained for more than software engineering — a deliberately broad data mix spanning STEM tasks, research papers, and general knowledge work, in addition to trillions of tokens of Cursor codebase and developer-agent interaction data. Available immediately across Cursor's desktop, web, iOS, CLI, and SDK surfaces, with double usage for the first week. Composer 2.5 remains available as a separate, smaller-weight-class model.

## Influenced pages
- [Grok 4.5](../../history/models/grok-4-5.md) — new model page (later superseded by [Grok 4.6](../../models/grok-4-6.md))
- [Cursor](../../tools/cursor.md) — updated SpaceX-acquisition section to reflect the model's launch
- [Grok Build](../../tools/grok-build.md) — updated to reflect Grok 4.5's launch and availability
- [State of Models](../../state-of/models.md) — replaced the Grok 4.20 entry with Grok 4.5

## Key claims extracted
- Grok 4.5 is a mixture-of-experts model, trained jointly by Cursor and SpaceXAI
- Training data: trillions of tokens of Cursor codebase + developer-agent interaction data, plus broad STEM/knowledge-work data (deliberately not coding-only, unlike Composer 2.5)
- Reinforcement learning on realistic, difficult environments spanning software engineering and broader knowledge work, built by a distributed agent system that constructs/tests/refines environments at scale
- Pricing: $2/M input, $6/M output (base); $4/M input, $18/M output (fast variant)
- Available today in Cursor desktop, web, iOS, CLI, and SDK; double usage for the first week
- Composer 2.5 remains available as a separate, smaller weight class; Cursor will keep releasing models in that size tier
- Per Cursor's own footnote: Grok 4.5 has an advantage on CursorBench because an earlier Cursor codebase snapshot was accidentally included in training; that data has been removed for future models
- Michael Truell (Cursor CEO, via X, cross-referenced from `raw/tweets/2026-08-25-mntruell-2074916251743457787.md`): "Opus-class model that's fast and low cost... a significant step up over any model we've developed so far, including Composer 2.5, and has become the daily driver for many on our team. First of many releases."
