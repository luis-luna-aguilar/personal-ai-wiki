---
type: proposal
sources:
  - raw/newsletters/2026-07-13-apple-just-sued-openai.md
  - raw/newsletters/2026-07-14-ainews-codex-usage-up-10x-in-6-months-to-7m-use.md
status: pending
created: 2026-09-06
---

# Proposal: the router isn't the moat — your eval data is

## Summary

### The source

With five new frontier models shipping in a single month, model selection has become its own engineering problem, and two sources converge on the same conclusion from different angles. The Code profiles the router landscape: Cognition's Devin Fusion switches models mid-task to cut cost (Cognition's own benchmark claims a 35% reduction while holding coding performance); Not Diamond trains custom routers from a customer's own uploaded, scored eval data, and that same technology powers OpenRouter's "Auto" mode. The argument: routing itself is now a commodity — OpenRouter sells one, Azure includes one, GitHub is full of them — but none of them can supply what actually makes a router good, which is eval data that defines "good" for a specific workload. Separately, AINews reports a concrete instance of the mechanism working: Devin Fusion, now running on Fable 5, can beat Opus 4.8 on cost per task not because Fable is cheaper, but because better delegation and judgment mean the model wastes fewer actions — in 81% of sampled Fable-led runs, the lead model never makes a single code edit itself, delegating the mechanical work entirely.

### What changes

- **Cost-aware AI task routing** gains a new "Evidence from practice" bullet on the eval-data-as-moat argument (Devin Fusion, Not Diamond, OpenRouter Auto) — a further concrete example of the page's "route by uncertainty, not only by task size" and expert-data-beats-generic-defaults guidance, now generalized from one company's internal data (the existing Bridgewater bullet) to a market-wide observation that routing is commoditizing while eval data isn't. Page date moves to 14 July.
- **Devin** gets its existing Devin Fusion entry extended with the new mechanism detail — the 81%-no-edit statistic explains *why* Fusion beats Opus 4.8 on cost, which the page's current text doesn't yet cover (it has the cost-reduction percentages but not this specific delegation mechanism). New Recent-changes entry.

### What to weigh

The 81%-no-edit statistic and the Terra-Max-vs-Fable-5-Max cost/score comparison both trace back to one AINews-relayed source (a coding-agent index explorer built by an individual, "skirano," not an institutional benchmark) — attributed as such rather than stated as an independently verified result. The Devin Fusion cost-reduction figures themselves are unchanged from what's already on `tools/devin.md` (sourced to Cognition's own blog); this proposal only adds the new delegation-mechanism explanation.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add a new "Evidence from practice" bullet on eval-data-as-moat (Devin Fusion, Not Diamond, OpenRouter Auto); bump `as_of`; add new source
    > See draft below

- [x] **Update** `wiki/tools/devin.md` — extend the Devin Fusion status bullet with the 81%-no-edit delegation-efficiency mechanism; add one Recent-changes entry; add new source
    > See draft below

- [x] **Create** `wiki/sources/newsletters/the-code-eval-data-moat-2026-07-13.md` — source summary (scoped to the router/eval-data item only; this issue's main story — the Apple/OpenAI lawsuit — is a separate signal, recommended skip, not actioned here)

- [x] **Create** `wiki/sources/newsletters/ainews-devin-fusion-router-moat-2026-07-14.md` — source summary (scoped to the Devin Fusion/Arena/cost-per-task item only; this issue's main story — Codex's 10x usage growth — is a separate signal not actioned here)

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter — bump `as_of` and add sources:

```yaml
as_of: 2026-07-14
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07, the-code-eval-data-moat-2026-07-13, ainews-devin-fusion-router-moat-2026-07-14]
```

Add to `## Evidence from practice` (new bullet, appended):

```md
- **Eval data, not the router, is the moat.** With several frontier models shipping in the same month, picking the right one for a task has become its own problem, and routing itself has commoditized — OpenRouter, Azure, and generic open-source routers all offer one. What none of them supply is the eval data that tells a router what "good" looks like for a specific workload: Not Diamond trains custom routers from a customer's own uploaded, scored examples, and the same approach powers OpenRouter's "Auto" mode. Cognition's Devin Fusion is a concrete instance of the mechanism working: running on Fable 5, it can beat Opus 4.8 on cost per task not because Fable is cheaper, but because stronger delegation and judgment mean fewer wasted actions — in 81% of sampled Fable-led runs, the lead model never makes a code edit itself (per AINews, relaying an independent coding-agent index analysis).
```

### wiki/tools/devin.md (updated)

Frontmatter — bump `as_of` and add source:

```yaml
as_of: 2026-07-14
sources: [devin-auto-triage-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, cognitioncom-blog-ai-productivity, the-code-spacexai-drops-grok-45-2026-07-09, ainews-devin-fusion-router-moat-2026-07-14]
```

`## Current status` — extend the existing Devin Fusion bullet:

> **Before:** `- **Devin Fusion (preview):** applies the [sidekick multi-model harness pattern](../workflows/agentic-orchestration-patterns.md) — a frontier model and a cheaper model run as two persistent, separately-cached agents, with the frontier model planning and reviewing while the sidekick handles mechanical work.`
>
> **After:** `- **Devin Fusion (preview):** applies the [sidekick multi-model harness pattern](../workflows/agentic-orchestration-patterns.md) — a frontier model and a cheaper model run as two persistent, separately-cached agents, with the frontier model planning and reviewing while the sidekick handles mechanical work. Running on Fable 5, Fusion can beat Opus 4.8 on cost per task not because Fable is cheaper per token, but because stronger delegation and judgment waste fewer actions: per an independent coding-agent index analysis relayed by AINews, in 81% of sampled Fable-led runs the lead model never makes a code edit itself.`

`## Recent changes` (new entry, inserted in date order — after the existing `[2026-07-14]` entries, since this is same-day evidence about the already-documented Fusion feature rather than a new capability):

```md
- [2026-07-14] Added the delegation-efficiency mechanism behind Devin Fusion's cost advantage on Fable 5: in 81% of sampled Fable-led runs, the lead model never edits code itself (per AINews, relaying an independent coding-agent index analysis).
```

### wiki/sources/newsletters/the-code-eval-data-moat-2026-07-13.md (new)

```md
---
title: "The Code — Everyone is building AI model routers; the real asset is your eval data"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-13-apple-just-sued-openai.md
url: https://codenewsletter.ai/p/openai-s-gpt-5-6-sol-wins-over-developers-cursor-drops-side-chat
published: 2026-07-13
ingested: 2026-09-06
domains: [training, agents]
---

# The Code — Everyone is building AI model routers; the real asset is your eval data

The Code's July 13 "Insight" section argues that with five new frontier models launching in a month, model routing has become both necessary and commoditized — the differentiator is a team's own eval data, not the router itself. This source page covers only that item; the issue's main story (Apple's lawsuit against OpenAI) is a separate, unrelated signal, recommended skip, not actioned here.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — added the eval-data-as-moat evidence bullet

## Key claims extracted

- Cognition's Devin Fusion switches models mid-task; Cognition's own benchmark claims it holds top-tier coding performance while cutting cost by 35%
- Not Diamond trains custom routers from a customer's own uploaded eval data (real prompts plus scored answers); this technology powers OpenRouter's "Auto" mode
- The argument: routing is now a commodity (OpenRouter, Azure, generic open-source routers all offer one); the durable asset is the eval data that defines "good" for a specific workload, since models themselves become commodities weekly
- Recommended starting point cited: Hamel Husain's guide to evals (hamel.dev/blog/posts/evals/)
```

### wiki/sources/newsletters/ainews-devin-fusion-router-moat-2026-07-14.md (new)

```md
---
title: "AINews — Coding-agent cost/perf tradeoffs: Terra Max, Devin Fusion, and Fable-led delegation"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-14-ainews-codex-usage-up-10x-in-6-months-to-7m-use.md
url: https://www.latent.space/p/ainews-codex-usage-up-10x-in-6-months
published: 2026-07-14
ingested: 2026-09-06
domains: [training, agents, coding]
---

# AINews — Coding-agent cost/perf tradeoffs: Terra Max, Devin Fusion, and Fable-led delegation

AINews' July 14 issue includes a "Coding Agents, Harness Design, and Cost-Per-Task Competition" section reporting that benchmarks are shifting from token price to cost per task. This source page covers only that section; the issue's main story (Codex's reported 10x usage growth in six months) is a separate signal not actioned here.

## Influenced pages

- [Devin](../../tools/devin.md) — added the delegation-efficiency mechanism (81% no-edit statistic) behind Devin Fusion's cost advantage on Fable 5
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — added as corroborating detail in the eval-data-as-moat evidence bullet

## Key claims extracted

- skirano built a coding-agent index explorer and found Terra Max slightly ahead of Fable 5 Max on score for materially lower cost
- Cognition reported that Devin Fusion now uses Fable 5, and that it can be lower cost per task than Opus 4.8 because stronger delegation and judgment reduce unnecessary work
- imjaredz highlighted the key stat: in 81% of Fable-led runs, the lead model never makes a code edit, implying expensive models can be cheaper when they avoid wasted actions
- Separately in the same section: harnesses are increasingly described as "the app" (threepointone), LangChain argues task-specialized harnesses beat generic wrappers, and Artificial Analysis emphasizes cost-per-task over token pricing as the more meaningful long-horizon metric
