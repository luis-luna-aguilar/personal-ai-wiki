---
type: proposal
source: raw/articles/2026-04-09-martinfowlercom-articles-exploring-gen-ai-sdd-3-toolshtml.md
status: pending
created: 2026-04-09
---

# Proposal: Understanding Spec-Driven Development (Kiro, spec-kit, Tessl) — Martin Fowler

## Summary
Birgitta Böckeler (on martinfowler.com) surveys "spec-driven development" (SDD) by trying three self-labeled SDD tools — Kiro, GitHub spec-kit, and Tessl Framework — and proposes a three-level taxonomy (spec-first → spec-anchored → spec-as-source). The overall tone is skeptical: the tools feel heavyweight, markdown review is painful, agents still ignore instructions, and the promise echoes model-driven development's old failure modes.

This is the wiki's first real ingest, so the proposal leans toward creating foundational pages (bootstrap phase, <30 pages, discipline relaxed).

## Intended changes

- [x] **Create** `wiki/concepts/spec-driven-development.md` — new concept page for SDD, the three levels, definition of "spec", and the memory-bank vs spec distinction
- [x] **Create** `wiki/tools/kiro.md` — VS Code-based SDD tool, requirements → design → tasks workflow, "steering" memory bank
- [x] **Create** `wiki/tools/spec-kit.md` — GitHub's CLI-based SDD scaffolder, constitution → specify → plan → tasks, slash-command driven
- [x] **Create** `wiki/tools/tessl.md` — Tessl Framework CLI/MCP, the only tool aspiring to spec-as-source; in private beta
- [x] **Update** `wiki/state-of/coding.md` — add new `spec-driven-development` subcategory listing all three tools, with "Recent changes" entry
- [x] **Create** `wiki/sources/articles/sdd-3-tools-fowler.md` — source summary
- [x] **Update** `wiki/index.md` — add new concept, tools, and note bootstrap progress (page count jumps from 0 to 4 content pages)

## Schema / vocabulary additions

- [x] Add subcategory `spec-driven-development` to `wiki/_schema/subcategories.md`
  - Parent domain: `coding`
  - Applies to types: `tool`, `workflow`, `concept`
  - Definition: Tools and workflows where a structured natural-language spec is authored before (and often alongside) code, intended as the primary artifact guiding AI coding agents.
- [x] Add tags to `wiki/_schema/tags.md`:
  - `github` — vendor/org
  - `open-source` — license/openness
  - `cli` — ecosystem
  - `vscode-fork` — ecosystem
	  - Comment: please remove this one.
  - `beta` — flavor (pre-GA product)
  - `spec-driven` — flavor (SDD-aligned)

## Page drafts

### wiki/concepts/spec-driven-development.md (new)

```
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
```

### wiki/tools/kiro.md (new)

```
---
title: Kiro
type: tool
domains: [coding]
subcategory: spec-driven-development
tags: [vscode-fork, spec-driven]
as_of: 2026-04-09
sources: [sdd-3-tools-fowler]
---

# Kiro

Kiro is a VS Code-based coding assistant that implements a simple, opinionated [[concepts/spec-driven-development|spec-driven development]] workflow. Of the three SDD tools Birgitta Böckeler surveyed, it is the lightest-weight — mostly spec-first, with no clear story for carrying a spec across multiple tasks.

## Current status (as of 2026-04-09)

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

- [2026-04-09] Page created from Fowler's SDD tool survey (tool tried ~September 2025)

## Sources

- [[sources/articles/sdd-3-tools-fowler]]
```

### wiki/tools/spec-kit.md (new)

```
---
title: spec-kit
type: tool
domains: [coding]
subcategory: spec-driven-development
tags: [github, open-source, cli, spec-driven]
as_of: 2026-04-09
sources: [sdd-3-tools-fowler]
---

# spec-kit

GitHub's open-source take on [[concepts/spec-driven-development|spec-driven development]]. Distributed as a CLI that scaffolds a workspace with prompt files, templates, and a memory bank, then interacts with the user through slash commands inside their coding assistant (Copilot, Cursor, etc.). It is the most customizable of the three SDD tools Birgitta Böckeler reviewed, because all its artifacts live directly in the user's workspace.

## Current status (as of 2026-04-09)

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

- [2026-04-09] Page created from Fowler's SDD tool survey (tool tried ~September 2025)

## Sources

- [[sources/articles/sdd-3-tools-fowler]]
```

### wiki/tools/tessl.md (new)

```
---
title: Tessl Framework
type: tool
domains: [coding]
subcategory: spec-driven-development
tags: [cli, beta, spec-driven]
as_of: 2026-04-09
sources: [sdd-3-tools-fowler]
---

# Tessl Framework

The [[concepts/spec-driven-development|SDD]] tool furthest along the spec-as-source direction. A CLI that also doubles as an MCP server, scaffolds workspace config for a variety of coding assistants, and treats the spec as a living artifact that can round-trip with code. Currently in private beta.

## Current status (as of 2026-04-09)

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

- [2026-04-09] Page created from Fowler's SDD tool survey (tool tried ~September 2025)

## Sources

- [[sources/articles/sdd-3-tools-fowler]]
```

### wiki/state-of/coding.md (updated)

```
---
title: State of Coding
type: state-of
domains: [coding]
tags: []
as_of: 2026-04-09
sources: [sdd-3-tools-fowler]
---

# State of Coding

Current state of AI tools for software development. Organized by subcategory — each subcategory can have multiple top players. Ambiguity is expected.

## Subcategories

### Spec-driven development

Tools where a structured natural-language spec is the primary input to AI coding agents. The term is contested and the field is early — no clear leader. See [[concepts/spec-driven-development]] for the concept and taxonomy.

- [[tools/kiro]] — VS Code-based; requirements → design → tasks; lightest-weight, mostly spec-first *(as of 2026-04-09)*
- [[tools/spec-kit]] — GitHub; CLI scaffolder + slash commands; constitution → specify → plan → tasks; most customizable *(as of 2026-04-09)*
- [[tools/tessl]] — CLI + MCP server; only tool pursuing spec-as-source; private beta *(as of 2026-04-09)*

## Recent changes

- [2026-04-09] First content for this page. Added `spec-driven-development` subcategory with Kiro, spec-kit, Tessl after ingesting Fowler's SDD survey.
```

### wiki/sources/articles/sdd-3-tools-fowler.md (new)

```
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
```

### wiki/index.md (updated)

```
---
title: Wiki Index
type: index
as_of: 2026-04-09
---

# Wiki Index

Catalog of every page in the wiki. This file is the LLM's starting point for every query and every ingest — read it first to find relevant pages before drilling in.

When adding a new wiki page (via a proposal), add its index entry under the correct section. One line per page: wikilink + one-line description + `(as_of: YYYY-MM-DD)`.

---

## State of

Read-me-first dashboards per domain.

- [[state-of/coding]] — current state of AI coding tools and workflows *(as_of: 2026-04-09)*
- [[state-of/models]] — current state of foundation models *(as_of: —)*
- [[state-of/agents]] — current state of agentic systems and tool use *(as_of: —)*

## Models

Foundation models. One page per model family or generation.

_(empty)_

## Tools

Tools and products built on top of models. One page per tool.

- [[tools/kiro]] — VS Code-based SDD tool, 3-doc workflow *(as_of: 2026-04-09)*
- [[tools/spec-kit]] — GitHub's CLI SDD scaffolder with slash commands *(as_of: 2026-04-09)*
- [[tools/tessl]] — CLI + MCP framework exploring spec-as-source; private beta *(as_of: 2026-04-09)*

## Benchmarks

Benchmark pages. Current leaderboards and methodology.

_(empty)_

## Workflows

Reusable patterns and recipes.

_(empty)_

## Concepts

Ideas and techniques (RAG, context engineering, compound engineering, etc.).

- [[concepts/spec-driven-development]] — SDD concept, three-level taxonomy, critiques *(as_of: 2026-04-09)*

## Trends

Things being watched that haven't solidified yet.

_(empty)_

## Sources

See `wiki/sources/` — source summaries are not indexed here (they're many and cheap). Use `grep` or Glob when you need them.

---

## Page count

- state-of: 3 (1 populated, 2 skeletons)
- models: 0
- tools: 3
- benchmarks: 0
- workflows: 0
- concepts: 1
- trends: 0

**Total content pages: 4.** The wiki is in the bootstrap phase (<30 pages) — categorization discipline is relaxed.
```

## Open questions

- **Memory bank as its own concept page?** The article carefully distinguishes "memory bank" from "spec," and each tool has its own name for it (steering / constitution / .tessl). I folded it into the SDD concept page as a section, but it could justify its own `concepts/memory-bank.md` as more sources accumulate. Leaning: wait until a second source mentions it before spinning it out.
	- Comment: Do not create a new concept page.
- **Tool attribution for Kiro.** The article does not say who makes Kiro (only "VS Code based distribution" at kiro.dev). I deliberately did not guess a vendor. If you want a vendor tag added later, let me know.
	- Comment: Leave it as is.
- **Tessl Registry vs Tessl Framework.** The article mentions the Tessl team considers the Registry their current public product, while the Framework is forward-looking. I created a page for the Framework only (since that is what the article is about) and titled it "Tessl Framework" — should I rename to just "Tessl" or split into two pages later?
	- Comment: Leave it as is.
- **`beta` tag.** I proposed it for Tessl, but it is a lifecycle state more than a cross-cutting attribute. Alternative: put lifecycle in the page body only and skip the tag. Your call.
	- Comment: Leave it as is.
- **Spec-kit page title casing.** I used lowercase `spec-kit` to match the repo name. If you prefer `Spec-kit` or `Spec-Kit` as a title, let me know.
	- 

## Comments from Luis

- Please document clearly how you expect answers on open questions, because I added a comment below, but that might not work for you.
-  there are things we can clearly say have an as-of date, like a tool that's obvious. There is other stuff that is more complex, like the state of coding. There are things in there referenced by an as-of date, a certain date, but the whole state of coding doesn't really match that date. We'll need to reconsider how to manage the staleness of such states for whole areas
-  Also I checked the checkbox of the things to include,  I was not clear if I had to leave it unchecked or not but I think 