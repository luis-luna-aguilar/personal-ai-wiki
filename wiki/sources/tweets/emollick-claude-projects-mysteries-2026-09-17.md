---
title: 'Ethan Mollick (@emollick) — Claude Projects handles teams of agents'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-26-emollick-2100665801800093959.md
url: https://x.com/emollick/status/2100665801800093959
published: 2026-09-17
ingested: 2026-10-26
domains: [agents]
---

# Ethan Mollick (@emollick) — Claude Projects handles teams of agents

Ethan Mollick (Wharton) describes an early-access Claude Projects run in which an orchestrator agent built a small organization of agents to investigate 18 historical mysteries over a day. Results are published at historical-mysteries.netlify.app, with research notes in the open-source emollick/historical_fun repo.

## Influenced pages

- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — worked example of coordinator-specialist routing in Projects

## Key claims extracted

- You talk to one main orchestrator agent and it spins up specialists, mixing expensive and cheap agents according to your preferences
- Asked Claude Fable to select historical mysteries to try to resolve; it ran research agents, chose mysteries based on accessible data, and opened 18 threads, one per mystery
- Each thread launched more agents (e.g. avalanche simulation, code-breaking), then passed summaries to write-up agents and a separate set of skeptical fact-check agents
- About a day of work, organized by the central orchestrator
- Caveats: tokens were unlimited during early access, so costs are unknown; results are "for fun", not definitive or error-free, but mostly reasonable and grounded in the literature; Mollick takes no money from AI labs
