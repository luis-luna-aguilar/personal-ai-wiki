---
title: Composer 2.5
type: model
domains: [coding, models]
subcategory: coding-model
tags: [closed-source]
as_of: 2026-05-18
sources: [cursor-composer-2-5-launch]
---

# Composer 2.5

Composer 2.5 is Cursor's in-house long-horizon coding model, an upgrade of Composer 2 announced May 18, 2026. It keeps the same Moonshot Kimi K2.5 base as its predecessor but changes how it's trained: targeted reinforcement learning with textual hints inserted at specific trajectory failure points, plus KL distillation between a hinted teacher and an unhinted student, over 25× more synthetic tasks than Composer 2 — including a new "feature deletion" task type meant to test whether the model removes code correctly rather than only adding it.

## Current status (as of 2026-05-18)

- Same Kimi K2.5 base as Composer 2; upgrade is in training method and data, not base model
- Targeted RL with textual feedback (hints at problem trajectory points) plus KL distillation between a hinted teacher and unhinted student
- 25× more synthetic tasks than Composer 2, including a new "feature deletion" task type
- Sharded Muon + dual mesh HSDP optimizer; reported 0.2s step time on a 1T-parameter model
- Pricing: $0.50/M input, $2.50/M output standard; $3.00/M input, $15.00/M output fast variant
- Cursor's next model is training on a SpaceX partnership at Colossus 2 scale (targeting million H100-equivalents)
- Backs [Cursor](../tools/cursor.md)'s coding workspace; remains Cursor's separate, smaller-weight-class model alongside [Grok 4.6](grok-4-6.md) (the jointly trained SpaceXAI model line, launched in July 2026 as Grok 4.5 and superseded 2026-08-13)

## Strengths

- Purpose-built training data (feature-deletion tasks) targets a specific failure mode — models that only know how to add code
- Unusually low input-token pricing for a frontier-adjacent coding model

## Weaknesses / caveats

- Benchmarks and pricing come from Cursor's own launch post; no independent replication captured
- Available only inside Cursor products; no standalone API

## Recent changes

- [2026-05-18] Launched: upgrade from Composer 2, targeted RL + KL distillation training method, 25× synthetic tasks, new pricing tiers

## Sources

- [Cursor Composer 2.5 — launch post](../sources/articles/cursor-composer-2-5-launch.md)
