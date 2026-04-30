---
title: '"Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain'
type: source
source_type: tweet
source_file: raw/tweets/2026-04-10-vtrivedy10-2041927488918413589.md
url: https://x.com/Vtrivedy10/status/2041927488918413589
published: 2026-04-10
ingested: 2026-04-10
domains: [agents]
---

# Better Harness: A Recipe for Harness Hill-Climbing with Evals

LangChain shares Better-Harness, an open-source prototype for autonomously improving agent harnesses using evals as a hill-climbing signal. Sources evals from hand-curation, production traces, and external datasets; uses optimization/holdout splits to guard against overfitting; iteratively diagnoses failures and proposes scoped harness changes.

## Influenced pages

- [[concepts/agent-improvement-loop]] — added Better-Harness section as concrete implementation

## Key claims extracted

- `harness + evals + harness engineering → better agent` (analogous to model training)
- Eval sources: hand-curated, production traces, external datasets
- Optimization/holdout split per behavioral category prevents overfitting
- One scoped change per iteration (may include prompt + tool together)
- Tested with Claude Sonnet 4.6 and GLM-5; near-full generalization to holdout
- Common changes: prompt/instruction updates, tool description edits, new tool additions
- Human review remains a gate — catches overfit instructions and token waste
- Open-sourced as a prototype for builders
