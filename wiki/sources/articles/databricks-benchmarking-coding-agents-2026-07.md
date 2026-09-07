---
title: "Databricks — Benchmarking coding agents on our multi-million line codebase"
type: source
source_type: article
source_file: raw/articles/2026-09-06-databrickscom-blog-benchmarking-coding-agents-databricks-mul.md
url: https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase
published: 2026-07-08
ingested: 2026-09-06
domains: [training, coding]
---

# Databricks — Benchmarking coding agents on our multi-million line codebase

Databricks' own primary post describing an internal benchmark built from real coding tasks their engineers already completed in Databricks' multi-million-line production codebase, graded against each task's actual held-out tests. Fetched directly to confirm a detail The Code's newsletter recap (see the companion source page) left unspecified: which harness was cheaper when the same model was run through more than one.

## Influenced pages

- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — confirms and sharpens the harness-choice finding already added from the newsletter recap

## Key claims extracted

- Models and harnesses clustered into 3 capability tiers on this benchmark; specific point differences within a tier can even out in real-world tasks
- Open-source GLM 5.2 matched Claude Opus 4.8's quality at roughly 30% lower cost per task
- Running the same model at the same thinking effort through Claude Code/Codex vs. Pi produced more than a 2x cost difference at equal quality; Pi sent about 3x less context per turn, kept a tighter working set, and finished in fewer runs — "in many cases, simple harnesses like Pi performed best on our workloads"
- Databricks is explicit that the lesson isn't "one harness is always cheaper" — model choice is only one piece of the puzzle, and harness/model swapping should stay flexible (they cite their own investment in Omnigent, a meta-harness, for this reason)
- Sonnet 5 cost $2.09 per completed task vs. Opus 4.8's $1.94, despite Sonnet's lower per-token rate, because it took longer and re-read more context
- Correctness was graded by patching in the held-out tests, not an LLM judge, "since we've found that this rewards sounding right over being right"
- Databricks argues any team's backlog of merged PRs is an unused benchmark already graded by tests the team wrote; they plan to keep running new agents/harnesses through it
