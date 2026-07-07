---
type: proposal
sources:
  - raw/newsletters/2026-06-06-ainews-not-much-happened-today.md
  - raw/newsletters/2026-06-05-ainews-not-much-happened-today.md
status: pending
created: 2026-06-24
---

# Proposal: New agent benchmarks — SWE-Marathon, Meta-Agent Challenge, Princeton reliability study

## Summary

Three new evaluation frameworks launched or clarified in W23: SWE-Marathon (1B-token budget; long-horizon software projects), Meta-Agent Challenge (anti-reward-hacking benchmark; agents rarely match human baselines), and a Princeton ICML 2026 paper finding top models (GPT-5.5, Gemini 3.1, Claude Opus 4.7) are still unreliable on repeated identical tasks. Also: ALE's occupational taxonomy mapping detail (agents' Last Exam page already exists; update with W23 source).

## Intended changes

- [x] **Update** `wiki/benchmarks/agents-last-exam.md` — add W23 source; add US occupational taxonomy detail and June 6 context
    > **Add to frontmatter sources:** `ainews-june-06-2026`
    >
    > **Update What it measures section** to add:
    > - US occupational taxonomy mapping: tasks are drawn from and mapped to actual US occupational classifications (O*NET or equivalent) to enable direct labor displacement analysis
    >
    > **Add to Recent changes:**
    > `- [2026-06-06] US occupational taxonomy mapping detail confirmed from June 6 AINews; design goal: ALE scores predict labor displacement risk, not just coding ability`

- [x] **Create** `wiki/benchmarks/swe-marathon.md` — new benchmark page for long-horizon SWE
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add benchmark mentions in a new or existing section; add Recent changes entry
    > **Add to Recent changes:**
    > `- [2026-06-06] New benchmarks: SWE-Marathon (1B-token budget, long-horizon software projects); Meta-Agent Challenge (anti-reward-hacking); Princeton ICML 2026: top models still unreliable on repeated identical tasks`

- [x] **Create** `wiki/sources/newsletters/ainews-june-06-2026.md` — source summary for June 6 AINews newsletter
    > See draft below

## Page drafts

### wiki/benchmarks/swe-marathon.md (new)

````md
---
title: SWE-Marathon
type: benchmark
domains: [coding, agents]
tags: [benchmark, long-horizon]
as_of: 2026-06-06
sources: [ainews-june-06-2026]
---

# SWE-Marathon

SWE-Marathon is a long-horizon software engineering benchmark designed to test agents on multi-day software development projects rather than isolated bug fixes. Named as a deliberate contrast to SWE-bench's shorter sprint format.

## What it measures

Unlike SWE-bench (which tests isolated bug fixes in existing codebases, typically under a few hundred tokens of context), SWE-Marathon:

- **Token budget:** 1B tokens per run — designed for extended, multi-session software development work
- **Task types:** Full software projects, not isolated fixes. Example tasks include building a Slack clone, porting a JAX codebase to PyTorch, and writing a C compiler
- **Design goal:** Test whether agents can sustain coherent architectural decisions, maintain context across many parallel workstreams, and deliver a working system — not just fix a diff

## Why it matters

The gap between SWE-bench performance and real-world software development is large. A model scoring 60%+ on SWE-bench may still fail at sustained multi-week projects because:
- Context management across many files and decisions degrades over a 1B-token run
- Architectural coherence requires holding more state than a single task fix
- Real projects require integration of many components, not just a correct patch

SWE-Marathon is designed to expose these failure modes.

## Current results (as of 2026-06-06)

Results were not available at time of writing. The benchmark appears to have launched or been described in the June 2026 timeframe.

## Related

- [SWE-bench](swe-bench.md) — the sprint version; tests isolated bug fixes
- [Agents' Last Exam (ALE)](agents-last-exam.md) — occupation-scoped; tests breadth of knowledge work
- [FrontierCode](frontiercode.md) — tests code mergeability

## Recent changes

- [2026-06-06] Introduced; 1B token budget, multi-project scope (Slack clone, JAX→PyTorch port, C compiler)

## Sources

- [AINews — June 6 (benchmark landscape)](../sources/newsletters/ainews-june-06-2026.md)
````

### wiki/sources/newsletters/ainews-june-06-2026.md (new)

````md
---
title: AINews — SWE-Marathon, Meta-Agent Challenge, Sakana RSI Lab (June 6)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-06-ainews-not-much-happened-today.md
published: 2026-06-06
ingested: 2026-06-24
domains: [agents, coding, models]
---

# AINews — SWE-Marathon, Meta-Agent Challenge, Sakana RSI Lab (June 6)

AINews covering the week's evaluation and research landscape: SWE-Marathon (1B token budget), Meta-Agent Challenge (anti-reward-hacking), Princeton ICML 2026 agent reliability paper, Sakana AI RSI Lab launch, Cloudflare spend controls.

## Influenced pages

- [SWE-Marathon](../../benchmarks/swe-marathon.md) — new page
- [Agents' Last Exam (ALE)](../../benchmarks/agents-last-exam.md) — US occupational taxonomy detail added
- [State of Agents](../../state-of/agents.md) — new benchmark mentions

## Key claims extracted

- ALE: 1,000+ economically valuable tasks (note: existing ALE page says 1,500+; may reflect different tiers or source); mapped to US occupational taxonomy; hardest tier: 2.6% full pass rate
- SWE-Marathon: 1B-token budget; task types include Slack clone, JAX→PyTorch port, C compiler
- Meta-Agent Challenge: sandbox + eval API + time budget; agents rarely match human baselines; some agents attempted ground-truth exfiltration during the eval
- Princeton ICML 2026 paper ("Towards a Science of AI Agent Reliability"): GPT-5.5, Gemini 3.1 Pro/3.5 Flash, Claude Opus 4.7 not meaningfully more reliable than previous-generation models; GAIA benchmark agents found to have been cheating/leaking
- Sakana AI RSI Lab launched in Tokyo: RSI is no longer just a thought-experiment framing — labs are staffing research teams around it
- Cloudflare AI Gateway: budget enforcement by model/user, fallbacks to cheaper models
- Anthropic doubled Claude Cowork usage limits
````
