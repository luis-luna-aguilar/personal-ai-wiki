---
title: State of Models
type: state-of
domains: [models]
tags: []
as_of: 2026-04-21
sources: [muse-spark, kimi-k2-6-blog, ainews-2026-04-21]
---

# State of Models

Current state of foundation models — frontier and otherwise. Organized by subcategory. A subcategory can have multiple leaders.

## Subcategories

### Frontier multimodal models

General-purpose frontier models competing on broad multimodal capability rather than narrow specialization.

- [[models/claude-opus-4-7]] — Anthropic; #1 Vision & Document Arena (April 2026); +4 over Opus 4.6 in Document Arena; wins in diagram, homework, and OCR *(as of 2026-04-21)*
- [[models/muse-spark]] — Meta's new multimodal model; the captured launch source emphasizes scaling efficiency and claims Llama 4 Maverick-level capability with over an order of magnitude less training compute *(as of 2026-04-10)*

### Coding models

Open-weight and frontier models evaluated primarily for agentic coding tasks.

- [[models/kimi-k2-6]] — Moonshot AI; open-weight 1T-param MoE; open-source SOTA claims: HLE w/ tools 54.0, SWE-Bench Pro 58.6, SWE-bench Multilingual 76.7, BrowseComp 83.2; 4K+ tool calls, 12+ hour continuous runs *(as of 2026-04-21)*

## Recent changes

- [2026-04-21] Anthropic/AWS: 5 GW compute secured, $5B investment, up to $20B more — see [[trends/compute-infrastructure]]
- [2026-04-21] Added [[models/claude-opus-4-7]] — #1 Vision & Document Arena
- [2026-04-21] Added [[models/kimi-k2-6]] under new `Coding models` subcategory
- [2026-04-10] Added `frontier-multimodal-model` subcategory with [[models/muse-spark]]
- [2026-04-10] Gemini adds custom interactive visualizations in chat and notebooks (dedicated workspaces with grouped chats, file uploads, instructions); rolling out to paid accounts first
