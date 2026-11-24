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
