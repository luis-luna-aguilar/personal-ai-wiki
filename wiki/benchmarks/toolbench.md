---
title: ToolBench
type: benchmark
domains: [agents]
tags: [agentic]
as_of: 2026-04-23
sources: [agents-evals-deep-research]
---

# ToolBench

ToolBench is a large-scale benchmark for evaluating agents on real-world tool use and API chaining. It covers over 16,000 real RESTful APIs sourced from the RapidAPI hub and tests agents on single-step, multi-step, and multi-tool planning scenarios.

## Current status (as of 2026-04-23)

- 16,000+ real RESTful APIs from RapidAPI
- Three task types: single-tool single-step, single-tool multi-step, and multi-tool multi-step
- Uses a DFSDT evaluation algorithm; agents must navigate a decision tree of possible API calls to find the correct sequence
- Useful as a reference benchmark for enterprise API competence

## Why it matters

ToolBench is directly relevant for evaluating agents that must interact with enterprise software stacks through API calls, the core capability behind most business process automation, integration agents, and internal workflow agents. The 16,000-API scale covers a breadth of real-world API diversity that synthetic benchmarks cannot replicate.

## Caveats

- APIs evolve over time; benchmark coverage may lag behind current API landscapes
- The DFSDT evaluation methodology makes direct comparison with non-DFSDT-based agents less clean

## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
