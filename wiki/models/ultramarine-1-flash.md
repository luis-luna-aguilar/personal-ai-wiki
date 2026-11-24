---
title: Ultramarine 1 Flash
type: model
domains: [models, finance, legal]
subcategory: domain-specialized-model
tags: [agentic]
as_of: 2026-10-14
sources: [paper-instruments-ultramarine-1-flash-2026-10-14, bertgodel-ultramarine-launch-2026-10-14]
---

# Ultramarine 1 Flash

Paper Instruments' agentic model for professional knowledge work (finance, law, consulting, operations): Z.ai's open GLM-5.3 Flash (see [GLM-5.3](glm-5-3.md)) with a large reinforcement-learning stage on synthetic tasks graded by rubrics. Its main contribution is a recipe for RL on work that has no single right answer; see [Non-verifiable RL](../concepts/non-verifiable-rl.md).

## Current status (as of 2026-10-14)

- Released 2026-10-14 on API; weights, training code, and tech report promised within two weeks. Post-trained by a team of five for about $300k all-in
- Beats its base on all six knowledge-work benchmarks reported (+4.1 points on average) with 6.5% fewer output tokens
- Internal PI Knowledge Work suite: 59.3 at $0.13 per task, vs Claude Fable 5 57.8 at $8.19 and GPT-5.6 Sol 55.1 at $2.09; trails Claude Opus 5.5 by 2.6 points ($6.96) and GPT-6 Sol by 2.0 ($1.26)
- Leads JobBench (62.9) and FrontierFinance (53.3) in its comparison set; behind Gemini 3.8 Flash and Fable 5 on DiligenceBench and APEX-Agents 1.1 (57.0 vs 64.3)
- Coding slips slightly below the base: Terminal-Bench 2.1 83.2 (base 84.3), DeepSWE 61.5 (base 63.4)

## How it was trained

- **Rubric-graded RL.** Each task is synthesised with its rubric, one checkable proposition per criterion ([Non-verifiable RL](../concepts/non-verifiable-rl.md))
- **Synthetic curriculum.** 88 environment types across 19 practice areas, each a workspace of real filings and synthetic documents plus live CRM, ERP, and ticketing systems behind MCP
- **Minimal harness.** Its own Feather harness with a 50-token system prompt; production instructions added only at the end (see [RL harness quality](../concepts/rl-harness-quality.md))

## Weaknesses / caveats

- The "Fable 5-level at 60x cheaper" headline comes from the launch thread; the report's strongest comparison is its own internal suite, and DiligenceBench is also the lab's own benchmark
- No vision training
- Weights not yet released as of the launch date

## Recent changes

- [2026-10-14] Released on API with a technical report; weights promised within two weeks.

## Sources

- [Ultramarine 1 Flash: Scaling Non-Verifiable RL](../sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md)
- [Daanish Khazi — Ultramarine 1 Flash launch thread](../sources/tweets/bertgodel-ultramarine-launch-2026-10-14.md)
