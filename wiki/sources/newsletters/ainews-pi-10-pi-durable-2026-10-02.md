---
title: AINews — Pi 1.0 and Pi Durable
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-02-ainews-pi-10-pi-durable-and-aie-nyc.md
published: 2026-10-02
ingested: 2026-10-20
domains: [agents, coding]
---

# AINews — Pi 1.0 and Pi Durable

The lead story of the 2 October 2026 AINews issue: Earendil, which the Pi harness joined, shipped Pi 1.0 and Pi Durable, both reaching the Hacker News front page. The issue lists Pi 1.0's features and describes Pi Durable as a TypeScript port that externalizes all of Pi's stateful components.

## Influenced pages

- [Pi](../../tools/pi.md) — new page
- [Agent runtime platforms](../../concepts/agent-runtime-platforms.md) — durable-harness section
- [State of Agents](../../state-of/agents.md) — Pi added under Agent frameworks

## Key claims extracted

- Pi 1.0: code mode (native MCP, Jev, image models), extension support for virtual models, deferred tool loading, cache warming for Anthropic models, mid-conversation system messages, new TUI theme, full-screen by default
- Pi Durable: every step recorded as a checkpointed task; agents and subagents resume from their last exact state after a failure or restart
- Runs on any JavaScript runtime (Node, Bun, Cloudflare); pluggable storage (memory, SQLite, JSONL); local or remote execution environments
- Parallel branching conversations in one harness; installable Extensions bundling prompts, tools, hooks, and durable tasks
- Background compaction; app state stored beside transcripts for multiplayer steering; hot-swapping tool and extension code mid-run
