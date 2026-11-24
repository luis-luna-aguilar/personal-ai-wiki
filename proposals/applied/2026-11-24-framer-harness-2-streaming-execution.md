---
type: proposal
source: raw/articles/2026-11-23-framercom-blog-harness-2.md
status: pending
created: 2026-11-24
---

# Proposal: Framer Harness 2, executing agent code as it streams

## Summary

### In short
When an agent writes one program instead of making many tool calls, the harness can start running that program before the model finishes writing it. It can also stop generation the moment an early check fails, which saves output tokens. Framer's Harness 2 does this in production and reports 43% fewer tool steps and 39% fewer cached input tokens per message. The proposal adds one pattern bullet next to the existing code-mode bullet on **Agentic orchestration patterns**, plus a source page. The reason to hesitate is length: the page is already at 106% of its ceiling, and this addition takes it to about 110%, the top of the warning band.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Framer, the website builder, published an engineering post on 2 November 2026 about rebuilding its in-app AI agent. The first harness had the model send small editing commands one at a time. That worked badly for repetitive or dependent edits: recolouring 100 frames meant 100 commands, and reading a value before writing it needed an extra model call. In Harness 2 the model instead writes one JavaScript program against the design document. As the code streams in, the harness splits it into complete statements and runs each one in a Web Worker straight away, so changes appear on the canvas before the model has finished writing.

The second idea is cancellation. The model is told to check its assumptions first, for example that a node exists. If a check fails, or the program returns early or hits a terminal error, the harness stops the rest of generation. Edits already made stay, and output tokens are not spent on code that would never run. Smaller write errors, such as out-of-range values, are clamped or skipped and reported at the end. External agents such as Claude Code, Cursor and ChatGPT Desktop now send one program over MCP to the same harness. Framer credits the April 2026 paper *Executing as You Generate* (arXiv 2604.00491), which does the same thing in Python.

### What changes
The wiki already records "code mode", where an agent batches its tool calls into one script, as a pattern from Uber's agent fleet. It does not cover running that script while it streams.

- **Agentic orchestration patterns** gains one bullet directly after the code-mode bullet, covering stream-time execution and early cancellation, Framer's numbers and the paper. It also gets a Recent-changes entry dated 2 November (nine entries become ten, so nothing spills) and the new source in its lists. The page date moves from 13 October to 2 November.
- One new source page for the Framer post.

### What to weigh
The saved copy of the post has no date. The 2 November date comes from the live page's `datePublished` metadata, and the post sits in the late-October to early-November inbox batch. The post gives the tool-step saving both as "2x fewer" and as 43%. The proposal uses 43%, the figure from its summary.

## Intended changes

- [ ] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add one bullet after the Code-mode bullet; add one Recent-changes entry dated 2026-11-02 at the top (9 → 10 entries, no spill); append the source id and Sources link; `as_of` 2026-10-13 → 2026-11-02
- [ ] **Create** `wiki/sources/articles/framer-harness-2-2026-11-02.md` — source summary

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter (`as_of` changes; `sources:` appends `framer-harness-2-2026-11-02` to the end of the live list):

```
as_of: 2026-11-02
sources: [...live list..., framer-harness-2-2026-11-02]
```

New bullet inserted directly after the "**Code-mode: batch tool calls into one script instead of one model turn each.**" bullet under `## Current patterns`:

```
- **Execute the script while it streams.** Framer's Harness 2 runs the model's JavaScript one complete statement at a time as it arrives, so edits appear before generation ends. A failed precondition, early return or terminal error cancels the rest of the stream and its output tokens; recoverable write errors are clamped or skipped and reported at the end. Framer reports 43% fewer tool steps and 39% fewer cached input tokens per message. *Sources: Framer (2026-11-02); arXiv 2604.00491*
```

`## Recent changes` (adds one entry at the top; list goes from 9 to 10, no spill):

```
- [2026-11-02] Added stream-time execution with early cancellation after the Code-mode pattern: Framer's Harness 2 runs agent-written JavaScript as it streams and cancels generation on a failed check (43% fewer tool steps, 39% fewer cached input tokens per message).
- [2026-10-19] Split the software-factory patterns ...
```

`## Sources` (appends one link at the end):

```
- [Framer — Harness 2: executing agent code as it streams](../sources/articles/framer-harness-2-2026-11-02.md)
```

### wiki/sources/articles/framer-harness-2-2026-11-02.md (new)

```
---
title: 'Framer — Harness 2: executing agent code as it streams'
type: source
source_type: article
source_file: raw/articles/2026-11-23-framercom-blog-harness-2.md
url: https://framer.com/blog/harness-2/
published: 2026-11-02
ingested: 2026-11-24
domains: [agents]
---

# Framer — Harness 2: executing agent code as it streams

Framer's engineering post on replacing its DSL-command agent harness with one where the model writes a single JavaScript program against the design document. The harness parses the program into complete statements ("cells") as it streams and runs them right away. It cancels the remaining generation when an early check fails. The publication date comes from the live page's `datePublished` metadata; the saved raw copy has none.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — new "execute the script while it streams" bullet after Code-mode

## Key claims extracted
- The old harness had the model emit INSERT/PATCH commands one at a time. Repeated edits, dependent read-then-write edits and multi-step workflows (inspect, publish to staging, promote) each needed many commands or model calls.
- Eager execution: streamed code is parsed into complete JavaScript statements, grouped into cells and run in order in a Web Worker, with bindings kept between cells and top-level `await` transpiled. `// @step` comments become progress messages.
- Cancellation: the agent is prompted to check its preconditions first. A terminal error or early return (including "no changes needed") cancels the remaining generation. Edits already applied are kept. Terminal errors are written to explain how to recover.
- Recoverable write errors don't stop the program: valid properties are applied, out-of-range values clamped, unsupported properties skipped, and warnings reported at the end. Dot-notation and sparse-array patches cut output tokens.
- An in-memory copy of the document in the worker allows synchronous reads and writes over documents with millions of nodes.
- External agents (ChatGPT Desktop, Claude Code, Cursor) submit one program over MCP to the same harness as the in-app agent, instead of making repeated requests through Framer's servers.
- Reported: 43% fewer tool steps (also written as "2x fewer") and 39% fewer cached input tokens per message, with no measured quality loss.
- Prior work: *Executing as You Generate* (arXiv 2604.00491, Sun et al., 1 April 2026) applies AST-based eager execution and early interruption to Python. Framer plans to adopt that paper's trick of dropping completed statements from the parse buffer.
```

## Schema / vocabulary additions

None.

## Open questions

None.
