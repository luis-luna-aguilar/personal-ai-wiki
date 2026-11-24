---
type: proposal
source: raw/articles/2026-09-10-openaicom-indexintroducing-the-agents-ap.md
sources:
  - raw/articles/2026-09-10-openaicom-indexintroducing-the-agents-ap.md
  - raw/newsletters/2026-09-12-ainews-deepseek-v41-flash-763b-p8b-d16b-novel.md
status: pending
created: 2026-11-24
---

# Proposal: OpenAI Agents API — sandbox choice, subagents, tool search, vaults, no platform fee

## Summary

### In short
OpenAI's Agents API sells the Codex harness as a managed service while leaving the compute choice to the developer, and it charges nothing on top of tokens and tools. Developers can run agents in an OpenAI-hosted sandbox, on their own infrastructure, or with one of nine sandbox partners, and they get built-in subagents, tool search, programmatic tool calling and credential vaults. The proposal adds these specifics to the existing Agents API bullet on **Agent execution runtimes** and creates one source page. The one thing to settle is a date: the wiki dates the API to DevDay (29 September), but the launch post is dated 10 September.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 10 September 2026 OpenAI published the launch post for the Agents API, in public beta for all developers. The pitch is that long-running agents need two things: a harness that manages context, tools and subagents, and infrastructure that keeps the agent running for days in an environment where it can work with files and run code. OpenAI offers the harness behind Codex as an API and keeps improving it with each model launch, so developers get new model capabilities without rewriting their own loop. The harness is open source, so its logic can be inspected.

The compute is the developer's choice. OpenAI's own hosted sandbox uses the infrastructure behind Codex and ChatGPT and can be preloaded with files, packages, skills and plugins. Agents can also run on the customer's own infrastructure or on one of nine partners: Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop and Vercel. A session is one API call naming the task, model, tools and environment. Subagents are switched on with a `multi_agent` setting that caps how many run at once; each keeps its own context while the main agent merges results. Tool search loads tool definitions only when needed, and programmatic tool calling lets the agent run, chain and filter calls in code so that only relevant results enter its context. Credentials are passed as vault IDs. The API supports MCP, custom functions and built-in web search, and compacts context automatically near the limit. There is no fee beyond tokens and tools.

### What changes
The wiki already describes the Agents API from DevDay coverage: the Codex harness with computer use and compaction, plus the Responses API changes. It lacks the sandbox options, subagents, tool search, vaults and pricing.

- **Agent execution runtimes** gains two sentences in the "Model-lab agent APIs" bullet and a clause in the matching Current-status bullet, a Recent-changes entry dated 10 September and the new source. Page date stays at 24 November.
- One new source page for the launch post.

### What to weigh
The partner list resembles the one on the separate **OpenAI Agents SDK** page; the drafts name the API explicitly so the two products are not merged. The Ciridae customer quote and the sample code's model name are left out as launch-time detail.

## Intended changes

- [ ] **Update** `wiki/concepts/agent-execution-runtimes.md` — extend the "Model-lab agent APIs" bullet and the Agents API Current-status bullet; adds one Recent-changes entry dated 2026-09-10 (list goes from 9 to 10, at the cap, no spill); append `openai-introducing-agents-api-2026-09-10` to frontmatter `sources:` and one line to `## Sources`; `as_of` stays 2026-11-24 and the Current-status stamp stays 2026-11-23
    > See draft below

- [ ] **Create** `wiki/sources/articles/openai-introducing-agents-api-2026-09-10.md` — source summary

## Page drafts

### wiki/concepts/agent-execution-runtimes.md (updated)

Frontmatter `sources:` appends `openai-introducing-agents-api-2026-09-10`; `as_of` unchanged (2026-11-24).

In `## Current status (as of 2026-11-23)`, the last bullet is replaced:

```
- Model labs now ship their own harness as an API: OpenAI's Agents API gives developers the Codex harness with computer use, compaction and subagents built in, runs it in an OpenAI-hosted, self-hosted or partner sandbox, and charges nothing beyond tokens and tools.
```

In `## Execution runtimes`, the "Model-lab agent APIs" bullet gains two sentences after its first sentence (the rest of the bullet is unchanged):

```
- **Model-lab agent APIs.** OpenAI's Agents API (DevDay, 2026-09-29) packages the Codex harness, including the same computer-use implementation the models are trained on, and runs OpenAI's own Codex Security and meeting-notes features. The harness is open source and maintained by OpenAI, but the compute is the developer's choice: an OpenAI-hosted sandbox (the infrastructure behind Codex and ChatGPT, preloadable with files, packages, skills and plugins), the developer's own infrastructure, or one of nine partners (Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, Vercel). Built in are subagents with a concurrency cap (`max_concurrent_subagents`), tool search, programmatic tool calling, credential vaults passed by ID, MCP and web search, with no fee beyond tokens and tools (public beta). The lower-level Responses API gained async tool calls (the model keeps reasoning while a tool runs), mid-turn steering over WebSockets, guaranteed 30-minute cache hits with a 12-hour retention tier for long-lived agent threads (previewed at DevDay, announced for the API around 2026-10-20, with mixed retention durations allowed within one request; DeepSeek's DeepInfer keeps agent prefixes for three days), cache pre-warming, and server-side compaction at a token threshold, with a manual `/compact` that big coding agents prefer. API lead Nikunj Handa calls the right level of abstraction (memory, storage) an open question. By November 2026 background mode covers multi-step agent runs: the application sends each turn as an asynchronous request, learns of completion by webhook or polling, and links follow-ups with a `continuation_id`; choosing a `2h` or `8h` completion window cuts token prices 30% or 40%, and these windows replace Flex processing on new models ([OpenAI discounted async processing](../workflows/async-discounted-processing.md)).
```

In `## Recent changes`, insert directly below the 2026-09-22 entry (date order):

```
- [2026-09-10] OpenAI's Agents API launch post: hosted, self-hosted or partner sandboxes (nine partners), built-in subagents, tool search and programmatic tool calling, credential vaults, no fee beyond tokens and tools.
```

In `## Sources`, append:

```
- [OpenAI — Introducing the Agents API](../sources/articles/openai-introducing-agents-api-2026-09-10.md)
```

### wiki/sources/articles/openai-introducing-agents-api-2026-09-10.md (new)

```
---
title: OpenAI — Introducing the Agents API
type: source
source_type: article
source_file: raw/articles/2026-09-10-openaicom-indexintroducing-the-agents-ap.md
url: https://openai.com/index/introducing-the-agents-api/
published: 2026-09-10
ingested: 2026-11-24
domains: [agents]
---

# OpenAI — Introducing the Agents API

OpenAI's launch post for the Agents API in public beta: the open-source Codex harness offered as a managed API, so developers can create a long-running cloud agent in one call that names the task, model, tools and environment. OpenAI maintains the harness and ships improvements with each model launch; the developer picks where the agent runs. AINews (2026-09-12) carried it as part of a wider move to collapse model, runtime and sandbox into one surface.

## Influenced pages
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — sandbox options, subagents, tool search, vaults and pricing added to the Model-lab agent APIs bullet

## Key claims extracted
- Public beta for all developers; no additional fee beyond tokens and tools
- Environments: OpenAI-hosted sandbox (same infrastructure as Codex and ChatGPT; configurable with files, packages, skills and plugins), the developer's own infrastructure, or partners Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop and Vercel
- Built-in subagents via `multi_agent` with `max_concurrent_subagents`; each subagent keeps its own context and the main agent merges results
- Tool search loads tool definitions on demand; programmatic tool calling runs, chains and filters tool calls in code
- Automatic context compaction near the context limit
- Credentials passed as `vault_ids`; supports MCP, custom functions and built-in web search
- Harness is open source; versioned access to new harness capabilities with each model launch
```

## Schema / vocabulary additions

None.

## Open questions

- The page dates the Agents API to DevDay (2026-09-29), but OpenAI's launch post is dated 2026-09-10 and DevDay coverage described it after the fact. Should the bullet's "(DevDay, 2026-09-29)" be corrected to "(public beta 2026-09-10)" as part of this change? The drafts leave it as is.
	- Yes
