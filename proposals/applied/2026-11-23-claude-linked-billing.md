---
type: proposal
source: raw/articles/2026-11-23-claudecom-resources-articles-linked-billing-on-claude-platfo.md
status: pending
created: 2026-11-23
---

# Proposal: Linked billing on the Claude Platform

## Summary

### In short

Companies no longer need to hand an Anthropic API key to every third-party AI tool. With linked billing they link their Claude Platform organization once, set a monthly spend limit per tool, and keep paying from their existing Anthropic commitment. Anthropic launched it in beta on 17 November with 19 platforms, among them Linear, Warp, Asana, and Factory. The proposal adds one AI FinOps control to Cost-aware AI task routing and creates a source page. Reason to hesitate: it is billing plumbing with no Claude Platform page to live on, so most of the detail stays on the source page.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

Anthropic's 17 November 2026 post introduces linked billing, in beta, on the Claude Platform (Anthropic's developer platform and Console). Until now, using Claude inside someone else's product, such as a coding agent or a workflow tool, usually meant pasting in your own API key. The post compares that key to a password: whoever holds it can run up charges on your account, and the platform has to store and protect it.

With linked billing the customer links their organization through a flow Anthropic hosts, and usage is billed to that organization directly; no key changes hands. A Console user with an Owner, Admin, or Billing role approves the link once for the whole organization, sets a monthly spend limit per platform (or a default for all), sees spend per platform in Console, and can unlink at any time. Usage can draw down an existing commitment or be paid as it goes. Platforms see each linked customer's requests, tokens, and models, and can decide request by request whether they or the customer pays. One caveat matters for security teams: requests run in the platform's organization, so the customer's own IP allowlists, encryption keys, and data-retention settings do not apply.

### What changes

The wiki's AI FinOps guidance covers budgets, routing, caching, and effort levels, but not how spend on third-party tools is controlled.

- **Cost-aware AI task routing** gains one AI FinOps bullet: link third-party AI tools to the company's own model account with a per-tool spend limit instead of sharing keys, with the settings caveat kept beside it. One Recent-changes entry dated 17 November; page date moves from 25 September to 17 November.
- Index line refreshed; one new source page.

### What to weigh

Whether this belongs on a Claude Platform tool page the wiki does not have yet; the draft keeps it to the FinOps control and asks below. The 19 named platforms get no updates of their own.

## Intended changes

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — one bullet appended to `## AI FinOps controls`; adds one Recent-changes entry dated 2026-11-17, placed below the existing 2026-11-23 entry (4 of 10, no spill); append 1 source id and 1 link; `as_of` 2026-09-25 → 2026-11-17
- [ ] **Update** `wiki/index.md` — refresh the `training/cost-aware-ai-task-routing` line (description and date)
- [ ] **Create** `wiki/sources/articles/claude-platform-linked-billing-2026-11-17.md` — source summary

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter changes:

```
as_of: 2026-11-17
sources: [...existing..., claude-platform-linked-billing-2026-11-17]
```

`## AI FinOps controls` — one bullet appended at the end of the list:

```
- Bring third-party AI tool spend under the company's own model account instead of handing each tool an API key. Anthropic's linked billing (beta, November 2026) lets an Owner, Admin, or Billing user link the organization to a supporting platform once, set a monthly spend limit per platform (or a default for all), see spend per platform in Console, draw down the existing Anthropic commitment, and unlink at any time; platforms can choose per request whether they or the customer pays. Check what the link does not carry: requests run in the platform's organization, so the customer's IP allowlists, encryption keys, and data-retention settings do not apply.
```

Recent changes — one entry inserted below the 2026-11-23 entry, above the 2026-10-19 entry:

```
- [2026-11-17] Added a FinOps control for third-party tool spend: Anthropic's linked billing replaces shared API keys with an organization link, per-platform monthly spend limits, and spend visible per platform; the customer's own IP allowlists, encryption keys, and retention settings do not apply to those requests.
```

Sources — one link appended:

```
- [Linked billing on the Claude Platform](../sources/articles/claude-platform-linked-billing-2026-11-17.md)
```

### wiki/index.md (updated)

One line replaced in place:

```
- [training/cost-aware-ai-task-routing](training/cost-aware-ai-task-routing.md) — route work to the cheapest competent executor (scripts, small/open models, frontier, humans); tasteful tokenmaxxing, route by novelty, token allocation as governance, AI FinOps controls including Anthropic's effort rule of thumb and per-platform spend limits via linked billing; case evidence on a separate page *(as_of: 2026-11-17)*
```

### wiki/sources/articles/claude-platform-linked-billing-2026-11-17.md (new)

```
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
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — FinOps control for third-party tool spend

## Key claims extracted
- Launched in beta on 2026-11-17 on the Claude Platform.
- No API key changes hands: usage is billed directly to the customer's linked organization; platforms store no customer keys, and customer keys never leave their organization.
- Platforms: Anthropic hosts the approval flow and billing (no metering or invoicing to build); per-customer request count, token usage, and models used in Console or via the Usage and Cost Analytics API (beta); per-request choice of whether the platform or the end customer pays.
- Customers: link through Anthropic's hosted flow; a Console user with Owner, Admin, or Billing role approves once for the whole organization; draw down an existing Anthropic commitment or pay as you go; monthly spend limit per platform or a default for each; spend per linked platform shown in Console; unlink from Console at any time.
- Requests run in the platform's organization, so customer-organization settings such as IP allowlists, encryption keys, and data retention do not apply.
- Supporting platforms at launch: Asana, ClickHouse, Factory, Gumloop, Harness, Higgsfield AI, Kilo Code, Linear, Major, Mintlify, Omni, OpenArt, Niteshift, Railway, Ramp, Runlayer, Tessera, Tines, and Warp.
- Platforms add support by creating an app in Console; customers can find supporting platforms on Claude Marketplace.
```

## Schema / vocabulary additions

None.

## Open questions

- Should the wiki start a `tools/claude-platform.md` page (Anthropic's developer platform: Console, billing, Marketplace, analytics APIs) to hold launches like this one? The draft keeps linked billing to the FinOps control and the source page.
	- Yes, separate it
