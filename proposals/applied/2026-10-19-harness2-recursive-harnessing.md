---
type: proposal
source: raw/papers/2026-10-19-arxivorg-html-261014224.md
status: pending
created: 2026-10-19
---

# Proposal: Harness² — Recursive Agent Harnessing for an Open World (Google Cloud AI Research)

## Summary

### In short
You can improve an agent's harness on a brand-new task without an answer key or a stronger model. Try two scoped edits, one fixing general habits and one adding field knowledge, re-run the same task, and keep only the edits whose runs behaved better. The improvement process itself can also learn: saved lessons make later edits better. Google Cloud AI Research's Harness² gained on every benchmark and setup tested, with frozen model weights, by up to 11.5 points. Adds a section to **Agent improvement loop** and a pointer on **Harness (agent)**. Hesitate because both pages are already over their length limits.

[[#Open questions|Open questions: 3 to answer.]]

### The source
On 9 October 2026, Google Cloud AI Research and Northwestern University published the Harness² paper and open-sourced its code. Methods that automatically improve an agent's harness (its prompts, memory, skills, tools and subagents) usually score each change against training tasks with known answers. Real work brings new tasks with no answer key.

Harness² improves the harness one task at a time and needs no answers. The agent does the task once. An editor model then writes two edited harnesses: one fixes general habits such as planning or checking its own output, and the other adds know-how for the task's field. Both run on the same task. The editor keeps only the edits whose runs behaved better than the first run. After each task, the winning harness and a note of lessons go into a library that guides later tasks. In the main example, adding a "trace your inputs, reopen your outputs" rule and a domain skill raised one task's score from 43.1 to 77.8.

Model weights never change. One round raised scores on all three benchmarks (office, job and legal work) in all four model and harness setups. The biggest gain was GLM-5 on WorkBuddy-Bench, from 64.2 to 75.7. Gains held when a model edited its own harness. The authors flag two limits: each round costs extra runs, and comparing behaviour isn't the same as checking answers.

### What changes
The wiki's improvement-loop page describes harness hill-climbing that needs an eval set (LangChain's Better-Harness), and the harness page lists self-modifying harnesses. Neither covers improving the harness one task at a time with no answer key.

- **Agent improvement loop** gains a Current-status bullet and a "Recursive harnessing without ground truth" section after Better-Harness, covering the propose-probe-compose round, the lessons library and the results, plus a Recent-changes line. Page date moves to 9 October.
- **Harness (agent)** gains a one-line pointer in its self-modifying harnesses list. Its Recent-changes list is full, so the oldest entry (14 July) moves to history. Page date moves to 9 October.
- **Index** updates both lines.
- New paper source page `sources/papers/harness2-recursive-harnessing-2026-10.md`, written as a plain-language explainer.

### What to weigh
Both pages are already over their length limits, the harness page by about three times. This adds about 310 words to one page and one line to the other, and the open questions offer splits. You linked the GitHub repo. I ingested the paper behind it as the fuller source and folded the README's extra details (license, network-access warning) into the same source page.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/agent-improvement-loop.md` — new section after "Better-Harness", one Recent-changes entry dated 2026-10-09 (list goes 8→9, no spill), source id + link, `as_of` → 2026-10-09

- [ ] **Update** `wiki/concepts/harness.md` — one bullet in "Self-modifying and recursive harnesses", one Recent-changes entry dated 2026-10-09, source id + link, `as_of` → 2026-10-09

- [ ] **Spill** `wiki/concepts/harness.md` → `wiki/history/concepts/harness.md` — the oldest Recent-changes entry ([2026-07-14]) falls off the 10-entry cap

- [ ] **Update** `wiki/index.md` — both concept lines: as_of → 2026-10-09; improvement-loop description gains "label-free per-task recursive harnessing"

- [ ] **Create** `wiki/sources/papers/harness2-recursive-harnessing-2026-10.md` — paper source summary (repo README at `raw/repos/google-research-harness2.md` noted as companion)

## Page drafts

### wiki/concepts/agent-improvement-loop.md (updated)

Frontmatter: append `harness2-recursive-harnessing-2026-10` to `sources:`; `as_of: 2026-10-09`.

`## Current status (as of 2026-07-29)` → `## Current status (as of 2026-10-09)`; append one bullet:

```
- **Label-free per-task refinement (October 2026):** Google Cloud AI Research's Harness² improves a frozen model's harness on each new task without an answer key, keeping only edits a behaviour comparison supports — see the section below
```

New section, inserted directly after `## Better-Harness: autonomous harness hill-climbing`:

```
## Recursive harnessing without ground truth

Better-Harness needs a scored eval set. Google Cloud AI Research's Harness² (paper and open-source code, October 2026) runs the loop inside each new task with no answer key, keeping model weights fixed:

1. **Reference run** — the agent does the task with its current harness.
2. **Propose** — an editor model writes two edited harnesses: an *invariant* one fixing general agent habits (planning, tool use, delegation, checking its own output) and a *domain* one adding the field's knowledge and procedures. The editable parts are files: system prompt, guardrails, memory, skills, tool guidance, scripts, subagents, and a middleware plugin.
3. **Probe** — both run on the same task under the same model and environment. Comparing their behaviour with the reference run shows whether an edit fixed the targeted weakness, changed nothing, or broke something. It does not show whether the answer is correct.
4. **Compose** — the editor merges, revises, or drops edits, tying each decision to an observed difference, and the combined harness produces the deliverable.
5. **Reflect** — the adopted harness and an `EXPERIENCE.md` of evidence-backed lessons go into a library. Later tasks start from the base harness and reuse library parts selectively, not wholesale.

The budget scales two ways: *parallel* (k candidates per scope, k compositions) or *sequential* (k chained rounds). Reported results: one round raised scores on WorkBuddy-Bench, JobBench, and Harvey's LAB legal benchmark in all four model–harness setups. GLM-5 under OpenCode went from 64.2 to 75.7 on WorkBuddy-Bench, and Gemini 3.5 Flash from 72.4 to 77.5. Gains held when each model edited its own harness, from GLM-5 to Claude Opus 5. Removing the library, the two editor scopes, or the compose step each cost 1.6–3.7 points. Editing without reference runs, probes, or library made things worse (WorkBuddy Code 73.4→63.2). The authors' caveats: each round costs extra runs, and behaviour comparisons inherit run-to-run noise and the model's own blind spots.
```

`## Recent changes` — adds one entry at the top (list goes 8→9; no spill):

```
- [2026-10-09] Added Harness² (Google Cloud AI Research): label-free per-task harness refinement via propose-probe-compose, plus a lessons library carried across tasks; up to +11.5 points on WorkBuddy-Bench with frozen weights.
```

`## Sources` — append:

```
- [Harness²: Recursive Agent Harnessing for an Open World — Google Cloud AI Research](../sources/papers/harness2-recursive-harnessing-2026-10.md)
```

### wiki/concepts/harness.md (updated)

Frontmatter: append `harness2-recursive-harnessing-2026-10` to `sources:`; `as_of: 2026-10-09`.

`### Self-modifying and recursive harnesses` — append one bullet after the "Self-modifying, persistent harnesses" bullet:

```
- **Per-task harness refinement without an answer key.** Google Cloud AI Research's open-source Harness² edits a frozen model's harness files for each new task, tests the edits against an unedited run, keeps only edits the behaviour comparison supports, and carries lessons forward in a library. See [Agent improvement loop](agent-improvement-loop.md#recursive-harnessing-without-ground-truth).
```

`## Recent changes` — adds one entry at the top; spills the oldest (`[2026-07-14] Added the Lilian Weng 2023-vs-2026 essay contrast…`) to history:

```
- [2026-10-09] Added Harness² as a per-task, label-free self-refining harness (details on Agent improvement loop).
```

`## Sources` — append:

```
- [Harness²: Recursive Agent Harnessing for an Open World — Google Cloud AI Research](../sources/papers/harness2-recursive-harnessing-2026-10.md)
```

### wiki/history/concepts/harness.md (updated)

Append (create the file if missing; add the archive header if opening a new block):

```
## Archived from current page on <apply date>

- [2026-07-14] Added the Lilian Weng 2023-vs-2026 essay contrast and Anthropic's "grown, not designed" framing, from AI Engineer World's Fair 2026 coverage.
```

### wiki/index.md (updated)

```
- [concepts/agent-improvement-loop](concepts/agent-improvement-loop.md) — workflow for improving AI agents through traces, evals, autoresearch loops, Better-Harness-style hill-climbing, label-free per-task recursive harnessing (Harness²), trace-to-memory feedback, and production feedback *(as_of: 2026-10-09)*
- [concepts/harness](concepts/harness.md) — scaffolding around an acting model: prompts, tools, recipes, orchestration, environment, evals, controls, security boundaries, managed-agent primitives, and live-run recovery *(as_of: 2026-10-09)*
```

### wiki/sources/papers/harness2-recursive-harnessing-2026-10.md (new)

```
---
title: 'Harness²: Recursive Agent Harnessing for an Open World — Google Cloud AI Research'
type: source
source_type: paper
source_file: raw/papers/2026-10-19-arxivorg-html-261014224.md
url: https://arxiv.org/abs/2610.14224
published: 2026-10-09
ingested: 2026-10-19
domains: [agents]
---

# Harness²: Recursive Agent Harnessing for an Open World — Google Cloud AI Research

Paper (arXiv 2610.14224, Xu, Chen, … Lee, Pfister; Google Cloud AI Research and Northwestern) with an Apache-2.0 code release at github.com/google-research/harness2 (README saved at `raw/repos/google-research-harness2.md`).

## The problem in plain words

An agent is a model plus a harness: the prompt, memory, skills, tools, and helpers around it. Tuning the harness by hand is slow, so researchers automate it. Most automated methods score each harness change against training tasks with known answers and then ship the best harness. Real work brings tasks nobody prepared answers for, and a harness tuned for last week's tasks may not fit. Harness² asks whether an agent can improve its harness on the task in front of it with no answer key, and get better at improving harnesses as it goes.

## How it works

- **Two harnesses.** The *execution harness* does the work. The *improvement harness* holds the editor's instructions and a library of past lessons.
- **One round (Propose → Probe → Compose).** Run the task once as a reference. An editor model writes two edited harnesses: one for general agent habits (planning, tool use, delegation, self-checking) and one for the field's knowledge and procedures. Run both on the same task. Compare how each behaved against the reference: did the targeted weakness go away, did nothing change, did something break? Merge only edits the comparison supports, then run the merged harness for the final deliverable.
- **More budget.** *Parallel* tries k candidates per scope and makes k merges, and a selector picks the best deliverable blind. *Sequential* chains k rounds, each building on the last.
- **Learning across tasks.** After each task, a reflector saves the adopted harness plus an `EXPERIENCE.md` (when it applies, what worked, the evidence) to the library. A lesson is saved only when the run comparison supports it. The next task starts from the base harness and pulls from the library selectively.
- **Eight editable parts**, each a file: system prompt, guardrails, memory, skills, tool guidance, scripts, subagents, middleware plugin.

## Example

On a JobBench memo task (Gemini 3.5 Flash, OpenCode), the baseline scored 43.1. It never reconciled figures across source files and never reopened its own outputs. The general edit added a guardrail: list every input, trace each figure to its source, and run a script that reopens and checks produced files. The domain edit added a reconciliation skill for schedule, venue, labour and budget files, plus number-format tool guidance. The composer kept all four edits, and the re-run scored 77.8.

## Why this is useful for our projects

The pattern carries over to any agent setup without labels: run, change one scoped thing, re-run the same task, and compare behaviour rather than trusting a score. Keep a lessons file only for changes the comparison actually supports. Splitting edits into "general agent habit" and "domain know-how" worked better than two generic editors when the authors removed one piece of the method at a time.

## Reported results

- Benchmarks: WorkBuddy-Bench (office, web, code), JobBench (long professional tasks), Harvey's LAB (legal; per-criterion pass rate). Means of three runs with shuffled task order.
- One round (k=1) improved every benchmark in all four setups (Gemini 3.5 Flash or GLM-5 × OpenCode or Codex). WorkBuddy averages: GLM-5/OpenCode 64.2→75.7, Gemini/OpenCode 72.4→77.5, Gemini/Codex 74.5→77.5, GLM-5/Codex 64.4→75.3. Up to +4.5 on JobBench and +11.8 points on LAB.
- Parallel recursion at k=5 added up to 3.9 (WorkBuddy), 4.2 (JobBench), and 6.7 points (LAB).
- Baselines: ReasoningBank (retrieved strategies), Meta-Harness (offline harness search on a training split), Harness Scaling (per-task revision without memory). Harness² beat all of them on WorkBuddy averages in all four setups, and in seven of eight JobBench/LAB cells. Meta-Harness led on Gemini/Codex LAB (76.5 vs 75.6).
- Ablations (Gemini/OpenCode, k=1): no library −3.1/−1.8 (WorkBuddy/JobBench), no scoped editors −2.9/−3.7, no composition −1.6/−1.9.
- Editing without reference runs, probes, or library dropped WorkBuddy Code from 73.4 to 63.2 and Web from 69.9 to 65.0. A library built at k=5 helped later one-round edits by 0.9–5.1 points. A library built on JobBench raised one-round WorkBuddy scores by 0.5–2.9 points.
- Same model as executor and editor (k=2): all five models tested, GLM-5 through Claude Opus 5, improved on every benchmark. Opus 5 gained 3.3/5.5/3.0; GLM-5 gained 13.7 on LAB. The default editor elsewhere is Claude Opus 4.8.

## Limits

- Every round adds executions and editor sessions; the paper tests only a small range of budgets.
- Behaviour comparisons are not correctness checks. They pick up run-to-run noise and blind spots shared by the editor and executor models, and adoption does not prove an edit transfers.
- The library is a simple index. The paper does not test consolidating it or retiring stale lessons.
- Executors run with unrestricted network access and the Codex sandbox off. Users must block access to public benchmark rubrics themselves.
- The cross-task library-transfer test is retrospective, not online adaptation.

## Influenced pages
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — new "Recursive harnessing without ground truth" section
- [Harness (agent)](../../concepts/harness.md) — pointer bullet in self-modifying harnesses

## Key claims extracted
- Recursive agent harnessing = task-level recursion (refine the execution harness) + harnessing-level recursion (update the improvement harness/library)
- Contrastive Propose–Probe–Compose works without ground-truth verifiers; contrasts guide composition, they don't verify correctness
- Invariant vs domain-scoped edits; eight file-mounted harness components (extends AHE's decomposition by one)
- One step improves all 3 benchmarks × 4 configs; up to +11.5 WorkBuddy, +4.5 JobBench, +11.8 pp LAB Partial
- Gains do not require a stronger editor model
- Code: Apache 2.0, OpenCode and Codex executors, parallel and sequential modes; "not an officially supported Google product"
```

## Schema / vocabulary additions
None.

## Open questions
- Should Harness² get its own `tools/` page? Assumed no: it is a research framework, not a product people deploy, and the concept section covers it.
	- Put it into tools as its own page, because its a tool by google.
- **Agent improvement loop** will be about 1,700 body words, over the 1,200-word concept ceiling. Its harness-optimization sections (Better-Harness, Harness², self-improving skills) could move to a new `concepts/automated-harness-optimization.md`, leaving pointers behind. Split now or later?
	- Split now if still necessary (if another proposal has not split it yet)
- **Harness (agent)** is about 3,550 body words, roughly three times its ceiling, before this change. Its "Self-modifying and recursive harnesses" and "Context-engineering and self-evolving harness research" sections are the natural next split, and could go to the same new page.
	- Split now if still necessary (if another proposal has not split it yet)
