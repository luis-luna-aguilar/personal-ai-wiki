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
