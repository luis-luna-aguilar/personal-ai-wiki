---
type: proposal
source: raw/repos/context-dot-dev-sgrep.md
sources:
  - raw/repos/context-dot-dev-sgrep.md
  - raw/articles/2026-10-20-xerjorg.md
  - raw/newsletters/2026-10-13-ainews-meta-muse-wonder-wonder-full-msls-cla.md
  - raw/tweets/2026-10-13-getcontextdev-2110070862972158174.md
  - raw/tweets/2026-10-13-d0znpp-2110038855047164404.md
triage: proposals/triage/2026-10-11-to-2026-10-20-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: Local search tools for agents (sgrep and XERJ)

## Summary

### In short
Plain grep is no longer the only sensible default for agent code search: ranking or indexing results locally can cut model spend without lowering solve rates, though exact search still wins on exact text. Context.dev's sgrep cut LLM API cost 21.3% against ripgrep on 100 SWE-bench Verified attempts (70 vs 68 solved), and XERJ reports 2.7x fewer output tokens when agents query an index instead of re-reading files. The proposal adds one pattern bullet to Agentic orchestration patterns and three source pages, with no tool pages. Reason to hesitate: that page sits at its 2,000-word ceiling and this takes it to about 106%, inside the warning band.

[[#Open questions|Open questions: 1 to answer.]]

### The source
On 13 October 2026 two small open-source search tools launched on the same day, both pitched at coding agents. Context.dev released sgrep, a Rust command-line tool that sits beside ripgrep (the fast exact-text search most agents already call). Ripgrep finds every match but has no sense of which match matters, so an agent either floods its context with junk or never sees the one passage it needed. sgrep reranks candidates by meaning using "static embeddings": one small stored vector per token, averaged, with no neural network run at search time, so it works on a laptop CPU with no account or server. Its README is unusually candid: use ripgrep for known names, sgrep for intent queries ("when does a failed scrape consume credits"), and it concedes that the rival tool CK beats it on snippet retrieval. In its own SWE-bench Verified run with GPT-6 Luna, piping ripgrep output through sgrep spent 21.3% less on the LLM and solved 70 of 100 attempts against 68.

XERJ, from Ivan Novikov, goes further: a single Rust binary that indexes code, documents and data and speaks the Elasticsearch API. Its pitch, "reference coding", is to clone the open-source repos closest to what you are building, index them, and let the agent look up real definitions instead of inventing method names. XERJ reports 2.7x fewer output tokens at the same solve rate over eight tasks, and also publishes a tie: on a ten-question data exam, its agent scored nine plus a partial against a grep-and-Python baseline's ten. The same week Perplexity, per an AINews summary, found grep beat semantic search 63% to 37% on financial-document questions.

### What changes
The wiki has no material on agent code-search tooling; the nearest pattern is Uber's knowledge-graph grounding "instead of blind code search" on the orchestration page.

- **Agentic orchestration patterns** gains one bullet under "Harness, packaging, and tool design": rank or index search results before they reach the context window, with sgrep, XERJ and the Perplexity counterpoint, and the rule of thumb of exact search for names, ranked search for intent. It gains one Recent-changes entry dated 13 October (9 of 10, no spill) and three sources. Page date moves to 13 October.
- New source pages `wiki/sources/repos/context-dot-dev-sgrep.md`, `wiki/sources/articles/xerj-org.md`, and a story page `wiki/sources/newsletters/ainews-perplexity-grep-vs-semantic-2026-10-13.md`.

### What to weigh
The xerj.org homepage carries no date, so its source page uses the launch tweet's 13 October date. The two launch tweets get no source pages because the README and homepage hold everything they say, except XERJ's "Corpus Hub" name for public shared corpora, which the bullet leaves out. The scope choice is a single bullet rather than tool pages; it leaves the orchestration page at about 106% of its ceiling, which needs no split.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add one bullet at the end of `### Harness, packaging, and tool design`; adds one Recent-changes entry dated 2026-10-13 (list goes 8 → 9, no spill); appends three ids to frontmatter `sources:` and three links to `## Sources`; `as_of` 2026-09-09 → 2026-10-13
- [ ] **Create** `wiki/sources/repos/context-dot-dev-sgrep.md` — source summary
- [ ] **Create** `wiki/sources/articles/xerj-org.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/ainews-perplexity-grep-vs-semantic-2026-10-13.md` — story-specific source summary for the AINews 2026-10-13 newsletter

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter changes:

```
as_of: 2026-10-13
sources: [...existing ids..., context-dot-dev-sgrep, xerj-org, ainews-perplexity-grep-vs-semantic-2026-10-13]
```

New bullet, appended as the last item of `### Harness, packaging, and tool design` (after the Code-mode bullet):

```
- **Rank or index search results before they reach the context window.** Ripgrep finds every match but not the one that matters, so agents either fill context with junk or miss the key passage. Context.dev's [sgrep](https://github.com/context-dot-dev/sgrep) (MIT, local Rust CLI) reranks ripgrep output with small static embeddings blended with BM25 keyword scores, no server or API call; on 100 SWE-bench Verified attempts it cut LLM spend 21.3% versus ripgrep and solved 70 versus 68. [XERJ](https://xerj.org) (Apache-2.0, one Rust binary with an Elasticsearch-compatible API) indexes code, docs, and reference repos so the agent retrieves a definition instead of reading files: 2.7x fewer output tokens at the same solve rate, but only a tie with grep-and-Python on a data exam. Exact search still wins on exact text: Perplexity found grep beat semantic search 63% to 37% on financial-document questions. Use exact search for known names, ranked or indexed search for intent queries. *Sources: sgrep README, xerj.org, AINews (2026-10-13)*
```

`## Recent changes` — insert one entry directly below the 2026-10-19 entry (date order, newest first):

```
- [2026-10-13] Added the ranked/indexed local search pattern: sgrep (ripgrep reranked by static embeddings, 21.3% lower LLM spend on SWE-bench Verified, 70 vs 68 solved) and XERJ (index-first reference coding, 2.7x fewer output tokens), with Perplexity's grep-beats-semantic counterpoint (63% vs 37%).
```

`## Sources` — append three links:

```
- [context-dot-dev/sgrep (GitHub README)](../sources/repos/context-dot-dev-sgrep.md)
- [XERJ — the search engine built for AI agents](../sources/articles/xerj-org.md)
- [AINews — Perplexity: grep beats semantic search on financial documents](../sources/newsletters/ainews-perplexity-grep-vs-semantic-2026-10-13.md)
```

### wiki/sources/repos/context-dot-dev-sgrep.md (new)

```
---
title: context-dot-dev/sgrep (GitHub README)
type: source
source_type: repo
source_file: raw/repos/context-dot-dev-sgrep.md
url: https://github.com/context-dot-dev/sgrep
published: 2026-10-13
ingested: 2026-10-20
domains: [coding, agents]
---

# context-dot-dev/sgrep (GitHub README)

README for sgrep, Context.dev's MIT-licensed local search CLI for agents, launched 2026-10-13. Written in Rust, it finds code and document passages by words and meaning, or reranks the output of a focused ripgrep command (`rg --json ... | sgrep "<query>" --stdin`). Ranking uses Minish Lab static embeddings (one stored vector per token, averaged; no transformer pass at search time, 32–34 MB model, CPU only), blended 75% semantic / 25% BM25, with exact identifier matches ranked first. No account, hosted index, or model server. The README positions it against ripgrep (exact names and regexes), CK (local semantic search, which beats sgrep on CoSQA snippet retrieval) and mgrep (hosted, uploads files).

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — ranked/indexed local search pattern

## Key claims extracted
- Piped sgrep used 21.3% less LLM API spend than ripgrep on SWE-bench Verified (GPT-6 Luna, 50 tasks x 2 repeats), solving 70/100 vs 68/100 attempts
- Leads complete-function retrieval on RepoQA (600 questions); CK semantic leads snippet retrieval on CoSQA (500 questions)
- Use ripgrep for exact matches; sgrep returns approximate matches and its scores are relative ranking signals, not confidence values
- Code parsing via Tree-sitter for Python, C/C++, C#, Go, Java, Rust, JS/TS; no PDF or image parsing
```

### wiki/sources/articles/xerj-org.md (new)

```
---
title: XERJ — the search engine built for AI agents
type: source
source_type: article
source_file: raw/articles/2026-10-20-xerjorg.md
url: https://xerj.org
published: 2026-10-13
ingested: 2026-10-20
domains: [coding, agents]
---

# XERJ — the search engine built for AI agents

Homepage of XERJ, an Apache-2.0 search engine shipped as one static Rust binary that indexes code, documents and data and answers agent queries from the index instead of the agent's context window. It speaks the Elasticsearch API, parses source with tree-sitter (36 languages) into a definitions field, and adds a namespaced `/_memory` API for agent memory. The page carries no date; the published date is the launch tweet's (Ivan Novikov, 2026-10-13), which also names a public "Corpus Hub" of shared reference corpora.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — ranked/indexed local search pattern

## Key claims extracted
- "Reference coding": clone and index the open-source repos closest to the project so the agent retrieves exact definitions before writing code
- Eight tasks in four languages, 16 runs per arm: 2.7x fewer output tokens than a grep-driven agent at the same solve rate, roughly half the cost; 9/9 vs 0/9 on a Rust library the model had not seen
- Definition-first search puts the right file first 94% of the time on an 80-task cross-file benchmark, vs 38% for body-text search
- On a 518 MB, ten-question data exam, a XERJ-backed agent scored 9 plus 1 partial vs a grep-and-Python baseline's 10/10: "a tie on accuracy"
- Built-in embedder is lexical feature-hashing, not neural; neural encoder is an optional upgrade
```

### wiki/sources/newsletters/ainews-perplexity-grep-vs-semantic-2026-10-13.md (new)

```
---
title: 'AINews — Perplexity: grep beats semantic search on financial documents'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-13-ainews-meta-muse-wonder-wonder-full-msls-cla.md
published: 2026-10-13
ingested: 2026-10-20
domains: [agents, coding]
---

# AINews — Perplexity: grep beats semantic search on financial documents

One item from the AINews 2026-10-13 issue on agent infrastructure: Perplexity runs each project as a Git forge with ephemeral agent sandboxes committing to S3 (under 2% of commits collide), and reports that grep beat semantic search 63% to 37% on financial-document questions (via @AravSrinivas). The same issue lists ColGrep-Agent-2B, a local code-search agent claiming 34% fewer API tokens.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — counterpoint in the ranked/indexed local search pattern

## Key claims extracted
- Perplexity: grep beat semantic search 63% to 37% on financial-document questions
- Perplexity: fewer than 2% of agent commits collide in its Git-forge-per-project setup
- ColGrep-Agent-2B: local code-search agent, 34% fewer API tokens
```

## Schema / vocabulary additions

None.

## Open questions
- Should sgrep or XERJ get their own `tools/` pages (assumed no: both are days-old launches with one benchmark each, so a pattern bullet is enough until a second source cites them)?
