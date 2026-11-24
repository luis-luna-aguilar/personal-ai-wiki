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
