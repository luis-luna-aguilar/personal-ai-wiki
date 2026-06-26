---
type: proposal
source: raw/newsletters/2026-06-10-ainews-anthropic-claude-fable-5-mythos-but-saf.md
status: pending
created: 2026-06-17
---

# Proposal: Agents' Last Exam (ALE) benchmark

## Summary

ALE (Agents' Last Exam) is a new benchmark designed to evaluate agents on real-world professional task performance aligned with actual labor-market occupations. 1,500+ tasks across 55 occupations, built by 300+ domain experts from 100+ institutions. Key finding: top agents score only 2.6% on the hardest tier — a useful counterpoint to claims that AI is displacing knowledge workers broadly. Source was a brief mention in the AINews Fable 5 issue; this is a lightweight ingest.

## Intended changes

- [x] **Create** `wiki/benchmarks/agents-last-exam.md` — new benchmark page
    > See draft below

- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add ALE as a concrete measurement of agent capability vs labor market readiness
    > **Before** (`## Concrete signals`, after the last bullet point):
    > (no ALE reference)
    > **After** (append new bullet):
    > `- **Agents' Last Exam (ALE, 2026):** Labor-market-aligned benchmark across 1,500+ tasks and 55 occupations. Top agents score 2.6% on the hardest tier. Provides a grounded counterpoint to displacement narratives: agents can do some professional tasks autonomously, but the hardest tier of real occupation-scoped work remains largely out of reach.`
    > **Update `## Recent changes`:**
    > `- [2026-06-10] Added ALE benchmark: 1,500+ tasks, 55 occupations, 300+ domain experts; top agents 2.6% on hardest tier — measurement of the gap between benchmark coding performance and real occupational task performance`

- [x] (Source already created as `wiki/sources/newsletters/ainews-fable5-june-2026.md` in the Fable 5 proposal)

## Open questions

- ALE was a brief mention in AINews — the primary source for more detail would be the ALE website or paper. This proposal treats it as a lightweight entry based on the available signal. A follow-up ingest from the primary ALE source could expand benchmarks and methodology.

## Page drafts

### wiki/benchmarks/agents-last-exam.md (new)

```md
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
```
