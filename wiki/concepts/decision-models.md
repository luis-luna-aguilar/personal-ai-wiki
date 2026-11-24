---
title: Decision models
type: concept
domains: [models, agents]
subcategory: decision-model
tags: []
as_of: 2026-10-17
sources: [latent-space-jev-diogo-almeida-2026-09-21, every-how-to-get-most-out-of-jev-2026-09-23, jackyk02-clm-contrastive-language-model-2026-09-23, ainews-jev-judge-clm-critique-2026-09-25, latent-space-openai-decisions-api-2026-09-30, cloudflare-clef-decision-models-2026-10-02, ainews-decisions-api-beta-vals-jev-2026-10-07, ainews-decision-models-product-category-2026-10-10, ainews-aa-decision-index-2026-10-14, ainews-liquid-d1-ultra-pplx-decider-2026-10-17]
---

# Decision models

Models that answer a typed question about a given input in one pass, without generating text: the probability that a statement is true, a pick from a fixed set of options, or a position on a scale. Because nothing is decoded token by token, many questions run in parallel within milliseconds and output is usually free. Code then branches, routes, sorts or thresholds on the result.

## Also called

System One models (TypeSafe's term), Constrained Decoding Models (ScaleDown), Decisions API (OpenAI); critics call them zero-shot classifiers.

## Current status (as of 2026-10-17)

- **Category formed in a month.** [Jev](../models/jev.md) launched on 2026-09-15; about 100 API clones followed within two weeks. By mid-October the field included Cloudflare's open-weight Clef and Clef-flash (2 October), OpenAI's Decisions API on GPT-6 Luna (public beta, $0.10/M input, no output charge), Perplexity's open pplx-decider (v1.1 27B, then v1.2 in 27B and 4B), Microsoft-Decision-1, Liquid d1 and vLLM Semantic Router's Decision 2.0. Unsloth published a notebook that turns Qwen3.5-4B into one on 8GB of VRAM.
- **Common build.** A frozen LLM backbone reads the input once (prefill only) and a small trained head scores each valid option. Cloudflare's Clef uses Qwen3.8-27B with a Brier-loss calibration step. CLM swaps the head for a contrastive pair of state and action encoders, so a fixed action set can be cached.
- **Benchmarks.** There are three competing indices: Cloudflare's "Jev Decision Index", Hugging Face's Decision Index v0.3 and Artificial Analysis's Decision Index (14 October). On AA's index, Liquid d1-ultra leads at 65 against Jev 1.14's 57. Claude Haiku 5.5 at low effort scores 61, but costs $184 against Jev's $42 per million tasks and takes 1.4 s against 0.13 s per task.
- **Where they fit.** Routing, approval gates, judging traces, tool selection, reranking, and real-time interfaces where an LLM's one-to-two-second turn breaks the feel. AA finds them competitive on classification and routing, but weaker and often overconfident on knowledge and reasoning. CLM's authors say Jev fails as a verifier on long-horizon coding tasks.
- **Skeptic view.** Critics call it standard zero-shot classification with better marketing. A small embedding model plus logistic regression beat Jev on Banking77 (93.3% vs 83.2%). The fair baseline is classifiers and rerankers, not LLMs emitting JSON.

## How to use one

Every's rule: if a person could make the call in under 10 seconds, send it to a decision model; slower calls go to an LLM. Break a fuzzy question ("is this urgent?") into separate yes/no checks ("did a person write it?", "is someone waiting on me?", "does ignoring it cost me?"), weight them in code, and test them on a sample you have already judged before running the full set. Almeida gives the same advice for production systems: ask many small independent questions rather than one compound instruction.

## Related

- [Jev](../models/jev.md) — the reference model the category formed around
- [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) — where decision models fit in a routing cascade
- [MedDecider-27B](../models/meddecider-27b.md) — a medical decision model tuned for clinical choices
- [ScaleDown](../models/scaledown.md) — classify/extract models with a Jev-compatible Decisions API, marketed as "Constrained Decoding Models"

## Recent changes

- [2026-10-17] Page created: the category from Jev's launch (2026-09-15) to Artificial Analysis's Decision Index and Liquid d1-ultra taking its top spot.

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
