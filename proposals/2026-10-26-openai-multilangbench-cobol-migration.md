---
type: proposal
source: raw/articles/2026-10-26-openaicom-index-low-resource-programming-languages.md
status: pending
created: 2026-10-26
---

# Proposal: OpenAI MultiLangBench and COBOL migration eval

## Summary

### In short
Frontier models are now good at code in languages with little training data, which used to be a weak spot. That makes migrating legacy COBOL a realistic job for a model, with tests as the safety net. OpenAI reports GPT-6 Astra at 87.4% on its new open MultiLangBench (GPT-5.6 Sol: 26.8%) and GPT-6.1 Sol at 86.6% to 97.9% on a COBOL-migration eval, up from 5.4%. The proposal creates a `benchmarks/multilangbench.md` page and updates **GPT-6 Astra** and **Acceptance contracts and test oracles**. One reason to hesitate is scope: GPT-6 Luna and GPT-6.1 Sol have no pages of their own, so their numbers live on the benchmark page.

[[#Open questions|Open questions: none.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 19 October 2026 OpenAI published a research post on coding in "low-resource" programming languages. These are languages like COBOL, Fortran and Visual Basic, which have far less public code and documentation to learn from than Python or JavaScript. They still run a lot of critical systems: the post says COBOL is behind more than 40% of online banking systems and 95% of ATM transactions. Customers had told OpenAI that coding models struggle with these languages.

OpenAI built two evaluations. MultiLangBench asks a model to build a SQLite-compatible database engine from scratch in each of 20 languages, over a long coding session. Database files act as a shared interface, so tests adapted from SQLite's own suite can grade every language the same way. GPT-6 Astra averages 87.4% of tests passed and is above 83% in 19 of the 20 languages. COBOL is still the hardest at 72.1%, up from 10.9%. The cheaper GPT-6 Luna reaches 40.3% for about $0.77 a sample, against $3.48 for GPT-5.6 Sol. OpenAI's chart puts GPT-6.1 Sol at 87.0%, close behind Astra. The setup and test suite are on GitHub.

The second eval migrates COBOL programs to C++, Java, Kotlin, Python or Rust. Hidden tests require the migrated program's outputs to match the original byte for byte, and a migration counts only if every test passes. The post's example of what goes wrong: COBOL's fixed-point arithmetic drops extra decimal digits unless told to round, so a rewrite that rounds runs without errors and still produces different financial results. GPT-6.1 Sol scores 86.6% at low reasoning effort, against 5.4% for GPT-5.6 Sol at 61% of the cost, and 97.9% at higher effort, close to saturating the eval. OpenAI adds that production migrations still need expert review and testing against the system's business rules.

### What changes
The wiki has only one COBOL mention: a COBOL-to-Java migration example on the forward-deployed-engineering page. Its benchmarks cover multilingual coding only through SWE-PolyBench's four languages.

- New page `benchmarks/multilangbench.md`. It covers the build-from-scratch design and the per-model pass rates, and has a short section on the companion COBOL migration eval.
- **GPT-6 Astra** gains a current-status bullet with both results and one Recent-changes entry dated 19 October. The list goes from 4 to 5 entries, nothing spills, and the page date stays 19 October.
- **Acceptance contracts and test oracles** gets the COBOL eval as a worked example under differential tests, including the rounding trap. It gains one Recent-changes entry and a Related link, and its date stays 19 October.
- The **Index** gains the benchmark page (benchmarks 12 → 13, total 248) and an updated GPT-6 Astra line.
- One new source page.

### What to weigh
The main call is scope. State of Coding has no benchmark section, and State of Finance tracks finance products rather than core-banking modernization, so neither changes. The COBOL eval stays inside the MultiLangBench page because it has no public release or name of its own.

## Intended changes

- [ ] **Create** `wiki/benchmarks/multilangbench.md` — new benchmark page (MultiLangBench plus the companion COBOL migration eval)
- [ ] **Update** `wiki/models/gpt-6-astra.md` — add current-status bullet on MultiLangBench and COBOL migration; adds one Recent-changes entry dated 2026-10-19 (4 → 5, no spill); merges source id into `sources:` and link into `## Sources`; `as_of` unchanged (2026-10-19)
- [ ] **Update** `wiki/training/acceptance-contracts-and-test-oracles.md` — extend the differential-tests bullet with the COBOL migration example; adds one Recent-changes entry dated 2026-10-19 (3 → 4, no spill); adds one Related line; merges source id and link; `as_of` unchanged (2026-10-19)
- [ ] **Update** `wiki/index.md` — add MultiLangBench under Benchmarks; refresh GPT-6 Astra description; benchmarks count 12 → 13, total 247 → 248
- [ ] **Create** `wiki/sources/articles/openai-low-resource-programming-languages-2026-10-19.md` — source summary

## Page drafts

### wiki/benchmarks/multilangbench.md (new)

```
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
- Average pass rate at max reasoning effort (OpenAI's chart): [GPT-6 Astra](../models/gpt-6-astra.md) 87.4%, GPT-6.1 Sol 87.0%, GPT-6 Sol 57.7%, GPT-6 Luna 40.3%, GPT-5.6 Terra 37.9%, [GPT-5.6 Sol](../models/gpt-5-6-sol.md) 26.8%, [GPT-5.5](../models/gpt-5-5.md) 25.8%, GPT-5.4 17.4%. Only OpenAI models are reported.
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
```

### wiki/models/gpt-6-astra.md (updated)

Frontmatter (merge, do not replace):

```
sources: [...existing..., openai-low-resource-programming-languages-2026-10-19]
```

In `## Current status (as of 2026-10-19)`, append after the "Codebase maintenance in Codex" bullet:

```
- **Low-resource languages (OpenAI evals):** 87.4% average test pass rate on [MultiLangBench](../benchmarks/multilangbench.md), building a SQLite-compatible engine in 20 languages (GPT-5.6 Sol: 26.8%); COBOL is its weakest language at 72.1%. On OpenAI's companion COBOL-migration eval, GPT-6.1 Sol reaches 86.6% at low effort and 97.9% at higher effort (GPT-5.6 Sol: 5.4%).
```

In `## Recent changes`, insert as the newest entry (above the existing 2026-10-19 entry):

```
- [2026-10-19] OpenAI published MultiLangBench (Astra 87.4% across 20 languages, up from 26.8% for GPT-5.6 Sol) and a COBOL-migration eval on which GPT-6.1 Sol reaches 97.9% at higher effort.
```

In `## Sources`, append:

```
- [OpenAI — Advancing coding in low-resource programming languages](../sources/articles/openai-low-resource-programming-languages-2026-10-19.md)
```

### wiki/training/acceptance-contracts-and-test-oracles.md (updated)

Frontmatter (merge, do not replace):

```
sources: [...existing..., openai-low-resource-programming-languages-2026-10-19]
```

In `## Oracles agents can't game`, replace the differential-tests bullet:

```
- **Differential tests** run old vs new, or yours vs a reference, on the same input. For migrations this is the main oracle: OpenAI's COBOL-migration eval requires byte-for-byte parity of outputs between the COBOL original and the rewrite on hidden tests, and passes a migration only if every test passes. It catches changes a reviewer would miss: COBOL drops extra decimal digits unless told to round, so a rewrite that rounds runs cleanly and still gets the money wrong ([MultiLangBench](../benchmarks/multilangbench.md)).
```

In `## Recent changes`, insert in date order (above the 2026-10-14 entry):

```
- [2026-10-19] Added OpenAI's COBOL-migration eval as a differential-test example: byte-for-byte output parity on hidden tests, all tests must pass.
```

In `## Related`, append:

```
- [MultiLangBench](../benchmarks/multilangbench.md) — OpenAI's multi-language build benchmark and COBOL-migration eval
```

In `## Sources`, append:

```
- [OpenAI — Advancing coding in low-resource programming languages](../sources/articles/openai-low-resource-programming-languages-2026-10-19.md)
```

### wiki/index.md (updated)

Under `## Benchmarks`, append:

```
- [benchmarks/multilangbench](benchmarks/multilangbench.md) — OpenAI's build-a-SQLite-engine benchmark across 20 languages incl. COBOL/Fortran/VB (Astra 87.4%), plus a COBOL-migration eval with byte-for-byte parity (GPT-6.1 Sol 97.9%) *(as_of: 2026-10-19)*
```

Replace the GPT-6 Astra line:

```
- [models/gpt-6-astra](models/gpt-6-astra.md) — OpenAI's new flagship, launched 2026-09-03; mixed third-party benchmark reception vs. Fable 5.1 but far more token-efficient; 87.4% on MultiLangBench; system card discloses a sharp CoT-monitorability decline *(as_of: 2026-10-19)*
```

In `## Page count`: `- benchmarks: 13` and `**Total content pages: 248.**`

### wiki/sources/articles/openai-low-resource-programming-languages-2026-10-19.md (new)

```
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
```

## Schema / vocabulary additions

None.

## Open questions

None.
