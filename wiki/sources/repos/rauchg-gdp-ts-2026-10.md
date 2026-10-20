---
title: 'rauchg/gdp-ts — Ghosts of Departed Proofs for TypeScript (GitHub)'
type: source
source_type: repo
source_file: raw/repos/rauchg-gdp-ts.md
url: https://github.com/rauchg/gdp-ts
ingested: 2026-10-19
domains: [coding, cybersecurity]
---

# rauchg/gdp-ts — Ghosts of Departed Proofs for TypeScript (GitHub)

README for gdp-ts, an MIT-licensed TypeScript library, linter preset, and agent skill that implements "Ghosts of Departed Proofs". Sensitive functions demand a compile-time proof about their exact arguments, minted only by a trusted module, so authorization ("can this user read this resource") and entitlement ("does this user pay for this resource") bugs become type errors that humans and coding agents cannot easily introduce. The README gives no release date; the fetch date (2026-10-19) stands in.

## Influenced pages

- [gdp-ts](../../tools/gdp-ts.md) — new tool page
- [State of Coding](../../state-of/coding.md) — new "Coding discipline skills" section
- [Acceptance contracts and test oracles](../../training/acceptance-contracts-and-test-oracles.md) — proof-carrying types added to "Oracles agents can't game"
- [Software factory](../../workflows/software-factory.md) — new prerequisite: make unsafe agent code fail to compile

## Key claims extracted

- Three steps: `name()` gives a runtime value a compile-time-only name; a trusted module checks a fact and returns a `Proof` (or null); sensitive functions demand the proof about their exact named arguments
- Calling a sensitive function with a raw id, a proof about a different value, the wrong proof, or no proof is a compile error
- Middleware only authenticates; the check happens in the route body, and a data layer that demands proofs is safe to export to routes, Server Actions, and jobs
- ~Zero runtime overhead: a proof is a frozen `{ kind }` object; no extra queries or dependencies
- Type-check cost about 0.3 ms per authorized call site on a cold TypeScript 7 check; grows with usage, not codebase size
- ESLint and Oxlint presets block forging proofs with `as` or minting them outside `proofs/`
- Agent skill (`npx skills add rauchg/gdp-ts`) is plain Markdown, guides agents and humans through the pattern, and includes "where to stop" advice (an ease-to-rigor slider)
- Incrementally adoptable; requires TypeScript 5.4+
- Complements, not replaces, policy engines (CASL, Oso, Cerbos, OpenFGA), branded types, and validation libraries (zod, valibot); a policy engine can run inside a proof function
- Pragmatic TypeScript port of Haskell `gdp` and Rust `departed` / `mononym` / `gdp_rs`
