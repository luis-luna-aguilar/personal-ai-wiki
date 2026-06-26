---
type: proposal
source: raw/newsletters/2026-06-03-scaling-past-informal-ai-carina-hong-axiom-mat.md
status: pending
created: 2026-06-24
---

# Proposal: Axiom Math — formal verification AI reaches Putnam level

## Summary

Axiom Math (Carina Hong, CEO; 7-month-old startup) disclosed results: solved all 12 Putnam 2025 problems; 99% on ProofGen (Verina codegen benchmark) vs OpenAI o3's 4.9%. Their thesis: formal verification creates a machine-checkable RL reward signal, enabling compounding improvements. Raised $200M Series A at $1.6B valuation. AXLE is their open-source interactive Lean application toolkit.

## Intended changes

- [x] **Create** `wiki/tools/axiom-math.md` — new tool page
    > See draft below

- [x] **Update** `wiki/state-of/science.md` — add formal verification / math reasoning subcategory; add Axiom Math entry; add Recent changes entry
    > **Add new subcategory section:**
    >
    > ### Formal verification and theorem proving
    >
    > AI systems that generate or verify formal mathematical proofs, providing machine-checkable correctness signals for RL training.
    >
    > - [Axiom Math](../tools/axiom-math.md) — 7-month-old startup; 12/12 Putnam 2025; 99% ProofGen (Verina) vs o3 at 4.9%; AXLE open-source interactive Lean toolkit; $200M Series A / $1.6B valuation; thesis: verifiable proofs = scalable RL reward signal *(as of 2026-06-03)*
    >
    > **Add to Recent changes:**
    > `- [2026-06-03] Added formal verification subcategory; Axiom Math: 12/12 Putnam 2025, 99% ProofGen vs o3's 4.9%; AXLE open-source Lean toolkit; $200M / $1.6B; thesis: formal verification = scalable RL reward signal`

- [x] **Create** `wiki/sources/newsletters/axiom-math-june-2026.md` — source summary
    > See draft below

## Schema / vocabulary additions

- [x] Add new subcategory `formal-verification` to `wiki/_schema/subcategories.md` — needed for Axiom Math tool page

## Page drafts

### wiki/tools/axiom-math.md (new)

````md
---
title: Axiom Math
type: tool
domains: [science]
subcategory: formal-verification
tags: [closed-source]
as_of: 2026-06-03
sources: [axiom-math-june-2026]
---

# Axiom Math

Axiom Math is a 7-month-old AI startup focused on formal mathematical reasoning. Their system generates machine-verified proofs using interactive Lean environments, creating a compounding RL reward signal. June 2026 results: solved all 12 Putnam 2025 competition problems; 99% on ProofGen (Verina benchmark) vs OpenAI o3's 4.9%.

## Current status (as of 2026-06-03)

- **Results:**
  - 12/12 Putnam 2025 problems solved
  - 99% (187/189) on ProofGen within the Verina codegen benchmark — OpenAI o3 scores 4.9% on the same
- **AXLE:** open-source interactive Lean applications toolkit; the interface layer for building with formal proofs
- **Business:** $200M Series A; $1.6B valuation; CEO Carina Hong
- 7 months old at time of writing

## Core thesis

Formal verification (Lean proofs) provides a machine-checkable ground-truth reward signal for RL training. Unlike natural-language math or code execution, a Lean proof is either valid or invalid — no ambiguity, no reward hacking. Carina Hong's framing: "Anything that can be specified can be proven. Humans are bad at specifying everything we want."

The Ramanujan analogy: just as Ramanujan's mathematical intuitions were extraordinary but unverified, AI models can generate brilliant mathematical intuitions that become trustworthy only when formalized into machine-verifiable proofs. Formal verification is the mechanism for "compounding brilliance."

## Strengths

- Machine-verifiable reward signal is immune to the reward hacking problems that plague natural-language RL
- AXLE is open-source — lower barrier for researchers to build on Lean environments
- Putnam and Verina results are independently checkable

## Weaknesses / caveats

- Very early company; most evidence is from founder interviews, not third-party replication
- The gap between Putnam-level theorem proving and real-world scientific discovery is large
- "Anything that can be specified" is an optimistic framing — many important problems resist formal specification

## Recent changes

- [2026-06-03] Introduced via Latent Space/Carina Hong podcast; initial results disclosed

## Sources

- [Axiom Math — Latent Space podcast with Carina Hong (June 3)](../../sources/newsletters/axiom-math-june-2026.md)
````

### wiki/sources/newsletters/axiom-math-june-2026.md (new)

````md
---
title: '"Scaling Past Informal AI" — Carina Hong / Axiom Math on Latent Space (June 3)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-03-scaling-past-informal-ai-carina-hong-axiom-mat.md
published: 2026-06-03
ingested: 2026-06-24
domains: [science]
---

# "Scaling Past Informal AI" — Carina Hong / Axiom Math on Latent Space (June 3)

Latent Space podcast/newsletter with Carina Hong (CEO, Axiom Math). Covers Axiom's approach to formal mathematical reasoning using interactive Lean environments, the thesis that verifiable proofs are the missing RL reward signal for scaling mathematical AI, and early benchmark results.

## Influenced pages

- [Axiom Math](../../tools/axiom-math.md) — new page
- [State of Science](../../state-of/science.md) — new subcategory and entry

## Key claims extracted

- 12/12 Putnam 2025 problems solved
- 99% (187/189) ProofGen on Verina codegen benchmark; OpenAI o3 scores 4.9%
- AXLE: open-source interactive Lean toolkit
- Thesis: formal verification → machine-checkable RL reward → compounding improvements
- "Anything that can be specified can be proven. Humans are bad at specifying everything we want."
- Ramanujan analogy: AI intuitions are brilliant but need formal verification to be trustworthy
- $200M Series A; $1.6B valuation; company is 7 months old at time of interview
````
