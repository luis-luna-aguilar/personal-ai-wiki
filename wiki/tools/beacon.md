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
