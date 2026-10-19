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
