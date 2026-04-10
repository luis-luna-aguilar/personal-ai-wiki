---
type: proposal
source: raw/articles/2026-04-09-projectsdev.md
status: applied
created: 2026-04-09
---

# Proposal: Stripe CLI `projects` developer preview

## Summary

`projects.dev` introduces the **Stripe CLI `projects`** developer preview, a CLI workflow for provisioning and managing third-party services like hosting, databases, auth, AI, and analytics. Stripe positions it as a unified control plane for humans or agents: provision services in accounts you own, sync credentials back into the environment, and manage upgrades, billing, and usage from the CLI.

This fits the wiki as a new tool page plus a new cross-domain subcategory. It is relevant to both `coding` and `agents`, because the explicit pitch is that developers or AI agents can create and manage app infrastructure through the same auditable CLI workflow.

## Intended changes

- [x] **Create** `wiki/tools/stripe-cli.md` — new tool page for the Stripe CLI `projects` workflow
  > Applied using the final naming approved in the proposal comments.

- [x] **Update** `wiki/state-of/coding.md` — add a new subcategory for agentic DevOps and place Stripe CLI under it
  > Applied.

- [x] **Update** `wiki/state-of/agents.md` — add the same subcategory from an agent-execution angle
  > Applied.

- [x] **Create** `wiki/sources/articles/stripe-cli.md` — source summary page
  > Applied using the final naming approved in the proposal comments.

- [x] **Update** `wiki/index.md` — add the new tool entry and refresh counts
  > Applied.

## Schema / vocabulary additions

- [x] Add subcategory `agentic-devops` to `wiki/_schema/subcategories.md`
  - Parent domain(s): `coding`, `agents`
  - Applies to types: `tool`
  - Definition: CLI-native tools that provision and manage third-party app infrastructure and credentials across multiple providers, in workflows designed to be executable by humans or agents.

## Page drafts

### wiki/tools/stripe-cli.md (applied)

```markdown
---
title: Stripe CLI
type: tool
domains: [coding, agents]
subcategory: agentic-devops
tags: [cli, beta, agentic, closed-source]
as_of: 2026-04-09
sources: [stripe-cli]
---

# Stripe CLI

Stripe CLI is Stripe's command-line tool, now extended with a developer-preview `projects` command group for provisioning and managing app-stack services across multiple providers. The product pitch is unusually agent-native: the same commands are meant to be usable by a human developer or by an AI agent provisioning hosting, databases, auth, AI, analytics, and similar services on the developer's behalf.

## Current status (as of 2026-04-09)

- The new `stripe projects` workflow is in **developer preview** / early access
- Distributed through the existing Stripe CLI under the `stripe projects` command group
- Designed to provision services in accounts the user already owns, rather than inside a Stripe-owned runtime
- Credentials generated during provisioning sync back into the local environment
- Stripe also positions it as a billing and subscription control plane: set up billing once, then upgrade, downgrade, monitor usage, and manage subscriptions from the CLI
- Official examples shown on the landing page:
  - `stripe projects init helloworld-app`
  - `stripe projects catalog`
  - `stripe projects add <provider>/<service>`
  - `stripe projects upgrade <provider>`

## What it is trying to solve

Provisioning an app stack still means signing up for multiple SaaS products, clicking through dashboards, managing API keys, and repeating the same setup steps across machines and teammates. Stripe's `projects` workflow presents a normalized CLI layer over that work so infrastructure provisioning becomes scriptable, auditable, and portable.

The key claim is not only convenience for developers, but **delegatability**: an agent can provision services through the same workflow, with credentials returned safely to the environment and changes remaining repeatable.

## Strengths

- Clear agent-compatible framing: "you or your agents" is the main product pitch, not an afterthought
- Unifies provider provisioning, credentials, and plan upgrades behind one CLI workflow
- Emphasizes portability across machines, teammates, and agents rather than a single hosted workspace
- Billing abstraction could remove one of the messiest non-coding parts of stack setup

## Weaknesses / caveats

- Still in developer preview; no evidence yet of broad provider coverage or production adoption
- The landing page is positioning-heavy and light on concrete implementation detail
- The exact supported provider catalog is not captured in the raw source beyond an example (`railway/hosting`) and a "more soon" teaser
- Adds Stripe as a control plane layer between the developer and multiple SaaS vendors, which may complicate debugging or vendor-specific workflows

## Recent changes

- [2026-04-09] Page created from the `projects.dev` landing page for the Stripe CLI `projects` developer preview

## Sources

- [[sources/articles/stripe-cli]]
```

### wiki/state-of/coding.md (applied)

```markdown
---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-04-09
sources: [sdd-3-tools-fowler, cursor-3-launch, stripe-cli]
---

# State of Coding

Current state of AI tools for software development. Organized by subcategory — each subcategory can have multiple top players. Ambiguity is expected.

## Subcategories

### Spec-driven development

Tools where a structured natural-language spec is the primary input to AI coding agents. The term is contested and the field is early — no clear leader. See [[concepts/spec-driven-development]] for the concept and taxonomy.

- [[tools/kiro]] — VS Code-based; requirements → design → tasks; lightest-weight, mostly spec-first *(as of 2026-04-09)*
- [[tools/spec-kit]] — GitHub; CLI scaffolder + slash commands; constitution → specify → plan → tasks; most customizable *(as of 2026-04-09)*
- [[tools/tessl]] — CLI + MCP server; only tool pursuing spec-as-source; private beta *(as of 2026-04-09)*

### Agentic coding workspace

Coding tools whose primary UI is built around managing one or more AI coding agents (local and cloud), rather than file-centric editing with AI assistance bolted on.

- [[tools/cursor]] — Cursor 3 is a unified agent workspace with multi-repo, local↔cloud handoff, plugin marketplace; built from scratch (not a VS Code fork); legacy IDE mode still available *(as of 2026-04-09)*

### Agentic DevOps

Tools that turn app-stack setup into a repeatable command-line workflow across multiple providers, with explicit support for agent-executable provisioning.

- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow provisions hosting, databases, auth, AI, analytics, and more across providers; credentials sync back to the environment and billing can be managed from the CLI *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] Added `agentic-devops` subcategory with [[tools/stripe-cli]] after ingesting the `projects.dev` launch page
- [2026-04-09] Cursor 3 launched; added new `agentic-coding-workspace` subcategory and placed Cursor under it
- [2026-04-09] First content for this page. Added `spec-driven-development` subcategory with Kiro, spec-kit, Tessl after ingesting Fowler's SDD survey.
```

### wiki/state-of/agents.md (applied)

```markdown
---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-09
sources: [cursor-3-launch, advisor-strategy, stripe-cli]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

## Subcategories

### Agent orchestration UIs

Surfaces (desktop, web, mobile, chat) where humans supervise, hand off, and review work across multiple AI agents running in parallel.

- [[tools/cursor]] — Cursor 3's desktop app surfaces local and cloud agents in one sidebar, with handoff between environments and demos/screenshots from cloud agents *(as of 2026-04-09)*

### Model orchestration

Patterns that combine models of different sizes or costs inside a single agentic task. Concerned with *how* agents are structured internally (which model runs the loop, which model steps in when), not with the user-facing surface.

- [[workflows/advisor-strategy]] — Anthropic: a small executor (Sonnet or Haiku) drives the loop and escalates to Opus as an *advisor* only when stuck. Shipped as a server-side `advisor_20260301` tool on the Claude API, making it a one-line change to a Messages request. Reported +2.7% on SWE-bench Multilingual *and* −11.9% cost for Sonnet+Opus-advisor vs Sonnet alone *(as of 2026-04-09)*

### Agentic DevOps

Agent-compatible tools that let a model provision external services and receive credentials through a repeatable CLI workflow instead of clicking through SaaS dashboards.

- [[tools/stripe-cli]] — Stripe explicitly pitches the CLI `projects` flow for "you or your agents": provision services across providers, sync credentials back to the environment, and manage upgrades or billing from the CLI *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] Added `agentic-devops` subcategory with [[tools/stripe-cli]] after ingesting the `projects.dev` landing page
- [2026-04-09] Added `model-orchestration` subcategory with [[workflows/advisor-strategy]] after ingesting Anthropic's advisor-strategy launch post.
- [2026-04-09] First content for this page. Added `agent-orchestration-ui` subcategory with Cursor after ingesting the Cursor 3 launch post.
```

### wiki/sources/articles/stripe-cli.md (applied)

```markdown
---
title: Stripe CLI `projects` developer preview
type: source
source_type: article
source_file: raw/articles/2026-04-09-projectsdev.md
url: https://projects.dev/
ingested: 2026-04-09
domains: [coding, agents]
---

# Stripe CLI `projects` developer preview

Landing page for the Stripe CLI `projects` developer preview, which turns multi-provider service provisioning into a CLI workflow. The notable angle is that the workflow is framed as equally usable by human developers and AI agents: provision resources in accounts you own, sync credentials back into the environment, and centralize upgrades, usage, and billing through Stripe.

## Influenced pages

- [[tools/stripe-cli]] — new tool page, main subject of the ingest
- [[state-of/coding]] — added `agentic-devops` subcategory and placed Stripe CLI under it
- [[state-of/agents]] — added the same subcategory from an agent-execution angle

## Key claims extracted

- The `stripe projects` workflow is in **developer preview** / early access
- Main promise: provision and manage multiple services from the CLI
- Explicitly pitched for "you or your agents"
- Scope includes hosting, databases, auth, AI, analytics, and more
- Resources are provisioned in accounts the user owns
- Credentials generated during provisioning sync back into the environment
- Changes are described as auditable and repeatable
- Billing details can be set up once and shared across the SaaS stack
- Upgrades, downgrades, usage monitoring, and subscription management are part of the CLI workflow
- Example commands shown: `stripe projects init`, `catalog`, `add`, `upgrade`
- Example provider/service format shown: `railway/hosting`

## Caveats

- The raw source is a marketing landing page, not detailed product docs
- The supported-provider list is not fully captured in the extract
- No benchmarks, pricing, or production customer examples are included in the page
```

### wiki/index.md (applied)

```markdown
---
title: Wiki Index
type: index
as_of: 2026-04-09
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page (via a proposal), add its index entry under the correct section. One line per page: wikilink + one-line description + `(as_of: YYYY-MM-DD)`.

---

## State of

Read-me-first dashboards per domain.

- [[state-of/coding]] — current state of AI coding tools and workflows *(as_of: 2026-04-09)*
- [[state-of/models]] — current state of foundation models *(as_of: —)*
- [[state-of/agents]] — current state of agentic systems and tool use *(as_of: 2026-04-09)*
- [[state-of/legal]] — current state of AI in legal practice *(as_of: 2026-04-09)*

## Models

Foundation models. One page per model family or generation.

- [[models/composer-2]] — Cursor's in-house frontier coding model; stub *(as_of: 2026-04-09)*

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/cursor]] — Cursor 3 agentic coding workspace; multi-repo, local↔cloud agent handoff *(as_of: 2026-04-09)*
- [[tools/harvey]] — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-09)*
- [[tools/kiro]] — VS Code-based SDD tool, 3-doc workflow *(as_of: 2026-04-09)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2026-04-09)*
- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow for provisioning and managing app-stack services across providers *(as_of: 2026-04-09)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2026-04-09)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

_(empty)_

## Workflows

Reusable patterns and recipes.

- [[workflows/advisor-strategy]] — Anthropic's small-executor + Opus-advisor escalation pattern, now a server-side `advisor_20260301` tool on the Claude API *(as_of: 2026-04-09)*

## Concepts

Ideas and techniques (RAG, context engineering, compound engineering, etc.).

- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, critiques *(as_of: 2026-04-09)*

## Trends

Things being watched that haven't solidified yet.

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-09)*

## Sources

See `wiki/sources/` — source summaries are not indexed here (they're many and cheap). Use `grep` or Glob when you need them.

---

## Page count

- state-of: 4 (3 populated, 1 skeleton)
- models: 1
- tools: 6
- benchmarks: 0
- workflows: 1
- concepts: 1
- trends: 1

**Total content pages: 10.** The wiki is in the bootstrap phase (<30 pages) — categorization discipline is relaxed.
```

## Resolution notes

- Renamed the tool from "Stripe Projects" to **Stripe CLI** based on the inline comment in the proposal.
- Renamed the proposed subcategory from `stack-provisioning-cli` to **`agentic-devops`** based on the inline answer in the proposal.
- Kept the dual-domain classification `domains: [coding, agents]` as approved in the inline answer.
