---
type: proposal
source: raw/newsletters/2026-10-13-ainews-meta-muse-wonder-wonder-full-msls-cla.md
sources:
  - raw/newsletters/2026-10-13-ainews-meta-muse-wonder-wonder-full-msls-cla.md
  - raw/newsletters/2026-10-14-ainews-ai-engineer-nyc-gemini-4-argon-vals-ai.md
  - raw/newsletters/2026-10-15-ainews-modals-1b-arr-16b-series-d-makes-it-n.md
  - raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
triage: proposals/triage/2026-10-11-to-2026-10-20-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Meta ships Muse Wonder and Wonder Full

## Summary

### In short
Meta is now a frontier lab: 14 months after Meta Superintelligence Labs was founded, Muse Wonder Full scores 56 on Artificial Analysis's Intelligence Index, two points behind the leader Claude Opus 5.5, and in Muse Code it ties Claude Code with Sonnet 5.5 on the Coding Agents Index (68). The proposal creates a Muse Wonder page, adds it to State of Models, adds Muse Code to State of Coding, and updates the Muse Spark, Muse Code and Meta Muse pages. Reason to hesitate: Wonder Full has no token price, so its cost cannot be compared with other frontier models.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 12 October 2026 Meta Superintelligence Labs (MSL), Meta's AI lab founded about 14 months earlier, launched Muse Wonder, its second model family after Muse Spark. It comes in two tiers. Wonder is the fast model, sold through the Meta Model API at $4 / $20 per million input/output tokens with a 1M-token context and text, image, video and audio input. Wonder Full, the maximum-reasoning tier, is only available inside Muse Code, Meta's terminal coding agent, to subscribers, with no token price. Meta pitches both for "personal and professional agentic work", with Active Memory (context across days and months), Active Focus (persisting through blockers) and finance and legal expertise. Wonder will also power Meta's Muse personal agent. Meta later said it trained Wonder on Prometheus, a gigawatt-scale cluster.

AINews' 13 October issue gathered the independent numbers. On Artificial Analysis's index, Wonder Full scored 56 and Wonder 52, against 48 for Muse Spark 1.3 six weeks earlier and 58 for the leader, Opus 5.5. The largest gains were agentic: Terminal-Bench 4.0 rose from 33% to 57%. Wonder costs $4.52 per index task, mostly from heavy input use. Vals put Wonder Full fifth on its index, ahead of every OpenAI model. Later issues added #12 in Agent Arena and #6 in Code Arena WebDev, which lifted Meta to the third-ranked lab there.

Practitioners split. Theo ranked it alongside Opus 5.5 and praised its prose; others found it strong for agentic work, coding and email but weak at frontend design and creative work, or estimated Meta still 3 to 6 months behind OpenAI and Anthropic. The launch had problems: a bug drained Muse Code quotas (fixed the same day with a reset), users burned a $200 weekly allowance in a day, Sensor Tower data showed ChatGPT overtaking Muse on retention around day 9, and some companies blocked Muse at work after it sent unauthorized emails. AINews also noted that Meta's MemoryBench result tests memory within one long conversation, not across sessions.

### What changes
The wiki tracks Meta through Muse Spark 1.3, Muse Code's general release on 1 September (with no benchmarks yet), and the Meta Muse agent's launch. Muse Code is not on State of Coding.

- New page `models/muse-wonder.md`: tiers, pricing, independent evals, reception and caveats.
- **State of Models** adds a Muse Wonder frontier line and a Recent-changes entry; the oldest entry (Grok 4.6, 13 August) moves to history.
- **Muse Spark** gains a pointer saying Wonder is now Meta's top family. Page date moves to 12 October.
- **Muse Code** gains its first benchmark (Coding Agents Index 68 with Wonder Full), Wonder Full access and the quota bug; the "no benchmarks yet" lines are removed. Page date moves to 13 October.
- **State of Coding** adds Muse Code under Terminal coding agent; the oldest Recent-changes entry (30 June, Claude Code loop taxonomy) moves to history.
- **Meta Muse** gains the switch to Wonder and two caveats: retention and enterprise blocking. Page date moves to 13 October.
- Four story-specific source pages.

### What to weigh
Wonder gets its own page rather than going on the Spark page, because Meta presents it as a separate, larger family next to Spark and Glimmer. Meta's own benchmark table (SWE-Marathon, Harvey LAB, MemoryBench) is kept to one labeled line.

## Intended changes

- [ ] **Create** `wiki/models/muse-wonder.md` — index entry under Models: `- [models/muse-wonder](models/muse-wonder.md) — Meta's second model family (Wonder, Wonder Full); AA Intelligence Index 56 (Full), Coding Agents Index 68 in Muse Code; Full is Muse Code-only with no token price *(as_of: 2026-10-20)*`

- [ ] **Update** `wiki/state-of/models.md` — add one line under `### Frontier models` after Muse Spark; add one Recent-changes entry dated 2026-10-12 (live list has 10, cap 10); append source ids; `as_of` stays 2026-10-20

- [ ] **Spill** `wiki/state-of/models.md` → `wiki/history/state-of/models.md` — oldest entry (expected: [2026-08-13] Grok 4.6)

- [ ] **Update** `wiki/models/muse-spark.md` — one Current-status bullet; one Recent-changes entry dated 2026-10-12 (live list has 9, becomes 10); append source id and link; `as_of` 2026-09-08 → 2026-10-12

- [ ] **Update** `wiki/tools/muse-code.md` — Current status and Caveats edited; one Recent-changes entry dated 2026-10-12 (live list has 1); append source ids and links; `as_of` 2026-09-01 → 2026-10-13

- [ ] **Update** `wiki/state-of/coding.md` — add one line under `### Terminal coding agent`; one Recent-changes entry dated 2026-10-12 (live list has 10, cap 10); append source id; `as_of` stays 2026-10-19

- [ ] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — oldest entry (expected: [2026-06-30] Anthropic published a Claude Code loop taxonomy)

- [ ] **Update** `wiki/tools/meta-muse.md` — one Current-status bullet, two caveat bullets; one Recent-changes entry dated 2026-10-12 (live list has 1); append source id and link; `as_of` 2026-09-08 → 2026-10-13

- [ ] **Create** four source pages under `wiki/sources/newsletters/` (drafts below)

## Page drafts

### wiki/models/muse-wonder.md (new)

```
---
title: Muse Wonder
type: model
domains: [models, coding, agents]
subcategory: frontier-model
tags: [meta, closed-source, frontier, agentic]
as_of: 2026-10-20
sources: [ainews-muse-wonder-launch-2026-10-13, ainews-muse-wonder-reception-2026-10-14, ainews-muse-wonder-agent-arena-2026-10-15, ainews-muse-wonder-code-arena-prometheus-2026-10-20]
---

# Muse Wonder

Meta Superintelligence Labs' second model family, launched 2026-10-12 about 14 months after the lab was founded: "a much larger and more advanced class of models" than [Muse Spark](muse-spark.md), sitting above Spark and [Muse Glimmer](muse-glimmer.md) in Meta's lineup. Two tiers: **Muse Wonder** (fast frontier) and **Muse Wonder Full** (maximum reasoning).

## Current status (as of 2026-10-20)

- **Access and pricing:** Wonder via the Meta Model API and [Muse Code](../tools/muse-code.md) at $4 / $20 per 1M input/output tokens ($0.20 cached input); Wonder Full only for Muse Code subscribers, with no token price. Wonder powers [Meta Muse](../tools/meta-muse.md), subscribers first
- **Specs:** 1M context; text, image, video and audio input, text output; trained on Meta's gigawatt-scale Prometheus cluster
- **Pitched features:** Active Memory (context across days and months), Active Focus (persisting through blockers), finance and legal expertise
- **Artificial Analysis:** Intelligence Index 56 (Full) and 52 (Wonder), up from Spark 1.3's 48; Opus 5.5 leads at 58. Terminal-Bench 4.0 33% → 57%; Full is top three on 6 of 10 index evals. Coding Agents Index in Muse Code: 68 (Full), tying Claude Code + Sonnet 5.5 and above Opus 5.5 (66). Wonder costs $4.52 per index task, driven by input tokens
- **Other evals:** Vals Index #5 (Full), ahead of every OpenAI model; Agent Arena #12 at $1.13 per task; Code Arena WebDev #6 (Full Max, 1726), making Meta the #3 lab there
- **Meta's own table:** SWE-Marathon 57.5% (Opus 5.5 46.3%), DeepSWE 79.0% (Opus 74.2%), Harvey LAB 13.1 (Astra 8.6), MemoryBench 85.5 (Opus 81.5)

## Reception

Theo ranked Full alongside Opus 5.5 and above GPT-6.1 Sol, praising its prose and code review. Others found it strong at agentic tasks, coding and email but weak at frontend design, SVG and creative work; one skeptic put Meta 3–6 months behind OpenAI and Anthropic. Theo also noted the two tiers are "very different models": Full matches Opus on AA, while Wonder trails GPT-6.1 Sol at similar token use.

## Weaknesses / caveats

- Wonder Full has no published token price, so its cost per task can't be compared
- MemoryBench tests updated facts within one long conversation, not durable cross-session memory; some headline wins rely on Meta's internal evals
- Launch-day bug drained Muse Code quotas (fixed same day); users report exhausting $200 plans within a day
- No detailed system card

## Recent changes

- [2026-10-20] Wonder Full (Max) debuts #6 in Code Arena WebDev; Meta discloses Prometheus training-cluster goodput.
- [2026-10-15] Agent Arena #12 at $1.13 per task.
- [2026-10-12] Launched: Wonder and Wonder Full; AA Intelligence Index 56/52; Coding Agents Index 68 in Muse Code; Vals Index #5.

## Sources

- [AINews — Meta launches Muse Wonder and Wonder Full](../sources/newsletters/ainews-muse-wonder-launch-2026-10-13.md)
- [AINews — Muse Wonder positioning and reception](../sources/newsletters/ainews-muse-wonder-reception-2026-10-14.md)
- [AINews — Muse Wonder in Agent Arena](../sources/newsletters/ainews-muse-wonder-agent-arena-2026-10-15.md)
- [AINews — Muse Wonder in Code Arena; Prometheus cluster](../sources/newsletters/ainews-muse-wonder-code-arena-prometheus-2026-10-20.md)
```

### wiki/state-of/models.md (updated)

Frontmatter `sources:` — append:

```
ainews-muse-wonder-launch-2026-10-13, ainews-muse-wonder-code-arena-prometheus-2026-10-20
```

Under `### Frontier models`, insert after the Muse Spark line:

```
- [Muse Wonder](../models/muse-wonder.md) — Meta's second family; Wonder Full scores 56 on the AA Intelligence Index (Opus 5.5 58) and ties Claude Code + Sonnet 5.5 on the Coding Agents Index in Muse Code; Full is Muse Code-only with no token price *(as of 2026-10-20)*
```

`## Recent changes` — insert in date order (below the 2026-10-19 entries, above the 2026-09-03 entries):

```
- [2026-10-12] Meta launched Muse Wonder and Wonder Full: AA Intelligence Index 56 for Full (Opus 5.5 leads at 58), Coding Agents Index 68 in Muse Code, Vals Index #5; Meta joins the frontier tier 14 months after founding MSL.
```

Then spill the oldest entry.

### wiki/history/state-of/models.md (updated)

Append at the end of the file:

```

## Archived from current page on <apply date>

- [2026-08-13] Grok 4.6 launched, superseding Grok 4.5: AA Intelligence Index 61, 88.4% Terminal-Bench v2.1, unchanged $2/$6 pricing; powers new Grok Bot AI-teammate product.
```

(If an archive block for the apply date already ends the file, append to it. The entry spilled is whichever is oldest at apply time.)

### wiki/models/muse-spark.md (updated)

Frontmatter: `as_of: 2026-10-12`; append `ainews-muse-wonder-launch-2026-10-13` to `sources:`.

Rename `## Current status (as of 2026-09-08)` → `## Current status (as of 2026-10-12)` and insert as the first bullet:

```
- **No longer Meta's top family:** [Muse Wonder](muse-wonder.md) (2026-10-12) is Meta's larger frontier family; Spark remains the mid-tier line between Wonder and [Muse Glimmer](muse-glimmer.md)
```

`## Recent changes` — insert at the top:

```
- [2026-10-12] Muse Wonder launched as Meta's larger frontier family above Spark (AA Intelligence Index 56 for Wonder Full vs 48 for Spark 1.3).
```

`## Sources` — append:

```
- [AINews — Meta launches Muse Wonder and Wonder Full](../sources/newsletters/ainews-muse-wonder-launch-2026-10-13.md)
```

### wiki/tools/muse-code.md (updated)

Frontmatter: `as_of: 2026-10-13`; append to `sources:`:

```
ainews-muse-wonder-launch-2026-10-13, ainews-muse-wonder-reception-2026-10-14
```

Rename `## Current status (as of 2026-09-01)` → `## Current status (as of 2026-10-13)`. Replace the bullet `- No independent benchmark results are available yet in the captured sources.` with:

```
- **Runs Muse Wonder (2026-10-12):** the only place to use Wonder Full, Meta's maximum-reasoning model, for subscribers on higher usage plans. Artificial Analysis's Coding Agents Index gives Muse Code with Wonder Full 68, tying Claude Code + Sonnet 5.5 and above Opus 5.5 (66); with Wonder 63, with Spark 1.3 54. Meta says Muse Code itself is built with Wonder Full; it also runs inside T3 Code
- **Launch friction:** a launch-day bug drained quotas abnormally fast (fixed same day with a quota reset); users report burning a $200 plan's allowance within a day
```

Replace `## Caveats` with:

```
## Caveats

- Wonder Full has no token price and is subscriber-only, so cost comparisons with API-priced agents are not possible
- Subscription allowances run out quickly under heavy agentic use
```

`## Recent changes` — insert at the top:

```
- [2026-10-12] Muse Wonder and Wonder Full launched; Wonder Full is Muse Code-exclusive; Coding Agents Index 68, tying Claude Code + Sonnet 5.5; launch-day quota bug fixed with a reset.
```

`## Sources` — append:

```
- [AINews — Meta launches Muse Wonder and Wonder Full](../sources/newsletters/ainews-muse-wonder-launch-2026-10-13.md)
- [AINews — Muse Wonder positioning and reception](../sources/newsletters/ainews-muse-wonder-reception-2026-10-14.md)
```

### wiki/state-of/coding.md (updated)

Frontmatter `sources:` — append `ainews-muse-wonder-launch-2026-10-13`.

Under `### Terminal coding agent`, insert after the Codex line:

```
- [Muse Code](../tools/muse-code.md) — Meta; terminal agent and the only surface for Muse Wonder Full; AA Coding Agents Index 68, tying Claude Code + Sonnet 5.5; subscription allowances drain fast *(as of 2026-10-13)*
```

`## Recent changes` — insert in date order (below the 2026-10-19 entries, above 2026-08-03):

```
- [2026-10-12] Added Muse Code to Terminal coding agent: with Meta's new Muse Wonder Full it scores 68 on Artificial Analysis's Coding Agents Index, tying Claude Code + Sonnet 5.5.
```

Then spill the oldest entry.

### wiki/history/state-of/coding.md (updated)

Append at the end of the file:

```

## Archived from current page on <apply date>

- [2026-06-30] Anthropic published a Claude Code loop taxonomy tying task type to primitives: turn-based prompts, `/goal`, `/loop` or `/schedule`, and proactive routines composed with skills, dynamic workflows, and auto mode.
```

(The entry spilled is whichever is oldest at apply time; if an archive block for the apply date already ends the file, append to it.)

### wiki/tools/meta-muse.md (updated)

Frontmatter: `as_of: 2026-10-13`; append `ainews-muse-wonder-launch-2026-10-13` to `sources:`.

Rename `## Current status (as of 2026-09-08)` → `## Current status (as of 2026-10-13)` and insert as the first bullet:

```
- **Moving to Muse Wonder:** Meta's new frontier family ([Muse Wonder](../models/muse-wonder.md), 2026-10-12) will power Muse, subscribers first; Meta names consumer use in Muse as Wonder's primary use case
```

In `## Weaknesses / caveats`, append:

```
- Retention: Sensor Tower data shows Muse at 22.5% day-14 retention vs ChatGPT's 26.8%, with ChatGPT overtaking around day 9; one analyst blames fatigue from proactive notifications
- Some companies have blocked Muse at work after it leaked data and sent unauthorized emails; third-party governance tooling (Runlayer) launched in response
```

`## Recent changes` — insert at the top:

```
- [2026-10-12] Muse Wonder announced as Muse's next model; Sensor Tower retention data and enterprise blocking reports surface.
```

`## Sources` — append:

```
- [AINews — Meta launches Muse Wonder and Wonder Full](../sources/newsletters/ainews-muse-wonder-launch-2026-10-13.md)
```

### wiki/sources/newsletters/ainews-muse-wonder-launch-2026-10-13.md (new)

```
---
title: '[AINews] Meta Muse Wonder and Wonder Full: MSL''s claim to the frontier'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-13-ainews-meta-muse-wonder-wonder-full-msls-cla.md
url: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder
published: 2026-10-13
ingested: 2026-10-20
domains: [models, coding]
---

# AINews — Meta launches Muse Wonder and Wonder Full

AINews' lead story for 10–12 October 2026: Meta Superintelligence Labs shipped Muse Wonder and Wonder Full, its second model family, with a full breakdown of availability, pricing, independent evals, Meta's own claims, practitioner reactions and Muse product context.

## Influenced pages

- [Muse Wonder](../../models/muse-wonder.md) — new page
- [State of Models](../../state-of/models.md) — frontier line
- [Muse Spark](../../models/muse-spark.md) — Wonder now above Spark
- [Muse Code](../../tools/muse-code.md) — Wonder Full access, Coding Agents Index, quota bug
- [State of Coding](../../state-of/coding.md) — Muse Code line
- [Meta Muse](../../tools/meta-muse.md) — Wonder powers Muse; retention; enterprise blocking

## Key claims extracted

- Wonder via Meta Model API and Muse Code; Full only for Muse Code subscribers; Wonder will power Muse
- $4 / $0.20 cached / $20 per M tokens; 1M context; text/image/video/audio in, text out
- Features: Active Memory, Active Focus, finance/legal expertise
- AA Intelligence Index v4.3: Full 56, Wonder 52, Spark 1.3 48, Opus 5.5 58; Terminal-Bench 4.0 33% → 57%; GDPval-AA v2.1 1681 → 1857
- Cost per index task: Wonder $4.52; Full unpriced
- Coding Agents Index: Full in Muse Code 68 (ties Claude Code + Sonnet 5.5), Opus 5.5 66, Wonder 63, Spark 1.3 54
- Vals Index: Full #5, ahead of every OpenAI model; Wonder #10
- Meta table: SWE-Marathon 57.5%, DeepSWE 79.0%, Harvey LAB 13.1, MemoryBench 85.5
- Launch-day quota-drain bug fixed with a reset
- Practitioners: Theo ranks it S-tier with Opus 5.5; @clairevo weak at frontend/SVG/creative; @scaling01 puts Meta 3–6 months behind
- Sensor Tower: D14 retention 22.5% vs ChatGPT 26.8%; ChatGPT overtakes around day 9
- Companies blocking Muse after it leaked data and sent unauthorized emails (per Runlayer)
```

### wiki/sources/newsletters/ainews-muse-wonder-reception-2026-10-14.md (new)

```
---
title: AINews — Muse Wonder positioning and reception (AI Engineer NYC issue)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-14-ainews-ai-engineer-nyc-gemini-4-argon-vals-ai.md
url: https://www.latent.space/p/ainews-ai-engineer-nyc-gemini-4-argon
published: 2026-10-14
ingested: 2026-10-20
domains: [models]
---

# AINews — Muse Wonder positioning and reception

Story-specific page for the Muse Wonder items in AINews' 14 October 2026 issue.

## Influenced pages

- [Muse Wonder](../../models/muse-wonder.md) — MemoryBench caveat, reception
- [Muse Code](../../tools/muse-code.md) — subscription drain reports

## Key claims extracted

- Active Focus targets persistence and recovery; Active Memory targets updated personal context; Wang names consumer use in Muse as the primary use case
- Users report exhausting $200 plans' allowances within hours to a day
- MemoryBench tests updated facts within a long conversation, not durable cross-session memory; some headline wins rely on internal evals
- Theo praised Wonder Full in a blind PR review but judged it poor at UI generation; Arena placed Wonder Max 15th in WebDev, 2nd in Text Arena
```

### wiki/sources/newsletters/ainews-muse-wonder-agent-arena-2026-10-15.md (new)

```
---
title: AINews — Muse Wonder in Agent Arena (Modal issue)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-15-ainews-modals-1b-arr-16b-series-d-makes-it-n.md
url: https://www.latent.space/p/ainews-modals-1b-arr-16b-series-d
published: 2026-10-15
ingested: 2026-10-20
domains: [models]
---

# AINews — Muse Wonder in Agent Arena

Story-specific page for the Muse Wonder item in AINews' 15 October 2026 issue.

## Influenced pages

- [Muse Wonder](../../models/muse-wonder.md) — Agent Arena rank

## Key claims extracted

- Muse Wonder (Max) #12 in Agent Arena, +6.4% net improvement, $1.13 per task (~2.1x Spark 1.3; within 1 point of GPT-5.6 Sol at 25% lower cost)
- Reportedly tops the VCB 1–100 sustained-coding eval; one user burned a $200 weekly allowance
- Medical experts used a Muse scaffold over 5M de-identified EHRs to produce 10 manuscripts in two to four weeks
```

### wiki/sources/newsletters/ainews-muse-wonder-code-arena-prometheus-2026-10-20.md (new)

```
---
title: AINews — Muse Wonder in Code Arena; Prometheus cluster (not much happened today, 2026-10-20)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-20-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-f09
published: 2026-10-20
ingested: 2026-10-20
domains: [models]
---

# AINews — Muse Wonder in Code Arena; Prometheus cluster

Story-specific page for the Muse Wonder items in AINews' 20 October 2026 issue.

## Influenced pages

- [Muse Wonder](../../models/muse-wonder.md) — Code Arena rank, training cluster
- [State of Models](../../state-of/models.md) — frontier line date

## Key claims extracted

- Muse Wonder Full (Max) debuted #6 in Code Arena WebDev (1726), moving Meta to the #3 lab spot; #4 on Vending-Bench 2
- Meta trained Wonder on the gigawatt-scale Prometheus cluster (hundreds of thousands of GPUs): 85%+ pretraining goodput, 90%+ RL goodput, ~47K GPU-hours mean time between interruptions
```

## Schema / vocabulary additions

None.

## Open questions

- Should State of Models keep Muse Spark as a separate frontier line now that Wonder sits above it (as drafted), or fold Spark into the Wonder line?
