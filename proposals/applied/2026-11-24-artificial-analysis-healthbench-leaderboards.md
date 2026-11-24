---
type: proposal
source: raw/articles/2026-11-24-artificialanalysisai-evaluations-healthbench.md
sources:
  - raw/articles/2026-11-24-artificialanalysisai-evaluations-healthbench.md
  - raw/articles/2026-11-24-artificialanalysisai-evaluations-healthbench-general.md
  - raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
status: pending
created: 2026-11-24
---

# Proposal: Artificial Analysis HealthBench leaderboards

## Summary

### In short
On medical-conversation benchmarks, how long an answer is allowed to be changes who wins: Claude Opus 5.5 had the top raw clinician score at 71.4% and drops to 59.9% once long answers are penalised. Artificial Analysis now runs independent HealthBench leaderboards, where Claude Sonnet 5.5 leads the general set (62.1%), Claude Fable 5.2 leads the clinician set (68.1%), and DeepSeek V4.1 Flash nearly matches Sonnet at a sixteenth of the cost. The proposal creates a HealthBench benchmark page and gives State of Healthcare its first medical-benchmark line. One reason to hesitate: the leaderboard carries no publication date, so the leader set is dated to today's fetch.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
HealthBench is OpenAI's benchmark of medical conversations. Each conversation comes with a rubric written by physicians, and a judge model checks the model's final reply against it, criterion by criterion; criteria can add or subtract up to ten points, so a bad reply can score below zero. There are two sets: 5,000 general health conversations, ranging from emergency referrals to global health, and HealthBench Professional, 525 conversations with clinicians covering consults, writing and research, including red-teaming and deliberately hard cases.

On 21 October Artificial Analysis started running both sets itself, four repeats per task, with the same OpenAI judge the original implementation uses. Its distinctive choice is to report two numbers per model: the raw score and a length-adjusted score that docks replies longer than 2,000 characters and rewards shorter ones. AINews, covering the launch, put the point bluntly: answer length is a ranking choice, not a cosmetic detail. Opus 5.5 had the best raw Professional score and fell well down the table after adjustment, and on the general set the model with the shortest answers led on communication quality while scoring lowest on completeness.

The leaderboard as read today has moved since launch. Sonnet 5.5 still leads the general set, with DeepSeek V4.1 Flash second at 60.9% for $0.005 a task against Sonnet's $0.08, and Fable 5.2 third. On the clinician set, Fable 5.2 has since taken the length-adjusted lead at 68.1%. GPT-6.2 Astra appears only on the general set, at 53.5%.

### What changes
The wiki has no medical benchmark today; State of Healthcare lists tools, one specialised model and use cases, but nothing that compares general models on medical answers.

- New page `benchmarks/healthbench.md`: what the two sets are, how scoring and the length adjustment work, current results for both sets, and the launch-time Opus example of the length effect. Results that belong to models the wiki has since replaced (GPT-6 Astra, GPT-6.1 Sol) are left out.
- **State of Healthcare** gains a "Medical-knowledge benchmarks" subcategory with one HealthBench line naming both leaders and the DeepSeek cost point, plus one Recent-changes entry dated 24 November (nine entries, under the cap). Page date moves to 24 November.
- **Index** gains the new benchmark page; the benchmark count moves from 13 to 14.
- Two source pages: one for the Artificial Analysis leaderboard (both tabs) and one story page for the AINews launch item.

### What to weigh
The triage asked only for a state-of line; the proposal goes further, creating a benchmark page and a new state-of subcategory, because the scoring method and two leader sets need more room than one dashboard bullet. The leaderboard is a live page with no publication date, so the current results are dated 24 November, the day it was read; the launch facts (Opus 5.5's raw-versus-adjusted drop, the communication-versus-completeness pattern) keep their 21 October date. Only the length-adjusted rankings and the headline figures were captured; per-theme breakdowns sit in charts that did not render as text.

## Intended changes

- [ ] **Create** `wiki/benchmarks/healthbench.md` — new benchmark page
- [ ] **Update** `wiki/state-of/healthcare.md` — new "Medical-knowledge benchmarks" subcategory with one line; adds one Recent-changes entry dated 2026-11-24 (nine entries, no spill); adds two source ids and two Sources links; `as_of` 2026-10-19 → 2026-11-24
- [ ] **Update** `wiki/index.md` — add `benchmarks/healthbench` under Benchmarks; benchmarks count 13 → 14
- [ ] **Create** `wiki/sources/articles/artificial-analysis-healthbench-2026-11.md` — source summary for the leaderboard page
- [ ] **Create** `wiki/sources/newsletters/ainews-healthbench-leaderboards-2026-10-21.md` — story source page for the AINews launch item

## Page drafts

### wiki/benchmarks/healthbench.md (new)

```
---
title: HealthBench
type: benchmark
domains: [healthcare]
tags: [openai]
as_of: 2026-11-24
sources: [artificial-analysis-healthbench-2026-11, ainews-healthbench-leaderboards-2026-10-21]
---

# HealthBench

OpenAI's benchmark of medical conversations, graded against rubrics written by physicians. It has two sets: **HealthBench**, 5,000 general health conversations from emergency referrals to global health, and **HealthBench Professional**, 525 clinician conversations across consult, writing and research tasks, including red-teaming and hard cases. Artificial Analysis has run independent leaderboards for both since 2026-10-21.

## How it is scored

- Each rubric criterion is worth −10 to +10 points. A judge model (GPT-5.4 low, as in OpenAI's implementation) checks which criteria the reply meets; a task scores the points earned over the positive points available, so it can fall below zero. Artificial Analysis runs four repeats per task.
- Artificial Analysis reports a raw score and a length-adjusted score. The adjustment lowers the score of replies longer than 2,000 characters and raises shorter ones; reasoning tokens do not count toward length. Cite which score you mean: the adjustment reorders the top of the table.

## Current results (as of 2026-11-24)

- **HealthBench, length-adjusted:** [Claude Sonnet 5.5](../models/claude-sonnet-5-5.md) 62.1%, [DeepSeek V4.1 Flash](../models/deepseek-v4-1-flash.md) 60.9%, Claude Fable 5.2 59.6%. [GPT-6.2 Astra](../models/gpt-6-2-astra.md) scores 53.5%.
- **Cost (launch figures, 2026-10-21):** DeepSeek V4.1 Flash reached its score at $0.005 per task, against $0.08 for Sonnet 5.5.
- **HealthBench Professional, length-adjusted:** Claude Fable 5.2 leads at 68.1% at xhigh effort (67.7% at max). Among models current in this wiki it is followed by Sonnet 5.5 (63.0%) and [GPT-6 Luna](../models/gpt-6-luna.md) (61.9%, the cheapest run at $0.0041 per task); results for models the wiki has since replaced are omitted. GPT-6.2 Astra has not been run on this set.
- **Length effect:** at launch, [Claude Opus 5.5](../models/claude-opus-5-5.md) had the highest raw Professional score (71.4%) but fell to 59.9% after adjustment. On the general set, the model with the shortest answers led on communication quality while scoring lowest on completeness.

## Why it matters

It is the wiki's first head-to-head medical leaderboard for general models. The spread between raw and length-adjusted scores shows that "best medical model" depends on whether long, exhaustive answers are rewarded, which is a product choice as much as a capability result.

## Recent changes

- [2026-11-24] Page created. Claude Fable 5.2 now leads HealthBench Professional (length-adjusted); Sonnet 5.5 still leads the general set.
- [2026-10-21] Artificial Analysis launched independent HealthBench and HealthBench Professional leaderboards with raw and length-adjusted scores.

## Sources

- [Artificial Analysis — HealthBench leaderboards](../sources/articles/artificial-analysis-healthbench-2026-11.md)
- [AINews — HealthBench leaderboards launch (Oct 21)](../sources/newsletters/ainews-healthbench-leaderboards-2026-10-21.md)
```

### wiki/state-of/healthcare.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-11-24
sources: [... existing ids ..., artificial-analysis-healthbench-2026-11, ainews-healthbench-leaderboards-2026-10-21]
```

New subcategory, inserted after `### Domain-specialized models` and before `### Document intelligence`:

```
### Medical-knowledge benchmarks

- [HealthBench](../benchmarks/healthbench.md) — OpenAI's physician-graded medical-conversation benchmark, run independently by Artificial Analysis; length-adjusted leaders are Claude Sonnet 5.5 on the general set (62.1%) and Claude Fable 5.2 on the clinician set (68.1%); DeepSeek V4.1 Flash is close on the general set at a sixteenth of the cost *(as of 2026-11-24)*
```

`## Recent changes` — adds one entry at the top (nine entries, no spill):

```
- [2026-11-24] Added HealthBench, the first medical-knowledge benchmark on the dashboard: Sonnet 5.5 leads the general set and Fable 5.2 the clinician set on Artificial Analysis' length-adjusted scores, and the length adjustment alone moves Opus 5.5 from first to mid-table.
```

`## Sources` — appends two links:

```
- [Artificial Analysis — HealthBench leaderboards](../sources/articles/artificial-analysis-healthbench-2026-11.md)
- [AINews — HealthBench leaderboards launch (Oct 21)](../sources/newsletters/ainews-healthbench-leaderboards-2026-10-21.md)
```

### wiki/index.md (updated)

Under `## Benchmarks`, add:

```
- [benchmarks/healthbench](benchmarks/healthbench.md) — OpenAI's physician-graded medical-conversation benchmark (5,000 general + 525 clinician conversations); Artificial Analysis leaderboards with raw and length-adjusted scores; Sonnet 5.5 and Fable 5.2 lead *(as_of: 2026-11-24)*
```

Update the State of Healthcare line's date to `*(as_of: 2026-11-24)*`, and in `## Page count` change `- benchmarks: 13` → `- benchmarks: 14`.

### wiki/sources/articles/artificial-analysis-healthbench-2026-11.md (new)

```
---
title: "Artificial Analysis — HealthBench and HealthBench Professional leaderboards"
type: source
source_type: article
source_file: raw/articles/2026-11-24-artificialanalysisai-evaluations-healthbench.md
url: https://artificialanalysis.ai/evaluations/healthbench
ingested: 2026-11-24
domains: [healthcare]
---

# Artificial Analysis — HealthBench and HealthBench Professional leaderboards

Artificial Analysis' independent leaderboards for OpenAI's HealthBench (5,000 general health conversations) and HealthBench Professional (525 clinician conversations), graded against physician-written rubrics with OpenAI's judge model. Each model gets a raw and a length-adjusted score. The page has no publication date; it was read on 2026-11-24. The Professional tab is in the raw file above; the general-set tab was captured separately at `raw/articles/2026-11-24-artificialanalysisai-evaluations-healthbench-general.md`.

## Influenced pages

- [HealthBench](../../benchmarks/healthbench.md) — new page: scoring method, current results for both sets
- [State of Healthcare](../../state-of/healthcare.md) — new Medical-knowledge benchmarks subcategory

## Key claims extracted

- Rubric criteria worth −10 to +10 points; judge GPT-5.4 (low), as in OpenAI's implementation; four repeats per task
- Length adjustment penalises replies over 2,000 characters and raises shorter ones; reasoning excluded from length
- HealthBench (length-adjusted): Claude Sonnet 5.5 62.1%, DeepSeek V4.1 Flash 60.9%, Claude Fable 5.2 59.6%, GPT-6.2 Astra 53.5%
- Headline: Claude Fable 5.2 (xhigh) scores highest on HealthBench Professional at 68.1%
- HealthBench Professional (length-adjusted, max-effort rows): Claude Fable 5.2 67.7%, Claude Sonnet 5.5 63.0%, GPT-6 Luna 61.9%, Claude Opus 5.5 59.9%
- Cheapest Professional run: GPT-6 Luna at $0.0041 per task
```

### wiki/sources/newsletters/ainews-healthbench-leaderboards-2026-10-21.md (new)

```
---
title: "AINews — Artificial Analysis HealthBench leaderboards launch (Oct 21)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
published: 2026-10-21
ingested: 2026-11-24
domains: [healthcare]
---

# AINews — Artificial Analysis HealthBench leaderboards launch (Oct 21)

The "Independent Evaluations" item in the 21 October AINews issue on Artificial Analysis' new HealthBench leaderboards, framed as evidence that answer length is a material ranking choice.

## Influenced pages

- [HealthBench](../../benchmarks/healthbench.md) — launch date, the Opus 5.5 length effect, the communication-versus-completeness pattern, cost comparison

## Key claims extracted

- Leaderboards for 5,000 general and 525 clinician conversations, graded with OpenAI models
- Claude Opus 5.5: highest raw Professional score (71.4%), 59.9% after length adjustment
- On general HealthBench, the shortest-answer model leads communication quality but scores lowest on completeness
- DeepSeek V4.1 Flash 60.9% at $0.005/task vs Claude Sonnet 5.5 62.1% at $0.08/task
```

## Schema / vocabulary additions

None.

## Open questions

None.
