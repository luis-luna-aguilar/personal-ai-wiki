---
title: Linked billing on the Claude Platform
type: source
source_type: article
source_file: raw/articles/2026-11-23-claudecom-resources-articles-linked-billing-on-claude-platfo.md
url: https://claude.com/resources/articles/linked-billing-on-claude-platform
published: 2026-11-17
ingested: 2026-11-23
domains: [agents, training]
---

# Linked billing on the Claude Platform

Anthropic's announcement of linked billing (beta) on the Claude Platform. Third-party platforms such as coding agents and workflow tools can let their customers pay for Claude API usage by linking the customer's Claude Platform organization instead of sharing an API key. Anthropic hosts the approval flow and bills the customer directly; customers set per-platform spend limits and can unlink at any time.

## Influenced pages
- [Claude Platform](../../tools/claude-platform.md) — new page; linked billing, Usage and Cost Analytics API, Claude Marketplace
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — FinOps control for third-party tool spend

## Key claims extracted
- Launched in beta on 2026-11-17 on the Claude Platform.
- No API key changes hands: usage is billed directly to the customer's linked organization; platforms store no customer keys, and customer keys never leave their organization.
- Platforms: Anthropic hosts the approval flow and billing (no metering or invoicing to build); per-customer request count, token usage, and models used in Console or via the Usage and Cost Analytics API (beta); per-request choice of whether the platform or the end customer pays.
- Customers: link through Anthropic's hosted flow; a Console user with Owner, Admin, or Billing role approves once for the whole organization; draw down an existing Anthropic commitment or pay as you go; monthly spend limit per platform or a default for each; spend per linked platform shown in Console; unlink from Console at any time.
- Requests run in the platform's organization, so customer-organization settings such as IP allowlists, encryption keys, and data retention do not apply.
- Supporting platforms at launch: Asana, ClickHouse, Factory, Gumloop, Harness, Higgsfield AI, Kilo Code, Linear, Major, Mintlify, Omni, OpenArt, Niteshift, Railway, Ramp, Runlayer, Tessera, Tines, and Warp.
- Platforms add support by creating an app in Console; customers can find supporting platforms on Claude Marketplace.
