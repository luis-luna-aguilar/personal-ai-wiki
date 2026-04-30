---
title: WebArena
type: benchmark
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# WebArena

WebArena is a stateful web navigation benchmark that challenges agents to complete goal-directed tasks across realistic web environments including e-commerce sites, content management systems, forums, and development platforms. Unlike static QA benchmarks, WebArena maintains state across interactions: an agent's actions in one step affect what it sees in the next.

## Current status (as of 2026-04-23)

- Human baseline: ~78% task success
- Best reported systems: ~57% (as reported; verify against current leaderboard)
- Tests agents against real web noise: popups, dynamic content, navigation menus, and multi-page flows
- Tasks require combining web navigation, information retrieval, and form submission across multiple sites

## Why it matters

WebArena is the primary benchmark for evaluating agents that must operate in open web environments: browser automation, web research agents, and e-commerce assistants. The 20+ point gap between best models and humans reveals how much current agents still struggle with real web environments as opposed to clean API-structured tasks.

Unlike OSWorld, WebArena focuses on web-native tasks rather than full desktop control, making it more directly relevant for web-facing product agents.

## Caveats

- Specific scores are from a research synthesis report (April 2026); verify against the WebArena leaderboard
- Web environments change over time; the benchmark requires maintenance to stay aligned with current site layouts
- Performance varies significantly based on how much scaffolding (tool suite, memory) is given to the agent

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
