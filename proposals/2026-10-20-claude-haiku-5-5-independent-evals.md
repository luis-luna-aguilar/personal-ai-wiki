---
type: proposal
source: raw/newsletters/2026-10-08-ainews-claude-haiku-55-better-than-gpt-6-luna.md
sources:
  - raw/newsletters/2026-10-08-ainews-claude-haiku-55-better-than-gpt-6-luna.md
  - raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
  - raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Claude Haiku 5.5 — independent evals temper the launch numbers

## Summary

### In short

Haiku 5.5 is cheap per token but not always per task: it beats GPT-6 Luna on independent tests, yet it reasons so heavily that its token bills can erase the price advantage. Artificial Analysis scores it 43 on its Intelligence Index against Luna's 38, using about three times Luna's output tokens. Vals finds it costs more per test than Haiku 4.5 on every shared benchmark. The proposal adds an independent-evals section to the Haiku 5.5 page, a caveat to the routing page and the real 7 October launch date across five pages. Reasons to hesitate: the launch date is inferred, and page dates move backwards from a fetch-date fallback.

[[#Open questions|Open questions: none.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

Three AINews issues from 8 to 10 October cover Claude Haiku 5.5, Anthropic's first new small model in about a year. The 8 October issue covers news from 6–7 October. It says Anthropic "shipped" Haiku 5.5 at exactly GPT-6 Luna's price ($0.10 input and $0.50 output per million tokens on prompts under 100k tokens). Anthropic halved Sonnet 5.5's cache-read price on the same day. The previous day's issue doesn't mention Haiku, so the launch was almost certainly 7 October.

Artificial Analysis supplied the most detailed outside numbers. Haiku 5.5 scores 43 on its Intelligence Index, slightly ahead of GLM-5.3 Flash (42), Gemini 3.8 Flash (41) and Luna (38), and 13 points behind Sonnet 5.5. It hallucinates far less than Luna: when it doesn't know, it more often says so. On Terminal-Bench 4.0 the independent run gives 33%, below the 39.2% in Anthropic's own table. An automation benchmark came in at 35%, but a pre-release safety bug made the model refuse too often. Anthropic is fixing it, and AA will re-run the test.

The main caveat is token use. At max effort Haiku 5.5 writes about 162,000 output tokens per index task, roughly three times Luna. Even at equal scores it is the wordier model. Vals reaches the same conclusion from another angle: the model takes many more steps (59 against Haiku 4.5's 17 on a legal-research task), so it costs more per test than Haiku 4.5 on every benchmark they share, despite a far lower token price. On the positive side, Vals has it third on Vibe Code Bench at 90.4%. Arena puts it at 1587 on WebDev, 257 points above Haiku 4.5 and six above Luna at the same price.

### What changes

The Haiku 5.5 page and its links were written from Anthropic's launch page. That page has no date, so the 19 October fetch date was used, and the launch-day Sonnet cache-read cut carries the same date.

- **Claude Haiku 5.5** gains the launch date and an "Independent evals and token use" section. The launch Recent-changes entry is re-dated to 7 October, and one entry is added. Page date moves from 19 to 10 October. This is the agreed exception for fallback dates.
- **Cost-aware AI task routing**: the Haiku tier-split bullet gains one sentence on per-task cost. Its Haiku entry is re-dated to 7 October, and one entry is added.
- **Claude Sonnet 5.5**: the cache-read entry is re-dated from 19 to 7 October, and the page date moves to 7 October.
- **State of Models** and the **index**: the Haiku line gains the AA score and moves to 10 October; the Sonnet line's stamp moves to 7 October; the launch entry is re-dated in place (no spill).
- The existing launch source page gains `published: 2026-10-07`. There are three new source pages.

### What to weigh

The 7 October date is inferred from AINews coverage windows, not stated by Anthropic. Several page dates move backwards, which the usual rule forbids. That is justified only because the old dates were fetch dates.

## Intended changes

- [ ] **Update** `wiki/models/claude-haiku-5-5.md` — launch date, new "Independent evals and token use" section; `as_of` 2026-10-19 → 2026-10-10 (fallback-date correction); sources merged. Recent changes: re-dates the live launch entry from 2026-10-19 to 2026-10-07 and adds one entry dated 2026-10-10 (2 entries, no spill).
    > See draft below

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — one sentence appended to the "Anthropic's own tier split for Haiku 5.5" bullet; re-dates the live entry "[2026-10-19] Added Anthropic's Haiku 5.5 / Sonnet 5.5 / Opus 5.5 tier split…" to 2026-10-07 and adds one entry dated 2026-10-08 (net +1, no spill); merges 2 source ids and 2 Sources links. `as_of` stays 2026-10-19 (other entries carry that date).
    > See draft below

- [ ] **Update** `wiki/models/claude-sonnet-5-5.md` — re-date the cache-read entry from 2026-10-19 to 2026-10-07 (it was announced with Haiku 5.5); `as_of` → 2026-10-07 if no newer-dated claim is on the page (fallback-date correction); add source id and link.
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — Haiku 5.5 leader line; re-date the live entry "[2026-10-19] Claude Haiku 5.5 launched; new Small / fast models section…" to 2026-10-07 and move it below the remaining 2026-10-19 entries (count unchanged, no spill); the Sonnet 5.5 line's date stamp becomes 2026-10-07 (the cache-read price it quotes dates from the Haiku launch; text otherwise unchanged)
    > **Before:** `- [Claude Haiku 5.5](../models/claude-haiku-5-5.md) — Anthropic; cheapest/fastest Claude tier, ~75% cheaper than Haiku 4.5; OSWorld 2.1 72.4%, GDPval-AA 1620; first Haiku with effort control; aimed at subagent, compaction, and high-volume work *(as of 2026-10-19)*`
    > **After:** `- [Claude Haiku 5.5](../models/claude-haiku-5-5.md) — Anthropic, launched 2026-10-07; cheapest/fastest Claude tier at GPT-6 Luna's price; AA Intelligence Index 43 (Luna 38), OSWorld 2.1 72.4%; heavy token use can make it costlier per task than Haiku 4.5; aimed at subagent, compaction, and high-volume work *(as of 2026-10-10)*`

- [ ] **Update** `wiki/index.md` — Haiku 5.5 line; the Sonnet 5.5 line's date stamp becomes `(as_of: 2026-10-07)`, text otherwise unchanged
    > **Before:** `- [models/claude-haiku-5-5](models/claude-haiku-5-5.md) — Anthropic's cheapest/fastest small model; ~75% cheaper than Haiku 4.5, first Haiku with effort control; for subagent, compaction and high-volume work *(as_of: 2026-10-19)*`
    > **After:** `- [models/claude-haiku-5-5](models/claude-haiku-5-5.md) — Anthropic's cheapest/fastest small model (launched 2026-10-07); ~75% cheaper per token than Haiku 4.5 but heavy token use per task; AA Intelligence Index 43, ahead of GPT-6 Luna; for subagent, compaction and high-volume work *(as_of: 2026-10-10)*`

- [ ] **Update** `wiki/sources/articles/claude-haiku-5-5-launch-2026-10-19.md` — add `published: 2026-10-07`; correct the "fetch date is used" sentence

- [ ] **Create** `wiki/sources/newsletters/ainews-claude-haiku-5-5-2026-10-08.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-haiku-5-5-vals-cost-per-test-2026-10-08.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-haiku-5-5-arena-webdev-2026-10-10.md`

## Page drafts

### wiki/models/claude-haiku-5-5.md (updated)

Changed frontmatter, intro, status heading, new section and Recent changes/Sources. "Evidence from early users", "Safety" and "Related" stay as they are; the new section goes between "Current status" and "Evidence from early users".

```
---
title: Claude Haiku 5.5
type: model
domains: [models]
subcategory: small-model
tags: [anthropic]
as_of: 2026-10-10
sources: [claude-haiku-5-5-launch-2026-10-19, ainews-claude-haiku-5-5-2026-10-08, ainews-haiku-5-5-vals-cost-per-test-2026-10-08, ainews-haiku-5-5-arena-webdev-2026-10-10]
---

# Claude Haiku 5.5

Anthropic's smallest, fastest and cheapest current Claude model, launched 2026-10-07 at GPT-6 Luna's token price, built for high-volume, cost-sensitive work: summaries, context compaction, database queries, classification, live customer support, browser use, and subagent roles under [Opus 5.5](claude-opus-5-5.md) or [Sonnet 5.5](claude-sonnet-5-5.md).

## Current status (as of 2026-10-10)

- Available on the Claude Platform as `claude-haiku-5-5`, and on AWS, Google Cloud and Microsoft Azure.
- First Haiku-class model with an adjustable effort setting (Low through Max).
- Pricing per 1M tokens, prompts up to / over 100k tokens: input $0.10 / $0.50, output $0.50 / $2.50, cache writes $0.125 / $0.625, cache reads $0.01 / $0.05 (Haiku 4.5: $1.00 / $5.00 / $1.25 / $0.10). Anthropic says it costs around 75% less than Haiku 4.5 on average, and that prompts up to 100k made up about 90% of Haiku 4.5 requests.
- Launch benchmarks (Haiku 5.5 / Haiku 4.5 / GPT-6 Luna / Sonnet 5.5): GDPval-AA v2.1 1620 / 735 / 1437 / 1840; AA-Briefcase v1.1 1578 / 614 / 1336 / 1824; OSWorld 2.1 offline subset 72.4% / 15.7% / 48.9% / 83.9%; Humanity's Last Exam 45.9% no tools, 57.4% with tools (Sonnet 5.5: 56.9% / 64.5%); Terminal-Bench 4.0 39.2% / 0.0% / 16.4% / 70.6%; FrontierCode 1.1 (Main) 46.4% / — / 42.4% / 52.1% (xhigh); Chartography 46.4% / 6.4% / 29.1% / 61.6% (no tools).
- Anthropic says Sonnet 5.5 and Opus 5.5 remain the better choice for complex agentic coding. Haiku 5.5 targets narrowly scoped tasks that were previously too expensive to run on Claude.
- 1M-token context window (Haiku 4.5: 200k); text and image input.

## Independent evals and token use

- **Ahead of Luna on capability.** Artificial Analysis: Intelligence Index 43 at max effort, ahead of GLM-5.3 Flash (42), Gemini 3.8 Flash (41) and GPT-6 Luna (38), 13 points behind Sonnet 5.5. Lower hallucination than its peers (40% against Luna's 77%), partly because it more often says it doesn't know. Vals: 90.4% on Vibe Code Bench (#3); #16 on the Vals Index. Arena WebDev 1587, 257 above Haiku 4.5 and six above Luna at the same price.
- **Below Anthropic's own numbers in places.** AA measures Terminal-Bench 4.0 at 33% (Anthropic: 39.2%). AutomationBench came in at 35%, against 53–60% for Luna and other small models, depressed by a pre-release over-refusal bug Anthropic is fixing; AA will re-run it.
- **Heavy token use.** At max effort it writes about 162k output tokens per AA index task, roughly 3x Luna, and going from xhigh to max adds 2 points for about 1.8x the tokens. Vals finds it takes many more steps (59 against Haiku 4.5's 17 on legal research) and so costs more per test than Haiku 4.5 on every shared benchmark, despite the lower token price. Set effort deliberately and measure cost per task.

## Recent changes

- [2026-10-10] Independent evals added: AA Intelligence Index 43 (ahead of GPT-6 Luna's 38), Terminal-Bench 4.0 33% against Anthropic's 39.2%, and heavy token use that makes it costlier per test than Haiku 4.5 on Vals.
- [2026-10-07] Launched: about 75% cheaper than Haiku 4.5, first Haiku with effort control, large benchmark gains over Haiku 4.5.

## Sources

- [Claude Haiku 5.5 launch](../sources/articles/claude-haiku-5-5-launch-2026-10-19.md)
- [AINews — Claude Haiku 5.5 launch and Artificial Analysis evals](../sources/newsletters/ainews-claude-haiku-5-5-2026-10-08.md)
- [AINews — Haiku 5.5 on Vals and Arena](../sources/newsletters/ainews-haiku-5-5-vals-cost-per-test-2026-10-08.md)
- [AINews — Haiku 5.5 Arena WebDev rank](../sources/newsletters/ainews-haiku-5-5-arena-webdev-2026-10-10.md)
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter `sources:` — append `ainews-claude-haiku-5-5-2026-10-08, ainews-haiku-5-5-vals-cost-per-test-2026-10-08`.

Sentence appended to the end of the "**Anthropic's own tier split for Haiku 5.5.**" bullet (before "See [Claude Haiku 5.5]…"):

```
Independent tests temper the price story: Haiku 5.5 writes about 3x GPT-6 Luna's output tokens per task at max effort, and Vals finds it costs more per test than Haiku 4.5 on every shared benchmark, so a cheaper token does not guarantee a cheaper task.
```

`## Recent changes` — the live entry `- [2026-10-19] Added Anthropic's Haiku 5.5 / Sonnet 5.5 / Opus 5.5 tier split and Cognition's Haiku-sidekick result to Model and harness selection wins.` becomes the dated entry below, re-sorted under the remaining 2026-10-19 entries, and one new entry is inserted above it:

```
- [2026-10-08] Added independent per-task cost evidence for Haiku 5.5 (heavy token use; costlier per test than Haiku 4.5 on Vals) to the Anthropic tier-split bullet.
- [2026-10-07] Added Anthropic's Haiku 5.5 / Sonnet 5.5 / Opus 5.5 tier split and Cognition's Haiku-sidekick result to Model and harness selection wins.
```

`## Sources` — append:

```
- [AINews — Claude Haiku 5.5 launch and Artificial Analysis evals](../sources/newsletters/ainews-claude-haiku-5-5-2026-10-08.md)
- [AINews — Haiku 5.5 on Vals and Arena](../sources/newsletters/ainews-haiku-5-5-vals-cost-per-test-2026-10-08.md)
```

### wiki/models/claude-sonnet-5-5.md (updated)

Frontmatter: `as_of` → `2026-10-07` unless the live page carries a claim dated later; `sources:` append `ainews-claude-haiku-5-5-2026-10-08`. If the live heading reads `## Current status (as of 2026-10-20)` or `(as of 2026-10-19)`, it takes the same date as `as_of`.

The cache-read Recent-changes entry, re-dated (and re-sorted by date):

```
- [2026-10-07] Cache reads halved from $0.20 to $0.10 per 1M tokens, announced with Haiku 5.5; Anthropic says this makes Sonnet 5.5 about 20% cheaper on most agentic work.
```

`## Sources` — append:

```
- [AINews — Claude Haiku 5.5 launch and Artificial Analysis evals](../sources/newsletters/ainews-claude-haiku-5-5-2026-10-08.md)
```

### wiki/state-of/models.md (updated)

Haiku 5.5 line under "Small / fast models":

```
- [Claude Haiku 5.5](../models/claude-haiku-5-5.md) — Anthropic, launched 2026-10-07; cheapest/fastest Claude tier at GPT-6 Luna's price; AA Intelligence Index 43 (Luna 38), OSWorld 2.1 72.4%; heavy token use can make it costlier per task than Haiku 4.5; aimed at subagent, compaction, and high-volume work *(as of 2026-10-10)*
```

Sonnet 5.5 line under "Frontier models": only its trailing stamp changes, to `*(as of 2026-10-07)*`.

`## Recent changes` — the live Haiku launch entry is re-dated and moved below the other 2026-10-19 entries (text unchanged):

```
- [2026-10-07] Claude Haiku 5.5 launched; new Small / fast models section. About 75% cheaper than Haiku 4.5, OSWorld 2.1 72.4% and Terminal-Bench 4.0 39.2% (Sonnet 5.5: 83.9% / 70.6%), first Haiku with an effort setting.
```

### wiki/index.md (updated)

```
- [models/claude-haiku-5-5](models/claude-haiku-5-5.md) — Anthropic's cheapest/fastest small model (launched 2026-10-07); ~75% cheaper per token than Haiku 4.5 but heavy token use per task; AA Intelligence Index 43, ahead of GPT-6 Luna; for subagent, compaction and high-volume work *(as_of: 2026-10-10)*
```

Sonnet 5.5 line: only its trailing stamp changes, to `*(as_of: 2026-10-07)*`.

### wiki/sources/articles/claude-haiku-5-5-launch-2026-10-19.md (updated)

Frontmatter gains `published: 2026-10-07` (after `url:`). In the summary paragraph, replace "The page carries no publication date; the fetch date (2026-10-19) is used." with:

```
The page itself carries no date; AINews launch coverage (covering 6–7 October, with no mention in the previous day's issue) dates the release to 2026-10-07.
```

### wiki/sources/newsletters/ainews-claude-haiku-5-5-2026-10-08.md (new)

```
---
title: 'AINews — Claude Haiku 5.5: better than GPT-6 Luna at the same pricing'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-ainews-claude-haiku-55-better-than-gpt-6-luna.md
url: https://www.latent.space/p/ainews-claude-haiku-55-better-than
published: 2026-10-08
ingested: 2026-10-20
domains: [models]
---

# AINews — Claude Haiku 5.5: better than GPT-6 Luna at the same pricing

The 2026-10-08 issue (covering 6–7 October) leads with the Claude Haiku 5.5 launch: pricing matched to GPT-6 Luna, same-day Sonnet 5.5 cache-read cut and subscriber API credits, partner rollouts, and a detailed Artificial Analysis evaluation with token-use caveats.

## Influenced pages
- [Claude Haiku 5.5](../../models/claude-haiku-5-5.md) — launch date, independent evals, token use
- [Claude Sonnet 5.5](../../models/claude-sonnet-5-5.md) — cache-read cut dated to the Haiku launch
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — per-task cost caveat
- [State of Models](../../state-of/models.md) — Haiku line

## Key claims extracted
- Haiku 5.5 shipped 6–7 October at $0.10/$0.50 per 1M tokens under 100k-token prompts, matching GPT-6 Luna; Sonnet 5.5 cache reads halved the same day
- AA Intelligence Index 43 at max effort; GLM-5.3 Flash 42, Gemini 3.8 Flash 41, GPT-6 Luna 38; Sonnet 5.5 56
- ~162k output tokens per AA index task at max effort, ~3x Luna; xhigh→max adds 2 points for ~1.8x tokens
- Terminal-Bench 4.0 33% (AA) vs Anthropic's 39.2%
- AA-Omniscience: 36% accuracy, 40% hallucination (Luna 44% / 77%)
- AutomationBench-AA 35%, depressed by a pre-release over-refusal bug; AA will re-run
- 1M-token context, up from 200k
```

### wiki/sources/newsletters/ainews-haiku-5-5-vals-cost-per-test-2026-10-08.md (new)

```
---
title: AINews — Haiku 5.5 on Vals and Arena
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
published: 2026-10-08
ingested: 2026-10-20
domains: [models]
---

# AINews — Haiku 5.5 on Vals and Arena

A block of Claude Haiku 5.5 results in the 2026-10-08 "not much happened today" issue. This page covers the Haiku 5.5 items only.

## Influenced pages
- [Claude Haiku 5.5](../../models/claude-haiku-5-5.md) — Vals cost per test, Vibe Code Bench, Arena WebDev
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — per-task cost caveat

## Key claims extracted
- Vals: heavy reasoning (59 vs 17 steps on Legal Research) makes it cost more per test than Haiku 4.5 on every shared benchmark
- Vals: 90.4% on Vibe Code Bench (#3); 54.3% on the Vals Index (#16)
- Price rises 5x beyond 100k tokens of context
- Code Arena WebDev 1587, +257 over Haiku 4.5
```

### wiki/sources/newsletters/ainews-haiku-5-5-arena-webdev-2026-10-10.md (new)

```
---
title: AINews — Haiku 5.5 Arena WebDev rank
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-10-ainews-typesafejev-at-100m-arr-75b-valuati.md
published: 2026-10-10
ingested: 2026-10-20
domains: [models]
---

# AINews — Haiku 5.5 Arena WebDev rank

A one-line Arena roundup item in the 2026-10-10 issue (headlined on TypeSafe/Jev). This page covers the Haiku 5.5 item only.

## Influenced pages
- [Claude Haiku 5.5](../../models/claude-haiku-5-5.md) — Arena WebDev rank vs GPT-6 Luna

## Key claims extracted
- Haiku 5.5 ranks #30 on Arena WebDev at $0.10/$0.50, matching GPT-6 Luna's price and scoring 6 points higher
```

## Schema / vocabulary additions

None.

## Open questions

None.
