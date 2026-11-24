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
