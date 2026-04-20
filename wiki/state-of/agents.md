---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-15
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents, agentic-thinking-lin, curiosity-driven-imagination, openai-agents-sdk-evolution]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

## Subcategories

### Agent orchestration UIs

Surfaces (desktop, web, mobile, chat) where humans supervise, hand off, and review work across multiple AI agents running in parallel.

- [[tools/cursor]] — Cursor 3's desktop app surfaces local and cloud agents in one sidebar, with handoff between environments and demos/screenshots from cloud agents *(as of 2026-04-02)*

### Agent orchestration

Platforms that run or coordinate long-horizon agents across execution environments, instead of only exposing a local loop or a thin UI over one agent.

- [[tools/claude-managed-agents]] — Anthropic's hosted runtime separates session, harness, and sandbox so long-running agents can recover from failures, attach tools or customer infrastructure, and start faster when no sandbox is needed immediately *(as of 2026-04-09)*
- [[tools/openai-agents-sdk]] — OpenAI's updated SDK combines a model-native harness with native sandbox execution, durable checkpoint / rehydration, provider-neutral manifests, and built-in support for MCP, skills, AGENTS.md, shell, and `apply_patch` *(as of 2026-04-15)*

### Model orchestration

Patterns that combine models of different sizes or costs inside a single agentic task. Concerned with *how* agents are structured internally (which model runs the loop, which model steps in when), not with the user-facing surface.

- [[workflows/advisor-strategy]] — Anthropic: a small executor (Sonnet or Haiku) drives the loop and escalates to Opus as an *advisor* only when stuck. Shipped as a server-side `advisor_20260301` tool on the Claude API, making it a one-line change to a Messages request. Reported +2.7% on SWE-bench Multilingual *and* −11.9% cost for Sonnet+Opus-advisor vs Sonnet alone *(as of 2026-04-09)*

### Agentic DevOps

Agent-compatible tools that let a model provision external services and receive credentials through a repeatable CLI workflow instead of clicking through SaaS dashboards.

- [[tools/stripe-cli]] — Stripe explicitly pitches the CLI `projects` flow for "you or your agents": provision services across providers, sync credentials back to the environment, and manage upgrades or billing from the CLI *(as of 2026-04-09)*

## Recent changes

- [2026-04-15] Added [[tools/openai-agents-sdk]] under `agent-orchestration` after ingesting OpenAI's Agents SDK evolution post.
- [2025-03-06] Added [[concepts/curiosity-driven-imagination]] — paper pattern for agents that recover from broken plans by exploring, learning new steps, and turning them into guided rewards
- [2026-04-10] Added [[concepts/agentic-thinking]] — Junyang Lin's essay on the shift from reasoning to agentic thinking
- [2026-04-09] Added `agent-orchestration` with [[tools/claude-managed-agents]] after ingesting Anthropic's Managed Agents architecture post.
- [2026-04-09] Added `agentic-devops` subcategory with [[tools/stripe-cli]] after ingesting the `projects.dev` landing page
- [2026-04-09] Added `model-orchestration` subcategory with [[workflows/advisor-strategy]] after ingesting Anthropic's advisor-strategy launch post.
- [2026-04-02] First content for this page. Added `agent-orchestration-ui` subcategory with Cursor after ingesting the Cursor 3 launch post.
