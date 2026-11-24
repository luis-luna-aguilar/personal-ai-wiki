---
type: proposal
source: raw/repos/asymptote-labs-agent-beacon.md
status: pending
created: 2026-11-24
---

# Proposal: Beacon (Asymptote Labs) — open-source memory layer across 20+ coding harnesses

## Summary

### In short
Agent memory is starting to sit across harnesses instead of inside one. Asymptote Labs' open-source Beacon records full session traces from Claude Code, Cursor, Codex and 20+ other coding tools. It extracts workflows, corrections and repo conventions, asks a human to approve them, and serves them back to every tool through MCP or skills. The proposal creates a Beacon tool page and adds it to Agent memory, the Knowledge architectures hub and State of Agents. The reason to hesitate is the date: the README has none, so everything is dated today.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The source is the README of `Asymptote-Labs/agent-beacon` on GitHub, captured on 23 November 2026. Beacon is MIT-licensed and calls itself "local-first." It runs in the background while a developer uses their usual coding agents. It collects each session through the harness's hooks, its OpenTelemetry export or by polling its logs. It then normalizes everything into one event format: prompts and responses, tool calls, shell commands, file edits, approvals, MCP activity and token counts, stored as plain JSONL files on the machine. The support table covers about thirty local agents, from Claude Code, Codex and Cursor to Pi, Hermes Agent and Kiro. Browser extensions cover Claude.ai and ChatGPT, and the cloud agents of Claude Code, Cursor and Devin are supported, as are CI jobs.

On top of the traces, Beacon runs a loop. It evaluates what worked, extracts reusable knowledge (a migration recipe, a debugging path that finally worked, a correction given to several agents), puts it in front of a human for review, and makes the approved items available to future agents through MCP or "Beacon Skills." The pitch is that a lesson learned in Cursor can help Codex. A local dashboard shows the traces, and sandboxed "lenses" render custom views of a single trace.

The README is candid about defaults. Interactive setup preselects Beacon Cloud, which forwards traces to Asymptote Labs, and keeping data local requires choosing Local. Setup also installs skills into `~/.claude/skills` and registers an MCP server in six harnesses unless the user opts out. The README offers no measurement of whether the extracted knowledge improves agent results.

### What changes
The wiki's Agent memory page covers memory lifecycles, Cognition's Agent Memory Repo and Devin Dreaming, but no tool that shares memory across different harnesses. The hub's Agent memory row has no tool pages yet.

- New page `tools/beacon.md`, filed as a knowledge platform on the agent-memory row, with the cloud-forwarding default and the skill and MCP installs listed as caveats.
- **Agent memory** gains a Current-status bullet on cross-harness memory and a Recent-changes entry. Page date moves to 24 November.
- **Knowledge architectures** lists Beacon as the first tool page in the Agent memory row. Its Recent-changes list is at its cap, so the oldest entry (28 July) moves to a new history file. Page date moves to 24 November.
- **State of Agents** adds Beacon under Knowledge platforms. Its list is also at its cap, so the oldest entry (9 October, Harness²) moves to history. Page date moves to 24 November.
- Index entry and one source page.

### What to weigh
The README carries no date, so the tool page and every page date it moves use today's ingest date, 24 November. "Memory layer" is already an alias of Agent memory on the term map, so no new concept or term row is needed. Beacon's human approval step and project-wide sharing edge toward a knowledge layer. The draft places it on the agent-memory row because its knowledge is written from agent sessions.

## Intended changes

- [ ] **Create** `wiki/tools/beacon.md` — new tool page
    > See draft below

- [ ] **Update** `wiki/concepts/agent-memory.md` — one Current-status bullet; Current-status stamp 2026-11-07 → 2026-11-24; adds one Recent-changes entry dated 2026-11-24 at the top (list goes from 6 to 7, no spill); append source id and Sources line; `as_of` 2026-11-07 → 2026-11-24
    > See draft below

- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — add Beacon to the Agent memory row's examples; adds one Recent-changes entry dated 2026-11-24 at the top; append source id and Sources line; `as_of` 2026-10-28 → 2026-11-24
    > See draft below

- [ ] **Spill** `wiki/concepts/knowledge-architectures.md` → `wiki/history/concepts/knowledge-architectures.md` (new file) — list is at its cap of 10, so the oldest entry (2026-07-28) spills
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — one line under Knowledge platforms; adds one Recent-changes entry dated 2026-11-24 at the top; append source id; `as_of` 2026-11-23 → 2026-11-24
    > See draft below

- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — list is at its cap of 10, so the oldest entry (2026-10-09, Harness²) spills
    > See draft below

- [ ] **Update** `wiki/index.md` — add the Beacon tool line; refresh the agent-memory line's date
    > See draft below

- [ ] **Create** `wiki/sources/repos/asymptote-labs-agent-beacon.md` — source summary

## Page drafts

### wiki/tools/beacon.md (new)

```md
---
title: Beacon
type: tool
domains: [agents, coding]
subcategory: knowledge-platform
tags: [open-source, agentic, knowledge-cluster]
as_of: 2026-11-24
sources: [asymptote-labs-agent-beacon]
---

# Beacon

Beacon is Asymptote Labs' open-source (MIT), local-first memory layer for AI coding agents. It records full session traces from Claude Code, Cursor, Codex, OpenCode, Cline and 20+ other harnesses. It then turns useful workflows, corrections, debugging paths and repo conventions into knowledge any of those agents can reuse. In the [Knowledge architectures](../concepts/knowledge-architectures.md) matrix it sits on the [agent memory](../concepts/agent-memory.md) row, with two differences: memory is shared across harnesses, and a human approves what is kept.

## Current status (as of 2026-11-24)

- Capture: hooks, OpenTelemetry export and log polling normalize sessions, prompts, responses, tool calls, commands, file edits, approvals, MCP activity and tokens into one event model, kept as local JSONL. Browser extensions cover Claude.ai and ChatGPT; Claude Code, Cursor and Devin cloud agents and CI jobs are also supported.
- Loop: run agents, capture history, evaluate what worked, extract knowledge, human review and approval, reuse. Agents retrieve approved knowledge through MCP or Beacon Skills (Agent Skills).
- A local read-only dashboard shows traces. "Lenses" are sandboxed single-file HTML views of one trace (diffs, token bill, security review) that a coding agent can write.
- Installs via Homebrew, signed Linux packages or a Windows MSI.

## Weaknesses / caveats

- Interactive setup preselects Beacon Cloud, which forwards traces to Asymptote Labs; keeping data local means choosing Local. The confirm screen says so before forwarding starts.
- Setup also installs Beacon Skills into `~/.agents/skills` and `~/.claude/skills`, and with Cloud registers an MCP server in Claude Code, Codex CLI, Cursor, VS Code, Gemini CLI and OpenCode, unless turned off.
- The README warns that the lens sandbox cannot block every way a browser can send data out.
- No published measurement yet that the extracted knowledge improves agent results.

## Recent changes

- [2026-11-24] Page created from the agent-beacon README.

## Sources

- [Asymptote-Labs/agent-beacon (GitHub)](../sources/repos/asymptote-labs-agent-beacon.md)
```

### wiki/concepts/agent-memory.md (updated)

Frontmatter: `as_of: 2026-11-07` → `as_of: 2026-11-24`; append `asymptote-labs-agent-beacon` to `sources:`.

Heading: `## Current status (as of 2026-11-07)` → `## Current status (as of 2026-11-24)`.

Insert as a new Current-status bullet directly after the Cognition bullet:

```md
- Memory is starting to sit across harnesses rather than inside one. Asymptote Labs' open-source [Beacon](../tools/beacon.md) captures sessions from 20+ coding harnesses into one trace format, extracts workflows, corrections and repo conventions, has a human approve them, and serves them back to every harness through MCP or Agent Skills.
```

Recent changes: insert at the top, above the 2026-11-24 split entry:

```md
- [2026-11-24] Added cross-harness memory: [Beacon](../tools/beacon.md) turns session traces from 20+ coding harnesses into human-approved, shared knowledge.
```

Sources: append:

```md
- [Asymptote-Labs/agent-beacon (GitHub)](../sources/repos/asymptote-labs-agent-beacon.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter: `as_of: 2026-10-28` → `as_of: 2026-11-24`; append `asymptote-labs-agent-beacon` to `sources:`.

In the Agent memory row of the canonical-pages table, replace the last cell:

> **Before:** `| Supermemory, Engram, mem0, Letta, Cognition's Agent Memory Repo (no tool pages yet) |`
> **After:** `| [Beacon](../tools/beacon.md), Supermemory, Engram, mem0, Letta, Cognition's Agent Memory Repo |`

Recent changes: insert at the top:

```md
- [2026-11-24] Beacon added as the Agent memory row's first tool page (cross-harness, human-approved memory from coding-agent traces).
```

Remove the oldest entry (spilled, see below):

```md
- [2026-07-28] Added Supermemory Company Brain to the Company brain row's tracked examples, mirroring the new production example on that page.
```

Sources: append:

```md
- [Asymptote-Labs/agent-beacon (GitHub)](../sources/repos/asymptote-labs-agent-beacon.md)
```

### wiki/history/concepts/knowledge-architectures.md (new)

```md
# Knowledge architectures — history

## Archived from current page on <apply date>

- [2026-07-28] Added Supermemory Company Brain to the Company brain row's tracked examples, mirroring the new production example on that page.
```

### wiki/state-of/agents.md (updated)

Frontmatter: `as_of: 2026-11-23` → `as_of: 2026-11-24`; append `asymptote-labs-agent-beacon` to `sources:`.

Append under `### Knowledge platforms`:

```md
- [Beacon](../tools/beacon.md) — Asymptote Labs; open-source, local-first memory layer that captures sessions from 20+ coding harnesses and serves human-approved workflows and corrections back over MCP or skills; cloud forwarding is the setup default *(as of 2026-11-24)*
```

Recent changes: insert at the top:

```md
- [2026-11-24] Added [Beacon](../tools/beacon.md) to Knowledge platforms: Asymptote Labs' open-source memory layer shared across 20+ coding harnesses.
```

Remove the oldest entry (spilled, see below):

```md
- [2026-10-09] Added [Harness²](../tools/harness2.md) to Agent frameworks: Google's open-source recursive harnessing framework, frozen weights, up to +11.5 points on WorkBuddy-Bench.
```

### wiki/history/state-of/agents.md (updated)

Append at the end of the file (link re-pointed for the history path):

```md

## Archived from current page on <apply date>

- [2026-10-09] Added [Harness²](../../tools/harness2.md) to Agent frameworks: Google's open-source recursive harnessing framework, frozen weights, up to +11.5 points on WorkBuddy-Bench.
```

### wiki/index.md (updated)

Add under Tools, directly after the OpenWiki line:

```md
- [tools/beacon](tools/beacon.md) — Asymptote Labs' open-source, local-first memory layer for coding agents: captures sessions from 20+ harnesses, extracts human-approved workflows and corrections, serves them back over MCP or skills; cloud forwarding is the setup default *(as_of: 2026-11-24)*
```

In the agent-memory line, change "Cognition's Agent Memory Repo and Devin Dreaming;" to "Cognition's Agent Memory Repo and Devin Dreaming; cross-harness memory (Beacon);" and `as_of: 2026-11-07` → `as_of: 2026-11-24`. In the knowledge-architectures line, `as_of: 2026-10-28` → `as_of: 2026-11-24`.

### wiki/sources/repos/asymptote-labs-agent-beacon.md (new)

```md
---
title: Asymptote-Labs/agent-beacon (GitHub)
type: source
source_type: repo
source_file: raw/repos/asymptote-labs-agent-beacon.md
url: https://github.com/Asymptote-Labs/agent-beacon
ingested: 2026-11-24
domains: [agents, coding]
---

# Asymptote-Labs/agent-beacon (GitHub)

README of Beacon, Asymptote Labs' MIT-licensed "cross-harness, self-improving memory layer" for AI coding agents. It covers capture across about thirty local harnesses plus browser, cloud and CI agents; a normalized OpenTelemetry-based trace format stored as JSONL; a capture → evaluate → extract → review → reuse loop served through MCP and Agent Skills; a local dashboard with sandboxed lenses; and install paths. The README carries no date; captured 2026-11-23.

## Influenced pages
- [Beacon](../../tools/beacon.md) — new tool page
- [Agent memory](../../concepts/agent-memory.md) — cross-harness memory bullet
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — first tool page on the Agent memory row
- [State of Agents](../../state-of/agents.md) — Knowledge platforms line

## Key claims extracted
- Captures sessions, prompts, responses, tool calls, commands, file activity, approvals, MCP interactions and token usage from Claude Code, Cursor, Codex, OpenCode, Cline and 20+ other harnesses
- Knowledge loop: run agents → capture → evaluate → extract → review and approve → reuse across agents
- Approved knowledge served via MCP or Beacon Skills; local `beacon` MCP server never touches the network
- Interactive setup preselects Beacon Cloud (forwards to Asymptote Labs); Local is an explicit opt-out; signing in alone forwards nothing
- Setup installs skills into `~/.agents/skills` and `~/.claude/skills` and, with Cloud, registers `beacon-managed` MCP in six harnesses unless turned off
- Lenses: sandboxed single-file HTML views of a trace; sandbox cannot block every exfiltration path
```

## Schema / vocabulary additions

None.

## Open questions

None.
