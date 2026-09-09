---
title: "Agent swarms and the new model economics"
type: source
source_type: article
source_file: raw/articles/2026-09-07-cursorcom-blog-agent-swarm-model-economics.md
url: https://cursor.com/blog/agent-swarm-model-economics
ingested: 2026-09-08
domains: [agents, coding]
---

# Agent swarms and the new model economics

Cursor's engineering blog details its second-generation agent swarm (planner/worker tree topology) building SQLite from scratch in Rust, documenting five multi-agent coordination failure modes and fixes, a self-authored "Field Guide" context mechanism, stacked "review lenses," and cost data across four model-mix configurations.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — coordination failure-modes pattern, Field Guide, review lenses
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — $1,339 vs. $10,565 same-task cost comparison

## Key claims extracted

- New swarm harness beat the old one in every model mix: 73-85% of held-out test suite in 4 hours vs. 11-77%
- >98% fewer merge conflicts (under 1,000 vs. over 70,000); 3-7x smaller final code for equal/better quality
- 5 named failure modes with fixes: split-brain design, planner contention, merge conflicts, megafiles, ossification
- Field Guide: self-authored, agent-owned shared context folder, line-budget constrained
- Review lenses: stacking multiple imperfect/decorrelated reviewers beats one "best" reviewer
- Cost: $1,339 (Opus 4.8 planner + Composer 2.5 workers) vs. $10,565 (GPT-5.5 solo) for the same task
