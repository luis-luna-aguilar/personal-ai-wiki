---
title: Qwen 3.8 27B
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [alibaba, open-weights]
as_of: 2026-08-20
sources: [ainews-memory-prices-openai-pause-2026-08-19, ainews-death-of-params-glm-53-2026-08-20]
---

# Qwen 3.8 27B

Alibaba's smaller sibling to [Qwen 3.8](qwen-3-8.md) (the Max variant), and the reference point for how far local/open models had caught up with frontier models by August 2026. Community-reported usage implies its weights shipped in the days following Qwen3.8-Max's 2026-08-13 open-weight release, though no primary Alibaba announcement of the 27B's own release is captured here.

## Current status (as of 2026-08-20)

- #1 local model in Cline within 4 days of availability
- Scores near DeepSeek V4-Pro / GPT-5.6 Luna Max territory on the Artificial Analysis Intelligence Index — described as the first local model to reach that tier
- #7 on AA's Agentic Index; #1 on Harvey's legal benchmark among open-weight models
- A community "refusal-removed" MLX build runs on Apple Silicon with near-zero refusals at 262K context

## Why it matters

Repeated, corroborated signal across three consecutive AINews issues (not a single hot take) that a 27B locally-runnable model is now credibly frontier-adjacent — directly relevant to [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md).

## Weaknesses / caveats

- This is aggregated secondary commentary (Twitter/Reddit relayed through a newsletter), not a primary Alibaba or Artificial Analysis report — treat the AA Intelligence Index placement and "first local model at that tier" framing as community-repeated claims, not verified benchmark citations
- The implied ship date (days after 2026-08-13) is inferred from usage reports, not a primary release announcement
- Some practitioners argue the benchmark parity overstates real-world coding quality versus Opus 4.5
- A Reddit thread reported a regression on offline factual recall (obscure trivia, historical/location identification) versus Qwen3.6-27B when web search/fetch tools were disabled — read as an intentional parameter-budget tradeoff toward coding/agentic strength, not a broad quality drop

## Recent changes

- [2026-08-20] Page created: Qwen3.8-27B becomes the reference point for local/open-model catch-up — #1 local model in Cline, AA Intelligence Index parity claims with DeepSeek V4-Pro/GPT-5.6 Luna Max, refusal-removed MLX build — offset by a reported factual-recall regression vs. Qwen3.6-27B.

## Sources

- [AINews — Memory prices up 500% in 12 months](../sources/newsletters/ainews-memory-prices-openai-pause-2026-08-19.md)
- [AINews — Death of Params: Z.ai CEO Jie Tang on GLM 5.3](../sources/newsletters/ainews-death-of-params-glm-53-2026-08-20.md)
