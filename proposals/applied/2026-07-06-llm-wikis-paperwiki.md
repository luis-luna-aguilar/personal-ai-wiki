---
type: proposal
source: raw/tweets/2026-07-06-omarsar0-2072735813469905026.md
status: pending
created: 2026-07-06
---

# Proposal: Augment knowledge layer with LLM Wikis / PaperWiki example

## Summary

Omar Sar / Elvis argues that "LLM Wikis" are an underused AI application: structured markdown knowledge bases maintained by agents and used as a compounding context layer for research workflows. This is not a new wiki concept; it is a concrete practitioner example of the existing [Knowledge layer](../wiki/concepts/knowledge-layer.md) pattern, with details that sharpen the current page: Obsidian vault, `qmd` indexing, HTML artifact, full-text plus semantic search, daily automation loops, and human-in-the-loop curation.

## Intended changes

- [x] **Update** `wiki/concepts/knowledge-layer.md` — augment the existing knowledge-layer concept with a practical LLM Wiki / PaperWiki example; update `as_of` and sources
    > **Update frontmatter:**
    > - `as_of: 2026-07-06`
    > - add `llm-wikis-paperwiki-2026-07-06` to `sources`
    >
    > **Add to `## Current status`:**
    > `- Practitioner examples now frame this as "LLM Wikis": maintained markdown knowledge layers for agents, often implemented as Obsidian vaults with rich metadata, full-text + semantic search, and generated HTML artifacts that research agents can navigate directly.`
    >
    > **Add after `## Why it matters`:**
    > ```md
    > ## LLM Wiki implementation pattern
    >
    > Omar Sar's PaperWiki example (July 2026) makes the existing knowledge-layer pattern concrete for research agents. Papers are curated into an Obsidian vault, indexed with `qmd`, exposed through an HTML artifact, and searched through both full-text and semantic search. Daily automations keep the wiki updated, while human-in-the-loop curation filters signal from social-media and aggregator noise.
    >
    > The useful design point is that agents "love markdown files": structured pages with metadata are easier for agents to navigate than raw paper lists, social feeds, or opaque vector chunks. The wiki becomes a compounding intelligence stack — new papers, prior notes, research-agent outputs, and verifier feedback all feed back into the same maintained substrate.
    >
    > For research workflows, this suggests a practical pattern: use agents to maintain the corpus, but keep the corpus legible to humans and file-native for other agents. Frontier models are not required for every step; Omar reports using a mix of Claude Opus 4.8 and DeepSeek V4 Flash, with future work on specialized models trained over the wiki.
    > ```
    >
    > **Add to Sources:**
    > `- [LLM Wikis / PaperWiki — Omar Sar](../sources/tweets/llm-wikis-paperwiki-2026-07-06.md)`

- [x] **Create** `wiki/sources/tweets/llm-wikis-paperwiki-2026-07-06.md` — required source summary for the ingested tweet; this is not a new content/concept page
    > See draft below.

## Page drafts

### wiki/sources/tweets/llm-wikis-paperwiki-2026-07-06.md (new)

````md
---
title: LLM Wikis / PaperWiki — Omar Sar
type: source
source_type: tweet
source_file: raw/tweets/2026-07-06-omarsar0-2072735813469905026.md
url: https://x.com/omarsar0/status/2072735813469905026
ingested: 2026-07-06
domains: [agents]
---

# LLM Wikis / PaperWiki — Omar Sar

Omar Sar / Elvis describes "LLM Wikis" as structured, agent-maintained knowledge bases for research workflows. His PaperWiki example uses Obsidian as the vault, `qmd` indexing, an HTML artifact, full-text and semantic search, and daily automation loops to keep curated paper knowledge accessible to research agents.

## Influenced pages

- [Knowledge layer](../../concepts/knowledge-layer.md) — adds LLM Wiki / PaperWiki as a practical implementation pattern

## Key claims extracted

- LLM Wikis are a high-value AI application because they intentionally build and scale a personal or team intelligence stack
- PaperWiki stores entries in an Obsidian vault, indexes with `qmd`, and presents the content through an HTML artifact
- Agents maintain the wiki in daily loops, with human-in-the-loop curation for source selection
- Full-text search plus semantic search makes the wiki accessible to both humans and agents
- Markdown files with rich metadata are easier for agents to navigate than raw feeds or paper aggregators
- The wiki helps reduce noise and identify higher-quality papers for research workflows
- Frontier models are not required for every maintenance step; Omar reports using Claude Opus 4.8 plus DeepSeek V4 Flash
- Future direction: train specialized models on top of the wiki so research agents can more quickly understand cutting-edge ideas and form research strategies
````

## Open questions

- None. This should stay on `concepts/knowledge-layer.md` for now; do not create a separate `workflows/llm-wiki.md` page from this single tweet.
	- Yes, keep it there.
