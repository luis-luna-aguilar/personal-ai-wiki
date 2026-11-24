---
title: Building with Claude Sonnet 5.5
type: source
source_type: article
source_file: raw/articles/2026-09-29-claudedev-blogbuilding-with-claude-sonne.md
url: https://claude.dev/blog/building-with-claude-sonnet-5-5/
published: 2026-09-28
ingested: 2026-10-20
domains: [models, coding]
---

# Building with Claude Sonnet 5.5

Anthropic's launch-day developer guide for Sonnet 5.5: when to choose it over Opus 5.5, pricing, model details, a migration path from Sonnet 5 with five breaking changes and one response-shape change, tuning advice, refusal handling and availability.

## Influenced pages
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — launch date, "Building with it" section, model details

## Key claims extracted
- Thinking on by default; `thinking: disabled` returns 400; `between_tools` replaces it, only at low/medium/high effort
- Forced `tool_choice` (`any`/`tool`) returns 400; computer use only via `computer_toolset_20260801` (Bedrock still accepts the old tool)
- Sonnet 5.5 executors reject Opus 4.8, Opus 4.7 and Sonnet 5 as advisors; advice comes back encrypted
- Default effort high on the API, medium in Claude Code; effort levels recalibrated
- 1M context; 128k max output, 300k on Batches with a beta header; knowledge cutoff June 2026
- Minimum cacheable prompt 512 tokens; cache reads $0.20 at launch; high-res images ~2.5x the tokens of Sonnet 4.6
- `/claude-api migrate` applies the changes; Claude Code's `sonnet` alias moves to Sonnet 5.5 from v2.1.284
