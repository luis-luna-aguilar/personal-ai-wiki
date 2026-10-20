---
type: proposal
source: raw/newsletters/2026-09-23-ainews-claude-opus-55-the-new-default-model-fo.md
sources:
  - raw/newsletters/2026-09-23-ainews-claude-opus-55-the-new-default-model-fo.md
  - raw/newsletters/2026-09-24-ainews-meta-connect-2026-muse-glasses-voice-v.md
  - raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
  - raw/newsletters/2026-09-22-vibe-check-opus-55-is-pulling-our-codex-converts.md
  - raw/newsletters/2026-09-27-opus-55-and-sol-split-the-team.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Claude Opus 5.5 — launch date, independent evals, hands-on verdict

## Summary

### In short

Opus 5.5's value claim survives independent testing only at default effort: it tops most third-party coding leaderboards, but its extra token use cancels the price cut at max effort. Artificial Analysis ranks it #1 on its Coding Agent Index (66) yet measures $5.98 per task at max effort against Opus 5's $5.86. The proposal dates the Opus 5.5 page to its 22 September launch, adds independent evals, a cost-and-effort caveat and Every's verdict, and touches State of Models, the routing page and the index. Reasons to hesitate: page dates move backwards from an ingest-date fallback, and both Every reviews were read as free previews only.

[[#Open questions|Open questions: none.]]

### The source

Anthropic launched Claude Opus 5.5 on Tuesday 22 September 2026, about an hour before OpenAI shipped GPT-6 Sol and Luna. AINews's launch-day issue (23 September) collects the reaction. Anthropic made Opus 5.5 the default in Claude Code and the Claude app at medium effort. The independent numbers are strong. The model is #1 on the Vals Index and the Vals RSI Index, sets a new top score on CursorBench (57.8%) and leads FrontierCode 1.1 Extended (65.3%). It is second on FrontierSWE (62.3%, behind GPT-6 Astra's 65.5%). Later issues add #1 on Artificial Analysis's Coding Agent Index (66, up from Opus 5's 60) and #1 on SimpleBench (88.4%).

The same issues complicate the "40% cheaper" headline. The list price fell 20%, to $4/$20 per million tokens, but the model uses far more tokens: Artificial Analysis measures $5.98 per task at max effort against Opus 5's $5.86. So the saving is real only at the default medium effort. Higher effort can also make results worse. On FrontierCode, a benchmark that penalizes unnecessary changes, xhigh costs 2.8 times as much as medium and scores 3.2 points lower. On Terminal-Bench-Science, the score peaks at xhigh and drops at max. ProgramBench's author adds that Anthropic's near-100% figure comes from 166 of 200 tasks and measures average test pass rate, not full completion. The new safeguards also over-triggered at first, sending some ordinary requests to the fallback model.

Every's Vibe Check (22 September, read as the free preview plus the 27 September recap) found Fable 5.1-level product and design work at about 60% less per token. The model became Kieran Klaassen's daily driver and pulled some Codex converts back. Two problems remain: it buries the main point in its prose, and it runs for hours unless you give it a budget. A viral animated-video tweet in the same signal is video-only and is skipped.

### What changes

The Opus 5.5 page was written today from Anthropic's undated launch post, so it has no launch date, no independent evals and an `as_of` set to the ingest date.

- **Claude Opus 5.5** gains the launch date and an independent-evals bullet. A new "Cost and effort caveats" section covers the max-effort cost parity, the effort curve and the ProgramBench subset. Every's verdict joins the early-user evidence. The placeholder Recent-changes entry is replaced by a dated launch entry, and one entry for the evals is added. Page date moves from 20 October back to 27 September, the newest real claim. This is the agreed exception for fallback dates.
- **State of Models**: the Opus 5.5 leader line gains the launch date and the AA Coding Agent Index lead, dated 27 September.
- **Cost-aware AI task routing** gains one short bullet: a lower list price does not mean a cheaper task, so measure cost per task at the effort you will run. One Recent-changes entry is added.
- **Index**, the **Opus 5 history page** ("superseded October 2026" becomes September) and the **existing launch source page** (gains `published: 2026-09-22`) get date fixes.
- Five new source pages, one per newsletter story.

### What to weigh

Moving `as_of` backwards breaks the usual rule. The original date was the ingest date, used only because the launch post carried none. The two Every pieces are paywalled previews, so the verdict comes from their summaries, not the full review.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/claude-opus-5-5.md` — launch date, independent evals, new "Cost and effort caveats" section, Every verdict; `as_of` 2026-10-20 → 2026-09-27 (fallback-date correction); sources merged. Recent changes: replaces the one placeholder entry dated 2026-10-20 with a launch entry dated 2026-09-22, and adds one entry dated 2026-09-27 (2 entries, no spill).
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — Opus 5.5 leader line only (no Recent-changes entry, so no spill)
    > **Before:** `- [Claude Opus 5.5](../models/claude-opus-5-5.md) — Anthropic flagship, supersedes Opus 5; Fable 5.1-level on most work per Anthropic, Terminal-Bench 4.0 66.4%, GDPval-AA 1846, about 40% cheaper than Opus 5 ($4/$20) *(as of 2026-10-20)*`
    > **After:** `- [Claude Opus 5.5](../models/claude-opus-5-5.md) — Anthropic flagship, launched 2026-09-22, supersedes Opus 5; Fable 5.1-level on most work per Anthropic; #1 on the Vals Index and AA Coding Agent Index (66); $4/$20, but the "40% cheaper" holds only at default effort *(as of 2026-09-27)*`

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — adds one bullet to "Cost variance and budgeting tradeoffs"; adds one Recent-changes entry dated 2026-09-23 (5 → 6 entries, no spill); merges 2 source ids and 2 Sources links. `as_of` stays 2026-10-19.
    > See draft below

- [ ] **Update** `wiki/index.md` — Opus 5.5 line
    > **Before:** `- [models/claude-opus-5-5](models/claude-opus-5-5.md) — Anthropic current flagship, supersedes Opus 5; Fable 5.1-level on most work per Anthropic at about 40% lower cost than Opus 5; clearer writing; Fable 5.1-class safeguards *(as_of: 2026-10-20)*`
    > **After:** `- [models/claude-opus-5-5](models/claude-opus-5-5.md) — Anthropic current flagship (launched 2026-09-22), supersedes Opus 5; #1 Vals Index and AA Coding Agent Index; ~40% cheaper than Opus 5 at default effort, not at max; Fable 5.1-class safeguards *(as_of: 2026-09-27)*`

- [ ] **Update** `wiki/history/models/claude-opus-5.md` — supersession line: "October 2026" → "2026-09-22"

- [ ] **Update** `wiki/sources/articles/claude-opus-5-5-launch.md` — add `published: 2026-09-22`; correct the "no publication date" sentence

- [ ] **Create** `wiki/sources/newsletters/ainews-claude-opus-5-5-launch-2026-09-23.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-opus-5-5-coding-agent-index-2026-09-24.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-opus-5-5-simplebench-effort-2026-09-25.md`
- [ ] **Create** `wiki/sources/newsletters/every-vibe-check-opus-5-5-2026-09-22.md`
- [ ] **Create** `wiki/sources/newsletters/every-recap-opus-5-5-verdict-2026-09-27.md`

## Page drafts

### wiki/models/claude-opus-5-5.md (updated)

Full page; unchanged lines are carried over from the live page.

```
---
title: Claude Opus 5.5
type: model
domains: [models, coding]
subcategory: frontier-model
tags: [anthropic, closed-source]
as_of: 2026-09-27
sources: [claude-opus-5-5-launch, ainews-claude-opus-5-5-launch-2026-09-23, ainews-opus-5-5-coding-agent-index-2026-09-24, ainews-opus-5-5-simplebench-effort-2026-09-25, every-vibe-check-opus-5-5-2026-09-22, every-recap-opus-5-5-verdict-2026-09-27]
---

# Claude Opus 5.5

Anthropic's current flagship and the first model in the Claude 5.5 family, launched 2026-09-22, superseding [Claude Opus 5](../history/models/claude-opus-5.md). Anthropic says it performs at the level of [Claude Fable 5.1](claude-fable-5-1.md) on most work at about 40% lower cost than Opus 5, and pitches it at long, sprawling coding jobs and knowledge work. It is Anthropic's first release since its call for "pacing the frontier." Independent evals put it at or near the top of most coding leaderboards, though the cost saving holds only at default effort.

## Current status (as of 2026-09-27)

- Available on the Claude Platform as `claude-opus-5-5`, and on AWS, Google Cloud and Microsoft Azure; thinking can no longer be switched off. Default model in Claude Code and the Claude app, at medium effort.
- Pricing per 1M tokens: $4 input, $20 output, $5 cache writes, $0.20 cache reads (Opus 5: $5 / $25 / $6.25 / $0.50). Fast mode (up to 2.5x speed) costs $8 / $40. Output is 30%+ faster than Opus 5.
- Launch benchmarks (Opus 5.5 / Fable 5.1 / Opus 5 / GPT-6 Astra): Terminal-Bench 4.0 66.4% / 55.8% / 52.3% / 57.9%; FrontierCode v1.1 54.4% / 50.3% / 48.0% / 53.3%; GDPval-AA v2.1 1846 / 1735 / 1708 / 1542; OSWorld 2.1 81.8% / 80.7% / 74.0% / —. Anthropic says the real-world gap to Fable 5.1 is narrower than these scores suggest.
- Independent evals: #1 on the Vals Index and Vals RSI Index; #1 on Artificial Analysis's Coding Agent Index at 66 (Opus 5: 60; AA measures Terminal-Bench 4.0 at 63.1%); CursorBench 57.8% (new top); FrontierCode 1.1 Extended 65.3% (#1); FrontierSWE 62.3% (#2, behind GPT-6 Astra's 65.5%); SimpleBench 88.4% (#1).
- Writing is clearer and puts key information first, which addresses the main complaint about Opus 5.
- Ships with Fable 5.1-class safeguards: cyber, biology and anti-distillation classifiers that fall back transparently (most cyber tasks route to Opus 4.8). Early users hit over-triggered fallbacks on ordinary requests; Anthropic says it is working to reduce incorrect flags. Anthropic reports its best-ever automated alignment-audit scores and ~85% fewer containment-boundary attempts than Opus 5, but notes the model often suspects it is being evaluated.

## Cost and effort caveats

- **Cheaper per token, not always per task.** Opus 5.5 uses many more tokens than Opus 5. Artificial Analysis measures $5.98 per Intelligence Index task at max effort against Opus 5's $5.86: extra tokens add about 80%, which the 20% price cut and cheaper cache reads only just offset. The "40% cheaper" claim holds at the default medium effort. On AA's Coding Agent Index it averages 15.6M tokens and $13.04 per task.
- **More effort can score lower.** On FrontierCode, which penalizes unnecessary changes, xhigh costs about 2.8x medium for a 3.2-point lower score. On Terminal-Bench-Science it climbs from 24% at low effort to 62% at xhigh, then falls to 59% at max.
- **ProgramBench subset.** Anthropic's near-100% figure covers 166 of 200 tasks and reports average test pass rate; ProgramBench itself scores full task completion.

## Evidence from early users

- Customers report the same quality as Opus 5 in roughly half the turns or tokens (Optiver, Lovable, Kiro); Deloitte says low-effort Opus 5.5 caught 72% of known code-review bugs against high-effort Opus 5's 56%.
- Every's Vibe Check: Fable 5.1-level product and design work at about 60% less per token than Fable. It became Kieran Klaassen's daily driver and pulled some Codex converts back; Dan Shipper still prefers Codex for knowledge work and writing. It still buries the main point in prose and runs for hours unless given a budget and a stopping point.
- Strong at visual work built from code: users shared videos, animations and Blender scenes generated entirely from code, including a one-shot ~80-minute Claude Code run that produced an animated explainer for about $20 of Opus usage.

## Recent changes

- [2026-09-27] Independent evals and hands-on reviews added: #1 on the Vals Index and AA Coding Agent Index (66), CursorBench 57.8%; AA finds the per-task saving over Opus 5 disappears at max effort; Every reports Fable-level design work but long, unbudgeted runs.
- [2026-09-22] Launched as the first Claude 5.5 model, superseding Opus 5; default in Claude Code and the Claude app at medium effort.

## Sources

- [Introducing Claude Opus 5.5](../sources/articles/claude-opus-5-5-launch.md)
- [AINews — Claude Opus 5.5 launch roundup](../sources/newsletters/ainews-claude-opus-5-5-launch-2026-09-23.md)
- [AINews — Opus 5.5 on the AA Coding Agent Index](../sources/newsletters/ainews-opus-5-5-coding-agent-index-2026-09-24.md)
- [AINews — Opus 5.5 SimpleBench and effort curve](../sources/newsletters/ainews-opus-5-5-simplebench-effort-2026-09-25.md)
- [Every — Vibe Check: Opus 5.5](../sources/newsletters/every-vibe-check-opus-5-5-2026-09-22.md)
- [Every — weekly recap: Opus 5.5 verdict](../sources/newsletters/every-recap-opus-5-5-verdict-2026-09-27.md)
```

### wiki/state-of/models.md (updated)

Only the Opus 5.5 line under "Frontier models" changes:

```
- [Claude Opus 5.5](../models/claude-opus-5-5.md) — Anthropic flagship, launched 2026-09-22, supersedes Opus 5; Fable 5.1-level on most work per Anthropic; #1 on the Vals Index and AA Coding Agent Index (66); $4/$20, but the "40% cheaper" holds only at default effort *(as of 2026-09-27)*
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter `sources:` — append `ainews-claude-opus-5-5-launch-2026-09-23, ainews-opus-5-5-simplebench-effort-2026-09-25` to the live list.

New bullet, appended at the end of `### Cost variance and budgeting tradeoffs`:

```
- **A lower list price is not a cheaper task.** Claude Opus 5.5 cut list prices 20% from Opus 5, but at max effort Artificial Analysis measures $5.98 per task against Opus 5's $5.86, because the newer model uses far more tokens; the advertised ~40% saving holds only at default effort. Higher effort can also lower quality: on FrontierCode, xhigh cost 2.8x medium for a 3.2-point lower score. Compare models on cost per completed task at the effort you will actually run. See [Claude Opus 5.5](../models/claude-opus-5-5.md).
```

`## Recent changes` — insert one entry above the existing 2026-07-08 entry (date order, newest first):

```
- [2026-09-23] Added Opus 5.5's list-price-vs-task-cost gap (max-effort cost per task no lower than Opus 5) to Cost variance and budgeting tradeoffs.
```

`## Sources` — append:

```
- [AINews — Claude Opus 5.5 launch roundup](../sources/newsletters/ainews-claude-opus-5-5-launch-2026-09-23.md)
- [AINews — Opus 5.5 SimpleBench and effort curve](../sources/newsletters/ainews-opus-5-5-simplebench-effort-2026-09-25.md)
```

### wiki/index.md (updated)

```
- [models/claude-opus-5-5](models/claude-opus-5-5.md) — Anthropic current flagship (launched 2026-09-22), supersedes Opus 5; #1 Vals Index and AA Coding Agent Index; ~40% cheaper than Opus 5 at default effort, not at max; Fable 5.1-class safeguards *(as_of: 2026-09-27)*
```

### wiki/history/models/claude-opus-5.md (updated)

Only the supersession line changes:

```
**Superseded by [Claude Opus 5.5](../../models/claude-opus-5-5.md), launched 2026-09-22.**
```

### wiki/sources/articles/claude-opus-5-5-launch.md (updated)

Frontmatter gains `published: 2026-09-22` (after `url:`). In the summary paragraph, replace the last two sentences ("The post carries no publication date; … The ingest date (2026-10-20) is used.") with:

```
The post itself carries no date; launch-day coverage (AINews, Every) dates the release to 2026-09-22, the same day as GPT-6 Sol and Luna, and Sonnet 5.5 and Haiku 5.5 followed, as the post said they would "in the coming weeks."
```

### wiki/sources/newsletters/ainews-claude-opus-5-5-launch-2026-09-23.md (new)

```
---
title: 'AINews — Claude Opus 5.5 launch roundup: independent evals, cost per task, safeguards'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-23-ainews-claude-opus-55-the-new-default-model-fo.md
url: https://www.latent.space/p/ainews-claude-opus-55-the-new-default
published: 2026-09-23
ingested: 2026-10-20
domains: [models, coding]
---

# AINews — Claude Opus 5.5 launch roundup

The launch-day issue covering Claude Opus 5.5 (released 2026-09-22, about an hour before GPT-6 Sol and Luna). It collects Anthropic's launch claims, third-party and partner evals, an Artificial Analysis cost-per-task breakdown, effort-scaling and ProgramBench caveats, the safeguard over-triggering complaints, and demos of visual work built from code. AINews switched its own pipeline to Opus 5.5 on the strength of its writing. This page covers the Opus 5.5 story only.

## Influenced pages
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — launch date, independent evals, cost and effort caveats, safeguard over-triggering
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — list price vs cost per task

## Key claims extracted
- Opus 5.5 launched 2026-09-22; default in Claude Code and the Claude app at medium effort
- #1 Vals Index and Vals RSI Index; CursorBench 57.8% (new top); FrontierCode 1.1 Extended 65.3% (#1); FrontierSWE 62.3% (#2 behind GPT-6 Astra 65.5%)
- List price cut 20% to $4/$20; AA: $5.98 per Intelligence Index task at max effort vs Opus 5's $5.86, so the "40% cheaper" claim applies at default medium effort
- On FrontierCode, xhigh effort costs ~2.8x medium for a 3.2-point lower score
- ProgramBench near-100% figure is from a 166/200 subset and uses average test pass rate
- First Opus with Fable 5.1-class safeguards; early over-triggered fallbacks reported
```

### wiki/sources/newsletters/ainews-opus-5-5-coding-agent-index-2026-09-24.md (new)

```
---
title: AINews — Opus 5.5 tops the Artificial Analysis Coding Agent Index
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-24-ainews-meta-connect-2026-muse-glasses-voice-v.md
published: 2026-09-24
ingested: 2026-10-20
domains: [models, coding]
---

# AINews — Opus 5.5 tops the Artificial Analysis Coding Agent Index

A short item in the 2026-09-24 issue (headlined on Meta Connect) reporting Artificial Analysis results for Claude Opus 5.5. This page covers the Opus 5.5 item only.

## Influenced pages
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — Coding Agent Index rank, tokens and cost per task

## Key claims extracted
- #1 on the AA Coding Agent Index at 66 (Opus 5: 60); Terminal-Bench 4.0 63.1%, DeepSWE v1.1 68.4%, SWE-Atlas-QnA 66.4%
- Cost per coding task rises to $13.04 at 15.6M tokens per task despite the lower list price
- Record 2631 Elo on a writing benchmark, though a max-effort run takes 17 minutes and $3.43 per script
```

### wiki/sources/newsletters/ainews-opus-5-5-simplebench-effort-2026-09-25.md (new)

```
---
title: AINews — Opus 5.5 SimpleBench lead, effort curve and code-built video
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
published: 2026-09-25
ingested: 2026-10-20
domains: [models, coding]
---

# AINews — Opus 5.5 SimpleBench lead, effort curve and code-built video

Items in the 2026-09-25 issue on Claude Opus 5.5: a SimpleBench lead, a vision ranking, a reasoning-effort curve on Terminal-Bench-Science, and Reddit threads on videos generated entirely from code. This page covers the Opus 5.5 items only.

## Influenced pages
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — SimpleBench, effort curve, code-built media
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — effort is not monotonic in quality

## Key claims extracted
- Opus 5.5 leads SimpleBench at 88.4%
- Terminal-Bench-Science: 24% at low effort, 62% at xhigh, 59% at max; Theo advises avoiding max
- One-shot autonomous Claude Code run produced a 30–60s animated explainer in ~1h20m for about $20 of Opus usage
```

### wiki/sources/newsletters/every-vibe-check-opus-5-5-2026-09-22.md (new)

```
---
title: 'Every — Vibe Check: Opus 5.5 Is Pulling Our Codex Converts Back to Claude'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-22-vibe-check-opus-55-is-pulling-our-codex-converts.md
url: https://every.to/vibe-check/vibe-check-opus-5-5-is-pulling-our-codex-converts-back-to-claude
published: 2026-09-22
ingested: 2026-10-20
domains: [models, coding]
---

# Every — Vibe Check: Opus 5.5 Is Pulling Our Codex Converts Back to Claude

Free preview of Every's paywalled Opus 5.5 review by Katie Parrott; the full review was not read. The team tested coding, design, writing and consulting work and found Fable 5.1-level performance at roughly 60% less per token, with a habit of doing extra credit while missing the assignment.

## Influenced pages
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — hands-on verdict

## Key claims extracted
- Kieran Klaassen replaced Fable 5.1 with Opus 5.5 as his daily driver; Mike Taylor and Tyler Nishida are reconsidering moves to Codex; Dan Shipper still prefers Codex for knowledge work and writing
- Most readable prose Every has measured, yet it buried ideas that GPT-6 Astra put first
- Unreliable finisher when time or precision is tight; one app burned 5.9M tokens before its core screens threw errors
- Advice: use it for visual products and creative collaboration; set a budget and a stopping point
```

### wiki/sources/newsletters/every-recap-opus-5-5-verdict-2026-09-27.md (new)

```
---
title: Every — weekly recap, Opus 5.5 verdict
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-27-opus-55-and-sol-split-the-team.md
published: 2026-09-27
ingested: 2026-10-20
domains: [models]
---

# Every — weekly recap, Opus 5.5 verdict

Every's Sunday recap ("Opus 5.5 and Sol Split the Team") summarizes the week's Vibe Checks. This page covers the Opus 5.5 verdict only.

## Influenced pages
- [Claude Opus 5.5](../../models/claude-opus-5-5.md) — condensed verdict and trade-offs

## Key claims extracted
- Opus 5.5 matched or beat Fable 5.1 on product and design work at 60% less per token
- It became Kieran Klaassen's daily driver and tempted Codex converts back to Claude
- Two trade-offs: it buries the point in prose, and it runs for hours unless given a budget
- Pick Opus 5.5 over GPT-6 Sol for ambitious coding and visual work (it built a webcam heart-rate monitor Sol could not finish)
```

## Schema / vocabulary additions

None.

## Open questions

None.
