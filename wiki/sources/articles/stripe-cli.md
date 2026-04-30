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

- [Stripe CLI](../../tools/stripe-cli.md) — new tool page, main subject of the ingest
- [Coding](../../history/state-of/coding.md) — added `agentic-devops` subcategory and placed Stripe CLI under it
- [Agents](../../history/state-of/agents.md) — added the same subcategory from an agent-execution angle

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
