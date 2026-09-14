---
title: Knowledge layer
type: concept
domains: [agents]
tags: [agentic, knowledge-cluster]
as_of: 2026-08-20
sources: [knowledge-layer-architecture, llm-wikis-paperwiki-2026-07-06, ainews-not-much-happened-2026-07-02, agent-memory-systems-layer-2026-06, karpathy-llm-wiki-gist, rvaniaaaa-second-brain-compiler-2026-08-20]
---

# Knowledge layer

A knowledge layer is a compiled, maintained context surface that sits between raw source material and the agents acting on it. Instead of forcing an agent to re-derive context from raw files at query time, the system continuously turns sources into structured wiki pages, indexes, entity pages, and syntheses that the agent can read directly. In the [Knowledge architectures](knowledge-architectures.md) matrix it is the personal- or team-scope store of *compiled documents*: an agent compiles, a human curates the schema and reviews.

## Also called

LLM wiki (Karpathy's name for the pattern), second brain (personal scope), PaperWiki (a research instance), wiki memory, maintained context surface. Not the same as a product's "knowledge base" feature, which is a document store rather than a compiled layer.

## Current status (as of 2026-08-20)

- Framed as an answer to why agents often feel generic: they start from thin or unstructured context
- Contrasted with naive RAG: compile once, cross-reference, and maintain over time rather than repeatedly searching raw chunks
- Often paired with a separate human-maintained rules layer for voice, preferences, constraints, and operating rules
- Becomes more useful as outputs, queries, and new sources compound back into the same system
- Practitioner examples now frame this as "LLM Wikis": maintained markdown knowledge layers for agents, often implemented as Obsidian vaults with rich metadata, full-text + semantic search, and generated HTML artifacts that research agents can navigate directly
- Wiki-style memory is moving from personal agent folders into explicit tooling: LangChain's [OpenWiki](../tools/openwiki.md) generates and maintains codebase docs meant for agents to consume.
- Maintained memory is distinct from retrieval-only memory. Engram/Context Hub-style systems point toward extracting candidate memories, reconciling them against existing knowledge, and committing cleaned facts before query time rather than retrieving every plausible old fragment.
- The common design direction is inspectable, editable, permission-aware knowledge that agents can share across sessions instead of hidden vector recall or one giant transcript.

## Why it matters

The core claim is not just retrieval quality. A maintained knowledge layer changes the agent's starting point from "guess from whatever I can find right now" to "act from a curated, versioned memory of this domain." That makes agent behavior more cumulative, more inspectable, and easier to improve over time.

## LLM Wiki implementation pattern

The pattern traces back to Andrej Karpathy's April 2026 "LLM Wiki" gist — a viral idea file describing exactly this architecture in his own terms, meant to be pasted directly to an LLM agent as a starting brief. Three layers: raw sources (immutable — the LLM reads but never modifies them), the wiki (a directory of LLM-owned markdown — summaries, entity pages, concept pages, an overview — that the human reads and the LLM writes and maintains), and the schema (a CLAUDE.md/AGENTS.md-style document defining structure and workflows, co-evolved by the user and the LLM over time). Three operations run on top: **Ingest** (read a new source, discuss takeaways, update relevant pages and the index, append to the log — a single source can touch 10-15 pages), **Query** (search the wiki and synthesize a cited answer — and file good answers back into the wiki as new pages, so explorations compound the same way ingested sources do), and **Lint** (periodically check for contradictions, stale claims, orphan pages, and missing cross-references). Karpathy distinguishes `index.md` (content-oriented — a catalog read first when answering a query, sufficient up to roughly 100 sources without embedding-based search infrastructure) from `log.md` (chronological, append-only, grep-able if entries share a consistent line prefix), and recommends `qmd` — a local hybrid BM25/vector markdown search tool — once scale outgrows the index file alone. He frames the pattern as a realized version of Vannevar Bush's 1945 Memex: a personal, curated, associatively-linked knowledge store, with the one problem Bush never solved — who does the maintenance — now handled by the LLM.

Omar Sar's PaperWiki example (July 2026) makes the same pattern concrete for research agents. Papers are curated into an Obsidian vault, indexed with `qmd`, exposed through an HTML artifact, and searched through both full-text and semantic search. Daily automations keep the wiki updated, while human-in-the-loop curation filters signal from social-media and aggregator noise. The useful design point is that agents "love markdown files": structured pages with metadata are easier for agents to navigate than raw paper lists, social feeds, or opaque vector chunks. Frontier models are not required for every step; Omar reports using a mix of Claude Opus 4.8 and DeepSeek V4 Flash, with future work on specialized models trained over the wiki.

A practitioner elaboration (@rvaniaaaa, August 2026) builds the same pattern specifically around Claude Desktop under the name "second brain" (a personal-scope alias for this page's concept), framing the choice as "storage vs. compiler" — a library only answers when searched, while a compiler reads each new source, connects it to everything already there, flags contradictions, and files the synthesis permanently, so the next source builds on processed understanding rather than raw inputs. It packages four starter prompts (ingesting a source, an interview-style prompt for building the user's CLAUDE.md, project-folder scaffolding, and a daily compilation loop that writes a change-brief) and claims the value of compilation — the model finding non-obvious links — only becomes visible around 50-100 well-compiled sources, with a good search engine doing much the same job below that density; it also notes the scheduled-task/file-access loop this depends on requires a paid Claude Desktop plan. Treat this source's practical additions on their own terms: it attributes at least two direct quotes to Karpathy that do not appear, verbatim or in close paraphrase, in his actual gist — those specific phrasings should be read as this author's own framing, not Karpathy's.

## Related

- [Knowledge architectures](knowledge-architectures.md) — the hub that places this page against agent memory, company brains, and ontologies
- [Agent memory](agent-memory.md) — a different store: what one agent learned from its own sessions, managed as a lifecycle. A knowledge layer is the shared, human-legible compiled corpus; the two usually coexist
- [Company brain](company-brain.md) — the organization-scope system a team's knowledge layer typically sits inside
- [Ontologies as agent guardrails](ontology-agent-guardrails.md) — a formal rule layer for validation and constraint, as opposed to compiled content for reading

## Recent changes

- [2026-09-09] Terminology reorganization: added the `## Also called` alias line, corrected the Current-status stamp to match the page date, and rewrote the Related lines to agree with the new [Knowledge architectures](knowledge-architectures.md) hub.
- [2026-08-20] Restructured the LLM Wiki section to lead with Karpathy's own original gist (the pattern's primary source, previously uncited here) rather than only the secondary PaperWiki example, and added a practitioner elaboration (@rvaniaaaa) built around Claude Desktop — with an explicit caveat that the elaboration misattributes two quotes to Karpathy.
- [2026-07-07] Agent-memory systems coverage reinforces that knowledge layers should reconcile and maintain facts rather than retrieve every plausible old fragment.
- [2026-07-02] OpenWiki and Engram-style memory reconciliation reinforced the shift from raw logs/retrieval toward maintained, agent-readable knowledge layers.

## Caveats

- The strongest current source is a practitioner essay, not an academic benchmark or vendor-neutral comparison
- The idea overlaps with context engineering, RAG, memory systems, and personal-knowledge-base workflows; the [Knowledge architectures](knowledge-architectures.md) hub records where the wiki draws each boundary

## Sources

- [AI Knowledge Layer](../sources/articles/knowledge-layer-architecture.md)
- [LLM Wikis / PaperWiki — Omar Sar](../sources/tweets/llm-wikis-paperwiki-2026-07-06.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
- [LLM Wiki (gist) — Andrej Karpathy](../sources/articles/karpathy-llm-wiki-gist.md)
- [The Second Brain Is Not a Storage System. It's a Compiler.](../sources/tweets/rvaniaaaa-second-brain-compiler-2026-08-20.md)
