---
title: "MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems"
type: source
source_type: paper
source_file: raw/papers/2026-08-25-arxivorg-abs-260518565v2.md
url: https://arxiv.org/abs/2605.18565v2
published: 2026-05-19
ingested: 2026-08-25
domains: [agents]
---

# MINTEval (arXiv paper)

Hyunji Lee et al. introduce MINTEval, a benchmark for long-horizon agent memory under multi-target interference — contexts with frequently updated, interconnected information, where earlier facts may be revised or contradicted later.

## Influenced pages
- [Agent memory](../../concepts/agent-memory.md) — added MINTEval as independent benchmark evidence for the "memory as systems problem" thesis

## Key claims extracted
- 15.6k question-answering pairs; long-horizon contexts averaging 138.8k tokens, extending up to 1.8M tokens per instance
- Four domains: state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits
- Two question types: single-target recall and multi-target aggregation
- Evaluated 7 systems (vanilla long-context LLMs, RAG, memory-augmented agent frameworks): consistently low performance, average accuracy 27.9%, worst on questions requiring aggregation over multiple pieces of evidence
- Performance is primarily limited by retrieval and memory construction; accuracy degrades further as the number of intervening updates increases
- v1 submitted 2026-05-18, v2 (current) 2026-05-19; only the abstract page was fetched

## Verification note
The "best system 33.4%" figure quoted on the agent-memory page comes from AINews' recap of the authors' thread, not from this abstract; it is attributed accordingly there.
