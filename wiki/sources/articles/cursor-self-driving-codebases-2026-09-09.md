---
title: "Towards self-driving codebases"
type: source
source_type: article
source_file: raw/articles/2026-09-09-cursorcom-blog-self-driving-codebases.md
url: https://cursor.com/blog/self-driving-codebases
ingested: 2026-09-09
domains: [agents, coding]
---

# Towards self-driving codebases

Cursor's account of the harness behind its long-running browser-building research: how the multi-agent design evolved from a flat, lock-based self-coordinating swarm through a planner/executor/judge split to a recursive planner/subplanner/worker topology, plus the freshness mechanisms, prompting lessons, and throughput tradeoffs learned along the way. No publish date is shown on the live page. The post is Cursor's own follow-up to "Scaling long-running autonomous coding" and is called "an earlier post about the swarm" by the already-ingested 2026-09-07 "Agent swarms and the new model economics" post — meaning it predates that post, likely by several months (it references Opus 4.5 and GPT-5.1/5.2 as current models, both superseded generations by the wiki's other pages' timelines). Dated by ingest-date fallback per the wiki's source-date rule.

## Influenced pages

- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — recursive planner/subplanner/worker topology, freshness mechanisms, prompting lessons, steady-error-rate design principles, and an extension to the swarm-coordination-failures pattern (new-VCS throughput jump, Coase framing)
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — extended the evaluator-separation pattern with a community Codex config example
- [Cursor](../../tools/cursor.md) — Recent-changes note on the harness research and its partial availability to users

## Key claims extracted

- Recursive planner/subplanner/worker topology: root planner never codes, spawns subplanners for subdividable scope, disposable workers report back a single handoff
- Removed a central integrator role once workers proved capable of resolving their own merge conflicts
- Freshness mechanisms: rewritten (not appended) scratchpad, self-summarization at context limits, self-reflection prompts, encouraged pivoting
- Prompting lessons: negative constraints beat positive reminders; concrete quantity ranges beat vague scope language
- Accepted a small, stable error rate rather than requiring 100% per-commit correctness, with a final "green branch" reconciliation pass
- Named design principles: anti-fragile, empirical-over-assumption-driven, design-for-throughput-explicitly
- Peaked at ~1,000 commits/hour across 10M tool calls over one continuous week with no human intervention
