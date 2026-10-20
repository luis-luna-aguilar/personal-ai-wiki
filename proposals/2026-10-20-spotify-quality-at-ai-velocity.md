---
type: proposal
source: raw/articles/2026-10-20-tco-gpjtdwz0tt.md
sources:
  - raw/articles/2026-10-20-tco-gpjtdwz0tt.md
  - raw/tweets/2026-10-15-xcom-shubh6200status211041971430877.md
  - raw/newsletters/2026-10-17-ainews-high-taste-testers-ep-1.md
triage: proposals/triage/2026-10-11-to-2026-10-20-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Spotify on quality at AI velocity

## Summary

### In short
When AI multiplies the volume of code changes, the quality risk sits in the delivery system, not the AI-written code: Spotify found no incident directly caused by AI-authored code, but found that change volume grew faster than its verification controls could adapt. Merged changes more than doubled year over year (about 8,100 to 17,000 in August) while the share of quality work rose and rework did not. The proposal adds the case to the engineering evidence page, a measurement pattern to the coding-evals page, and an automated-change failure to agentic infrastructure operations. One reason to hesitate: the article's exact publication date is inferred from its URL.

[[#Open questions|Open questions: none.]]

### The source
Spotify Engineering's post "AI Changed How Spotify Builds", dated September 2026 by its URL and widely shared on 14 October, reviews quality during the company's AI ramp-up. Spotify runs nearly 3,000 production services for 777 million monthly users, and the post opens by saying "AI slop" was not the problem. Four areas strained at once: a content-processing pipeline whose failures could go unnoticed for hours; fleet-wide automated changes, where an agent-driven dependency upgrade passed every check and still broke production; compute scarcity, which the industry's AI demand worsened and which made previously invisible regional failovers noticeable to users; and mobile releases, where each release looked healthy while small regressions piled up.

Spotify then checked its own data. Monthly incident retrospectives now ask two extra questions: did AI-authored code directly contribute, and did the higher volume of change strain review, testing, rollout or observability? The answer was no to the first and yes to the second. Merged changes more than doubled year over year, and quality and optimization work rose from 27% to 31% of the mix, so engineers did more than twice as much absolute quality work. Spotify rebuilt its "rework rate" metric, which weighs how recent the changed code is, and saw no rise even as an industry report (FAROS 2026) found code churn rising sharply. It is watching two warning signs, PR size and code complexity, and has chosen not to loosen those thresholds until it knows whether they still mean what they used to. The fixes are end-to-end monitoring, more rollback capacity, scheduling automated changes during the owning team's working hours, and longer-term mobile quality signals. A separate AINews item adds a related number: Claude writes about 90% of Claude Code's own code, and between June and September merged PRs doubled while the reverted share fell more than 40%.

### What changes
The wiki already tracks agent-scale change volume through Anthropic's CI and source-control cases, but has no company-scale study of whether quality held.

- **Engineering AI adoption: evidence from practice** gains a Spotify case bullet in its adoption-and-volume section, and the Claude Code figure is appended to the Anthropic internal-data subsection. Page date stays 19 October.
- **Evals for agentic software development** gains one proven pattern: measure quality at the delivery-system level with incident questions and rework rate, and hold thresholds steady while their meaning is uncertain. Page date stays 19 October.
- **Agentic infrastructure operations** gains Spotify's failed automated dependency upgrade as evidence and a matching failure mode. Page date stays 19 October.
- One new article source page and one AINews story page.

### What to weigh
The article's only date is the "2026/9" in its URL, so its source page and Recent-changes entries use 30 September. The tweet that pointed to the article adds nothing, so it gets no source page. The evals page reaches about 97% of its length ceiling.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/engineering-ai-adoption-evidence.md` — new Spotify bullet under `### Adoption and volume data`; one sentence appended to the Anthropic RSI bullet; adds two Recent-changes entries dated 2026-10-17 and 2026-09-30 (9 of 10 after insert, no spill); merge two source ids; `as_of` stays 2026-10-19.

- [ ] **Update** `wiki/training/evals-for-agentic-software-development.md` — one bullet under `## Proven patterns`; adds one Recent-changes entry dated 2026-09-30 (7 of 10, no spill); merge source; `as_of` stays 2026-10-19.

- [ ] **Update** `wiki/training/agentic-infrastructure-operations.md` — one bullet under `## Evidence from practice`, one under `## Failure modes`; adds one Recent-changes entry dated 2026-09-30 (2 of 10); merge source; `as_of` stays 2026-10-19.

- [ ] **Create** `wiki/sources/articles/spotify-quality-at-higher-velocity-2026-09.md` — source summary.

- [ ] **Create** `wiki/sources/newsletters/ainews-claude-code-90-percent-2026-10-17.md` — AINews story page for the Claude Code figure.

## Page drafts

### wiki/training/engineering-ai-adoption-evidence.md (updated)

Frontmatter: append `spotify-quality-at-higher-velocity-2026-09, ainews-claude-code-90-percent-2026-10-17` to `sources:`; `as_of: 2026-10-19` unchanged.

Under `### Adoption and volume data`, append after the GitHub commit-volume bullet:

```
- Spotify (September 2026, Spotify Engineering): merged changes more than doubled year over year in August (about 8,100 to 17,000), and quality and optimization work rose from 27% to 31% of the mix (more than twice the absolute quality work) while maintenance fell from 31% to 25%. Monthly incident retrospectives found no case where AI-authored code was a material direct cause, but found that "the volume of change increased faster than some of our verification controls could adapt": an agent-driven dependency upgrade passed checks and failed in production, AI-driven compute scarcity made regional failovers visible to users, and mobile regressions accumulated across individually healthy releases. A rebuilt rework-rate metric (weighted by the age of the code changed) showed no rise while industry code churn rose sharply (FAROS 2026). PR size and complexity are creeping up, and Spotify is deliberately not loosening those thresholds until it knows whether they still signal risk. Spotify's conclusion: AI raised the capacity to produce change, and the next constraint is verifying it. The measurement pattern is on [Evals for agentic software development](evals-for-agentic-software-development.md), the automated-change fixes on [Agentic infrastructure operations](agentic-infrastructure-operations.md).
```

Under `### Anthropic internal data and infrastructure`, append to the end of the "Anthropic internal RSI data (June 2026)" bullet:

```
 A later data point (October 2026): Claude writes about 90% of Claude Code's own code, and from June to September merged PRs doubled while the share reverted fell by more than 40%.
```

`## Recent changes` — insert in date order (after the 2026-10-19 entries):

```
- [2026-10-17] Added Claude Code's own figures: ~90% Claude-written, merged PRs doubled June→September, reverted share down 40%+.
```

and (after the 2026-10-15 entry):

```
- [2026-09-30] Added Spotify's quality review: merged changes doubled year over year, no AI-authored code as a direct incident cause, but change volume outran verification controls; rework rate flat while industry churn rose.
```

`## Sources` — append:

```
- [Spotify Engineering — AI Changed How Spotify Builds](../sources/articles/spotify-quality-at-higher-velocity-2026-09.md)
- [AINews — Claude writes ~90% of Claude Code (Oct 17)](../sources/newsletters/ainews-claude-code-90-percent-2026-10-17.md)
```

### wiki/training/evals-for-agentic-software-development.md (updated)

Frontmatter: append `spotify-quality-at-higher-velocity-2026-09` to `sources:`; `as_of: 2026-10-19` unchanged.

Under `## Proven patterns`, append:

```
- **Measure quality at the delivery-system level once change volume jumps.** Spotify adds two questions to every major-incident retrospective (did AI-authored code directly contribute? did the volume of change strain review, testing, rollout, or observability?), tracks rework rate weighted by the age of the code changed rather than raw code churn, and holds PR-size and complexity thresholds steady instead of loosening them while it is unclear whether they still signal risk. See [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md).
```

`## Recent changes` — insert in date order (after the 2026-10-19 entries):

```
- [2026-09-30] Added Spotify's delivery-system quality measurement as a proven pattern: two AI questions in incident retrospectives, age-weighted rework rate over churn, thresholds held steady.
```

`## Sources` — append:

```
- [Spotify Engineering — AI Changed How Spotify Builds](../sources/articles/spotify-quality-at-higher-velocity-2026-09.md)
```

### wiki/training/agentic-infrastructure-operations.md (updated)

Frontmatter: append `spotify-quality-at-higher-velocity-2026-09` to `sources:`; `as_of: 2026-10-19` unchanged.

Under `## Evidence from practice`, append:

```
- **Spotify Fleet Management (September 2026)** merges most fleet-wide automated changes without a human once they pass safety checks, and now runs agent-driven changes such as a Java migration across backend services finished in three days. An automated dependency upgrade passed every check and still failed in production, hurting users. Spotify's response is about the delivery system, not the agent: stronger safeguards, more rollback capacity, and scheduling automated changes during the owning team's working hours so someone is there to respond. See [Engineering AI adoption: evidence from practice](engineering-ai-adoption-evidence.md) for the wider quality data.
```

Under `## Failure modes`, append:

```
- Letting automated change volume grow faster than rollback capacity and on-hand owners; a change that passes every check can still fail in production when no one who owns the service is around
```

`## Recent changes` — insert after the 2026-10-19 entry:

```
- [2026-09-30] Added Spotify's automated dependency-upgrade failure and its fixes (rollback capacity, changes scheduled in owners' working hours); new failure mode on change volume outrunning rollback and ownership.
```

`## Sources` — append:

```
- [Spotify Engineering — AI Changed How Spotify Builds](../sources/articles/spotify-quality-at-higher-velocity-2026-09.md)
```

### wiki/sources/articles/spotify-quality-at-higher-velocity-2026-09.md (new)

```
---
title: "Spotify Engineering — AI Changed How Spotify Builds. What We Learned (and Fixed) About Quality at Higher Velocity"
type: source
source_type: article
source_file: raw/articles/2026-10-20-tco-gpjtdwz0tt.md
url: https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity
published: 2026-09-30
ingested: 2026-10-20
domains: [coding]
---

# Spotify Engineering — AI Changed How Spotify Builds

Spotify's review of software quality during its AI ramp-up: four strained areas (content processing, fleet-wide automated changes, compute scarcity and failover, mobile release quality), what its incident and PR data show about AI-authored code, and the delivery-system fixes it made. The URL places it in September 2026; the day is unknown, so `published:` uses the month's last day. Found via a 2026-10-14 tweet by Shubham Mishra that adds nothing beyond the link.

## Influenced pages

- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — Spotify case bullet
- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — delivery-system quality measurement pattern
- [Agentic infrastructure operations](../../training/agentic-infrastructure-operations.md) — automated dependency-upgrade failure and fixes

## Key claims extracted

- ~3,000 production services, 777M MAU, 11–12M backend requests/s; 500K+ new media items processed daily
- Incident retrospectives: AI-authored code not identified as a material direct contributor; "the volume of change increased faster than some of our verification controls could adapt"
- Merged changes more than doubled YoY in August (~8,100 → 17,000); quality/optimization 27% → 31% of mix; maintenance/configuration 31% → 25%
- Rebuilt rework-rate metric (weights age of code changed) shows no rise, while FAROS 2026 reports a sharp industry rise in code churn
- PR size and code complexity creeping up; thresholds deliberately not rewritten
- Fleet Management: most automated changes auto-merge after safety checks; agentic Java migration across backend services in three days; one automated dependency upgrade passed checks and failed in production → stronger safeguards, rollback capacity, changes scheduled in owners' working hours
- AI-driven industry compute scarcity made regional failovers user-visible; reserved edge capacity doubled after a May incident
- Content pipeline (June 24 incident): end-to-end monitoring, scheduler fix, batch jobs deprioritized, service tiering reworked
- Mobile: broadened quality signals with longer-term trends
- Conclusion: AI increased capacity to produce change; the next constraint is the ability to verify it
```

### wiki/sources/newsletters/ainews-claude-code-90-percent-2026-10-17.md (new)

```
---
title: AINews — Claude writes ~90% of Claude Code (Oct 17)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-17-ainews-high-taste-testers-ep-1.md
published: 2026-10-17
ingested: 2026-10-20
domains: [coding]
---

# AINews — Claude writes ~90% of Claude Code (Oct 17)

One item from the 17 October AINews issue, citing a ClaudeDevs post on Claude Code's own development.

## Influenced pages

- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — Anthropic internal-data sentence

## Key claims extracted

- Claude writes about 90% of Claude Code's code
- Merged PRs doubled from June to September 2026 while the reverted share fell more than 40%
```

## Schema / vocabulary additions

None.

## Open questions

None.
