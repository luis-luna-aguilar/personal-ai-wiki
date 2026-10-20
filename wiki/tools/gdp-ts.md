---
title: gdp-ts
type: tool
domains: [coding]
subcategory: coding-discipline-skill
tags: [open-source, github]
as_of: 2026-10-19
sources: [rauchg-gdp-ts-2026-10]
---

# gdp-ts

An open-source (MIT) TypeScript library, lint preset, and agent skill (repo `rauchg/gdp-ts`) that turns a class of authorization and entitlement bugs into compile errors. It ports the Haskell/Rust "Ghosts of Departed Proofs" idea: a sensitive function demands a proof that a check ran on its exact arguments, and only a trusted module can mint that proof. Neither a developer nor a coding agent can drop the check or check the wrong value and still compile.

## Current status (as of 2026-10-19)

- Three steps: `name()` gives a runtime value (such as a project id) a compile-time-only name; a trusted `proofs/` module runs the real check and returns a proof tied to those named values, or null; data-layer functions require that proof as an argument
- A raw id, a proof about a different value, the wrong proof, or no proof is a type error; ESLint and Oxlint presets block forged proofs (`{} as Proof`) and proofs minted outside `proofs/`
- Agent skill (`npx skills add rauchg/gdp-ts`) is plain Markdown that guides agents and people through the pattern, including advice on how much of a codebase to prove
- About 0.3 ms of type-check time per authorized call site and almost no runtime cost; incrementally adoptable, TypeScript 5.4+

## Why it matters

It moves a rule agents must follow at every call site out of review and instructions and into the compiler, the same "enforce, don't instruct" direction as lint-rule-driven [software factories](../workflows/software-factory.md). It complements policy engines (CASL, Oso, Cerbos, OpenFGA), which decide access and can run inside a proof function.

## Weaknesses / caveats

- Mainly a library with a skill attached
- New; the README is the only source and gives no adoption data or release date
- Safety depends on the lint preset being on, since a type cast can forge a proof

## Recent changes

- [2026-10-19] Page created from the gdp-ts README.

## Related

- [Acceptance contracts and test oracles](../training/acceptance-contracts-and-test-oracles.md) — proof-carrying types as an oracle agents can't game
- [Ponytail](ponytail.md) — another cross-agent coding-discipline skill

## Sources

- [rauchg/gdp-ts — Ghosts of Departed Proofs for TypeScript (GitHub)](../sources/repos/rauchg-gdp-ts-2026-10.md)
