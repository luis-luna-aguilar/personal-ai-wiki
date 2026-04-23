---
name: wiki-research-request
description: Build detailed deep-research request documents from weak or missing topics in this Obsidian AI Wiki. Use when the user identifies a wiki content gap, wants to improve coverage before ingesting new sources, asks for a research brief/request/prompt based on current wiki contents, or wants to turn scattered wiki notes into a targeted research agenda for later deep research and ingestion.
---
# Wiki Research Request

## Overview

Use this skill to turn "the wiki is missing or weak on X" into a precise research request that another deep-research agent can execute. The output should explain what the wiki already knows, what is missing, what questions to answer, what source types to prioritize, and how the eventual findings should map back into the wiki.

## Workflow

1. Read `LLM-INSTRUCTIONS.md` first and follow the wiki rules.
2. Read `wiki/index.md` before any broader search.
3. Identify candidate pages from the index, then inspect only the relevant pages. Do not read `wiki/history/` unless the user explicitly asks.
4. Search the relevant wiki sections with `rg` for the user's topic and adjacent terms.
5. Build a gap map: what the wiki already says, what is thin or missing, what contradictions or open questions exist, and which future wiki pages would likely change.
6. Write a research request document, normally under `research-requests/YYYY-MM-DD-topic.md` unless the user specifies another path.
7. Do not ingest findings into `wiki/` during this step. This skill creates the request that will drive later research and ingestion.

## Research Request Shape

Use `references/research-request-template.md` as the starting structure. Adapt section names when useful, but keep these core elements:

- **Purpose:** The reason this research matters to the wiki and the user.
- **Current wiki baseline:** Concise synthesis of existing coverage with links to relevant wiki pages.
- **Known gaps:** Specific missing information, not generic "needs more research."
- **Research questions:** Actionable questions a deep-research agent can answer.
- **Source priorities:** Which sources to seek first, such as vendor docs, engineering blogs, academic papers, benchmark reports, practitioner case studies, talks, podcasts, or public repos.
- **Desired outputs:** The pages, concepts, training guidance, benchmarks, or proposals the later ingest should be able to create or update.
- **Exclusions:** What the research should not spend time on.
- **Ingestion notes:** Candidate wiki destinations and schema implications. If a new tag/domain/subcategory may be needed, call it out as a future proposal, not as an already-approved change.

## Quality Bar

- Make the request detailed enough that a separate researcher can run with it without this conversation.
- Tie gaps to actual wiki content. Avoid saying the wiki lacks something unless you checked relevant pages.
- Prefer operational questions over abstract surveys. The wiki is for tools, workflows, concepts, trends, and training guidance.
- Ask for patterns, examples, failure modes, metrics, and implementation recipes, not only definitions.
- Keep the research request source-seeking, not conclusion-heavy. It should define what to investigate, not pretend the research has already been done.

