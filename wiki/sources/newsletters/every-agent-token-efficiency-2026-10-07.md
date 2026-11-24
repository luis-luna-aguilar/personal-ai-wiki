---
title: "Building a More Efficient Agent — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-07-building-a-more-efficient-agent.md
url: https://every.to/context-window/building-a-more-efficient-agent
published: 2026-10-07
ingested: 2026-10-20
domains: [agents]
---

# Building a More Efficient Agent — Every

Every's Context Window edition on cutting the Every Agent's token cost, plus Every Podcast highlights on why the company traded personal agents for one company agent. A Sonnet-coordinator router raised cost; an Opus 5.5 upgrade, leaner tools, and a cache-key fix cut cost on 11 frequent tasks by over 80%. Includes a four-step cost-audit workflow with prompts.

## Influenced pages

- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — coordinator-router failure, cache-key bug, four-step audit
- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — reasons personal agents died off; work/home agent split
- [Claude Managed Agents](../../tools/claude-managed-agents.md) — supporting source for the production bullet

## Key claims extracted

- Routing all tasks through a Sonnet coordinator that escalated to Opus lowered quality and speed and raised cost (requests often ran on both)
- Tool-output trimming and deferred tool loading cut cost about 10%
- Per-user Slack IDs in memory-folder names made system prompts unique and broke caching; the fix cut cost 74% in a best-case test
- Overall: >80% token-cost reduction across 11 frequent tasks; tokens passed to customers at zero markup
- Willie Williams: personal bots in Slack mostly died off because they were hard to maintain and nobody remembered which did what; expects a company agent at work and a personal agent at home
