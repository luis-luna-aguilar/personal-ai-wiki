---
type: proposal
source: raw/newsletters/2026-07-17-ainews-kimi-k3-28t-a50b-the-largest-open-model.md
status: pending
created: 2026-09-06
---

# Proposal: Moonshot's Kimi K3 supersedes K2.7-Code as its flagship

## Summary

### The source

On 2026-07-17, AINews carried the full technical and benchmark breakdown of Kimi K3, Moonshot AI's new flagship: 2.8 trillion total parameters (the largest open model announced to date), 1M-token context, native text+image multimodal input, a new attention mechanism called Kimi Delta Attention claimed to decode 6.3x faster at 1M context, and "Attention Residuals" for training efficiency. Moonshot promised open weights by 2026-07-27; usage surged enough on the hosted API that Moonshot briefly paused new subscriptions, alongside a reported $31.5B valuation round (per a companion newsletter). Independent numbers from Artificial Analysis place K3 at 57 on its Intelligence Index — comparable to Opus 4.8 and GPT-5.5, though behind Fable 5 and GPT-5.6 Sol — at $0.94/task, undercutting both GPT-5.6 Sol ($1.04) and Opus 4.8 ($1.80). On Arena's human-preference leaderboard, K3 jumped from #18 (as K2.6) to #1 in the Frontend Code Arena, with 1679 Elo and a 76% pairwise win rate versus Fable 5's 63%. The one regression: K3's hallucination rate on Artificial Analysis's Omniscience eval rose to 51% from K2.6's 39%, despite the accuracy gain. A third newsletter frames the release against China's broader open-weight push and revenue growth.

### What changes

The wiki currently tracks Moonshot's flagship as Kimi K2.7-Code (`models/kimi-k2-7-code.md`), a narrower coding-specialist model listed in State of Models' Coding-models subcategory and referenced from State of Coding's Kimi Code tool line.

- **Kimi K2.7-Code moves to history** (`wiki/history/models/kimi-k2-7-code.md`, unchanged) and **new page `models/kimi-k3.md`** becomes the current Moonshot flagship — broader in scope than its predecessor (general multimodal model, not a coding specialist), so it's filed under the Open-weight-model subcategory rather than Coding-model.
- **State of Models** removes the K2.7-Code line from Coding models and adds a new K3 line under Open-weight models (2.8T params, Intelligence Index 57, $0.94/task, #1 Frontend Code Arena). A new Recent-changes entry is added dated 17 July; the section is at its 10-entry cap, so the oldest entry spills to `wiki/history/state-of/models.md`.
- **Open-weight momentum broadens** gains a Current-signal bullet naming K3 as the clearest open-weight capability jump so far in the trend this page tracks, plus a Recent-changes entry (same cap/spill mechanics as above, against that page's own history file).
- One new source page, `sources/newsletters/ainews-kimi-k3-2026-07-17.md`, folding in all three same-day newsletters (the valuation and China-framing pieces add context, not independent technical claims).

### What to weigh

The "supersedes K2.7-Code" call is a judgment about the two models' relative scope, not an explicit Moonshot statement — K2.7-Code was coding-specialized while K3 is a general flagship that happens to lead a coding-preference arena, so treating K3 as Moonshot's one current flagship (rather than keeping both live) is worth a second look. Separately, `tools/kimi-code.md` (the CLI tool) currently says it's "powered by Kimi K2.7-Code" — nothing in this source says whether the tool itself has moved to K3, so that page is left untouched here rather than guessed at. All benchmark figures are Artificial Analysis's/Arena's independent numbers, not Moonshot's own claims, so sourcing is solid; weights aren't out yet as of the source date (promised 2026-07-27), so this page describes an announced-but-not-yet-open model.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/kimi-k3.md` — new current-flagship page
    > See draft below

- [ ] **Spill** `wiki/models/kimi-k2-7-code.md` → `wiki/history/models/kimi-k2-7-code.md` — superseded by Kimi K3; page content carries over unchanged
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — removes the K2.7-Code line from Coding models; adds a K3 line under Open-weight models; adds one Recent-changes entry dated 2026-07-17; spills the oldest Recent-changes entry to history
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — adds one Current-signal bullet on Kimi K3; adds one Recent-changes entry dated 2026-07-17; spills the oldest Recent-changes entry to history
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-kimi-k3-2026-07-17.md` — source summary covering all three newsletters

- [ ] **Update** `wiki/index.md` — replace the `models/kimi-k2-7-code` entry with `models/kimi-k3`

## Page drafts

### wiki/models/kimi-k3.md (new)

```md
---
title: Kimi K3
type: model
domains: [models, coding]
subcategory: open-weight-model
tags: [moonshot-ai, open-weights, agentic]
as_of: 2026-07-17
sources: [ainews-kimi-k3-2026-07-17]
---

# Kimi K3

Moonshot AI's new flagship, announced 2026-07-17, and its largest model to date at 2.8T total parameters — the largest open-model announcement seen so far. Supersedes [Kimi K2.7-Code](../history/models/kimi-k2-7-code.md) as Moonshot's current flagship; broader in scope than its coding-specialist predecessor. Open weights promised by 2026-07-27.

## Current status (as of 2026-07-17)

- 2.8T total parameters; 1M-token context; native text+image multimodal input
- Kimi Delta Attention: new attention mechanism claimed 6.3x faster decoding at 1M context
- "Attention Residuals" architecture for training efficiency
- Open weights promised 2026-07-27; hosted API usage surged enough that Moonshot briefly paused new subscriptions
- Artificial Analysis Intelligence Index: 57 — comparable to Opus 4.8 and GPT-5.5, behind Fable 5 and GPT-5.6 Sol — at $0.94/task (vs. GPT-5.6 Sol's $1.04, Opus 4.8's $1.80)
- Arena Frontend Code Arena: #1, 1679 Elo, 76% pairwise win rate (vs. Fable 5's 63%) — jumped from #18 as K2.6

## Caveats

- Hallucination rate on Artificial Analysis's Omniscience eval regressed to 51% (from K2.6's 39%) despite the accuracy gain
- Weights not yet released as of the source date; benchmarked via hosted API

## Recent changes

- [2026-07-17] Announced: 2.8T params, Kimi Delta Attention, Intelligence Index 57, #1 Frontend Code Arena; supersedes Kimi K2.7-Code as Moonshot's flagship

## Sources

- [AINews — Kimi K3 (2.8T, largest open model)](../sources/newsletters/ainews-kimi-k3-2026-07-17.md)
```

### wiki/history/models/kimi-k2-7-code.md (new — spilled, unchanged content)

```md
---
title: Kimi K2.7-Code
type: model
domains: [models, coding]
subcategory: coding-model
tags: [moonshot-ai, open-weights, agentic]
as_of: 2026-06-13
sources: [kimi-k27-code-june-2026]
---

# Kimi K2.7-Code

Moonshot AI's June 2026 open-source coding model. Successor to Kimi K2.6. 1T total / 32B active MoE with MLA attention, 256K context. Claims strong improvements in coding task efficiency — 30% fewer reasoning tokens than K2.6 on the same tasks.

## Current status (as of 2026-06-13)

- 1T total / 32B active MoE; MLA attention; 256K context
- Open-source; vLLM and SGLang support on day of release
- **Benchmark claims (Moonshot-reported):**
  - +21.8% on Kimi Code Bench v2
  - +11.0% on Program Bench
  - +31.5% on MLS Bench Lite
  - 30% fewer reasoning tokens than K2.6
  - KernelBench-Hard: more authentic Triton kernels than K2.6 (qualitative community signal)
- Community reception: honest benchmark behavior, solid step up from K2.6; several benchmarks are Moonshot's own

## Caveats

- Primary benchmark comparisons are Moonshot-reported; independent leaderboard positions not yet available
- Released the same week as GLM-5.2, which received more community attention
- K2.6's long-horizon execution demos (12+ hour runs, 4K+ tool calls) have not been replicated publicly for K2.7-Code yet

## Recent changes

- [2026-06-13] Released as open-source; supersedes Kimi K2.6
- [2026-07-17] Superseded by Kimi K3 as Moonshot's current flagship; archived to history

## Sources

- [Kimi K2.7-Code release — AINews June 2026](../../sources/newsletters/kimi-k27-code-june-2026.md)
```

### wiki/state-of/models.md (updated)

Remove from Coding models:

```md
- [Kimi K2.7-Code](../models/kimi-k2-7-code.md) — Moonshot AI; open-source 1T/32B MoE; 256K context; +21.8% Kimi Code Bench v2; 30% fewer reasoning tokens than K2.6; vLLM/SGLang day-0 support *(as of 2026-06-13)*
```

Add to Open-weight models:

```md
- [Kimi K3](../models/kimi-k3.md) — Moonshot AI; 2.8T params; Kimi Delta Attention; Intelligence Index 57 at $0.94/task; #1 Frontend Code Arena (1679 Elo, 76% win rate); open weights promised 2026-07-27 *(as of 2026-07-17)*
```

New Recent-changes entry (insert as newest; enforce cap by spilling the oldest live entry to `wiki/history/state-of/models.md`):

```md
- [2026-07-17] Kimi K3 (2.8T, Moonshot) announced: Intelligence Index 57, #1 Frontend Code Arena; supersedes Kimi K2.7-Code as Moonshot's flagship, moved from Coding models to Open-weight models.
```

### wiki/trends/open-weight-momentum-broadens.md (updated)

New Current-signal bullet:

```md
- **Kimi K3 (Moonshot, July 2026):** the clearest open-weight capability jump in this trend so far — 2.8T params, Intelligence Index 57 (Opus 4.8/GPT-5.5 tier), and #1 on Arena's Frontend Code Arena, up from #18 as K2.6. Open weights promised 2026-07-27.
```

New Recent-changes entry (insert as newest; enforce cap by spilling the oldest live entry to `wiki/history/trends/open-weight-momentum-broadens.md`):

```md
- [2026-07-17] Kimi K3 (Moonshot, 2.8T) announced: Intelligence Index 57, #1 Frontend Code Arena — the clearest open-weight capability jump in this trend so far.
```

### wiki/sources/newsletters/ainews-kimi-k3-2026-07-17.md (new)

```md
---
title: AINews — Kimi K3 (2.8T, largest open model)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-17-ainews-kimi-k3-28t-a50b-the-largest-open-model.md
ingested: 2026-09-06
domains: [models, coding]
---

# AINews — Kimi K3 (2.8T, largest open model)

Moonshot AI announced Kimi K3, its new flagship: 2.8T total parameters, Kimi Delta Attention, 1M-token context, Intelligence Index 57, and #1 on Arena's Frontend Code Arena. Open weights promised 2026-07-27; hosted usage surged enough to pause new subscriptions. Supersedes Kimi K2.7-Code as Moonshot's flagship.

## Influenced pages

- [Kimi K3](../../models/kimi-k3.md) — new page
- [Kimi K2.7-Code](../../history/models/kimi-k2-7-code.md) — archived, superseded
- [State of Models](../../state-of/models.md) — Coding models line removed, Open-weight models line added
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — new Current-signal bullet

## Key claims extracted

- 2.8T total parameters, largest open-model announcement to date
- Kimi Delta Attention: 6.3x faster decoding claimed at 1M context
- Artificial Analysis Intelligence Index 57 at $0.94/task
- Arena Frontend Code Arena #1 (1679 Elo, 76% win rate), up from #18 as K2.6
- Omniscience hallucination rate regressed to 51% (from 39% for K2.6)
- Open weights promised 2026-07-27
```

## Schema / vocabulary additions

None.

## Open questions

- `tools/kimi-code.md` (the CLI tool) still says it's powered by K2.7-Code — should a future source confirm whether Kimi Code has moved to K3, that page would need its own update; nothing in this source addresses it, so it's left alone here.
