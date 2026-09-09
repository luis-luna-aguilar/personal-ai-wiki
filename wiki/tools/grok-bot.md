---
title: Grok Bot
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [xai, agentic]
as_of: 2026-09-05
sources: [ainews-spacexai-grok-46-and-grok-bot-2026-08-13, latent-space-grok-bot-openclaw-2026-09-05]
---

# Grok Bot

xAI's (SpaceXAI) entry into the AI-teammate/multiplayer-agent category, launched 2026-08-13 alongside its underlying model, [Grok 4.6](../models/grok-4-6.md). Described as "AI teammates with their own cloud computers": agents that can log into tools, watch Slack and GitHub Actions, run scheduled routines, and spawn other bots. Positioned against Anthropic's Claude Tag; AINews read the strength of early reviews as validation that the AI-teammate space is the next major agent-product battleground.

## Current status (as of 2026-08-13)

- Runs on Grok 4.6; launched the same day to what AINews describes as "very positive reviews"
- Core capabilities per the launch coverage: persistent cloud compute per bot, tool/service login, monitoring of Slack and GitHub Actions, scheduled routines, and bot-spawning
- Tied to the Cursor↔SpaceX/xAI relationship — the same team that shipped Grok 4.5 co-trained with Cursor

## Hands-on review (as of 2026-09-05)

A five-day Latent Space review (against OpenClaw 2.0, see [OpenClaw](openclaw.md)) found:

- Near-zero setup for connectors: open the plugin catalog, sign in through a normal browser login, done — no MCP server JSON, no pasted API credentials
- Runs on an always-on hosted cloud computer per Bot; state and sessions persist across devices with no server for the user to maintain
- "Bots," not code, are the programmable unit: each gets a name, role, and identity, and multiple Bots compose into a "group chat" that can route work between them (e.g. an Agentic Engineer Bot routing design work to Claude Code, debugging to Codex)
- Tradeoffs: no model picker (routing happens behind the scenes), no manual context/compaction control the way Claude Code or Codex expose
- Security-relevant caveat: every Bot on an account shares the same underlying computer, files, browser sessions, and logins — separate Bots are an organizational boundary, not a security boundary
- Reviewer's verdict: strong as a low-setup "digital chief of staff" for admin, summarizing, and project tracking; not yet a replacement for direct-control tools on deep implementation work

## Why it matters

A new named entrant to the AI-teammate/multiplayer-agent category the wiki already tracks via [Claude Tag](claude-tag.md) — see [State of Agents](../state-of/agents.md).

## Recent changes

- [2026-09-05] Latent Space's five-day hands-on review: near-zero-setup connectors, Bot-as-atomic-unit design, shared-computer/session caveat (org boundary, not security boundary), and a "useful for shallow work, not deep implementation" verdict.
- [2026-08-13] Launched alongside Grok 4.6: "AI teammates with their own cloud computers," positioned against Claude Tag

## Sources

- [AINews — SpaceXAI Grok 4.6 and Grok Bot](../sources/newsletters/ainews-spacexai-grok-46-and-grok-bot-2026-08-13.md)
- [Latent Space — OpenClaw Power, MacBook Simplicity: Five Days With Grok Bot](../sources/newsletters/latent-space-grok-bot-openclaw-2026-09-05.md)
