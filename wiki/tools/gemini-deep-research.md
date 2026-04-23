---
title: Gemini Deep Research
type: tool
domains: [agents]
subcategory: deep-research-tool
tags: [google, closed-source, agentic]
as_of: 2026-04-22
sources: [gemini-deep-research-max, ainews-2026-04-22]
---

# Gemini Deep Research

Google's deep research agent, available in two tiers: Deep Research (standard) and Deep Research Max. The Max tier is the most fully benchmarked publicly available deep research implementation as of April 2026. Runs on [[tools/gemini]] (Gemini 3.1 Pro on the Max tier).

## Current status (as of 2026-04-22)

**Deep Research Max benchmarks:**
- DeepSearchQA: 93.3%
- BrowseComp: 85.9%
- HLE (Humanity's Last Exam): 54.6%

**Distinctive capabilities (Max tier):**
- MCP support — connect arbitrary MCP servers so the research loop can reach internal data, not just the public web
- Multimodal inputs — PDF, CSV, image, audio, video accepted as context
- Code execution — runs code during the research loop for quantitative analysis
- Collaborative planning — user can adjust the research plan mid-run, not only after output
- Real-time progress streaming — see intermediate findings as they emerge
- Native chart and infographic generation inline in the research report

## Why it matters

Gemini Deep Research Max is currently the most benchmarked and feature-rich public deep research implementation. The MCP integration in particular extends the category from "public web research" to "internal knowledge research," which meaningfully broadens enterprise applicability.

See [[concepts/deep-research]] for the category concept and [[tools/openai-deep-research]] for OpenAI's implementation.

## Recent changes

- [2026-04-22] Added Deep Research Max benchmark scores and feature set from AINews coverage

## Sources

- [[sources/articles/gemini-deep-research-max]]
- [[sources/newsletters/ainews-2026-04-22]]
