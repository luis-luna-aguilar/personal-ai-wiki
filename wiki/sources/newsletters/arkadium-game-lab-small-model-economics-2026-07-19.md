---
title: "Every — The Model Is the Easy Part (Arkadium/Game Lab)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-19-the-model-is-the-easy-part.md
published: 2026-07-19
ingested: 2026-09-06
domains: [agents, models]
---

# Every — The Model Is the Easy Part (Arkadium/Game Lab)

Every's July 19 newsletter, reported by Good Start Labs (which worked directly with Arkadium), describes Game Lab — a public leaderboard built with Meta and DeepMind that scores how well frontier models play simple games. Frontier models that make novel scientific discoveries lose about 90% of their Gin Rummy games against casual humans; Arkadium instead trained a 4.6M-parameter, 18MB expert model that wins about 90% of the time at roughly $60/year to run at 1M requests/day, versus multi-millions for a frontier LLM at the same volume.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — new evidence bullet on narrow purpose-built models beating frontier LLMs on out-of-distribution tasks, with a concrete cost ratio

## Key claims extracted

- Frontier models (including ones that make novel math/science discoveries) lose ~90% of Gin Rummy games against casual human players.
- Arkadium trained a 4.6M-parameter, 18MB expert model that beats human players ~90% of the time, running on a regular CPU.
- At 1M requests/day, the expert model costs ~$60/year to run; an equivalent-volume frontier LLM would cost multi-millions.
- Game Lab is a public leaderboard built by Arkadium with Every's Good Start Labs, Meta, and DeepMind.
