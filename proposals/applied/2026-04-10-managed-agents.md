---
type: proposal
source: raw/articles/2026-04-10-anthropiccom-engineering-managed-agents.md
status: applied
created: 2026-04-10
---

# Proposal: Anthropic Managed Agents

## Summary

Anthropic introduces **Managed Agents**, a hosted Claude Platform service for running long-horizon agents via stable interfaces around three decoupled components: a durable **session** log, a stateless **harness** ("brain"), and one or more **sandboxes/tools** ("hands"). The architecture pitch is that agent infrastructure should virtualize these pieces the way operating systems virtualized hardware, so implementation details can change as models improve without forcing users to rebuild around each generation's quirks.

The key operational claims are reliability, security, and scale. By moving the harness out of the container and treating sandboxes as interchangeable "cattle," Anthropic says failed sandboxes can be reprovisioned, failed harnesses can resume from the session log, secrets can be kept out of the sandbox entirely, and time-to-first-token improved materially after decoupling the brain from the hands (roughly **60% lower p50** and **over 90% lower p95**, per the post). This looks substantive enough for a new tool page, plus a new agents-domain subcategory rather than folding it into the existing advisor-strategy workflow.

## Intended changes

- [x] **Create** `wiki/tools/claude-managed-agents.md` — new tool page for Anthropic's hosted managed-agent runtime on the Claude Platform
  > See full draft below.

- [x] **Update** `wiki/state-of/agents.md` — add a new `managed-agent-runtime` subcategory with [[tools/claude-managed-agents]], add `managed-agents` to frontmatter `sources`, and add a Recent changes entry
  > See diff snippet below.

- [x] **Create** `wiki/sources/articles/managed-agents.md` — source summary page
  > See full draft below.

- [x] **Update** `wiki/index.md` — add the new tool entry and refresh page counts
  > See diff snippet below.

## Schema / vocabulary additions

- [x] Add subcategory `managed-agent-runtime` to `wiki/_schema/subcategories.md`
  - Parent domain(s): `agents`
  - Applies to types: `tool`
  - Definition: Hosted platforms that run long-horizon agents on the user's behalf via durable sessions plus attachable execution environments and tools, rather than embedding the full agent loop inside a single local process or container.

## Page drafts

### wiki/tools/claude-managed-agents.md (new)

```markdown
---
title: Claude Managed Agents
type: tool
domains: [agents]
subcategory: managed-agent-runtime
tags: [anthropic, closed-source, agentic]
as_of: 2026-04-10
sources: [managed-agents]
---

# Claude Managed Agents

Claude Managed Agents is Anthropic's hosted runtime for long-horizon agents on the Claude Platform. Instead of treating an agent as one long-lived container, the system separates three pieces behind stable interfaces: a durable **session** log, a stateless **harness** that runs the Claude loop, and one or more **sandboxes/tools** that perform actions.

The product thesis is architectural rather than UX-heavy: agent infrastructure should be resilient to model change. Anthropic frames Managed Agents as a "meta-harness" that stays stable even as context engineering, harness logic, and execution environments change underneath it.

## Current status (as of 2026-04-10)

- Hosted service on the Claude Platform for long-running agents
- Core abstractions exposed in the post: `session`, `harness`, `sandbox`
- Harness is decoupled from the execution container and calls tools through a generic interface like `execute(name, input) -> string`
- Session is stored outside the harness as an append-only event log and can be resumed with operations like `wake(sessionId)`, `getSession(id)`, `emitEvent(id, event)`, and `getEvents()`
- Sandboxes are provisioned on demand rather than assumed to exist for every session from the start
- Designed to connect Claude to customer infrastructure, including resources in a customer's own VPC
- Supports MCP-backed tools with OAuth credentials stored outside the sandbox in a secure vault

## Why it matters

Most agent frameworks still treat the full loop as one coupled unit: model context, harness logic, execution environment, credentials, and session state all live together. Anthropic's claim is that this becomes fragile as models improve, because harness workarounds that were necessary for one model generation quickly turn into dead weight for the next.

Managed Agents pushes the durable parts outside the model context window and outside the sandbox. That makes it easier to recover from failures, reconnect a session to new harness instances, attach many execution environments, and keep credentials structurally unreachable from generated code.

## Architecture

### Brain, hands, session

- **Brain:** Claude plus the harness that runs the loop
- **Hands:** sandboxes and external tools that execute actions
- **Session:** durable event log of what happened

Each can fail or be replaced independently. A dead sandbox becomes a tool-call error that Claude can retry after reprovisioning. A dead harness can be restarted and resumed from the session log.

### Session outside the context window

Anthropic explicitly treats the session as recoverable context that lives outside Claude's context window. The harness can fetch slices of past events and transform them before reintroducing them into the live prompt, instead of relying only on irreversible compaction or trimming decisions.

### Security boundary

The post argues for a structural security boundary: secrets should never be reachable from the sandbox where Claude-generated code runs.

- Git credentials can be wired into the local remote during sandbox setup without exposing the token to the agent
- MCP calls go through a proxy that looks up session-bound credentials from a secure vault
- The harness itself does not need direct access to user credentials

## Reported operational gains

Vendor-reported architecture metrics from the post:

- After decoupling the brain from the hands, **p50 time-to-first-token** dropped by roughly **60%**
- **p95 time-to-first-token** dropped by **over 90%**

The mechanism is straightforward: sessions that do not immediately need a sandbox can begin inference before any container is provisioned.

## Strengths

- Clean separation between durable state, orchestration logic, and execution environments
- Better failure recovery story than single-container agent designs
- Security model is structural, not only prompt- or policy-based
- Fits enterprise deployment constraints better by connecting to customer-owned infrastructure
- Makes "many brains, many hands" a first-class architecture instead of an afterthought

## Weaknesses / caveats

- The source is an engineering architecture post, not full product documentation
- No pricing, availability tiering, or concrete API surface beyond example interfaces is captured in the source
- Reported latency improvements are vendor-internal numbers
- The post explains the platform shape well, but says less about current user-facing ergonomics, limits, or adoption

## Related

- [[workflows/advisor-strategy]]
- [[state-of/agents]]

## Recent changes

- [2026-04-10] Page created from Anthropic's "Scaling Managed Agents: Decoupling the brain from the hands" engineering post

## Sources

- [[sources/articles/managed-agents]]
```

### wiki/sources/articles/managed-agents.md (new)

```markdown
---
title: Scaling Managed Agents: Decoupling the brain from the hands
type: source
source_type: article
source_file: raw/articles/2026-04-10-anthropiccom-engineering-managed-agents.md
url: https://www.anthropic.com/engineering/managed-agents
ingested: 2026-04-10
domains: [agents]
---

# Scaling Managed Agents: Decoupling the brain from the hands

Anthropic presents Managed Agents, a hosted Claude Platform service for long-horizon agents built around decoupling the harness ("brain"), execution environments ("hands"), and durable session log. The post is primarily an architecture explanation: replace single-container agent designs with stable interfaces so failures can be recovered independently, secrets stay out of sandboxes, and the platform can adapt as model capabilities change.

## Influenced pages

- [[tools/claude-managed-agents]] — new tool page, main subject of the ingest
- [[state-of/agents]] — adds a new `managed-agent-runtime` subcategory and places Claude Managed Agents under it

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
- Reported latency effect: roughly **60% lower p50 TTFT** and **over 90% lower p95 TTFT**
- The architecture supports connecting Claude to customer-owned infrastructure, including VPC resources
- The platform is meant to support "many brains, many hands" rather than a single agent bound to one container

## Caveats

- This is an Anthropic engineering post, not a neutral benchmark or third-party evaluation
- The post gives interface shapes and architectural claims, but not full public API docs, pricing, or product limits
- The TTFT improvements are reported without a public methodology section in the captured source
```

### wiki/state-of/agents.md (updated snippet)

```markdown
---
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents]
---

### Managed agent runtimes

Hosted platforms that run long-horizon agents on the user's behalf using durable sessions plus attachable execution environments, instead of binding the full loop to one local process or container.

- [[tools/claude-managed-agents]] — Anthropic's hosted runtime decouples session, harness, and sandbox; supports MCP tools and customer infrastructure; reports roughly 60% lower p50 TTFT and over 90% lower p95 after decoupling brain from hands *(as of 2026-04-10)*

## Recent changes

- [2026-04-10] Added `managed-agent-runtime` subcategory with [[tools/claude-managed-agents]] after ingesting Anthropic's Managed Agents architecture post.
```

### wiki/index.md (updated snippet)

```markdown
## Tools

- [[tools/claude-managed-agents]] — Anthropic's hosted long-horizon agent runtime built around decoupled session, harness, and sandbox abstractions *(as_of: 2026-04-10)*

## Page count

- tools: 7
...
**Total content pages: 16.**
```

## Open questions

- Should the tool page title/path be **Claude Managed Agents** (product-specific) or just **Managed Agents** (shorter, but more collision-prone if the wiki later tracks other vendors' managed-agent offerings)?
	- let's keep it as is 
- The article has a strong architectural concept inside it: "session as recoverable context object outside the model context window." Keep that embedded in the tool page for now, or split it later into its own `concepts/` page if more sources converge on the same pattern?
	-  let's keep it in the tool too. We'll see how this evolves 

## Comments

- I don't like the category name that you chose for managed runtimes. I think this is also part of agents orchestration; otherwise we are splitting the categories too thin

- What is P50 and P95? What is that nomenclature about?

- Also the concept of "hardness" here is not very clear. What are you referring to? Can you please explain it in simple words? Are you referring to the model being used for that session or the full tool at that point in time? I don't know, like Claude code at that point in time.

- It needs to be clear at the beginning of the tool documentation that this is not a product yet and it's more like a concept 
