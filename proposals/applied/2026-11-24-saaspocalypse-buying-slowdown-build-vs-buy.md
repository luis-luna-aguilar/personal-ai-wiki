---
type: proposal
source: raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
sources:
  - raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
  - raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
  - raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
  - raw/tweets/2026-11-24-xcom-jasonlk-2122449076990185948.md
status: pending
created: 2026-11-24
---

# Proposal: The "SaaSpocalypse" looks like a buying slowdown; where to build versus buy

## Summary

### In short
The feared "SaaSpocalypse", customers leaving software vendors to vibe-code their own tools, looks so far like a slowdown in new purchases rather than churn: Jason Lemkin's slide shows HubSpot keeping 101% net revenue retention while new customers fell by half in two quarters. Notion's Ivan Zhao and Every's Dan Shipper sketch where the line falls: people build the daily tools they want to tinker with and keep buying shared systems that encode how a team works. The proposal creates one short trend page and four source pages. Reason to hesitate: scope, since it opens a new trend page for a signal the triage rated lightweight and opinion-heavy.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Three Every newsletters from mid-November 2026 circle the same question: if anyone can build software with an AI agent, will companies stop paying for it? On 16 November SaaStr's Jason Lemkin posted a slide on X: HubSpot's customers were mostly staying (101% net revenue retention), but new customers fell by half in two quarters. Every relayed it on 18 November, adding that Monday.com's net-new customers were also down. Every's head of evals Mike Taylor reads it as a buying slowdown, not an exodus: like hiring with few layoffs but fewer new hires, existing customers stay while new ones dry up. AI made it worse by eroding the search-engine traffic HubSpot grew on.

The same issue summarized Notion CEO Ivan Zhao at Every's Thesis: 2027: build the tools you use daily and want to customize; buy what you would rather someone else got right, and security-critical systems. He adds that agent-built code quickly becomes hard to follow, and Notion uses a kanban board to see what its agents are building. On 13 November Shipper argued SaaS survives because adopting a tool is a team agreeing how work happens, which personal vibe-coding does not replace. And on 19 November Every reported that staff writer Katie Parrott built her own word processor, Wordbetter, on Fable 5.2.

### What changes
The wiki has no page on whether agents erode demand for SaaS; the term appears only in a June source page quoting Figma.

- New page `trends/agents-and-saas-demand.md`: the slowdown-not-churn reading of Lemkin's data, the build-versus-buy line, the team-agreement argument, and the personal-software examples, with what to watch.
- **Agents reshape organizations** gains a Related link to it (no body change, since that page is at 98% of its length ceiling).
- Four new source pages (Lemkin's post and three newsletter stories); the index gains the new trend page.

### What to weigh
Scope: a new trend page rather than a section, because the natural host, Agents reshape organizations, is at 98% of its length ceiling and the question (does agent-built software erode SaaS demand?) is distinct from it; the page is kept short and attributes each claim. Lemkin's post was read as text (fetched through the browser); the slide image and the Monday.com figure come via Every's summary.

## Intended changes

- [ ] **Create** `wiki/trends/agents-and-saas-demand.md` — new trend page
- [ ] **Update** `wiki/trends/agents-reshape-organizations.md` — add one `## Related` line; no other change, `as_of` unchanged
- [ ] **Update** `wiki/index.md` — add the new trend page under Trends; trends count 28 → 29, total 311 → 312
- [ ] **Create** `wiki/sources/tweets/jasonlk-hubspot-new-customers-2026-11-16.md` — source summary (Lemkin's post)
- [ ] **Create** `wiki/sources/newsletters/every-saas-slowdown-zhao-build-buy-2026-11-18.md` — story page (Lemkin chart, Zhao podcast)
- [ ] **Create** `wiki/sources/newsletters/every-why-saas-still-matters-2026-11-13.md` — story page (Dan Shipper's argument)
- [ ] **Create** `wiki/sources/newsletters/every-wordbetter-2026-11-19.md` — story page (Wordbetter)

## Page drafts

### wiki/trends/agents-and-saas-demand.md (new)

```
---
title: Agents and SaaS demand
type: trend
domains: [agents, coding]
tags: [agentic]
as_of: 2026-11-19
sources: [jasonlk-hubspot-new-customers-2026-11-16, every-saas-slowdown-zhao-build-buy-2026-11-18, every-why-saas-still-matters-2026-11-13, every-wordbetter-2026-11-19]
---

# Agents and SaaS demand

Whether AI agents that let anyone build software erode demand for bought software. The fear has a name, the "SaaSpocalypse"; the evidence so far points to fewer new purchases rather than customers leaving, and to a line between tools people build for themselves and systems teams keep buying.

## Current status (as of 2026-11-19)

- **Slowdown, not churn.** Jason Lemkin (SaaStr, November 2026): HubSpot's customers were mostly staying (101% net revenue retention), but new customers fell by half in two quarters; Every adds that Monday.com's net-new customers are also down. Every's Mike Taylor reads it as a buying slowdown, like hiring with few layoffs but fewer new hires, made worse by AI eroding the search traffic HubSpot grew on.
- **Build what you tinker with, buy what must be right.** Notion CEO Ivan Zhao: build the daily tools you want to customize; buy what you would rather someone else got right, and security-critical systems your company would struggle to maintain. He adds that agent-built software quickly becomes hard to follow; Notion uses a kanban board to see what its agents are building.
- **SaaS as a team agreement.** Every's Dan Shipper: adopting a tool is a team agreeing how work happens and handing off the job of keeping that system coherent, which one person's vibe-coded tool does not provide. His prediction is a shift from one set of rules enforced on everyone toward building blocks the users shape.
- **Professionals now build their own pro tools.** Every staff writer Katie Parrott built Wordbetter, a word processor with her writing skills built in, on [Claude Fable 5.2](../models/claude-fable-5-2.md) (November 2026), after abandoning an AI editor in 2025; a colleague built a rival, Everytype, on [Fable 5.1](../history/models/claude-fable-5-1.md).

## What to watch

- Whether net-new declines spread across SaaS categories and whether retention starts to slip.
- Whether vendors reposition as the data and permissions layer agents work on (Zhao's framing for Notion) rather than as the interface.

## Recent changes

- [2026-11-19] Page created from Lemkin's HubSpot post and Every's November coverage: HubSpot new customers halved at 101% NRR, Zhao's build-versus-buy line, Shipper's team-agreement argument, and Wordbetter.

## Related

- [Agents reshape organizations](agents-reshape-organizations.md) — the broader shift in how organizations work as agents take on coordination
- [Agent-readable web](../concepts/agent-readable-web.md) — SaaS products exposing docs, APIs and MCP servers so outside agents can operate them

## Sources

- [Jason Lemkin on X — HubSpot new customers halved at 101% NRR](../sources/tweets/jasonlk-hubspot-new-customers-2026-11-16.md)
- [Every — SaaS slowdown and Ivan Zhao on when to build your own tools](../sources/newsletters/every-saas-slowdown-zhao-build-buy-2026-11-18.md)
- [Every — Why SaaS still matters](../sources/newsletters/every-why-saas-still-matters-2026-11-13.md)
- [Every — Our staff writer built her own word processor](../sources/newsletters/every-wordbetter-2026-11-19.md)
```

### wiki/trends/agents-reshape-organizations.md (updated)

`## Related`, append:

```
- [Agents and SaaS demand](agents-and-saas-demand.md) — whether agent-built software erodes demand for bought SaaS: slowdown-not-churn data and the build-versus-buy line
```

### wiki/index.md (updated)

Under `## Trends`, insert after the `trends/ai-labor-market-effects` line:

```
- [trends/agents-and-saas-demand](trends/agents-and-saas-demand.md) — whether agents erode demand for SaaS: HubSpot new customers halved at 101% NRR, Zhao's build-versus-buy line, SaaS as a team agreement, professionals building their own tools *(as_of: 2026-11-19)*
```

Page count: `- trends: 29` and `**Total content pages: 312.**`

### wiki/sources/tweets/jasonlk-hubspot-new-customers-2026-11-16.md (new)

```
---
title: "Jason Lemkin on X: Why HubSpot needed to get back to founder mode, in one slide"
type: source
source_type: tweet
source_file: raw/tweets/2026-11-24-xcom-jasonlk-2122449076990185948.md
url: https://x.com/jasonlk/status/2122449076990185948
published: 2026-11-16
ingested: 2026-11-24
domains: [agents]
---

# Jason Lemkin on X: Why HubSpot needed to get back to founder mode, in one slide

SaaStr founder Jason Lemkin's post on HubSpot's customer numbers, the data point behind the "SaaSpocalypse is a slowdown" reading.

## Influenced pages

- [Agents and SaaS demand](../../trends/agents-and-saas-demand.md) — slowdown-not-churn data

## Key claims extracted

- HubSpot customers were mostly staying: 101% net revenue retention
- New customers fell by half in two quarters
```

### wiki/sources/newsletters/every-saas-slowdown-zhao-build-buy-2026-11-18.md (new)

```
---
title: "SaaS slowdown and Ivan Zhao on when to build your own tools — Every (Microsoft's CEO Wants Every Company to Own Its Own Model)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
url: https://every.to/context-window/microsoft-s-ceo-wants-every-company-to-own-its-own-model
published: 2026-11-18
ingested: 2026-11-24
domains: [agents]
---

# SaaS slowdown and Ivan Zhao on when to build your own tools — Every

Story page for two items in Every's 18 November Context Window: Mike Taylor's read of Jason Lemkin's SaaS net-new data, and the Every Podcast summary of Notion CEO Ivan Zhao on which tools to build and which to buy.

## Influenced pages

- [Agents and SaaS demand](../../trends/agents-and-saas-demand.md) — slowdown-not-churn reading; build-versus-buy line

## Key claims extracted

- Relays Lemkin's chart: HubSpot net-new customers down while retention stays high; Monday.com net-new also down
- Taylor: the "SaaSpocalypse" is a slowdown in buying, not customers leaving to vibe-code; AI eroded HubSpot's SEO acquisition engine
- Zhao: build the tools you use daily and want to customize; buy what you'd rather someone else got right and security-critical systems
- Zhao: agents need well-organized company data; Notion as keeper of company data with access controls
- Zhao: within a week of agents working on a large codebase "you sort of don't understand what's going on"; Notion uses a kanban board to see what agents are building
```

### wiki/sources/newsletters/every-why-saas-still-matters-2026-11-13.md (new)

```
---
title: "Why SaaS still matters — Every (Your Attention Is AI's New Bottleneck)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
url: https://every.to/context-window/your-attention-is-ai-s-new-bottleneck
published: 2026-11-13
ingested: 2026-11-24
domains: [agents]
---

# Why SaaS still matters — Every (Your Attention Is AI's New Bottleneck)

Story page for the Frontier-feed item in Every's 13 November Context Window: Dan Shipper's argument for why teams keep paying for shared software when anyone can vibe-code their own.

## Influenced pages

- [Agents and SaaS demand](../../trends/agents-and-saas-demand.md) — SaaS as a team agreement

## Key claims extracted

- Adopting a tool is a team agreeing that work happens a certain way and handing off the job of keeping that system coherent
- Most SaaS works like an authoritarian regime (one person's rules enforced on everyone); the alternative is a "liberal constitution" of building blocks users shape
```

### wiki/sources/newsletters/every-wordbetter-2026-11-19.md (new)

```
---
title: "Our staff writer built her own word processor — Every (What We Let Our Agents Buy)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
url: https://every.to/context-window/what-we-let-our-agents-buy
published: 2026-11-19
ingested: 2026-11-24
domains: [agents]
---

# Our staff writer built her own word processor — Every (What We Let Our Agents Buy)

Story page for the Wordbetter item in Every's 19 November Context Window.

## Influenced pages

- [Agents and SaaS demand](../../trends/agents-and-saas-demand.md) — professionals building their own pro tools

## Key claims extracted

- Katie Parrott abandoned her first AI editor in 2025 after six weeks of debugging
- In November 2026 she introduced Wordbetter, a word processor with her Compound Writing skills, voice/style/audience files and an on-demand AI writing coach, built with Fable 5.2
- First feature request (dark mode) returned as a draft pull request in 17 minutes
- Kieran Klaassen built a rival word processor, Everytype, with Fable 5.1
```

## Schema / vocabulary additions

None.

## Open questions

None.
