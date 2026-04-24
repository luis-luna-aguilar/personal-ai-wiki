---
type: proposal
source: raw/deep-research/2026-04-24 Agentic Devops.md
status: applied
created: 2026-04-24
---

# Proposal: Broaden agentic DevOps tooling coverage

## Summary

The current wiki treats `agentic-devops` mostly as provision-through-a-CLI. The report surfaces a broader, more important layer: Kubernetes-native agent runtimes, diagnostic tools, approval-gated control planes, and post-deploy verification surfaces. This proposal broadens the meaning of `agentic-devops` in the schema, updates the state-of pages, and creates four selective tool pages:

- **Kagent** — Kubernetes-native agent runtime / control plane
- **K8sGPT** — Kubernetes diagnostics and triage
- **Skyflo** — approval-gated AI control layer for Kubernetes and CI/CD
- **Checkly** — Playwright-based synthetic verification / monitoring as code

I recommend *broadening* the existing `agentic-devops` subcategory instead of adding a new one. The category already exists, and the new evidence shows that provisioning was only one early slice of a wider agentic infrastructure surface.

## Schema / vocabulary change

- [x] **Update** `wiki/_schema/subcategories.md`
  > Broaden `agentic-devops`

**Before:**

```md
### agentic-devops
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** CLI-native tools that provision and manage third-party app infrastructure and credentials across multiple providers, in workflows designed to be executable by humans or agents.
- **Examples:** [[tools/stripe-cli]]
```

**After:**

```md
### agentic-devops
- **Parent domain(s):** coding, agents
- **Applies to types:** tool
- **Definition:** Tools and control planes that let humans or agents provision, diagnose, operate, verify, and safely mutate infrastructure through repeatable, auditable interfaces — spanning provisioning CLIs, Kubernetes diagnostics, approval-gated execution layers, and post-deploy verification.
- **Examples:** [[tools/stripe-cli]], [[tools/kagent]], [[tools/k8sgpt]], [[tools/skyflo]], [[tools/checkly]]
```

## Intended changes

- [x] **Create** `wiki/tools/kagent.md`
- [x] **Create** `wiki/tools/k8sgpt.md`
- [x] **Create** `wiki/tools/skyflo.md`
- [x] **Create** `wiki/tools/checkly.md`
- [x] **Update** `wiki/state-of/agents.md`
- [x] **Update** `wiki/state-of/coding.md`
- [x] **Update** `wiki/index.md`

## Page drafts

### `wiki/tools/kagent.md` (new)

```md
---
title: Kagent
type: tool
domains: [agents, coding]
subcategory: agentic-devops
tags: [open-source, agentic]
as_of: 2026-04-24
sources: [agentic-devops-deep-research]
---

# Kagent

Kagent is a Kubernetes-native framework for building, deploying, and managing AI agents inside Kubernetes. Its distinctive claim is that production agents need more than a server: they need identity, policy, observability, tool lifecycle management, and human-in-the-loop control on infrastructure teams already trust.

## Current status (as of 2026-04-24)

- Official materials position Kagent as a Kubernetes-native agent runtime
- GitHub README emphasizes agents, model configs, MCP tool servers, and OpenTelemetry tracing as first-class primitives
- Solo's product page frames Kagent as the identity, orchestration, and governance layer for production agents running on Kubernetes
- Official positioning explicitly mentions MCP and A2A support plus human-in-the-loop patterns

## Strengths

- One of the clearest current examples of "agent runtime as infrastructure platform" rather than app-level SDK only
- Strong fit for teams already standardized on Kubernetes
- Makes governance and observability part of the runtime, not a later patch

## Weaknesses / caveats

- Highly Kubernetes-centric
- Product and open-source positioning are still closely tied to Solo's ecosystem and framing

## Sources

- [[sources/deep-research/2026-04-24-agentic-devops]]
```

### `wiki/tools/k8sgpt.md` (new)

```md
---
title: K8sGPT
type: tool
domains: [agents, coding]
subcategory: agentic-devops
tags: [open-source, cli, agentic]
as_of: 2026-04-24
sources: [agentic-devops-deep-research]
---

# K8sGPT

K8sGPT is a Kubernetes diagnostic tool that scans cluster state and explains problems in plain English. It matters to agentic operations because it acts as a structured diagnostic surface: a way for humans or agents to query Kubernetes issues without translating raw cluster noise manually every time.

## Current status (as of 2026-04-24)

- Official README positions K8sGPT as a tool for scanning, diagnosing, and triaging Kubernetes issues
- Docs pitch it as "Kubernetes SRE superpowers"
- Supports multiple model backends and exposes an MCP-related integration surface in the docs/README
- Available both as CLI tooling and deeper cluster/operator-style usage

## Strengths

- Clear diagnostic use case rather than vague agent-platform positioning
- Useful as a reusable skill surface inside a broader agentic infrastructure stack
- Good bridge between traditional kubectl-heavy ops work and agent-friendly workflows

## Weaknesses / caveats

- Kubernetes-specific rather than a general infrastructure tool
- Best understood as diagnosis/triage infrastructure, not as a full agent runtime or control plane

## Sources

- [[sources/deep-research/2026-04-24-agentic-devops]]
```

### `wiki/tools/skyflo.md` (new)

```md
---
title: Skyflo
type: tool
domains: [agents, coding]
subcategory: agentic-devops
tags: [open-source, agentic]
as_of: 2026-04-24
sources: [agentic-devops-deep-research]
---

# Skyflo

Skyflo is a self-hosted AI control layer for Kubernetes and CI/CD workflows. Its core product idea is governance, not chat: natural-language intent is translated into typed infrastructure operations, but every mutating tool call pauses for explicit approval and the system verifies the result afterward.

## Current status (as of 2026-04-24)

- Official site describes Skyflo as approval-gated by design
- The platform's control loop is explicit: plan, approve, execute, verify
- Site copy says read operations flow freely while mutating operations require explicit human approval
- Official materials emphasize typed MCP-based execution, auditability, and self-hosted deployment

## Strengths

- One of the clearest concrete expressions of deterministic governance around infrastructure agents
- Strong fit for teams that want agents near production systems without pretending approval gates are optional
- More operationally serious than "chat with kubectl" wrappers

## Weaknesses / caveats

- The approval gate is the point, but it also limits full autonomy
- Current framing is heavily centered on Kubernetes and CI/CD workflows

## Sources

- [[sources/deep-research/2026-04-24-agentic-devops]]
```

### `wiki/tools/checkly.md` (new)

```md
---
title: Checkly
type: tool
domains: [agents, coding]
subcategory: agentic-devops
tags: [closed-source]
as_of: 2026-04-24
sources: [agentic-devops-deep-research]
---

# Checkly

Checkly is a synthetic monitoring platform centered on Playwright-based browser checks, API checks, and Monitoring as Code. In the agentic infrastructure context, it matters as the post-deploy verification layer: a way to validate that infrastructure or application changes still work from the outside in.

## Current status (as of 2026-04-24)

- Official docs emphasize Monitoring as Code and synthetic monitoring integrated into CI/CD
- Checkly supports Playwright-based browser checks and Playwright Check Suites
- Docs position existing Playwright suites as reusable for production monitoring, not only pre-merge testing
- The product sits closer to verification and external validation than to diagnosis or mutation

## Strengths

- Strong bridge between application verification and infrastructure verification
- Useful for "did the change actually work?" loops after deploys
- Relevant to both DevOps teams and browser/self-verification patterns for agentic systems

## Weaknesses / caveats

- Closed-source commercial platform
- More post-deploy validation than full infrastructure operations platform

## Sources

- [[sources/deep-research/2026-04-24-agentic-devops]]
```

## State-of updates

### `wiki/state-of/agents.md`

Replace the current `### Agentic DevOps` section:

```md
### Agentic DevOps

Agent-compatible tools that let a model provision external services and receive credentials through a repeatable CLI workflow instead of clicking through SaaS dashboards.

- [[tools/stripe-cli]] — Stripe explicitly pitches the CLI `projects` flow for "you or your agents": provision services across providers, sync credentials back to the environment, and manage upgrades or billing from the CLI *(as of 2026-04-09)*
```

With:

```md
### Agentic DevOps

Agent-compatible infrastructure tools and control planes for provisioning, diagnosing, operating, and verifying live systems through repeatable, auditable interfaces.

- [[tools/stripe-cli]] — early provisioning/control-plane example: provision services across providers, sync credentials back to the environment, and manage upgrades or billing from a CLI designed for humans or agents *(as of 2026-04-09)*
- [[tools/kagent]] — Kubernetes-native agent runtime / governance layer with MCP tool servers, tracing, and human-in-the-loop control *(as of 2026-04-24)*
- [[tools/k8sgpt]] — Kubernetes diagnosis and triage surface that turns cluster problems into agent-usable plain-English context *(as of 2026-04-24)*
- [[tools/skyflo]] — approval-gated AI control layer for Kubernetes and CI/CD; strongest current example of explicit mutate-with-approval ops design *(as of 2026-04-24)*
- [[tools/checkly]] — outside-in post-deploy verification via synthetic monitoring and Playwright-based checks *(as of 2026-04-24)*
```

### `wiki/state-of/coding.md`

Replace the current `### Agentic DevOps` section:

```md
### Agentic DevOps

Tools that turn app-stack setup into a repeatable command-line workflow across multiple providers, with explicit support for agent-executable provisioning.

- [[tools/stripe-cli]] — Stripe CLI's developer-preview `projects` workflow provisions hosting, databases, auth, AI, analytics, and more across providers; credentials sync back to the environment and billing can be managed from the CLI *(as of 2026-04-09)*
```

With:

```md
### Agentic DevOps

Tools that move AI coding systems closer to full software delivery by covering provisioning, diagnosis, deployment safety, and post-deploy verification rather than code generation alone.

- [[tools/stripe-cli]] — provisioning-first example: agent-compatible CLI for standing up and managing app-stack services across providers *(as of 2026-04-09)*
- [[tools/k8sgpt]] — diagnosis surface for Kubernetes-heavy software teams; useful when coding-agent output needs operational interpretation and triage *(as of 2026-04-24)*
- [[tools/skyflo]] — strongest current example of approval-gated execution for infrastructure mutations triggered from natural-language operational intent *(as of 2026-04-24)*
- [[tools/checkly]] — post-deploy verification layer that turns Playwright/browser checks into continuous synthetic validation *(as of 2026-04-24)*
```

Add one recent change to both pages:

```md
- [2026-04-24] Broadened `agentic-devops` from provisioning-only CLI workflows toward a fuller infrastructure-operations stack: diagnosis, approval-gated mutation, and post-deploy verification
```

### `wiki/index.md`

Add under `## Tools`:

```md
- [[tools/kagent]] — Kubernetes-native runtime and governance layer for production AI agents *(as_of: 2026-04-24)*
- [[tools/k8sgpt]] — Kubernetes diagnostics and triage tool usable by humans and agents *(as_of: 2026-04-24)*
- [[tools/skyflo]] — approval-gated AI control layer for Kubernetes and CI/CD operations *(as_of: 2026-04-24)*
- [[tools/checkly]] — synthetic verification and Monitoring as Code built around Playwright and API checks *(as_of: 2026-04-24)*
```

## Verification notes

- **Kagent:** verified via GitHub README and Solo product page
- **K8sGPT:** verified via official docs and GitHub README
- **Skyflo:** verified via official site; approval gate and plan/approve/execute/verify loop are explicitly documented
- **Checkly:** verified via official docs for Monitoring as Code and Playwright checks
