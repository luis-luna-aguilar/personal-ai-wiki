---
title: 'AINews — Claude Haiku 5.5: better than GPT-6 Luna at the same pricing'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-ainews-claude-haiku-55-better-than-gpt-6-luna.md
url: https://www.latent.space/p/ainews-claude-haiku-55-better-than
published: 2026-10-08
ingested: 2026-10-20
domains: [models]
---

# AINews — Claude Haiku 5.5: better than GPT-6 Luna at the same pricing

The 2026-10-08 issue (covering 6–7 October) leads with the Claude Haiku 5.5 launch: pricing matched to GPT-6 Luna, same-day Sonnet 5.5 cache-read cut and subscriber API credits, partner rollouts, and a detailed Artificial Analysis evaluation with token-use caveats.

## Influenced pages
- [Claude Haiku 5.5](../../models/claude-haiku-5-5.md) — launch date, independent evals, token use
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — cache-read cut dated to the Haiku launch
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — per-task cost caveat
- [State of Models](../../state-of/models.md) — Haiku line

## Key claims extracted
- Haiku 5.5 shipped 6–7 October at $0.10/$0.50 per 1M tokens under 100k-token prompts, matching GPT-6 Luna; Sonnet 5.5 cache reads halved the same day
- AA Intelligence Index 43 at max effort; GLM-5.3 Flash 42, Gemini 3.8 Flash 41, GPT-6 Luna 38; Sonnet 5.5 56
- ~162k output tokens per AA index task at max effort, ~3x Luna; xhigh→max adds 2 points for ~1.8x tokens
- Terminal-Bench 4.0 33% (AA) vs Anthropic's 39.2%
- AA-Omniscience: 36% accuracy, 40% hallucination (Luna 44% / 77%)
- AutomationBench-AA 35%, depressed by a pre-release over-refusal bug; AA will re-run
- 1M-token context, up from 200k
