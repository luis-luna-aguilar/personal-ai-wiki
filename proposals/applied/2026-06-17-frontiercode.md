---
type: proposal
source: raw/newsletters/2026-06-09-ainews-frontiercode-benchmarking-for-code-quali.md
status: pending
created: 2026-06-17
---

# Proposal: FrontierCode benchmark

## Summary

Cognition (makers of Devin) launched FrontierCode on June 9, a new coding benchmark targeting whether code is actually *mergeable* into production rather than just passing unit tests. Built with open-source maintainers (40+ hours per task), it revealed that the best pre-Fable model scored only ~13% on the hardest Diamond tier — far below SWE-bench numbers — before Fable 5 brought it to 29.3%. Needs a new benchmark page and minor state-of/coding update.

## Intended changes

- [x] **Create** `wiki/benchmarks/frontiercode.md` — new benchmark page
    > See draft below

- [x] **Update** `wiki/state-of/coding.md` — add FrontierCode reference to the Claude Code terminal coding agent entry
    > **Before (Claude Code entry):** `- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: \`/goal\` autonomous loops, Agent View multi-session supervision, and dynamic workflows (\`ultracode\`); Claude Code + Fable 5 [max] scored 77 on the DeepSWE index — the current top score — though Fable 5 is suspended under export controls; Claude Code + Opus 4.7 remains the accessible Anthropic stack *(as of 2026-06-17)*`
    > **After:** append ` FrontierCode Diamond: Fable 5 29.3% (prior best 13.4%); benchmark targets mergeable code quality, not test-passing` before the `*(as of …)*` close

- [x] **Create** `wiki/sources/newsletters/ainews-frontiercode-june-2026.md` — source summary
    > See draft below

## Page drafts

### wiki/benchmarks/frontiercode.md (new)

```md
---
title: FrontierCode
type: benchmark
domains: [coding]
tags: [cognition, benchmark]
as_of: 2026-06-09
sources: [ainews-frontiercode-june-2026, ainews-fable5-june-2026]
---

# FrontierCode

FrontierCode is a coding benchmark released by Cognition (makers of Devin) in June 2026 that targets whether code is actually *mergeable* into a real production codebase — not just whether it passes unit tests. It was explicitly inspired by FrontierMath's approach of using saturation-resistant hard problems.

## What it measures

Standard coding benchmarks (SWE-bench-Verified, SWE-bench Pro) evaluate whether an agent's patch passes test suites. METR separately found that many SWE-bench-passing PRs would not actually be merged by maintainers. FrontierCode directly addresses this gap.

Evaluation dimensions per task:
- Regression safety
- Code cleanliness
- Scope adherence
- Test correctness
- Maintainability

Tasks were built in collaboration with open-source maintainers; each task took 40+ hours to construct. Benchmark design explicitly modeled on FrontierMath — focusing the hardest tier on problems that remain far from saturated.

## Tiers

FrontierCode has at least three tiers. The hardest public tier is **Diamond**.

## Current leaderboard (as of 2026-06-09)

| Model | FrontierCode Diamond |
|---|---|
| Claude Mythos 5 | 30.9% |
| Claude Fable 5 | 29.3% |
| Claude Opus 4.8 (prior best) | ~13.4% |

Pre-Fable 5: the best available model scored ~13.4% — well below the 50%+ scores common on SWE-bench-style evals. The gap signals that standard benchmarks overstate production-readiness.

## Why it matters

FrontierCode recalibrates what "good coding performance" means. A model that scores 80% on SWE-Bench Pro may still only produce mergeable code ~30% of the time on hard Diamond-tier tasks. This benchmark is now cited by Cognition and adopted by Anthropic as a primary launch benchmark for Fable 5.

The benchmark also serves as a feedback loop: Cognition integrates FrontierCode results into Devin's development, and good benchmarks are becoming training data targets rather than just static scoreboards.

## Recent changes

- [2026-06-09] Launched; Opus 4.8 scored ~13.4% on Diamond tier
- [2026-06-10] Fable 5 launched with 29.3% Diamond, Mythos 5 at 30.9%

## Sources

- [AINews — FrontierCode launch (June 9)](../sources/newsletters/ainews-frontiercode-june-2026.md)
- [AINews — Fable 5 FrontierCode Diamond score (June 10)](../sources/newsletters/ainews-fable5-june-2026.md)
```

### wiki/sources/newsletters/ainews-frontiercode-june-2026.md (new)

```md
---
title: "AINews — FrontierCode: Benchmarking for Code Quality over Slop (June 9)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-09-ainews-frontiercode-benchmarking-for-code-quali.md
published: 2026-06-09
ingested: 2026-06-17
domains: [coding, agents]
---

# AINews — FrontierCode: Benchmarking for Code Quality over Slop (June 9)

AINews (Latent Space) coverage of FrontierCode launch, Kimi Code/Work releases, Agent Arena launch, and coding agent workflow signals. AINews editors were personally involved in FrontierCode's creation.

## Influenced pages
- [FrontierCode](../../benchmarks/frontiercode.md) — benchmark page created
- [State of Coding](../../state-of/coding.md) — FrontierCode reference added
- [Kimi Code](../../tools/kimi-code.md) — tool page created

## Key claims extracted
- FrontierCode (Cognition): benchmark for mergeable code quality; 40+ hours per task; built with open-source maintainers
- Evaluation dimensions: regression safety, cleanliness, scope adherence, test correctness, maintainability
- Pre-Fable best (Opus 4.8): ~13.4% on hardest Diamond tier
- METR separately found many SWE-bench-passing PRs would not be merged
- Kimi Code: open-source coding agent update; 1-line CLI; video-as-context; ACP support; plugins; IDE integration
- Kimi Work: desktop agent; 300 local sub-agents; browser-use; finance tools; persistent memory
- Agent Arena: leaderboard from 1M+ real-world sessions; causal tracing across 5 signals
```
