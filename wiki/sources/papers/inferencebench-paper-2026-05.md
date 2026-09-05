---
title: "InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents"
type: source
source_type: paper
source_file: raw/papers/2026-08-25-arxivorg-abs-260720468.md
url: https://arxiv.org/abs/2607.20468
published: 2026-05-20
ingested: 2026-08-25
domains: [agents, coding]
---

# InferenceBench (arXiv paper)

Jehyeok Yeon, Ben Rank, and Maksym Andriushchenko introduce InferenceBench: agents must deploy and optimize an OpenAI-compatible LLM inference server under a two-hour, one-H100 budget, across four optimization scenarios (prefill latency, decode latency, concurrent-request throughput, and a balanced mix). The goal is to test genuine open-ended optimization rather than retrieval of a memorized solution recipe.

## Influenced pages
- [InferenceBench](../../benchmarks/inferencebench.md) — new benchmark page

## Key claims extracted
- Across 15 frontier agent configurations, agents beat a naive PyTorch baseline by up to 8.08x and often match/exceed default-settings vLLM (4.05x)
- Agents still fall short of a simple hyperparameter search under the same budget (up to 11.53x) — the paper's central negative result
- Agents overwhelmingly converge on a single inference framework (the abstract does not name it or give a percentage)
- Agents enumerate many relevant techniques but test only a few distinct configurations, spending remaining budget re-measuring, repairing, or tuning hyperparameters rather than exploring substantially different strategies
- The authors' conclusion: the bottleneck is not domain knowledge but proposing diverse configurations, evaluating them systematically, and submitting the best one
- Submitted to arXiv 2026-05-20 (cs.AI); only the abstract page was fetched

## Verification note
AINews' secondary recap additionally claimed an "inverse scaling" finding — smaller models like Claude Sonnet 4.6 and GLM-5 ranking better by preserving robust final states. This claim does not appear in the fetched abstract; the full paper body was not fetched, so this specific claim is flagged unverified rather than included on the benchmark page as confirmed.
