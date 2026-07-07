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

- [Axiom Math — Latent Space podcast with Carina Hong (June 3)](../sources/newsletters/axiom-math-june-2026.md)
