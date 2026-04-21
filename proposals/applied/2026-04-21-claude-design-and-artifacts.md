---
type: proposal
sources:
  - raw/tweets/2026-04-21-claudeai-2045156267690213649.md
  - raw/newsletters/2026-04-18-ainews-the-two-sides-of-openclaw.md
  - raw/tweets/2026-04-21-xcom-felixriesebergstatus2046334841-1.md
  - raw/tweets/2026-04-21-aakashgupta-2046331327780356219.md
status: pending
created: 2026-04-21
---

# Proposal: Claude Design and live artifacts expand Anthropic beyond chat

## Summary

This batch adds a missing product-layer story around Anthropic: Opus 4.7 is not just a model release. Claude Design turns natural-language prompting into prototypes, slides, and one-pagers, while Cowork's Live Artifacts turns connectors into persistent dashboards and reports. The wiki already has Cowork, but it understates the broader "artifact-first agent" direction.

## Intended changes

- [x] **Update** `wiki/tools/claude-cowork.md` — broaden the page from dashboard pressure to Anthropic's larger artifact workflow
  > Add that Cowork now sits alongside Claude Design in a broader Anthropic push toward generated business artifacts, not just delegated desktop tasks.

- [x] **Update** `wiki/models/claude-opus-4-7.md` — add a product-level implication of the vision upgrade
  > Add a `Current status` bullet:
  > `- Powers Claude Design, Anthropic's research-preview surface for prototypes, slides, and one-pagers`

- [x] **Update** `wiki/state-of/agents.md` — make Cowork's line explicitly mention the surrounding artifact-generation direction
  > Replace the current Cowork line with:
  > `- [[tools/claude-cowork]] — Anthropic; desktop knowledge-work agent with Live Artifacts, released alongside Claude Design as part of a broader push toward generated dashboards, reports, and prototypes *(as of 2026-04-21)*`

- [x] **Create** `wiki/sources/tweets/claude-design-launch.md` — source summary for the official launch signal
  > See draft below.

## Page drafts

### wiki/tools/claude-cowork.md (updated snippet)

```md
## Current status (as of 2026-04-21)

- Desktop-first agent that works where most knowledge work happens: local files, folders, and everyday applications
- Live Artifacts shipped in April 2026: dashboards, trackers, and reports wired to connectors that auto-refresh on open
- Reported connectors include Slack, Salesforce, Google Drive, Asana, and Jira
- Released in the same product moment as Claude Design, Anthropic's research-preview surface for prototypes, slides, and one-pagers

## Why it matters

Cowork pushes agent UX beyond chat and toward delegated desktop work. The adjacent Claude Design launch suggests Anthropic is also moving toward artifact-first interfaces: not just answering questions, but producing living dashboards, reports, decks, and prototypes as first-class outputs.
```

### wiki/sources/tweets/claude-design-launch.md (new)

```md
---
title: Claude Design launch
type: source
source_type: tweet
source_file: raw/tweets/2026-04-21-claudeai-2045156267690213649.md
url: https://x.com/claudeai/status/2045156267690213649
published: 2026-04-21
ingested: 2026-04-21
domains: [models, agents]
---

# Claude Design launch

Anthropic announces Claude Design, a research-preview surface for generating prototypes, slides, and one-pagers by talking to Claude. The launch ties the product directly to Opus 4.7's improved visual capability and makes artifact generation a first-class Anthropic workflow.

## Key claims extracted

- Claude Design generates prototypes, slides, and one-pagers from natural language
- Anthropic ties the product directly to Opus 4.7 as its most capable vision model
- Available in research preview on Pro, Max, Team, and Enterprise plans
```

## Comments

- I want to have Claude Design as a separate tool from Cowork, because it is. Make sure to document it separate. I approved the pages creation, but do it separate from Cowork.