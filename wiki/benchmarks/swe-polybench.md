---
title: SWE-PolyBench
type: benchmark
domains: [coding]
tags: []
as_of: 2026-04-23
sources: [amazon-swe-polybench, legacy-ai-tools-roadmap-xlsx, agents-evals-deep-research]
---

# SWE-PolyBench

SWE-PolyBench is a software engineering benchmark from Amazon Science that expands beyond narrow single-language issue-fix evaluation. The key reason it matters in this wiki is that it pushes coding-agent evaluation closer to the multilingual, messier, more varied reality of practical engineering work.

## Current status (as of 2026-04-23)

- 2,110 real-world repository instances across Java, JavaScript, TypeScript, and Python
- Evaluates using two methods: traditional execution-based tests and Concrete Syntax Tree (CST) node-retrieval metrics; the CST metrics expose limitations in how well models navigate non-Python syntax structures
- Directly addresses SWE-bench's Python-only limitation; designed to expose multi-language capability gaps in frontier models
- Published by Amazon Science

## Why it matters

- Better stress-tests claims about general software engineering capability
- Helps separate narrow benchmark optimization from broader coding usefulness

## Sources

- [[sources/articles/amazon-swe-polybench]]
- [[sources/notes/legacy-ai-tools-roadmap-xlsx]]
- [[sources/deep-research/2026-04-23-agents-evals]]
