---
type: proposal
sources:
  - raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md
  - raw/papers/2026-08-25-arxivorg-abs-260720468.md
  - raw/papers/2026-08-25-arxivorg-abs-260518565v2.md
  - raw/articles/2026-08-25-tbenchai-news-tb-science-announcement.md
status: pending
created: 2026-08-25
---

# Proposal: New agent benchmarks target R&D automation, scientific workflows, and long-context memory

## Summary

### The source

The 21 May 2026 AINews issue, headlined by OpenAI's Erdős result, also surfaced three new agent benchmarks, each checked here against its primary. InferenceBench (arXiv, 20 May) asks whether an agent can tune an LLM inference server given one H100 and two hours. Across 15 frontier agent configurations, agents beat a naive PyTorch baseline by up to 8.08x and default vLLM by 4.05x, yet a plain hyperparameter sweep under the same budget reaches 11.53x. The authors' reading: agents know the right techniques but converge on one framework and test few configurations. Terminal-Bench Science (tbench.ai, around 21 May) extends the Terminal-Bench shell benchmark into real research workflows across five natural-science fields: 100+ planned tasks, verified by pytest checks, calibrated to a 10–20% solve rate, contributed by scientists through a Stanford/Laude Institute pipeline.

MINTEval (arXiv, 19 May) tests agent memory under "interference" — long contexts where facts are later revised or contradicted. Its 15.6k questions run over contexts averaging 138.8k tokens (up to 1.8M) from dialogue, Wikipedia revisions and GitHub commits. Seven systems — long-context LLMs, RAG and memory-augmented agents alike — average just 27.9%, falling further as updates pile up. Only the arXiv abstracts were read, not the full papers.

### What changes

The wiki knew Terminal-Bench from one April research synthesis, and agent memory as a concept resting mostly on Supermemory's claims via newsletters; InferenceBench had no page.

- **Terminal-Bench** gains a Terminal-Bench Science section, a matching status bullet and a first-ever Recent changes list; the April numbers and "verify" caveat stay verbatim. Page date moves to 21 May.
- **Agent memory** gains a sixth status bullet on MINTEval and a Recent changes entry filed below the newer July one. Its two caveats become three: the original wording survives, and MINTEval is added as independent evidence that every architecture struggles, not that one wins. Page date stays at July.
- New page `benchmarks/inferencebench.md` states only abstract-backed numbers; AINews' "inverse scaling" claim (Claude Sonnet 4.6 and GLM-5 ranking well) sits in Caveats as unverified.
- Four source pages: the two papers, the TB-Science announcement, and a lightweight AINews summary scoped to the benchmark cluster. No dashboards, leader lines, spills or schema changes.

### What to weigh

Two figures exist only in the AINews recap — the inverse-scaling claim and MINTEval's "best system 33.4%" — and are kept with "per AINews" attribution; strike either and the newsletter leaves that page's sources (and the InferenceBench page date reverts to 20 May). Terminal-Bench will look fresher than its headline numbers, which remain unverified April synthesis. Agent memory's status hits six bullets, past the concept-page guideline — accept, or fold MINTEval into the caveats only. TB-Science's 21 May date is inferred from the newsletter; the page is undated and shows a passed 17 August deadline.

## Verification note

Per `AGENTS.md`'s instruction to verify benchmark claims against primaries rather than relying on the AINews recap alone, I ran targeted web searches and fetched:
- InferenceBench paper: https://arxiv.org/abs/2607.20468 (submitted 2026-05-20)
- Terminal-Bench Science announcement: https://www.tbench.ai/news/tb-science-announcement
- MINTEval paper: https://arxiv.org/abs/2605.18565v2 (v1 2026-05-18, v2 2026-05-19)

Only the arXiv abstract pages were fetched, not the full papers. All numeric claims in the page drafts below come from these primary sources except two that appear only in the AINews recap and are attributed to it wherever used: the InferenceBench "inverse scaling" effect (Claude Sonnet 4.6 and GLM-5 ranking better), kept as an unverified caveat on the new InferenceBench page, and MINTEval's "best system 33.4%" figure (the abstract gives only the 27.9% average).

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/benchmarks/terminal-bench.md` — add a "Terminal-Bench Science" section and a new Recent-changes section (page previously had none); `as_of` bumped 2026-04-23 → 2026-05-21 with the `## Current status` heading bumped to match and one TB-Science bullet added; two sources added
    > See draft below

- [x] **Update** `wiki/concepts/agent-memory.md` — add MINTEval as independent benchmark evidence; new Recent-changes entry (placed below the existing, newer 2026-07-07 entry); two sources added (paper + AINews issue); Caveats rewritten preserving original wording; `as_of` unchanged (2026-07-07 remains the newest claim on the page)
    > See draft below

- [x] **Create** `wiki/benchmarks/inferencebench.md` — no existing page; now well-supported by a primary arXiv paper

- [x] **Create** `wiki/sources/papers/inferencebench-paper-2026-05.md`
- [x] **Create** `wiki/sources/articles/terminal-bench-science-announcement.md`
- [x] **Create** `wiki/sources/papers/minteval-paper-2026-05.md`
- [x] **Create** `wiki/sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md` — discovery-source summary (kept lightweight; scoped to the agent-benchmark cluster of the issue only)

## Page drafts

### wiki/benchmarks/terminal-bench.md (updated)

Frontmatter:

```md
---
title: Terminal-Bench
type: benchmark
domains: [agents, coding]
tags: [agentic, cli]
as_of: 2026-05-21
sources: [agents-evals-deep-research, terminal-bench-science-announcement, ainews-erdos-benchmarks-cluster-2026-05-21]
---
```

`## Current status` (full section — heading bumped to match `as_of`; existing bullets unchanged, one TB-Science bullet appended):

```md
## Current status (as of 2026-05-21)

- 89 hard, real-world multi-step tasks in isolated container environments
- Frontier models score below 65% (as reported; verify against current leaderboard)
- Tasks cover system administration, compilation, and CLI-based debugging
- Evaluates agents in real shell environments, not simulated inputs
- Terminal-Bench Science extension announced 2026-05-21: 100+ planned natural-science workflow tasks, contributions open (see section below)
```

New section, inserted between `## Why it matters` and `## Caveats`:

```md
## Terminal-Bench Science (as of 2026-05-21)

Terminal-Bench Science (TB-Science) extends the Terminal-Bench franchise from software-engineering tasks into real computational workflows from the natural sciences: life, physical, earth, mathematical, and engineering sciences. It targets 100+ tasks, each scientifically grounded (drawn from real research), objectively verifiable via deterministic pytest-based checks, and calibrated toward a 10-20% solve rate at release so tasks remain genuinely hard rather than saturated on day one. Tasks are contributed by practicing scientists through a Propose → Build → Review pipeline (Harbor Task Format), hosted by Stanford University and the Laude Institute, with contributor co-authorship on the resulting paper. Task contributions were open as of the announcement.
```

New section, added at the end of the file (page had no Recent-changes section before):

```md
## Recent changes

- [2026-05-21] Terminal-Bench Science extension announced: 100+ planned tasks across five scientific domains, contributor-sourced via the Harbor Task Format, targeting a 10-20% solve rate at release.
```

`## Sources` (full section, two lines added):

```md
## Sources

- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/agents-evals-deep-research.md)
- [Terminal-Bench Science announcement](../sources/articles/terminal-bench-science-announcement.md)
- [AINews — agent-benchmark cluster (InferenceBench, Terminal-Bench Science, MINTEval)](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
```

### wiki/concepts/agent-memory.md (updated)

Frontmatter — two source ids added (the AINews issue is included because the 33.4% best-system figure is only reported there):

```md
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06, minteval-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21]
```

New bullet added to `## Current status`, after the existing "ReContext and BlockSearch-style work..." bullet:

```md
- MINTEval (arXiv, 2026-05) gives independent benchmark evidence for this: across 7 systems (vanilla long-context LLMs, RAG, and memory-augmented agent frameworks) evaluated on long, interference-heavy contexts (state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits — averaging 138.8k tokens, up to 1.8M), average accuracy is only 27.9% (best system 33.4%, per AINews' recap of the authors' thread), with accuracy degrading further as the number of intervening updates increases.
```

`## Recent changes` (full section — new entry placed below the existing, newer 2026-07-07 entry):

```md
## Recent changes

- [2026-07-07] AINews memory cluster updates agent memory from retrieval problem to systems layer: extraction, dedupe, reconciliation, scoping, lifecycle, and offline trace writeback.
- [2026-05-19] MINTEval published: a dedicated benchmark for long-horizon memory under multi-target interference; 7 evaluated systems average 27.9% accuracy (best 33.4% per AINews' recap), giving independent confirmation that current memory systems are far from solved.
```

`## Caveats` — rewritten to keep both original caveats (still true for the vendor-derived sources) and add MINTEval as independent evidence:

> **Before:**
> ```
> - The current source set is centered on one startup's claims and a benchmark delta reported through newsletter coverage
> - This should be read as an architectural signal worth watching, not as proof that vector retrieval is obsolete in every setting
> ```
>
> **After:**
> ```
> - Most of the lifecycle-architecture framing (extraction, dedupe, reconciliation) still traces back to one startup's claims (Supermemory, plus Engram) and a benchmark delta reported through newsletter coverage, not to independent benchmarks
> - MINTEval is an independent academic benchmark (an arXiv preprint, not a vendor claim) and gives harder evidence that current memory systems — vanilla long-context LLMs, RAG, and memory-augmented agents alike — struggle badly (27.9% avg accuracy) on realistic interference-heavy tasks
> - This should still be read as an architectural signal worth watching, not as proof that vector retrieval is obsolete in every setting — MINTEval shows every evaluated approach struggling, not one architecture winning
> ```

`## Sources` (full section, two lines added):

```md
## Sources

- [Agent memory without vector databases](../sources/newsletters/agent-memory-without-vector-db.md)
- [Memory versus context rot in late February](../sources/newsletters/memory-vs-context-rot-february.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
- [MINTEval (arXiv paper)](../sources/papers/minteval-paper-2026-05.md)
- [AINews — agent-benchmark cluster (InferenceBench, Terminal-Bench Science, MINTEval)](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
```

### wiki/benchmarks/inferencebench.md (new)

```md
---
title: InferenceBench
type: benchmark
domains: [agents, coding]
tags: [agentic]
as_of: 2026-05-21
sources: [inferencebench-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21]
---

# InferenceBench

InferenceBench evaluates whether AI agents can perform open-ended LLM inference-serving optimization — not by retrieving a known recipe, but by genuinely exploring the solution space. Given a target model, one H100 GPU, an optimization scenario (prefill latency, decode latency, concurrent-request throughput, or a balanced mix), and a two-hour wall-clock budget, an agent must deploy an OpenAI-compatible inference server and optimize the speed of LLM inference.

## Current status (as of 2026-05-21)

- Across 15 frontier agent configurations, agents reliably beat a naive PyTorch baseline (up to 8.08x) and often match or exceed default-settings serving engines (4.05x for vLLM)
- But agents still fall below a simple hyperparameter search under the same time budget (up to 11.53x) — the benchmark's key negative result
- Agents overwhelmingly converge on a single inference framework rather than exploring alternatives
- Agent trajectories show agents enumerate many relevant optimization techniques but test only a few distinct configurations, spending remaining budget re-measuring, repairing, or tuning hyperparameters rather than exploring substantially different strategies

## Why it matters

InferenceBench targets AI R&D automation directly: can an agent optimize its own serving infrastructure, not just write application code? The gap versus a bare hyperparameter sweep suggests the bottleneck isn't domain knowledge (agents know the right techniques) but breadth of exploration and systematic evaluation — a distinct failure mode from the coding-benchmark gaps tracked elsewhere in this wiki (e.g. [FrontierCode](frontiercode.md)).

## Caveats

- Small, early benchmark: one paper, 15 agent configurations; only the arXiv abstract has been read, so per-model results and any leaderboard are not captured here
- AINews' secondary coverage (2026-05-21) additionally claimed an "inverse scaling" finding — smaller models like Claude Sonnet 4.6 and GLM-5 ranking better by preserving robust final states. This does **not** appear in the fetched arXiv abstract; we did not pull the full paper body, so this specific claim is flagged unverified rather than stated as confirmed on this page.

## Sources

- [InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents (arXiv)](../sources/papers/inferencebench-paper-2026-05.md)
- [AINews — agent-benchmark cluster](../sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md)
```

### wiki/sources/papers/inferencebench-paper-2026-05.md (new)

```md
---
title: "InferenceBench: A Benchmark for Open-Ended LLM Inference Optimization by AI Agents"
type: source
source_type: paper
source_file: raw/papers/2026-08-25-arxivorg-abs-260720468.md
url: https://arxiv.org/abs/2607.20468
published: 2026-05-20
ingested: 2026-08-25
domains: [agents, coding]
---

# InferenceBench (arXiv paper)

Jehyeok Yeon, Ben Rank, and Maksym Andriushchenko introduce InferenceBench: agents must deploy and optimize an OpenAI-compatible LLM inference server under a two-hour, one-H100 budget, across four optimization scenarios (prefill latency, decode latency, concurrent-request throughput, and a balanced mix). The goal is to test genuine open-ended optimization rather than retrieval of a memorized solution recipe.

## Influenced pages
- [InferenceBench](../../benchmarks/inferencebench.md) — new benchmark page

## Key claims extracted
- Across 15 frontier agent configurations, agents beat a naive PyTorch baseline by up to 8.08x and often match/exceed default-settings vLLM (4.05x)
- Agents still fall short of a simple hyperparameter search under the same budget (up to 11.53x) — the paper's central negative result
- Agents overwhelmingly converge on a single inference framework (the abstract does not name it or give a percentage)
- Agents enumerate many relevant techniques but test only a few distinct configurations, spending remaining budget re-measuring, repairing, or tuning hyperparameters rather than exploring substantially different strategies
- The authors' conclusion: the bottleneck is not domain knowledge but proposing diverse configurations, evaluating them systematically, and submitting the best one
- Submitted to arXiv 2026-05-20 (cs.AI); only the abstract page was fetched

## Verification note
AINews' secondary recap additionally claimed an "inverse scaling" finding — smaller models like Claude Sonnet 4.6 and GLM-5 ranking better by preserving robust final states. This claim does not appear in the fetched abstract; the full paper body was not fetched, so this specific claim is flagged unverified rather than included on the benchmark page as confirmed.
```

### wiki/sources/articles/terminal-bench-science-announcement.md (new)

```md
---
title: "Terminal-Bench-Science: Contribute your scientific workflows as tasks for AI Agents"
type: source
source_type: article
source_file: raw/articles/2026-08-25-tbenchai-news-tb-science-announcement.md
url: https://www.tbench.ai/news/tb-science-announcement
published: 2026-05-21
ingested: 2026-08-25
domains: [agents, science]
---

# Terminal-Bench Science announcement

Official announcement of Terminal-Bench-Science (TB-Science), extending the Terminal-Bench franchise from software-engineering tasks into real computational workflows across the natural sciences. Hosted by Stanford University and the Laude Institute, built on the Harbor Task Format, with contributor co-authorship on the resulting paper.

## Influenced pages
- [Terminal-Bench](../../benchmarks/terminal-bench.md) — new "Terminal-Bench Science" section

## Key claims extracted
- Targets 100+ tasks across life sciences, physical sciences, earth sciences, mathematical sciences, and engineering sciences
- Tasks must be scientifically grounded (real research workflows), objectively verifiable (deterministic pytest-based checks), and genuinely difficult (targeting a 10-20% solve rate at release)
- Contribution pipeline: Propose → Build → Review, via the Harbor Task Format; an LLM judge screens proposals against a rubric and human reviewers approve proposals and task PRs
- Hosted by Stanford University and the Laude Institute as an open academic collaboration; contributors with merged tasks receive co-authorship on the resulting paper
- Task PR deadline stated on the page: August 17, 2026 (the page carries no publication date and reads as a living document; this may be a since-passed interim deadline rather than the final one)
- Builds on Terminal-Bench, already adopted by Anthropic, OpenAI, and Google DeepMind for software-engineering agent evaluation
```

### wiki/sources/papers/minteval-paper-2026-05.md (new)

```md
---
title: "MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems"
type: source
source_type: paper
source_file: raw/papers/2026-08-25-arxivorg-abs-260518565v2.md
url: https://arxiv.org/abs/2605.18565v2
published: 2026-05-19
ingested: 2026-08-25
domains: [agents]
---

# MINTEval (arXiv paper)

Hyunji Lee et al. introduce MINTEval, a benchmark for long-horizon agent memory under multi-target interference — contexts with frequently updated, interconnected information, where earlier facts may be revised or contradicted later.

## Influenced pages
- [Agent memory](../../concepts/agent-memory.md) — added MINTEval as independent benchmark evidence for the "memory as systems problem" thesis

## Key claims extracted
- 15.6k question-answering pairs; long-horizon contexts averaging 138.8k tokens, extending up to 1.8M tokens per instance
- Four domains: state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits
- Two question types: single-target recall and multi-target aggregation
- Evaluated 7 systems (vanilla long-context LLMs, RAG, memory-augmented agent frameworks): consistently low performance, average accuracy 27.9%, worst on questions requiring aggregation over multiple pieces of evidence
- Performance is primarily limited by retrieval and memory construction; accuracy degrades further as the number of intervening updates increases
- v1 submitted 2026-05-18, v2 (current) 2026-05-19; only the abstract page was fetched

## Verification note
The "best system 33.4%" figure quoted on the agent-memory page comes from AINews' recap of the authors' thread, not from this abstract; it is attributed accordingly there.
```

### wiki/sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md (new)

```md
---
title: "[AINews] OpenAI GPT-next disproves 80 year old Erdős planar unit distance problem for under $1000"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md
url: https://www.latent.space/p/ainews-openai-gpt-next-disproves
published: 2026-05-21
ingested: 2026-08-25
domains: [agents, models]
---

# AINews — Erdős result and agent-benchmark cluster

AINews Twitter-recap issue whose headline story is an OpenAI general-purpose model's disproof of a long-standing Erdős unit-distance conjecture (not covered on this page). This summary covers only the agent-benchmark cluster from the same issue: InferenceBench, Terminal-Bench Science, and MINTEval — all three were checked against their primary sources (two arXiv abstract pages and the Terminal-Bench Science site) rather than taken on this newsletter's word alone. Two figures appear only in this recap and are attributed to it where used: the InferenceBench "inverse scaling" claim and MINTEval's best-system 33.4%.

## Influenced pages
- [InferenceBench](../../benchmarks/inferencebench.md) — discovery source; factual claims sourced from the primary arXiv abstract; supplies the attributed, unverified inverse-scaling caveat
- [Terminal-Bench](../../benchmarks/terminal-bench.md) — discovery source; factual claims sourced from the primary tbench.ai announcement
- [Agent memory](../../concepts/agent-memory.md) — discovery source; factual claims sourced from the primary MINTEval arXiv abstract; supplies the attributed best-system 33.4% figure

## Key claims extracted
- InferenceBench: frontier agents underperform a simple vLLM/SGLang hyperparameter-tuning baseline; reported (but not primary-source-confirmed) inverse-scaling effect where Claude Sonnet 4.6 and GLM-5 rank well by preserving robust final states
- Terminal-Bench Science: extends agent evaluation into real scientific workflows; task contributions open
- MINTEval: long-context memory under frequent updates/interference; average instance length 138.8k tokens (up to 1.8M); average accuracy across 7 systems 27.9% (matches the primary abstract), best system 33.4% (recap-only; not in the abstract)
```

## Schema / vocabulary additions

None needed. `domains: [agents, coding]` / `[agents]` / `[agents, science]` and `tags: [agentic]` all already exist in the controlled vocabulary.

## Open questions

- The Terminal-Bench Science page shows an "August 17, 2026" PR deadline despite being fetched today (2026-08-25); this reads like a living page whose deadline text may be stale relative to our fetch date rather than the announcement's original claim. Flagged in the source page rather than treated as a hard fact.
- `benchmarks/terminal-bench.md`'s existing "Current status" numbers (sub-65% frontier score) are unchanged from an April 2026 research-synthesis report and were not re-verified as part of this proposal — only the new Terminal-Bench Science section is newly sourced.
