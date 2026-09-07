---
title: AI in mathematics
type: trend
domains: [science]
tags: []
as_of: 2026-08-11
sources: [openai-erdos-unit-distance-2026-05, anthropic-riemann-hypothesis-2026-08-11]
---

# AI in mathematics

Split out from [AI in Science](ai-in-science.md) because pure-mathematics results now form a distinct, fast-moving cluster of their own: general-purpose frontier reasoning models (not math-specialized systems) are producing results on long-standing open problems, verified or partially verified by professional mathematicians, alongside a parallel track of dedicated math tooling (research workbenches, formal-verification/proof-checking systems). The throughline across both tracks is that intelligence applied to mathematics is starting to look less like a benchmark exercise and more like actual research contribution — with real caveats about verification, disclosure, and how much credit belongs to the base model versus the surrounding harness.

## Current status (as of 2026-08-11)

- **OpenAI disproves the Erdős planar unit-distance conjecture (2026-05-20):** an internal OpenAI general-purpose reasoning model — explicitly not a math-specialized or scaffolded system — disproved the planar unit-distance conjecture Paul Erdős posed in 1946, producing an infinite family of constructions beating the long-assumed "square grid" upper bound (later refined by Princeton's Will Sawin to δ = 0.014). The proof was checked by external mathematicians (Noga Alon, Tim Gowers, Arul Shankar, Jacob Tsimerman), who co-authored a companion paper; Gowers called it "a milestone in AI mathematics... I would have recommended acceptance without any hesitation" for the Annals of Mathematics. OpenAI frames it as the first time AI has autonomously solved a prominent open problem central to a subfield of mathematics, while explicitly cautioning that "expertise becomes more valuable, not less" since humans still choose problems and interpret results. OpenAI discloses no model name, version, run duration, or cost — the "<32 hours / <$1,000 / GPT-5.6" figures that circulated in secondary coverage are unverified speculation, not an OpenAI claim.
- **Anthropic reports a Riemann Hypothesis bound improvement (2026-08-11):** an unreleased internal research Claude variant, tasked with the Riemann Hypothesis, did not solve the conjecture but improved a longstanding lower bound — the proven share of non-trivial zeta-function zeros known to lie on the critical line rose from 41.6% to 67.2% — reached via large-scale retries and exploration over roughly 31M output tokens rather than a single clean derivation. Engineers and outside commentators (including mathematician @jdlichtman) characterized it as theorem-search progress, not conjecture resolution, and it is not yet independently verified by outside mathematicians the way the Erdős result was.
- **Dedicated math tooling is building in parallel:** [State of Science](../state-of/science.md) tracks two supporting signals — Google DeepMind's **AI Co-Mathematician**, an asynchronous research workbench scoring 48% on FrontierMath Tier 4, and **[Axiom Math](../tools/axiom-math.md)**, a formal-verification startup (12/12 Putnam 2025, 99% ProofGen) built on the thesis that machine-checkable proofs are a scalable RL reward signal. Both are narrower, more instrumented efforts than the two headline results above, but point at the same trend from the tooling side.

## Why it matters

The Erdős and Riemann results share a pattern worth watching: both come from *general-purpose* reasoning models rather than math-specialized systems, both rely on massive inference-time search/retries rather than a single insight, and both are disclosed by the lab itself with varying degrees of independent verification (Erdős: fully verified and co-published with mathematicians; Riemann: not yet). That verification gap is the load-bearing caveat for this whole trend — a lab's own announcement is not the same evidentiary weight as a peer-reviewed or externally reproduced result, and this page should keep tracking which is which as more results land.

## Recent changes

- [2026-09-07] Split out of [AI in Science](ai-in-science.md) into its own page, at the user's request, once pure-math signals (Erdős, Riemann Hypothesis) accumulated enough weight to warrant separate tracking from the page's broader biology/materials/self-driving-lab focus.
- [2026-08-13] Unconfirmed: a tweet from mathematician Steven Strogatz reported that a neurosurgery resident used ChatGPT 5.6 to solve an open numerical-linear-algebra problem; no name, paper, or institutional confirmation exists yet. Not added to Current status pending verification.
- [2026-08-11] Anthropic reported an unreleased research Claude variant improved a Riemann Hypothesis-related bound (41.6% → 67.2% of zeta zeros proven on the critical line), via ~31M output tokens of retries/exploration; not yet independently verified.
- [2026-05-20] OpenAI's general-purpose reasoning model disproved the 1946 Erdős planar unit-distance conjecture, verified by external mathematicians with a companion paper — the first pure-math signal in this cluster.

## Sources

- [OpenAI model disproves the Erdős planar unit-distance conjecture](../sources/articles/openai-erdos-unit-distance-2026-05.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
