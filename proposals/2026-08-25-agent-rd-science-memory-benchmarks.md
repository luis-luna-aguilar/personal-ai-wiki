---
type: proposal
source: raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md
status: pending
created: 2026-08-25
---

# Proposal: New agent benchmarks target R&D automation, scientific workflows, and long-context memory

## Summary
Three benchmark releases from the same AINews issue: **InferenceBench** (AI R&D automation via open-ended inference-optimization tasks), **Terminal-Bench Science** (extends Terminal-Bench into real scientific workflows), and **MINTEval** (long-context agent memory under frequent updates/interference). The triage flagged this signal `verify-first` since it was AINews-recap-sourced — **all three were subsequently located and independently verified against their primary sources** (two arXiv papers, one project announcement page), so this proposal is grounded in the primaries, with the newsletter kept only as a discovery/secondary source.

## Verification note

Per `AGENTS.md`'s instruction to verify benchmark claims against primaries rather than relying on the AINews recap alone, I ran targeted web searches and fetched:
- InferenceBench paper: https://arxiv.org/abs/2607.20468 (submitted 2026-05-20)
- Terminal-Bench Science announcement: https://www.tbench.ai/news/tb-science-announcement
- MINTEval paper: https://arxiv.org/abs/2605.18565v2 (v1 2026-05-18, v2 2026-05-19)

All numeric claims in the page drafts below come from these primary sources, not from the newsletter. One AINews claim (an "inverse scaling" effect on InferenceBench, where Claude Sonnet 4.6 and GLM-5 rank better) does **not** appear in the fetched abstract — see the caveat on the new InferenceBench page and the Open Questions below.

## Intended changes

- [x] **Update** `wiki/benchmarks/terminal-bench.md` — add a "Terminal-Bench Science" section and a new Recent-changes section (page previously had none); `as_of` bumped 2026-04-23 → 2026-05-21
    > See draft below

- [x] **Update** `wiki/concepts/agent-memory.md` — add MINTEval as independent benchmark evidence; new Recent-changes entry (placed below the existing, newer 2026-07-07 entry); `as_of` unchanged (2026-07-07 remains the newest claim on the page)
    > See draft below

- [x] **Create** `wiki/benchmarks/inferencebench.md` — no existing page; now well-supported by a primary arXiv paper

- [x] **Create** `wiki/sources/papers/inferencebench-paper-2026-05.md`
- [x] **Create** `wiki/sources/articles/terminal-bench-science-announcement.md`
- [x] **Create** `wiki/sources/papers/minteval-paper-2026-05.md`
- [x] **Create** `wiki/sources/newsletters/ainews-erdos-benchmarks-cluster-2026-05-21.md` — discovery-source summary (kept lightweight; the OpenAI Erdős math result and Cohere Command A+ release from the same issue are explicitly *not* actioned here)

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

Frontmatter — one source id added:

```md
sources: [agent-memory-without-vector-db, memory-vs-context-rot-february, agent-memory-systems-layer-2026-06, minteval-paper-2026-05]
```

New bullet added to `## Current status`, after the existing "ReContext and BlockSearch-style work..." bullet:

```md
- MINTEval (arXiv, 2026-05) gives independent benchmark evidence for this: across 7 memory systems evaluated on long, interference-heavy contexts (state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits — averaging 138.8k tokens, up to 1.8M), average accuracy is only 27.9% and the best system reaches just 33.4%, with accuracy degrading further as the number of intervening updates increases.
```

`## Recent changes` (full section — new entry placed below the existing, newer 2026-07-07 entry):

```md
## Recent changes

- [2026-07-07] AINews memory cluster updates agent memory from retrieval problem to systems layer: extraction, dedupe, reconciliation, scoping, lifecycle, and offline trace writeback.
- [2026-05-19] MINTEval published: a dedicated benchmark for long-horizon memory under multi-target interference; 7 evaluated systems average 27.9% accuracy (best: 33.4%), giving independent confirmation that current memory systems are far from solved.
```

`## Caveats` — update to reflect that the "one startup's claims" caveat is now partly addressed by an independent benchmark:

> **Before:**
> ```
> - The current source set is centered on one startup's claims and a benchmark delta reported through newsletter coverage
> - This should be read as an architectural signal worth watching, not as proof that vector retrieval is obsolete in every setting
> ```
>
> **After:**
> ```
> - Most of the lifecycle-architecture framing (extraction, dedupe, reconciliation) still traces back to vendor claims (Supermemory, Engram) rather than independent benchmarks
> - MINTEval is an independent, peer-reviewable benchmark (not a vendor claim) and gives harder evidence that current memory systems — vanilla long-context LLMs, RAG, and memory-augmented agents alike — struggle badly (27.9% avg accuracy) on realistic interference-heavy tasks
> - This should still be read as an early, unsettled area rather than proof that any specific architecture (vector retrieval or otherwise) is the wrong approach
> ```

`## Sources` (full section, one line added):

```md
## Sources

- [Agent memory without vector databases](../sources/newsletters/agent-memory-without-vector-db.md)
- [Memory versus context rot in late February](../sources/newsletters/memory-vs-context-rot-february.md)
- [Agent memory becomes a systems layer](../sources/newsletters/agent-memory-systems-layer-2026-06.md)
- [MINTEval (arXiv paper)](../sources/papers/minteval-paper-2026-05.md)
```

### wiki/benchmarks/inferencebench.md (new)

```md
---
title: InferenceBench
type: benchmark
domains: [agents, coding]
tags: [agentic]
as_of: 2026-05-20
sources: [inferencebench-paper-2026-05, ainews-erdos-benchmarks-cluster-2026-05-21]
---

# InferenceBench

InferenceBench evaluates whether AI agents can perform open-ended LLM inference-serving optimization — not by retrieving a known recipe, but by genuinely exploring the solution space. Given a target model, one H100 GPU, an optimization scenario (prefill latency, decode latency, concurrent-request throughput, or a balanced mix), and a two-hour wall-clock budget, an agent must deploy and tune an OpenAI-compatible inference server from an unconstrained action space: install packages, compile dependencies, adopt vLLM/SGLang/TensorRT-LLM, apply quantization, write custom kernels, or build a server from scratch.

## Current status (as of 2026-05-20)

- Across 15 frontier agent configurations, agents reliably beat a naive PyTorch baseline (up to 8.08x) and often match or exceed default-settings serving engines (4.05x for vLLM)
- But agents still fall below a simple hyperparameter search under the same time budget (up to 11.53x) — the benchmark's key negative result
- 93.9% of agent runs converge on a vLLM-based final launcher even when SGLang, TGI, and TensorRT-LLM are explicitly available in the prompt
- Agent trajectories show agents enumerate many relevant optimization techniques but test only a few distinct configurations, spending remaining budget re-measuring or repairing rather than exploring meaningfully different strategies

## Why it matters

InferenceBench targets AI R&D automation directly: can an agent optimize its own serving infrastructure, not just write application code? The gap versus a bare hyperparameter sweep suggests the bottleneck isn't domain knowledge (agents know the right techniques) but breadth of exploration and systematic evaluation — a distinct failure mode from the coding-benchmark gaps tracked elsewhere in this wiki (e.g. [FrontierCode](frontiercode.md)).

## Caveats

- Small, early benchmark: one paper, 15 agent configurations, no public leaderboard cited yet
- AINews' secondary coverage additionally claimed an "inverse scaling" finding — smaller models like Claude Sonnet 4.6 and GLM-5 ranking better by preserving robust final states. This does **not** appear in the fetched arXiv abstract; we did not pull the full paper body, so this specific claim is flagged unverified rather than stated as confirmed on this page.

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
- 93.9% of agent runs converge on a vLLM-based launcher even when SGLang, TGI, and TensorRT-LLM are explicitly available
- Agents enumerate many relevant techniques but test only a few distinct configurations, spending remaining budget re-measuring/repairing rather than exploring broadly
- Submitted to arXiv 2026-05-20 (cs.AI)

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
- Contribution pipeline: Propose → Build → Review, via the Harbor Task Format, with an LLM judge plus human reviewers at each stage
- Task PR deadline stated on the page: August 17, 2026 (the page reads as a living document; this may be a since-passed interim deadline rather than the final one)
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
- Four domains: state tracking, multi-turn dialogue, Wikipedia revisions, GitHub commits; ~149 sessions/domain, ~86 updates deep on average
- Two question types: single-target recall and multi-target aggregation
- Evaluated 7 systems (vanilla long-context LLMs, RAG, memory-augmented agent frameworks): average accuracy only 27.9%, best system 33.4%
- Performance is primarily limited by retrieval and memory construction; accuracy degrades further as the number of intervening updates increases
- v1 submitted 2026-05-18, v2 (current) 2026-05-19
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

AINews Twitter-recap issue whose headline story is an OpenAI general-purpose model's disproof of a long-standing Erdős unit-distance conjecture (**not actioned in this proposal** — separately flagged in the triage as verify-first against OpenAI's own announcement). This summary covers only the agent-benchmark cluster from the same issue: InferenceBench, Terminal-Bench Science, and MINTEval — all three were independently verified against their primary sources (two arXiv papers and the Terminal-Bench Science site) rather than taken on this newsletter's word alone.

## Influenced pages
- [InferenceBench](../../benchmarks/inferencebench.md) — discovery source; factual claims sourced from the primary arXiv paper
- [Terminal-Bench](../../benchmarks/terminal-bench.md) — discovery source; factual claims sourced from the primary tbench.ai announcement
- [Agent memory](../../concepts/agent-memory.md) — discovery source; factual claims sourced from the primary MINTEval arXiv paper

## Key claims extracted
- InferenceBench: frontier agents underperform a simple vLLM/SGLang hyperparameter-tuning baseline; reported (but not primary-source-confirmed) inverse-scaling effect where Claude Sonnet 4.6 and GLM-5 rank well by preserving robust final states
- Terminal-Bench Science: extends agent evaluation into real scientific workflows; task contributions open
- MINTEval: long-context memory under frequent updates/interference; average instance length 138.8k tokens (up to 1.8M); average accuracy across 7 systems 27.9%, best system 33.4% (matches the primary paper)
- Not actioned from this issue: OpenAI's Erdős unit-distance result (math milestone; recommend verify-first against OpenAI's own announcement); Cohere Command A+ open release (thin secondary signal, no existing Cohere page)
```

## Schema / vocabulary additions

None needed. `domains: [agents, coding]` / `[agents]` / `[agents, science]` and `tags: [agentic]` all already exist in the controlled vocabulary.

## Open questions

- The OpenAI Erdős-conjecture math result and the Cohere Command A+ release, both from the same triage signal batch, are explicitly **not** covered by this proposal — they were called out in the triage as separate `verify-first` items. Let me know if you'd like those drafted as their own proposals.
- The Terminal-Bench Science page shows an "August 17, 2026" PR deadline despite being fetched today (2026-08-25); this reads like a living page whose deadline text may be stale relative to our fetch date rather than the announcement's original claim. Flagged in the source page rather than treated as a hard fact.
- `benchmarks/terminal-bench.md`'s existing "Current status" numbers (sub-65% frontier score) are unchanged from an April 2026 research-synthesis report and were not re-verified as part of this proposal — only the new Terminal-Bench Science section is newly sourced.
