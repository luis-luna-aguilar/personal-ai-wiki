---
type: proposal
source: raw/newsletters/2026-08-04-ainews-qwen-38-max24t-and-27b-new-open-weig.md
status: pending
created: 2026-09-07
---

# Proposal: Qwen 3.8 Max ships in full

## Summary

### The source

AINews' 2026-08-04 issue covers Alibaba's Qwen3.8-Max moving from live preview to a full launch. The new flagship weighs in at 2.4T total parameters with roughly 95B active per token by third-party estimate (a ~4% activation ratio), a 1M-token context window, and API pricing of $2/M input and $6/M output tokens. Alibaba says open weights are coming "next week" for both Qwen3.8-Max and a smaller companion, Qwen3.8-27B. Third-party evals landed quickly and favorably: #4 overall on Frontend Code Arena at 1,668 Elo (behind only Claude Opus 5 and Kimi K3), #2 on Vision Arena, and a Vals AI Index score of 66.1 that matches Claude Opus 4.7 at roughly 2.3x lower cost per test, with SWE-bench at 87.3% and Terminal-Bench 2.1 at 67.4 — up from 57.5 for Qwen 3.7 Max about two and a half months earlier. The clearest substantive pushback wasn't about capability but licensing: a widely-shared post read the license terms as restricting use or even download of the model in the US, EU, UK, and Korea, echoing a nearly identical complaint raised the same week about MiniMax H3's release. AINews frames the broader move as Alibaba choosing ecosystem influence over exclusivity, as DeepSeek, Kimi, and other Chinese open releases eroded the case for keeping a top-tier model API-only.

### What changes

The wiki currently has Qwen 3.8 only as a preview page (entered live preview 2026-07-20, 2.4T reported, open-weight *commitment* but no benchmarks or pricing). This converts it to the full-launch state and reflects the new licensing wrinkle across three pages.

- **Qwen 3.8** rewrites Current status with real benchmarks, real pricing, the Qwen3.8-27B companion, and the license-restriction caveat. Page date moves to 4 August.
- **State of Models** gains a new Open-weight models line for Qwen 3.8 Max, and a new Recent-changes entry; the oldest entry falls off to history since the section is at its 10-entry cap.
- **Open-weight momentum broadens** updates its existing Qwen3.8-Max-Preview bullet to reflect the full launch and the licensing caveat, and gains a new Recent-changes entry; oldest entry falls off to history under the same cap.
- New source page for the AINews recap.

### What to weigh

The 95B active-parameter figure and the license-restriction reading both come from third-party summaries (ZhihuFrontier and a single X post from OstrisAI, respectively), not an Alibaba spec sheet or statement — Alibaba hasn't clarified the license terms in the source coverage, so that caveat is carried as reported, not confirmed. Both **State of Models** and **Open-weight momentum broadens** are already sitting at the 10-entry Recent-changes cap, and other proposals from this same digest batch also touch both pages, so the actual oldest entry spilled at apply time may not match what's shown here — that's expected and resolved by the standard rebase rules, not a defect in this draft.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/qwen-3-8.md` — full-launch rewrite: benchmarks, pricing, Qwen3.8-27B sibling, licensing caveat
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — add Qwen 3.8 Max to Open-weight models; add Recent-changes entry (spills oldest)
    > See draft below

- [ ] **Update** `wiki/trends/open-weight-momentum-broadens.md` — update Qwen3.8-Max-Preview bullet to full-launch + licensing caveat; add Recent-changes entry (spills oldest)
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-qwen38-max-launch-2026-08-04.md` — source summary

- [ ] **Update** `wiki/index.md` — update the `models/qwen-3-8` line to reflect full launch

## Page drafts

### wiki/models/qwen-3-8.md (updated)

```md
---
title: Qwen 3.8
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [alibaba, open-weights]
as_of: 2026-08-04
sources: [alibaba-qwen38-preview-2026-07-20, ainews-china-policy-openweight-2026-07-21, ainews-qwen38-max-launch-2026-08-04]
---

# Qwen 3.8

Alibaba's flagship after Qwen 3.7. Entered live preview 2026-07-20 and shipped as a full launch on 2026-08-04 as Qwen3.8-Max, with open weights promised "next week" for both Qwen3.8-Max and a smaller companion, Qwen3.8-27B.

## Current status (as of 2026-08-04)

- Qwen3.8-Max: 2.4T total parameters, ~95B active per token (third-party estimate, ~4% activation ratio); 1M context; API priced at $2/M input, $6/M output, $0.25/M cached tokens
- Open weights promised "next week" for both Qwen3.8-Max and a companion Qwen3.8-27B
- Frontend Code Arena: #4 overall at 1,668 Elo, behind only Claude Opus 5 (1,705) and Kimi K3 (1,676)
- Vals AI Index: 66.1, matching Claude Opus 4.7 at roughly 2.3x lower cost per test; SWE-bench 87.3% (ahead of GPT-5.5 and GLM-5.2, behind Claude Opus 4.8's 89.2%); Terminal-Bench 2.1 at 67.4, up from 57.5 for Qwen 3.7 Max about two and a half months earlier
- Vision Arena: #2 at 1,305, 13 points behind Claude Fable 5
- Licensing: terms reportedly restrict use or download in the US, EU, UK, and Korea — a similar complaint was raised about MiniMax H3 the same week, raising the question of how "open" a geographically-restricted release really is for Western teams

## Why it matters

Succeeds [Qwen 3.7](qwen-3-7.md) as Alibaba's flagship, moving from preview to a real open-weight-committed launch just over two weeks after Kimi K3. If the license restrictions hold as reported, this complicates the "open weights as sovereignty infrastructure" argument tracked on [Open-weight momentum broadens](../trends/open-weight-momentum-broadens.md) — the weights may not be legally usable by the Western teams that argument targets.

## Caveats

- Active-parameter count (~95B) and some benchmark framing come from third-party summaries (ZhihuFrontier), not Alibaba's own spec sheet
- Weights not yet released at time of writing — "next week" is Alibaba's stated timeline, not a confirmed date
- The license-restriction claim comes from a single X post (@ostrisai) reacting to the terms; no clarifying statement from Alibaba appears in the source coverage

## Recent changes

- [2026-08-04] Full launch as Qwen3.8-Max: 2.4T/~95B active, real benchmarks (Frontend Code Arena #4, SWE-bench 87.3%, Terminal-Bench 2.1 67.4), open weights promised "next week" alongside a Qwen3.8-27B sibling; license reportedly restricts use/download in US/EU/UK/Korea
- [2026-07-21] Third-party roundup reports 2.4T parameters, native video understanding, still inconsistent on long-horizon tasks
- [2026-07-20] Alibaba puts Qwen3.8-Max into live preview, claiming near-Fable-5 capability

## Sources

- [Superhuman — Alibaba teases new frontier model](../sources/newsletters/alibaba-qwen38-preview-2026-07-20.md)
- [AINews — Open-weight competition, Chinese model policy, geopolitics of AI](../sources/newsletters/ainews-china-policy-openweight-2026-07-21.md)
- [AINews — Qwen 3.8 Max (2.4T) and 27B ship](../sources/newsletters/ainews-qwen38-max-launch-2026-08-04.md)
```

### wiki/state-of/models.md (updated)

Add to `### Open-weight models`, after the Laguna S 2.1 line:

```md
- [Qwen 3.8](../models/qwen-3-8.md) — Alibaba; 2.4T/~95B-active MoE; #4 Frontend Code Arena (1,668 Elo); SWE-bench 87.3%, Terminal-Bench 2.1 67.4; open weights promised for Max + 27B sibling; license reportedly restricts use in US/EU/UK/Korea *(as of 2026-08-04)*
```

Insert into `## Recent changes` as the newest entry (this is a delta — the live list determines what, if anything, spills to keep the section at its 10-entry cap):

```md
- [2026-08-04] Qwen3.8-Max (Alibaba, 2.4T/~95B active) added to Open-weight models: #4 Frontend Code Arena, SWE-bench 87.3%, Terminal-Bench 2.1 67.4; open weights promised for Max + a 27B sibling; license reportedly restricts use in US/EU/UK/Korea.
```

Add `ainews-qwen38-max-launch-2026-08-04` to the frontmatter `sources:` list.

### wiki/trends/open-weight-momentum-broadens.md (updated)

Replace the existing `**Qwen3.8-Max-Preview (July 2026):**` bullet under `## Current signal` with:

```md
- **Qwen 3.8 Max ships in full (August 2026):** Alibaba's flagship moved from preview to launch on 2026-08-04 — 2.4T total/~95B active parameters, strong third-party benchmarks (#4 Frontend Code Arena, SWE-bench 87.3%, Terminal-Bench 2.1 67.4, up from 57.5 two and a half months earlier), and an open-weight commitment for both the Max and a companion Qwen3.8-27B, due "next week." The clearest complication: the license reportedly restricts use or download in the US, EU, UK, and Korea — the same week a similar restriction was flagged on MiniMax H3 — a concrete instance of the "how open is open-weight" question this trend has tracked since the Fable-ban sovereignty framing above.
```

Insert into `## Recent changes` as the newest entry (delta; live list determines what spills):

```md
- [2026-08-04] Qwen 3.8 Max ships in full (2.4T/~95B active): strong third-party benchmarks, open weights promised for Max + a 27B sibling — but license reportedly restricts use/download in US/EU/UK/Korea, echoing a similar MiniMax H3 complaint.
```

Add `ainews-qwen38-max-launch-2026-08-04` to the frontmatter `sources:` list, and add the following line under `## Sources`:

```md
- [AINews — Qwen 3.8 Max (2.4T) and 27B ship](../sources/newsletters/ainews-qwen38-max-launch-2026-08-04.md)
```

### wiki/sources/newsletters/ainews-qwen38-max-launch-2026-08-04.md (new)

```md
---
title: AINews — Qwen 3.8 Max (2.4T) and 27B ship
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-04-ainews-qwen-38-max24t-and-27b-new-open-weig.md
url: https://www.latent.space/p/ainews-qwen-38-max24t-and-27b-new
published: 2026-08-04
ingested: 2026-09-07
domains: [models]
---

# AINews — Qwen 3.8 Max (2.4T) and 27B ship

AINews recap of Alibaba's Qwen3.8-Max full launch: 2.4T total / ~95B active parameters, 1M context, $2/$6 per M token pricing, open weights promised "next week" for both Max and a companion Qwen3.8-27B. Covers third-party benchmark placements (Frontend Code Arena #4, Vals AI Index 66.1, SWE-bench 87.3%, Terminal-Bench 2.1 67.4), the strategic read (Alibaba choosing ecosystem influence over exclusivity as DeepSeek, Kimi, and other Chinese open models weaken the case for keeping top-tier systems API-only), and licensing pushback (reported US/EU/UK/Korea use restrictions, echoing a similar MiniMax H3 complaint).

## Influenced pages

- [models/qwen-3-8](../../models/qwen-3-8.md) — full-launch update: real benchmarks, pricing, Qwen3.8-27B sibling, licensing caveat
- [state-of/models](../../state-of/models.md) — added to Open-weight models subcategory
- [trends/open-weight-momentum-broadens](../../trends/open-weight-momentum-broadens.md) — Current-signal bullet updated from preview to full launch; licensing-restriction pattern noted

## Key claims extracted

- Qwen3.8-Max: 2.4T total parameters, ~95B active (third-party estimate), 1M context
- API pricing: $2.00/M input, $6.00/M output, $0.25/M cached tokens
- Open weights promised "next week" for Qwen3.8-Max and Qwen3.8-27B
- Frontend Code Arena #4 overall (1,668 Elo), behind Claude Opus 5 (1,705) and Kimi K3 (1,676)
- Vals AI Index 66.1, matching Claude Opus 4.7 at ~2.3x lower cost per test
- SWE-bench 87.3%, Terminal-Bench 2.1 67.4 (up from 57.5 for Qwen 3.7 Max)
- License reportedly restricts use/download in US, EU, UK, and Korea (per @ostrisai)
```

### wiki/index.md (updated)

Replace the existing `models/qwen-3-8` line with:

```md
- [models/qwen-3-8](models/qwen-3-8.md) — Alibaba's flagship; Qwen3.8-Max ships in full at 2.4T/~95B active; #4 Frontend Code Arena; open weights promised for Max + 27B sibling; license reportedly restricts US/EU/UK/Korea *(as_of: 2026-08-04)*
```

## Open questions

- None beyond the sourcing caveats noted above.
