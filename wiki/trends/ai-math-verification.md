---
title: AI math verification
type: trend
domains: [science]
tags: []
as_of: 2026-09-09
sources: [every-our-agents-ourselves-2026-08-30, anthropic-flt-formalization-2026-09-09]
---

# AI math verification

Split out from [AI in mathematics](ai-in-mathematics.md) because checking, formalizing and digesting AI-produced proofs is becoming a track of its own. As models produce apparently-correct proofs faster than mathematicians can referee them, the bottleneck moves from finding proofs to verifying and understanding them. This page covers that side: machine-checked formalization, the human work of extracting a proof's core idea, and the dedicated tooling built around both. The claimed results themselves (Erdős, Riemann, Navier-Stokes, OpenAI's 722-manuscript release) stay on AI in mathematics.

## Current status (as of 2026-09-09)

- **Terence Tao names a verification bottleneck: "proof indigestion" (2026-08-12):** Tao describes AI systems now producing more apparently-correct proofs than mathematicians can verify or explain. His worked example: an AI-generated, Lean-formalized proof of Sendov's conjecture (a longstanding polynomial-roots problem) that machine-verified across all 90,000 lines but was barely comprehensible to a human. Tao spent several days extracting the core idea with AI assistance into a ~15,000-line version he calls "remarkably elementary" for a problem that had resisted experts for decades. His framing: turning an AI-generated proof into something a human can understand, explain, and build on — not finding the proof — may become mathematics' primary human task going forward. Distinct from the Erdős and Riemann results on [AI in mathematics](ai-in-mathematics.md): this is not a new result, but a new bottleneck in how results get consumed.
- **Anthropic produces the first complete computer-checked proof of Fermat's Last Theorem (2026-08-18):** Unlike the Erdős and Riemann results on [AI in mathematics](ai-in-mathematics.md), this is not new mathematics — Andrew Wiles proved FLT in 1995 — but a *formalization*: converting Wiles's proof into Lean, a language a computer can verify step-by-step, directly answering Tao's "proof indigestion" concern above by making a landmark proof machine-checkable rather than producing another one that needs digesting. Anthropic researcher Tianyi Peng's team set a general-purpose internal research model — described as "roughly comparable to Claude Fable 5.1," not Fable 5.1 itself — loose on the problem; working largely autonomously with a multi-agent Claude Code-based harness over 11 days (about six billion output tokens), it produced 13 million lines of Lean code and proved 29,500 intermediate theorems, more than 5x the size of Mathlib, the community's own proof library. Kevin Buzzard, who has led a multi-year community effort toward the same goal since 2024, called it "extraordinary" and confirmed the proof uses only Lean's three standard axioms and matches Mathlib's own statement of FLT via an independent comparator tool. The project succeeded once switched to Prove2Me, an open collaborative formalization platform (Peng et al., arXiv:2608.28433) that maintains a DAG of theorem statements agents use to pick next targets and avoid memory-degradation-driven duplicate work — roughly 7% of the final proof's non-boilerplate lines came from earlier failed attempts before this shift. Buzzard: autoformalization "artefacts are now robust enough to be built upon," a step toward catching errors across the existing mathematical corpus and easing the referee burden on AI-generated results going forward.
- **Dedicated math tooling is building in parallel:** [State of Science](../state-of/science.md) tracks two supporting signals — Google DeepMind's **AI Co-Mathematician**, an asynchronous research workbench scoring 48% on FrontierMath Tier 4, and **[Axiom Math](../tools/axiom-math.md)**, a formal-verification startup (12/12 Putnam 2025, 99% ProofGen) built on the thesis that machine-checkable proofs are a scalable RL reward signal. Both are narrower, more instrumented efforts than the headline results on [AI in mathematics](ai-in-mathematics.md), but point at the same trend from the tooling side.

## Recent changes

- [2026-11-23] Page split out from [AI in mathematics](ai-in-mathematics.md): Tao's "proof indigestion", Anthropic's Fermat's Last Theorem formalization, and dedicated math tooling moved here.
- [2026-09-09] Anthropic reports the first complete computer-checked (Lean) proof of Fermat's Last Theorem — a formalization of Wiles's existing 1995 proof, not new mathematics — completed 2026-08-18 by a Fable-5.1-class internal model working largely autonomously over 11 days via the Prove2Me collaborative-formalization platform; framed as the verification-side answer to Tao's "proof indigestion" concern tracked above.
- [2026-08-12] Terence Tao names "proof indigestion": AI-generated proofs (his worked example: a 90,000-line Lean-verified proof of Sendov's conjecture) are outpacing the field's capacity to extract and communicate their reasoning, not just to generate results.

## Sources

- [Every — Our Agents, Ourselves](../sources/newsletters/every-our-agents-ourselves-2026-08-30.md)
- [Formalizing Fermat's Last Theorem](../sources/articles/anthropic-flt-formalization-2026-09-09.md)
