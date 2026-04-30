---
title: GAIA
type: benchmark
domains: [agents, models]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# GAIA

GAIA tests fundamental multimodal reasoning, web browsing, and tool-use capability through 466 questions designed to require genuine reasoning chains rather than pattern matching. The questions are conceptually simple for humans but expose deep capability gaps in current frontier models.

## Current status (as of 2026-04-23)

- Human baseline: ~92%
- Frontier LLMs without agentic scaffolding: ~15% (as reported; verify against current leaderboard)
- 466 total questions, designed to be relatively resistant to straightforward data contamination
- Requires combining multimodal reasoning, web access, and tool use in a single task

## Why it matters

GAIA provides a hard upper-bound-style benchmark for measuring general agent capability. The large human/model gap quantifies how far current systems still are from the "smart human with internet access" baseline.

It is useful for selecting foundation models, tracking long-term capability changes, and separating genuine reasoning-plus-tool-use ability from benchmark gaming.

## Caveats

- Low baseline scores mean GAIA is mainly a discriminator at the top end; it does not sharply differentiate most current models
- Scores can vary significantly depending on how much scaffolding, tool access, and retry budget is provided

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
