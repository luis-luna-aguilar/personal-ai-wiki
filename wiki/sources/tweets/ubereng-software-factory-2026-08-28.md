---
title: "Running a Software Factory Efficiently at Uber Scale"
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-ubereng-2093444169037762840.md
url: https://x.com/UberEng/status/2093444169037762840
published: 2026-08-28
ingested: 2026-09-09
domains: [agents, coding]
---

# Running a Software Factory Efficiently at Uber Scale

Uber Engineering's first-party account (posted by @udaykiran) of how it runs and cost-optimizes its internal AI coding-agent fleet: adoption numbers, a six-term cost equation, benchmark-driven Pareto-optimal model selection (uReview, the internal Uber SWE Benchmark), token-efficiency defaults (auto-compaction, reasoning effort, prompt-cache TTL), MCP-schema-bloat fixes (CLI tool resolution, tool search, Code-mode), the AI Context Graph for context grounding, and a spend-visibility/anti-pattern-dashboard stack.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — benchmark-driven model selection, FinOps controls (caching TTL, compaction, reasoning-effort default, spend visibility)
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — AI Context Graph and Code-mode patterns
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — Software Factory adoption numbers and strategic framing

## Key claims extracted

- 70%+ of Uber PRs attributed to agents; 3,600+ agent skills; 30,000+ skill executions/day
- Feb-Aug 2026: weekly active agentic users +7x, weekly agentic requests +9.4x; total spend stabilized since April
- With model held constant, cost/1,000 requests down ~34% from peak, cost/session down ~52% from June peak
- Benchmark-driven model selection (4-step process); uReview graded on precision/recall/F1 + cost against real PRs with known bugs; internal Uber SWE Benchmark
- Subagent-defaults-to-cheaper-model is called the single most impactful, still-growing cost lever
- Auto-compaction at 400K tokens (even on 1M-context models); reasoning effort defaulted to Medium
- Prompt-cache TTL: 1-hour for interactive sessions (was 5-minute, causing rebuilds on idle gaps), 5-minute for subagents
- MCP schema bloat: 100+ tools added 50-70K tokens of schema overhead; fixed via CLI tool resolution and tool search
- Code-mode: batches tool calls into one subprocess script; >50% token reduction on minimal responses, >90% on bulk workflows; 25+ pre-built code-mode skills deployed
- AI Context Graph: 24M nodes / 80M edges / 86 node types / 117 edge types across 30+ internal systems; 38-second grounded answer vs. 20+ minutes/2 subagents/3 errors ungrounded
- Session Analysis Dashboard flags 16 named cost anti-patterns with dollar impact, zero setup required
