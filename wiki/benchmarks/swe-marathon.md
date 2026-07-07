---
title: SWE-Marathon
type: benchmark
domains: [coding, agents]
tags: []
as_of: 2026-06-06
sources: [ainews-june-06-2026]
---

# SWE-Marathon

SWE-Marathon is a long-horizon software engineering benchmark designed to test agents on multi-day software development projects rather than isolated bug fixes. Named as a deliberate contrast to SWE-bench's shorter sprint format.

## What it measures

Unlike SWE-bench, which tests isolated bug fixes in existing codebases, SWE-Marathon tests extended software projects:

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

- [2026-06-06] Introduced; 1B token budget, multi-project scope (Slack clone, JAX -> PyTorch port, C compiler)

## Sources

- [AINews — June 6 (benchmark landscape)](../sources/newsletters/ainews-june-06-2026.md)
