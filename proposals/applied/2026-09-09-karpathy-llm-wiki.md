---
type: proposal
source: raw/articles/2026-09-09-gistgithubcom-karpathy-442a6bf555914893e9891c11519de94f.md
status: pending
created: 2026-09-09
---

# Proposal: Karpathy's original "LLM Wiki" gist + a practitioner elaboration ("The Second Brain Is Not a Storage System")

## Summary

### The source

In April 2026, Andrej Karpathy posted a viral tweet about using LLMs to build personal knowledge bases, then followed up with a GitHub gist — an "idea file" meant to be pasted directly to an LLM agent — describing the pattern in full: "LLM Wiki." The gist has since collected 5,000+ stars and a large comment thread of independent implementations. Its architecture has three layers: raw sources (immutable — articles, papers, images, data files the LLM reads but never modifies), the wiki (a directory of LLM-generated markdown — summaries, entity pages, concept pages, an overview — that the LLM owns entirely and the human reads), and the schema (a CLAUDE.md- or AGENTS.md-style document telling the LLM how the wiki is structured and what workflows to follow, co-evolved by the user and the LLM over time). Three operations run on top: Ingest (read a new source, discuss takeaways, update relevant pages and the index, append to the log — a single source can touch 10-15 pages), Query (search the wiki, synthesize an answer with citations, in whatever output form fits — and importantly, file good answers back into the wiki as new pages so explorations compound too), and Lint (periodically check for contradictions, staleness, orphan pages, and missing cross-references). Karpathy calls index.md content-oriented (a catalog, read first when answering a query, sufficient up to roughly 100 sources without embedding-based search) and log.md chronological (append-only, grep-able if entries share a consistent prefix), and recommends `qmd` — a local hybrid BM25/vector markdown search tool — once scale outgrows the index alone. He frames the idea as a modern answer to Vannevar Bush's 1945 Memex: a personal, curated, associatively-linked knowledge store, with the one problem Bush never solved — who does the maintenance — now handled by the LLM. Separately, on August 20, 2026, a practitioner (@rvaniaaaa) posted an X Article elaborating the same pattern specifically around Claude Desktop's scheduled-tasks and file-access features, under the name "second brain": a "storage vs. compiler" framing, four copy-paste prompts (source ingestion, a CLAUDE.md-building interview, project-folder scaffolding, a daily compilation loop that files a change-brief), a claimed 50-100-source density threshold before compounding value becomes visible, and an explicit note that the scheduled-task loop needs a paid Claude Desktop plan. That post also attributes two "quotes" directly to Karpathy that do not actually appear in his gist — a sourcing issue flagged below, not repeated as fact.

### What changes

The wiki's Knowledge layer concept page already tracks this exact pattern under the heading "LLM Wiki implementation pattern," but has only ever cited a July 2026 secondary example (Omar Sar's PaperWiki) — never Karpathy's own original gist, the pattern's actual origin. Since the 9 September terminology reorganization, the page also carries an `## Also called` line that already lists "LLM wiki" and "second brain (personal scope)" as aliases, and the [Knowledge architectures](../wiki/concepts/knowledge-architectures.md) hub maps both terms to this page — so neither source introduces a new term; both land on the existing canonical page.

- **Knowledge layer** gets its "LLM Wiki implementation pattern" section restructured to lead with Karpathy's own original framing (the three-layer architecture, the three operations, the index/log distinction, the "file answers back into the wiki" principle, the Memex framing) in his own terms, keeping the existing PaperWiki paragraph as a concrete named implementation underneath it. A short, clearly-attributed closing paragraph adds rvaniaaaa's practical elaboration (the storage-vs-compiler framing, the four starter prompts, the density-threshold claim) with an explicit, un-buried caveat that this secondary source misattributes two quotes to Karpathy. One Recent-changes entry is added (the list has 3 entries, cap 10, no spill). Page date and the Current-status stamp move to 20 August (the newer of the two new sources).
- Two new source pages are created: one for Karpathy's gist, one for rvaniaaaa's elaboration.

### What to weigh

Karpathy's gist itself carries no visible byline date on the fetched page, but 2026-04-04 is corroborated by multiple independent mentions inside the raw content — including a secondary article quoting Karpathy's own dated follow-up tweet — so it's used here as a corroborated date, not a confirmed byline; flagged in the new source page rather than silently treated as certain. Separately, rvaniaaaa's misattributed Karpathy quotes are a genuine accuracy problem specific to that one secondary source — it doesn't affect Karpathy's own gist, and the wiki draft handles it with an explicit caveat rather than repeating the misattribution or dropping the source outright, since the rest of that post's content (the prompts, the density claim) is the author's own useful elaboration, not a record of Karpathy's words. This proposal was rewritten on 9 September against the reorganized Knowledge layer page; the drafts below assume that page as it now stands.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/knowledge-layer.md` — replace the LLM Wiki section to lead with Karpathy's original gist, add a caveated rvaniaaaa paragraph, add 1 Recent-changes entry (newest first; 3 entries live, no spill), bump `as_of` and the Current-status stamp to 2026-08-20, add both source ids
    > See draft below

- [ ] **Create** `wiki/sources/articles/karpathy-llm-wiki-gist.md` — source summary; no existing page covers this URL

- [ ] **Create** `wiki/sources/tweets/rvaniaaaa-second-brain-compiler-2026-08-20.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/concepts/knowledge-layer.md (updated)

Frontmatter: bump `as_of: 2026-07-06` → `as_of: 2026-08-20`; append `karpathy-llm-wiki-gist` and `rvaniaaaa-second-brain-compiler-2026-08-20` to `sources:`. Change the heading `## Current status (as of 2026-07-06)` → `## Current status (as of 2026-08-20)`. The `## Also called` line is unchanged: it already lists "LLM wiki" and "second brain (personal scope)".

Replace the `## LLM Wiki implementation pattern` section in full with:

```
## LLM Wiki implementation pattern

The pattern traces back to Andrej Karpathy's April 2026 "LLM Wiki" gist — a viral idea file describing exactly this architecture in his own terms, meant to be pasted directly to an LLM agent as a starting brief. Three layers: raw sources (immutable — the LLM reads but never modifies them), the wiki (a directory of LLM-owned markdown — summaries, entity pages, concept pages, an overview — that the human reads and the LLM writes and maintains), and the schema (a CLAUDE.md/AGENTS.md-style document defining structure and workflows, co-evolved by the user and the LLM over time). Three operations run on top: **Ingest** (read a new source, discuss takeaways, update relevant pages and the index, append to the log — a single source can touch 10-15 pages), **Query** (search the wiki and synthesize a cited answer — and file good answers back into the wiki as new pages, so explorations compound the same way ingested sources do), and **Lint** (periodically check for contradictions, stale claims, orphan pages, and missing cross-references). Karpathy distinguishes `index.md` (content-oriented — a catalog read first when answering a query, sufficient up to roughly 100 sources without embedding-based search infrastructure) from `log.md` (chronological, append-only, grep-able if entries share a consistent line prefix), and recommends `qmd` — a local hybrid BM25/vector markdown search tool — once scale outgrows the index file alone. He frames the pattern as a realized version of Vannevar Bush's 1945 Memex: a personal, curated, associatively-linked knowledge store, with the one problem Bush never solved — who does the maintenance — now handled by the LLM.

Omar Sar's PaperWiki example (July 2026) makes the same pattern concrete for research agents. Papers are curated into an Obsidian vault, indexed with `qmd`, exposed through an HTML artifact, and searched through both full-text and semantic search. Daily automations keep the wiki updated, while human-in-the-loop curation filters signal from social-media and aggregator noise. The useful design point is that agents "love markdown files": structured pages with metadata are easier for agents to navigate than raw paper lists, social feeds, or opaque vector chunks. Frontier models are not required for every step; Omar reports using a mix of Claude Opus 4.8 and DeepSeek V4 Flash, with future work on specialized models trained over the wiki.

A practitioner elaboration (@rvaniaaaa, August 2026) builds the same pattern specifically around Claude Desktop under the name "second brain" (a personal-scope alias for this page's concept), framing the choice as "storage vs. compiler" — a library only answers when searched, while a compiler reads each new source, connects it to everything already there, flags contradictions, and files the synthesis permanently, so the next source builds on processed understanding rather than raw inputs. It packages four starter prompts (ingesting a source, an interview-style prompt for building the user's CLAUDE.md, project-folder scaffolding, and a daily compilation loop that writes a change-brief) and claims the value of compilation — the model finding non-obvious links — only becomes visible around 50-100 well-compiled sources, with a good search engine doing much the same job below that density; it also notes the scheduled-task/file-access loop this depends on requires a paid Claude Desktop plan. Treat this source's practical additions on their own terms: it attributes at least two direct quotes to Karpathy that do not appear, verbatim or in close paraphrase, in his actual gist — those specific phrasings should be read as this author's own framing, not Karpathy's.
```

Add to `## Recent changes`, in date order (newest first): directly below the existing `[2026-09-09]` terminology-reorganization entry and above the `[2026-07-07]` entry:

```
- [2026-08-20] Restructured the LLM Wiki section to lead with Karpathy's own original gist (the pattern's primary source, previously uncited here) rather than only the secondary PaperWiki example, and added a practitioner elaboration (@rvaniaaaa) built around Claude Desktop — with an explicit caveat that the elaboration misattributes two quotes to Karpathy.
```

The list has 3 entries live (cap is 10) — no spill needed.

### wiki/sources/articles/karpathy-llm-wiki-gist.md (new)

```md
---
title: "LLM Wiki (gist)"
type: source
source_type: article
source_file: raw/articles/2026-09-09-gistgithubcom-karpathy-442a6bf555914893e9891c11519de94f.md
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
published: 2026-04-04
ingested: 2026-09-09
domains: [agents]
---

# LLM Wiki (gist)

Andrej Karpathy's original "idea file" describing the LLM Wiki pattern: an LLM-maintained personal knowledge base compiled from raw sources, structured as three layers (raw sources, wiki, schema) with three operations (ingest, query, lint). Meant to be pasted directly to an LLM agent as a starting brief for instantiating the pattern in any domain. No publish-date byline is visible on the fetched gist page itself; 2026-04-04 is corroborated by multiple independent references within the raw content (including a secondary article quoting Karpathy's own dated follow-up tweet), not a direct byline.

## Influenced pages

- [Knowledge layer](../../concepts/knowledge-layer.md) — primary-source treatment of the LLM Wiki pattern, previously only cited via a secondary example

## Key claims extracted

- Three-layer architecture: raw sources (immutable), the wiki (LLM-owned markdown), the schema (CLAUDE.md/AGENTS.md-style, co-evolved with the user)
- Three operations: Ingest (a source can touch 10-15 pages), Query (answers should be filed back into the wiki as new pages), Lint (contradictions, staleness, orphan pages, missing cross-references)
- index.md is content-oriented (catalog, read first, works to ~100 sources without embeddings); log.md is chronological/append-only and grep-able with a consistent line prefix
- Recommends `qmd` (local hybrid BM25/vector markdown search, CLI + MCP server) once scale outgrows the index file
- Framed as a realized Vannevar Bush Memex (1945): the maintenance problem Bush never solved is handled by the LLM
- Explicitly abstract/idea-only — meant to be co-instantiated by the user and their LLM agent for their own domain
- Gist has 5,000+ stars/forks and a large comment thread of independent implementations and variants
```

### wiki/sources/tweets/rvaniaaaa-second-brain-compiler-2026-08-20.md (new)

```md
---
title: "The Second Brain Is Not a Storage System. It's a Compiler."
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-rvaniaaaa-2090512486738845784.md
url: https://x.com/rvaniaaaa/status/2090512486738845784
published: 2026-08-20
ingested: 2026-09-09
domains: [agents]
---

# The Second Brain Is Not a Storage System. It's a Compiler.

A practitioner's (@rvaniaaaa) elaboration of Karpathy's LLM Wiki pattern built specifically around Claude Desktop, under the name "second brain" (which the wiki treats as a personal-scope alias of the knowledge-layer concept): a "storage vs. compiler" framing, four copy-paste starter prompts (source ingestion, a CLAUDE.md-building interview, project-folder scaffolding, a daily compilation loop), a claimed 50-100-source density threshold before compounding value appears, and a note that the loop requires a paid Claude Desktop plan (scheduled tasks and file access aren't on the free tier). Caution: this post attributes at least two direct quotes to Karpathy that do not appear, verbatim or in close paraphrase, in Karpathy's actual gist — treat those specific phrasings as this author's own, not Karpathy's.

## Influenced pages

- [Knowledge layer](../../concepts/knowledge-layer.md) — practitioner-elaboration paragraph, with the misattribution caveat

## Key claims extracted

- "Storage vs. compiler" framing: a library only answers on search; a compiler reads, connects, flags contradictions, and files synthesis permanently on every new source
- Four starter prompts: ingest a source, interview-build CLAUDE.md, scaffold a project folder (Inputs/Process/Outputs/Feedback), run a daily compilation loop with a change-brief
- Claimed density threshold: compounding value (non-obvious links) becomes visible around 50-100 well-compiled sources
- Requires Claude Desktop on a paid plan — free tier lacks the scheduled-tasks/file-access features the loop depends on
- Misattributes at least two quotes to Andrej Karpathy not found in his actual gist text
- Uses "second brain" for what the wiki calls a personal-scope knowledge layer; no new concept introduced
```
