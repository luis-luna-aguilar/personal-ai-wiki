---
type: proposal
source: raw/newsletters/2026-05-20-anthropic-is-onto-something.md
status: pending
created: 2026-08-25
---

# Proposal: Anthropic agent infrastructure — sandboxes, MCP tunnels, Stainless acquisition, and the harness/agent-labs thesis

## Summary

Three related May 2026 signals from the oldest-25 email digest, all verified against primary sources during drafting: (1) Anthropic shipped self-hosted sandboxes (public beta) and MCP tunnels (research preview) for Claude Managed Agents, confirmed via Anthropic's own blog post; (2) Anthropic acquired Stainless, confirmed via Anthropic's own announcement (price undisclosed by Anthropic; ~$300M figure remains secondary-sourced to The Information); (3) a cluster of "harness thesis" evidence — Greg Brockman's "the model alone is no longer the product," MCP's 2026-07-28 stateless release candidate, managed sandboxes becoming first-class primitives across labs, and a single-agent-first orchestration heuristic — confirmed via primary/near-primary tweets from Brockman and MCP maintainer David Soria Parra.

## Intended changes

- [ ] **Update** `wiki/tools/claude-managed-agents.md` — add self-hosted sandboxes (public beta) + MCP tunnels (research preview); bump `as_of` 2026-05-13 → 2026-05-20
    > See draft below

- [ ] **Update** `wiki/concepts/harness.md` — extend the managed-agent-platform-primitives pattern with Anthropic's sandbox/tunnel split; add the "Code as Agent Harness" survey as a reinforcing framing
    > See draft below

- [ ] **Update** `wiki/concepts/mcp.md` — add the MCP 2026-07-28 stateless release candidate and the Stainless acquisition; add a `## Recent changes` section (page currently has none)
    > See draft below

- [ ] **Update** `wiki/concepts/agent-labs-vs-model-labs.md` — add Brockman/AI21/DeepSeek evidence that the Agent Labs thesis is accelerating; add a `## Recent changes` section (page currently has none)
    > See draft below

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add a single-agent-first escalation-threshold pattern
    > See draft below

- [ ] **Spill** `wiki/workflows/agentic-orchestration-patterns.md` → `wiki/history/workflows/agentic-orchestration-patterns.md` — page is already at the 10-entry cap (confirmed by fresh read); adding a new entry pushes it to 11, so the current bottom entry (`[2026-06-24] Token-tightening coverage...`) spills to history
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-acquires-stainless.md` — source summary for Anthropic's official acquisition announcement

- [ ] **Create** `wiki/sources/articles/claude-managed-agents-updates-2026-05.md` — source summary for Anthropic's self-hosted-sandboxes/MCP-tunnels blog post

- [ ] **Create** `wiki/sources/articles/code-as-agent-harness-paper.md` — source summary for the arXiv survey

- [ ] **Create** `wiki/sources/tweets/mcp-2026-07-28-stateless-rc.md` — source summary for the MCP maintainer's RC announcement

- [ ] **Create** `wiki/sources/tweets/brockman-model-not-product.md` — source summary for Greg Brockman's tweet

- [ ] **Create** `wiki/sources/newsletters/anthropic-is-onto-something.md` — source summary for The Code newsletter (2026-05-20)

- [ ] **Create** `wiki/sources/newsletters/google-io-agents-agents-agents.md` — source summary for Every's newsletter (2026-05-20)

- [ ] **Create** `wiki/sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md` — source summary for AINews (2026-05-23)

- [ ] **Create** `wiki/sources/newsletters/ainews-new-ai-infra-unicorns-exa-modal-turbop.md` — source summary for AINews (2026-05-22), scoped only to the single-agent-first orchestration item

## Page drafts

### wiki/tools/claude-managed-agents.md (updated)

```md
---
title: Claude Managed Agents
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, closed-source, agentic]
as_of: 2026-05-20
sources: [managed-agents, every-managed-agents-vibe-check, anthropic-platform-expansion-april-2026, claude-managed-agents-memory, anthropic-spacex-dreams-2026-05-07, claude-managed-agents-feature-parity-2026-05-13, claude-managed-agents-updates-2026-05, anthropic-is-onto-something]
---
```

Append to the end of the `## Current status (as of 2026-05-13)` bullet list (heading text left as-is, consistent with existing drift between the heading date and frontmatter `as_of` already present on this page):

```md
- **Self-hosted sandboxes** (public beta, announced at Code with Claude London, May 2026): tool execution can run on the customer's own infrastructure or through a supported managed provider (Cloudflare, Daytona, Modal, Vercel), while Anthropic's hosted agent loop — orchestration, context management, error recovery — stays on Anthropic's side. Sensitive files, packages, and services never leave the customer's perimeter; the customer controls compute sizing and the runtime image.
- **MCP tunnels** (research preview): let Managed Agents reach MCP servers inside a private network without exposing them to the public internet. A lightweight gateway the customer deploys makes a single outbound connection — no inbound firewall rules, no public endpoints, traffic encrypted end to end. Supported in both Managed Agents and the Messages API; managed from Claude Console workspace settings by org admins.
```

Add to `## Recent changes` (new top entry):

```md
- [2026-05-20] Anthropic shipped self-hosted sandboxes (public beta) and MCP tunnels (research preview): tool execution can run on customer infrastructure or through Cloudflare/Daytona/Modal/Vercel while Anthropic keeps the orchestration loop; MCP tunnels reach private MCP servers without exposing them publicly.
```

Add to `## Sources`:

```md
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
```

### wiki/concepts/harness.md (updated)

Frontmatter `sources:` list — append `claude-managed-agents-updates-2026-05, code-as-agent-harness-paper` (as_of stays 2026-07-08; this new content is older than the page's current newest claim).

Update the existing "Managed-agent platform primitives" bullet under `## What good harness engineering looks like` (append a sentence, rest of bullet unchanged):

```md
- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution. Google adding these to the Gemini API is another sign that "harness" is becoming product infrastructure, not only application code. Anthropic's Claude Managed Agents took this further in May 2026 with self-hosted sandboxes (public beta) and MCP tunnels (research preview): the orchestration loop stays hosted while tool execution and private MCP connectivity move onto customer-controlled infrastructure — splitting the "brain" (hosted) from the "hands" (customer perimeter) as a general product primitive rather than an internal implementation detail.
```

Add a new bullet at the end of the same list:

```md
- **Code as the operational substrate, not just output.** A May 2026 survey ("Code as Agent Harness," arXiv:2605.18747) frames code as the shared medium connecting agent reasoning, acting, and environment modeling — not merely the artifact an agent produces. It organizes harness design around three layers: the interface where code links reasoning/action/environment; harness mechanisms (planning, memory, tool use, feedback-driven control); and scaling from single-agent to multi-agent settings, where shared code artifacts support coordination, review, and verification.
```

Add to `## Recent changes` (2 new top entries):

```md
- [2026-05-20] Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview), extending the harness security boundary so tool execution and private MCP connectivity can run on customer infrastructure while Anthropic keeps the orchestration loop.
- [2026-05-18] "Code as Agent Harness" survey (arXiv:2605.18747) frames code as the operational substrate for agent reasoning, planning, memory, tool use, and multi-agent coordination.
```

Add to `## Sources`:

```md
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [Code as Agent Harness (arXiv:2605.18747)](../sources/articles/code-as-agent-harness-paper.md)
```

### wiki/concepts/mcp.md (updated)

Frontmatter `sources:` list — append `mcp-2026-07-28-stateless-rc, anthropic-acquires-stainless, google-io-agents-agents-agents, ainews-all-model-labs-are-now-agent-labs` (as_of stays 2026-06-29; this new content is older than the page's current newest claim).

Append to the `## Current status (as of 2026-04-23)` bullet list:

```md
- MCP's 2026-07-28 release candidate makes the protocol stateless: no handshake, no session ID, and any request can hit any server instance — a significant operational simplification for MCP server operators (easier horizontal scaling, no sticky-session requirements). The RC also adds first-class extensions (MCP Apps, Tasks), auth hardening, and a formal deprecation policy.
- Anthropic acquired Stainless (May 2026) — an SDK/CLI/MCP-server generation platform used by hundreds of companies, including former customers OpenAI and Google — to extend Claude's ability to connect to data and tools. Stainless CEO Alex Rattray had already argued publicly for MCP server design principles that make tools legible to agents: keep the tool count small, give tools precise names, and aim for tightly defined outputs.
```

Add a new `## Recent changes` section (page currently has none), inserted between `## Why it matters` and `## Sources`:

```md
## Recent changes

- [2026-05-22] MCP 2026-07-28 release candidate makes the protocol stateless (no handshake, no session ID, any request can hit any server instance); adds MCP Apps and Tasks as first-class extensions, auth hardening, and a formal deprecation policy.
- [2026-05-18] Anthropic acquired Stainless, an SDK/MCP-server generation platform used by hundreds of companies including former customers OpenAI and Google, to strengthen Claude's agent-facing developer tooling stack. Price undisclosed by Anthropic; reported by The Information at "north of $300M" via secondary coverage (unverified against a primary figure).
```

Add to `## Sources`:

```md
- [MCP 2026-07-28 release candidate — stateless protocol](../sources/tweets/mcp-2026-07-28-stateless-rc.md)
- [Anthropic acquires Stainless](../sources/articles/anthropic-acquires-stainless.md)
```

### wiki/concepts/agent-labs-vs-model-labs.md (updated)

Frontmatter `sources:` list — append `brockman-model-not-product, ainews-all-model-labs-are-now-agent-labs` (as_of stays 2026-06-11; this new content is older than the page's current newest claim).

Add a new section after `## Relationship to model sovereignty` and before `## Sources`:

```md
## Evidence the shift is accelerating (May 2026)

- OpenAI President Greg Brockman: "the model alone is no longer the product" — a notable reversal from a position he and other "Team Big Model" veterans held previously.
- AI21 shuttered its dedicated model team, pivoting fully to agents.
- DeepSeek — historically the most "pure model" of the frontier open-weight labs — is building its first dedicated "harness team."
- This cuts both ways for the model-neutrality implication above: a lab that tightly co-trains its model with its own harness can also use that coupling to funnel users toward its own agent product rather than a model-agnostic API, a countervailing force against model neutrality.

## Recent changes

- [2026-05-22] Greg Brockman's "the model alone is no longer the product," AI21 shuttering its model team for an agents pivot, and DeepSeek building its first harness team reinforce the Agent Labs framing — even historically model-only labs are absorbing harness work.
```

Add to `## Sources`:

```md
- [Greg Brockman: "the model alone is no longer the product"](../sources/tweets/brockman-model-not-product.md)
- [AINews — All Model Labs are now Agent Labs](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
```

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter `sources:` list — append `ainews-new-ai-infra-unicorns-exa-modal-turbop` (as_of stays 2026-07-14; this new content is older than the page's current newest claim).

Add a new bullet to `## Current patterns`, placed after the existing "Coordinator-specialist routing" bullet:

```md
- **Single-agent-first escalation threshold.** Start with a single-agent system and only introduce manager/sub-agent or decentralized multi-agent topologies once tool sprawl or prompt bloat makes the single-agent design unmanageable — treat multi-agent orchestration as an escalation, not a default starting architecture. *Source: Cameron Wolfe (@cwolferesearch) synthesis via AINews, May 2026*
```

Add new top entry to `## Recent changes` (this pushes the section to 11 entries, triggering the spill below):

```md
- [2026-05-22] Added single-agent-first escalation threshold: start single-agent, only add manager/sub-agent or decentralized multi-agent topologies once tool sprawl or prompt bloat becomes unmanageable (Cameron Wolfe synthesis via AINews).
```

Remove the current bottom entry (spilled to history, see below):

```md
- [2026-06-24] Token-tightening coverage adds AI FinOps controls: budgets, model routing, prompt caching, cheaper defaults, checkpoints, and outcome-based spend review.
```

Add to `## Sources`:

```md
- [AINews — New AI infra unicorns: Exa, Modal, Turbopuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-exa-modal-turbop.md)
```

### wiki/history/workflows/agentic-orchestration-patterns.md (updated)

Append to the existing `## Archived from current page on 2026-08-25` section (same-day spill already recorded this morning — append rather than create a second dated header):

```md
- [2026-06-24] Token-tightening coverage adds AI FinOps controls: budgets, model routing, prompt caching, cheaper defaults, checkpoints, and outcome-based spend review.
```

### wiki/sources/articles/anthropic-acquires-stainless.md (new)

```md
---
title: Anthropic acquires Stainless
type: source
source_type: article
source_file: raw/articles/2026-08-25-anthropiccom-news-anthropic-acquires-stainless.md
url: https://www.anthropic.com/news/anthropic-acquires-stainless
published: 2026-05-18
ingested: 2026-08-25
domains: [agents]
---

# Anthropic acquires Stainless

Anthropic's official announcement confirming it acquired Stainless, an SDK/CLI/MCP-server generation platform founded in 2022 that has powered every official Anthropic SDK since the early API days and counts hundreds of companies (including former customers OpenAI and Google) as users. Anthropic frames the deal as extending Claude's ability to connect to data and tools. The announcement does not disclose a purchase price.

## Influenced pages
- [Model Context Protocol](../../concepts/mcp.md) — added the acquisition and its tie to MCP-server design legibility
- [Agent Labs vs Model Labs](../../concepts/agent-labs-vs-model-labs.md) — supporting evidence of Anthropic building out agent-facing developer tooling

## Key claims extracted
- Acquisition announced 2026-05-18
- Stainless founded 2022; generates SDKs (TypeScript, Python, Go, Java, etc.), CLIs, and MCP servers from an API spec
- Former Stainless customers include OpenAI and Google
- Anthropic states the goal is to "advance Claude's ability to connect to data and tools"
- No purchase price disclosed by Anthropic; The Information reported a price "north of $300 million" (secondary source, via Every's newsletter coverage — unverified against a primary figure)
```

### wiki/sources/articles/claude-managed-agents-updates-2026-05.md (new)

```md
---
title: "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels"
type: source
source_type: article
source_file: raw/articles/2026-08-25-claudecom-blog-claude-managed-agents-updates.md
url: https://claude.com/blog/claude-managed-agents-updates
published: 2026-05-20
ingested: 2026-08-25
domains: [agents]
---

# New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Anthropic's official Claude Managed Agents blog post announcing two features unveiled at Code with Claude London: self-hosted sandboxes (public beta) and MCP tunnels (research preview). Self-hosted sandboxes let a Managed Agent execute tools on the customer's own infrastructure or a supported managed provider (Cloudflare, Daytona, Modal, Vercel) while Anthropic's hosted agent loop still handles orchestration, context management, and error recovery. MCP tunnels let agents reach MCP servers inside a private network — via a lightweight customer-deployed gateway — without exposing them to the public internet.

## Influenced pages
- [Claude Managed Agents](../../tools/claude-managed-agents.md) — added self-hosted sandboxes and MCP tunnels to current status
- [Harness (agent)](../../concepts/harness.md) — extended the managed-agent-platform-primitives pattern with this example

## Key claims extracted
- Self-hosted sandboxes: public beta; MCP tunnels: research preview (request access via a Claude form)
- Supported sandbox providers: Cloudflare, Daytona, Modal, Vercel — each with a named early-access customer example (Amplitude, Clay, Rogo, and others)
- Sandbox provisioning, resource sizing, and runtime image are controlled by the customer
- MCP tunnels supported in both Managed Agents and the Messages API; managed from Claude Console workspace settings by org admins
- No inbound firewall rules or public endpoints required for MCP tunnels; traffic is encrypted end to end
```

### wiki/sources/articles/code-as-agent-harness-paper.md (new)

```md
---
title: "Code as Agent Harness"
type: source
source_type: article
source_file: raw/articles/2026-08-25-arxivorg-abs-260518747.md
url: https://arxiv.org/abs/2605.18747
published: 2026-05-18
ingested: 2026-08-25
domains: [agents]
---

# Code as Agent Harness

An arXiv survey (submitted 2026-05-18, cs.CL/cs.AI) arguing that code is becoming the operational substrate for agent systems rather than only a final output. The paper organizes harness design around three layers: the harness interface (where code connects agents to reasoning, action, and environment modeling), harness mechanisms (planning, memory, tool use for long-horizon execution, plus feedback-driven control), and scaling the harness from single-agent to multi-agent settings, where shared code artifacts support coordination, review, and verification. It surveys applications across coding assistants, GUI/OS automation, embodied agents, scientific discovery, and enterprise workflows, and names open challenges including evaluation beyond final task success and regression-free harness improvement.

## Influenced pages
- [Harness (agent)](../../concepts/harness.md) — added as a research framing reinforcing code-centered harness design

## Key claims extracted
- Frames "code as agent harness": code as the operational substrate for reasoning, acting, environment modeling, and execution-based verification, not just a target output
- Three-layer structure: harness interface, harness mechanisms (planning/memory/tool use/feedback control), and multi-agent scaling
- Open challenges named: evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across agents, human oversight for safety-critical actions
- This is a synthesis/survey paper, not a benchmark result — its framing is a useful vocabulary, not an empirical claim about any specific system
```

### wiki/sources/tweets/mcp-2026-07-28-stateless-rc.md (new)

```md
---
title: "MCP 2026-07-28 release candidate: stateless protocol"
type: source
source_type: tweet
source_file: raw/tweets/2026-08-25-redirect-e9187825-ab02-42eb-ac5f-ad4d73f120dc.md
url: https://x.com/dsp_
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# MCP 2026-07-28 release candidate: stateless protocol

David Soria Parra (an MCP protocol maintainer) announced the release candidate for the MCP 2026-07-28 protocol revision. The headline change: MCP becomes stateless — no handshake, no session ID, and any request can hit any server instance, removing sticky-session requirements and simplifying horizontal scaling for MCP server operators. The RC also adds first-class extensions (MCP Apps, Tasks), auth hardening, and a formal deprecation policy.

## Influenced pages
- [Model Context Protocol](../../concepts/mcp.md) — added the stateless RC as a protocol-evolution update

## Key claims extracted
- MCP 2026-07-28 RC removes handshake and session-ID requirements; any request can hit any server instance
- Adds MCP Apps and Tasks as first-class protocol extensions
- Adds auth hardening and a formal deprecation policy
- The "2026-07-28" string names the protocol revision, not necessarily its public announcement date; the announcement itself was captured via an AINews recap dated 2026-05-23, and the direct tweet fetch returned a reply rather than the original post body — the claim is grounded in an MCP maintainer's account, not an official MCP spec-repo changelog
```

### wiki/sources/tweets/brockman-model-not-product.md (new)

```md
---
title: 'Greg Brockman: "the model alone is no longer the product"'
type: source
source_type: tweet
source_file: raw/tweets/2026-08-25-redirect-319f79bc-9ba8-4279-9445-16881405c3d0.md
url: https://x.com/gdb
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# Greg Brockman: "the model alone is no longer the product"

OpenAI President Greg Brockman stated publicly that "the model alone is no longer the product" — cited by AINews as a notable reversal from a position he and other "Team Big Model" veterans held previously, and as part of a broader pattern of Model Labs absorbing agent/harness work.

## Influenced pages
- [Agent Labs vs Model Labs](../../concepts/agent-labs-vs-model-labs.md) — added as reinforcing evidence for the thesis

## Key claims extracted
- Brockman: "the model alone is no longer the product"
- Framed by AINews as a reversal from his and peers' earlier position
- Contextualized alongside AI21 shuttering its model team (pivoting to agents) and DeepSeek building its first "harness team"
```

### wiki/sources/newsletters/anthropic-is-onto-something.md (new)

```md
---
title: "Anthropic is onto something"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-anthropic-is-onto-something.md
url: https://codenewsletter.ai/p/google-drops-gemini-3-5-flash-github-breached-via-a-malicious-extension
published: 2026-05-20
ingested: 2026-08-25
domains: [agents, cybersecurity]
---

# Anthropic is onto something

The Code newsletter (2026-05-20) covering Google I/O's Gemini 3.5 Flash / Antigravity 2.0 launch, Anthropic's self-hosted sandboxes and MCP tunnels for Claude Managed Agents, and GitHub's confirmation that a compromised employee device and poisoned VS Code extension led to the theft of internal repositories.

## Influenced pages
- [Claude Managed Agents](../../tools/claude-managed-agents.md) — self-hosted sandboxes / MCP tunnels
- [Harness (agent)](../../concepts/harness.md) — managed-agent platform primitives example
- [State of Cybersecurity](../../state-of/cybersecurity.md) — GitHub breach entry (handled in the companion cybersecurity proposal)

## Key claims extracted
- Anthropic rolled out self-hosted sandboxes (public beta) and MCP tunnels (research preview) for Claude Managed Agents at Code with Claude London
- GitHub confirmed internal repos were stolen via a compromised employee device and a malicious/poisoned VS Code extension; attacker claimed ~3,800 repos
- Gemini 3.5 Flash and Antigravity 2.0 are covered but not re-ingested here — already tracked via other, more detailed sources per the triage note
```

### wiki/sources/newsletters/google-io-agents-agents-agents.md (new)

```md
---
title: "Google I/O: Agents, Agents, Agents"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-google-io-agents-agents-agents.md
url: https://every.to/context-window/google-i-o-agents-agents-agents
published: 2026-05-20
ingested: 2026-08-25
domains: [agents]
---

# Google I/O: Agents, Agents, Agents

Every's Context Window newsletter (2026-05-20) on Google I/O's agent-first announcements, Anthropic's reported ~$300M acquisition of Stainless, and a mini-Vibe Check of Figma's new in-canvas design agent.

## Influenced pages
- [Model Context Protocol](../../concepts/mcp.md) — Stainless acquisition and its MCP-server design-legibility angle
- [Agent Labs vs Model Labs](../../concepts/agent-labs-vs-model-labs.md) — supporting context (Anthropic building out agent-facing tooling)

## Key claims extracted
- Anthropic acquired Stainless; Every reports the price as "north of $300 million" per The Information, with terms not disclosed by Anthropic (cross-checked against Anthropic's own announcement, which does not disclose price)
- Stainless CEO Alex Rattray had previously outlined MCP server design principles for agent legibility: small tool counts, precise tool names, tightly-defined outputs
- Former Stainless customers include OpenAI and Google
- Figma's in-canvas design agent and the broader Google I/O agent announcements are not re-ingested here — out of scope for this proposal
```

### wiki/sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md (new)

```md
---
title: "[AINews] All Model Labs are now Agent Labs"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
url: https://www.latent.space/p/ainews-all-model-labs-are-now-agent
published: 2026-05-23
ingested: 2026-08-25
domains: [agents, cybersecurity]
---

# [AINews] All Model Labs are now Agent Labs

AINews/Latent Space digest (2026-05-23) covering the "model alone is no longer the product" thesis (Greg Brockman, AI21's pivot, DeepSeek's new harness team), the MCP 2026-07-28 stateless release candidate, managed-sandbox primitives becoming first-class (Gemini Managed Agents + Interactions API, CoreWeave Sandboxes, Cloudsail), DeepSeek V4-Pro's permanent price cut, and Anthropic's Project Glasswing reporting 10,000+ high/critical-severity vulnerabilities found within a month.

## Influenced pages
- [Agent Labs vs Model Labs](../../concepts/agent-labs-vs-model-labs.md) — added Brockman/AI21/DeepSeek evidence
- [Model Context Protocol](../../concepts/mcp.md) — MCP stateless RC
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — Glasswing 10,000+ vulnerabilities figure (handled in the companion cybersecurity proposal)
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Glasswing figure (handled in the companion cybersecurity proposal)

## Key claims extracted
- Greg Brockman: "the model alone is no longer the product"; AI21 shuttered its model team to pivot to agents; DeepSeek building its first "harness team"
- MCP 2026-07-28 RC is stateless (no handshake/session ID); adds MCP Apps/Tasks, auth hardening, deprecation policy
- Managed sandboxes as first-class primitives: Gemini Managed Agents + Interactions API, CoreWeave Sandboxes (public preview), Cloudsail (per-task Cloudflare sandboxes)
- Anthropic: Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch
- DeepSeek V4-Pro discount made permanent; Chinese open-weight models closing the gap — not re-ingested here, out of scope for this proposal
```

### wiki/sources/newsletters/ainews-new-ai-infra-unicorns-exa-modal-turbop.md (new)

```md
---
title: "[AINews] New AI infra unicorns: Exa, Modal, Turbopuffer"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa-modal-turbop.md
url: https://www.latent.space/
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# [AINews] New AI infra unicorns: Exa, Modal, Turbopuffer

AINews/Latent Space digest (2026-05-22). Only the agent-orchestration guidance item is ingested here; the newsletter's broader coverage (Exa/Modal/Turbopuffer funding, Daytona compute-infra interview highlights, the OpenAI Erdős math result follow-on, Cartesia/Runway multimodal updates) is out of scope for this proposal and not re-ingested.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — added single-agent-first escalation threshold

## Key claims extracted
- Cameron Wolfe (@cwolferesearch) synthesis: start with single-agent systems; only move to manager/sub-agent or decentralized multi-agent topologies once tool sprawl or prompt bloat becomes unmanageable
- Cognition's "sub-Devin" workflow reportedly compresses 2+ engineer-weeks of work into a couple of hours (practitioner anecdote via a Twitter reply, not independently verified)
```

## Schema / vocabulary additions

None required — all frontmatter uses existing controlled `domains` (`agents`, `cybersecurity`), and no new `subcategory` or `tags` values are introduced.

## Open questions

- **Stainless acquisition price is unverified.** Anthropic's own announcement (`https://www.anthropic.com/news/anthropic-acquires-stainless`, fetched directly) does not disclose a purchase price. The "~$300M" figure traces only to The Information via Every's newsletter recap. I've flagged this in both `concepts/mcp.md`'s new Recent-changes entry and the Stainless source-summary page. Treat the price as unconfirmed until a primary figure surfaces.
- **No dedicated `tools/stainless.md` page was created.** Stainless is now absorbed into Anthropic rather than an independently tracked product, so I folded its content into `concepts/mcp.md`. Flag if you'd prefer a standalone tool page instead (e.g. to track it as a discrete acquisition/integration story over time).
- **MCP 2026-07-28 RC sourcing is thin.** The only source is an MCP maintainer's tweet via an AINews recap (the direct tweet fetch returned a reply, not the original post body — the title metadata captured the original text). If you want this claim on firmer footing, worth checking the official MCP spec repo's changelog directly.
- **Cross-proposal dependency.** This proposal creates `wiki/sources/newsletters/anthropic-is-onto-something.md` and `wiki/sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md`, both of which the companion cybersecurity proposal (`2026-08-25-ai-cybersecurity-glasswing-github-breach.md`) also links to without recreating. Apply this proposal first (or apply both together) so those links resolve immediately rather than briefly pointing at not-yet-created pages.
