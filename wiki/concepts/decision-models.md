---
title: Decision models
type: concept
domains: [models, agents]
subcategory: decision-model
tags: []
as_of: 2026-11-20
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, jackyk02-clm-contrastive-language-model-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, latent-space-openai-decisions-api-2026-09-30, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17, hume-audio-decision-model-api-2026-11-08, trycua-cua-repo-2026-11, ainews-cua-s1-forms-2026-09-19, vals-claimbench-2026-11-20, cmpnd-dspy-wsp-2026-11-13]
---

# Decision models

Models that answer a typed question about a given input in one pass, without generating text: the probability that a statement is true, a pick from a fixed set of options, or a position on a scale. Because nothing is decoded token by token, many questions run in parallel within milliseconds and output is usually free. Code then branches, routes, sorts or thresholds on the result.

## Also called

System One models (TypeSafe's term; Cua says "System 1"), Constrained Decoding Models (ScaleDown), Decisions API (OpenAI); critics call them zero-shot classifiers.

## Current status (as of 2026-11-20)

- **Category formed in a month.** [Jev](../models/jev.md) launched on 2026-09-15; about 100 API clones followed within two weeks. By mid-October the field included Cloudflare's open-weight Clef and Clef-flash (2 October), OpenAI's Decisions API on GPT-6 Luna (public beta, $0.10/M input, no output charge), Perplexity's open pplx-decider (v1.1 27B, then v1.2 in 27B and 4B), Microsoft-Decision-1, Liquid d1 and vLLM Semantic Router's Decision 2.0. Unsloth published a notebook that turns Qwen3.5-4B into one on 8GB of VRAM. In November Hume AI added the first audio-native one, the [Hume Audio Decision Model](../models/hume-audio-decision-model.md), which judges how speech sounds rather than what a transcript says. Cua's open CUA-S1-FORMS (September) is the first built for computer use: it scores which value belongs in which form field, and which elements to leave alone, from structured UI elements, while application code orders the actions.
- **Common build.** A frozen LLM backbone reads the input once (prefill only) and a small trained head scores each valid option. Cloudflare's Clef uses Qwen3.8-27B with a Brier-loss calibration step. CLM swaps the head for a contrastive pair of state and action encoders, so a fixed action set can be cached.
- **Benchmarks.** There are three competing indices: Cloudflare's "Jev Decision Index", Hugging Face's Decision Index v0.3 and Artificial Analysis's Decision Index (14 October). On AA's index, Liquid d1-ultra leads at 65 against Jev 1.14's 57. Claude Haiku 5.5 at low effort scores 61, but costs $184 against Jev's $42 per million tasks and takes 1.4 s against 0.13 s per task. Vals AI's ClaimBench (1,960 claims checked against 10-K excerpts: supported, contradicted, or not addressed) tests the cascade use directly: a decision model answers when its confidence clears a threshold tuned for at most 1% errors and sends the rest to an LLM. Perplexity's Decider V1.3 in front of Haiku 5.5 reached 99.85% accuracy for $0.10 per 1,000 claims, against $1.19 for Haiku's own label call, and answered almost every claim itself; d1-ultra leads the standalone board at 100%. Subtle one-word contradictions separate the field (Decider V1.3 99.0%, the weakest models near 50%).
- **Where they fit.** Routing, approval gates, judging traces, tool selection, reranking, and real-time interfaces where an LLM's one-to-two-second turn breaks the feel. AA finds them competitive on classification and routing, but weaker and often overconfident on knowledge and reasoning. CLM's authors say Jev fails as a verifier on long-horizon coding tasks.
- **Tuning after release.** Cmpnd's experimental `dspy-wsp` optimizer has GPT-6 Astra edit an open decision model's weights directly ([weight-space programming](weight-space-programming.md)) over 25 test runs for about $5–10. On five models from 0.6B to 9B (including d1 and Clef-Flash models) it added 1.9–16.1 accuracy points on 400 held-out cases, and 6.5–20.0 with Cmpnd's ReAnchor threshold refit; the edited model runs locally.
- **Skeptic view.** Critics call it standard zero-shot classification with better marketing. A small embedding model plus logistic regression beat Jev on Banking77 (93.3% vs 83.2%). The fair baseline is classifiers and rerankers, not LLMs emitting JSON.

## How to use one

Every's rule: if a person could make the call in under 10 seconds, send it to a decision model; slower calls go to an LLM. Break a fuzzy question ("is this urgent?") into separate yes/no checks ("did a person write it?", "is someone waiting on me?", "does ignoring it cost me?"), weight them in code, and test them on a sample you have already judged before running the full set. Almeida gives the same advice for production systems: ask many small independent questions rather than one compound instruction.

## Related

- [Jev](../models/jev.md) — the reference model the category formed around
- [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) — where decision models fit in a routing cascade
- [MedDecider-27B](../models/meddecider-27b.md) — a medical decision model tuned for clinical choices
- [ScaleDown](../models/scaledown.md) — classify/extract models with a Jev-compatible Decisions API, marketed as "Constrained Decoding Models"
- [Hume Audio Decision Model](../models/hume-audio-decision-model.md) — the first audio-native decision model, for judging tone, pacing and background sound
- [Cua](../tools/cua.md) — computer-use infrastructure whose CUA-S1-FORMS scores form-filling decisions
- [Weight-space programming](weight-space-programming.md) — tuning an open decision model by editing its weights directly

## Recent changes

- [2026-11-20] Added Vals AI's ClaimBench: a Decider V1.3 → Haiku 5.5 cascade checks 10-K claims at 99.85% accuracy for $0.10 per 1,000, against $1.19 for Haiku alone.
- [2026-11-13] Cmpnd's `dspy-wsp` added: direct weight edits improved all five open decision models it tested by 1.9–16.1 points for about $5–10 each.
- [2026-11-08] Hume AI's Audio Decision Model added to the rival list as the first audio-native decision model.
- [2026-10-17] Page created: the category from Jev's launch (2026-09-15) to Artificial Analysis's Decision Index and Liquid d1-ultra taking its top spot.
- [2026-09-19] Cua's CUA-S1-FORMS added as the first computer-use decision model.

## Sources

- [Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)](../sources/newsletters/latent-space-jev-diogo-almeida-2026-09-21.md)
- [Every — How to Get the Most Out of Jev](../sources/newsletters/every-how-to-get-most-out-of-jev-2026-09-23.md)
- [Jacky Kwok — Introducing Contrastive Language Model (CLM)](../sources/tweets/jackyk02-clm-contrastive-language-model-2026-09-23.md)
- [AINews — Jev as a judge, CLM, and the classifier critique](../sources/newsletters/ainews-jev-judge-clm-critique-2026-09-25.md)
- [Latent Space — How OpenAI shipped its Decisions API](../sources/newsletters/latent-space-openai-decisions-api-2026-09-30.md)
- [Cloudflare — Introducing Clef decision models](../sources/articles/cloudflare-clef-decision-models-2026-10-02.md)
- [AINews — Decisions API beta, pplx-decider, and Vals on Jev](../sources/newsletters/ainews-decisions-api-beta-vals-jev-2026-10-07.md)
- [AINews — Decision models become a product category](../sources/newsletters/ainews-decision-models-product-category-2026-10-10.md)
- [AINews — Artificial Analysis launches a Decision Index](../sources/newsletters/ainews-aa-decision-index-2026-10-14.md)
- [AINews — Liquid d1-ultra tops the Decision Index; pplx-decider v1.2](../sources/newsletters/ainews-liquid-d1-ultra-pplx-decider-2026-10-17.md)
- [Hume AI — Audio Decisions API launch page](../sources/articles/hume-audio-decision-model-api-2026-11-08.md)
- [trycua/cua GitHub README](../sources/repos/trycua-cua-repo-2026-11.md)
- [AINews — Cua open-sources CUA-S1-FORMS](../sources/newsletters/ainews-cua-s1-forms-2026-09-19.md)
- [Vals AI — ClaimBench leaderboard and methodology](../sources/articles/vals-claimbench-2026-11-20.md)
- [Cmpnd — Weight-Space Programming with DSPy](../sources/articles/cmpnd-dspy-wsp-2026-11-13.md)
