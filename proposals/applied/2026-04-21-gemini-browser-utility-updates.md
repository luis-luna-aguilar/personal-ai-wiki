---
type: proposal
sources:
  - raw/newsletters/2026-04-15-chrome-gets-new-ai-powers.md
  - raw/newsletters/2026-04-16-shoemaker-company-pivots-to-ai.md
  - raw/newsletters/2026-04-16-gemini-gets-a-mac-app.md
status: pending
created: 2026-04-21
---

# Proposal: Gemini browser and utility updates

## Summary

This is the one lightweight ingest from the weekly batch. Google shipped a set of practical product updates rather than a category-defining leap: Chrome Skills for reusable browser-side Gemini workflows, Gemini 3.1 Flash TTS for promptable speech output, and a native Gemini Mac app. These belong on the Gemini tool page as incremental product-shape updates.

## Intended changes

- [x] **Update** `wiki/tools/gemini.md` — expand the page from a thin stub into a more current product summary
  > See snippet below.

- [x] **Update** `wiki/index.md` — refresh the Gemini line
  > Replace:
  > `- [[tools/gemini]] — Google's AI chatbot; custom visualizations, notebooks, Google ecosystem integration *(as_of: 2026-04-10)*`
  >
  > With:
  > `- [[tools/gemini]] — Google's AI assistant; custom visualizations, notebooks, Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app *(as_of: 2026-04-21)*`

- [x] **Create** `wiki/sources/newsletters/gemini-browser-utility-updates.md` — source summary

## Page drafts

### wiki/tools/gemini.md (updated snippet)

```md
---
title: Gemini
type: tool
domains: [models]
subcategory: ai-assistant
tags: [google, closed-source]
as_of: 2026-04-21
sources: [gemini-browser-utility-updates]
---

# Gemini

Google's AI assistant product, built on the Gemini model family. Combines conversational AI, search, productivity features, and increasingly lightweight workflow utilities across browser, desktop, and media-generation surfaces.

## Current status (as of 2026-04-21)

- Custom interactive visualizations in chat
- Notebooks for grouped chats, file uploads, and persistent instructions
- Chrome Skills: reusable Gemini prompts that run as one-click browser workflows
- Gemini 3.1 Flash TTS: promptable text-to-speech with controllable tone, pace, and delivery
- Native Gemini Mac app

## Strengths

- Deep Google ecosystem integration
- Product cadence increasingly focused on practical utility surfaces, not just chat quality

## Recent changes

- [2026-04-21] Added Chrome Skills, Gemini 3.1 Flash TTS, and native Mac app
- [2026-04-10] Custom visualizations and notebooks features announced; rolling out to paid accounts
```

### wiki/sources/newsletters/gemini-browser-utility-updates.md (new)

```md
---
title: Gemini browser and utility updates
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-15-chrome-gets-new-ai-powers.md
ingested: 2026-04-21
domains: [models]
---

# Gemini browser and utility updates

Newsletter-derived summary of three related Google product updates: Chrome Skills for reusable Gemini browser workflows, Gemini 3.1 Flash TTS for promptable speech output, and a native Gemini Mac app.

## Key claims extracted

- Chrome Skills turns saved prompts into one-click browser workflows
- Gemini 3.1 Flash TTS supports natural-language control over tone, pace, and delivery
- Google shipped a native Gemini app for macOS
```
