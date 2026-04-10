---
title: Spec-Driven Development (SDD)
type: concept
domains: [coding, agents]
subcategory: spec-driven-development
tags: [spec-driven]
as_of: 2026-04-09
sources: [sdd-3-tools-fowler]
---

# Spec-Driven Development (SDD)

A loosely-defined AI-assisted coding approach where a structured, behavior-oriented artifact written in natural language — the **spec** — is authored before code and used as the primary input to AI coding agents. The term is still in flux and already semantically diffused: some practitioners use "spec" as a synonym for "detailed prompt," while self-labeled SDD tools differ substantially in how they structure and maintain specs.

## Current status (as of 2026-04-09)

- Term is new and contested; no shared definition across tools
- Three self-labeled SDD tools exist: [[tools/kiro]], [[tools/spec-kit]], [[tools/tessl]]
- Real-world usage reports are scarce; most tutorials are greenfield from-scratch apps
- Healthy skepticism in the practitioner community about whether SDD amplifies or solves existing AI-coding pain points

## The three levels of SDD

Per Birgitta Böckeler's taxonomy on martinfowler.com:

1. **Spec-first** — A spec is written before the code for the task at hand, then may be discarded.
2. **Spec-anchored** — The spec is kept and evolved over the lifetime of the feature, re-used across future changes.
3. **Spec-as-source** — The spec is *the* source file. Humans only edit the spec; generated code is marked do-not-edit.

All SDD tools are at least spec-first. Fewer commit to spec-anchored. Only [[tools/tessl]] is actively exploring spec-as-source.

## What is a spec?

There is no canonical definition. The working definition from the Fowler article:

> A structured, behavior-oriented artifact — or a set of related artifacts — written in natural language that expresses software functionality and serves as guidance to AI coding agents.

Tools disagree on structure, level of detail, and file topology (Kiro: 3 files; spec-kit: ~8 files per spec; Tessl: 1 spec : 1 code file).

## Spec vs memory bank

An important distinction: **specs** describe a particular feature or change; the **memory bank** is the broader codebase context (rules files, architecture overviews, project conventions) that is relevant across all AI coding sessions. Tools have their own names for memory bank: Kiro calls it "steering," spec-kit calls it the "constitution," Tessl uses a `.tessl/framework` folder plus `AGENTS.md`/`KNOWLEDGE.md`.

## Open questions and critiques

From the Fowler review:

- **Problem-size fit.** Kiro turned a small bug into 4 user stories and 16 acceptance criteria. Spec-kit generated many verbose markdown files for a 3–5 point feature. Neither offers multiple workflows for different problem sizes.
- **Review overhead.** Reviewing generated markdown specs is often more tedious than reviewing code.
- **False sense of control.** Larger context windows do not guarantee instruction-following. Agents still ignore or over-apply spec content.
- **Functional vs technical separation.** SDD tools ask authors to separate functional intent from technical detail, but this is a long-standing pain point for the profession; tutorials are inconsistent.
- **Target user unclear.** Workflows incorporate product/requirements artifacts (user stories, goals) while assuming the user is a developer.
- **MDD echoes.** Spec-as-source recalls model-driven development, which never took off for business apps due to overhead and constraints. LLMs remove the need for a parseable grammar but reintroduce non-determinism — possibly combining the worst of both.

## Recent changes

- [2026-04-09] Page created from Fowler's "Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl"

## Sources

- [[sources/articles/sdd-3-tools-fowler]]
