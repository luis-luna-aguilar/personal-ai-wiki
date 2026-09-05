---
title: Grok Build
type: tool
domains: [coding]
subcategory: terminal-coding-agent
tags: [xai, agentic, cli]
as_of: 2026-07-08
sources: [grok-build-may-2026, spacex-cursor-june-2026, ainews-spacexai-grok-45-2026-07-09]
---

# Grok Build

xAI's CLI coding agent. Early beta, available to SuperGrok Heavy subscribers via a curl install. Designed for "high-level professional work."

## Current status (as of 2026-07-08)

- Early beta; install via `curl` command; SuperGrok Heavy subscribers only
- **Plan mode**: review and adjust each step before diffs are applied — prevents runaway changes on large tasks
- **Parallel subagents in worktrees**: delegates massive tasks to parallel subagents, each in their own git worktree — same isolation pattern as Claude Code's `--worktree` flag
- **Grok 4.5 (July 2026):** the jointly trained SpaceXAI/Cursor model launched and is available in Grok Build; Coding Agent Index 76 in Grok Build, on par with GPT-5.5 in Codex and below Fable 5 in Claude Code (per Artificial Analysis, via AINews). See [Grok 4.5](../models/grok-4-5.md).

## Weaknesses / caveats

- Early beta, gated to SuperGrok Heavy subscription tier
- Beyond Artificial Analysis' Coding Agent Index (so far only seen via AINews' recap), still limited independent/third-party benchmarking of Grok 4.5 inside Grok Build specifically

## Recent changes

- [2026-07-08] Grok 4.5 launched and is available in Grok Build; Coding Agent Index 76 per Artificial Analysis (via AINews), on par with GPT-5.5 in Codex, below Fable 5 in Claude Code.
- [2026-06-17] Grok Build to receive jointly trained model from SpaceX/Cursor collaboration
- [2026-05-15] Launched as early beta CLI coding agent

## Sources

- [Grok Build launch — The Code, May 2026](../sources/newsletters/grok-build-may-2026.md)
- [SpaceX acquires Cursor + Cursor Origin launch (June 2026)](../sources/newsletters/spacex-cursor-june-2026.md)
- [AINews — SpaceXAI launches Grok 4.5](../sources/newsletters/ainews-spacexai-grok-45-2026-07-09.md)
