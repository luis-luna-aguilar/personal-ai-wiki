---
title: Vals AI — CUA-bench leaderboard and methodology
type: source
source_type: article
source_file: raw/articles/2026-11-24-valsai-benchmarks-cua_bench.md
url: https://www.vals.ai/benchmarks/cua_bench
published: 2026-10-13
ingested: 2026-11-24
domains: [computer-use, agents]
---

# Vals AI — CUA-bench leaderboard and methodology

Vals AI's computer-use benchmark: agents play six commercial games, three named and three held out, for three hours each using only screen pixels, keyboard and mouse. Launched around 2026-09-19 (AINews); the date used is the "updated" stamp on Vals's benchmark list.

## Influenced pages
- [State of Computer Use](../../state-of/computer-use.md) — one-line CUA-bench pointer and Recent-changes entry
- [OSWorld](../../benchmarks/osworld.md) — one-line CUA-bench pointer as the real-time, pixel-only counterpart

## Key claims extracted
- Public games: Minecraft, SUPERHOT, eFootball; each paired with an unnamed held-out game of the same genre
- Per-game ladder of ordered milestones worth 100 points; score is the six-game mean
- Real time: latency counts against the model
- Nine models tested; GPT-6 Astra 26.7 public / 11.7 held out; Claude Opus 5.5 14.0 / 14.0; Claude Fable 5.1 22.3 / 4.0
- One trial per cell; public/held-out gaps are observed, not measured training effects
- Models run in their vendor's own CLI harness, driving a GPU game desktop over MCP
- Grading from native game state or signed recordings, not agent self-reports
