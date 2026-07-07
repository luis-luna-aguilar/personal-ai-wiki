---
title: Shepherd
type: tool
domains: [agents, coding]
subcategory: agent-framework
tags: [open-source, agentic]
as_of: 2026-07-06
sources: [shepherd-live-agent-rollback-2026-07-06]
---

# Shepherd

Shepherd is an open-source tool described as Git-like version control for live AI agent runs. Its core idea is to let teams checkpoint, rollback, and fork agent trajectories while the agent is operating, rather than treating each run as an all-or-nothing transcript.

## Current status (as of 2026-07-06)

- Positioned around live agent recovery: save a run state, return to it, and branch from there.
- Relevant to long-running coding agents where a late bad decision can poison a session.
- Fits the broader shift from "loop forever" prompts toward explicit loop-control primitives.

## Strengths

- Makes failed or drifting agent trajectories easier to recover.
- Gives teams a concrete mental model: version-control semantics for agent state.

## Weaknesses / caveats

- Current source is a tweet-forward; verify the repository for implementation details before relying on it operationally.
- The wiki should treat it as an emerging tool, not a proven category leader.

## Recent changes

- [2026-07-06] Added as an emerging live-agent rollback/forking tool.

## Sources

- [Shepherd live agent rollback tweet](../sources/tweets/shepherd-live-agent-rollback-2026-07-06.md)
