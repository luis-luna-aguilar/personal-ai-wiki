---
title: Claude Managed Agents
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, closed-source, agentic]
as_of: 2026-04-15
sources: [managed-agents, every-managed-agents-vibe-check]
---

# Claude Managed Agents

Claude Managed Agents is not yet documented here as a mature end-user product. At this point, the source reads more like an Anthropic architecture and platform direction: a hosted Claude Platform runtime for long-running agents built around three separate pieces, instead of one all-in-one agent container.

Those three pieces are:

- a durable **session** log that stores what happened
- a **harness**, meaning the loop that runs Claude and decides when to call tools
- one or more **sandboxes/tools** that do the actual work

Anthropic's core idea is that these pieces should be decoupled so the system can keep evolving as models improve, without forcing users to rebuild around each model generation's quirks.

## Current status (as of 2026-04-15)

- Public beta service on the Claude Platform for long-running agents
- Handles agent infrastructure primitives including sessions, memory, tool use, and credentials
- Core abstractions in the post: `session`, `harness`, `sandbox`
- Harness is decoupled from the execution container and calls tools through a generic interface like `execute(name, input) -> string`
- Session lives outside the harness as an append-only event log and can be resumed with operations like `wake(sessionId)`, `getSession(id)`, `emitEvent(id, event)`, and `getEvents()`
- Sandboxes are provisioned on demand instead of being assumed to exist for every session from the start
- Designed to connect Claude to customer infrastructure, including resources in a customer's own VPC
- Supports MCP-backed tools with OAuth credentials stored outside the sandbox in a secure vault
- Every reports that Spiral used the service to spin up a new agent in a few hours; the cited benefit was less custom infrastructure maintenance, not just faster initial coding
- Existing agents can be updated through the dashboard by changing the system prompt or underlying model and saving

## Why it matters

Many agent systems still bundle the model loop, execution environment, secrets, and state into one long-lived process or container. Anthropic's claim is that this becomes brittle over time: fixes made for one model generation can turn into dead weight for the next.

Managed Agents moves the durable state outside the live context window and keeps credentials outside the sandbox where generated code runs. That makes it easier to recover from failures, reconnect a session to a fresh harness, attach multiple execution environments, and change the implementation underneath without changing the top-level shape of the system.

Every's practitioner read adds a product-adoption angle: if the hosted primitive works well enough, teams that have been building custom agent infrastructure may redirect effort away from sessions, memory, tool calling, credentials, and prompt/model deployment machinery toward the domain-specific behavior of the agent itself.

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

## Weaknesses / caveats

- The source is an engineering architecture post, not full product documentation
- No pricing, availability tiering, or detailed public API surface is captured here
- Reported latency improvements are vendor-internal numbers
- Every's Spiral example is a practitioner anecdote, not a broad evaluation
- The post and mini-vibe-check explain the platform shape better than current limits, production constraints, or failure cases

## Related

- [[workflows/advisor-strategy]]
- [[state-of/agents]]

## Recent changes

- [2026-04-15] Every reported Claude Managed Agents is in public beta and highlighted Spiral's use of it to create an agent in a few hours while offloading sessions, memory, tool use, and credential handling
- [2026-04-09] Page created from Anthropic's "Scaling Managed Agents: Decoupling the brain from the hands" engineering post

## Sources

- [[sources/articles/managed-agents]]
- [[sources/articles/every-managed-agents-vibe-check]]
