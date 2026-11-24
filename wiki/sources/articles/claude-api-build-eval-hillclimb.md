---
title: Anthropic — Automating eval design and hillclimbing with Claude
type: source
source_type: article
source_file: raw/articles/2026-10-26-claudedev-blog-automating-eval-design-and-hillclimbing.md
url: https://claude.dev/blog/automating-eval-design-and-hillclimbing/
ingested: 2026-10-26
domains: [agents, coding]
---

# Anthropic — Automating eval design and hillclimbing with Claude

Anthropic's claude.dev post on eval-design and hill-climbing guidance added to the claude-api skill in Claude Code. `/claude-api build-eval` builds an eval in the user's codebase: it samples cases from production first, validates the grader with the user, and runs noise, plumbing and headroom checks. `/claude-api hillclimb` improves a prompt, skill, model choice or harness one patch at a time, with a held-out split to catch overfitting. Two worked examples: a support-ticket cost climb and the claude-api skill's own eval. No publication date in the post; ingest date used (it uses Sonnet 5, not 5.5, suggesting late September 2026).

## Influenced pages

- [Evals for workflow and task agents](../../training/evals-for-agentic-work.md) — eval-design checks, case sampling, grader validation, support-ticket example
- [Automated harness optimization](../../concepts/automated-harness-optimization.md) — the hillclimb loop and its overfitting guards
- [Agent skill methodology](../../training/agent-skill-methodology.md) — training priors overriding skill content

## Key claims extracted

- Four elements of a good eval: tasks mirror production; stronger models and more effort score higher; "passable" headroom at the frontier (not from impossible/ambiguous tasks); low run-to-run variance (including environment leftovers)
- Adversarial sampling: choosing cases today's model fails samples its capability valleys; pick cases a human can explain as hard; user traffic can skew easy
- build-eval input order: production transcripts (after retention/sensitivity questions), bug reports/tickets, 5–10 hand-written, codebase-synthesized; review page before proceeding
- Grader: cheapest that fits; programmatic when outputs are constrained; otherwise LLM judge, different model from the one tested, rubric as checkable claims, blind random-order comparison against a baseline when one exists
- Diagnostics: grader run twice on identical output; timeouts/API errors/truncation; warn when baseline ≥ ~95%
- Hillclimb: random train/test split; noise must be below the smallest actionable gain; one root-cause patch per round; keep only if train and test both improve; revert on train-only gain or any regression; after 2–3 stalled rounds, sort failures by cause; finish on the best test-set version; recommend against merging gains within noise
- Overfitting guards: split cases, never paste failures into the prompt, keep answers structurally out of reach
- Support example: 44 tickets (30 search / 14 held out); Opus 4.8 high 74.4% at 4.6¢ → Opus 5.5 low 87.8% at 1.9¢ → Sonnet 5 low 88.9% at 1¢ → improved prompt 98.9% at 1¢; held-out 90.5% vs 78.6% at ~1/5 the cost; Opus 5.5 tokens 20% cheaper than Opus 4.8, cache reads 60% cheaper
- claude-api skill eval: 66.1% → 74% (eight missing features) → 77% (C#/Java type tables) → 80% (remembered-to-current API table) → ~88% (fixed a mis-specified task and a grader contradicting the docs)
