---
title: '[AINews] Gemini 4 Argon issue — GPT-6.1 Sol evals story'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafab.md
url: https://www.latent.space/p/ainews-gemini-4-argon-gdms-answer
published: 2026-10-01
ingested: 2026-10-20
domains: [models]
---

# AINews — GPT-6.1 Sol independent evals

The GPT-6.1 Sol story from AINews' Gemini 4 Argon issue: leaderboard placements, Artificial Analysis's per-task cost breakdown, the Luna image-encoding fix, and a hands-on read on the Ultrafast tier.

## Influenced pages

- [GPT-6.1 Sol](../../models/gpt-6-1-sol.md) — leaderboards, cost explanation, Ultrafast hands-on
- [GPT-6 Luna](../../models/gpt-6-luna.md) — image-encoding fix
- [Cost-aware routing evidence](../../training/cost-aware-routing-evidence.md) — per-task cost vs token use

## Key claims extracted

- #1 MathArena; #3 Code Arena WebDev at 1759, 70 points above GPT-6 Sol at the same $2/$10
- AA: $0.72 per task at max effort vs $3.26 for Astra and $1.04 for GPT-6 Sol; saving from fewer turns and a lower cache-read price
- AA Intelligence Index: Gemini 4 Argon 53, GPT-6 Astra 53, GPT-6.1 Sol 52
- OpenAI fixed an image-encoding bug, adding one Intelligence Index point to GPT-6 Luna
- Ultrafast: up to 300 tok/s on NVIDIA GPUs at low batch sizes (SemiAnalysis); generation about 8x faster but end-to-end agent tasks only 2–4x faster because tool latency dominates
