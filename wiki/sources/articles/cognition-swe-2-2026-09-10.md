---
title: 'Cognition — Introducing SWE-2: Pushing the Pareto Frontier'
type: source
source_type: article
source_file: raw/articles/2026-11-23-cognitioncom-blog-swe-2.md
url: https://cognition.com/blog/swe-2
published: 2026-09-10
ingested: 2026-11-24
domains: [coding, models]
---

# Cognition — Introducing SWE-2: Pushing the Pareto Frontier

Cognition's launch post for SWE-2, its in-house coding model for Devin, post-trained from Kimi K3 with RL scaled to multiple trillions of parameters. It covers the benchmark table, the behaviour changes against SWE-1.7, and a training method that fits a per-effort-level cost penalty into one RL run. AINews (2026-09-12) relayed the launch and added Devin Voice, built on GPT-Live and SWE-2 (`raw/newsletters/2026-09-12-ainews-deepseek-v41-flash-763b-p8b-d16b-novel.md`).

## Influenced pages
- [Devin](../../tools/devin.md) — SWE-2 replaces the SWE-1.7 bullet
- [FrontierCode](../../benchmarks/frontiercode.md) — new FrontierCode 1.1 section
- [State of Coding](../../state-of/coding.md) — refreshed Devin leader line

## Key claims extracted
- SWE-2 is post-trained from Kimi K3 (2.8T parameters); Cognition's first RL at multi-trillion-parameter scale, building on the SWE-1.7 recipe.
- Reward R = S − λ_e·C, with a linear cost penalty per effort level, λ_e fitted to the slope of the base model's cost–performance frontier; all effort levels train in one run. Length-weighted reward baselines, NVFP4/FP8 kernels with quantization-aware training, an online draft model, 3x more RL environments.
- FrontierCode 1.1 Main: SWE-2 50.0%, GPT-6 Astra 53.3%, Fable 5.1 50.9%, Grok 4.6 48.0%, GPT-5.6 Sol 47.5%, Kimi K3 44.2%, SWE-1.7 42.0%. SWE-2 is within a point of Fable 5.1 at 64% lower cost.
- DeepSWE 1.1 73.0%; Terminal-Bench 2.1 92.8%; Terminal-Bench 4.0 27.3% (Fable 5.1 55.8%, GPT-6 Astra 57.9%).
- SWE-2 medium scores above SWE-1.7 with 58% fewer turns and 81% lower cost (mean steps 53 vs 127). The gains come mostly from more focused exploration.
- Available from launch in Devin Desktop and CLI, rolling out to Devin Web and Fusion.
