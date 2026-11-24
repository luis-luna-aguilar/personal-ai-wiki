---
title: Jacky Kwok — Introducing Contrastive Language Model (CLM)
type: source
source_type: tweet
source_file: raw/tweets/2026-09-23-jackyk02-2102905335925424285.md
url: https://x.com/jackyk02/status/2102905335925424285
published: 2026-09-23
ingested: 2026-10-20
domains: [models, agents]
---

# Jacky Kwok — Introducing Contrastive Language Model (CLM)

Launch thread for CLM-8B, an open-weight decision model that embeds the situation and each candidate action separately and ranks them by similarity, instead of scoring options with a head on one LLM pass.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — contrastive variant, verifier claim

## Key claims extracted
- Up to 9x faster than Jev at comparable computer-use, gaming and tool-calling performance
- After light fine-tuning: DeepSWE 81.6%, Terminal-Bench 2.1 87.6% as a verifier; "Jev fails to serve as an effective verifier" on these long-horizon tasks
- State and action embeddings are cached independently, which helps when the state changes but the action set does not
- Trained on 60M Q&A pairs, 30M synthetic hard negatives and 1M agent trajectories; loss follows power-law scaling
