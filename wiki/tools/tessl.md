---
title: Tessl Framework
type: tool
domains: [coding]
subcategory: spec-driven-development
tags: [cli, beta, spec-driven]
as_of: 2025-10-15
sources: [sdd-3-tools-fowler]
---

# Tessl Framework

The [[concepts/spec-driven-development|SDD]] tool furthest along the spec-as-source direction. A CLI that also doubles as an MCP server, scaffolds workspace config for a variety of coding assistants, and treats the spec as a living artifact that can round-trip with code. Currently in private beta.

## Current status (as of 2025-10-15)

- **Private beta** — not publicly available
- Distributed as a CLI; same binary runs as an MCP server
- Only SDD tool explicitly aspiring to **spec-anchored** and even **spec-as-source** usage
- Current mapping is 1 spec ↔ 1 code file; team is experimenting with higher-level mappings
- Tessl team themselves frame the Framework as more of a future product than the current public [Tessl Registry](https://tessl.io)

## How it works

- `tessl document --code <file>` reverse-engineers a spec from an existing code file
- `tessl build` generates code from a spec
- Generated code files are marked `// GENERATED FROM SPEC - DO NOT EDIT`
- Specs use tags like `@generate`, `@test`, and include an API section for interfaces exposed to other parts of the codebase

## Memory bank

Lives in `.tessl/framework/` with additional conventions via `KNOWLEDGE.md` and `AGENTS.md`.

## Strengths

- Only tool seriously exploring spec-as-source
- Low per-spec abstraction level (one spec per code file) reduces LLM reinterpretation and error surface
- Bidirectional workflow: reverse-engineer → iterate → regenerate
- CLI + MCP integration plays nicely with multiple coding assistants

## Weaknesses / caveats

- Private beta; no production usage reports
- Low abstraction (per-file specs) raises fragmentation concerns at scale
- Non-determinism: the same spec can generate different code across runs; iteration toward "unambiguous" specs reminded Böckeler of classic specification-writing pitfalls
- Parallels with MDD (model-driven development) suggest spec-as-source may inherit both MDD's inflexibility and LLMs' non-determinism

## Recent changes

- [2025-10-15] Page created from Fowler's SDD tool survey (tool tried ~September 2025)

## Sources

- [[sources/articles/sdd-3-tools-fowler]]
