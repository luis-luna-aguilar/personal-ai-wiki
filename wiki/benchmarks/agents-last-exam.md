---
title: "Agents' Last Exam (ALE)"
type: benchmark
domains: [agents]
tags: []
as_of: 2026-11-23
sources: [ainews-fable5-june-2026, ainews-june-06-2026, openai-introducing-gpt-6-2-astra-sol]
---

# Agents' Last Exam (ALE)

ALE is a benchmark designed to evaluate AI agents on tasks that reflect real-world professional work across actual labor-market occupations — as opposed to synthetic programming problems or exam-style reasoning.

## What it measures

Unlike SWE-bench (software engineering tasks) or FrontierCode (code mergeability), ALE is explicitly occupation-scoped. Tasks are drawn from real professional work and evaluated on whether an agent can autonomously complete them to professional standard.

- **Scale:** 1,500+ tasks
- **Occupational scope:** 55 distinct occupations
- **Contributor pool:** 300+ domain experts across 100+ institutions
- **US occupational taxonomy mapping:** tasks are drawn from and mapped to actual US occupational classifications to enable direct labor displacement analysis
- **Design goal:** performance on ALE should predict labor displacement risk, not just coding ability

## Tiers

ALE has at least three tiers of task difficulty, from standard occupational tasks to the hardest professional edge cases.

## Current results (as of 2026-11-23)

- **Top agents on hardest tier:** 2.6% task completion
- **v1.1 (OpenAI, 2026-11-23):** [GPT-6.2 Astra](../models/gpt-6-2-astra.md) sets a new high, 5.2 points above GPT-6 Astra at under a third of the cost and 5.5 points above Claude Fable 5.2 at 5% of the cost. OpenAI notes the leaderboard's Fable 5.2 result excludes nine tasks that used a fallback model. Absolute scores and the tier were not captured.

This is a significantly lower number than SWE-bench or similar coding benchmarks, suggesting that agent capability is highly domain-specific and does not automatically transfer from well-benchmarked domains (coding) to the broader landscape of knowledge work occupations.

## Why it matters

ALE provides empirical grounding for the question "how displaced are knowledge workers right now?" The answer it suggests: less than coding benchmarks imply. Agents that score 80%+ on SWE-bench score ~2.6% on the hardest occupational tasks in other professions.

This does not mean agents are not impactful — it means the impact is concentrated in specific task types (code, structured data, document extraction) where agents were specifically trained and tested, rather than uniformly distributed across all professional knowledge work.

## Recent changes

- [2026-11-23] OpenAI reports GPT-6.2 Astra sets a new high on ALE v1.1 (+5.2 over GPT-6 Astra, +5.5 over Claude Fable 5.2).
- [2026-06-10] Launched; top agent score: 2.6% on hardest tier; 1,500+ tasks, 55 occupations
- [2026-06-06] US occupational taxonomy mapping detail confirmed from June 6 AINews; design goal: ALE scores predict labor displacement risk, not just coding ability

## Sources

- [AINews — Fable 5 launch issue (June 10)](../sources/newsletters/ainews-fable5-june-2026.md)
- [AINews — SWE-Marathon, Meta-Agent Challenge, Sakana RSI Lab (June 6)](../sources/newsletters/ainews-june-06-2026.md)
- [OpenAI — Introducing GPT-6.2 Astra and Sol](../sources/articles/openai-introducing-gpt-6-2-astra-sol.md)
