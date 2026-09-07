---
type: proposal
source: raw/newsletters/2026-08-06-a-codex-of-ones-own.md
status: pending
created: 2026-09-07
---

# Proposal: Interview-driven onboarding for a personal agent workspace

## Summary

### The source

Every's "A Codex of One's Own" (Katie Parrott, 2026-08-06) opens with a comparison: Every's head of operations Arielle Shipper and head of consulting Natalia Quintero sat down to compare their Codex setups, expecting to find common ground. They found almost none. Natalia's own setup runs on detailed planning, context organization, and close supervision of outputs; Arielle — described as particularly good at "having minimal process while still executing on what needs to be done" — instead sets up reminders and standing messages so that a task "can just get done without her having to track or pay attention to it." The piece's throughline is that Codex is open-ended enough to live in one chat thread, sit atop a carefully organized workspace, or land somewhere in between, which leaves every new user facing the same unanswered question: set it up for *what*? Borrowing someone else's setup gives you their ideas, not their workload, their brain, or their life. Parrott's own answer was to skip the copying step entirely: she told Codex she wanted help designing her workspace and asked it to interview her — about her work, her needs, and which decisions she wanted the system to keep deferring to her on. Codex turned her answers into a proposed desktop architecture and a set of pinned threads, and she then handed the same approach to a colleague so she could run the interview for herself.

### What changes

`training/company-wide-ai-enablement.md` currently documents several onboarding and rollout patterns (platform-plus-spokes, aha-moment workflows, thread-per-task chat orchestration) but nothing about how an individual user should configure their own agent workspace in the first place.

- **Company-wide AI enablement** gains one new "Proven patterns" bullet describing interview-driven workspace onboarding: have the agent interview the new user about their work, needs, and which decisions they want to keep making themselves, then let it propose the workspace structure from those answers — rather than copying someone else's setup wholesale. Page date moves to 6 August.
- New source page for the Every newsletter, since no page for this raw file exists yet.

### What to weigh

This is a single first-person anecdote from one Every writer, not a study or a pattern independently observed across multiple organizations — closer in evidentiary weight to the page's existing "Let AI write the agent instructions" bullet (also a single Every example) than to the multi-source patterns like thread-per-task orchestration. The piece is behind Every's paywall past the free-preview section used here, so the actual interview prompt itself (which the source explicitly saves for paying subscribers) is not available to include.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/company-wide-ai-enablement.md` — add one Proven-patterns bullet on interview-driven agent-workspace onboarding, one new Recent-changes entry, bump `as_of` to 2026-08-06, append new source id
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/codex-interview-onboarding-2026-08-06.md` — source summary

## Page drafts

### wiki/training/company-wide-ai-enablement.md (updated)

Frontmatter: bump `as_of: 2026-07-29` → `as_of: 2026-08-06`; append `codex-interview-onboarding-2026-08-06` to the `sources:` list.

New bullet appended to the end of `## Proven patterns` (after the existing "Keep humans at the judgment boundary" bullet):

```md
- **Interview-driven agent-workspace onboarding.** Rather than copying someone else's agent setup, have the agent interview the new user first — about their work, their needs, and which decisions they want to keep making themselves — then let it propose a workspace structure (pinned threads, file/desktop organization) from those answers. Every's Katie Parrott used this pattern with Codex, then handed the same approach to a colleague to run for herself. The reason it matters: two Every staffers who compared their own hand-built Codex setups found them almost nothing alike — one built on minimal process and reminders, the other on detailed planning and supervision — because a workable setup mirrors how the individual actually works, not a template borrowed from someone else.
```

New entry added to `## Recent changes` (current live list has 7 entries; this becomes the 8th, newest-first, no spill expected since the cap is 10):

```md
- [2026-08-06] Added interview-driven agent-workspace onboarding pattern: have the agent interview the new user before proposing a workspace structure, rather than copying someone else's setup.
```

New line appended to `## Sources`:

```md
- [A Codex of One's Own — Every](../sources/newsletters/codex-interview-onboarding-2026-08-06.md)
```

### wiki/sources/newsletters/codex-interview-onboarding-2026-08-06.md (new)

```md
---
title: "A Codex of One's Own — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-06-a-codex-of-ones-own.md
url: https://every.to/context-window/a-codex-of-ones-own
published: 2026-08-06
ingested: 2026-09-07
domains: [training]
---

# A Codex of One's Own — Every

Every's Katie Parrott compares two staffers' wildly different Codex setups (one minimal-process, one detailed-planning-and-supervision) to argue that a personal agent workspace should mirror how its user actually works rather than copy someone else's template. Her own solution: have Codex interview her about her work, needs, and which decisions she wanted to keep making herself, then let it propose a desktop architecture and pinned threads from her answers — an approach she then handed to a colleague to run for herself. The same issue also carries a shorter Signal item on Demis Hassabis's move to GDM Chair/Alphabet Chief Scientist and Meta's Muse Code beta launch, covered separately.

## Influenced pages

- [training/company-wide-ai-enablement](../../training/company-wide-ai-enablement.md) — new Proven-patterns bullet on interview-driven agent-workspace onboarding

## Key claims extracted

- Every's Arielle Shipper (minimal process, reminders/messages) and Natalia Quintero (detailed planning, context organization, supervision) have almost nothing in common in how they configure Codex
- Katie Parrott had Codex interview her about her work, needs, and which decisions she wanted to keep making herself, then had it propose a desktop architecture and pinned threads from her answers
- She then handed the same interview-based approach to colleague Laura Entis to run for herself
```
