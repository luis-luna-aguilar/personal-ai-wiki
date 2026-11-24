---
title: 'Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-21-jev-system-one-models-for-prod-not-god-with-di.md
url: https://www.latent.space/p/jev
published: 2026-09-21
ingested: 2026-10-20
domains: [models]
---

# Latent Space — Jev: System One models for Prod, not God (Diogo Almeida)

Long interview with TypeSafe CEO Diogo Almeida, a co-author of InstructGPT, a week after Jev's launch. He explains Jev as a model built for software rather than chat: three question types instead of generated text, trained for calibrated probabilities instead of human preference. He also covers TypeSafe's refusal to publish benchmarks or refuse requests, and its practice of freezing each model version.

## Influenced pages
- [Jev](../../models/jev.md) — what it is, primitives, RLCD, product stance
- [Decision models](../../concepts/decision-models.md) — definition, "System One" alias, design advice
- [State of Models](../../state-of/models.md) — Decision models section

## Key claims extracted
- Three primitives: Noulli (from Bernoulli; probability a statement is true), Choice (pick among options), Score (position on a scale); mapped to if, switch and sort
- RLCD (reinforcement learning for calibrated decisions) is unpublished; Almeida argues RLHF causes mode collapse and miscalibration
- TypeSafe is "extremely anti-public benchmarks"; Jev does not refuse, because a refusal inside a software dependency breaks the software
- Deployed model versions are never changed
- Advice: ask many small independent questions in parallel rather than one compound instruction
