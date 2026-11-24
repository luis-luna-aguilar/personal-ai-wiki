---
title: 'Protocol-Preserving Context Trimming for Agentic Workflows: Benefits, Failure Regimes, and Budget Guardrails'
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-abs-260916461.md
url: https://arxiv.org/abs/2609.16461
published: 2026-09-15
ingested: 2026-11-24
domains: [agents]
---

# Protocol-Preserving Context Trimming for Agentic Workflows

Long agent runs keep growing their history, so harnesses trim it, and trimming is usually judged by how many tokens it removes. This single-author paper (read from its arXiv abstract) also checks whether the task still succeeds. It compares five strategies across retained-context levels and workflow complexity: recency, relevance, summarization, protocol-aware trimming (keep the state the workflow depends on, compress the rest) and adaptive budget guardrails.

## Influenced pages
- [Context editing](../../concepts/context-editing.md) — "Trim by protocol, not by recency" bullet

## Key claims extracted
- Conventional strategies: about 60% mean token savings, task success 66.6–77.3%, protocol adherence 85.5–88.6%
- Protocol-aware trimming: 92.2% task success; with adaptive guardrails 96.0% success, 96.3% protocol adherence, 1.0% cascading failure, 56.0% token savings
- Retaining 25% or less of context raised failure odds 10.92-fold vs 50% or more
- Critical context thresholds rise with workflow complexity
