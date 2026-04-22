---
title: Coding agents move toward review and concurrent supervision
type: source
source_type: newsletter
source_file: raw/newsletters/2026-03-10-anthropic-drops-claude-code-review.md
published: 2026-03-10
ingested: 2026-04-22
domains: [coding, agents]
---

# Coding agents move toward review and concurrent supervision

This source summary groups an early-March cluster on how coding-agent products were starting to change shape. The common signal is that the center of gravity was moving away from "ask for code in one thread" and toward supervised, concurrent, and reusable workflows: multi-agent review, side-channel supervision, and explicit operating guidance for durable agent setup.

## Influenced pages

- [[tools/claude-code]] — adds the March Code Review and `/btw` signals as early evidence of the product's supervision direction
- [[tools/codex]] — grounds the product's AGENTS.md / MCP / skills / automation framing in an earlier first-party guide

## Key claims extracted

- Claude Code Review launched as a managed multi-agent PR-review system that verifies findings and ranks them by severity
- Anthropic reported substantive PR comments increasing from 16% to 54% internally after adopting that workflow
- `/btw` introduced side-chain conversations during active Claude Code work, making supervision less serial
- OpenAI's Codex guide framed durable repo guidance, external context connections, skills, review, and automation as core workflow primitives rather than niche setup
