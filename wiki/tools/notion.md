---
title: Notion
type: tool
domains: [agents]
subcategory: agent-native-documents
tags: [agentic, collaboration]
as_of: 2026-05-14
sources: [notion-external-agents-api-may-2026]
---

# Notion

Notion is a widely used knowledge and collaboration workspace. As of May 2026, it has extended into agent-native territory: the External Agents API lets third-party AI agents (Claude Code, Codex, Cursor, Devin, Warp, Decagon) operate directly inside Notion workspaces as a shared, reviewable context layer rather than treating Notion as a static read-only knowledge base.

## Current status (as of 2026-05-14)

- **External Agents API**: enables Claude Code, Cursor, Codex, Devin, Warp, and Decagon to read and act inside Notion workspaces — agents treat Notion as a shared context layer with human reviewability built in
- **Workers**: custom code runs in a secure sandbox; supports syncing live data from any API and deploying custom agent logic inside the Notion surface
- **CLI**: developer tooling for building and deploying Workers
- Free through August 2026 on Business and Enterprise plans

## Strengths

- Major installed base: enterprise and SMB teams already use Notion as a knowledge hub, so agents operate where the work already lives
- Shared context model: human and agent edits appear in the same surface with revision history — closer to the agent-native document ideal than pasting AI output into a doc

## Weaknesses / caveats

- Workers and External Agents API are new; depth of integration with each named agent partner is unverified beyond launch announcements
- Free-through-August pricing suggests the commercial model for agent integrations is not yet settled

## Recent changes

- [2026-05-14] Developer Platform launched: External Agents API, Workers (secure sandbox), CLI; agent partners include Claude Code, Cursor, Codex, Devin, Warp, Decagon

## Sources

- [Notion External Agents API launch — May 2026](../sources/newsletters/notion-external-agents-api-may-2026.md)
