---
title: Cua
type: tool
domains: [computer-use, agents]
subcategory: computer-use
tags: [open-source, agentic, cli]
as_of: 2026-11-24
sources: [cua-spaces-connect-your-agent-docs, trycua-cua-repo-2026-11, ainews-cua-s1-forms-2026-09-19]
---

# Cua

Open computer-use infrastructure from Cua AI: a desktop app (Cua Spaces) that gives agents their own full desktops, a background driver for native apps (Cua Driver), a cross-language sandbox SDK and `cua` CLI, a benchmark suite (cua-bench), and small open decision models for computer use (CUA-S1).

## Current status (as of 2026-11-24)

- **Spaces.** Each Space is a macOS VM built locally on a Mac, or a Linux image, running on the user's own computers (reachable through a cua.ai relay) or in their own AWS, Google Cloud or Modal account. A signed-in app such as Chrome or Slack can be "teleported" into a Space and stays signed in; people and agents can share one desktop with separate cursors. Free for individuals, Pro $18/month, Teams $30/seat/month.
- **Driven by coding agents over MCP.** Setup adds a `cua` MCP server and skills to Claude Code, Codex, Cursor, Gemini CLI, Hermes, OpenClaw and others. Agents create Spaces, run commands (`space_bash`), upload files, stream the desktop, move a browser session in (`teleport_browser_session`) and share a Space read-only. A `spaces:readonly` permission scope limits agents that only need to look.
- **Nested agent runs.** An agent can start long-lived Claude Code or Codex runs inside a Space (`agent_start` / `agent_message`, or `startThread` in the TypeScript SDK); runs live in the guest and survive the client going away.
- **Credential isolation.** Host credential files are never copied into a Space. Each run gets only the saved provider key its harness reads, keys are written 0600 and redacted from logs, and key management is not exposed as MCP tools, so no agent can read or change keys. To reuse a Claude plan, Cua copies only the short-lived access token and never refreshes it, so the user's own Claude Code stays signed in.
- **CUA-S1-FORMS (September 2026).** First of Cua's small "System 1" [decision models](../concepts/decision-models.md) for computer use: it scores form-filling decisions (which value goes in which field, which elements to leave alone) from structured UI elements instead of generating tokens; application code orders the actions and Cua Driver executes them. MIT code; weights and a synthetic dataset on Hugging Face.

## Weaknesses / caveats

- Spaces itself is source-available (FSL-1.1-MIT, MIT after two years), not MIT like the rest of the repo.
- CUA-S1 is labelled an early research release, not a replacement for a general agent's planning.
- Several older Cua packages are deprecated; `cuabot` has known security issues and Cua says to uninstall it.

## Recent changes

- [2026-11-24] Page created: Cua Spaces 0.9.4 docs (agent-driven desktop VMs over MCP, nested runs, credential isolation) and the CUA-S1-FORMS decision model.

## Sources

- [Cua docs — Connect your agent](../sources/articles/cua-spaces-connect-your-agent-docs.md)
- [trycua/cua GitHub README](../sources/repos/trycua-cua-repo-2026-11.md)
- [AINews — Cua open-sources CUA-S1-FORMS](../sources/newsletters/ainews-cua-s1-forms-2026-09-19.md)
