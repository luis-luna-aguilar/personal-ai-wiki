---
type: proposal
source: raw/newsletters/2026-07-19-the-model-is-the-easy-part.md
status: pending
created: 2026-09-06
---

# Proposal: Arkadium's 4.6M-parameter model beats frontier LLMs at games, for $60/year

## Summary

### The source
Every's July 19 newsletter ("The Model Is the Easy Part") tells the story of Arkadium, a game publisher with hundreds of titles and tens of millions of players, working with Every's own Good Start Labs on Game Lab — a public leaderboard, built in partnership with Meta and DeepMind, that scores how well frontier models play simple games. The headline result: models that make novel math and science discoveries lose roughly 90% of their Gin Rummy games against casual human players, because frontier training data contains almost no Gin Rummy. Arkadium's fix wasn't a bigger model — it was a much smaller one. They trained a purpose-built 4.6-million-parameter model (an 18-megabyte file, runs on a regular CPU) that beats human players about 90% of the time. The economics are the real story: at 1 million requests a day, that expert model costs roughly $60/year to run, versus multi-millions for an equivalent-volume frontier LLM. Every frames this as a broader lesson about AI adoption maturing past "get the tool in people's hands" toward defining a measurable goal first — which is what revealed that a frontier LLM wasn't the right tool for Arkadium's goal at all.

### What changes
The wiki's cost-aware task-routing page already argues that narrow, well-defined tasks are often better served by small, purpose-built models than frontier LLMs, backed by evidence like Bridgewater's tuned Qwen3-235B and Databricks' harness-cost benchmark.

- **Cost-aware AI task routing** gains a new evidence bullet: the Arkadium/Game Lab result, with the concrete $60/year-vs-multi-millions cost ratio and the "frontier models are shaped by what they've seen" framing for why a general-purpose model loses to a narrow specialist on an out-of-distribution task. Page date moves to 19 July.
- New source page for the Every newsletter.

### What to weigh
Nothing beyond the sourcing noted above — this is a single newsletter's own reporting on a partnership Every itself worked on (Good Start Labs), so it's a first-party account rather than independent verification, but the specific numbers (parameter count, file size, cost estimate) are stated plainly enough to record as-is.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add one new "Evidence from practice" bullet; bump `as_of` and merge new source id
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/arkadium-game-lab-small-model-economics-2026-07-19.md` — source summary

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter changes:
```
as_of: 2026-07-19
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07, the-code-databricks-coding-benchmark-2026-07-10, databricks-benchmarking-coding-agents-2026-07, the-code-eval-data-moat-2026-07-13, ainews-devin-fusion-router-moat-2026-07-14, arkadium-game-lab-small-model-economics-2026-07-19]
```

New bullet, appended to `## Evidence from practice` (after the Databricks bullet):
```
- **Arkadium's Game Lab.** Game publisher Arkadium, working with Every's Good Start Labs, Meta, and DeepMind on a public model-vs-human game leaderboard, found that frontier models making novel math and science discoveries lose about 90% of their Gin Rummy games against casual players — because frontier training data contains almost no Gin Rummy. Arkadium's fix was a purpose-built 4.6-million-parameter model (an 18MB file, runs on a regular CPU) that beats human players roughly 90% of the time. At 1 million requests/day, it costs about $60/year to run, versus multi-millions for an equivalent-volume frontier LLM — a concrete cost ratio for routing well-defined, out-of-distribution-for-frontier tasks to a narrow specialist instead.
```

New line, appended to `## Sources`:
```
- [Every — The Model Is the Easy Part (Arkadium/Game Lab)](../sources/newsletters/arkadium-game-lab-small-model-economics-2026-07-19.md)
```

### wiki/sources/newsletters/arkadium-game-lab-small-model-economics-2026-07-19.md (new)

```md
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
```

## Open questions
None.
