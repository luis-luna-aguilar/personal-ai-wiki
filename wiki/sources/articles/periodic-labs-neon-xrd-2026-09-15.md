---
title: Periodic Labs — Nature Is Our Learning Environment (Neon)
type: source
source_type: article
source_file: raw/articles/2026-11-24-periodiccom-news-nature-is-our-learning-environment.md
url: https://periodic.com/news/nature-is-our-learning-environment
published: 2026-09-15
ingested: 2026-11-24
domains: [science]
---

# Periodic Labs — Nature Is Our Learning Environment (Neon)

Periodic Labs' research post introducing Periodic Neon, published with the company announcement "Building Labs that Learn" (https://periodic.com/news/building-labs-that-learn). Periodic runs high-throughput materials labs in Menlo Park and trains AI on their output. Neon post-trains Kimi K2.6, a 1T-parameter open-weight model, with scientific midtraining and RL on Periodic's own powder X-ray diffraction (XRD) data, to identify which crystal phases a synthesis produced. Neon is deployed in Periodic's labs. The publication date is taken from Liam Fedus's launch thread (15 September 2026); the posts show none.

## Influenced pages
- [AI in Science](../../trends/ai-in-science.md) — Periodic Labs paragraph under Self-driving labs
- [State of Science](../../state-of/science.md) — Periodic Labs leader line under Self-driving labs
- [Harness vs model](../../concepts/harness-vs-model.md) — same-model 3.8× harness comparison

## Key claims extracted
- FrontierXRD (134 hard multiphase lab samples, about five phases each): Neon 55.3% success vs 2.7% for base Kimi K2.6; above GPT-6 Astra and Claude Fable 5.1 at lower cost per analysis
- Neon also outperforms frontier models on 198 XRD measurements from chemical systems held out of midtraining and RL
- Final training run: 1,300 H200 GPUs (vs Astra's reported 100,000+ Blackwell GPUs); performance rises with RL compute and inference compute
- Reward: an ensemble of two agentic LLM judges built from an expert rubric; judge-expert agreement 74.6% vs expert-expert 77.2%, 84% vs expert consensus
- Scientific midtraining (literature, code, experimental data; corpus doubling monthly) raised later RL rewards and FrontierXRD success
- Same model (Claude Opus 5, high effort): Periodic's scientific harness 3.8× higher XRD success than Claude Code with open databases and BGMN, at similar cost
- Cost basis: API list prices with perfect caching for external models; $2.5/hour H200 throughput for Neon
- Next: training Periodic's AI to direct campaigns, develop synthesis procedures and choose experiments
