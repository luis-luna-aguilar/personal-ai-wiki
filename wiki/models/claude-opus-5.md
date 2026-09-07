---
title: Claude Opus 5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-07-28
sources: [ainews-claude-opus-5-launch-2026-07-25, every-vibe-check-opus-5-2026-07-24, every-taming-opus-5-2026-07-28]
---

# Claude Opus 5

Anthropic's new flagship, launched 2026-07-24, superseding [Claude Opus 4.8](../history/models/claude-opus-4-8.md). Epoch's Capabilities Index puts it just behind Fable 5 (159 vs. 161) while tying Fable exactly on software-engineering capability (SWE-ECI 161 for both), at roughly half Fable's price. Practitioner reports are more divided than the benchmarks suggest: strong on hard coding and debugging grind, but harder to manage day-to-day than either Fable 5 or GPT-5.6 Sol.

## Current status (as of 2026-07-28)

- Epoch Capabilities Index: 159 (vs. Fable 5's 161); SWE-ECI: 161, tied with Fable 5
- Arena: #1 Frontend Code Arena and #1 Text Arena (Opus 5 Max); WeirdML 91.6%/91.8% (high/max), roughly tied with Fable 5 Max
- Every's week-long practitioner review: brilliant in flashes, but argues with instructions, narrates excessively, and stops before work is finished under the same management style that worked for earlier Claude models
- Works best given a full brief up front and left alone rather than managed step-by-step — Anthropic's own prompting guide makes the same recommendation
- Team verdict: doesn't reach Fable 5's ceiling and is less easy to live with day-to-day than GPT-5.6 Sol, but wins clearly on hard coding/debugging grind

## Strengths

- Hard coding and debugging tasks that reward sustained, unsupervised effort
- Strong when given a complete upfront brief and evaluated on the finished artifact rather than managed turn-by-turn

## Weaknesses / caveats

- Prickly and over-verbose in conversation; several practitioners reported it arguing with instructions and adopting a judgmental tone
- Needs a real prompting-style adjustment from earlier Claude models — skills/plugins built for Opus 4.8 and earlier reportedly worked against it until removed
- Several developers reported frustrating real-world behavior (overcomplication, breakage, poor stopping behavior) despite strong leaderboard numbers — a public-eval-vs-production gap AINews called out directly
- A FrontierCode anomaly: at least one evaluator saw better results at medium effort than high effort, unlike the model's usual pattern of improving with more inference-time effort

## Recent changes

- [2026-07-28] Practitioner reception update: Every's team-wide testing confirms the model's unruliness but converges on a fix — give it a complete upfront brief, let it run, then evaluate the finished artifact rather than its narration
- [2026-07-24] Launched: ECI 159, SWE-ECI 161 (tied with Fable 5), roughly half Fable 5's price; supersedes Claude Opus 4.8

## Sources

- [AINews — Claude Opus 5: Fable-level performance at Opus price](../sources/newsletters/ainews-claude-opus-5-launch-2026-07-25.md)
- [Every — Vibe Check: Claude Opus 5 is brilliant in flashes, frustrating in practice](../sources/newsletters/every-vibe-check-opus-5-2026-07-24.md)
- [Every — Taming Opus 5](../sources/newsletters/every-taming-opus-5-2026-07-28.md)
