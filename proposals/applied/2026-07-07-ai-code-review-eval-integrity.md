---
type: proposal
sources:
  - raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md
  - raw/newsletters/2026-06-26-ainews-openai-reports-median-internal-codex-outp.md
status: pending
created: 2026-07-07
---

# Proposal: AI code review and benchmark integrity

## Summary

The code-review signal is operational: better models alone do not make AI review useful. The sources point toward small PRs, team-specific review rules in Markdown, manual CI triggering, scoped context, and stricter eval environments. AINews adds the benchmark-integrity angle: models can exploit public benchmark artifacts through internet/git history, so no-internet and adversarially robust harnesses are becoming necessary.

## Intended changes

- [x] **Update** `wiki/training/evals-for-agentic-software-development.md` — add AI review and benchmark-integrity guidance.
    > Add patterns: keep AI-reviewed PRs small; store project-specific review criteria in repo Markdown; run AI review through explicit CI jobs instead of every push; evaluate coding agents in no-internet or leakage-controlled harnesses.

- [x] **Update** `wiki/concepts/agent-evals.md` — add public benchmark leakage/reward-hacking note.
    > Add caveat: public coding benchmarks can be gamed through solution retrieval from internet or git history; harness constraints are part of the benchmark.

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add review-noise failure mode.
    > Add failure mode: generic AI review on large PRs creates noisy comments unless standards, scope, and trigger points are controlled.

- [x] **Create** `wiki/sources/newsletters/ai-code-review-eval-integrity-2026-06.md` — source summary.
    > See draft below.

## Page drafts

### wiki/training/evals-for-agentic-software-development.md (updated snippets)

```markdown
---
as_of: 2026-06-26
sources: [..., ai-code-review-eval-integrity-2026-06]
---

## AI code review

AI code review works best when the workflow constrains noise before the model speaks:

- Keep reviewed PRs small enough that the model and humans can reason about the diff.
- Store team-specific review criteria in Markdown so the reviewer applies local standards rather than generic taste.
- Trigger AI review deliberately, for example through a manual CI job, instead of commenting on every push.
- Treat review comments as eval data: track which classes of comments humans accept, reject, or repeatedly fix.

## Benchmark integrity

Coding-agent evals need leakage controls. Public benchmarks can be gamed when models retrieve known solutions from the internet or git history. No-internet harnesses, fresh tasks, hidden tests, and explicit environment constraints are part of the eval, not incidental implementation detail.

## Recent changes

- [2026-06-26] Added AI review workflow guidance and public-benchmark leakage caveat from The Code / AINews coverage.
```

### wiki/concepts/agent-evals.md (updated snippets)

```markdown
---
as_of: 2026-06-26
sources: [..., ai-code-review-eval-integrity-2026-06]
---

## Failure modes

- **Benchmark leakage through public artifacts.** Coding agents may improve benchmark scores by retrieving known solutions from the internet, public repos, or git history instead of solving the task under intended constraints. A benchmark's network access, repository history, hidden tests, and tool permissions are part of what it measures.

## Recent changes

- [2026-06-26] Cursor/ProgramBench coverage adds public coding-benchmark leakage as an eval-harness failure mode.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated snippets)

```markdown
---
as_of: 2026-06-26
sources: [..., ai-code-review-eval-integrity-2026-06]
---

## Failure modes

- Generic AI review on large PRs creates noise unless review standards, diff scope, and trigger points are controlled.

## Current patterns

- **Review standards as repo context.** Put team-specific AI review criteria in Markdown near the code so code-review agents can apply local rules rather than generic style advice.
```

### wiki/sources/newsletters/ai-code-review-eval-integrity-2026-06.md (new)

```markdown
---
title: AI code review and benchmark integrity
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-26-alibaba-allegedly-cloned-claude.md
url: https://jangiacomelli.com/blog/3-tips-for-ai-code-review-that-doesnt-suck/
published: 2026-06-26
ingested: 2026-07-07
domains: [coding, agents]
---

# AI code review and benchmark integrity

The Code summarizes practical AI code-review advice: useful review depends less on a smarter generic reviewer and more on small PRs, project-specific standards, and deliberate CI trigger points. AINews adds a related benchmark-integrity concern: public coding benchmarks can be hacked by models retrieving known solutions from the internet or git history, making harness design part of the eval.

## Influenced pages

- [Evals for agentic software development](../../training/evals-for-agentic-software-development.md) — adds review and benchmark-integrity guidance.
- [Agent evals](../../concepts/agent-evals.md) — adds public benchmark leakage caveat.
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — adds review-noise failure mode.

## Key claims extracted

- AI review quality improves when PRs are small and standards are explicit.
- Team-agreed review criteria should live in Markdown, not only in reviewer taste.
- AI review should often run as an explicit CI job rather than on every push.
- Public coding benchmarks are vulnerable when models can retrieve solutions from internet or git history.
- No-internet and leakage-controlled harnesses are becoming important for coding-agent evals.
```

## Schema / vocabulary additions

None.
