---
type: proposal
sources:
  - raw/newsletters/2026-07-01-aiewf-daily-dispatch-loops-software-factories.md
  - raw/newsletters/2026-07-01-how-cursor-deploys-ai-inside-the-enterprise.md
  - raw/newsletters/2026-07-01-warp-ceo-zach-lloyd-on-why-software-factories-are.md
  - raw/newsletters/2026-07-01-forward-deployed-engineers-and-the-future-of-softw.md
status: pending
created: 2026-07-06
---

# Proposal: Software factories and forward-deployed agent engineering

## Summary
AIEWF and related Latent Space coverage converges on a shift from individual coding assistants to lifecycle-level software factories. The sources connect long-running agents, enterprise deployment teams, FDEs, and "agent engineers" who bind agents into customer workflows, APIs, SOPs, release processes, and change management.

## Intended changes

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add a "software factory loop" pattern.
    > **Draft pattern:** Software factory loop — long-running agents cover planning, design, coding, test, review, deployment, maintenance, and feedback, with humans supervising interfaces, policies, and escalation rather than editing every artifact.

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add FDE/agent-engineer rollout pattern.
    > **Draft guidance:** Treat agent deployment as workflow engineering. The hard work is mapping enterprise systems, permissions, SOPs, tone, release gates, and incident paths, not merely installing an assistant.

- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add organizational signal: FDE teams expand as software factories move into enterprise adoption.

- [x] **Create** `wiki/sources/newsletters/software-factories-fde-2026-07.md` — consolidated source summary.

## Updated Page Snippets

### `wiki/workflows/agentic-orchestration-patterns.md`

> **Before:**
> `- **Control layer before software factory.** The AI Engineer World Fair loops debate sharpened the current constraint: loops are already useful, but the field has not settled the control layer for permissions, cost ceilings, review bottlenecks, and recovery. Treat "software factory" as a destination, not a starting architecture.`

> **After:**
> `- **Control layer before software factory.** The AI Engineer World Fair loops debate sharpened the current constraint: loops are already useful, but the field has not settled the control layer for permissions, cost ceilings, review bottlenecks, and recovery. Treat "software factory" as a destination, not a starting architecture.`
> `- **Software factory loop.** Long-running agents can cover planning, design, coding, testing, review, deployment, maintenance, and feedback, while humans supervise interfaces, policies, escalation, and customer-specific workflow fit rather than editing every artifact.`

### `wiki/training/ai-enablement-software-development.md`

> **Before:**
> `- Invest in CI/CD capacity, test infrastructure, and deployment rollback as part of the AI adoption budget — not only developer tooling`

> **After:**
> `- Invest in CI/CD capacity, test infrastructure, deployment rollback, and workflow-integration capacity as part of the AI adoption budget — not only developer tooling. Enterprise software factories need people who map systems, permissions, SOPs, and release gates into the agent loop.`

### `wiki/trends/agents-reshape-organizations.md`

> **Before:**
> `- **Frontier labs are moving downstream into deployment services.** Current coverage frames OpenAI and Anthropic as selling workflow design, context wiring, permissions, evals, and human handoff systems around models rather than only API access.`

> **After:**
> `- **Frontier labs and agent-tool vendors are moving downstream into deployment services.** Current coverage frames OpenAI, Anthropic, Cursor, Warp, and Sierra-style teams as selling workflow design, context wiring, permissions, evals, human handoff systems, and forward-deployed implementation around agents rather than only model or tool access.`

## Page Drafts

### `wiki/sources/newsletters/software-factories-fde-2026-07.md` (new)

```md
---
title: Software factories and forward-deployed agent engineering
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-01-aiewf-daily-dispatch-loops-software-factories.md
published: 2026-07-01
ingested: 2026-07-06
domains: [coding, agents, training]
---

# Software factories and forward-deployed agent engineering

AIEWF and Latent Space coverage describes software factories as lifecycle-level systems: agents participate across planning, design, coding, testing, review, deployment, monitoring, and maintenance. Related interviews with Cursor, Warp, and Sierra emphasize FDE and agent-engineering teams that adapt these systems to enterprise workflows rather than selling a generic assistant.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — software factory loop pattern
- [AI enablement for software development](../../training/ai-enablement-software-development.md) — FDE/agent-engineer rollout guidance
- [Agents reshape organizations](../../trends/agents-reshape-organizations.md) — organizational signal

## Key claims extracted
- Cursor frames enterprise adoption around deploying AI software factories into real workflows.
- Warp describes Oz as automating the software-engineering loop across triage, spec, implementation, review, verification, shipping, and monitoring.
- Sierra frames agent engineers as customer-facing implementers who connect production agents to systems, APIs, SOPs, tone, and release processes.
```
