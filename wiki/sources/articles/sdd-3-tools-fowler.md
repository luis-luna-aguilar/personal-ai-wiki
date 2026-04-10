---
title: Understanding Spec-Driven Development — Kiro, spec-kit, and Tessl (Fowler)
type: source
source_type: article
source_file: raw/articles/2026-04-09-martinfowlercom-articles-exploring-gen-ai-sdd-3-toolshtml.md
url: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
ingested: 2026-04-09
domains: [coding, agents]
---

# Understanding Spec-Driven Development — Kiro, spec-kit, and Tessl (Fowler)

Birgitta Böckeler's survey of three self-labeled SDD tools, published on martinfowler.com as part of the "Exploring Gen AI" series. Proposes a three-level taxonomy for SDD (spec-first, spec-anchored, spec-as-source), walks through how each tool implements its workflow, and ends with sharp, practitioner-framed skepticism about whether elaborate upfront specs will actually improve AI-assisted coding.

## Influenced pages

- [[concepts/spec-driven-development]] — initial concept page, taxonomy and critiques
- [[tools/kiro]] — initial tool page
- [[tools/spec-kit]] — initial tool page
- [[tools/tessl]] — initial tool page
- [[state-of/coding]] — first subcategory populated (`spec-driven-development`)

## Key claims extracted

- SDD has three observable levels: **spec-first**, **spec-anchored**, **spec-as-source**; only Tessl actively pursues the latter two
- "Spec" is an overloaded term; working definition is "a structured, behavior-oriented natural-language artifact that guides AI coding agents"
- Distinction between **spec** (feature-scoped) and **memory bank** (codebase-wide context)
- Kiro workflow: Requirements → Design → Tasks (3 markdown files); memory bank called "steering" with defaults `product.md`, `structure.md`, `tech.md`
- Spec-kit workflow: Constitution → Specify → Plan → Tasks; CLI scaffolds workspace; one spec = ~8 files; creates a branch per spec
- Tessl Framework: CLI + MCP server; `tessl document` reverse-engineers specs, `tessl build` regenerates code; generated code marked `// GENERATED FROM SPEC - DO NOT EDIT`; 1 spec : 1 code file currently
- Tessl Framework is in private beta
- Reviewer critiques: one-size workflows fail on small and medium tasks; markdown review load is high; larger context windows don't fix instruction-following; functional/technical separation is unclear; spec-as-source echoes MDD's failure modes
- Tools were tried in September 2025 — fast-evolving, may have changed since
