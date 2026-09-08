---
type: proposal
source: raw/newsletters/2026-08-21-simulation-the-new-scaling-law-joon-sung-park.md
status: pending
created: 2026-09-07
---

# Proposal: Simile's $2B round and the "synthetic human subject" thesis

## Summary

### The source

Two sources tell one story. The first is a Latent Space podcast with Joon Sung Park, the researcher behind the 2023 "Generative Agents" (Smallville) paper, who has since cofounded Simile AI — a company that just raised a $2B Series B from GreenOaks and Index Ventures, backed by Fei-Fei Li and Andrej Karpathy. Simile builds "digital twins": models post-trained not on general web text but on two-hour biographical interviews, transaction and observational data, and registered randomized-controlled-trial data pulled from the Open Science Framework. Park's core claim is that frontier chat models make poor stand-ins for real people precisely because they're trained to be rational and helpful — Simile instead wants a model that makes the same mistakes and holds the same inconsistent biases a specific person would. Their flagship result: digital twins reproduce a real person's survey and behavioral answers 85% as accurately as that person reproduces their own answers two weeks later, versus roughly 20-60% for a frontier model simply prompted to role-play the person. Customers including CVS, Wealthfront, Gallup, and Deloitte use the models for concept testing, synthetic focus groups, and population-level simulation (even earnings-call reaction modeling) in place of human panels.

The second source, a same-week AINews essay, places Simile inside a longer arc: since 2022, one part of the ML pipeline after another has flipped from human-supplied to model-supplied — the reward signal/judge (RLHF, then RLAIF, then LLM-as-judge), the training data (Phi's synthetic textbooks), the teacher (distillation from Alpaca through DeepSeek-R1), the curriculum (self-rewarding models choosing their own training tasks), the researcher (autoresearch loops), and the RL environment itself (Z.ai's fully synthesized training environments behind GLM-5.3). The essay frames Simile as the next flip: the human "subject" — the source of preferences and behavior that everything else was trying to satisfy — going synthetic too. It argues the one part of the loop that resists this pattern is the physical world, where wet-lab experiments still can't be fully simulated away.

### What changes

No wiki page currently covers AI-simulated human populations or "digital twin" modeling as a category, so this proposes a new trend page rather than an update to an existing one.

- New page `trends/synthetic-human-simulation.md`, covering Simile's approach and results plus the "synthetic-everything" framing as connective context, with `domains: [agents, models]`.
- New source page for the Latent Space Simile podcast.
- New source page for the AINews "synthetic-everything" essay — this same raw file is also referenced (for different content) by a separate proposal on DeepSeek-V4-Flash-Vision-Exp; if that proposal lands first, this one's Influenced-pages line gets appended to the existing source page rather than creating a duplicate.
- Updates `wiki/index.md` to list the new page and bump the trend/total page counts.

### What to weigh

The 85%-accuracy figure and the customer list come entirely from Simile's own published research and the podcast interview — there is no independent third-party evaluation cited in either source, so the page should read as a company's reported result, not a verified benchmark. The "synthetic-everything" eight-stage framing is a single newsletter's editorial synthesis rather than an established industry taxonomy; it's included here as useful narrative scaffolding, not as a wiki-endorsed model of the field. Whether this deserves a `trend` page versus a `concept` page is a genuine judgment call — I went with trend since the immediate news hook (a $2B round) is time-bound, but the underlying idea (behavior foundation models) may prove more conceptual and durable than that framing suggests.

## Intended changes

- [x] **Approve all**

- [ ] **Create** `wiki/trends/synthetic-human-simulation.md` — new trend page
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-simile-simulation-2026-08-21.md` — source summary
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-10-worse-100x-cheaper-2026-08-22.md` — source summary
    > See draft below

- [ ] **Update** `wiki/index.md` — add new trend page entry, bump page counts
    > See draft below

## Page drafts

### wiki/trends/synthetic-human-simulation.md (new)

```md
---
title: AI-simulated human populations
type: trend
domains: [agents, models]
tags: [agentic]
as_of: 2026-08-22
sources: [latent-space-simile-simulation-2026-08-21, ainews-10-worse-100x-cheaper-2026-08-22]
---

# AI-simulated human populations

The trend: models trained specifically to reproduce how real people behave — not just what they say — are emerging as a distinct category, positioned as a replacement for focus groups, user panels, and market-research surveys rather than as general-purpose assistants.

## Current signal

- **Simile AI ($2B Series B, August 2026):** cofounded by Joon Sung Park (author of the 2023 "Generative Agents"/Smallville paper), Simile builds "digital twins" post-trained on two-hour biographical interviews, transaction/observational data, and registered randomized-controlled-trial data from the Open Science Framework. Reported result: digital twins reproduce a real person's survey and behavioral responses 85% as accurately as the person reproduces their own answers two weeks later — versus 20-60% for frontier chat models prompted to role-play the same person, because frontier models are trained to be rational/agentic rather than to copy human bias, inconsistency, and "irrational" behavior.
- Simile trains two distinct model types — population-level and individual-level — and reports early scaling laws: more human behavioral data and compute produce predictable gains in simulation accuracy, the same shape as pretraining scaling laws.
- Customers reportedly include CVS, Wealthfront, Gallup (a strategic partnership), and Deloitte, using the models for concept testing, synthetic focus groups, and earnings-call reaction simulation at the population level rather than one-off individual prediction.
- **The broader pattern:** an AINews essay frames Simile as "Stage 7" of a longer sequence in which each part of the ML pipeline has gone synthetic in turn since 2022 — the reward/judge (RLHF → RLAIF → LLM-as-judge), training data (Phi's textbooks, WRAP), the teacher (Alpaca/distillation), the curriculum (self-rewarding models), the researcher (AlphaEvolve, autoresearch loops), and the RL environment (Z.ai's synthesized-environment pipeline behind GLM-5.3) — leaving the human "subject" (preferences, behavior, demand) as the next component to be modeled rather than measured directly. The one stage the essay argues resists full synthesis is the physical world (wet-lab science, embodied experiment).

## Why it matters

If digital twins are accurate enough to substitute for real user panels on concept testing and policy questions, it reframes market research and UX testing as an inference workload rather than a data-collection exercise — and raises the same "is the sample actually representative" question that election polling already has to answer, just moved into a trained model instead of a survey methodology.

## What to watch

- Whether independent, non-Simile-run evaluations confirm the 85% figure and how it degrades outside the population/task types Simile has already validated
- Whether other approaches (Shopify's SimGym, Tencent's cruder billion-persona cross-matrix method) converge on "post-train specifically on human behavioral data," or stay closer to prompting frontier models with demographic priors
- Whether this becomes its own state-of subcategory, or stays a niche layered on top of existing agent/research tooling

## Recent changes

- [2026-08-22] Page created: Simile's $2B Series B and 85%-accuracy digital-twin claim, framed within a broader "synthetic-everything" pattern (judge → data → teacher → curriculum → researcher → environment → human subject) traced back to 2022.

## Sources

- [Latent Space — Simulation: the new Scaling Law (Joon Sung Park, Simile AI)](../sources/newsletters/latent-space-simile-simulation-2026-08-21.md)
- [AINews — 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking over](../sources/newsletters/ainews-10-worse-100x-cheaper-2026-08-22.md)
```

### wiki/sources/newsletters/latent-space-simile-simulation-2026-08-21.md (new)

```md
---
title: "Simulation: the new Scaling Law — Joon Sung Park, Simile AI"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-21-simulation-the-new-scaling-law-joon-sung-park.md
url: https://www.latent.space/p/simile
published: 2026-08-21
ingested: 2026-09-07
domains: [agents, models]
---

# Simulation: the new Scaling Law — Joon Sung Park, Simile AI

Latent Space podcast interview with Simile AI cofounder Joon Sung Park (author of the 2023 "Generative Agents"/Smallville paper), given shortly after Simile's $2B Series B. Covers the shift from generative agents to "digital twins" trained on interviews, transaction/observational data, and registered RCTs; the 85%-accuracy replication result against a 1,000-person study; why frontier models make poor human simulators; population- vs. individual-level models; and the long-term ambition to simulate large populations for product, policy, and social-science questions.

## Influenced pages

- [AI-simulated human populations](../../trends/synthetic-human-simulation.md) — new page

## Key claims extracted

- Simile raised a $2B Series B (GreenOaks, Index Ventures; backed by Fei-Fei Li, Andrej Karpathy)
- Digital twins reproduce real people's survey/behavioral responses 85% as accurately as the people reproduce their own answers two weeks later
- Frontier models prompted to role-play the same people score 20-60% on the same replication task
- Training data comes in three buckets: interview data, observational/transaction behavioral data, and causal data from randomized controlled trials (sourced partly from the Open Science Framework)
- Simile trains separate population-level and individual-level models
- Reports early scaling laws: more human behavioral data and compute predictably improve simulation accuracy
- Customers include CVS, Wealthfront, Gallup (strategic partnership), Deloitte

### wiki/sources/newsletters/ainews-10-worse-100x-cheaper-2026-08-22.md (new)

```md
---
title: "AINews — 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking over"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-22-ainews-10-worse-100x-cheaper-10000x-faster-w.md
url: https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x
published: 2026-08-22
ingested: 2026-09-07
domains: [agents, models]
---

# AINews — 10% worse, 100x cheaper, 10000x faster: Why Simulation is taking over

An AINews essay arguing that one component of the ML pipeline after another has gone synthetic since 2022 — reward/judge, training data, teacher, curriculum, researcher, and RL environment — with the human "subject" (preferences, behavior, demand) next, framing Simile as the concrete current example. The same issue's Twitter/Reddit recap also covers DeepSeek's V4-Flash-Vision-Exp launch and continued Qwen3.8-27B momentum, which a separate proposal draws on.

## Influenced pages

- [AI-simulated human populations](../../trends/synthetic-human-simulation.md) — new page, primary source for the "synthetic-everything" framing
- [DeepSeek V4](../../models/deepseek-v4.md) — V4-Flash-Vision-Exp multimodal update, from this issue's Twitter/Reddit recap

## Key claims extracted

- Eight-stage synthetic-pipeline framing: reward signal (2022) → training data (2023) → teacher (2023) → curriculum (2024) → researcher (2026) → RL environment (2026) → human subject (2025/2026, Simile) → physical world (in progress, resists full synthesis)
- Frames Simile's digital twins as "Stage 7," citing its 85%-accuracy replication result
- Cites Z.ai/GLM-5.3's synthesized-environment training pipeline as the concrete "Stage 6" example
- Physical-world experiments (wet-lab science) are argued to be the one stage that can't be fully synthesized, only compressed
- DeepSeek shipped DeepSeek-V4-Flash-Vision-Exp: multimodal (text+image) input, 83.9 Terminal-Bench 2.1, 75.9 Toolathlon-Verified, 64.3 Chartography, positioned as closing the gap to Opus-4.8

### wiki/index.md (updated)

> **Before** (`## Trends` section, last line):
> ```
> - [trends/ai-music-commercialization](trends/ai-music-commercialization.md) — AI music moving from novelty to commercial category; ElevenMusic, Suno, Udio as early anchors; rightsholder economics emerging *(as_of: 2026-05-01)*
> ```
> **After** (adds a new line at the end of `## Trends`):
> ```
> - [trends/ai-music-commercialization](trends/ai-music-commercialization.md) — AI music moving from novelty to commercial category; ElevenMusic, Suno, Udio as early anchors; rightsholder economics emerging *(as_of: 2026-05-01)*
> - [trends/synthetic-human-simulation](trends/synthetic-human-simulation.md) — models trained on interviews, transaction data, and RCTs to reproduce real human behavior for concept testing and synthetic panels, led by Simile AI *(as_of: 2026-08-22)*
> ```
>
> **Before** (`## Page count`):
> ```
> - trends: 12
> ...
> **Total content pages: 188.**
> ```
> **After:**
> ```
> - trends: 13
> ...
> **Total content pages: 189.**
> ```

## Open questions

- Is `trend` the right type, or should this be a `concept` page given the underlying idea (behavior foundation models) may outlast the current news cycle? I defaulted to `trend` since a funding round is the immediate hook.

