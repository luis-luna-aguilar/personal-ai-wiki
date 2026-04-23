---
title: Deep Research (concept)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-04-22
sources: [openai-deep-research, gemini-deep-research-max, legacy-ai-tools-roadmap-xlsx]
---

# Deep Research (concept)

Deep Research is a class of longer-horizon research agents that plan, search, read, synthesize, and iterate across many sources to produce structured research outputs — rather than answering in a single pass. Both OpenAI and Google now ship productized versions, making this a distinct product category rather than a buried assistant feature.

## What it is

The core workflow:
1. **Planning phase** — the agent breaks the research question into sub-questions or a search plan
2. **Web browsing / source gathering** — iterative search and page reading across many sources
3. **Synthesis** — compiling, structuring, and cross-referencing findings
4. **Output** — a long-form, cited research report, often with charts, tables, or structured data

The key distinction from "chat with search": the agent controls the search loop, not the user. It decides what to look for next, how many passes to take, and when it has enough.

## Why it matters

- Represents a practical bridge between chat assistants and fully autonomous agents
- MCP integration (Gemini) means the research loop can reach internal data sources, not just the public web
- Long-horizon research quality depends heavily on the planning loop, not just retrieval quality
- Becoming a standard feature at most frontier labs

## Current implementations

- [[tools/openai-deep-research]] — OpenAI's productized version; available via ChatGPT and API
- [[tools/gemini-deep-research]] — Gemini Deep Research and Deep Research Max; the most fully benchmarked public variant (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE on Max tier)

## Caveats

- Quality claims are mostly vendor-reported from launch posts
- Planning quality varies significantly across implementations
- "Deep research" as a brand is used loosely across the industry

## Sources

- [[sources/articles/openai-deep-research]]
- [[sources/articles/gemini-deep-research-max]]
- [[sources/notes/legacy-ai-tools-roadmap-xlsx]]
