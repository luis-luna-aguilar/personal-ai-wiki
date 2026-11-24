---
title: AINews — Jev as a judge, CLM, and the classifier critique
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
url: https://www.latent.space/p/ainews-the-future-of-latent-space
published: 2026-09-25
ingested: 2026-10-20
domains: [models]
---

# AINews — Jev as a judge, CLM, and the classifier critique

The decision-model story from the 2026-09-25 AINews issue. It covers TypeSafe's fundraise, a paper testing Jev as an LLM judge, ecosystem adoption, and two Reddit threads: one arguing Jev is standard zero-shot classification, one comparing it with CLM.

## Influenced pages
- [Jev](../../models/jev.md) — judge results, Banking77 baseline
- [Decision models](../../concepts/decision-models.md) — skeptic view
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — escalation cascade result

## Key claims extracted
- TypeSafe reportedly raising $1B+ at a $10B+ valuation, a week after a $200M round
- Jev-as-a-Judge paper: $0.044 per 1K judgments, 152 ms median, ~277x cheaper than GPT-6; within 3 points on RewardBench and HaluEval, 14.5 points behind on JudgeBench; escalating low-confidence calls to GPT-6 Astra keeps 99% accuracy at 57% of the cost
- turbopuffer native reranking includes Jev; Jev is the top OpenRouter model at 1K–10K context
- Reddit critique: BGE-small plus logistic regression scored 93.3% on Banking77 vs Jev's 83.2%; the fair baselines are zero-shot classifiers, cross-encoders and rerankers
