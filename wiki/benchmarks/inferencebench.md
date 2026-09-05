---
title: InferenceBench
type: benchmark
domains: [agents, coding]
tags: [agentic]
as_of: 2026-05-21
sources: [inferencebench-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21]
---

# InferenceBench

InferenceBench evaluates whether AI agents can perform open-ended LLM inference-serving optimization — not by retrieving a known recipe, but by genuinely exploring the solution space. Given a target model, one H100 GPU, an optimization scenario (prefill latency, decode latency, concurrent-request throughput, or a balanced mix), and a two-hour wall-clock budget, an agent must deploy an OpenAI-compatible inference server and optimize the speed of LLM inference.

## Current status (as of 2026-05-21)

- Across 15 frontier agent configurations, agents reliably beat a naive PyTorch baseline (up to 8.08x) and often match or exceed default-settings serving engines (4.05x for vLLM)
- But agents still fall below a simple hyperparameter search under the same time budget (up to 11.53x) — the benchmark's key negative result
- Agents overwhelmingly converge on a single inference framework rather than exploring alternatives
- Agent trajectories show agents enumerate many relevant optimization techniques but test only a few distinct configurations, spending remaining budget re-measuring, repairing, or tuning hyperparameters rather than exploring substantially different strategies

## Why it matters

InferenceBench targets AI R&D automation directly: can an agent optimize its own serving infrastructure, not just write application code? The gap versus a bare hyperparameter sweep suggests the bottleneck isn't domain knowledge (agents know the right techniques) but breadth of exploration and systematic evaluation — a distinct failure mode from the coding-benchmark gaps tracked elsewhere in this wiki (e.g. [FrontierCode](frontiercode.md)).

## Caveats

- Small, early benchmark: one paper, 15 agent configurations; only the arXiv abstract has been read, so per-model results and any leaderboard are not captured here
- AINews' secondary coverage (2026-05-21) additionally claimed an "inverse scaling" finding — smaller models like Claude Sonnet 4.6 and GLM-5 ranking better by preserving robust final states. This does **not** appear in the fetched arXiv abstract; we did not pull the full paper body, so this specific claim is flagged unverified rather than stated as confirmed on this page.

## Sources

- [InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents (arXiv)](../sources/papers/inferencebench-paper-2026-05.md)
- [AINews — agent-benchmark cluster](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
