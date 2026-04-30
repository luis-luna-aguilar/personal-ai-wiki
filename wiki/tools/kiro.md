---
title: Kiro
type: tool
domains: [coding]
subcategory: spec-driven-development
tags: [spec-driven]
as_of: 2025-10-15
sources: [sdd-3-tools-fowler]
---

# Kiro

Kiro is a VS Code-based coding assistant that implements a simple, opinionated [spec-driven development](../concepts/spec-driven-development.md) workflow. Of the three SDD tools Birgitta Böckeler surveyed, it is the lightest-weight — mostly spec-first, with no clear story for carrying a spec across multiple tasks.

## Current status (as of 2025-10-15)

- Distributed as a VS Code-based product (see kiro.dev)
- Workflow guided inside the editor; 3 markdown docs per feature
- No published evidence of spec-anchored usage patterns
- No usage reports from long-running brownfield codebases

## Workflow

**Requirements → Design → Tasks.** Each step is one markdown document.

- **Requirements** — list of user stories ("As a…") with GIVEN/WHEN/THEN acceptance criteria
- **Design** — observed sections: component architecture diagram, Data Flow, Data Models, Error Handling, Testing Strategy, Implementation Approach, Migration Strategy (structure may vary per task)
- **Tasks** — a checklist traced back to requirement numbers, with in-editor UI for running and reviewing each task's changes

## Memory bank: "steering"

Kiro calls its memory bank **steering**. Default topology when you let Kiro generate it: `product.md`, `structure.md`, `tech.md`. Contents are flexible; the workflow does not depend on specific files being present.

## Strengths

- Simpler mental model than spec-kit (3 files vs ~8)
- In-editor task review UI
- Lightweight setup compared to CLI-scaffolded alternatives

## Weaknesses / caveats

- Heavyweight for small tasks: a minor bug became 4 user stories / 16 acceptance criteria in Böckeler's test
- Appears to be spec-first only — unclear how specs evolve past a single task
- Unknown fit for brownfield codebases

## Recent changes

- [2025-10-15] Page created from Fowler's SDD tool survey (tool tried ~September 2025)

## Sources

- [Understanding Spec-Driven Development — Kiro, spec-kit, and Tessl (Fowler)](../sources/articles/sdd-3-tools-fowler.md)
