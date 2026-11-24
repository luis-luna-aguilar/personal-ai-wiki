---
title: AINews — Managed Agents flows, agent-team economics, Devin trees
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
published: 2026-10-10
ingested: 2026-10-20
domains: [agents]
---

# AINews — Managed Agents flows, agent-team economics, Devin trees

The "Multi-Agent Orchestration and Coding Tools" section of the 10 October 2026 AINews issue: Claude Managed Agents dynamic workflows enter public beta, Vals AI measures whether agent teams pay off, Prime Intellect's agent swarm rewrites Prime Agent in Rust, and Devins can spawn trees of managed Devins.

## Influenced pages

- [Claude Managed Agents](../../tools/claude-managed-agents.md) — public beta, 1,000-agent limit, beta header, cost warning
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — agent-team measurements
- [Devin](../../tools/devin.md) — Devin trees
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — Vals team-cost bullet

## Key claims extracted

- Claude Managed Agents dynamic workflows (public beta): lead agent writes a phased plan, fans out to up to 1,000 agents per run, merges results; enabled with `multiagent_20261001`
- Anthropic advises starting with scoped tasks because token use can be high
- Vals AI, Vibe Code Bench, GPT-6 Sol and Opus 5.5 alone vs. as teams: teams cost 1.8–5.1x more; only Sol at medium effort improved significantly (+7.3 points)
- Sol delegated in parallel along architectural lines; Opus ran sequential waves, about 6.8 subagents and ~1,140 subagent tool calls per app at max effort, no significant gain
- Prime Intellect: 2,000+ agents, 10K+ sandboxes, 200B+ GLM-5.3 tokens over two weeks rewrote Prime Agent in Rust; ~13x faster to usable input, 83% less startup memory
- Devins can spawn trees of managed Devins, so wall time tracks the slowest branch rather than the sum
