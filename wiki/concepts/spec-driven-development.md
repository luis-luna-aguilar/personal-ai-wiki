---
title: Spec-Driven Development (SDD)
type: concept
domains: [coding, agents]
subcategory: spec-driven-development
tags: [spec-driven]
as_of: 2026-04-22
sources: [sdd-3-tools-fowler, spec-is-new-code]
---

# Spec-Driven Development (SDD)

A loosely-defined AI-assisted coding approach where a structured, behavior-oriented artifact written in natural language — the **spec** — is authored before code and used as the primary input to AI coding agents. The term is still in flux and already semantically diffused: some practitioners use "spec" as a synonym for "detailed prompt," while self-labeled SDD tools differ substantially in how they structure and maintain specs.

## Current status (as of 2026-04-22)

- The ecosystem is independently converging on spec-first approaches from multiple directions — not just dedicated SDD tools
- GitHub Spec-Kit: 77,000 stars as of April 2026; agent-agnostic; works across Claude Code, Cursor, and others
- OpenAI Symphony: monitors issue trackers, spins up autonomous agents per issue; requires a `SPEC.md` as the contract between human and agent
- "The Ralph Loop": PRD placed in an infinite agent loop; progress persists in files and git (not in context window), so the agent can resume across sessions
- Plan mode in Claude Code and Cursor is now framed as a lightweight built-in SDD step — the ecosystem is absorbing the concept at the platform level
- The core argument gaining traction: agent failures are mostly *communication failures*, not model failures. The problem is ambiguity in instructions, not model capability.

## The three levels of SDD

Per Birgitta Böckeler's taxonomy on martinfowler.com:

1. **Spec-first** — A spec is written before the code for the task at hand, then may be discarded.
2. **Spec-anchored** — The spec is kept and evolved over the lifetime of the feature, re-used across future changes.
3. **Spec-as-source** — The spec is *the* source file. Humans only edit the spec; generated code is marked do-not-edit.

All SDD tools are at least spec-first. Fewer commit to spec-anchored. Only [Tessl Framework](../tools/tessl.md) is actively exploring spec-as-source.

## What is a spec?

There is no canonical definition. The working definition from the Fowler article:

> A structured, behavior-oriented artifact — or a set of related artifacts — written in natural language that expresses software functionality and serves as guidance to AI coding agents.

Tools disagree on structure, level of detail, and file topology (Kiro: 3 files; spec-kit: ~8 files per spec; Tessl: 1 spec : 1 code file).

## Spec vs memory bank

An important distinction: **specs** describe a particular feature or change; the **memory bank** is the broader codebase context (rules files, architecture overviews, project conventions) that is relevant across all AI coding sessions. Tools have their own names for memory bank: Kiro calls it "steering," spec-kit calls it the "constitution," Tessl uses a `.tessl/framework` folder plus `AGENTS.md`/`KNOWLEDGE.md`.

## New patterns (2026)

### The Ralph Loop
A PRD lives in an infinite agent loop. The agent executes steps, writes progress to files and git commits after each step, and can be interrupted and resumed without losing state. The loop continues until the PRD is complete. Key insight: progress in files/git, not in the context window.

### OpenAI Symphony
Monitors your issue tracker, identifies new issues, spins up autonomous coding agents per issue. Requires a `SPEC.md` as the formal contract between human intent and agent execution. No `SPEC.md` → no agent run.

### Plan mode as lightweight SDD
Built-in plan modes in Claude Code (shift-tab) and Cursor act as a minimal spec-and-plan step before execution. The ecosystem is absorbing SDD at the platform level for users who never use a dedicated SDD tool.

## Open questions and critiques

From the Fowler review:

- **Problem-size fit.** Kiro turned a small bug into 4 user stories and 16 acceptance criteria. Spec-kit generated many verbose markdown files for a 3–5 point feature. Neither offers multiple workflows for different problem sizes.
- **Review overhead.** Reviewing generated markdown specs is often more tedious than reviewing code.
- **False sense of control.** Larger context windows do not guarantee instruction-following. Agents still ignore or over-apply spec content.
- **Functional vs technical separation.** SDD tools ask authors to separate functional intent from technical detail, but this is a long-standing pain point for the profession; tutorials are inconsistent.
- **Target user unclear.** Workflows incorporate product/requirements artifacts (user stories, goals) while assuming the user is a developer.
- **MDD echoes.** Spec-as-source recalls model-driven development, which never took off for business apps due to overhead and constraints. LLMs remove the need for a parseable grammar but reintroduce non-determinism — possibly combining the worst of both.

## Recent changes

- [2025-10-15] Page created from Fowler's "Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl"
- [2026-04-22] Added ecosystem convergence signal: Spec-Kit 77k stars, OpenAI Symphony, The Ralph Loop, and plan mode as built-in SDD step

## Sources

- [Understanding Spec-Driven Development — Kiro, spec-kit, and Tessl (Fowler)](../sources/articles/sdd-3-tools-fowler.md)
- ["The Spec Is the New Code" — Julian De Angelis](../sources/tweets/spec-is-new-code.md)
