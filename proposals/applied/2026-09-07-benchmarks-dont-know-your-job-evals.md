---
type: proposal
source: raw/newsletters/2026-08-25-benchmarks-dont-know-your-job.md
status: pending
created: 2026-09-07
---

# Proposal: "Benchmarks don't know your job" — the case for task-specific evals over leaderboard-chasing

## Summary

### The source

An Every newsletter makes a case that should sharpen this wiki's existing evals guidance rather than introduce a new idea: public benchmarks tell a company that one model is generally more capable than another, but not whether it caught the clause a company's lawyers care about, preserved its house style, or actually saved an employee a round of double-checking. Mercor CEO Brendan Foody and Box CEO Aaron Levie are both quoted arguing that companies spending tens of millions of dollars a year on AI frequently do so without "offline evals" — a fixed set of real internal tasks used to compare models before they touch live work — leaving them unable to say whether they're getting what they paid for. Every's own worked example is instructive precisely because it looks like a success story until you check the mechanism: KateBench, an AI copyeditor trained on ~30,000 of the company's editor-in-chief's past edits and run directly inside Google Docs, showed an apparently strong 85-90% acceptance rate across recent runs — until the engineer who owns it discovered the number was inflated by a silent cap that discarded any suggestion past the 40th on long essays, quietly throwing away good edits before an editor ever saw them, and that the acceptance rate itself is noisy run-to-run because the model doesn't produce identical edits twice. Two new benchmarks cited in the same piece reinforce the caution from different angles: CentaurBench found the model best at completing a task solo often isn't the best at improving a weaker model's first attempt (true on 5 of 7 tasks tested), and Thinkingbox found the strongest coding model's 65% single-attempt pass rate fell to 25% once it had to perform reliably across 20 consecutive attempts.

### What changes

The wiki already has a dedicated page for workflow/task-agent evals built around exactly this "single-shot success rates mislead" thesis (`pass^k`, task-specific metrics per business workflow); this proposal gives that guidance a concrete, current worked example rather than opening new ground.

- **Evals for workflow and task agents** gains its first `## Evidence from practice` section (the page currently jumps straight from guidance to task-specific-metrics tables without one) and its first `## Recent changes` section, since neither existed on the page before. Page date moves to 25 August.
- New source page for the Every newsletter.

### What to weigh

This page (`training/evals-for-agentic-work.md`) predates the wiki's later convention of giving every training page a dated `## Recent changes` section — adding one here for the first time is a light structural change, not just a content addition, so it's worth the reviewer's attention even though it follows the standard template used elsewhere. `concepts/agent-evals.md` covers overlapping ground (benchmark-framing critique, "chart psychosis") but is centered on coding/technical agents; I judged the workflow-agent-specific page a better fit for this business-buying-decision framing and left `agent-evals.md` untouched to keep this a single-page, minimal-scope change.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/training/evals-for-agentic-work.md` — add Evidence from practice and Recent changes sections, bump as_of
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-benchmarks-dont-know-your-job-2026-08-25.md` — source summary
    > See draft below

## Page drafts

### wiki/training/evals-for-agentic-work.md (updated)

> **Frontmatter:** `as_of: 2026-04-23` → `as_of: 2026-08-25`; append `every-benchmarks-dont-know-your-job-2026-08-25` to `sources:` (was `sources: [agents-evals-deep-research]`).

> New section, inserted after `## Simulated users for safe pre-deployment testing` and before `## LLM-as-judge for qualitative dimensions`:

```md
## Evidence from practice

- **Public benchmarks can't answer a buying decision.** Mercor CEO Brendan Foody and Box CEO Aaron Levie both argue companies spending tens of millions of dollars a year on AI frequently do so without offline evals — a fixed set of real internal tasks used to compare models before they touch live work — leaving them unable to say whether a model actually does the job they bought it for, or whether a cheaper model would do it just as well.
- **KateBench: a high acceptance rate that looked finished but wasn't.** Every's internal AI copyeditor (trained on ~30,000 of its editor-in-chief's past edits, run inside Google Docs) showed an apparently strong 85-90% acceptance rate — until the engineer who owns it found the number was inflated by a silent cap that discarded any suggestion past the 40th on long essays, quietly dropping good edits before an editor ever saw them. The acceptance rate is also noisy run-to-run, since the model doesn't produce identical edits twice, so a single high-scoring run doesn't prove improvement.
- **CentaurBench: the best solo performer isn't always the best helper.** On 5 of 7 tasks tested, the model best at completing a task alone was not the model best at improving a weaker model's first attempt — a distinct failure mode from the reliability problem above, relevant whenever an eval setup assumes "the strongest model" is interchangeable across roles.
- **Thinkingbox: reliability collapses under repetition, echoing this page's pass^k thesis with a fresh number.** The strongest coding model tested passed 65% of single attempts, but its success rate fell to 25% when required to perform reliably across 20 consecutive attempts — an independent data point for the same pass@k-vs-pass^k gap this page already documents.
```

> New section, appended at the end of the file after `## Sources`:

```md
## Recent changes

- [2026-08-25] Added Evidence from practice: Mercor/Box CEO case for task-specific offline evals over leaderboard-chasing; KateBench's inflated acceptance rate (silent 40-suggestion cap, run-to-run noise); CentaurBench (best solo model ≠ best helper model, 5/7 tasks); Thinkingbox (65% single-attempt pass rate falls to 25% across 20 consecutive attempts).
```

> **Sources** (append, after the existing single entry):
```md
- [Every — Benchmarks Don't Know Your Job](../sources/newsletters/every-benchmarks-dont-know-your-job-2026-08-25.md)
```

### wiki/sources/newsletters/every-benchmarks-dont-know-your-job-2026-08-25.md (new)

```md
---
title: Benchmarks Don't Know Your Job
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-25-benchmarks-dont-know-your-job.md
url: https://every.to/context-window/benchmarks-don-t-know-your-job
published: 2026-08-25
ingested: 2026-09-07
domains: [agents, training]
---

# Benchmarks Don't Know Your Job

Every's Context Window newsletter arguing companies need task-specific offline evals rather than public-benchmark comparisons to make AI buying decisions, using Every's own KateBench copyeditor as a worked example of a benchmark number that looked finished but wasn't, plus CentaurBench and Thinkingbox findings on reliability and helper-model selection.

## Influenced pages

- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — new Evidence from practice and Recent changes sections

## Key claims extracted

- Mercor CEO Brendan Foody, Box CEO Aaron Levie: companies spend tens of millions on AI without offline evals (fixed real-task comparisons before live deployment)
- KateBench's 85-90% acceptance rate was inflated by a silent 40-suggestion cap that discarded suggestions past that point; acceptance rate is also noisy run-to-run
- CentaurBench: on 5 of 7 tasks, the model best at solo completion wasn't the best at improving a weaker model's first attempt
- Thinkingbox: strongest coding model's 65% single-attempt pass rate fell to 25% across 20 consecutive attempts
- Open-weight token share on Vercel's AI Gateway grew from 28% to 62% in two months (per Guillermo Rauch, cited in this piece)
- Legal-worker Codex adoption grew 108-fold since February (per Andreessen Horowitz "Charts of the Week," cited in this piece)
```

## Open questions

- None beyond the scope note above (agent-evals.md left untouched to keep this a single-page change).
