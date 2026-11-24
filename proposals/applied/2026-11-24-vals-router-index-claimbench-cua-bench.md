---
type: proposal
source: raw/articles/2026-11-24-valsai-benchmarks-vals_router_index.md
sources:
  - raw/articles/2026-11-24-valsai-benchmarks-vals_router_index.md
  - raw/articles/2026-11-24-valsai-benchmarks-claimbench.md
  - raw/articles/2026-11-24-valsai-benchmarks-cua_bench.md
  - raw/newsletters/2026-10-21-ainews-deepseek-deepinfer-open-source-sota-infe.md
  - raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
status: pending
created: 2026-11-24
---

# Proposal: Vals AI — Router Index, ClaimBench cascade, CUA-bench

## Summary

### In short
Off-the-shelf model routers do not yet beat simply picking one good model, while a narrow decision-model cascade cuts cost about twelvefold at near-perfect accuracy. Vals AI found all six routers it tested beaten on both score and cost by at least one single model, and a Perplexity decision model in front of Claude Haiku 5.5 checked 10-K claims for $0.10 per 1,000 against $1.19. The proposal adds both to the routing evidence and decision-model pages, and creates a CUA-bench page for Vals's real-time game benchmark, where no tested model averages 20 of 100. Reason to hesitate: CUA-bench's results predate GPT-6.2 Astra and Fable 5.2.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Vals AI runs independent evaluations, and three of its leaderboard pages feed this proposal. The **Router Index** (last updated 3 November) ran six commercial routers, products that pick a model for each request, through the roughly 1,250 agentic finance, coding, law and tax tasks of the Vals Index, each at its default setting: OpenRouter's Auto Router, Fireworks' Nexus Auto with two model pools, Ramp's Router, the OpenRouter-hosted Jev Router and Sakana's Fugu Max. None landed on the cost-accuracy frontier. The closest, Nexus Auto with Sol, scored 60.0% at $1.25 per task, while DeepSeek V4.1 Flash alone scored 61.3% at $0.66. Picking each task's best model from a router's own pool in hindsight, within the router's budget, would have scored 8 to 27 points higher, so the headroom is real but the products do not capture it. Vals traces part of the loss to routers running models at low reasoning effort, and to Ramp's router handing the final "submit" step to the cheaper GPT-6 Luna, whose submissions passed 25% of the time against 46% for the stronger model.

**ClaimBench** (updated 20 November) asks whether a 10-K excerpt supports, contradicts or says nothing about a claim, across 1,960 claims. A decision model (a small model that returns a probability per label instead of generating text) answers when its confidence clears a threshold tuned for at most 1% errors, and sends the rest to an LLM. Perplexity's Decider V1.3 in front of Haiku 5.5 reached 99.85% accuracy for $0.10 per 1,000 claims; Liquid's d1-ultra tops the standalone board at 100%. Subtle wording contradictions are the hard case.

**CUA-bench** (updated 13 October) has agents play six commercial games for three hours each with only screen pixels, keyboard and mouse; three games are named, three are held out so training on the public titles would show as a gap. GPT-6 Astra leads at about 19 of 100.

### What changes
The wiki records Vals's agent-team study and a Jev-as-judge escalation result, but has no measurement of packaged routers, no ClaimBench and no CUA-bench.

- **Cost-aware routing: evidence from practice** gains a Router Index bullet under Routing as infrastructure; the oldest Recent-changes entry spills to history. Page date moves to 3 November.
- **Decision models** gains ClaimBench in its Benchmarks bullet, including the cascade cost. Page date moves to 20 November.
- New page `benchmarks/cua-bench.md`, listed in the index (benchmarks 14 → 15).
- **State of Computer Use** gains a one-line pointer to CUA-bench and a Recent-changes entry; its oldest entry spills to history. Page date stays 24 November.
- Three new source pages, one per Vals page.

### What to weigh
CUA-bench's page carries no date of its own; 13 October comes from the "updated" stamp on Vals's benchmark list. Its tested models are one generation behind (GPT-6 Astra, Fable 5.1), so the page frames the result as the leaderboard's state, not a ranking of current models. ClaimBench and the Router Index replace the AINews figures from 21 October (Decider V1.2, five routers) with the live pages' newer numbers. A separate page for CUA-bench is a scope choice; see Open questions.

## Intended changes

- [ ] **Update** `wiki/training/cost-aware-routing-evidence.md` — add a Router Index bullet under Routing as infrastructure; add source id and link; as_of 2026-10-19 → 2026-11-03; adds one Recent-changes entry dated 2026-11-03
- [ ] **Spill** `wiki/training/cost-aware-routing-evidence.md` → `wiki/history/training/cost-aware-routing-evidence.md` — list at cap 10; spills the oldest entry (2026-09-25, Anthropic's effort analysis)
- [ ] **Update** `wiki/concepts/decision-models.md` — ClaimBench in the Benchmarks bullet; Current status stamp and as_of → 2026-11-20; adds one Recent-changes entry dated 2026-11-20; adds source id and link
- [ ] **Create** `wiki/benchmarks/cua-bench.md` — Vals's real-time game computer-use benchmark
- [ ] **Update** `wiki/state-of/computer-use.md` — one-line CUA-bench pointer under Computer use; adds one Recent-changes entry dated 2026-10-13; adds source id and link; as_of unchanged (2026-11-24)
- [ ] **Spill** `wiki/state-of/computer-use.md` → `wiki/history/state-of/computer-use.md` — list at cap 10; spills the oldest entry (2026-05-05, knowledge-work OS framing; the Gemini downloadable-files entry already spilled today)
- [ ] **Update** `wiki/index.md` — add `benchmarks/cua-bench`; benchmarks count 14 → 15, total 311 → 312
- [ ] **Create** `wiki/sources/articles/vals-router-index-2026-11-03.md`
- [ ] **Create** `wiki/sources/articles/vals-claimbench-2026-11-20.md`
- [ ] **Create** `wiki/sources/articles/vals-cua-bench-2026-10-13.md`

## Page drafts

### wiki/training/cost-aware-routing-evidence.md (updated)

Frontmatter: `as_of: 2026-11-03`; append `vals-router-index-2026-11-03` to `sources:`.

New bullet in `### Routing as infrastructure`, inserted directly after the "Eval data, not the router, is the moat." bullet:

```
- **Packaged routers lose to a single good model.** Vals AI's Router Index ran six routers at their default settings (OpenRouter Auto Router, Fireworks Nexus Auto with two pools, Ramp Router, the OpenRouter-hosted Jev Router, Sakana Fugu Max) through the Vals Index's roughly 1,250 agentic finance, coding, law and tax tasks. Every router was beaten on both score and cost by at least one single model: the best, Nexus Auto with Sol, scored 60.0% at $1.25 per task against [DeepSeek V4.1 Flash](../models/deepseek-v4-1-flash.md) alone at 61.3% for $0.66. Choosing the best model from each router's own pool in hindsight, within its budget, would have added 8–27 points, so the headroom exists but the products miss it. Vals points to two causes: routers ran models at lower reasoning effort, which hurt most on coding, and Ramp's router gave the final submit step to the cheaper GPT-6 Luna in 131 of 198 Terminal-Bench attempts, which passed 25% of the time against 46% for the stronger model. The narrow cascades under "Decision models for the yes/no steps" below are a different case: one fixed question, a calibrated confidence threshold, and escalation only below it.
```

`## Recent changes` — insert directly under the 2026-11-23 entry:

```
- [2026-11-03] Added Vals AI's Router Index: all six routers tested lose on both score and cost to at least one single model; hindsight selection within budget would add 8–27 points.
```

Then remove the oldest entry (`- [2026-09-25] Added Anthropic's effort analysis ...`) per the Spill item.

`## Sources` — append:

```
- [Vals AI — Vals Router Index](../sources/articles/vals-router-index-2026-11-03.md)
```

### wiki/history/training/cost-aware-routing-evidence.md (updated — spill)

Append at the end of the file. The file already ends with a 2026-11-24 archive block; if applied on that date, add the entry to that block instead of opening a new header:

```

## Archived from current page on <apply date>

- [2026-09-25] Added Anthropic's effort analysis to Model and harness selection wins (Terminal-Bench 3.0: effort buys edge-case verification, not a better approach).
```

### wiki/concepts/decision-models.md (updated)

Frontmatter: `as_of: 2026-11-20`; append `vals-claimbench-2026-11-20` to `sources:`.

Heading: `## Current status (as of 2026-11-20)`.

Replace the **Benchmarks** bullet with:

```
- **Benchmarks.** There are three competing indices: Cloudflare's "Jev Decision Index", Hugging Face's Decision Index v0.3 and Artificial Analysis's Decision Index (14 October). On AA's index, Liquid d1-ultra leads at 65 against Jev 1.14's 57. Claude Haiku 5.5 at low effort scores 61, but costs $184 against Jev's $42 per million tasks and takes 1.4 s against 0.13 s per task. Vals AI's ClaimBench (1,960 claims checked against 10-K excerpts: supported, contradicted, or not addressed) tests the cascade use directly: a decision model answers when its confidence clears a threshold tuned for at most 1% errors and sends the rest to an LLM. Perplexity's Decider V1.3 in front of Haiku 5.5 reached 99.85% accuracy for $0.10 per 1,000 claims, against $1.19 for Haiku's own label call, and answered almost every claim itself; d1-ultra leads the standalone board at 100%. Subtle one-word contradictions separate the field (Decider V1.3 99.0%, the weakest models near 50%).
```

`## Recent changes` — insert at the top:

```
- [2026-11-20] Added Vals AI's ClaimBench: a Decider V1.3 → Haiku 5.5 cascade checks 10-K claims at 99.85% accuracy for $0.10 per 1,000, against $1.19 for Haiku alone.
```

`## Sources` — append:

```
- [Vals AI — ClaimBench leaderboard and methodology](../sources/articles/vals-claimbench-2026-11-20.md)
```

### wiki/benchmarks/cua-bench.md (new)

```
---
title: CUA-bench
type: benchmark
domains: [computer-use, agents]
tags: [agentic]
as_of: 2026-10-13
sources: [vals-cua-bench-2026-10-13]
---

# CUA-bench

Vals AI's computer-use benchmark built on commercial video games. An agent gets three hours per game with only screen pixels in and keyboard and mouse out: no API, game state, save files or memory inspection. Because the games run in real time, slow decisions cost points as much as wrong ones.

## Current status (as of 2026-10-13)

- **Design.** Six games in genre pairs. Three are public (Minecraft, SUPERHOT, eFootball); each has a held-out partner of the same genre whose name is not published, so a model trained on the named titles would show a public-versus-held-out gap. Each game has an ordered ladder of milestones worth 100 points (Minecraft: log, crafting table, ... enter the Nether); the score is the mean of the six.
- **Results.** Nine models tested; none averages 20 of 100. GPT-6 Astra leads (26.7 public, 11.7 held out), Claude Opus 5.5 scores 14.0 on both halves, and Claude Fable 5.1 shows the widest gap (22.3 vs 4.0). With one trial per cell, Vals treats the gaps as something to watch, not proof of training on the named games.
- **Harness.** Each model runs in its vendor's own CLI agent (Codex, Claude Code, Muse Code, Google's computer-use agent) on a CPU sandbox driving a GPU game desktop over MCP.
- **Grading.** Scores are recomputed afterwards from the game's own saved state or, for the online sports games, from signed screen recordings, not from what the agent reported.
- The tested models predate [GPT-6.2 Astra](../models/gpt-6-2-astra.md) and [Claude Fable 5.2](../models/claude-fable-5-2.md).

## Why it matters

Most computer-use benchmarks hand the agent a DOM, an accessibility tree or an API. CUA-bench measures the raw pixel-and-latency loop that people do without effort, and shows it is far from solved. Vals also expects it to test continuous learning: lessons from winning at an easy level have to turn into timing and reflexes, which do not compress into text the way puzzle lessons do.

## Related

- [OSWorld](osworld.md) — computer-use benchmark on real operating systems, with time to think between actions
- [State of Computer Use](../state-of/computer-use.md)
- [Cua](../tools/cua.md) — unrelated open computer-use stack (trycua) with a similar name

## Recent changes

- [2026-10-13] Page created from Vals's leaderboard: no model above 20 of 100; GPT-6 Astra leads.

## Sources

- [Vals AI — CUA-bench leaderboard and methodology](../sources/articles/vals-cua-bench-2026-10-13.md)
```

### wiki/state-of/computer-use.md (updated)

Frontmatter: append `vals-cua-bench-2026-10-13` to `sources:`; `as_of` stays 2026-11-24.

Insert after the **Knowledge-work OS pattern** paragraph in `### Computer use`:

```
**How far raw computer use still has to go:** on [CUA-bench](../benchmarks/cua-bench.md), where agents play commercial games from pixels, keyboard and mouse in real time, no tested model averages 20 of 100.
```

`## Recent changes` — insert between the 2026-10-14 and 2026-09-30 entries:

```
- [2026-10-13] Vals AI's CUA-bench: real-time play of six commercial games (three held out) from pixels only; no tested model averages 20 of 100.
```

Then remove the oldest entry (`- [2026-05-05] Added knowledge-work OS framing ...`) per the Spill item.

`## Sources` — append:

```
- [Vals AI — CUA-bench leaderboard and methodology](../sources/articles/vals-cua-bench-2026-10-13.md)
```

### wiki/history/state-of/computer-use.md (updated — spill)

Append at the end of the file. The file already ends with a 2026-11-24 archive block; if applied on that date, add the entry to that block instead of opening a new header:

```

## Archived from current page on <apply date>

- [2026-05-05] Added knowledge-work OS framing: left-sidebar desktop app + agentic terminal is emerging as a universal knowledge-work interface pattern; sticky workflow state creates switching costs
```

### wiki/index.md (updated)

Under `## Benchmarks`, after the `benchmarks/osworld` line:

```
- [benchmarks/cua-bench](benchmarks/cua-bench.md) — Vals AI's real-time computer-use benchmark: six commercial games (three held out) played from pixels, keyboard and mouse for three hours; no tested model averages 20 of 100 *(as_of: 2026-10-13)*
```

Page count: `- benchmarks: 15`; `**Total content pages: 312.**`

### wiki/sources/articles/vals-router-index-2026-11-03.md (new)

```
---
title: Vals AI — Vals Router Index
type: source
source_type: article
source_file: raw/articles/2026-11-24-valsai-benchmarks-vals_router_index.md
url: https://www.vals.ai/benchmarks/vals_router_index
published: 2026-11-03
ingested: 2026-11-24
domains: [agents, models]
---

# Vals AI — Vals Router Index

Vals AI's leaderboard comparing six commercial model routers, each at its default settings, with every single model on the Vals Index's eight agentic finance, coding, law and tax benchmarks (about 1,250 tasks). None of the routers sits on the cost-accuracy frontier. Date is the page's last-update stamp (3 November, when Nexus Auto with Sol was added); AINews first reported a five-router version on 2026-10-21.

## Influenced pages
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — new Router Index bullet

## Key claims extracted
- Routers: OpenRouter Auto Router, Fireworks Nexus Auto (Sol pool and Opus pool), Ramp Router, Jev Router (TypeSafe, via OpenRouter), Sakana Fugu Max
- Each router beaten on both score and cost by at least one single model
- Best router: Nexus Auto with Sol 60.0% at $1.25/task; DeepSeek V4.1 Flash 1017 alone 61.3% at $0.66
- Oracle routing within each router's budget: +8 (Ramp) to +27 (Jev Router) points
- Routers appear to run models at lower reasoning effort by default; coding suffers most
- Ramp Router gave the final submit step to GPT-6 Luna in 131/198 Terminal-Bench attempts (25% pass) vs GPT-6.1 Sol (46% pass)
- Fugu Max weakest: about 110 median steps on Terminal-Bench, 45 of 66 tasks failed in all three runs
```

### wiki/sources/articles/vals-claimbench-2026-11-20.md (new)

```
---
title: Vals AI — ClaimBench leaderboard and methodology
type: source
source_type: article
source_file: raw/articles/2026-11-24-valsai-benchmarks-claimbench.md
url: https://www.vals.ai/benchmarks/claimbench
published: 2026-11-20
ingested: 2026-11-24
domains: [models, finance]
---

# Vals AI — ClaimBench leaderboard and methodology

Vals AI's benchmark for whether a decision model can take over checking claims against SEC 10-K filings: 1,960 claims, each labeled supported, contradicted or insufficient evidence against an excerpt. It ranks 30 decision models alone and measures a cascade where each sends low-confidence claims to an LLM. AINews reported an earlier version (Decider V1.2) on 2026-10-21; this page's 20 November numbers replace it.

## Influenced pages
- [Decision models](../../concepts/decision-models.md) — ClaimBench added to the Benchmarks bullet

## Key claims extracted
- Five claim categories of about 392 each: direct support, subtle contradiction, numeric discrepancy, missing evidence, non-supporting citation; gold labels from the construction rule
- Standalone leaders: d1-ultra 100.00%, Decider V1.3 99.80%, d1.2-ultra 99.75%
- Cascade: threshold set for at most 1% errors on 30% of claims, frozen, applied to the other 70%
- Decider V1.3 → Claude Haiku 5.5: 99.85% accuracy, $0.10 per 1,000 claims; Haiku label call alone $1.19
- Decider V1.3 latency 1.7 s per claim vs 5.1 s for Haiku 5.5
- Subtle contradiction is the hardest category (Decider V1.3 99.0%; weakest models about 50%)
```

### wiki/sources/articles/vals-cua-bench-2026-10-13.md (new)

```
---
title: Vals AI — CUA-bench leaderboard and methodology
type: source
source_type: article
source_file: raw/articles/2026-11-24-valsai-benchmarks-cua_bench.md
url: https://www.vals.ai/benchmarks/cua_bench
published: 2026-10-13
ingested: 2026-11-24
domains: [computer-use, agents]
---

# Vals AI — CUA-bench leaderboard and methodology

Vals AI's computer-use benchmark: agents play six commercial games, three named and three held out, for three hours each using only screen pixels, keyboard and mouse. Launched around 2026-09-19 (AINews); the date used is the "updated" stamp on Vals's benchmark list.

## Influenced pages
- [CUA-bench](../../benchmarks/cua-bench.md) — new benchmark page
- [State of Computer Use](../../state-of/computer-use.md) — one-line pointer and Recent-changes entry

## Key claims extracted
- Public games: Minecraft, SUPERHOT, eFootball; each paired with an unnamed held-out game of the same genre
- Per-game ladder of ordered milestones worth 100 points; score is the six-game mean
- Real time: latency counts against the model
- Nine models tested; GPT-6 Astra 26.7 public / 11.7 held out; Claude Opus 5.5 14.0 / 14.0; Claude Fable 5.1 22.3 / 4.0
- One trial per cell; public/held-out gaps are observed, not measured training effects
- Models run in their vendor's own CLI harness, driving a GPU game desktop over MCP
- Grading from native game state or signed recordings, not agent self-reports
```

## Schema / vocabulary additions

None.

## Open questions

- CUA-bench gets its own page here because the wiki has no other real-time computer-use benchmark. Would you rather keep it as a single line on State of Computer Use and the OSWorld page, and skip the new page?
	- Ok, skip it
