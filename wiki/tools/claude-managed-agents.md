---
title: Claude Managed Agents
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, closed-source, agentic]
as_of: 2026-10-12
sources: [managed-agents, every-managed-agents-vibe-check, anthropic-platform-expansion-april-2026, claude-managed-agents-memory, anthropic-spacex-dreams-2026-05-07, claude-managed-agents-feature-parity-2026-05-13, claude-managed-agents-updates-2026-05, anthropic-is-onto-something, ainews-openai-agi-bar-2026-08-28, every-agent-claude-managed-agents-2026-10-08, every-agent-token-efficiency-2026-10-07, ainews-cma-flows-agent-teams-2026-10-10, latent-space-claude-dynamic-workflows-2026-10-12]
---

# Claude Managed Agents

Claude Managed Agents is a hosted Claude Platform runtime for long-running agents, in public beta, built around three separate pieces instead of one all-in-one agent container.

Those three pieces are:

- a durable **session** log that stores what happened
- a **harness**, meaning the loop that runs Claude and decides when to call tools
- one or more **sandboxes/tools** that do the actual work

Anthropic's core idea is that these pieces should be decoupled so the system can keep evolving as models improve, without forcing users to rebuild around each model generation's quirks.

## Current status (as of 2026-10-12)

- Public beta service on the Claude Platform for long-running agents
- Official launch framing: developers specify tasks and tools while Anthropic handles orchestration, permissions, and sandboxing
- Handles agent infrastructure primitives including sessions, memory, tool use, and credentials
- Anthropic is simultaneously expanding adjacent agent surfaces: custom agents inside Claude for packaged recurring jobs, and longer-running monitor/loop patterns in Claude Code
- Core abstractions in the post: `session`, `harness`, `sandbox`
- Harness is decoupled from the execution container and calls tools through a generic interface like `execute(name, input) -> string`
- Session lives outside the harness as an append-only event log and can be resumed with operations like `wake(sessionId)`, `getSession(id)`, `emitEvent(id, event)`, and `getEvents()`
- Sandboxes are provisioned on demand instead of being assumed to exist for every session from the start
- Designed to connect Claude to customer infrastructure, including resources in a customer's own VPC
- Supports MCP-backed tools with OAuth credentials stored outside the sandbox in a secure vault
- Every reports that Spiral used the service to spin up a new agent in a few hours; the cited benefit was less custom infrastructure maintenance, not just faster initial coding
- **Every Agent in production (October 2026):** Every built @Every, one Slack agent shared by the whole company, on CMA after a month of self-hosting a single agent persuaded it not to run its own infrastructure. Each Slack thread is one session on a VM billed at 8 cents an hour while running; memory is folders of notes the agent reads at session start; app calls pause the agent and are made by Every's servers with the asking user's own login, so the agent never holds a credential.
- Existing agents can be updated through the dashboard by changing the system prompt or underlying model and saving
- Built-in memory is now in public beta: memories are mounted as files on the agent filesystem instead of hidden inside a proprietary opaque memory layer
- Memory stores can be shared across agents with scoped permissions (for example org-wide read-only plus per-user read/write)
- Changes are tracked with audit logs and surfaced as session events in the Claude Console; developers can roll back or redact prior memory state
- Anthropic is explicitly pitching memory as a way to replace custom retrieval / memory infrastructure for long-running agent deployments
- **Dreams feature** (May 2026, research preview): agents periodically reflect on past sessions to identify long-term patterns that no single session can surface — recurring mistakes, shared user preferences, stale assumptions. The reflection produces a cleaned-up, consolidated memory store that improves future session performance. Available in research preview; request access via Claude's form.
- Anthropic says new Claude API features such as advisor strategy, code execution, and web search ship same-day into Managed Agents, reinforcing the product as a hosted platform service rather than a static sample runtime.
- **Self-hosted sandboxes** (public beta, announced at Code with Claude London, May 2026): tool execution can run on the customer's own infrastructure or through a supported managed provider (Cloudflare, Daytona, Modal, Vercel), while Anthropic's hosted agent loop — orchestration, context management, error recovery — stays on Anthropic's side. Sensitive files, packages, and services never leave the customer's perimeter; the customer controls compute sizing and the runtime image.
- **MCP tunnels** (research preview): let Managed Agents reach MCP servers inside a private network without exposing them to the public internet. A lightweight gateway the customer deploys makes a single outbound connection — no inbound firewall rules, no public endpoints, traffic encrypted end to end. Supported in both Managed Agents and the Messages API; managed from Claude Console workspace settings by org admins.
- **General availability (August 2026):** computer use, the browser tool, the Skills API (versioned reusable procedures), and the Files API (now with expiration control, 5x higher rate limits to 500 RPM, and 1 TB/org) all moved from research preview to GA, alongside an AG-UI adapter that maps chat threads to managed sessions and streams text, tool calls, and thinking into custom UIs.
- **Vercel Chat SDK cookbook:** Anthropic published a cookbook connecting Managed Agents to Vercel's Chat SDK, giving a unified chat layer with server-side harness, session management, and memory — packaging the pattern as a reusable recipe rather than bespoke integration work.

### Dynamic workflows (flows)

- **Dynamic workflows, or "flows" (public beta, October 2026):** the API version of Claude Code's dynamic workflows, enabled with the `multiagent_20261001` beta. A lead agent plans in phases and writes an orchestration program that launches subagents (up to 1,000 per run), collects results, and manages what each sees, replacing the developer-configured coordinator and subagent roster; preconfigured subagents can still be passed in. Subagents share a filesystem but cannot message each other through the API. The model does not know its budget while running, so developers set a session budget, and Anthropic advises starting with scoped tasks because token use can be high. The Console graphs every lead-to-subagent payload. Anthropic suggests the Dreams feature (which rewrites a memory store from past transcripts, merging duplicates and replacing stale entries) to make repeated flows cheaper. See [Multi-agent coordination](../workflows/multi-agent-coordination.md).

## Why it matters

Many agent systems still bundle the model loop, execution environment, secrets, and state into one long-lived process or container. Anthropic's claim is that this becomes brittle over time: fixes made for one model generation can turn into dead weight for the next.

Managed Agents moves the durable state outside the live context window and keeps credentials outside the sandbox where generated code runs. That makes it easier to recover from failures, reconnect a session to a fresh harness, attach multiple execution environments, and change the implementation underneath without changing the top-level shape of the system.

Every's practitioner read adds a product-adoption angle: if the hosted primitive works well enough, teams that have been building custom agent infrastructure may redirect effort away from sessions, memory, tool calling, credentials, and prompt/model deployment machinery toward the domain-specific behavior of the agent itself.

It also looks less like a one-off architecture post when viewed alongside the surrounding Anthropic product cadence. Managed Agents, custom agents inside Claude, and Claude Code's event-driven/background workflows all point toward the same direction: Anthropic wants the durable agent loop to live on its platform rather than only inside one local session or one-off prompt.

Anthropic is making a strong product bet on inspectable file-backed memory rather than magical hidden persistence. That matters because it keeps memory legible to developers, reviewable for enterprise governance, and compatible with the same bash/code tools agents already use.

## Architecture

### Brain, hands, session

- **Brain:** Claude plus the harness that runs the loop
- **Hands:** sandboxes and external tools that execute actions
- **Session:** durable event log of what happened

Each piece can fail or be replaced independently. If a sandbox dies, that shows up as a tool-call failure and a fresh sandbox can be provisioned. If the harness dies, a new one can restart and resume from the session log.

### Session outside the context window

Anthropic explicitly treats the session as recoverable context that lives outside Claude's live context window. The harness can fetch slices of earlier events and decide what to pass back into the prompt, instead of relying only on irreversible summarization or trimming.

### Security boundary

The post argues for a structural security boundary: secrets should never be reachable from the sandbox where Claude-generated code runs.

- Git credentials can be wired into the local remote during sandbox setup without exposing the token to the agent
- MCP calls can go through a proxy that looks up session-bound credentials from a secure vault
- The harness itself does not need direct access to user credentials

## Reported operational gains

Anthropic reports faster startup after decoupling the brain from the hands.

- **p50 TTFT** means the median time-to-first-token: half of sessions started faster than this
- **p95 TTFT** means the slower tail: 95% of sessions started within this time
- Reported result: roughly **60% lower p50 TTFT**
- Reported result: **over 90% lower p95 TTFT**

The simple reason is that sessions that do not need a sandbox immediately can start inference before any container is provisioned.

## Strengths

- Clear separation between state, orchestration logic, and execution environments
- Better failure recovery story than single-container agent designs
- Security model is structural, not only prompt- or policy-based
- Better fit for enterprise setups where Claude needs to reach customer-owned infrastructure
- Makes multi-agent and multi-environment orchestration easier to reason about
- Reduces the amount of custom agent infrastructure product teams have to maintain if the hosted service fits their use case
- Dashboard-based prompt/model updates can make existing agents easier to iterate
- Fits a broader Anthropic platform move instead of standing alone as an isolated runtime

## Weaknesses / caveats

- The adjacent "custom agents" surface is still thinly documented in the current source set. Here it should be read as preconfigured recurring agents for specific jobs, not a fully separate platform category.
- Session VM pricing is known only from Every's account (8 cents an hour while running); token cost follows the Claude model chosen per session
- **Claude-only, no zero-data retention.** CMA runs only Claude models: a session can pick a cheaper Claude model, but there is no routing to other labs. Because it keeps session history to resume work, it is not eligible for Anthropic's zero-data-retention option. Every's own inventory of what leaving would take (harness, sessions, memory, tools, sandboxes) came to months of work.
- **Long sessions need rotating.** A three-day DM session kept paying to rewrite its whole history into the cache, and near the context limit Opus sometimes returned empty replies. Starting a fresh session with a short recap once a DM goes quiet cut total cost 39% on replayed conversations. Teams running their own servers beside the hosted agent must answer outstanding tool requests before a deploy, or the agent hangs.
- Reported latency improvements are vendor-internal numbers
- Every's Spiral example is a practitioner anecdote, not a broad evaluation
- The post and mini-vibe-check explain the platform shape better than current limits, production constraints, or failure cases

## Related

- [Advisor strategy](../workflows/advisor-strategy.md)
- [Agents](../state-of/agents.md)

## Recent changes

- [2026-10-12] Dynamic workflows ("flows") in public beta: the lead agent writes its own multi-agent orchestration, up to 1,000 agents per run; session budgets, shared filesystem, Console payload graph.
- [2026-10-08] Every's production account of the Every Agent: thread-per-session on 8¢/hour VMs, credential proxying through its own servers, and the limits it lives with (Claude-only, no zero-data retention, long sessions rotated with a recap for −39% cost).
- [2026-08-28] Computer use, browser tool, Skills API, and Files API reach general availability (plus higher Files API rate limits and 1 TB/org); AG-UI adapter added; Vercel Chat SDK cookbook published.
- [2026-05-20] Anthropic shipped self-hosted sandboxes (public beta) and MCP tunnels (research preview): tool execution can run on customer infrastructure or through Cloudflare/Daytona/Modal/Vercel while Anthropic keeps the orchestration loop; MCP tunnels reach private MCP servers without exposing them publicly.
- [2026-05-13] Anthropic says Managed Agents receives new Claude API capabilities such as advisor strategy, code execution, and web search on the same day they ship.
- [2026-05-07] Dreams feature added (research preview): periodic session reflection producing consolidated memory stores for long-term pattern recognition across sessions; available via research preview access request
- [2026-04-24] Built-in memory launched in public beta: file-backed stores, scoped sharing, audit logs, rollback/redaction controls, and Claude Console event visibility
- [2026-04-15] Official launch framing and adjacent custom-agent / long-running-workflow signals make Managed Agents look less like a one-off architecture post and more like Anthropic's core platform direction
- [2026-04-15] Every reported Claude Managed Agents is in public beta and highlighted Spiral's use of it to create an agent in a few hours while offloading sessions, memory, tool use, and credential handling

## Sources

- [Scaling Managed Agents: Decoupling the brain from the hands](../sources/articles/managed-agents.md)
- [Mini-Vibe Check: Claude Managed Agents Handle the Infrastructure Work](../sources/articles/every-managed-agents-vibe-check.md)
- [Anthropic platform expansion — April 2026](../sources/newsletters/anthropic-platform-expansion-april-2026.md)
- [Built-in memory for Claude Managed Agents](../sources/articles/claude-managed-agents-memory.md)
- [Claude Managed Agents same-day Claude API feature parity](../sources/tweets/claude-managed-agents-feature-parity-2026-05-13.md)
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [The Code — Anthropic is onto something (2026-05-20)](../sources/newsletters/anthropic-is-onto-something.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [Every — Why We Handed Our Agent's Infrastructure to Anthropic](../sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md)
- [Every — Building a More Efficient Agent](../sources/newsletters/every-agent-token-efficiency-2026-10-07.md)
- [AINews — Managed Agents flows, agent-team economics, Devin trees](../sources/newsletters/ainews-cma-flows-agent-teams-2026-10-10.md)
- [Latent Space — How Anthropic's dynamic workflows coordinate Claude agents](../sources/newsletters/latent-space-claude-dynamic-workflows-2026-10-12.md)
