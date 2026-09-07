---
type: proposal
source: raw/newsletters/2026-07-25-ainews-claude-opus-5-fable-level-performance-at.md
status: pending
created: 2026-09-06
---

# Proposal: Claude Opus 5 launches — strong on paper, rough in practice

## Summary

### The source

Anthropic shipped Claude Opus 5 in a Friday release (2026-07-24), and five sources tell the story from different angles. AINews's launch recap (2026-07-25) leads with the benchmark headline: Epoch's Capabilities Index puts Opus 5 at 159, just one point behind Fable 5's 161, while the two tie exactly on SWE-ECI (software-engineering capability) at 161 — Opus 5 matching Fable on coding at roughly half Fable's price. Community reaction split immediately: some called the ECI result "incredibly underrated" given how much better the model felt in practice, while a separate thread flagged an odd inconsistency where Opus 5 scored better at medium reasoning effort than at high effort on FrontierCode, unlike its usual pattern of improving with more compute.

Every's practitioner accounts (a "Vibe Check" preview on 2026-07-24, and a fuller follow-up called "Taming Opus 5" on 2026-07-28) tell a rougher story. In its first week at Every, Opus 5 argued with instructions, stopped before finishing work, and fought the skills and plugins the team had built for earlier Claude models — until they deleted those instructions, at which point it "sometimes got dramatically better," producing strong software and rigorous writing with much less process. By the following Monday, the wider Every team converged on a working pattern: give Opus 5 a full brief up front, leave it alone, and judge the finished artifact rather than its narration — a recommendation Anthropic's own prompting guide independently makes. The team's overall verdict: Opus 5 doesn't reach Fable 5's ceiling, and it's harder to live with day-to-day than GPT-5.6 Sol, but it wins clearly on hard coding and debugging grind. A later AINews roundup (2026-07-28) adds the Arena numbers: #1 on Frontend Code Arena and Text Arena, and a WeirdML score roughly tied with Fable 5's top tier — alongside several developers publicly reporting overcomplication, breakage, and poor stopping behavior in real use, a gap between leaderboard placement and production experience AINews called out directly.

### What changes

The wiki currently treats Claude Opus 4.8 as Anthropic's current accessible flagship on its own page and as a leader line on State of Models. This is a straightforward supersession, plus the addition of a well-documented practitioner account of how to actually prompt the new model.

- **New page `models/claude-opus-5.md`** carries the launch numbers (ECI 159, SWE-ECI 161, Arena #1 placements), the practitioner-reported quirks (argues with instructions, over-verbose, needs a full-brief prompting style), and the team verdict against Fable 5 and GPT-5.6 Sol.
- **Claude Opus 4.8** is archived in full to `wiki/history/models/claude-opus-4-8.md`, unchanged, and removed from `wiki/index.md`.
- **State of Models** swaps the Opus 4.8 leader line for Opus 5 in the Frontier models subcategory, and its page date moves to 28 July (the newest source-backed claim, the practitioner-reception update). The GLM-5.2 Recent-changes entry (23 June), currently the oldest on the page at its 10-entry cap, spills to `wiki/history/state-of/models.md`.
- **Two benchmark leaderboards** (`benchmarks/swe-bench.md`, `benchmarks/terminal-bench.md`) each carry an Opus 4.8 row that links to the live model page; since that page is moving to history, both rows are repointed to the archived path and relabeled historical, matching how Composer 2 and Kimi K2.6 are already shown on those same tables. No score changes — this is a mechanical link fix, not a new data point.
- Three new source pages, one per newsletter used (AINews launch recap, Every's Vibe Check preview, Every's Taming Opus 5 follow-up).

### What to weigh

Both Every "Vibe Check" emails are paywalled previews — the underlying full review was not fetched, so the practitioner-quirks material here comes from the free teaser paragraphs and the fuller "Taming Opus 5" follow-up email, not the complete essay. The two vibe-check emails are also near-duplicate resends of the same preview (same content, different final paragraph); only the fuller one is used as a source to avoid a near-empty duplicate source page. Nothing else here is a judgment call beyond ordinary sourcing.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/models/claude-opus-5.md` — new current-flagship page, supersedes Opus 4.8
    > See draft below

- [ ] **Spill** `wiki/models/claude-opus-4-8.md` → `wiki/history/models/claude-opus-4-8.md` — moved verbatim, no content changes; removed from `wiki/index.md`

- [ ] **Update** `wiki/state-of/models.md` — replace the Opus 4.8 leader line with Opus 5, bump page `as_of` to 2026-07-28, add one Recent-changes entry, spill the oldest (2026-06-23 GLM-5.2) entry to history
    > See draft below

- [ ] **Update** `wiki/benchmarks/swe-bench.md` — repoint the Opus 4.8 leaderboard row to the archived page path, relabel historical
    > See draft below

- [ ] **Update** `wiki/benchmarks/terminal-bench.md` — repoint the Opus 4.8 leaderboard row to the archived page path, relabel historical
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-claude-opus-5-launch-2026-07-25.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-opus-5-2026-07-24.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-taming-opus-5-2026-07-28.md` — source summary

## Page drafts

### wiki/models/claude-opus-5.md (new)

````md
---
title: Claude Opus 5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-07-28
sources: [ainews-claude-opus-5-launch-2026-07-25, every-vibe-check-opus-5-2026-07-24, every-taming-opus-5-2026-07-28]
---

# Claude Opus 5

Anthropic's new flagship, launched 2026-07-24, superseding [Claude Opus 4.8](../history/models/claude-opus-4-8.md). Epoch's Capabilities Index puts it just behind Fable 5 (159 vs. 161) while tying Fable exactly on software-engineering capability (SWE-ECI 161 for both), at roughly half Fable's price. Practitioner reports are more divided than the benchmarks suggest: strong on hard coding and debugging grind, but harder to manage day-to-day than either Fable 5 or GPT-5.6 Sol.

## Current status (as of 2026-07-28)

- Epoch Capabilities Index: 159 (vs. Fable 5's 161); SWE-ECI: 161, tied with Fable 5
- Arena: #1 Frontend Code Arena and #1 Text Arena (Opus 5 Max); WeirdML 91.6%/91.8% (high/max), roughly tied with Fable 5 Max
- Every's week-long practitioner review: brilliant in flashes, but argues with instructions, narrates excessively, and stops before work is finished under the same management style that worked for earlier Claude models
- Works best given a full brief up front and left alone rather than managed step-by-step — Anthropic's own prompting guide makes the same recommendation
- Team verdict: doesn't reach Fable 5's ceiling and is less easy to live with day-to-day than GPT-5.6 Sol, but wins clearly on hard coding/debugging grind

## Strengths

- Hard coding and debugging tasks that reward sustained, unsupervised effort
- Strong when given a complete upfront brief and evaluated on the finished artifact rather than managed turn-by-turn

## Weaknesses / caveats

- Prickly and over-verbose in conversation; several practitioners reported it arguing with instructions and adopting a judgmental tone
- Needs a real prompting-style adjustment from earlier Claude models — skills/plugins built for Opus 4.8 and earlier reportedly worked against it until removed
- Several developers reported frustrating real-world behavior (overcomplication, breakage, poor stopping behavior) despite strong leaderboard numbers — a public-eval-vs-production gap AINews called out directly
- A FrontierCode anomaly: at least one evaluator saw better results at medium effort than high effort, unlike the model's usual pattern of improving with more inference-time effort

## Recent changes

- [2026-07-28] Practitioner reception update: Every's team-wide testing confirms the model's unruliness but converges on a fix — give it a complete upfront brief, let it run, then evaluate the finished artifact rather than its narration
- [2026-07-24] Launched: ECI 159, SWE-ECI 161 (tied with Fable 5), roughly half Fable 5's price; supersedes Claude Opus 4.8

## Sources

- [AINews — Claude Opus 5: Fable-level performance at Opus price](../sources/newsletters/ainews-claude-opus-5-launch-2026-07-25.md)
- [Every — Vibe Check: Claude Opus 5 is brilliant in flashes, frustrating in practice](../sources/newsletters/every-vibe-check-opus-5-2026-07-24.md)
- [Every — Taming Opus 5](../sources/newsletters/every-taming-opus-5-2026-07-28.md)
````

### wiki/history/models/claude-opus-4-8.md (new — moved verbatim)

Move the current `wiki/models/claude-opus-4-8.md` file to this path with no content changes.

### wiki/state-of/models.md (updated)

Frontmatter: bump `as_of: 2026-07-17` → `as_of: 2026-07-28`; append `ainews-claude-opus-5-launch-2026-07-25` and `every-taming-opus-5-2026-07-28` to the `sources:` list.

Frontier models subcategory — replace this line:
```
- [Claude Opus 4.8](../models/claude-opus-4-8.md) — Anthropic; current accessible flagship after 4.7; AINews cites 1M context, SWE-Bench Pro 69.2%, APEX-SWE 45.3% Pass@1, GDPval-AA 1890 Elo; Dynamic Workflows in Claude Code and Figma MCP bidirectional code-to-design/design-to-code loop; stronger than 4.7 but still cost/turn-count sensitive vs GPT-5.5 in some workloads *(as of 2026-06-03)*
```
with:
```
- [Claude Opus 5](../models/claude-opus-5.md) — Anthropic; current flagship after 4.8; Epoch Capabilities Index 159 (vs. Fable 5's 161), SWE-ECI 161 tied with Fable 5, roughly half Fable's price; Arena #1 Frontend Code Arena and Text Arena; practitioner reports call it prickly and over-verbose day-to-day versus GPT-5.6 Sol, though strong on hard coding/debugging grind *(as of 2026-07-28)*
```

Recent changes — insert as the newest entry (above the 2026-07-17 Kimi K3 entry):
```
- [2026-07-24] Claude Opus 5 launched, superseding Opus 4.8: Epoch Capabilities Index 159 (vs Fable 5's 161), SWE-ECI 161 tied with Fable 5; Arena #1 Frontend Code Arena/Text Arena; practitioner reports (Every) call it prickly and harder to manage day-to-day than Fable 5 or GPT-5.6 Sol despite strong benchmark placement.
```
This pushes the list to 11 entries; spill the oldest (`- [2026-06-23] GLM-5.2 follow-on coverage adds frontier-adjacent open-weight signal: strong AA-Briefcase cost/performance, broad hosted-provider adoption, and coding-agent harness uptake.`) to `wiki/history/state-of/models.md` under a new `## Archived from current page on 2026-09-06` header.

### wiki/benchmarks/swe-bench.md (updated)

Replace this leaderboard row:
```
| [Claude Opus 4.8](../models/claude-opus-4-8.md) | Pro | 69.2% | 2026-06-04 |
```
with:
```
| [Claude Opus 4.8](../history/models/claude-opus-4-8.md) (historical, superseded by [Claude Opus 5](../models/claude-opus-5.md)) | Pro | 69.2% | 2026-06-04 |
```
Add to Recent changes: `- [2026-09-06] Repointed Claude Opus 4.8 to its archived page after Claude Opus 5 superseded it; score unchanged, link/label fix only.`

### wiki/benchmarks/terminal-bench.md (updated)

Replace this leaderboard row:
```
| [Claude Opus 4.8](../models/claude-opus-4-8.md) | Hard | gains reported; no exact score published | 2026-06-04 |
```
with:
```
| [Claude Opus 4.8](../history/models/claude-opus-4-8.md) (historical, superseded by [Claude Opus 5](../models/claude-opus-5.md)) | Hard | gains reported; no exact score published | 2026-06-04 |
```
Add to Recent changes (create the section immediately above `## Sources` if it doesn't already exist): `- [2026-09-06] Repointed Claude Opus 4.8 to its archived page after Claude Opus 5 superseded it; score unchanged, link/label fix only.`

### wiki/sources/newsletters/ainews-claude-opus-5-launch-2026-07-25.md (new)

```md
---
title: "AINews — Claude Opus 5: Fable-level performance at Opus price"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-25-ainews-claude-opus-5-fable-level-performance-at.md
url: https://www.latent.space/p/ainews-claude-opus-5-fable-level
published: 2026-07-25
ingested: 2026-09-06
domains: [models, coding]
---

# AINews — Claude Opus 5: Fable-level performance at Opus price

AINews's launch-day recap of Claude Opus 5, aggregating Twitter/Reddit reaction. Leads with Epoch's benchmark numbers (ECI 159 vs. Fable 5's 161, SWE-ECI 161 tied with Fable), notes community pushback that the score understates real-world gains, and flags a FrontierCode anomaly where medium reasoning effort outscored high effort.

## Influenced pages

- [Claude Opus 5](../../models/claude-opus-5.md) — new page; launch benchmark numbers
- [State of Models](../../state-of/models.md) — leader-line swap from Opus 4.8

## Key claims extracted

- Claude Opus 5 launched 2026-07-24 (Friday release)
- Epoch Capabilities Index: Opus 5 = 159, Fable 5 = 161
- SWE-ECI: Opus 5 = 161, tied with Fable 5
- FrontierCode: medium reasoning effort scored higher than high effort for at least one evaluator, an inconsistency with the usual pattern
```

### wiki/sources/newsletters/every-vibe-check-opus-5-2026-07-24.md (new)

```md
---
title: "Every — Vibe Check: Claude Opus 5 is brilliant in flashes, frustrating in practice"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-24-vibe-check-claude-opus-5-is-brilliant-in-flashes-1.md
url: https://every.to/vibe-check/opus-5
published: 2026-07-24
ingested: 2026-09-06
domains: [models, coding]
---

# Every — Vibe Check: Claude Opus 5 is brilliant in flashes, frustrating in practice

Paywalled-preview email announcing Every's full Opus 5 review. The free teaser: Opus 5 argued with instructions, stopped before finishing work, and fought skills built for earlier Claude models in its first week — until the team deleted those instructions, after which it "sometimes got dramatically better." Verdict trailed in the teaser: doesn't reach Fable 5's ceiling, less easy to use day-to-day than GPT-5.6 Sol. The full review itself was not fetched (paywalled); a second, near-duplicate email resend of this same preview (`raw/newsletters/2026-07-24-vibe-check-claude-opus-5-is-brilliant-in-flashes.md`) was not separately ingested.

## Influenced pages

- [Claude Opus 5](../../models/claude-opus-5.md) — practitioner-quirks framing, team verdict vs. Fable 5 and GPT-5.6 Sol

## Key claims extracted

- Opus 5 argued with instructions and stopped before work was finished under process built for earlier Claude models
- Removing that process sometimes made results "dramatically better"
- Team verdict: doesn't reach Fable 5's ceiling; less easy to use day-to-day than GPT-5.6 Sol
```

### wiki/sources/newsletters/every-taming-opus-5-2026-07-28.md (new)

```md
---
title: "Every — Taming Opus 5"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-28-taming-opus-5.md
url: https://every.to/context-window/taming-opus-5
published: 2026-07-28
ingested: 2026-09-06
domains: [models, coding]
---

# Every — Taming Opus 5

Follow-up to Every's Vibe Check, covering the wider team's weekend experience with Opus 5. Confirms the model's unruliness (needs heavy management to stay concise, adopts a prickly/judgmental tone) but converges on a working pattern: give it a complete brief, walk away, and evaluate the finished artifact rather than its step-by-step narration — the same recommendation as Anthropic's own prompting guide for Opus 5.

## Influenced pages

- [Claude Opus 5](../../models/claude-opus-5.md) — prompting guidance, practitioner-reception Recent-changes entry

## Key claims extracted

- Opus 5 needs more management/repeated prompting to stay concise than Fable 5 or Opus 4.8
- Working pattern that got good results: give a substantial job with a clear finish line, then leave it alone; evaluate the output, not the narration
- Anthropic's own prompting guide for Opus 5 recommends the same full-brief-then-run approach
```

## Open questions

- The full Every "Vibe Check" review is paywalled and was not fetched — if you have access, the full essay likely has more specific coding/writing/agent test results than the free teaser captured here.
