---
title: "[AINews] OpenAI GPT-next disproves 80 year old Erdős planar unit distance problem for under $1000"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md
url: https://www.latent.space/p/ainews-openai-gpt-next-disproves
published: 2026-05-21
ingested: 2026-08-25
domains: [agents, models]
---

# AINews — Erdős result and agent-benchmark cluster

AINews Twitter-recap issue whose headline story is an OpenAI general-purpose model's disproof of a long-standing Erdős unit-distance conjecture (not covered on this page). This summary covers the agent-benchmark cluster from the same issue — InferenceBench, Terminal-Bench Science, and MINTEval, all three checked against their primary sources (two arXiv abstract pages and the Terminal-Bench Science site) rather than taken on this newsletter's word alone — plus the issue's Cohere Command A+ recap. Two figures appear only in this recap and are attributed to it where used: the InferenceBench "inverse scaling" claim and MINTEval's best-system 33.4%.

## Influenced pages
- [InferenceBench](../../benchmarks/inferencebench.md) — discovery source; factual claims sourced from the primary arXiv abstract; supplies the attributed, unverified inverse-scaling caveat
- [Terminal-Bench](../../benchmarks/terminal-bench.md) — discovery source; factual claims sourced from the primary tbench.ai announcement
- [Agent memory](../../concepts/agent-memory.md) — discovery source; factual claims sourced from the primary MINTEval arXiv abstract; supplies the attributed best-system 33.4% figure
- [Cohere Command A+](../../models/cohere-command-a-plus.md) — secondary source for AA placement and community architecture discussion (Cohere's own post is the primary source)
- [State of Models](../../state-of/models.md) — new Open-weight models entry
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new bullet on fully-open releases broadening beyond the usual labs

## Key claims extracted
- InferenceBench: frontier agents underperform a simple vLLM/SGLang hyperparameter-tuning baseline; reported (but not primary-source-confirmed) inverse-scaling effect where Claude Sonnet 4.6 and GLM-5 rank well by preserving robust final states
- Terminal-Bench Science: extends agent evaluation into real scientific workflows; task contributions open
- MINTEval: long-context memory under frequent updates/interference; average instance length 138.8k tokens (up to 1.8M); average accuracy across 7 systems 27.9% (matches the primary abstract), best system 33.4% (recap-only; not in the abstract)
- Command A+ released as Apache 2.0 open weights; Cohere's first fully open Apache 2.0 model per Cohere co-founder @aidangomez
- ~218B MoE / 25B active, multimodal, 48 languages; runs on as little as 2x H100s at W4A4; vLLM day-0 support
- Artificial Analysis: Intelligence Index 37, "around Claude 4.5 Haiku territory," with especially strong non-hallucination behavior and decent speed but weaker scientific reasoning and coding than top peer models
- Community architecture discussion (not confirmed by Cohere): parallel transformer block, large shared-expert usage, LayerNorm over RMSNorm, 32-layer depth, atypical head/expert configuration
