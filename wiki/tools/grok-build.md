---
title: Grok Build
type: tool
domains: [coding]
subcategory: terminal-coding-agent
tags: [xai, agentic, cli]
as_of: 2026-06-17
sources: [grok-build-may-2026, spacex-cursor-june-2026]
---

# Grok Build

xAI's CLI coding agent. Early beta, available to SuperGrok Heavy subscribers via a curl install. Designed for "high-level professional work."

## Current status (as of 2026-06-17)

- Early beta; install via `curl` command; SuperGrok Heavy subscribers only
- **Plan mode**: review and adjust each step before diffs are applied — prevents runaway changes on large tasks
- **Parallel subagents in worktrees**: delegates massive tasks to parallel subagents, each in their own git worktree — same isolation pattern as Claude Code's `--worktree` flag
- No public benchmark data at launch
- **Jointly trained model (June 2026):** SpaceX/xAI is co-training a new model with Cursor that will power Grok Build; expected to represent a significant capability upgrade from the current xAI model backend

## Weaknesses / caveats

- Early beta, gated to SuperGrok Heavy subscription tier
- No publicly verified benchmark or real-world performance data yet

## Recent changes

- [2026-06-17] Grok Build to receive jointly trained model from SpaceX/Cursor collaboration
- [2026-05-15] Launched as early beta CLI coding agent

## Sources

- [Grok Build launch — The Code, May 2026](../sources/newsletters/grok-build-may-2026.md)
- [SpaceX acquires Cursor + Cursor Origin launch (June 2026)](../sources/newsletters/spacex-cursor-june-2026.md)
