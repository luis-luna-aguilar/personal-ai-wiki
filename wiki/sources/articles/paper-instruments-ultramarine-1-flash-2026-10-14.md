---
title: 'Ultramarine 1 Flash: Scaling Non-Verifiable RL — Paper Instruments'
type: source
source_type: article
source_file: raw/articles/2026-10-20-tco-bq3ymfajqh.md
url: https://www.paperinstruments.com/blog/ultramarine
published: 2026-10-14
ingested: 2026-10-20
domains: [models, agents, finance, legal]
---

# Ultramarine 1 Flash: Scaling Non-Verifiable RL — Paper Instruments

Technical report for Ultramarine 1 Flash, a reinforcement-learning post-train of GLM-5.3 Flash for professional knowledge work. The core contribution is a recipe for rewarding open-ended deliverables: tasks and rubrics are synthesised together, each criterion tests one proposition, and filters screen for answer leakage and reward hacking. The curriculum is fully synthetic (88 environment types across finance, law, consulting, operations), trained in the lab's minimal Feather harness on E2B sandboxes with a modified CISPO objective, LoRA rank 64, and 131k context.

## Influenced pages

- [Ultramarine 1 Flash](../../models/ultramarine-1-flash.md) — new page
- [Non-verifiable RL](../../concepts/non-verifiable-rl.md) — new concept page: task and rubric co-design, one proposition per criterion
- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — one-proposition-per-criterion rubric guidance
- [RL harness quality](../../concepts/rl-harness-quality.md) — three environment-design choices

## Key claims extracted

- Improves on GLM-5.3 Flash across all six knowledge-work benchmarks, +4.1 points on average, with 6.5% fewer tokens
- PI Knowledge Work (internal): 59.3 at $0.13/task vs Fable 5 57.8 ($8.19), GPT-5.6 Sol 55.1 ($2.09); within 2.6 of Opus 5.5 and 2.0 of GPT-6 Sol
- JobBench 62.9, FrontierFinance 53.3, APEX-Agents 1.1 57.0 (Gemini 3.8 Flash 64.3); Terminal-Bench 2.1 83.2 (base 84.3)
- Overfit criteria reject valid answers; vague criteria reward plausible errors; criterion boundaries matter more than a stronger judge
- Production traces rejected as RL data because they embed one user's unstated assumptions into the reward
- Environment failures are excluded from training, not scored zero; agent loop and grader sit outside the sandbox
- Training system prompt is ~50 tokens; production instructions only introduced in final stages
