---
title: MiniMax M3
type: model
domains: [models, coding]
subcategory: coding-model
tags: [agentic]
as_of: 2026-06-02
sources: [ainews-cosmos-nemotron-june-2026, ainews-june-05-2026]
---

# MiniMax M3

MiniMax's claimed "open-weight frontier model" with 1M context and strong agent benchmarks. Significant caveat: weights and parameter count were not publicly disclosed at launch, making the "open-weight" label contested. Supersedes MiniMax M2.7 in the coding model tier if the open-weight claim is ultimately fulfilled.

## Current status (as of 2026-06-02)

- 1M context (512K guaranteed)
- Native multimodality
- **Benchmarks:** 59.0% SWE-Bench Pro, 66.0% Terminal Bench 2.1, 74.2% MCP Atlas
- **PostTrainBench:** #3 overall (behind Claude Opus 4.7 and GPT-5.5)
- Day-0 support: Novita, Vercel AI Gateway, Cloudflare Workers AI, and others
- **Contested claim:** At launch, neither model weights nor parameter count were publicly disclosed. This is the "open-weight without weights" launch pattern — arguably not open-weight at time of writing.

## Strengths

- Strong agent benchmark placement (PostTrainBench #3) at a claimed open-weight price tier
- 1M context with 512K guaranteed is among the largest for open-accessible models
- MCP Atlas score (74.2%) suggests strong tool-use and protocol adherence

## Weaknesses / caveats

- "Open-weight" claim is contested — weights not disclosed at launch
- High token consumption noted by practitioners
- Verbose self-check loops observed in long tasks
- Requirement drift on very long tasks — model loses track of original constraints

## Recent changes

- [2026-06-02] Launched; initial benchmarks; weights not disclosed at launch despite open-weight claim

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra, MiniMax M3 (June 2)](../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
- [AINews — June 5 (PostTrainBench placement)](../sources/newsletters/ainews-june-05-2026.md)
