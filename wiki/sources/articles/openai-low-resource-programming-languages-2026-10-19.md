---
title: OpenAI — Advancing coding in low-resource programming languages
type: source
source_type: article
source_file: raw/articles/2026-10-26-openaicom-index-low-resource-programming-languages.md
url: https://openai.com/index/low-resource-programming-languages/
published: 2026-10-19
ingested: 2026-10-26
domains: [coding, models]
---

# OpenAI — Advancing coding in low-resource programming languages

OpenAI research post introducing two evaluations for languages with little public training data. MultiLangBench has a model build a SQLite-compatible database engine from scratch in 20 languages, graded by tests adapted from SQLite's suite via database files as a shared interface; the setup and tests are on GitHub. The COBOL migration eval has a model port COBOL programs to C++, Java, Kotlin, Python or Rust with byte-for-byte output parity on hidden tests. GPT-6 Astra and GPT-6.1 Sol show large gains over GPT-5.6 Sol on both, at lower cost.

## Influenced pages

- [MultiLangBench](../../benchmarks/multilangbench.md) — new benchmark page, including the COBOL migration eval
- [GPT-6 Astra](../../models/gpt-6-astra.md) — MultiLangBench and COBOL-migration results
- [Acceptance contracts and test oracles](../../training/acceptance-contracts-and-test-oracles.md) — differential-test example for migrations

## Key claims extracted

- COBOL supports 40%+ of online banking systems, 80% of in-person card transactions, 95% of ATM transactions; Fortran is used in weather forecasting and nuclear reactor safety analysis
- MultiLangBench (max effort): GPT-6 Astra 87.4% average across 20 languages vs 26.8% for GPT-5.6 Sol; above 83% in 19 of 20; COBOL 10.9% → 72.1%, OCaml 25.6% → 85.8%, Fortran 21.4% → 83.5%, Visual Basic 27.5% → 89.4%
- Chart: GPT-6.1 Sol 87.04%, GPT-6 Sol 57.66%, GPT-6 Luna 40.31%, GPT-5.6 Terra 37.92%, GPT-5.5 25.81%, GPT-5.4 17.42%
- GPT-6 Luna 40.3% at ~$0.77/sample vs $3.48 for GPT-5.6 Sol (~78% lower)
- COBOL migration: hidden tests, byte-for-byte parity on observable outputs, success only if all tests pass; GPT-6.1 Sol 86.6% at low effort vs 5.4% for GPT-5.6 Sol at 61% of the cost; 97.9% at higher effort
- Production migration still requires expert review and testing against business rules and dependencies
