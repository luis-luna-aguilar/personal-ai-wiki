---
title: Muse Wonder
type: model
domains: [models, coding, agents]
subcategory: frontier-model
tags: [meta, closed-source, frontier, agentic]
as_of: 2026-10-20
sources: [ainews-muse-wonder-launch-2026-10-13, ainews-muse-wonder-reception-2026-10-14, ainews-muse-wonder-agent-arena-2026-10-15, ainews-muse-wonder-code-arena-prometheus-2026-10-20]
---

# Muse Wonder

Meta Superintelligence Labs' second model family, launched 2026-10-12 about 14 months after the lab was founded: "a much larger and more advanced class of models" than [Muse Spark](muse-spark.md), sitting above Spark and [Muse Glimmer](muse-glimmer.md) in Meta's lineup. Two tiers: **Muse Wonder** (fast frontier) and **Muse Wonder Full** (maximum reasoning).

## Current status (as of 2026-10-20)

- **Access and pricing:** Wonder via the Meta Model API and [Muse Code](../tools/muse-code.md) at $4 / $20 per 1M input/output tokens ($0.20 cached input); Wonder Full only for Muse Code subscribers, with no token price. Wonder powers [Meta Muse](../tools/meta-muse.md), subscribers first
- **Specs:** 1M context; text, image, video and audio input, text output; trained on Meta's gigawatt-scale Prometheus cluster
- **Pitched features:** Active Memory (context across days and months), Active Focus (persisting through blockers), finance and legal expertise
- **Artificial Analysis:** Intelligence Index 56 (Full) and 52 (Wonder), up from Spark 1.3's 48; Opus 5.5 leads at 58. Terminal-Bench 4.0 33% → 57%; Full is top three on 6 of 10 index evals. Coding Agents Index in Muse Code: 68 (Full), tying Claude Code + Sonnet 5.5 and above Opus 5.5 (66). Wonder costs $4.52 per index task, driven by input tokens
- **Other evals:** Vals Index #5 (Full), ahead of every OpenAI model; Agent Arena #12 at $1.13 per task; Code Arena WebDev #6 (Full Max, 1726), making Meta the #3 lab there
- **Meta's own table:** SWE-Marathon 57.5% (Opus 5.5 46.3%), DeepSWE 79.0% (Opus 74.2%), Harvey LAB 13.1 (Astra 8.6), MemoryBench 85.5 (Opus 81.5)

## Reception

Theo ranked Full alongside Opus 5.5 and above GPT-6.1 Sol, praising its prose and code review. Others found it strong at agentic tasks, coding and email but weak at frontend design, SVG and creative work; one skeptic put Meta 3–6 months behind OpenAI and Anthropic. Theo also noted the two tiers are "very different models": Full matches Opus on AA, while Wonder trails GPT-6.1 Sol at similar token use.

## Weaknesses / caveats

- Wonder Full has no published token price, so its cost per task can't be compared
- MemoryBench tests updated facts within one long conversation, not durable cross-session memory; some headline wins rely on Meta's internal evals
- Launch-day bug drained Muse Code quotas (fixed same day); users report exhausting $200 plans within a day
- No detailed system card

## Recent changes

- [2026-10-20] Wonder Full (Max) debuts #6 in Code Arena WebDev; Meta discloses Prometheus training-cluster goodput.
- [2026-10-15] Agent Arena #12 at $1.13 per task.
- [2026-10-12] Launched: Wonder and Wonder Full; AA Intelligence Index 56/52; Coding Agents Index 68 in Muse Code; Vals Index #5.

## Sources

- [AINews — Meta launches Muse Wonder and Wonder Full](../sources/newsletters/ainews-muse-wonder-launch-2026-10-13.md)
- [AINews — Muse Wonder positioning and reception](../sources/newsletters/ainews-muse-wonder-reception-2026-10-14.md)
- [AINews — Muse Wonder in Agent Arena](../sources/newsletters/ainews-muse-wonder-agent-arena-2026-10-15.md)
- [AINews — Muse Wonder in Code Arena; Prometheus cluster](../sources/newsletters/ainews-muse-wonder-code-arena-prometheus-2026-10-20.md)
