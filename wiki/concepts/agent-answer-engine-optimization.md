---
title: Agent answer-engine optimization (AEO)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-07
sources: [latent-space-aeo-tracker-2026-09-07]
---

# Agent answer-engine optimization (AEO)

The practice — and the measurable phenomenon behind it — of optimizing content and positioning so AI models recommend a product or tool when a user asks an agent for a suggestion, the LLM-era successor to search-engine optimization. Latent Space's "Frontier AEO tracker" is the first published attempt to measure it directly: six prompt variations across seven frontier models and 161 product categories, scored on first-choice weight, alternative-mention weight, and negative weight for anti-recommendations.

## Current status (as of 2026-09-07)

- Models show meaningful self-bias recommending tools from their own ecosystem: Fable/Opus favor Claude Code, Sol/Astra favor Codex, Grok favors Cursor, Muse favors Muse Code, SWE-1.7 favors Devin
- 28 of 161 tracked categories have a genuinely universal top choice across all surveyed models — the rest are contested "AEO battlegrounds"
- Anthropic's models cite more sources per answer than OpenAI's (Opus median 11, Fable median 15, vs. Sol median 9, Astra median 5)
- Astra is unusually "sticky": its answer rarely flips when a question is lightly paraphrased, raising the practical value of optimizing specifically for it
- Methodology is inspectable — every prompt/answer pair is published — but the project has a stated commercial angle (AEO-as-a-service)

## Why it matters

As agents increasingly mediate product discovery, self-serving bias in tool recommendations becomes a competitive dynamic worth tracking in its own right, distinct from raw model capability — and a second independent measurement of the same effect would meaningfully strengthen this still single-source finding.

## Recent changes

- [2026-09-07] Page created from Latent Space's Frontier AEO tracker.

## Sources

- [Latent Space — The Frontier AEO Tracker](../sources/newsletters/latent-space-aeo-tracker-2026-09-07.md)
