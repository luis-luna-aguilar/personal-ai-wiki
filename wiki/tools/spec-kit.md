---
title: spec-kit
type: tool
domains: [coding]
subcategory: spec-driven-development
tags: [github, open-source, cli, spec-driven]
as_of: 2025-10-15
sources: [sdd-3-tools-fowler]
---

# spec-kit

GitHub's open-source take on [spec-driven development](../concepts/spec-driven-development.md). Distributed as a CLI that scaffolds a workspace with prompt files, templates, and a memory bank, then interacts with the user through slash commands inside their coding assistant (Copilot, Cursor, etc.). It is the most customizable of the three SDD tools Birgitta Böckeler reviewed, because all its artifacts live directly in the user's workspace.

## Current status (as of 2025-10-15)

- Open-source, repo: github.com/github/spec-kit
- CLI-based scaffolder; works with multiple coding assistants
- Uses slash commands (e.g. `/specify`, `/plan`, `/tasks`)
- Aspires to spec-anchored per GitHub's blog post, but in practice appears to still be spec-first: creates a new branch per spec, and the community has raised confusion over spec lifetime ([discussion #152](https://github.com/github/spec-kit/discussions/152))

## Workflow

**Constitution → ⟲ Specify → Plan → Tasks ⟲**

Each workflow step instantiates a set of files and prompts via bash scripts and templates. The workflow makes heavy use of checklists inside the generated markdown as a kind of AI-interpreted "definition of done" for each step.

## Memory bank: "constitution"

Spec-kit's memory bank is a prerequisite of the workflow and is called the **constitution** — a rules file containing high-level, "immutable" architectural principles that should apply to every change. It is heavily referenced by the agent during planning.

## File topology

One spec is made up of many files. In Böckeler's test, a single spec directory (`specs/001-when-a-user/`) contained 8 files: `data-model`, `plan`, `tasks`, `spec`, `research`, `api`, `component`, and more.

## Strengths

- Fully customizable — everything lives in the user's workspace
- Broad assistant support via slash commands
- Explicit constitution concept separates stable principles from per-task specs
- Open source

## Weaknesses / caveats

- Heavy: many markdown files per spec, verbose and repetitive to review
- Workflow feels like "overkill" for small and medium tasks (per Böckeler's 3–5 point story test)
- Branch-per-spec suggests spec lifetime is tied to a change request, not a feature — contradicting the spec-anchored aspiration
- Agent still ignored research-step findings in observed use (duplicated existing classes)
- Unclear when to stay purely functional vs add technical detail

## Recent changes

- [2025-10-15] Page created from Fowler's SDD tool survey (tool tried ~September 2025)

## Sources

- [Understanding Spec-Driven Development — Kiro, spec-kit, and Tessl (Fowler)](../sources/articles/sdd-3-tools-fowler.md)
