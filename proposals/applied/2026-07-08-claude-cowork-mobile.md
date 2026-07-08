---
type: proposal
source: raw/newsletters/2026-07-08-claude-cowork-now-runs-on-mobile.md
status: pending
created: 2026-07-08
---

# Proposal: Claude Cowork web/mobile and scheduled tasks

## Summary

Anthropic expanded Claude Cowork beta to web and mobile for Max subscribers, turning Cowork from a desktop-first agent into a cross-device background work surface. The signal updates Cowork's current status and the agents dashboard.

## Intended changes

- [x] **Update** `wiki/tools/claude-cowork.md` — add web/mobile and scheduled-task status; bump `as_of` and sources.
- [x] **Update** `wiki/state-of/agents.md` — refresh the Cowork leader line and recent changes.
- [x] **Create** `wiki/sources/newsletters/claude-cowork-mobile-2026-07.md` — source summary.

## Page drafts

### wiki/tools/claude-cowork.md (updated sections)

```md
---
title: Claude Cowork
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, agentic]
as_of: 2026-07-08
sources: [claude-cowork-launch, aakash-gupta-cowork, claude-design-launch, claude-productivity-surfaces, anthropic-desktop-agent-expansion-late-march, anthropic-persistent-workflow-surfaces-february, awsai-cowork-bedrock-2026-04-23, claude-cowork-mobile-2026-07]
---

## Current status (as of 2026-07-08)

- Desktop-first agent that works across local files, folders, and everyday applications; now expanded into a cross-device Cowork beta on web and mobile for Max subscribers.
- Users can start delegated work at a desk, monitor it from a phone, and retrieve the final output from any device.
- Scheduled tasks can now run even when the user's computer is closed, strengthening Cowork's position as a background-agent surface rather than only a local desktop app.
- Anthropic extended Fable 5 access on paid plans through 2026-07-12 before moving it to usage credits, making Cowork's economics more usage-sensitive for frontier-model-backed work.
- Positioned for high-effort, repeatable knowledge-work tasks rather than one-off prompt-response use.

## Recent changes

- [2026-07-08] Cowork beta expands to web/mobile for Max subscribers; scheduled tasks can run while the user's computer is closed; Fable 5 access extended through 2026-07-12.
- [2026-05-14] Claude for Small Business and Claude for Legal launched: 27 combined one-click agentic workflows on Cowork, with QuickBooks/PayPal/DocuSign integrations; first direct vertical automation product push
- [2026-04-23] AWS Bedrock public research preview: Cowork now available via Bedrock, keeping prompts, files, and model responses within the customer's AWS account
- [2026-02-25] Cowork added scheduled tasks, making recurring delegated work first-class before the later Dispatch / Channels / Live Artifacts expansion
- [2026-04-21] Added late-March framing: Cowork is positioned as a VM-backed, local-first delegated desktop workflow, not only an April artifact surface
```

### wiki/state-of/agents.md (updated sections)

```md
### Agent orchestration

- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; cross-device background agent for delegated knowledge work, now available on web/mobile beta with scheduled tasks that can run while the user's computer is closed *(as of 2026-07-08)*

## Recent changes

- [2026-07-08] Claude Cowork beta expands to web/mobile and strengthens scheduled background work, making Cowork a cross-device agent surface rather than only a desktop app.
- [2026-07-03] Vercel eve interview adds an agent-framework signal: agents as a new software category needing resumability, long-running jobs, skills, sandboxes, observability, and evals.
- [2026-06-24] Claude Tag beta makes Slack a multiplayer Anthropic agent surface: Claude can be tagged into threads with selected channel/tool/data/codebase access.
```

### wiki/sources/newsletters/claude-cowork-mobile-2026-07.md (new)

```md
---
title: Claude Cowork web/mobile beta
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-08-claude-cowork-now-runs-on-mobile.md
url: https://claude.com/blog/cowork-web-mobile/
published: 2026-07-08
ingested: 2026-07-08
domains: [agents]
---

# Claude Cowork web/mobile beta

The Code reports that Anthropic expanded Claude Cowork beta to web and mobile for Max subscribers. Users can start work at a desk, monitor it from mobile, retrieve outputs across devices, and run scheduled tasks even when the computer is closed.

## Influenced pages

- [Claude Cowork](../../tools/claude-cowork.md) — updates current status and recent changes.
- [State of Agents](../../state-of/agents.md) — refreshes the Cowork orchestration entry.

## Key claims extracted

- Cowork beta is available on web and mobile for Max subscribers.
- Users can start, monitor, and retrieve delegated work across devices.
- Scheduled tasks can run even if the computer is closed.
- Fable 5 access was extended on paid plans through 2026-07-12 before moving to usage credits.
```

## Schema / vocabulary additions

None.
