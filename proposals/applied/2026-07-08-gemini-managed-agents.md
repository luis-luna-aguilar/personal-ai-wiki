---
type: proposal
source: raw/newsletters/2026-07-08-claude-cowork-now-runs-on-mobile.md
status: pending
created: 2026-07-08
---

# Proposal: Gemini managed agents infrastructure

## Summary

Google is turning managed-agent primitives into Gemini API platform features: MCP support, background execution, custom function calling, credential refresh, and the Interactions API as a stateful agent interface. This updates Gemini and the harness/agents pages.

## Intended changes

- [x] **Update** `wiki/tools/gemini.md` — add managed-agent API status and recent change.
- [x] **Update** `wiki/state-of/agents.md` — add Gemini managed agents to agent frameworks/platforms.
- [x] **Update** `wiki/concepts/harness.md` — add managed-agent platform primitives as harness infrastructure.
- [x] **Create** `wiki/sources/newsletters/gemini-managed-agents-2026-07.md` — source summary.

## Page drafts

### wiki/tools/gemini.md (updated sections)

```md
---
title: Gemini
type: tool
domains: [models, computer-use, agents]
subcategory: ai-assistant
tags: [google, closed-source]
as_of: 2026-07-08
sources: [gemini-browser-utility-updates, gemini-deep-research-max, ainews-2026-04-22, google-cloud-next-2026, gemini-downloadable-files-2026-04-30, gemini-computer-use-aside-2026-06, gemini-managed-agents-2026-07]
---

**Managed agents in Gemini API (as of 2026-07-08):**

Google added hosted-agent primitives to the Gemini API: MCP support for direct access to internal tools and databases, background execution for long-running tasks, custom function calling, and credential refresh across interactions. AINews also describes the Gemini Interactions API as GA and the new default interface for Gemini models and agents, combining models, agents, async execution, tool support, multimodal generation, and managed execution surfaces.

## Recent changes

- [2026-07-08] Gemini API managed agents add MCP support, background execution, custom function calling, and credential refresh; AINews frames Interactions API as Google's default stateful interface for models and agents.
- [2026-06-25] Gemini 3.5 Flash adds built-in computer use for browser, desktop, and mobile with sensitive-action confirmations and prompt-injection shutdown behavior.
```

### wiki/state-of/agents.md (updated sections)

```md
### Agent frameworks

- [Gemini](../tools/gemini.md) / Gemini API managed agents — Google; hosted managed-agent interface with MCP support, background execution, custom function calling, credential refresh, and Interactions API statefulness *(as of 2026-07-08)*
- [Google ADK](../tools/google-adk.md) — Google; open-source ADK now positioned as the developer layer inside Gemini Enterprise Agent Platform; Agent Studio adds a low-code wrapper, and Model Garden expands the surrounding stack to 200+ models *(as of 2026-04-23)*

## Recent changes

- [2026-07-08] Google managed agents in the Gemini API add MCP support, background execution, custom function calling, and credential refresh, making hosted agent runtime features first-party Gemini primitives.
- [2026-07-03] Vercel eve interview adds an agent-framework signal: agents as a new software category needing resumability, long-running jobs, skills, sandboxes, observability, and evals.
```

### wiki/concepts/harness.md (updated sections)

```md
## What good harness engineering looks like

- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution. Google adding these to the Gemini API is another sign that "harness" is becoming product infrastructure, not only application code.

## Recent changes

- [2026-07-08] Gemini API managed agents add hosted harness primitives: MCP support, background execution, custom function calling, credential refresh, and stateful agent interactions.
- [2026-07-01] Added agent recipes as a harness packaging pattern: model choices, evals, judges, human expertise, failure history, and signal processing bundled with the workflow.
```

### wiki/sources/newsletters/gemini-managed-agents-2026-07.md (new)

```md
---
title: Gemini managed agents in the API
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-08-claude-cowork-now-runs-on-mobile.md
url: https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api/
published: 2026-07-08
ingested: 2026-07-08
domains: [agents, models]
tags: [google]
---

# Gemini managed agents in the API

The Code reports that Google added four production-oriented upgrades to hosted agents in the Gemini API: MCP support, background execution, custom function calling, and credential refresh. AINews adds that the Gemini Interactions API is now the default stateful surface for Gemini models and agents.

## Influenced pages

- [Gemini](../../tools/gemini.md) — adds managed-agent API status.
- [State of Agents](../../state-of/agents.md) — adds Gemini managed agents under frameworks/platforms.
- [Harness](../../concepts/harness.md) — adds managed-agent platform primitives.

## Key claims extracted

- MCP support lets Gemini agents connect directly to internal databases and APIs.
- Background execution lets long-running work continue server-side.
- Custom function calling and credential refresh make long sessions more durable.
- AINews frames Interactions API as a default stateful interface for Gemini models and agents.
```

## Schema / vocabulary additions

None.
