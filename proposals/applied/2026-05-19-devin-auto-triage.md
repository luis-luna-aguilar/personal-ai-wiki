---
type: proposal
sources:
  - raw/newsletters/2026-05-19-ainews-how-to-land-a-job-at-a-frontier-lab-on-p.md
  - raw/newsletters/2026-05-19-the-ai-boom-divides-silicon-valley.md
status: pending
created: 2026-05-19
---

# Proposal: Cognition ships Devin Auto-Triage — always-on persistent bug triage agent

## Summary

Cognition shipped Auto-Triage, a persistent Devin agent that monitors Slack channels and investigates bugs as they're reported. A parent Devin filters noise, then spins up focused sub-sessions to find root causes, post diagnoses, and tag code owners. Shared long-term memory deduplicates repeat reports. Early users (Modal) describe it as more useful than homegrown triage automations.

## Intended changes

- [x] **Update** `wiki/state-of/agents.md` — add Devin Auto-Triage to the `### Persistent coding agents` subcategory; add recent-change entry
    > See diff below

- [x] **Create** `wiki/sources/articles/devin-auto-triage-2026-05.md` — source summary page

## Page drafts

### wiki/state-of/agents.md — update `### Persistent coding agents`

Add after the OpenClaw bullet:

```md
- **Devin Auto-Triage** — Cognition; always-on persistent agent that monitors Slack channels and investigates bugs as reported; parent Devin filters noise and dispatches focused sub-sessions; shared long-term memory for deduplication across repeat reports; early users (Modal) describe it as more useful than homegrown triage automations *(as of 2026-05-19)*
```

Add to `## Recent changes`:

```
- [2026-05-19] Devin Auto-Triage: Cognition ships the first always-on session-persistent bug triage agent; Slack monitoring + parent/child Devin structure + long-term deduplication memory
```

### wiki/sources/articles/devin-auto-triage-2026-05.md (new)

```md
---
title: Devin Auto-Triage launch
type: source
source_type: article
url: https://x.com/cognition/status/2056396941181727210
published: 2026-05-19
ingested: 2026-05-19
domains: [agents, coding]
---

# Devin Auto-Triage launch

Cognition launched Auto-Triage, a persistent Devin agent that operates in Slack as an always-on first responder for bugs, alerts, and incidents. A manager Devin filters noise; focused sub-sessions find root causes, post diagnoses, and tag code owners. Shared long-term memory deduplicates repeat reports. Early adopter Modal called it more useful than typical homegrown triage automations.

## Influenced pages

- [State of Agents](../../state-of/agents.md) — added to Persistent coding agents subcategory

## Key claims extracted

- Always-on persistent Devin monitors Slack channels for bug reports
- Parent Devin filters noise before spinning up focused sub-sessions
- Shared long-term memory deduplicates repeat reports and learns team ownership map
- Generates PR candidates in addition to diagnoses
- Modal (early user): more useful than homegrown triage automations
```

## Open questions

- Should Devin get its own `wiki/tools/devin.md` page given this is a notable product milestone? Currently no Devin page in the wiki. Could be created with this as the first full-ingest source.
	- Yes, lets create its own tool page and locate everything Devin in there
