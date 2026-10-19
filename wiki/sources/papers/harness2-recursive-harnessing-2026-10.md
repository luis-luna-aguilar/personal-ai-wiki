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
- [Automated harness optimization](../../concepts/automated-harness-optimization.md) — "Recursive harnessing without ground truth" section and Current-status bullet (page created by splitting Agent improvement loop and Harness)
- [Harness²](../../tools/harness2.md) — new tool page
- [State of Agents](../../state-of/agents.md) — leader line under Agent frameworks

## Key claims extracted
- Recursive agent harnessing = task-level recursion (refine the execution harness) + harnessing-level recursion (update the improvement harness/library)
- Contrastive Propose–Probe–Compose works without ground-truth verifiers; contrasts guide composition, they don't verify correctness
- Invariant vs domain-scoped edits; eight file-mounted harness components (extends AHE's decomposition by one)
- One step improves all 3 benchmarks × 4 configs; up to +11.5 WorkBuddy, +4.5 JobBench, +11.8 pp LAB Partial
- Gains do not require a stronger editor model
- Code: Apache 2.0, OpenCode and Codex executors, parallel and sequential modes; "not an officially supported Google product"
