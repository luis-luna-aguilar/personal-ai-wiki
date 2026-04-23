---
title: Personal Wiki Agent PRD
status: draft
date: 2026-04-23
owner: Luis
---

# Personal Wiki Agent

## Overview

Build a dedicated agent that turns this personal wiki into a reusable expert system for other agents and AI clients. The agent must accept open-ended prompts such as questions, situation analyses, claim evaluations, and requests for judgment, then autonomously decide how to query the wiki, read only the relevant files, synthesize a full answer, and return it through a single tool interface.

The implementation will use **Deep Agents** as the internal harness and **OpenRouter** as the model gateway so the same system can be evaluated across multiple models without vendor lock-in.

The system must be packaged as a separate subproject inside this repository, not as root-level scripts mixed into wiki operations.

## Problem

Today, the wiki is useful inside a Codex session because the harness knows how to:

- read operating instructions
- inspect `wiki/index.md`
- choose which files to read
- separate current facts from personal views
- synthesize an answer

Outside that environment, the wiki is just a folder. Other agents do not automatically know how to operate it well, which means:

- answers are inconsistent
- agents may read too much or the wrong files
- the wiki is not exposed as a stable reusable capability
- missing knowledge is not systematically surfaced back to Luis

## Goal

Create a **Personal Wiki Agent** that behaves like a specialized analyst over this repository and can be invoked by external AI clients through one clear tool:

- `use_personal_wiki`

The tool should feel like: “Use Luis's personal wiki.”

## Non-Goals

- Replace the wiki ingest workflow
- Modify wiki pages during normal query execution
- Expose generic filesystem access as the public product
- Build a broad multi-tool workspace assistant in v1
- Depend on an active Codex or Claude Code session

## Users

- Primary: Luis, using Claude Desktop, ChatGPT, Codex, or similar agentic products
- Secondary: other agents acting on Luis's behalf

## Core User Stories

1. As Luis, I want to ask a question grounded in my curated wiki and receive a full answer, not just file excerpts.
2. As Luis, I want the agent to decide which wiki files to read instead of me naming them manually.
3. As Luis, I want the agent to distinguish factual wiki content from my personal opinions and takes.
4. As Luis, I want every answer to include a **Gaps** section that tells me what the wiki does not know well enough yet.
5. As Luis, I want to evaluate multiple models through OpenRouter without changing the wiki agent architecture.
6. As Luis, I want the same agent to run locally on my computer and be exposable later as a remote MCP server if needed.

## Product Principles

- **One public tool.** The external interface stays simple.
- **Full answer, not retrieval dump.** The wiki agent is responsible for synthesis.
- **Instruction-led querying.** The agent must follow query-specific repo instructions before exploring files.
- **Index-first reading.** `wiki/index.md` is the default starting point for wiki queries.
- **Selective reading.** Prefer targeted file inspection over broad scans.
- **Fact vs opinion separation.** Personal views are distinct from factual wiki state.
- **Page-level dating.** Each consulted page must carry its own `as_of` date in the output.
- **Gap reporting is mandatory.** Missing knowledge is a first-class product output.
- **Local-first architecture.** The first deployment target is Luis's own computer.

## Solution

Build a dedicated subproject at `personal-wiki-agent/` containing:

- a query-only instruction file
- Deep Agents runtime code
- tool definitions for reading and searching this repo
- config files with safe defaults
- MCP server entrypoint
- optional CLI for local testing
- evaluation configuration for model comparison through OpenRouter

Externally, clients interact with a single tool:

- `use_personal_wiki`

Internally, the Deep Agent:

1. loads query instructions
2. reads `wiki/index.md`
3. classifies the prompt internally
4. selects relevant pages and supporting files
5. reads only what it needs
6. uses `personal/` only when judgment or personal views are relevant
7. synthesizes a final answer
8. returns structured output including consulted pages and gaps

## Public Tool Contract

### Tool name

- `use_personal_wiki`

### Tool description

Use Luis's personal wiki to answer questions, analyze situations, evaluate claims, surface relevant pages, summarize recent changes, and provide judgment grounded in the wiki and Luis's personal notes.

### Input

```json
{
  "prompt": "Should I invest more in MCP-heavy workflows for my internal AI tools?",
  "context": "I care about interoperability and durable leverage.",
  "preferences": {
    "include_personal_views": true
  }
}
```

### Output

```json
{
  "answer": "Full synthesized answer...",
  "consulted_pages": [
    {
      "path": "wiki/concepts/mcp.md",
      "title": "Model Context Protocol",
      "as_of": "2026-04-22",
      "why_used": "Core concept page for the protocol in question"
    }
  ],
  "gaps": [
    {
      "type": "missing_evidence",
      "message": "The wiki lacks a dedicated page comparing MCP adoption outcomes across teams.",
      "suggested_addition": "Create a workflow or trend page on practical MCP adoption patterns."
    }
  ],
  "notes": [
    "Personal opinion pages were included in this answer"
  ]
}
```

## Internal Query Modes

The public interface remains one tool, but the engine may internally route to one dominant mode:

- factual question
- situation analysis
- claim evaluation
- page discovery
- recent-changes summary
- advisory judgment

This routing is internal. Users should not need to select from a menu in ordinary use.

## Mandatory Gaps Section

Every response must contain a `Gaps` section.

The gap analysis must identify one or more of:

- missing page that should exist
- stale page whose `as_of` is too old for a confident answer
- weak source coverage for the question asked
- personal viewpoint missing where judgment was requested
- conflicting evidence not sufficiently resolved by current pages
- inability to answer due to lack of coverage in the wiki

If there are no major gaps, the section should still say so explicitly:

- `No major knowledge gaps detected for this query.`

This requirement is critical because the agent must improve the wiki feedback loop, not only consume it.

## Functional Requirements

### Query behavior

- Must load a lightweight query-only instruction file on every run
- Must read `wiki/index.md` before deep file reads for normal wiki queries
- Must be able to search the repo for relevant pages and supporting files
- Must read file contents selectively
- Must synthesize a final answer using the model
- Must support factual and opinionated/advisory responses
- Must attach `as_of` to each consulted page
- Must always include `Gaps`

### Knowledge boundaries

- Must treat `wiki/` as factual curated state
- Must treat `personal/` as Luis's views, philosophies, and takes
- Must keep those categories distinct in the answer
- Must not silently blend personal opinions into factual statements

### Safety and control

- Must be read-only in normal query mode
- Must not ingest new material during query execution
- Must not write to `wiki/`, `personal/`, or `proposals/` during answering
- Must obey file and tool limits from config

### Deployment

- Must run locally on Luis's machine
- Must support local MCP exposure for Claude Desktop
- Should support remote MCP exposure later for ChatGPT-compatible remote connector flows

### Model routing

- Must use OpenRouter as the default provider layer
- Must allow model selection in config
- Must support evaluating multiple candidate models without changing core code

## Non-Functional Requirements

- Prefer correctness and judgment quality over low latency
- Keep architecture provider-agnostic at the agent layer
- Keep configuration file-driven wherever possible
- Use `personal_wiki_*` naming in code and config for product-specific clarity
- Preserve a clean separation between the wiki repository and the agent runtime code

## Deep Agents Fit

Deep Agents is the selected harness because it already provides the main behavioral primitives this product needs:

- planning
- context management via filesystem tools
- subagent support for context isolation
- skills
- permissions
- long-running agent patterns

This is a better fit than a generic retrieval wrapper because the product is not “search the wiki,” it is “operate the wiki as a bounded expert agent.”

## Repository Layout

```text
personal-wiki-agent/
  PRD.md
  README.md
  pyproject.toml
  personal_wiki_agent/
    __init__.py
    query_instructions.md
    config.default.toml
    config.local.example.toml
    server.py
    cli.py
    models.py
    output_schema.py
    prompts/
      system.md
      answer_format.md
    tools/
      get_index.py
      search_repo.py
      read_file.py
      recent_changes.py
      read_personal_context.py
    evals/
      scenarios.yaml
      models.yaml
```

## Query Instructions

Create a dedicated lightweight file:

- `personal-wiki-agent/personal_wiki_agent/query_instructions.md`

This file should contain query behavior only, including:

- current-state-first answering
- read `wiki/index.md` first
- prefer targeted reads
- use `personal/` only when needed
- separate fact from opinion
- return consulted pages with page-specific `as_of`
- always return `Gaps`
- never ingest or mutate wiki content during query runs

## Configuration

Use a config file as the primary control surface.

### Primary config files

- `personal-wiki-agent/personal_wiki_agent/config.default.toml`
- `personal-wiki-agent/personal_wiki_agent/config.local.toml`

### Secrets

Secrets may come from environment variables, but names must be product-specific:

- `PERSONAL_WIKI_OPENROUTER_API_KEY`

### Safe defaults

```toml
[personal_wiki_agent]
provider = "openrouter"
model = "anthropic/claude-sonnet-4.6"
max_steps = 10
max_files = 8
max_search_results = 12
include_personal_by_default = false
require_index_first = true
stale_after_days = 30
hard_stale_after_days = 90
return_consulted_pages = true
return_gaps = true
answer_style = "concise_analyst"

[personal_wiki_agent.transport]
enable_local_mcp = true
enable_remote_mcp = false

[personal_wiki_agent.paths]
repo_root = ".."
index_path = "../wiki/index.md"
personal_root = "../personal"
wiki_root = "../wiki"
```

## Answer Format

Every answer should contain:

### 1. Answer

The direct synthesized response.

### 2. Evidence

Optional short evidence framing when useful.

### 3. Consulted pages

Each consulted page must include:

- `path`
- `title`
- `as_of`
- `why_used`

### 4. Gaps

Explicit missing knowledge, missing evidence, or stale coverage.

## Deployment Strategy

### Phase 1: local-first

- Run on Luis's computer
- Expose as a local MCP server
- Target Claude Desktop first

### Phase 2: remote-compatible

- Add remote MCP transport for ChatGPT-compatible custom connector flows
- Keep the same agent code and tool contract

## Evaluation

The agent will incur model costs, so model evaluation is required.

### Evaluation goals

- compare answer quality across OpenRouter models
- compare gap detection quality across models
- compare file selection discipline
- compare cost and latency tradeoffs

### Initial evaluation dimensions

- factual accuracy against known wiki-covered questions
- quality of advisory judgment
- fact vs opinion separation
- usefulness of `Gaps`
- over-reading vs selective reading
- citation completeness and page-level `as_of` attachment

### Candidate model classes

- Anthropic reasoning/coding models
- OpenAI reasoning/coding models
- strong open or hybrid models available through OpenRouter

## Success Metrics

- A single prompt from an external client reliably triggers `use_personal_wiki`
- Returned answers are full syntheses, not context dumps
- 100% of responses include a meaningful `Gaps` section
- Consulted pages always include page-level `as_of`
- The agent typically starts from `wiki/index.md` and limits deep reads to relevant files
- Luis can compare multiple models through config without architecture changes
- Claude Desktop can use the local MCP server successfully

## Risks

- Deep Agents may still require meaningful customization to behave like a disciplined wiki analyst
- Some models may be weak at file-selection discipline despite tool support
- ChatGPT remote MCP support may require a public endpoint rather than localhost-only access
- Gap reporting may become generic unless tightly prompted and evaluated
- If query instructions drift from repo reality, answer quality will degrade

## Open Questions

- Which initial OpenRouter model should be the default for development?
- Should recent changes be inferred only from `wiki/log.md`, or also from `proposals/applied/` by default?
- Should advisory answers explicitly separate “world state,” “Luis's likely view,” and “my recommendation” as three sections?
- Should the remote MCP deployment be part of v1 or deferred until local quality is proven?

## Milestones

### Milestone 1: foundation

- create `personal-wiki-agent/`
- add PRD
- add query-only instructions
- add default config
- scaffold Deep Agents runtime

### Milestone 2: local answering

- implement repo tools
- implement answer schema
- implement mandatory `Gaps`
- expose local MCP server
- validate on Claude Desktop

### Milestone 3: model evaluation

- define eval scenarios
- compare candidate OpenRouter models
- tune prompts and config defaults

### Milestone 4: remote transport

- add remote MCP deployment path
- validate ChatGPT-compatible integration if desired

## Acceptance Criteria

- [ ] A dedicated `personal-wiki-agent/` subproject exists
- [ ] The product exposes one public tool: `use_personal_wiki`
- [ ] Query behavior is governed by a lightweight query-only instruction file
- [ ] The agent uses Deep Agents as the internal harness
- [ ] The model layer is routed through OpenRouter
- [ ] Every response contains a `Gaps` section
- [ ] Every consulted page includes its own `as_of`
- [ ] Fact vs personal opinion is kept distinct
- [ ] Local MCP deployment is a first-class target
- [ ] The system is read-only during query execution

