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
