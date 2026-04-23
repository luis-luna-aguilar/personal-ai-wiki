---
type: proposal
sources:
  - raw/articles/Building agents that reach production systems with MCP _ Claude.pdf
  - raw/articles/2026-04-23-tco-d47tgmzhnl.md
  - raw/tweets/2026-04-23-awsai-2046670809289081344.md
  - raw/newsletters/2026-04-23-openai-drops-a-privacy-focused-model.md
status: pending
created: 2026-04-23
---

# Proposal: Anthropic — MCP Guidance Blog + Claude Cowork on AWS Bedrock

## Summary
Two Anthropic agent-platform signals on the same day: (1) a full Anthropic blog post on when production agents should use direct APIs vs CLIs vs MCP, with concrete design patterns for remote MCP servers, context-efficient clients, auth, and skills pairing; (2) Claude Cowork in public research preview via Amazon Bedrock, keeping data within the customer's AWS account.

## Intended changes

- [ ] **Update** `wiki/concepts/mcp.md` — add guidance section on APIs vs CLIs vs MCP decision; update as_of
- [ ] **Update** `wiki/tools/claude-cowork.md` — add AWS Bedrock deployment section; update as_of; prepend Recent changes entry
- [ ] **Create** `wiki/sources/articles/anthropic-mcp-production-systems.md` — source summary for Anthropic's MCP blog post
- [ ] **Create** `wiki/sources/tweets/awsai-cowork-bedrock-2026-04-23.md` — source summary for AWS Bedrock availability tweet

*Note: The full Anthropic article is now available locally as `raw/articles/Building agents that reach production systems with MCP _ Claude.pdf`, so the MCP update below reflects the actual article rather than the earlier tweet stub.*

## Page drafts

### wiki/concepts/mcp.md (update — diff only)

> **Replace current `## Current status` block with:**
> ```markdown
> ## Current status (as of 2026-04-23)
>
> - Originated by Anthropic as an open standard for connecting assistants to external systems
> - Increasingly treated as shared infrastructure rather than a vendor-specific feature
> - Useful for both local and hosted agent systems because it standardizes tool discovery and invocation
>
> **When to use APIs vs CLIs vs MCP (Anthropic guidance, April 2026):**
> - Direct APIs: fine for one agent talking to one service, or a small number of integrations that do not need reuse across platforms
> - CLIs: best for quick, permissive integrations in local environments with a shell and filesystem
> - MCP: best when the integration needs a common protocol layer across web, mobile, desktop, and cloud-hosted agents, with standardized auth, discovery, and richer semantics
> - Anthropic's framing is that production agents increasingly run in the cloud, so MCP becomes the compounding integration layer even if mature stacks still ship all three: API, CLI, and MCP
>
> **Effective MCP server patterns (Anthropic, April 2026):**
> - Build remote servers for maximum reach across cloud, web, and mobile clients
> - Group tools around user intent rather than mirroring raw API endpoints one-to-one
> - For very large surfaces, expose a thin code-orchestration layer instead of hundreds of separate tools
> - Add richer protocol semantics where useful: MCP Apps for inline UI, elicitation for missing parameters or destructive confirmation, and standardized OAuth flows
>
> **Context-efficient MCP client patterns:**
> - Tool search: load tool definitions on demand instead of injecting the full catalog into context
> - Programmatic tool calling: process and aggregate tool results in code so only the final output reaches the model context
>
> **Skills + MCP:**
> - Skills and MCP are complementary: MCP exposes capabilities, skills encode procedural knowledge
> - Anthropic highlights two pairing patterns: bundle skills and MCP servers together as a plugin, or distribute skills alongside an MCP server so expertise travels with the integration
> ```

> **Add to `sources` frontmatter:** `anthropic-mcp-production-systems`

> **Update `as_of`:** `as_of: 2026-04-23`

### wiki/tools/claude-cowork.md (update — diff only)

> **Add new section before `## Why it matters`:**
> ```markdown
> ## AWS Bedrock deployment (as of 2026-04-23)
>
> Claude Cowork is now available via Amazon Bedrock in public research preview. Organizations can run Cowork through their own AWS environment, with prompts, files, and model responses kept within the customer's AWS account. Addresses the data-residency and private-cloud requirements of enterprise and regulated-industry customers.
> ```

> **Add to `## Recent changes` (prepend):**
> `- [2026-04-23] AWS Bedrock public research preview: Cowork now available via Bedrock, keeping all data within the customer's AWS account`

> **Update `as_of`:** `as_of: 2026-04-23`

> **Add to `sources` frontmatter:** `awsai-cowork-bedrock-2026-04-23`

### wiki/sources/articles/anthropic-mcp-production-systems.md (new)

````md
---
title: Building agents that reach production systems with MCP
type: source
source_type: article
source_file: raw/articles/Building agents that reach production systems with MCP _ Claude.pdf
url: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
published: 2026-04-22
ingested: 2026-04-23
domains: [agents]
---

# Building agents that reach production systems with MCP

Anthropic's April 22, 2026 MCP guidance post. It is the clearest current articulation of where direct APIs, CLIs, and MCP each fit in production agent systems, and adds concrete implementation guidance for remote MCP servers, auth, context-efficient clients, and the way skills should complement protocol-level tool access.

## Influenced pages

- [[concepts/mcp]] — production guidance for APIs vs CLIs vs MCP; server/client design patterns; skills pairing

## Key claims extracted

- Direct APIs work well for narrow one-agent / one-service integrations, but do not scale cleanly because each agent-service pair becomes bespoke
- CLIs are strong in local shell-native environments but do not generalize well to web, mobile, or cloud-hosted agents
- MCP is the shared protocol layer for remote, authenticated, reusable integrations across clients and deployment environments
- Anthropic argues that production agents increasingly run in the cloud, which makes remote MCP servers the highest-leverage integration layer
- Recommended server patterns: build remote servers, group tools around intent, and use code orchestration for very large API surfaces
- Recommended client patterns: tool search for on-demand tool loading and programmatic tool calling to keep large tool results out of model context
- Skills complement MCP by encoding procedural knowledge on top of raw capabilities; Anthropic expects tighter server-skill pairing to become a standard pattern
````

### wiki/sources/tweets/awsai-cowork-bedrock-2026-04-23.md (new)

````md
---
title: AWS AI — Claude Cowork now available via Amazon Bedrock
type: source
source_type: tweet
source_file: raw/tweets/2026-04-23-awsai-2046670809289081344.md
url: https://x.com/awsai/status/2046670809289081344
published: 2026-04-23
ingested: 2026-04-23
domains: [agents]
---

# AWS AI — Claude Cowork now available via Amazon Bedrock

AWS AI announcement: Claude Cowork is in public research preview on Amazon Bedrock. Organizations can run Cowork through their AWS environment, keeping prompts, files, and model responses within their own AWS account.

## Influenced pages

- [[tools/claude-cowork]] — Bedrock deployment option, data residency

## Key claims extracted

- Claude Cowork available via Amazon Bedrock in public research preview
- All prompts, files, and model responses stay within the customer's AWS account
````

## Comments

- I manually downloaded the blocked article so you can re-do this proposal. You can find it here: raw/articles/Building agents that reach production systems with MCP _ Claude.pdf
