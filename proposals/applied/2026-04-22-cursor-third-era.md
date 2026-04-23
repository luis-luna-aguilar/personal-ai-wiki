---
type: proposal
sources:
  - raw/tweets/2026-04-22-mntruell-2026736314272591924.md
  - raw/tweets/2026-04-22-danshipper-2039769564641140967.md
status: pending
created: 2026-04-22
---

# Proposal: Cursor 3 update + Michael Truell "Third Era" essay

## Summary

Two strong sources on where Cursor and agentic coding are heading. Michael Truell's essay defines a concrete "third era" progression (Tab → sync agents → cloud agents) with internal data: 35% of Cursor's own PRs are from autonomous cloud agents, and agent users now outnumber Tab users 2:1. Dan Shipper's vibe check gives a frank external view of Cursor 3: promising orchestration direction, but awkward transition that risks alienating IDE users.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — add Truell's third-era data and Shipper vibe check
    > **Add new section `## The third era thesis` after `## What's new in Cursor 3.1`:**
    > ```markdown
    > ## The third era thesis
    >
    > Michael Truell's April 2026 essay defines three eras of AI software development:
    >
    > 1. **Tab autocomplete** — code written keystroke-by-keystroke with AI fill-in
    > 2. **Synchronous agents** — prompt-and-response loops, developer in the loop at every step; practical only for a few agents in parallel (they compete for local machine resources)
    > 3. **Cloud agents** — agents running on their own VMs over hours; developer defines the problem and reviews artifacts (videos, previews, logs) rather than diffs; many in parallel is practical
    >
    > Internal Cursor data (as of April 2026): 35% of PRs merged internally at Cursor are now created by autonomous cloud agents. Agent users now outnumber Tab users 2:1 (was the reverse in March 2025); agent usage has grown 15× in one year. Truell's profile of a "third era developer": agents write ~100% of their code, they spend time on problem breakdown and artifact review, they spin up multiple agents simultaneously instead of hand-holding one.
    > ```
    >
    > **Update `## Weaknesses / caveats`** — add Shipper vibe check paragraph:
    > ```markdown
    > - Dan Shipper's vibe check (April 2026) after a week of internal Every testing: fast desktop performance, local↔cloud demo videos are a "wow moment," but "it's still an early product and it's not clear who will love it." The rewrite deprioritizes the IDE, which alienates sizable existing Cursor fans. Summary: "the right strategic move, but an awkward in-between stage."
    > ```
    >
    > **Update `as_of: 2026-04-22` in frontmatter.**
    >
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added Truell's third-era data: 35% of Cursor internal PRs from cloud agents; 2:1 agent-to-Tab user ratio; 15× agent usage growth YoY
    > - [2026-04-22] Added Shipper vibe check: promising direction, awkward transition, early-product caveats
    > ```

- [x] **Update** `wiki/state-of/coding.md` — update Cursor line in `Agentic coding workspace` and update as_of
    > **Before:**
    > ```
    > - [[tools/cursor]] — Cursor remains the clearest reference point for the category: by early March its cloud-agent story was already explicitly about remote agents booting environments, testing their own work, returning demo videos, and giving humans a supervision surface for review rather than just an IDE with AI features *(as of 2026-03-06)*
    > ```
    > **After:**
    > ```
    > - [[tools/cursor]] — Cursor 3 is a full rewrite as a cloud-agent orchestration platform; 35% of Cursor's internal PRs now from autonomous cloud agents; 2:1 agent-to-Tab users; Truell defines this as the "third era" where cloud agents run independently and developers review artifacts, not diffs *(as of 2026-04-22)*
    > ```
    > **Update `as_of: 2026-04-22` in frontmatter.**
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Cursor 3 confirmed as cloud-agent orchestration bet: 35% internal PRs from cloud agents, 2:1 agent-to-Tab user ratio per Truell essay
    > ```

- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add Truell's internal data as a concrete signal
    > **Add to `## Concrete signals`:**
    > ```markdown
    > - **Cursor's internal development has already crossed the threshold.** Michael Truell's April 2026 essay reports 35% of Cursor's internal PRs are now created by autonomous cloud agents operating on their own VMs — not a research claim, an operational report from a company actively building this way. The third-era developer pattern he describes (agents write ~100% of code, human role shifts to problem definition and artifact review) is already the default for part of his own team.
    > ```
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added Cursor/Truell internal data: 35% of PRs from cloud agents; third-era dev pattern operational inside Cursor itself
    > ```

- [x] **Create** `wiki/sources/tweets/cursor-third-era.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/tweets/cursor-third-era.md (new)

```md
---
title: Michael Truell — "The third era of AI software development"
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-mntruell-2026736314272591924.md
url: https://x.com/mntruell/status/2026736314272591924
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents]
---

# Michael Truell — "The third era of AI software development"

Cursor CEO's essay defining three eras of AI-assisted development: Tab autocomplete → synchronous agents → cloud agents. Reports 35% of Cursor's internal PRs are created by autonomous cloud agents; agent users now outnumber Tab users 2:1; agent usage grew 15× in one year. Describes the "third era developer" pattern and Cursor 3 as a step in that direction.

Secondary source: Dan Shipper's vibe check (`raw/tweets/2026-04-22-danshipper-2039769564641140967.md`) gives an external week-of-testing perspective: fast desktop, demo videos impressive, but early-stage and risks alienating existing IDE users.

## Influenced pages

- [[tools/cursor]] — third-era data added; vibe check caveats added
- [[state-of/coding]] — Cursor line updated with third-era framing
- [[trends/agents-reshape-organizations]] — Truell internal data added as concrete signal

## Key claims extracted

- Three eras: Tab → sync agents → cloud agents
- 35% of Cursor internal PRs now from autonomous cloud agents
- 2:1 agent-to-Tab users (was reversed March 2025)
- 15× agent usage growth YoY in Cursor
- Third-era dev: agents write ~100% of code; human reviews artifacts not diffs
- Sync agents impractical at scale because they compete for local machine resources
- Cloud agents remove both constraints (compete for resources, need human in loop per step)
```
