---
title: "Agents' Last Exam (ALE)"
type: benchmark
domains: [agents]
tags: [benchmark, labor-market]
as_of: 2026-06-10
sources: [ainews-fable5-june-2026]
---

# Agents' Last Exam (ALE)

ALE is a benchmark designed to evaluate AI agents on tasks that reflect real-world professional work across actual labor-market occupations — as opposed to synthetic programming problems or exam-style reasoning.

## What it measures

Unlike SWE-bench (software engineering tasks) or FrontierCode (code mergeability), ALE is explicitly occupation-scoped. Tasks are drawn from real professional work and evaluated on whether an agent can autonomously complete them to professional standard.

- **Scale:** 1,500+ tasks
- **Occupational scope:** 55 distinct occupations
- **Contributor pool:** 300+ domain experts across 100+ institutions
- **Design goal:** performance on ALE should predict labor displacement risk, not just coding ability

## Tiers

ALE has at least three tiers of task difficulty, from standard occupational tasks to the hardest professional edge cases.

## Current results (as of 2026-06-10)

- **Top agents on hardest tier:** 2.6% task completion

This is a significantly lower number than SWE-bench or similar coding benchmarks, suggesting that agent capability is highly domain-specific and does not automatically transfer from well-benchmarked domains (coding) to the broader landscape of knowledge work occupations.

## Why it matters

ALE provides empirical grounding for the question "how displaced are knowledge workers right now?" The answer it suggests: less than coding benchmarks imply. Agents that score 80%+ on SWE-bench score ~2.6% on the hardest occupational tasks in other professions.

This does not mean agents are not impactful — it means the impact is concentrated in specific task types (code, structured data, document extraction) where agents were specifically trained and tested, rather than uniformly distributed across all professional knowledge work.

## Recent changes

- [2026-06-10] Launched; top agent score: 2.6% on hardest tier; 1,500+ tasks, 55 occupations

## Sources

- [AINews — Fable 5 launch issue (June 10)](../sources/newsletters/ainews-fable5-june-2026.md)
