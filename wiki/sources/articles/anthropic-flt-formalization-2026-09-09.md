---
title: Formalizing Fermat's Last Theorem
type: source
source_type: article
source_file: raw/articles/2026-09-09-anthropiccom-research-formalizing-fermats-last-theorem.md
url: https://www.anthropic.com/research/formalizing-fermats-last-theorem
ingested: 2026-09-09
domains: [science]
---

# Formalizing Fermat's Last Theorem

Anthropic's account of the first complete, computer-checked (Lean) proof of Fermat's Last Theorem — a formalization of Andrew Wiles's 1995 proof, produced largely autonomously by an internal research model over 11 days via the Prove2Me collaborative-formalization platform. No publish-date byline is shown on the live page; the proof itself completed 2026-08-18 per an in-page quoted timestamp from the model's own reasoning log, and the post was very likely published shortly after, but no explicit date was found.

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — new Current-status entry, framed as the verification-side answer to Tao's "proof indigestion" concern

## Key claims extracted

- First complete, computer-checked proof of Fermat's Last Theorem, in Lean
- Completed 2026-08-18 (per an in-page quoted timestamp), 11 days of largely-autonomous work
- Model: "a general-purpose internal research model roughly comparable to Claude Fable 5.1" (not confirmed to be Fable 5.1 itself)
- ~6 billion output tokens; 13 million lines of Lean code; 29,500 intermediate theorems proved
- Proof is >5x the size of Mathlib, the community's own proof library
- Uses only Lean's 3 standard axioms; matches Mathlib's own FLT statement per an independent comparator tool
- Kevin Buzzard (led a community FLT-formalization effort since 2024) reviewed and endorsed the proof as "extraordinary"
- ~7% of the final proof's non-boilerplate lines came from earlier failed attempts, before the project switched to the Prove2Me platform
- Prove2Me: open collaborative formalization platform (Peng et al., arXiv:2608.28433) maintaining a DAG of theorem statements to coordinate agents and avoid duplicate work
