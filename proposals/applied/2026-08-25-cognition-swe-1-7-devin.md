---
type: proposal
source: raw/newsletters/2026-07-09-spacexai-drops-grok-45.md
status: pending
created: 2026-08-25
---

# Proposal: Cognition ships SWE-1.7, a budget frontier coding model for Devin

## Summary

### The source

On 9 July 2026 The Code newsletter recapped Cognition's release of SWE-1.7, a "budget frontier" coding model for Devin, its autonomous coding agent. Cognition post-trained Kimi K2.7 inside Devin's own agent harness — the tools, memory and loops the agent runs in — so the model learns the environment it will work in. The pitch is price: Cognition says SWE-1.7 "matches GPT-5.5 within a point" on FrontierCode, its own coding benchmark, at roughly $2 per task, with Opus 4.8 still slightly ahead. The model can summarize its own progress and resume, allowing sessions of up to six hours. It is available in Devin now.

Two caveats. The recap is one paragraph and gives neither a numeric score nor which FrontierCode tier (Diamond or the cost-aware Extended) it means. And Cognition's own blog post was not fetched, so everything here is secondhand. Grok 4.5 and GPT-Live, in the same issue, are handled elsewhere.

### What changes

The wiki's Devin page (dated 14 July) covers Auto-Triage, Security Swarm, MapReduce, Fusion and the productivity estimator but not SWE-1.7; the FrontierCode page (dated 29 June) has no SWE-1.7 claim either.

- **Devin** gains one Current-status bullet and a Recent-changes entry. The source is older than the page's newest claims, so the entry slots in third, below the two 14 July lines, and the page date stays at 14 July. Nothing spills; a pre-existing date misorder is fixed in passing. No existing wording changes.
- **FrontierCode** gains a short caveated subsection, "SWE-1.7 on FrontierCode (secondhand)," between the Extended table and Why it matters, plus a Recent-changes entry at the top. Leaderboard tables untouched. Page date moves to 9 July; a misorder is fixed here too.
- A new source page `sources/newsletters/the-code-spacexai-drops-grok-45-2026-07-09.md` records the issue, scoped to SWE-1.7. No dashboards, leader lines or schema are touched.

### What to weigh

Every performance claim traces to one paragraph of The Code relaying Cognition; the drafts attribute it that way in all four places it appears, but for a verified treatment — exact tier, score, pricing — I should fetch cognition.com/blog/swe-1-7 and revise before applying. Separately, SWE-1.7 gets no `models/` page: it is filed as a Devin-harness capability only, reasonable given the thin sourcing, but say so if you'd rather have a dedicated model page now instead of only if it ships standalone.

## Chronology note (read before applying)

`tools/devin.md` and `benchmarks/frontiercode.md` were both heavily rewritten earlier today (2026-08-25) from a different, more recent batch of sources — current `as_of: 2026-07-14` on devin.md and `as_of: 2026-06-29` on frontiercode.md, with substantial new content (Agentic MapReduce, Devin Fusion, the productivity estimator, and a FrontierCode Extended tier). This SWE-1.7 signal is dated **2026-07-09**, which is:

- **older** than `tools/devin.md`'s current `as_of` (2026-07-14) → the new Recent-changes entry is inserted **below** the two 2026-07-14 entries (not prepended above them), and `as_of` **stays at 2026-07-14** since that remains the newest source-backed claim on the page.
- **newer** than `benchmarks/frontiercode.md`'s current `as_of` (2026-06-29) → the new entry goes at the **top** of Recent changes, and `as_of` **bumps to 2026-07-09**.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/tools/devin.md` — add SWE-1.7 as a Current-status bullet (attributed to The Code's recap); insert Recent-changes entry directly after the two `[2026-07-14]` lines and reorder the section to strict reverse-chronological (fixes pre-existing `[2026-06-29]`-above-`[2026-07-02]` misorder); `as_of` unchanged (2026-07-14); add new source
    > See draft below

- [x] **Update** `wiki/benchmarks/frontiercode.md` — add a caveated "SWE-1.7 on FrontierCode" subsection; new Recent-changes entry at top and reorder the section to strict reverse-chronological (fixes pre-existing `[2026-06-09]`-above-`[2026-06-10]` misorder); `as_of` bumped to 2026-07-09; add new source
    > See draft below

- [x] **Create** `wiki/sources/newsletters/the-code-spacexai-drops-grok-45-2026-07-09.md` — source summary for The Code's 2026-07-09 issue (SWE-1.7 portion only)

## Page drafts

### wiki/tools/devin.md (updated)

Frontmatter — add one source id, no other changes:

```md
---
title: Devin
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: []
as_of: 2026-07-14
sources: [devin-auto-triage-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, cognitioncom-blog-ai-productivity, the-code-spacexai-drops-grok-45-2026-07-09]
---
```

New bullet appended to the end of `## Current status (as of 2026-07-14)`:

```md
- **SWE-1.7 (July 2026):** a budget frontier coding model for Devin, post-trained from Kimi K2.7 inside Devin's own agent harness; per The Code's recap, Cognition claims it matches GPT-5.5 within a point on FrontierCode at roughly $2/task with Opus 4.8 slightly ahead (secondhand — tier and numeric score unspecified, Cognition's blog post not yet read); can summarize its own progress and resume where it left off, enabling coding sessions up to six hours
```

`## Recent changes` (full section, new entry inserted third — after the two 2026-07-14 entries, before the 2026-07-02 entry; the section is also reordered to strict reverse-chronological, moving the pre-existing `[2026-06-29]` line below `[2026-07-02]`):

```md
## Recent changes

- [2026-07-14] Cognition detailed Agentic MapReduce (Plan/Shard/Map/Reduce/Verify) as the architecture behind Security Swarm; reported 72% recall on a CVE-pinned benchmark vs. rival scanners.
- [2026-07-14] Cognition's session-level productivity estimator (`r_log = 0.74`, human-hours-equivalent, calibrated conservative) is now running in production with customers.
- [2026-07-09] Cognition released SWE-1.7, a budget frontier coding model post-trained from Kimi K2.7 inside Devin's agent harness; per The Code's recap, Cognition claims it matches GPT-5.5 within a point on FrontierCode at ~$2/task with Opus 4.8 slightly ahead (secondhand, tier unspecified); supports up to six-hour sessions via self-summarization and resume.
- [2026-07-02] Cognition shipped Devin Security Swarm for parallel vulnerability discovery, sandbox reproduction, exploitability validation, and fix PRs.
- [2026-06-29] Devin Fusion (preview): multi-model "sidekick" harness matches frontier performance at 35% lower cost (41% with Fable 5) on FrontierCode Extended; 88% of Cognition's internal merged PRs driven by the automated router.
- [2026-05-19] Auto-Triage shipped: always-on Slack monitoring, parent/child Devin structure, shared long-term deduplication memory
```

`## Sources` (full section, one line added):

```md
## Sources

- [Devin Auto-Triage launch](../sources/articles/devin-auto-triage-2026-05.md)
- [The Code - Cognition ships Devin for Security](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Agentic MapReduce (Cognition/Devin blog)](../sources/articles/devinai-blog-agentic-map-reduce.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
- [Estimating the Productivity of an Autonomous AI Software Engineer](../sources/articles/cognitioncom-blog-ai-productivity.md)
- [The Code - SpaceXAI drops Grok 4.5](../sources/newsletters/the-code-spacexai-drops-grok-45-2026-07-09.md)
```

### wiki/benchmarks/frontiercode.md (updated)

Frontmatter — `as_of` bumped, one source id added:

```md
---
title: FrontierCode
type: benchmark
domains: [coding]
tags: [cognition, benchmark]
as_of: 2026-07-09
sources: [ainews-frontiercode-june-2026, ainews-fable5-june-2026, cognitioncom-blog-devin-fusion, the-code-spacexai-drops-grok-45-2026-07-09]
---
```

New subsection inserted between `## FrontierCode Extended (cost-aware, as of 2026-06-29)` and `## Why it matters`:

```md
## SWE-1.7 on FrontierCode (secondhand, 2026-07-09)

Per The Code newsletter's recap (2026-07-09) of Cognition's SWE-1.7 release (a budget coding model for [Devin](../tools/devin.md), post-trained from Kimi K2.7 inside Devin's agent harness), Cognition claims the model matches GPT-5.5 within a point on FrontierCode at roughly $2/task, with Opus 4.8 staying slightly ahead. The recap does not specify which tier (Diamond vs. Extended) or give a numeric score, and Cognition's own announcement (`cognition.com/blog/swe-1-7`) has not been read — treat this as a directional, secondhand vendor claim, not a leaderboard entry.
```

`## Recent changes` (full section, new entry at top; the section is also reordered to strict reverse-chronological, moving the pre-existing `[2026-06-10]` line above `[2026-06-09]`):

```md
## Recent changes

- [2026-07-09] Per The Code's recap, Cognition claims SWE-1.7 (Devin) matches GPT-5.5 within a point on FrontierCode at ~$2/task, with Opus 4.8 slightly ahead (secondhand, tier unspecified, no numeric score).
- [2026-06-29] Cognition introduced FrontierCode Extended (score + avg. cost/task) alongside Devin Fusion; Fusion+Fable5 leads the cost-adjusted comparison at 57.6/$3.00, while Fable5 alone scores marginally higher (57.0) at much higher cost ($5.12).
- [2026-06-10] Fable 5 launched with 29.3% Diamond, Mythos 5 at 30.9%
- [2026-06-09] Launched; Opus 4.8 scored ~13.4% on Diamond tier
```

`## Sources` (full section, one line added):

```md
## Sources

- [AINews — FrontierCode launch (June 9)](../sources/newsletters/ainews-frontiercode-june-2026.md)
- [AINews — Fable 5 FrontierCode Diamond score (June 10)](../sources/newsletters/ainews-fable5-june-2026.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
- [The Code - SpaceXAI drops Grok 4.5](../sources/newsletters/the-code-spacexai-drops-grok-45-2026-07-09.md)
```

### wiki/sources/newsletters/the-code-spacexai-drops-grok-45-2026-07-09.md (new)

```md
---
title: The Code - SpaceXAI drops Grok 4.5
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-09-spacexai-drops-grok-45.md
url: https://codenewsletter.ai/p/spacexai-drops-grok-4-5-openai-brings-a-new-gen-of-voice-models
published: 2026-07-09
ingested: 2026-08-25
domains: [coding, models]
---

# The Code - SpaceXAI drops Grok 4.5

"The Code" newsletter issue (2026-07-09) covering three items: xAI/SpaceXAI's Grok 4.5 launch (co-trained with Cursor, positioned as "Opus-class" at lower cost), OpenAI's GPT-Live full-duplex voice model, and Cognition's SWE-1.7 — a budget frontier coding model for Devin, post-trained from Kimi K2.7 inside Devin's own agent harness. This summary is scoped to the SWE-1.7 item; Grok 4.5 and GPT-Live are tracked from their own primary sources and are not actioned from this issue. All SWE-1.7 claims here are the newsletter's recap of Cognition's announcement; Cognition's blog post (`cognition.com/blog/swe-1-7`) was not read.

## Influenced pages
- [Devin](../../tools/devin.md) — added SWE-1.7 as a new Current-status bullet and Recent-changes entry
- [FrontierCode](../../benchmarks/frontiercode.md) — added a secondhand SWE-1.7 performance claim (no numeric score, tier unspecified)

## Key claims extracted
- Cognition released SWE-1.7, post-trained from Kimi K2.7 inside Devin's agent harness
- Per the newsletter, it matches GPT-5.5 within a point on Cognition's FrontierCode benchmark at roughly $2/task; Opus 4.8 stays slightly ahead (tier and numeric score not given)
- Can summarize its own progress and resume where it left off, enabling coding sessions up to six hours
- Available in Devin today (devin.ai)
- (Not actioned from this issue) Grok 4.5 launch and GPT-Live voice model
```

## Open questions

- Cognition's own blog post (`cognition.com/blog/swe-1-7`) was not fetched for this proposal — only the secondary newsletter recap was available. If you'd like a deeper/verified SWE-1.7 treatment (exact FrontierCode tier, numeric score, pricing details), I can fetch it and revise this proposal before applying.
- No new `models/swe-1-7.md` page was created — the triage scoped this signal to `devin.md` + `frontiercode.md` updates only, treating SWE-1.7 as a Devin-harness capability rather than a standalone tracked model. Flag if you'd prefer a dedicated model page instead.
