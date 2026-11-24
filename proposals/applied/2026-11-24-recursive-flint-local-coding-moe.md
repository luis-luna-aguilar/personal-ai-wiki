---
type: proposal
source: raw/articles/2026-11-24-huggingfaceco-recursivesi-flint.md
sources:
  - raw/articles/2026-11-24-huggingfaceco-recursivesi-flint.md
  - raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
  - raw/newsletters/2026-09-14-why-you-should-work-on-ai-for-ai-research-richar.md
status: pending
created: 2026-11-24
---

# Proposal: Recursive Flint, a local coding MoE partly designed by an automated research loop

## Summary

### In short
An automated research loop has now helped build a shipped model: Recursive says its "Eureka Machine" chose Flint's sparse architecture, low-bit training and kernels, and Flint is a 40B-parameter, 2.5B-active open coding model that runs on a 24GB laptop at 114–150 tokens a second. Recursive reports 89.7% on SWE-bench Pro v2 and 54.9% on Terminal-Bench 2.1, under Apache 2.0. The proposal creates a Flint model page, adds it to State of Models, and adds Recursive's AI-for-AI-research results to the Agent improvement loop page. The reason to hesitate is length: that concept page lands right at 110% of its ceiling, the edge of the warning band.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Recursive is Richard Socher's company; he founded You.com, and Recursive raised a $4.65B seed round to automate AI research itself. On Latent Space in September, Socher described an early "baby" version of its system. On Karpathy's NanoChat, a community contest to train a small language model to the lowest bits per byte, hundreds of people with their agents had reached 0.937. Recursive's system went lower in under two days, did the same on the NanoGPT training speedrun, and topped all but a handful of kernels on SOL-ExecBench (a GPU-kernel benchmark) without CUDA experts on the team. One finding cuts the other way: starting from Karpathy's own code reached a better result than starting from a plain transformer, so expert starting points still matter.

On 21 October, Recursive released Flint on Hugging Face. It is a mixture-of-experts model (only a few of its 256 expert blocks run per token) with 39.8B total and about 2.5B active parameters, a 262K-token context, and a June 2026 knowledge cutoff. It was trained from scratch in under four months, and Recursive says the Eureka Machine took part in ideation, implementation and validation, claiming a 71% size cut with almost no quality loss. LM Studio lists about 24GB to run it locally; users measured 114–132 tokens a second on an M5 Max, NVIDIA cites over 220 on a 64GB RTX Spark, and Recursive-built kernels added 55% speed there without changing weights. vLLM, SGLang and OpenRouter (free at launch) supported it on day one. Recursive positions it as an on-device complement to cloud agents, not a replacement.

### What changes
The wiki has nothing on Recursive or Flint. Its local-coding entries are Alibaba's Qwen models, and its autoresearch material covers harnesses and Palantir's training loop, not systems aimed at AI research.

- New page `models/recursive-flint.md`: specs, claimed scores, local speeds, the Eureka Machine's role, and caveats (no independent scores yet; Reddit sees it as arriving just after Qwen3.8-27B in the same class).
- **State of Models** adds Flint to Coding models. One Recent-changes entry; the list is at its cap, so the oldest entry moves to history.
- **Agent improvement loop** gains a paragraph under "Autoresearch over model weights" on Recursive's NanoChat, speedrun and kernel results, the expert-starting-point finding, and Flint as the loop's first shipped model, plus a Recent-changes entry.
- The index gains the Flint page and refreshes the improvement-loop line.
- Three new source pages: the model card, AINews's Flint story, and the Socher interview.

### What to weigh
The 21 October release date comes from AINews's launch-day coverage; the model card is undated. Agent improvement loop goes from 1,212 to about 1,320 body words, right at 110% of its ceiling: still a warning, not a split, but the next addition will make it a split candidate, and the two autoresearch sections (harness and weights/AI research) are the natural cut when that happens. State of Models ends near 108% of its ceiling, also within tolerance.

## Intended changes

- [ ] **Create** `wiki/models/recursive-flint.md` — new model page
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — add one Flint line under `### Coding models` (after Qwen 3.6 35B-A3B); add one Recent-changes entry dated 2026-10-21 (list is at the 10-entry cap, so the oldest entry spills); append source id `huggingface-recursive-flint-2026-10-21` to `sources:`; `as_of` unchanged (already newer)
    > See draft below

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — the oldest Recent-changes entry (currently the lower of the two 2026-10-19 entries, the Domain-specialized models / MedDecider-27B entry; the 2026-10-16 and 2026-10-17 entries already spilled today) moves to history
    > See draft below

- [ ] **Update** `wiki/concepts/agent-improvement-loop.md` — one paragraph appended to `## Autoresearch over model weights`; one Recent-changes entry dated 2026-10-21 (list at 8, no spill); append two source ids and two Sources lines; `as_of` unchanged (2026-10-24 is newer)
    > See draft below

- [ ] **Update** `wiki/index.md` — add `models/recursive-flint` under Models; refresh the agent-improvement-loop description; models count 50 → 51, total 311 → 312
    > See draft below

- [ ] **Create** `wiki/sources/articles/huggingface-recursive-flint-2026-10-21.md` — source summary (model card)

- [ ] **Create** `wiki/sources/newsletters/ainews-recursive-flint-2026-10-22.md` — source summary (AINews Flint story; one per story)

- [ ] **Create** `wiki/sources/newsletters/latent-space-socher-recursive-2026-09-14.md` — source summary (Socher interview)

## Page drafts

### wiki/models/recursive-flint.md (new)

```md
---
title: Recursive Flint
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights]
as_of: 2026-10-21
sources: [huggingface-recursive-flint-2026-10-21, ainews-recursive-flint-2026-10-22, latent-space-socher-recursive-2026-09-14]
---

# Recursive Flint

Recursive's open-weight mixture-of-experts model for coding agents, released 2026-10-21 under Apache 2.0. It has 39.8B total and about 2.5B active parameters per token and is built to run locally: Recursive positions it as an on-device complement to frontier cloud agents, not a replacement. Recursive (Richard Socher's company) says its automated research system, the Eureka Machine, helped design it.

## Current status (as of 2026-10-21)

- Claimed scores: Terminal-Bench 2.1 54.9% (Terminus 2 harness; web-retrieved solutions counted as failures), SWE-bench Pro v2 89.7%, SWE-bench Verified 74.2% (mini-swe-agent).
- 262K-token context; 49 layers (2 dense, 47 MoE), 256 routed experts with 6 per token plus a shared expert, mixed sliding-window and full attention; knowledge cutoff June 2026.
- Runs in about 24GB locally (LM Studio). Users measured 114–132 tok/s on an M5 Max (int4 MLX); NVIDIA cites over 220 tok/s on a 64GB RTX Spark; vLLM reports 500 tok/s on one GB200 at 100K context (NVFP4).
- Day-zero support in vLLM, SGLang (one B300 or H200 per replica) and OpenRouter (free at launch); NeMo fine-tuning recipes. No Transformers modeling code yet.

## Built by an automated research loop

Trained from scratch in under four months. Recursive says the Eureka Machine, which proposes ideas, implements them, runs experiments and picks follow-ups, contributed the sparse architecture, low-bit training and kernels, for a claimed 71% size reduction with almost no quality loss. Its kernels raised generation speed on RTX Spark by 55% without changing weights. See [Agent improvement loop](../concepts/agent-improvement-loop.md) for Recursive's earlier research-automation results.

## Weaknesses / caveats

- No independent benchmark results yet; comparison scores on the model card mix Recursive-measured and developer-reported numbers.
- r/LocalLlama read it as the "35B-A3B"-class model people wanted, but arriving after [Qwen 3.8 27B](qwen-3-8-27b.md) made it less of a surprise.
- Long reasoning can exhaust the output budget; Recursive recommends at least 32K output tokens for hard problems.

## Recent changes

- [2026-10-21] Released on Hugging Face (Apache 2.0) with day-zero vLLM, SGLang and OpenRouter support.

## Sources

- [RecursiveSI/flint model card — Hugging Face](../sources/articles/huggingface-recursive-flint-2026-10-21.md)
- [AINews — Flint launch and local serving (2026-10-22)](../sources/newsletters/ainews-recursive-flint-2026-10-22.md)
- [Latent Space — Richard Socher on AI for AI research](../sources/newsletters/latent-space-socher-recursive-2026-09-14.md)
```

### wiki/state-of/models.md (updated)

Frontmatter: append `huggingface-recursive-flint-2026-10-21` to `sources:` (no other change).

New line under `### Coding models`, inserted after the Qwen 3.6 35B-A3B line:

```md
- [Recursive Flint](../models/recursive-flint.md) — Recursive; 39.8B/2.5B-active MoE, Apache 2.0, runs in ~24GB locally at 114–150+ tok/s; claimed 89.7% SWE-bench Pro v2, 54.9% Terminal-Bench 2.1; partly designed by Recursive's automated research loop *(as of 2026-10-21)*
```

Recent changes (adds one entry, inserted by date between the live 2026-10-26 and 2026-10-20 entries; the oldest entry, the 2026-10-19 Domain-specialized models entry, is removed and spills to history):

```md
- [2026-10-21] Recursive Flint added to Coding models: a 40B/2.5B-active Apache 2.0 MoE that runs in about 24GB locally, with claimed 89.7% SWE-bench Pro v2, partly designed by Recursive's Eureka Machine.
```

### wiki/history/state-of/models.md (updated)

Appended at the end of the file. The file already ends with a 2026-11-24 archive block; if applied on that date, add the entry to that block instead of opening a new header:

```md

## Archived from current page on <apply date>

- [2026-10-19] Added the "Domain-specialized models" section with MedDecider-27B, a medical decision model that returns calibrated option probabilities without generating text.
```

### wiki/concepts/agent-improvement-loop.md (updated)

Frontmatter: append `latent-space-socher-recursive-2026-09-14, ainews-recursive-flint-2026-10-22` to `sources:` (`as_of` stays 2026-10-24).

Paragraph appended to the end of `## Autoresearch over model weights`:

```md
Recursive, Richard Socher's company ($4.65B seed), points the loop at AI research itself. Its early "baby" system, Socher said in September 2026, beat the best human-plus-agent results on Karpathy's NanoChat (bits per byte below the community's 0.937) and the NanoGPT training speedrun in under two days, and topped all but a handful of kernels on SOL-ExecBench with no CUDA experts on the team. Starting from Karpathy's code reached a better result than starting from a vanilla transformer, so expert starting points still matter. In October the same "Eureka Machine" helped design [Flint](../models/recursive-flint.md), a shipped open coding model: sparse architecture, low-bit training, and kernels that added 55% generation speed.
```

Recent changes (adds one entry; list goes from 8 to 9, no spill):

```md
- [2026-10-24] Added autoresearch over model weights: Palantir's AutoResearch loop from operational episodes through held-back evals and iterated training recipes to a gated deployment that feeds overrides back as training data.
- [2026-10-21] Added Recursive's AI-for-AI-research results (NanoChat, NanoGPT speedrun, SOL-ExecBench kernels; expert starting points still help) and Flint as the first shipped model its loop helped design.
- [2026-10-19] Split the harness-optimization sections (Better-Harness, self-improving skills) out to [Automated harness optimization](automated-harness-optimization.md), which also takes the new Harness² material.
```

Sources (appends two lines):

```md
- [Latent Space — Richard Socher on AI for AI research](../sources/newsletters/latent-space-socher-recursive-2026-09-14.md)
- [AINews — Flint launch and local serving (2026-10-22)](../sources/newsletters/ainews-recursive-flint-2026-10-22.md)
```

### wiki/index.md (updated)

New line under `## Models` (after the laguna-s-2-1 line):

```md
- [models/recursive-flint](models/recursive-flint.md) — Recursive's Apache 2.0 local coding MoE (39.8B/2.5B active, 262K context, ~24GB); claimed 89.7% SWE-bench Pro v2; partly designed by Recursive's Eureka Machine research loop *(as_of: 2026-10-21)*
```

Replaced line under `## Concepts`:

```md
- [concepts/agent-improvement-loop](concepts/agent-improvement-loop.md) — workflow for improving AI agents through traces, evals, autoresearch loops (including over model weights and AI research itself: Palantir AutoResearch, Recursive), trace-to-memory feedback, eval-suite hygiene, and production feedback *(as_of: 2026-10-24)*
```

Page count: `- models: 51` and `**Total content pages: 312.**`

### wiki/sources/articles/huggingface-recursive-flint-2026-10-21.md (new)

```md
---
title: RecursiveSI/flint model card — Hugging Face
type: source
source_type: article
source_file: raw/articles/2026-11-24-huggingfaceco-recursivesi-flint.md
url: https://huggingface.co/RecursiveSI/flint
published: 2026-10-21
ingested: 2026-11-24
domains: [models, coding]
---

# RecursiveSI/flint model card — Hugging Face

Recursive's Hugging Face model card for Flint, its open-weight MoE for coding agents: architecture, claimed benchmark scores and evaluation settings, SGLang serving kit, recommended sampling, training stages, limitations and the Apache 2.0 license. The card is undated; the release date comes from AINews's launch coverage.

## Influenced pages

- [Recursive Flint](../../models/recursive-flint.md) — new page
- [State of Models](../../state-of/models.md) — added to Coding models

## Key claims extracted

- 39.8B total parameters, about 2.5B active per token (2.2B excluding the output head); 49 layers (2 dense, 47 MoE); 256 routed experts, 6 per token, plus a shared expert
- 35 sliding-window layers (513-token window) and 14 full-attention layers; 262,144-token context; knowledge cutoff June 2026
- Terminal-Bench 2.1 54.9% (Terminus 2; solutions found via web retrieval counted as failures), SWE-bench Pro v2 89.7%, SWE-bench Verified 74.2% (mini-swe-agent); average pass@1 over at least five attempts
- Runs on one B300 or H200 per replica with the bundled SGLang kit; quantized variants for NVIDIA and Apple Silicon; no Transformers modeling code yet
- Trained from scratch through pretraining, mid-training, SFT and RL
- Recommended: temperature 1.0, top-p 0.95, top-k 20, at least 32,768 output tokens for hard problems
- Apache 2.0; hosted API terms are separate
```

### wiki/sources/newsletters/ainews-recursive-flint-2026-10-22.md (new)

```md
---
title: AINews — Flint launch and local serving (2026-10-22)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-22-ainews-openais-patch-the-planet-program-is-1-of.md
url: https://www.latent.space/p/ainews-openais-patch-the-planet-program
published: 2026-10-22
ingested: 2026-11-24
domains: [models, coding]
---

# AINews — Flint launch and local serving (2026-10-22)

The Flint story from AINews's 2026-10-22 issue (Other News plus the r/LocalLlama recap): Recursive's local coding MoE launched with broad local-serving support, claimed benchmark scores, measured local speeds, and the Eureka Machine's role in building it.

## Influenced pages

- [Recursive Flint](../../models/recursive-flint.md) — local speeds, availability, community reception, Eureka Machine contribution
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — Flint as a shipped model designed partly by an automated research loop

## Key claims extracted

- Apache 2.0 coding MoE, ~40B total / 2.5B active, 262K context; LM Studio says about 24GB locally; positioned as an on-device complement to frontier cloud agents
- Advertised short-context speeds over 125 tok/s on a MacBook Pro and 150 tok/s on RTX Spark; a user measured 114–132 tok/s on an M5 Max with int4 MLX
- NVIDIA (GTC Berlin) claims over 220 tok/s on a 64GB RTX Spark; Eureka Machine kernels improved RTX Spark generation speed by 55% without changing weights; NeMo Automodel SFT/LoRA and NeMo RL GRPO support
- Eureka Machine took part in ideation, implementation and validation (sparse architecture, low-bit training, kernels); claimed 71% size reduction with almost no quality loss; built from scratch in under four months
- Day-zero vLLM (500 tok/s on one GB200 at 100K context, NVFP4) and free OpenRouter access
- r/LocalLlama: the "35B-A3B"-class model people wanted, but Qwen3.8-27B made it less surprising
```

### wiki/sources/newsletters/latent-space-socher-recursive-2026-09-14.md (new)

```md
---
title: Latent Space — Why you should work on AI for AI research (Richard Socher, Recursive)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-14-why-you-should-work-on-ai-for-ai-research-richar.md
url: https://www.latent.space/p/recursive
published: 2026-09-14
ingested: 2026-11-24
domains: [agents, models]
---

# Latent Space — Why you should work on AI for AI research (Richard Socher, Recursive)

Latent Space interview with Richard Socher (You.com, AIX Ventures) about Recursive, his company aiming at recursive self-improvement by automating AI research. He walks through early results from a first "baby" version of the system and argues AI research that takes thousands of people years could shrink to weeks. The episode also covers reward hacking, constitutions, open source and regulation; only the research-automation results are used.

## Influenced pages

- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — Recursive's AI-for-AI-research results
- [Recursive Flint](../../models/recursive-flint.md) — company context

## Key claims extracted

- Recursive raised a $4.65B seed round to build the "Eureka Machine", an AI that automates invention, starting with AI research
- On Karpathy's NanoChat, where the community with agents reached 0.937 bits per byte, Recursive's early system went lower in under two days; it also beat the NanoGPT speedrun
- On SOL-ExecBench it was best on all but a handful of kernels, without deep CUDA expertise on the team
- Starting from an expert's code (Karpathy's) reached an even better result than starting from a vanilla transformer: human starting points still matter
```

## Schema / vocabulary additions

None.

## Open questions

None.
