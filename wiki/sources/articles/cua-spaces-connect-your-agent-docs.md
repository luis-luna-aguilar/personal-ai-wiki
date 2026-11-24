---
title: Cua docs — Connect your agent
type: source
source_type: article
source_file: raw/articles/2026-11-23-cuaai-docs-spaces-guides-connect-your-agent.md
url: https://cua.ai/docs/spaces/guides/connect-your-agent
ingested: 2026-11-24
domains: [computer-use, agents]
---

# Cua docs — Connect your agent

Cua's guide to connecting coding agents to Cua Spaces. Setup (app or `cua connect setup`) writes a `cua` MCP server and skills into each agent's settings; agents can then create Spaces, run commands, send files, stream the desktop, teleport a signed-in browser session, share Spaces read-only, and start nested Claude Code or Codex runs. Most of the page explains how credentials are kept out of Spaces. The page carries no publication date; it was fetched on 2026-11-23.

## Influenced pages
- [Cua](../../tools/cua.md) — new tool page
- [State of Computer Use](../../state-of/computer-use.md) — new Cua leader line
- [Agent execution runtimes](../../concepts/agent-execution-runtimes.md) — nested agent runs and credential isolation

## Key claims extracted
- Supported agents include Claude Code, Codex, Cursor, Gemini CLI, Hermes and OpenClaw; any other can add `cua daemon mcp` by hand.
- Main MCP tools: `list_spaces`/`create_space`, `space_bash`, `send_file`, `stream_endpoint`, `teleport_browser_session`, `share_space`, `delete_space`.
- `agent_start`, `agent_message`, `agent_status`, `agent_stop` run Claude Code or Codex inside a Space; runs survive the client going away. TypeScript: `startThread` from `@trycua/cua/spaces`.
- Host credential files are never copied into a Space; a run gets only the saved key its harness reads, or keys named in `env_from_host`; keys are written 0600 and redacted from the run log.
- Key management methods are daemon methods, not MCP tools: no agent can read, add or remove a key.
- Claude plan reuse: Cua copies only the access token, never the refresh token, and never refreshes, so the user's own Claude Code stays signed in; copying to other computers is off by default.
- `--permissions spaces:readonly` limits an agent to read-only use; `space_bash`, `send_file`, `teleport_app` and `hotspot_start` act with the user's authority.
