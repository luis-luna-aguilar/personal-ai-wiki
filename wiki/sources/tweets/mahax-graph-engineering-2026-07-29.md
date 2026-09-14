---
title: Mahax on X — Graph Engineering with Claude
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-mahaximus_-2082442856417956173.md
url: https://x.com/Mahaximus_/status/2082442856417956173
published: 2026-07-29
ingested: 2026-09-09
domains: [agents, coding]
---

# Mahax on X — Graph Engineering with Claude

X Article (2.5M views, 649 likes) by Mahax (@Mahaximus_) explaining "graph engineering" as a mental model for agent workflows: nodes are bounded units of work, edges are genuine data dependencies, and a "fake-edge test" finds steps that only run in sequence because of how they were typed rather than a real dependency. Covers the fan-out/fan-in "diamond" shape, a "checker node" for screening bad parallel outputs before they reach a combining step, and a heuristic for choosing a static graph (fixed upfront, fast, auditable) over a dynamic one (built as it runs, flexible, harder to audit) that recommends starting static and reaching for dynamic only under real pressure. Illustrates the ideas with a YAML-like `workflow: / nodes: / depends_on:` syntax presented as a Claude Code parallel-workflow feature — this syntax does not match Anthropic's documented Dynamic Workflows implementation (an orchestration script Claude itself writes, not a user-declared static dependency graph; see [Claude Code](../../tools/claude-code.md)) and is treated here as the author's own teaching illustration, not verified product syntax.

## Influenced pages
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — expanded the "Hybrid graph orchestration" pattern with graph vocabulary, the fake-edge test, the diamond/checker-node pairing, and the static-vs-dynamic selection heuristic

## Key claims extracted
- A node is one bounded unit of work with a single output; an edge is a genuine data dependency, not mere sequence
- The fake-edge test: ask whether a later step actually consumes an earlier step's output; if not, run them in parallel
- The "diamond" fan-out/fan-in shape is fastest when parallel nodes are independent and the combining node needs all of them
- A "checker node" between the parallel layer and the combining node should catch empty, contradictory, off-topic, low-confidence, or malformed outputs
- Start with a static graph; switch to a dynamic graph only when the work's scope can't be known upfront, and never when the run must be fully auditable afterward
