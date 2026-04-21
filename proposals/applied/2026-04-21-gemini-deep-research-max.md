---
type: proposal
source: raw/articles/2026-04-21-bloggoogle-innovation-and-ai-models-and-research-gemini-mode.md
status: pending
created: 2026-04-21
---

# Proposal: Gemini Deep Research and Deep Research Max

## Summary

Google announced two new Gemini API research agents on April 21, 2026: `Deep Research`, positioned as the faster lower-latency successor to the December preview, and `Deep Research Max`, positioned as the highest-quality asynchronous/background option. The launch materially expands Gemini's current product picture in this wiki from browser and utility features into long-horizon research workflows with MCP support, multimodal grounding, native charts/infographics, and paid public-preview API availability.

## Intended changes

- [x] **Update** `wiki/tools/gemini.md` — add Deep Research / Deep Research Max to Gemini's current status and recent changes
  > Relevant snippet:
  > ```md
  > ---
  > title: Gemini
  > type: tool
  > domains: [models]
  > subcategory: ai-assistant
  > tags: [google, closed-source]
  > as_of: 2026-04-21
  > sources: [gemini-browser-utility-updates, gemini-deep-research-max]
  > ---
  > 
  > # Gemini
  > 
  > Google's AI assistant product, built on the Gemini model family. Combines conversational AI, search, productivity features, and increasingly agentic research and workflow utilities across browser, desktop, API, and media-generation surfaces.
  > 
  > ## Current status (as of 2026-04-21)
  > 
  > - Deep Research and Deep Research Max launched in paid public preview via the Gemini API
  > - Built on Gemini 3.1 Pro for long-horizon research workflows across web and custom sources
  > - MCP support, file-store connectivity, multimodal grounding, and optional web-off mode for custom-data-only research
  > - Native charts and infographics generated inline inside analytical reports
  > - Chrome Skills: reusable Gemini prompts that run as one-click browser workflows
  > - Native Gemini Mac app
  > 
  > ## Strengths
  > 
  > - Deep Google ecosystem integration
  > - Product cadence now spans both lightweight utility features and heavier autonomous research workflows
  > 
  > ## Weaknesses / caveats
  > 
  > - Thin source coverage in this wiki relative to ChatGPT and Claude
  > - Deep Research Max benchmark and quality claims here come from Google's own launch post
  > - Current page still mixes consumer assistant features with developer/API capabilities because source coverage is not yet deep enough to justify a split page
  > 
  > ## Recent changes
  > 
  > - [2026-04-21] Added Deep Research and Deep Research Max: Gemini API public preview, MCP support, multimodal grounding, and native visual reports
  > - [2026-04-21] Added Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app
  > - [2026-04-10] Custom visualizations and notebooks features announced; rolling out to paid accounts
  > 
  > ## Sources
  > 
  > - [[sources/newsletters/gemini-browser-utility-updates]]
  > - [[sources/articles/gemini-deep-research-max]]
  > ```

- [x] **Create** `wiki/sources/articles/gemini-deep-research-max.md` — source summary for the Google launch post
  > See full draft below.

## Page drafts

### wiki/sources/articles/gemini-deep-research-max.md (new)

```md
---
title: Gemini Deep Research and Deep Research Max launch
type: source
source_type: article
source_file: raw/articles/2026-04-21-bloggoogle-innovation-and-ai-models-and-research-gemini-mode.md
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/
published: 2026-04-21
ingested: 2026-04-21
domains: [models, agents]
---

# Gemini Deep Research and Deep Research Max launch

Google introduces two upgraded Gemini API research agents built on Gemini 3.1 Pro. `Deep Research` is positioned as the faster interactive/default option, while `Deep Research Max` uses more test-time compute for slower but more comprehensive background research. The post frames Gemini's Deep Research stack less as a summarizer and more as an autonomous research layer for enterprise and developer workflows that combine open-web retrieval with proprietary data sources.

## Influenced pages

- [[tools/gemini]] — expands the page from browser/productivity utilities into API-level autonomous research capabilities

## Key claims extracted

- Published April 21, 2026
- Deep Research and Deep Research Max are available in paid public preview via the Gemini API
- Both are built with Gemini 3.1 Pro
- Deep Research replaces the December preview release with lower latency, lower cost, and higher quality
- Deep Research Max uses extended test-time compute for more comprehensive asynchronous/background research workflows
- The agent can search the web, remote MCP servers, file uploads, and connected file stores in combination or selectively
- MCP support is explicitly positioned as the bridge to proprietary and specialized data providers
- Reports can include native charts and infographics, not just text
- Inputs can include PDFs, CSVs, images, audio, and video for multimodal grounding
- The launch post claims improved factuality, more source diversity, and better handling of conflicting evidence versus the December release
```

## Open questions

- None for this pass. If more Gemini API sources accumulate, it may become worth splitting developer-facing agent capabilities into a separate page instead of keeping them on `wiki/tools/gemini.md`.
