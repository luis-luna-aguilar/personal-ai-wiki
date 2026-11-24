---
title: An Empirical Study of Harness Design for Coding Agents
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-abs-260920804.md
url: https://arxiv.org/abs/2609.20804
published: 2026-09-17
ingested: 2026-11-24
domains: [agents, coding]
---

# An Empirical Study of Harness Design for Coding Agents

Most harness comparisons test whole products against each other, so nobody learns which part made the difference. This paper (read from its arXiv abstract) fixes one lightweight coding harness and changes one component at a time: planning, the action space (which tools the model gets), and context management. It covers four models on SWE-Bench Verified and Terminal-Bench 2.1, in 176 matched settings.

## Influenced pages
- [Harness vs model](../../concepts/harness-vs-model.md) — the "bash-capable models don't need predefined tools" condition in the tool-surface subsection

## Key claims extracted
- Context management matters more as the context budget tightens; most of its benefit is preventing context-overflow failures
- Rule-based elision before LLM summarization is the most efficient context strategy tested; making elided content recoverable adds machinery models rarely use, with no accuracy gain
- Planning is an accuracy scaffold for weaker models and a cost saver for stronger ones
- Predefined tools help models with weak bash skills; bash-capable models work well with a bash-only interface at substantially lower cost, especially on command-line tasks
