---
title: MiniMax M3
type: model
domains: [models, coding]
subcategory: coding-model
tags: [minimax, agentic]
as_of: 2026-10-20
sources: [ainews-cosmos-nemotron-june-2026, ainews-june-05-2026, ainews-deepseek-v4-1-flash-1017-2026-10-20]
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

## M3.1 Flash (as of 2026-10-20)

MiniMax's cheaper, faster sibling, revealed as the stealth model "Space Bunny" that topped usage leaderboards:

- **Pricing:** $0.15 / $0.60 per 1M input/output tokens, cache reads $0.015; MiniMax claims 1/3 the cost and 3x the speed of M3. Weights due 23 October 2026; free for a limited time on OpenRouter, OpenCode, Cline and Ollama Cloud.
- **MiniMax's figures:** DeepSWE 74%, Automation-Bench 62%, BabyVision 91%.
- **Artificial Analysis:** Intelligence Index 42 (level with GLM-5.3-Flash, behind [DeepSeek V4.1 Flash](deepseek-v4-1-flash.md)'s 45) at about $0.22 per task; HLE 48%, AA-Omniscience accuracy 56%, but a **93% hallucination rate** because it attempts nearly every question.
- **Arenas:** #12 open in Code Arena WebDev (1588, +106 over M3); #26 on Design Arena frontend.

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

- [2026-10-20] M3.1 Flash launched (formerly stealth "Space Bunny"): $0.15/$0.60, AA Intelligence Index 42 with a 93% hallucination rate; weights due 23 October.
- [2026-06-02] Launched; initial benchmarks; weights not disclosed at launch despite open-weight claim

## Sources

- [AINews — NVIDIA Cosmos 3, Nemotron 3 Ultra, MiniMax M3 (June 2)](../sources/newsletters/ainews-cosmos-nemotron-june-2026.md)
- [AINews — June 5 (PostTrainBench placement)](../sources/newsletters/ainews-june-05-2026.md)
- [AINews — DeepSeek V4.1 Flash 1017, MiniMax M3.1 Flash, Mercury 3 (20 October 2026)](../sources/newsletters/ainews-deepseek-v4-1-flash-1017-2026-10-20.md)
