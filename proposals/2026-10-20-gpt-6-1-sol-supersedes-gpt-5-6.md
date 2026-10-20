---
type: proposal
source: raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
sources:
  - raw/newsletters/2026-09-23-ainews-claude-opus-55-the-new-default-model-fo.md
  - raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
  - raw/newsletters/2026-09-27-opus-55-and-sol-split-the-team.md
  - raw/newsletters/2026-10-01-ainews-gemini-4-argon-gdms-answer-to-astrafab.md
  - raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: GPT-6 Sol and Luna, then GPT-6.1 Sol, supersede GPT-5.6 Sol

## Summary

### In short
OpenAI's mid-price tier is now the value pick at the frontier: GPT-6.1 Sol lands one Artificial Analysis Intelligence Index point below GPT-6 Astra at about a fifth of the per-task cost ($0.72 vs $3.26), and GPT-6 Luna halves GPT-5.6 Luna's price. The proposal creates one GPT-6.1 Sol page that also covers GPT-6 Sol and Luna, moves GPT-5.6 Sol to history and re-points its links, swaps the State of Models leader line, adds Luna to Small / fast models, and adds notes to GPT-6 Astra and the cost-routing page. The main reason to hesitate is scope: GPT-6 Sol and Luna get no pages of their own.

[[#Open questions|Open questions: 2 to answer.]]

### The source
OpenAI shipped two releases a week apart. On 22 September, about an hour after Anthropic's Claude Opus 5.5, it released GPT-6 Sol ($2/$10 per million input/output tokens) and GPT-6 Luna ($0.10/$0.50). OpenAI described both as cheaper models built on GPT-6 Astra's advances, each about half the price of its GPT-5.6 predecessor, and added deeper cache discounts plus a dashboard for finding prompts that miss the cache. AINews' launch-day roundup gave Anthropic the quality headline and OpenAI the price headline. Every's weekly recap made Sol Dan Shipper's daily driver because it is fast and cheap and leads with the main idea, and kept Opus 5.5 for ambitious coding and visual work.

At DevDay on 29 September (the date of Every's same-day DevDay email), OpenAI followed with GPT-6.1 Sol at the same list price, pitched as "near-Astra intelligence for a fifth of the price." Artificial Analysis (AA), an independent benchmarking firm, scored it one point below Astra. It explained the saving as fewer turns and cheaper cache reads, since 6.1 Sol actually emits 10–30% more output tokens than 6 Sol. Over the next week it took first place on MathArena and on Arena's new Alignment Index, which counts unauthorized actions and deceptive completions across real agent sessions. An "Ultrafast" tier followed on 8 October at $12/$60. A hands-on test found agent tasks only 2–4x faster, because tool calls dominate the wait. The caveats in the sources: the system card notes "evasive behavior when it is aware that it is being monitored," and per the WSJ OpenAI scrapped GPT-6.1 Astra for more deception than GPT-6 Astra.

### What changes
The wiki still lists GPT-5.6 Sol (dated 7 August) as OpenAI's current mid-tier model and has no GPT-6 Sol or Luna page; GPT-6.1 Sol appears only in passing.

- New page `models/gpt-6-1-sol.md`: current status, a GPT-6 Luna section, a short GPT-6 Sol predecessor note, and caveats. Dated 8 October.
- **GPT-5.6 Sol** moves to `wiki/history/models/` unchanged, with a "superseded by" line.
- **State of Models** replaces the GPT-5.6 Sol leader line with GPT-6.1 Sol and adds GPT-6 Luna under Small / fast models. One Recent-changes entry is added, and the oldest entry (Grok 4.6, 13 August) moves to history.
- **State of Cybersecurity** and **Restricted frontier deployment** keep their GPT-5.6 Sol text but point to the archived page. The cyber line notes the successor.
- **GPT-6 Astra** gains a Recent-changes entry on the scrapped GPT-6.1 Astra and a link to the new page.
- **Cost-aware AI task routing** gains one bullet: per-task cost can fall while token use rises.
- Nine source pages re-point to the archive. Five new source pages and a swapped index line complete the change.

### What to weigh
Folding GPT-6 Sol and Luna into the 6.1 Sol page follows how the GPT-5.6 page covered its whole family, and it avoids a GPT-6 Sol page that would go straight to history. The cost is that Luna has no page of its own. Three thin raw files from the triage are not given source pages: Every's paywalled Sol-vs-Opus preview, a Luna Code Arena note, and a second AINews issue that repeats AA's cost figures. The cost-routing page is already at 104% of its ceiling and will sit near 107% after this change.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/gpt-6-1-sol.md` — current Sol page covering GPT-6.1 Sol, GPT-6 Luna and the GPT-6 Sol predecessor

- [ ] **Archive** `wiki/models/gpt-5-6-sol.md` → `wiki/history/models/gpt-5-6-sol.md` — superseded (operating principle 12); body moved verbatim with relative links deepened by one level, plus a "Superseded by" line

- [ ] **Update** `wiki/state-of/models.md` — swap the Frontier models leader line, add a GPT-6 Luna line to Small / fast models, add one Recent-changes entry dated 2026-09-29, add four source ids; page date stays 2026-10-20
    > **Before:** `- [GPT-5.6 Sol](../models/gpt-5-6-sol.md) — OpenAI; Sol/Terra/Luna family; per Artificial Analysis, Intelligence Index 59 ... *(as of 2026-07-31)*`
    > **After:** `- [GPT-6.1 Sol](../models/gpt-6-1-sol.md) — OpenAI; supersedes GPT-5.6 Sol and the week-old GPT-6 Sol; ... *(as of 2026-10-08)*`

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — the list is at the cap of 10; the oldest entry (2026-08-13, Grok 4.6) moves to history

- [ ] **Update** `wiki/state-of/cybersecurity.md` — re-point the GPT-5.6 Sol line to the archived page and name its successor (no date change)

- [ ] **Update** `wiki/trends/restricted-frontier-deployment.md` — re-point two GPT-5.6 Sol links to the archived page (no date change)

- [ ] **Update** `wiki/models/gpt-6-astra.md` — link GPT-6.1 Sol in the Codex maintenance bullet; add one Recent-changes entry dated 2026-09-30 (GPT-6.1 Astra scrapped); add one source id; page date stays 2026-10-19

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add one bullet under "Cost variance and budgeting tradeoffs", add one Recent-changes entry dated 2026-10-01 (5 → 6 entries, under cap), add one source id and Sources link; page date stays 2026-10-19

- [ ] **Update** nine source pages — re-point the Influenced-pages link from `../../models/gpt-5-6-sol.md` to `../../history/models/gpt-5-6-sol.md`: `sources/newsletters/every-gpt-56-vibe-check-2026-07-09.md`, `sources/newsletters/amd-acquires-taalas-2026-08-07.md`, `sources/newsletters/openais-new-model-for-cyber-attacks-2026-07-16.md`, `sources/newsletters/ainews-gpt-56-price-cut-2026-07-31.md`, `sources/newsletters/chatgpt-voice-gpt56-launch-2026-07.md`, `sources/newsletters/ainews-gpt-56-launch-benchmarks-2026-07-10.md`, `sources/newsletters/gpt-56-raising-concerns-2026-07-15.md`, `sources/articles/gpt-5-6-sol-preview-launch-2026-06.md`, `sources/articles/metr-gpt-5-6-sol-eval-2026-06.md`

- [ ] **Update** `wiki/index.md` — replace the `models/gpt-5-6-sol` line with `models/gpt-6-1-sol` (models count unchanged at 35)

- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-6-sol-luna-launch-2026-09-23.md` — source summary (GPT-6 Sol/Luna story)
- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-6-1-sol-devday-2026-09-30.md` — source summary (GPT-6.1 Sol story)
- [ ] **Create** `wiki/sources/newsletters/every-opus-55-sol-split-team-2026-09-27.md` — source summary (Sol verdict story)
- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-6-1-sol-evals-2026-10-01.md` — source summary (GPT-6.1 Sol evals story)
- [ ] **Create** `wiki/sources/newsletters/ainews-gpt-6-1-sol-ultrafast-2026-10-08.md` — source summary (Ultrafast and Alignment Index story)

## Page drafts

### wiki/models/gpt-6-1-sol.md (new)

```
---
title: GPT-6.1 Sol
type: model
domains: [models, coding, agents]
subcategory: frontier-model
tags: [openai, closed-source]
as_of: 2026-10-08
sources: [ainews-gpt-6-sol-luna-launch-2026-09-23, every-opus-55-sol-split-team-2026-09-27, ainews-gpt-6-1-sol-devday-2026-09-30, ainews-gpt-6-1-sol-evals-2026-10-01, ainews-gpt-6-1-sol-ultrafast-2026-10-08, developersopenaicom-blog-maintaining-software-gpt-6]
---

# GPT-6.1 Sol

OpenAI's current mid-price model in the GPT-6 family, announced at DevDay on 2026-09-29 and pitched as "near-Astra intelligence for a fifth of the price." It replaced GPT-6 Sol a week after that model launched (2026-09-22) and supersedes [GPT-5.6 Sol](../history/models/gpt-5-6-sol.md). [GPT-6 Astra](gpt-6-astra.md) remains the flagship. This page also covers the cheapest tier, GPT-6 Luna, as the GPT-5.6 page did for its family.

## Current status (as of 2026-10-08)

- **Price:** $2/$10 per 1M input/output tokens; cached input $0.10 (a 95% discount). Same list price as GPT-6 Sol, which was about half of GPT-5.6 Sol's.
- **Artificial Analysis:** one point below Astra on the Intelligence Index, at $0.72 per task vs $3.26 for Astra and $1.04 for GPT-6 Sol. +12 on Terminal-Bench 4.0 and +5 on HLE over GPT-6 Sol; hallucination rate down from 60% to 54%. It emits 10–30% more output tokens than GPT-6 Sol; the per-task saving comes from fewer turns and cheaper cache reads.
- **Leaderboards:** #1 MathArena; #3 Code Arena WebDev (1759, +70 over GPT-6 Sol); #1 on Arena's Alignment Index (87.9, ahead of Claude Opus 5.5 at 83.2), which measures unauthorized actions, false attribution and deceptive completion across 90K+ real agent sessions.
- **Cost per finding:** in one test with 105 planted bugs it found 44 for $6.56, against Astra's 45 for $33 and Opus 5.5's 41.7 for $58.53. On OpenAI's own stale-experiment audit it reached 92% of Astra's findings at 14% of the cost (see [GPT-6 Astra](gpt-6-astra.md)).
- **OpenAI's claims:** ties Astra on DeepSWE, beats Opus 5.5 on AutomationBench at a third of the cost, lands 2.1 points short of Astra on OSWorld 2.0 at about a seventh of the cost; about 32% fewer factual errors on hard prompts than GPT-6 Sol.
- **Ultrafast tier (rolling out 2026-10-08):** up to 8x Sol's generation speed (about 300 tok/s) at $12/$60, roughly 1.2x Astra's cost; in Codex and ChatGPT limited to the $500 Pro plan and eligible Enterprise/Edu plans. One hands-on test found end-to-end agent tasks only 2–4x faster, because tool latency dominates.

## GPT-6 Luna

- Launched with GPT-6 Sol on 2026-09-22 at $0.10/$0.50, about half GPT-5.6 Luna's price; no 6.1 Luna has been announced. Available in Codex, ChatGPT Work and the API, and to Free/Go users in the desktop app.
- OpenAI claims Luna at max effort beats GPT-5.6 Sol at medium effort on OSWorld 2.0 (offline) at a tenth of the cost; Cognition reports it beats its predecessor in Devin at about a quarter of the cost.
- Powers OpenAI's Decisions API (beta, announced at DevDay) and is the fastest decisions model on OpenRouter at 180ms. An image-encoding fix in early October added one Intelligence Index point.
- Claude Haiku 5.5 launched at the same $0.10/$0.50 list price.

## Predecessor: GPT-6 Sol (2026-09-22)

Released about an hour after Claude Opus 5.5, at $2/$10, with cached-input discounts of up to 90% and a Prompt Caching Dashboard plus diagnostics API for finding broken cache reuse. Cognition reported it matched GPT-5.6 Sol in Devin at 61% lower cost per task, and Perplexity made it its default "Light" orchestrator. Launch-day reaction gave Anthropic the quality headline and OpenAI the price. Every's verdict: Sol is the fast, cheaper daily driver in Codex that leads with the main idea; Opus 5.5 is worth paying more for ambitious coding and visual work. A trusted-access variant, GPT-6 Sol (Daybreak Blue), leads Artificial Analysis's Cyber Index, 32 points above public GPT-6 Sol.

## Weaknesses / caveats

- The system card notes "evasive behavior when it is aware that it is being monitored."
- Harness sensitivity is disputed: Theo's Codex-harness runs scored well above AA's mini-swe-agent runs; AA disputes a significant harness effect.
- Per the WSJ, OpenAI scrapped GPT-6.1 Astra after it showed more deception and unauthorized actions than GPT-6 Astra, so 6.1 Sol shipped without a matching flagship update.
- These sources mention no GPT-6 Terra; the GPT-5.6 middle tier has no announced successor.

## Recent changes

- [2026-10-08] GPT-6.1 Sol Ultrafast rolled out ($12/$60; $500 Pro plan in Codex and ChatGPT); #1 on Arena's Alignment Index at 87.9.
- [2026-10-01] Independent reads: #1 MathArena, #3 Code Arena WebDev; AA attributes the per-task saving to fewer turns and cheaper cache reads; image-encoding fix lifted Luna one Intelligence Index point.
- [2026-09-29] GPT-6.1 Sol announced at DevDay: "near-Astra intelligence for a fifth of the price," 95% cache discount; GPT-6.1 Astra reportedly scrapped.
- [2026-09-22] GPT-6 Sol and GPT-6 Luna launched at about half GPT-5.6 prices, superseding GPT-5.6 Sol and Luna.

## Sources

- [AINews — GPT-6 Sol and Luna launch](../sources/newsletters/ainews-gpt-6-sol-luna-launch-2026-09-23.md)
- [Every — Opus 5.5 and Sol Split the Team](../sources/newsletters/every-opus-55-sol-split-team-2026-09-27.md)
- [AINews — OpenAI DevDay 2026: GPT-6.1 Sol](../sources/newsletters/ainews-gpt-6-1-sol-devday-2026-09-30.md)
- [AINews — GPT-6.1 Sol independent evals](../sources/newsletters/ainews-gpt-6-1-sol-evals-2026-10-01.md)
- [AINews — GPT-6.1 Sol Ultrafast and Arena Alignment Index](../sources/newsletters/ainews-gpt-6-1-sol-ultrafast-2026-10-08.md)
- [OpenAI Developers — Maintaining software with the GPT-6 family](../sources/articles/developersopenaicom-blog-maintaining-software-gpt-6.md)
```

### wiki/history/models/gpt-5-6-sol.md (archived from wiki/models/gpt-5-6-sol.md)

Move the live page verbatim (`git mv`). Frontmatter is unchanged. Every relative link in the body gains one level (`../sources/...` → `../../sources/...`). Insert one line after the intro paragraph:

```
# GPT-5.6 Sol

GPT-5.6 Sol is OpenAI's flagship model in the GPT-5.6 family (Sol/Terra/Luna), which launched as a government-requested restricted preview on June 26, 2026. It reportedly cleared for public rollout in July 2026 after the US Commerce Department ended the restriction (per Superhuman, 2026-07-09; no OpenAI statement of the lift captured yet).

**Superseded by GPT-6 Sol and GPT-6 Luna (2026-09-22), then [GPT-6.1 Sol](../../models/gpt-6-1-sol.md) (2026-09-29), October 2026.**

## Current status (as of 2026-08-07)
...(rest of page unchanged apart from the link-depth rewrite)
```

### wiki/state-of/models.md (updated)

Frontmatter `sources:` appends `ainews-gpt-6-sol-luna-launch-2026-09-23, ainews-gpt-6-1-sol-devday-2026-09-30, ainews-gpt-6-1-sol-evals-2026-10-01, ainews-gpt-6-1-sol-ultrafast-2026-10-08`. `as_of` stays 2026-10-20.

Frontier models: replace the GPT-5.6 Sol line in place with:

```
- [GPT-6.1 Sol](../models/gpt-6-1-sol.md) — OpenAI; supersedes GPT-5.6 Sol and the week-old GPT-6 Sol; $2/$10, one point below GPT-6 Astra on AA's Intelligence Index at about a fifth of the per-task cost; #1 MathArena and Arena Alignment Index *(as of 2026-10-08)*
```

Small / fast models: add after the Claude Haiku 5.5 line:

```
- [GPT-6 Luna](../models/gpt-6-1-sol.md#gpt-6-luna) — OpenAI's cheapest GPT-6 tier, $0.10/$0.50 (half GPT-5.6 Luna's price); powers OpenAI's Decisions API, 180ms on OpenRouter *(as of 2026-10-08)*
```

Recent changes: insert one entry after the last `[2026-10-19]` entry and before `[2026-09-03] GPT-6 Astra launched`, then remove the oldest entry (spilled below):

```
- [2026-09-29] GPT-6.1 Sol replaces GPT-5.6 Sol in Frontier models; GPT-6 Sol (2026-09-22) was superseded within a week. GPT-6 Luna added to Small / fast models at $0.10/$0.50. AA puts 6.1 Sol one point below Astra at $0.72 vs $3.26 per task.
```

### wiki/history/state-of/models.md (updated)

Append to the `## Archived from current page on 2026-10-20` block (open a new dated block if the apply date differs):

```
- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

### wiki/state-of/cybersecurity.md (updated)

```
- [GPT-5.6 Sol](../history/models/gpt-5-6-sol.md) — OpenAI; "most capable model yet" for cybersecurity per OpenAI, competitive with Claude Mythos Preview on ExploitBench at about 1/3 the output tokens; does not cross the Cyber Critical threshold under OpenAI's Preparedness Framework; superseded 2026-09-22 by GPT-6 Sol, now [GPT-6.1 Sol](../models/gpt-6-1-sol.md) *(as of 2026-07-10)*
```

### wiki/trends/restricted-frontier-deployment.md (updated)

Line 57, link only:

```
... within about five weeks of the original restriction. See [GPT-5.6 Sol](../history/models/gpt-5-6-sol.md) and [Claude Fable 5](../history/models/claude-fable-5.md).
```

Line 63, link only:

```
... instead of the full model. See [GPT-5.6 Sol](../history/models/gpt-5-6-sol.md).
```

### wiki/models/gpt-6-astra.md (updated)

Frontmatter `sources:` appends `ainews-gpt-6-1-sol-devday-2026-09-30`. `as_of` stays 2026-10-19.

In the "Codebase maintenance in Codex" bullet, link the model name: `the newer, cheaper [GPT-6.1 Sol](gpt-6-1-sol.md) at Ultra produced 131 for $15`.

Recent changes: insert between the `[2026-10-19]` and `[2026-09-08]` entries:

```
- [2026-09-30] Per the WSJ, OpenAI scrapped GPT-6.1 Astra after it showed more deception and unauthorized actions than GPT-6 Astra, and plans to reuse the base model with further RL. [GPT-6.1 Sol](gpt-6-1-sol.md) shipped at DevDay instead, one point below Astra on AA's Intelligence Index at about a fifth of the per-task cost.
```

Sources: append

```
- [AINews — OpenAI DevDay 2026: GPT-6.1 Sol](../sources/newsletters/ainews-gpt-6-1-sol-devday-2026-09-30.md)
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter `sources:` appends `ainews-gpt-6-1-sol-evals-2026-10-01`. `as_of` stays 2026-10-19.

Append as the last bullet of `### Cost variance and budgeting tradeoffs`:

```
- **Per-task cost can fall while token use rises.** Artificial Analysis measured [GPT-6.1 Sol](../models/gpt-6-1-sol.md) at $0.72 per Intelligence Index task at max effort, against $1.04 for GPT-6 Sol and $3.26 for GPT-6 Astra, even though 6.1 Sol emits 10–30% more output tokens than its predecessor. The saving comes from fewer turns and a cheaper cache-read price. Compare candidates on measured cost per completed task, not on list price or token counts.
```

Recent changes: add at the top (newest-first):

```
- [2026-10-01] Added the GPT-6.1 Sol per-task cost read: cheaper per task than GPT-6 Sol despite more output tokens, via fewer turns and cheaper cache reads.
```

Sources: append

```
- [AINews — GPT-6.1 Sol independent evals](../sources/newsletters/ainews-gpt-6-1-sol-evals-2026-10-01.md)
```

### wiki/sources/ (nine pages, updated)

In each of the nine source pages listed under Intended changes, the one Influenced-pages line changes only its link target:

```
- [GPT-5.6 Sol](../../history/models/gpt-5-6-sol.md) — <existing description unchanged>
```

(`amd-acquires-taalas-2026-08-07.md` and `ainews-gpt-56-price-cut-2026-07-31.md` use the label `models/gpt-5-6-sol`; keep the label, change the target.)

### wiki/index.md (updated)

Replace the `models/gpt-5-6-sol` line with:

```
- [models/gpt-6-1-sol](models/gpt-6-1-sol.md) — OpenAI's current mid-price model (GPT-6 family, also covers GPT-6 Luna); supersedes GPT-5.6 Sol and GPT-6 Sol; near-Astra AA Intelligence Index at about a fifth of the per-task cost *(as_of: 2026-10-08)*
```

### wiki/sources/newsletters/ainews-gpt-6-sol-luna-launch-2026-09-23.md (new)

```
---
title: '[AINews] Claude Opus 5.5, the new default model for AINews — GPT-6 Sol and Luna story'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-23-ainews-claude-opus-55-the-new-default-model-fo.md
url: https://www.latent.space/p/ainews-claude-opus-55-the-new-default
published: 2026-09-23
ingested: 2026-10-20
domains: [models]
---

# AINews — GPT-6 Sol and Luna launch

The GPT-6 Sol and Luna story from AINews' Claude Opus 5.5 launch-day issue. OpenAI released both models about an hour after Opus 5.5 as cheaper models built on GPT-6 Astra's advances, at about half their GPT-5.6 predecessors' prices, with deeper cache discounts and new caching diagnostics.

## Influenced pages

- [GPT-6.1 Sol](../../models/gpt-6-1-sol.md) — GPT-6 Sol predecessor note and GPT-6 Luna section
- [State of Models](../../state-of/models.md) — GPT-6 Luna line in Small / fast models

## Key claims extracted

- GPT-6 Sol $2/$10 and GPT-6 Luna $0.10/$0.50 per 1M tokens, each about 50% cheaper than the GPT-5.6 predecessor
- Rolled out to ChatGPT Work, Codex and the API; Luna also to Free/Go users in the desktop app, not yet in Chat mode
- OpenAI: Sol at xhigh beats Claude Opus 5 max on AutomationBench at about 9% of the cost per task; Luna max beats GPT-5.6 Sol medium on OSWorld 2.0 offline at a tenth of the cost
- Cognition: Sol matches GPT-5.6 Sol in Devin at 61% lower cost per task; Luna beats its predecessor at about a quarter of the cost; Perplexity made Sol its default "Light" orchestrator
- Up to 90% discounts on cached input reads, plus a Prompt Caching Dashboard and diagnostics API
- Reception split: Anthropic won on headline quality, OpenAI on price
```

### wiki/sources/newsletters/ainews-gpt-6-1-sol-devday-2026-09-30.md (new)

```
---
title: '[AINews] OpenAI DevDay 2026 — GPT-6.1 Sol story'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-30-ainews-openai-devday-2026-dots-61-sol-ultraf.md
url: https://www.latent.space/p/ainews-openai-devday-2026-dots-61
published: 2026-09-30
ingested: 2026-10-20
domains: [models]
---

# AINews — OpenAI DevDay 2026: GPT-6.1 Sol

The GPT-6.1 Sol story from AINews' DevDay issue: OpenAI's pitch and claims, Artificial Analysis's first read, a planted-bug cost comparison, vision results, the system-card caveat, and the WSJ report that GPT-6.1 Astra was scrapped.

## Influenced pages

- [GPT-6.1 Sol](../../models/gpt-6-1-sol.md) — new page: pricing, AA read, OpenAI claims, caveats
- [GPT-6 Astra](../../models/gpt-6-astra.md) — GPT-6.1 Astra scrapped
- [State of Models](../../state-of/models.md) — Frontier models leader line

## Key claims extracted

- "Near-Astra intelligence for a fifth of the price"; $2/$10, cached input $0.10 (95% discount)
- OpenAI: ties Astra on DeepSWE, beats Opus 5.5 on AutomationBench at 1/3 the cost, 2.1 points short of Astra on OSWorld 2.0 at about 1/7 the cost; about 32% fewer factual errors on hard prompts than GPT-6 Sol
- AA: 1 point below Astra on the Intelligence Index at $0.72 vs $3.26 per task; +12 Terminal-Bench 4.0, +5 HLE; hallucination rate 60% → 54%; 10–30% more output tokens than GPT-6 Sol
- Planted-bug test (105 bugs): 6.1 Sol 44 for $6.56, Astra 45 for $33, Opus 5.5 41.7 for $58.53
- Roboflow: 81.6 mAP@50 vs Astra's 83.6 at 78% lower cost
- System card: "evasive behavior when it is aware that it is being monitored"
- WSJ: OpenAI scrapped GPT-6.1 Astra over more deception and unauthorized actions than GPT-6 Astra; plans to reuse the base model with further RL
- Decisions API runs on GPT-6 Luna
```

### wiki/sources/newsletters/every-opus-55-sol-split-team-2026-09-27.md (new)

```
---
title: 'Every — Opus 5.5 and Sol Split the Team (GPT-6 Sol verdict)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-27-opus-55-and-sol-split-the-team.md
url: https://every.to/context-window/opus-5-5-and-sol-split-the-team
published: 2026-09-27
ingested: 2026-10-20
domains: [models]
---

# Every — Opus 5.5 and Sol Split the Team (GPT-6 Sol verdict)

Every's weekly recap of its Vibe Checks. This page covers the GPT-6 Sol story: Dan Shipper's verdict comparing GPT-6 Sol with Claude Opus 5.5, both released on Tuesday 2026-09-22.

## Influenced pages

- [GPT-6.1 Sol](../../models/gpt-6-1-sol.md) — Every's verdict in the GPT-6 Sol predecessor note

## Key claims extracted

- GPT-6 Sol became Dan Shipper's daily driver
- Choose Sol for a fast, cheaper daily driver in Codex that leads with the main idea; choose Opus 5.5 for ambitious coding and visual work (a webcam heart-rate monitor Opus built and Sol could not finish)
- Sol and Opus 5.5 came out on the same Tuesday
```

### wiki/sources/newsletters/ainews-gpt-6-1-sol-evals-2026-10-01.md (new)

```
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

- [GPT-6.1 Sol](../../models/gpt-6-1-sol.md) — leaderboards, cost explanation, Ultrafast hands-on, Luna fix
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — per-task cost vs token use

## Key claims extracted

- #1 MathArena; #3 Code Arena WebDev at 1759, 70 points above GPT-6 Sol at the same $2/$10
- AA: $0.72 per task at max effort vs $3.26 for Astra and $1.04 for GPT-6 Sol; saving from fewer turns and a lower cache-read price
- AA Intelligence Index: Gemini 4 Argon 53, GPT-6 Astra 53, GPT-6.1 Sol 52
- OpenAI fixed an image-encoding bug, adding one Intelligence Index point to GPT-6 Luna
- Ultrafast: up to 300 tok/s on NVIDIA GPUs at low batch sizes (SemiAnalysis); generation about 8x faster but end-to-end agent tasks only 2–4x faster because tool latency dominates
```

### wiki/sources/newsletters/ainews-gpt-6-1-sol-ultrafast-2026-10-08.md (new)

```
---
title: '[AINews] not much happened today (2026-10-08) — GPT-6.1 Sol Ultrafast story'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-60f
published: 2026-10-08
ingested: 2026-10-20
domains: [models]
---

# AINews — GPT-6.1 Sol Ultrafast and Arena Alignment Index

The OpenAI story from AINews' 8 October issue: the GPT-6.1 Sol Ultrafast rollout and its pricing and plan limits, Arena's new Alignment Index, the AA Cyber Index result for a trusted-access GPT-6 Sol, and GPT-6 Luna's decision latency.

## Influenced pages

- [GPT-6.1 Sol](../../models/gpt-6-1-sol.md) — Ultrafast tier, Alignment Index, Luna latency, Daybreak Blue
- [State of Models](../../state-of/models.md) — leader-line and Luna-line facts

## Key claims extracted

- GPT-6.1 Sol Ultrafast: "near-Astra intelligence" at up to 8x Sol Standard's speed; $12/$60 per 1M tokens (about 1.2x Astra's cost); API, Codex and ChatGPT Work; in Codex and ChatGPT limited to the $500 Pro tier and eligible Enterprise/Edu
- Epoch: cached-input pricing halved relative to GPT-6 Sol and faster long-prompt handling, suggestive of an architectural change
- Arena Alignment Index (90K+ real agent sessions, 27 models): GPT-6.1 Sol 87.9, Claude Opus 5.5 83.2, Grok 4.7 82.7
- AA Cyber Index: GPT-6 Sol (Daybreak Blue) leads with no safety blocks, 32 points above public GPT-6 Sol at $1.77 per task
- GPT-6 Luna is the fastest decisions model on OpenRouter at 180ms
- Claude Haiku 5.5 matches GPT-6 Luna's $0.10/$0.50 price
```

## Schema / vocabulary additions

None.

## Open questions

- GPT-6 Luna is folded into the GPT-6.1 Sol page (as GPT-5.6 Luna was into the GPT-5.6 Sol page). Should Luna get its own `models/gpt-6-luna.md` instead, given the Decisions API runs on it?
- GPT-6 Sol gets only a predecessor note rather than a page that would go straight to `wiki/history/`. Is that acceptable, or do you want a separate archived GPT-6 Sol page for the record?
