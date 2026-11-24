---
title: "Why We Handed Our Agent's Infrastructure to Anthropic — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-why-we-handed-our-agents-infrastructure-to-anthro.md
url: https://every.to/source-code/why-we-handed-our-agent-s-infrastructure-to-anthropic
published: 2026-10-08
ingested: 2026-10-20
domains: [agents]
---

# Why We Handed Our Agent's Infrastructure to Anthropic — Every

Every engineer Paridhi Agarwal explains how the Every Agent, a single Slack agent shared by the whole company, came to run on Claude Managed Agents: why per-employee OpenClaw agents ("pets") were abandoned, why self-hosting even one agent was dropped after a month, how Slack threads map to sessions and credentials stay on Every's servers, and the trade-offs accepted (Claude-only, no zero-data retention, deploy-time hangs, long-session cost and empty replies).

## Influenced pages

- [Claude Managed Agents](../../tools/claude-managed-agents.md) — production customer bullet, Claude-only / no-ZDR and long-session caveats
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — Every Agent no longer "in-progress"; rented machinery
- [Multiplayer AI](../../concepts/multiplayer-ai.md) — first production case against the rubric
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "company agent" term-map row

## Key claims extracted

- Every Agent launched 2026-10-06; built over five months; moved to CMA in early May after a month of self-hosting
- Each Slack thread is a CMA session on a VM costing 8 cents an hour while running; memory is folders of notes read at session start
- App calls pause the agent and are executed by Every's servers with the user's own login; the agent never holds credentials; skill changes need the skill owner's approval
- A small, fast model decides whether to reply, react with an emoji, or stay quiet on untagged thread messages
- Opus 5 made replies grow from ~280 to ~880 characters; Opus 5.5 fixed it
- Rotating idle DMs into a fresh session with a recap cut total cost 39% on replayed conversations
- CMA runs only Claude and is not eligible for zero-data retention; moving off would take months
