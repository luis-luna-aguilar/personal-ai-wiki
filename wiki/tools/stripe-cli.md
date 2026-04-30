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

- [Stripe CLI `projects` developer preview](../sources/articles/stripe-cli.md)
