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
