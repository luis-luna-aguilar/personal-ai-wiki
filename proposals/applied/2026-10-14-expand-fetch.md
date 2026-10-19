---
type: proposal
source: raw/articles/2026-10-14-expandai-blog-announcing-expand-fetch.md
status: pending
created: 2026-10-14
---

# Proposal: Expand Fetch launch

## Summary

### In short
Agents are confidently wrong about web pages because ordinary page-to-Markdown converters drop icons, break tables, and miss data loaded behind the scenes. Reliable reading takes models that understand the rendered page. Expand Fetch uses one model to sort page elements into keep, cut, or move aside, and another to read the hidden data, scoring 74.1% on Expand's own benchmark against 55.3% for Exa and 27.2% for Firecrawl. This adds a reader-side counterpart to the wiki's publisher-side coverage: a tool page, a new `web-data-extraction` subcategory, and small sections on two state-of pages. Hesitate because approving adds a new vocabulary subcategory that so far holds one tool.

[[#Open questions|Open questions: 1 to answer.]]

### The source
Expand, a small applied research lab that started out building research agents, has launched Expand Fetch, an API that turns any URL into Markdown an agent can rely on. Their pitch is that agents are "confidently wrong" about the web because the converters that feed them drop icons, break tables and miss data the page loads behind the scenes. The example is a pricing page where a ✗ next to "Uptime SLA" disappears in conversion, so the agent says both plans include it.

Fetch combines two models Expand trained from scratch. Iris looks at the page as the browser renders it and sorts each element into three buckets: preserve (main Markdown), prune (ads, cookie banners) or appendix (navigation and footers, kept but moved aside). Expand reports 92.7% F1 on this sorting, against 69.6% for TypeSafe's Jev model. X-Ray reads the hidden JSON a page loads (prices, stock status, customer stories) and returns the useful parts alongside the Markdown. Every fetch is saved as a citable snapshot. Price is $1 per 1,000 fetches.

On MDBench, a private benchmark Expand built with customers (1,094 questions over 326 hard pages, answered by Claude Sonnet 5.5), Expand scores 74.1% against Exa at 55.3% and Firecrawl at 27.2%. Expand says engineers at OpenAI and Amazon Science use it.

### What changes
The wiki covers the agent-readable web only from the publisher side: sites serving Markdown to agents (Vercel) and metering agent access (Cloudflare). It has no page for the reader side, tools that fetch and clean arbitrary pages for agents.

- New page `tools/expand-fetch.md` covering Fetch, Iris, X-Ray, snapshots, Highlights, Crawl and WebSync, with the benchmark claims labelled as vendor-reported.
- New subcategory `web-data-extraction` in the schema, for fetch/crawl/extract APIs built for agents.
- **State of Agents** and **State of Computer Use** each gain a small "Agent web data extraction" section with Expand Fetch as its only entry, plus a Recent-changes line. Both lists are at their cap, so each spills its oldest entry to history. Both page dates move to 14 October.
- **Agent-readable web** gains one bullet framing fetch-side tools as the counterpart for the many sites that don't serve agent-native Markdown, and a Recent-changes line. Page date moves to 14 October.
- **Index** gains the tool line; tool count goes from 95 to 96. One new source page.

### What to weigh
The blog post carries no publication date, so 14 October (the ingest date) stands in for it. Approving also adds a new subcategory, `web-data-extraction`, to the controlled vocabulary. It holds one tool for now, and other fetch and crawl APIs are expected to join it.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/expand-fetch.md` — new tool page

- [ ] **Update** `wiki/state-of/agents.md` — add `### Agent web data extraction` section after `### Deep research tools`; add one Recent-changes entry dated 2026-10-14; add source id; `as_of` → 2026-10-14

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — oldest Recent-changes entry (`[2026-07-02] OpenWiki and wiki memory…`) falls off the cap

- [ ] **Update** `wiki/state-of/computer-use.md` — add `### Agent web data extraction` section after `### Agent-readable web infrastructure`; add one Recent-changes entry dated 2026-10-14; add source id and Sources link; `as_of` → 2026-10-14

- [ ] **Spill** `wiki/state-of/computer-use.md` → `wiki/history/state-of/computer-use.md` — oldest Recent-changes entry (`[2026-05-01] Added Codex…`) falls off the cap

- [ ] **Update** `wiki/concepts/agent-readable-web.md` — one Current-status bullet, one Recent-changes entry dated 2026-10-14, source id + Sources link; `as_of` → 2026-10-14

- [ ] **Update** `wiki/index.md` — add tool line under `## Tools`; tools count 95 → 96; update as_of on state-of/agents, state-of/computer-use, concepts/agent-readable-web lines

- [ ] **Create** `wiki/sources/articles/expand-fetch-launch-2026-10.md` — source summary

## Page drafts

### wiki/tools/expand-fetch.md (new)

```
---
title: Expand Fetch
type: tool
domains: [agents, computer-use]
subcategory: web-data-extraction
tags: [closed-source, agentic]
as_of: 2026-10-14
sources: [expand-fetch-launch-2026-10]
---

# Expand Fetch

Expand's web-fetch API for agents: send a URL, get back accurate Markdown, useful hidden JSON from the page, and a citable snapshot of what was fetched. Built by Expand, an applied research lab that started from research agents misreading pages. Pages are loaded as a real browser loads them, with JavaScript rendering, residential proxies and bot protection handled.

## Current status (as of 2026-10-14)
- Launched with two in-house models that run on every fetch: **Iris** (page-to-Markdown) and **X-Ray** (hidden JSON).
- **Iris** reads the rendered page (element position, size, weight) and sorts each DOM element into *preserve* (main Markdown), *prune* (ads, cookie banners, UI chrome) or *appendix* (nav, footers — kept but moved aside). Vendor-reported: 92.7% F1 on Expand's validation set vs 69.6% for TypeSafe's Jev; ~500K tokens/sec.
- **X-Ray** extracts question-relevant data from the JSON a page loads (prices, stock, map/diagram data), filtering analytics and config. Expand says no other provider it tested returns hidden JSON.
- **Wayback Machine** snapshot of every fetch, with each Markdown line linked back to its source location; **Highlights** returns only passages matching a query (>95% token savings claimed).
- **Crawl** runs Fetch across whole sites (1 credit/page); **WebSync** streams site additions, changes and removals. Pricing $1 per 1,000 fetches.
- Vendor-run, private **MDBench Hard v1** (1,094 questions, 326 hard pages, Claude Sonnet 5.5 answering): Expand 74.1%, Exa 55.3%, Firecrawl 27.2%.

## Why it matters
Most of the web does not serve agent-native Markdown, so agents depend on a fetch layer. Expand's argument is that lossy conversion — dropped icons, broken tables, missing JSON — produces confidently wrong answers, and that heuristic readers (Readability-style "one main content area") can't cover real layouts. The snapshot-per-fetch design also makes agent answers auditable after the page changes.

## Weaknesses / caveats
- All benchmark numbers are vendor-run; MDBench is private and was built around cases where existing systems struggle.
- Named users (engineers at OpenAI and Amazon Science) are vendor claims.

## Recent changes
- [2026-10-14] Launch: Fetch with Iris and X-Ray, Wayback snapshots, Highlights, Crawl, WebSync; $1 per 1,000 fetches.

## Sources
- [Announcing Expand Fetch](../sources/articles/expand-fetch-launch-2026-10.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter: append `expand-fetch-launch-2026-10` to `sources:`; `as_of: 2026-10-14`.

New section, inserted after `### Deep research tools`:

```
### Agent web data extraction

APIs that fetch, clean, and extract web pages for agents, so agents read sites that don't serve agent-native formats. See [Agent-readable web](../concepts/agent-readable-web.md) for the publisher side.

- [Expand Fetch](../tools/expand-fetch.md) — URL → Markdown via a trained page-reading model (Iris), plus hidden-JSON extraction, citable snapshots, Crawl and WebSync; vendor-run benchmark puts it ahead of Exa and Firecrawl *(as of 2026-10-14)*
```

Recent changes — adds one entry at the top:

```
- [2026-10-14] Added `Agent web data extraction` subcategory with [Expand Fetch](../tools/expand-fetch.md): agent-oriented fetch API with trained Markdown (Iris) and hidden-JSON (X-Ray) models; vendor-run MDBench 74.1% vs Exa 55.3%, Firecrawl 27.2%.
```

Spills the oldest entry: `- [2026-07-02] OpenWiki and wiki memory reinforce maintained codebase documentation as an agent context layer.`

### wiki/history/state-of/agents.md (updated)

Appends:

```

## Archived from current page on 2026-10-14

- [2026-07-02] OpenWiki and wiki memory reinforce maintained codebase documentation as an agent context layer.
```

### wiki/state-of/computer-use.md (updated)

Frontmatter: append `expand-fetch-launch-2026-10` to `sources:`; `as_of: 2026-10-14`.

New section, inserted after `### Agent-readable web infrastructure` (before `## Recent changes`):

```
### Agent web data extraction

The reader side of the agent-readable web: APIs that fetch and clean arbitrary pages for agents.

- [Expand Fetch](../tools/expand-fetch.md) — renders the page like a browser, keeps tables and icons as Markdown, extracts hidden JSON, and snapshots every fetch for citation *(as of 2026-10-14)*
```

Recent changes — adds one entry at the top:

```
- [2026-10-14] Added `Agent web data extraction` with [Expand Fetch](../tools/expand-fetch.md), the reader-side counterpart to sites serving agent-native Markdown.
```

Spills the oldest entry (the `[2026-05-01] Added Codex under Computer use…` line).

Sources — appends:

```
- [Announcing Expand Fetch](../sources/articles/expand-fetch-launch-2026-10.md)
```

### wiki/history/state-of/computer-use.md (updated)

Appends:

```

## Archived from current page on 2026-10-14

- [2026-05-01] Added [Codex](../../tools/codex.md) under `Computer use` as a horizontal computer-work contender; secondary newsletter coverage frames it as targeting docs, sheets, slides, browser flows, and connected workplace apps
```

### wiki/concepts/agent-readable-web.md (updated)

Frontmatter: append `expand-fetch-launch-2026-10` to `sources:`; `as_of: 2026-10-14`.

Current status — appends one bullet:

```
- The reader side is maturing in parallel: fetch APIs such as [Expand Fetch](../tools/expand-fetch.md) clean arbitrary pages for agents because most sites still serve only human HTML; Expand argues lossy conversion (dropped icons, broken tables, missing page JSON) makes agents confidently wrong.
```

Recent changes — adds one entry at the top:

```
- [2026-10-14] Expand Fetch launch adds the reader-side view: trained page-to-Markdown and hidden-JSON models for sites that don't serve agent-native formats.
```

Sources — appends:

```
- [Announcing Expand Fetch](../sources/articles/expand-fetch-launch-2026-10.md)
```

### wiki/index.md (updated)

Under `## Tools`, in alphabetical position:

```
- [tools/expand-fetch](tools/expand-fetch.md) — Expand's agent web-fetch API: trained Markdown (Iris) and hidden-JSON (X-Ray) models, citable snapshots, Highlights, Crawl, WebSync *(as_of: 2026-10-14)*
```

Update `as_of` on the `state-of/agents`, `state-of/computer-use` and `concepts/agent-readable-web` lines to `2026-10-14`. Page count: `- tools: 95` → `- tools: 96`.

### wiki/sources/articles/expand-fetch-launch-2026-10.md (new)

```
---
title: Announcing Expand Fetch
type: source
source_type: article
source_file: raw/articles/2026-10-14-expandai-blog-announcing-expand-fetch.md
url: https://expand.ai/blog/announcing-expand-fetch
ingested: 2026-10-14
domains: [agents, computer-use]
---

# Announcing Expand Fetch

Expand's launch post for Expand Fetch, a web-fetch API for agents. It argues that Markdown converters drop icons, tables and page-loaded JSON, leaving agents confidently wrong, and introduces two trained models — Iris (sorts rendered DOM elements into preserve/prune/appendix) and X-Ray (extracts useful hidden JSON) — plus per-fetch snapshots, query-based Highlights, Crawl and WebSync. Benchmarks are vendor-run. No publication date on the page; ingest date used.

## Influenced pages
- [Expand Fetch](../../tools/expand-fetch.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new Agent web data extraction section
- [State of Computer Use](../../state-of/computer-use.md) — new Agent web data extraction section
- [Agent-readable web](../../concepts/agent-readable-web.md) — reader-side counterpart bullet

## Key claims extracted
- Iris: preserve / prune / appendix classification on the rendered page; 93.9% precision, 91.7% recall, 92.7% F1 vs Jev 75.7% / 66.5% / 69.6% on Expand's validation set; ~500K tokens/sec
- X-Ray: extracts question-relevant data from page-loaded JSON (e.g. 17,374 tokens on Linear's pricing page)
- MDBench Hard v1 (private, 1,094 questions, 326 pages, Claude Sonnet 5.5 answering): Expand 74.1%, Exa 55.3%, Firecrawl 27.2%
- Highlights: >95% token savings by returning query-matched passages
- Every fetch saved as a citable snapshot with line-level provenance
- Crawl (1 credit/page) and WebSync (continuous change streaming)
- $1 per 1,000 fetches; engineers at OpenAI and Amazon Science named as users
```

## Schema / vocabulary additions
- [ ] Add new subcategory `web-data-extraction` to `wiki/_schema/subcategories.md` (and its declared-slugs line):
    ```
    ### web-data-extraction
    - **Parent domain(s):** agents, computer-use
    - **Applies to types:** tool
    - **Definition:** APIs and services that fetch, render, clean, and extract web pages or whole sites into agent-usable formats (Markdown, structured data, snapshots), including crawling and change tracking. Distinct from `computer-use` (operating UIs) and `document-intelligence` (PDFs, forms, files).
    - **Examples:** [Expand Fetch](../tools/expand-fetch.md)
    ```

## Open questions
- Exa and Firecrawl appear only as benchmark competitors here. Should they get tool pages under the new subcategory when a primary source about them comes in? (Assumed: not from this source.)
	- Right now, no new page for them.
