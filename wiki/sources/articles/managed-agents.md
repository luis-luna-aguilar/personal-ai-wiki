---
title: 'Scaling Managed Agents: Decoupling the brain from the hands'
type: source
source_type: article
source_file: raw/articles/2026-04-10-anthropiccom-engineering-managed-agents.md
url: https://www.anthropic.com/engineering/managed-agents
published: 2026-04-09
ingested: 2026-04-10
domains: [agents]
---

# Scaling Managed Agents: Decoupling the brain from the hands

Anthropic presents Managed Agents, a hosted Claude Platform runtime for long-horizon agents built around decoupling the harness ("brain"), execution environments ("hands"), and durable session log. The post is mostly an architecture explanation rather than a conventional product launch: replace single-container agent designs with stable interfaces so failures can be recovered independently, secrets stay out of sandboxes, and the platform can adapt as model capabilities change.

## Influenced pages

- [[tools/claude-managed-agents]] — new tool page, main subject of the ingest
- [[state-of/agents]] — adds a broader `agent-orchestration` subcategory entry for Claude Managed Agents

## Key claims extracted

- Managed Agents is a hosted Claude Platform service for long-running agents
- Anthropic virtualizes three components: **session**, **harness**, and **sandbox**
- The harness no longer lives inside the execution container; it calls sandboxes/tools via `execute(name, input) -> string`
- Sandboxes can be reprovisioned with a standard recipe such as `provision({resources})`
- Harness failures can be recovered by restarting and resuming from the session log with operations like `wake(sessionId)`, `getSession(id)`, and `emitEvent(id, event)`
- The session is treated as durable context outside Claude's live context window and can be queried via `getEvents()`
- Event slices can be transformed in the harness before being passed back into the model context
- Credentials are kept structurally out of the sandbox
- Git auth can be wired into the local remote during sandbox initialization without exposing the token inside the sandbox
- MCP tools can be called through a proxy that fetches OAuth credentials from a secure vault
- Decoupling the brain from the hands let Anthropic provision containers only when needed
- Reported latency effect: roughly **60% lower median time-to-first-token** and **over 90% lower p95 time-to-first-token**
- The architecture supports connecting Claude to customer-owned infrastructure, including VPC resources
- The platform is meant to support many brains and many hands rather than a single agent bound to one container

## Caveats

- This is an Anthropic engineering post, not a neutral benchmark or third-party evaluation
- The post gives interface shapes and architectural claims, but not full public API docs, pricing, or product limits
- The TTFT improvements are reported without a public methodology section in the captured source
