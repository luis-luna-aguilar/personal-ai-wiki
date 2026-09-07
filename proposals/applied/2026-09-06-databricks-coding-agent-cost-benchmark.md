---
type: proposal
source: raw/newsletters/2026-07-10-gpt-56-beats-fable-5-on-coding.md
status: pending
created: 2026-09-06
---

# Proposal: Databricks' real-PR benchmark — the harness matters as much as the model

## Summary

### The source

Most coding-agent cost comparisons in this wiki are model-vs-model, at the per-token or per-task level. Databricks did something different: they built a private benchmark from real pull requests their own engineers had already completed in a multi-million-line production codebase, then graded agents against the original PR's actual tests — a task set no model has trained on and no vendor can game. Three findings worth having in the wiki. First, open-source GLM 5.2 matched Claude Opus 4.8's quality at roughly 30% lower cost per task. Second, and more surprising: running the *same* model through two different coding harnesses (they compared Claude Code and Pi) can double the cost with no meaningful change in output quality — the difference came down to how much context each harness sent per turn and how many runs it took to finish. Third, sticker prices mislead: in this benchmark, Sonnet 5 cost $2.09 per completed task versus Opus's $1.94, even though Sonnet's per-token rate is lower — because Sonnet took longer and re-read more context to get there. Databricks' closing argument: a team's own merged PRs, with their passing tests, are an eval set no model has seen, and most teams are sitting on this asset unused.

### What changes

- **Cost-aware AI task routing** gains a new "Evidence from practice" bullet citing all three Databricks findings (GLM 5.2/Opus 4.8 parity, harness choice doubling cost, sticker-price-vs-actual-task-cost) plus the "your own merged PRs are an eval set" argument, which extends the page's existing routing guidance from "which model" to "which model *and* which harness, measured per completed task, not per token." Page date moves to 10 July.

### What to weigh

This is one vendor's internal, unaudited benchmark — Databricks' own codebase, own task selection, own grading. The specific numbers (30%, $2.09 vs $1.94, "doubles") are worth having as illustrative evidence of the underlying mechanism (harness and task-completion cost vary independently of sticker price), not as a general ranking of GLM 5.2 vs. Opus 4.8 or Sonnet vs. Opus — the draft attributes every figure to "Databricks' benchmark" rather than stating it as an established fact.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/training/cost-aware-ai-task-routing.md` — add a new "Evidence from practice" bullet citing Databricks' real-PR cost benchmark; bump `as_of`; add new source
    > See draft below

- [x] **Create** `wiki/sources/newsletters/the-code-databricks-coding-benchmark-2026-07-10.md` — source summary (scoped to the Databricks benchmark item only; this issue's main story — GPT-5.6's coding benchmarks and the Entire git-hosting network — is a separate signal not actioned here)

Note. Please include which of Code vs Pi was the cheaper alternative.

## Page drafts

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter — bump `as_of` and add source:

```yaml
as_of: 2026-07-10
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07, the-code-databricks-coding-benchmark-2026-07-10]
```

Add to `## Evidence from practice` (new bullet, appended):

```md
- **Databricks' real-PR coding-agent benchmark.** Databricks built a private benchmark from real pull requests its own engineers had already completed in a multi-million-line production codebase, grading agents against each PR's original tests — a task set no model has trained on. Findings: open-source GLM 5.2 matched Claude Opus 4.8's quality at roughly 30% lower cost per task; running the *same* model through different coding harnesses (Claude Code vs. Pi) can double the cost with no meaningful quality change, driven by how much context each harness sends per turn and how many runs it takes; and per-token sticker prices mislead — in this benchmark Sonnet 5 cost $2.09 per completed task versus Opus's $1.94, despite Sonnet's lower per-token rate, because it took longer and re-read more context. Databricks argues a team's own merged PRs, with passing tests, are an untapped, model-agnostic eval set — the routing lesson extends from "which model" to "which model *and* which harness, measured per completed task."
```

### wiki/sources/newsletters/the-code-databricks-coding-benchmark-2026-07-10.md (new)

```md
---
title: "The Code — Databricks' real-PR coding-agent cost benchmark"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-10-gpt-56-beats-fable-5-on-coding.md
url: https://codenewsletter.ai/p/openai-unveils-gpt-5-6-meta-debuts-its-first-paid-ai-model
published: 2026-07-10
ingested: 2026-09-06
domains: [training, coding]
---

# The Code — Databricks' real-PR coding-agent cost benchmark

The Code's July 10 "Insight" section covers a Databricks benchmark built from real pull requests completed in Databricks' own multi-million-line codebase, graded against the original PRs' tests. This source page covers only that item; the issue's main story (GPT-5.6's coding benchmarks) and the Entire git-hosting-network item are separate signals handled elsewhere.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — added a new evidence bullet citing all three findings

## Key claims extracted

- Databricks graded coding agents on real PRs from its own codebase using the original PR's tests as the grader — a private, uncontaminated benchmark
- Open-source GLM 5.2 performed as well as Claude Opus 4.8 while costing about 30% less per task
- The same model run through different harnesses (Claude Code vs. Pi) can double the cost with no meaningful quality change; the efficient harness sent less context per turn and needed fewer runs
- In this benchmark, Sonnet 5 cost $2.09 per completed task and Opus 4.8 cost $1.94, despite Sonnet's lower per-token pricing, because Sonnet took longer and re-read more context
- Databricks argues teams' own merged PRs (with passing tests) are an untapped, model-agnostic eval source; the post outlines a method: pick the right PRs, rewrite their intent into prompts, hold out the tests for scoring
