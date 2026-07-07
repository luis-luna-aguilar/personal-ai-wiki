---
title: Getting started with loops
type: source
source_type: article
source_file: raw/articles/2026-07-06-claudecom-blog-getting-started-with-loops.md
url: https://claude.com/blog/getting-started-with-loops
published: 2026-06-30
ingested: 2026-07-06
domains: [coding, agents]
---

# Getting started with loops

Anthropic's Claude Code team defines agentic loops as agents repeating cycles of work until a stop condition is met, then classifies Claude Code loops into turn-based, goal-based, time-based, and proactive patterns.

## Influenced pages

- [Claude Code](../../tools/claude-code.md) - official loop taxonomy and token-management guidance
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) - loop taxonomy, stop criteria, and cost-aware loop primitives
- [State of Coding](../../state-of/coding.md) - recent-change note for Claude Code's loop taxonomy

## Key claims extracted

- Turn-based loops are normal prompt-driven agentic loops where the human keeps directing each turn.
- Goal-based loops use `/goal` and work best when success criteria are deterministic and bounded by turn caps.
- Time-based loops use `/loop` locally or `/schedule` in routines for recurring checks and external-system monitoring.
- Proactive loops compose `/schedule`, `/goal`, skills, dynamic workflows, and auto mode for recurring well-defined work.
- Loops should start simple, use explicit success/stop criteria, pilot before large runs, route routine work to cheaper models where possible, and use scripts for deterministic steps.
