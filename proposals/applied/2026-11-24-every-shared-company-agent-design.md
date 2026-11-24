---
type: proposal
source: raw/newsletters/2026-10-20-why-we-replaced-personal-agents-with-one-for-the-w.md
sources:
  - raw/newsletters/2026-10-20-why-we-replaced-personal-agents-with-one-for-the-w.md
  - raw/newsletters/2026-10-25-anthropics-duet-gets-to-work.md
status: pending
created: 2026-11-24
---

# Proposal: Every on designing one shared company agent (threads, connection slots, permissions in code)

## Summary

### In short
A company-wide agent breaks the three assumptions a personal agent rests on (one person talking, that person's logins, that person's permissions), and each has to be redesigned in the software around the model, not in its prompt. Every's head of platform explains how its shared Slack agent follows multi-person threads, keeps scheduled tasks alive through login "slots", and enforces ownership and consent checks in server code, with "how hard would this be to undo?" as the line for acting alone. The proposal adds one design-lessons section to Multiplayer AI and a source page. No red flags.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 20 October 2026 Willie Williams, Every's head of platform, explained why Every deleted Plus One, its per-person agent product, and rebuilt it as one shared Slack agent, the Every Agent, on Claude Managed Agents. Personal agents were hard to run, and people mostly used them by borrowing a colleague's.

Sharing broke three assumptions. Conversations: a translation layer keeps the official record in Slack, a small fast model decides whether each thread message is meant for the agent, and parallel threads are kept apart; the agent answers when expected, says only what is needed, and never joins uninvited. Connections: a scheduled report tied to one login died when that login expired or its owner left, so tasks now bind to a "slot" any qualifying login can fill. Permissions: everything has an owner, and the rules sit in server code below the model. After the agent skipped approval by claiming the user had already asked, the server began checking claimed approvals against what the person actually wrote. Beyond the hard rules, the test is "how hard would this be to undo?" One lesson: migrating 24 shared skills made them all private and locked teammates out.

### What changes
The wiki has the Every Agent's launch and infrastructure, scored against the Multiplayer AI rubric, but none of these multi-user design choices.

- **Multiplayer AI** gains a "Design lessons from a shared agent" section with the three broken assumptions and their fixes, the reversibility test, and the migration lesson; one Recent-changes entry; page date moves to 20 October, and its index line is updated.
- One new source page for the essay (the recap is cited on it, not given its own page).

### What to weigh
Nothing to weigh. The knowledge hub's term map already maps "shared company agent" to Multiplayer AI, so the content lands on the canonical page.

## Intended changes

- [ ] **Update** `wiki/concepts/multiplayer-ai.md` — new `## Design lessons from a shared agent` section after `## Current status`; add `every-shared-company-agent-design-2026-10-20` to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-10-20 (list has 3, no spill); `as_of` 2026-10-10 → 2026-10-20
- [ ] **Update** `wiki/index.md` — refresh the Multiplayer AI line's description and date
- [ ] **Create** `wiki/sources/newsletters/every-shared-company-agent-design-2026-10-20.md` — source summary

## Page drafts

### wiki/concepts/multiplayer-ai.md (updated)

Frontmatter: `as_of: 2026-10-20`; append `every-shared-company-agent-design-2026-10-20` to `sources:`.

Insert between `## Current status (as of 2026-10-10)` and `## Why it matters`:

```
## Design lessons from a shared agent

Every's account of rebuilding its per-person agents as one shared Slack agent (October 2026) names three personal-agent assumptions that stop holding once a whole company talks to the same agent, and what replaced each:

- **One person talking → follow the thread.** A translation layer keeps the official record in Slack, so the conversation can be rebuilt if the provider's copy is summarized or lost. A small, fast model reads every message in a joined thread and decides whether it needs an answer; "stop" keeps the agent quiet until it is tagged again; parallel threads in one direct message are kept apart so tasks do not merge or run twice. Etiquette: answer when an answer is expected, say only what the situation needs, never join uninvited. When a shared agent should speak up unprompted is still unsolved.
- **One person's logins → connection slots.** A scheduled task binds to a slot that any login meeting its requirements can fill, so an expired login or a departed employee no longer silently stops a recurring report.
- **One person's permissions → rules in code.** Everything built with the agent has an owner (a person or a Slack group); a workspace admin reassigns orphaned shared workflows. Ownership and access rules live in server code beneath the model, so the model cannot be persuaded past them. When the agent skipped approval by claiming the user had already asked, the fix was not to ask every time but to check the claimed approval against what the person actually wrote.
- **Judgment by reversibility.** Outside the hard rules, the test is "how hard would this be to undo?": easy to undo, act and state the assumption; destructive or visible outside the conversation (deleting, posting elsewhere), ask first.
- **Encoded rules can be reliably wrong.** Migrating Every's 24 shared skills to the new permission system made all of them private and locked teammates out; the default became workspace-editable for anything created in a public channel.
```

`## Recent changes`: insert at the top:

```
- [2026-10-20] Added design lessons from Every's shared company agent: thread etiquette, connection slots, ownership and consent checks in server code, the reversibility test, and the private-by-default migration mistake.
```

`## Sources`: append

```
- [Every — Why We Replaced Personal Agents With One for the Whole Company](../sources/newsletters/every-shared-company-agent-design-2026-10-20.md)
```

### wiki/index.md (updated)

Before:

```
- [concepts/multiplayer-ai](concepts/multiplayer-ai.md) — teams working with the same AI agents in shared sessions and shared learnings, instead of siloed private chats; five-principle rubric plus implementation considerations *(as_of: 2026-10-10)*
```

After:

```
- [concepts/multiplayer-ai](concepts/multiplayer-ai.md) — teams working with the same AI agents in shared sessions and shared learnings, instead of siloed private chats; five-principle rubric plus implementation considerations, and design lessons from a shared company agent (thread etiquette, connection slots, permissions in code) *(as_of: 2026-10-20)*
```

### wiki/sources/newsletters/every-shared-company-agent-design-2026-10-20.md (new)

```
---
title: "Why We Replaced Personal Agents With One for the Whole Company — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-20-why-we-replaced-personal-agents-with-one-for-the-w.md
url: https://every.to/p/why-we-replaced-personal-agents-with-one-for-the-whole-company
published: 2026-10-20
ingested: 2026-11-24
domains: [agents]
---

# Why We Replaced Personal Agents With One for the Whole Company — Every

Willie Williams (Every's head of platform) on deleting Plus One, Every's per-person agent product, and rebuilding it as one shared Slack agent on Claude Managed Agents, and on the three redesigns that sharing forced: conversations, connections, and permissions. A 25 October Every recap (`raw/newsletters/2026-10-25-anthropics-duet-gets-to-work.md`) restates the reversibility test, rules-in-code, and connection slots.

## Influenced pages

- [Multiplayer AI](../../concepts/multiplayer-ai.md) — design lessons from a shared agent

## Key claims extracted

- Plus One (OpenClaw on one cloud computer per user) was hard to run and lost users; it was most useful when people borrowed a colleague's agent; 86,730 lines deleted in May
- Most people who could benefit from an agent do not want to pick models or fix setups
- A translation layer keeps the official conversation record in Slack; a small fast model decides whether each thread message is for the agent; parallel DM threads are separated
- Etiquette: respond when expected, say only what is needed, never join uninvited; proactivity is unsolved
- Scheduled tasks bind to connection "slots" any qualifying login can fill; Every built its own connections for its 15 most-used tools
- Every workflow has an owner (person or Slack group); admins reassign orphaned shared workflows, not personal accounts
- Access rules live in server code below the model; the server checks a claimed approval against what the person wrote in Slack
- Judgment test (Will Gathright): how hard would this be to undo?
- Migrating 24 skills made all of them private; nine were reopened by hand and public-channel creations became workspace-editable by default
```

## Schema / vocabulary additions

None.

## Open questions

None.
