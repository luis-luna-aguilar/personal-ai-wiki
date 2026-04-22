---
type: proposal
source: raw/newsletters/2026-04-22-ainews-openai-launches-gpt-image-2.md
status: pending
created: 2026-04-22
---

# Proposal: Gemini Deep Research Max — benchmark scores + state-of/agents update

## Summary

AINews provided benchmark scores and workflow details for Google Deep Research Max that weren't in the original launch source already ingested (gemini-deep-research-max.md). New details: 93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE for the Max variant; collaborative planning (user can adjust research plan mid-run); real-time progress streaming; code execution. AINews framing: overnight due-diligence / analyst report generation is now a standard productized use case; MCP-backed internal data access makes proprietary corpora first-class.

## Intended changes

- [ ] **Update** `wiki/tools/gemini.md` — add benchmark scores and two missing capability details to Current status
    > **Replace in `## Current status (as of 2026-04-21)`:**
    > ```
    > Before:
    > - Deep Research and Deep Research Max launched in paid public preview via the Gemini API
    > - Built on Gemini 3.1 Pro for long-horizon research workflows across web and custom sources
    > - MCP support, file-store connectivity, multimodal grounding, and optional web-off mode for custom-data-only research
    > - Native charts and infographics generated inline inside analytical reports
    >
    > After:
    > - Deep Research and Deep Research Max launched in paid public preview via the Gemini API
    > - Built on Gemini 3.1 Pro for long-horizon research workflows across web and custom sources
    > - Benchmark scores (Max variant): 93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE
    > - Capabilities: MCP support (arbitrary MCP servers for internal data), multimodal inputs (PDF, CSV, image, audio, video), code execution, collaborative planning (user can adjust the research plan mid-run), real-time progress streaming
    > - Native charts and infographics generated inline inside analytical reports
    > ```
    > **Update `as_of` to `2026-04-22`** and add `ainews-2026-04-22` to `sources` frontmatter.
    >
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Added benchmark scores for Deep Research Max (93.3% DeepSearchQA, 85.9% BrowseComp, 54.6% HLE); added collaborative planning and code execution capabilities from AINews coverage
    > ```

- [ ] **Update** `wiki/state-of/agents.md` — note research agents as an emerging subcategory signal
    > **Append to `## Recent changes`:**
    > ```
    > - [2026-04-22] Google Deep Research Max scores (93.3% DeepSearchQA) and HF ml-intern autonomous loop mark the emergence of a distinct "full-stack research agent" tier — see [[tools/gemini]] and [[tools/hf-ml-intern]]
    > ```
