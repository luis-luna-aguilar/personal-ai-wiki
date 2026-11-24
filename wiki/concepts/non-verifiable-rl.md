---
title: Non-verifiable RL
type: concept
domains: [models, agents]
tags: [agentic]
as_of: 2026-10-14
sources: [paper-instruments-ultramarine-1-flash-2026-10-14, bertgodel-ultramarine-launch-2026-10-14]
---

# Non-verifiable RL

Reinforcement learning on work that has no automatic checker, such as diligence memos, board pre-reads or legal analysis. Coding RL can reward a model when the tests pass; for open-ended professional deliverables the reward has to come from a rubric that a judge model grades. The hard part moves from the model to the rubric: it must state what a correct answer contains precisely enough to reward good work and refuse plausible errors.

## Current status (as of 2026-10-14)

- **Task and rubric are written together.** Paper Instruments synthesises each training task with its rubric instead of grading against one golden answer, then filters for answer leakage and reward hacking.
- **One proposition per criterion.** A criterion copied from a golden answer ("uses the phrase 'sole forecast basis'") rejects valid alternatives; a vague one ("provides a useful update") rewards plausible errors. A good criterion states one checkable condition, with the entities, dates and thresholds needed, judged met or unmet; independent accomplishments stay separate so partial work earns partial credit. The lab argues criterion boundaries matter more than a stronger judge.
- **Synthetic workspaces, not production traces.** Real user traces bake one person's unstated assumptions into the reward, so the curriculum was fully synthetic: 88 environment types with real filings, synthetic documents and live business systems.
- **It works at small-lab scale.** [Ultramarine 1 Flash](../models/ultramarine-1-flash.md) gained 4.1 points over its base across six knowledge-work benchmarks, post-trained by five people for about $300k; coding slipped slightly.

## Why it matters

Most business work an agent does has no compiler or test suite. If rubric-graded RL holds up, small labs can post-train open models for specific professions cheaply, and the same rubric discipline carries over to judging deployed agents with LLM judges.

## Related

- [Evals for workflow and task agents](../training/evals-for-agentic-work.md) — the same rubric discipline applied to judging deployed agents
- [RL harness quality](rl-harness-quality.md) — environment failure modes that corrupt any RL reward, verifiable or not

## Recent changes

- [2026-10-14] Page created from Paper Instruments' Ultramarine 1 Flash report.

## Sources

- [Paper Instruments — Ultramarine 1 Flash: Scaling Non-Verifiable RL](../sources/articles/paper-instruments-ultramarine-1-flash-2026-10-14.md)
- [Daanish Khazi — Ultramarine 1 Flash launch thread](../sources/tweets/bertgodel-ultramarine-launch-2026-10-14.md)
