---
title: Vals AI — ClaimBench leaderboard and methodology
type: source
source_type: article
source_file: raw/articles/2026-11-24-valsai-benchmarks-claimbench.md
url: https://www.vals.ai/benchmarks/claimbench
published: 2026-11-20
ingested: 2026-11-24
domains: [models, finance]
---

# Vals AI — ClaimBench leaderboard and methodology

Vals AI's benchmark for whether a decision model can take over checking claims against SEC 10-K filings: 1,960 claims, each labeled supported, contradicted or insufficient evidence against an excerpt. It ranks 30 decision models alone and measures a cascade where each sends low-confidence claims to an LLM. AINews reported an earlier version (Decider V1.2) on 2026-10-21; this page's 20 November numbers replace it.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — ClaimBench added to the Benchmarks bullet

## Key claims extracted
- Five claim categories of about 392 each: direct support, subtle contradiction, numeric discrepancy, missing evidence, non-supporting citation; gold labels from the construction rule
- Standalone leaders: d1-ultra 100.00%, Decider V1.3 99.80%, d1.2-ultra 99.75%
- Cascade: threshold set for at most 1% errors on 30% of claims, frozen, applied to the other 70%
- Decider V1.3 → Claude Haiku 5.5: 99.85% accuracy, $0.10 per 1,000 claims; Haiku label call alone $1.19
- Decider V1.3 latency 1.7 s per claim vs 5.1 s for Haiku 5.5
- Subtle contradiction is the hardest category (Decider V1.3 99.0%; weakest models about 50%)
