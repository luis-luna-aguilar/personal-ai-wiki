---
title: MultiLangBench
type: benchmark
domains: [coding, models]
tags: [openai, open-source]
as_of: 2026-10-19
sources: [openai-low-resource-programming-languages-2026-10-19]
---

# MultiLangBench

OpenAI's benchmark for building software in many programming languages, including low-resource ones (languages with little public code or documentation, such as COBOL, Fortran and Visual Basic). A model must build a SQLite-compatible database engine from scratch in a given language over an extended coding session: organize the codebase, manage state, handle errors, and add features without breaking existing ones. The setup and test suite are public on GitHub, with per-language results.

## Current status (as of 2026-10-19)

- 20 languages: C, C#, C++, COBOL, Common Lisp, Fortran, Go, Java, JavaScript, Lean, OCaml, PHP, PowerShell, Python, Ruby, Rust, Scala, Swift, Visual Basic, Zig.
- Grading uses database files as a shared interface: the candidate program takes an initial database and a SQL query and writes a modified database, which is checked against the reference SQLite. Tests are adapted from SQLite's own suite, so every language gets the same tests. Reports test pass rate and API cost.
- Average pass rate at max reasoning effort (OpenAI's chart): [GPT-6 Astra](../models/gpt-6-astra.md) 87.4%, [GPT-6.1 Sol](../models/gpt-6-1-sol.md) 87.0%, GPT-6 Sol 57.7%, [GPT-6 Luna](../models/gpt-6-luna.md) 40.3%, GPT-5.6 Terra 37.9%, GPT-5.6 Sol 26.8%, [GPT-5.5](../models/gpt-5-5.md) 25.8%, GPT-5.4 17.4%. Only OpenAI models are reported.
- Astra clears 83% in 19 of 20 languages; COBOL stays hardest at 72.1% (GPT-5.6 Sol: 10.9%). GPT-6 Luna improves on GPT-5.6 Sol in every language at ~$0.77 vs $3.48 per sample (~78% cheaper).

## Companion eval: COBOL migration

Published alongside MultiLangBench, not released separately. Models migrate COBOL programs to C++, Java, Kotlin, Python or Rust. Hidden tests require byte-for-byte parity on observable outputs, and a migration counts only if every test passes. This catches COBOL-specific behaviour a rewrite can silently change: fixed-point arithmetic drops extra decimal digits unless rounding is requested, so a rewrite that rounds runs cleanly and still gets financial results wrong. GPT-6.1 Sol: 86.6% at low effort (GPT-5.6 Sol 5.4%, at 61% of Sol 5.6's cost) and 97.9% at higher effort, near saturation. OpenAI notes production migrations still need expert review and testing against business rules.

## Why it matters

- One of the few benchmarks aimed at low-resource languages that run banking, payments, weather and nuclear-safety software
- Build-from-scratch (MultiLangBench) and preserve-behaviour (migration) test complementary skills; issue-fix benchmarks like [SWE-bench](swe-bench.md) and [SWE-PolyBench](swe-polybench.md) test neither

## Related

- [Acceptance contracts and test oracles](../training/acceptance-contracts-and-test-oracles.md) — the migration eval is a differential-test oracle at scale
- [Forward-deployed engineering](../training/forward-deployed-engineering.md) — a COBOL-to-Java customer migration in practice

## Sources

- [OpenAI — Advancing coding in low-resource programming languages](../sources/articles/openai-low-resource-programming-languages-2026-10-19.md)
