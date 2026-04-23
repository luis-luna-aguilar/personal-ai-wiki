---
title: Deep Research
type: tool
domains: [agents]
subcategory: deep-research-tool
tags: [openai, google, closed-source, agentic]
as_of: 2026-04-22
sources: [openai-deep-research, gemini-deep-research-max, legacy-ai-tools-roadmap-xlsx]
---

# Deep Research

Deep Research is the emerging product category for longer-horizon research agents that plan, search, read, gather sources, and synthesize outputs over many steps instead of answering in a single pass. Both OpenAI and Google now ship productized versions, which is enough to treat Deep Research as its own tool space rather than a buried assistant feature.

## Current status (as of 2026-04-22)

- OpenAI and Google both ship productized versions; the category is no longer a preview feature buried inside an assistant
- Product shape is converging on: planning phase → web browsing → source synthesis → asynchronous or extended research runs
- Gemini's variant is the most fully specified publicly: 93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE on the Max tier
- Gemini Deep Research Max capabilities: MCP support (arbitrary MCP servers for internal data), multimodal inputs (PDF, CSV, image, audio, video), code execution, collaborative planning (user can adjust the research plan mid-run), real-time progress streaming, native charts and infographics generated inline in analytical reports
- Both OpenAI and Google offer API access to their Deep Research variants; Gemini's is built on Gemini 3.1 Pro

## Why it matters

- Distinct workflow class, not just "chat with search" — the planning and iteration loop is the product
- Becoming a practical bridge between assistants and more autonomous knowledge-work agents
- MCP integration (Gemini) means Deep Research can reach internal data sources, not just the public web

## Sources

- [[sources/articles/openai-deep-research]]
- [[sources/articles/gemini-deep-research-max]]
- [[sources/notes/legacy-ai-tools-roadmap-xlsx]]

