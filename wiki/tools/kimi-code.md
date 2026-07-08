---
title: Kimi Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [moonshot-ai, open-source, open-weights]
as_of: 2026-06-19
sources: [ainews-frontiercode-june-2026, kimi-goal-mode-creative-agents-2026-06]
---

# Kimi Code

Moonshot AI's open-source coding agent, updated June 2026 with significant new capabilities. Powered by the [Kimi K2.7-Code](../models/kimi-k2-7-code.md) open-weight model. Accompanied by a separate desktop agent product, Kimi Work.

## Current status (as of 2026-06-09)

- Open-source coding agent from Moonshot AI (China)
- **1-line CLI install** — lowest barrier-to-entry install of any major coding agent
- **Video as coding context** — drag-and-drop video files as context for coding tasks (unique among major coding agents)
- **ACP support** — Agent Communication Protocol; enables cross-agent coordination
- **Plugins and IDE integration** — extends beyond CLI to IDE surfaces
- Powered by Kimi K2.7-Code (1T/32B MoE, 256K context, open-weight)

## Kimi Work (companion desktop agent)

Kimi Work is Moonshot's desktop agent product, launched the same week:
- Up to 300 local sub-agents running in parallel
- Browser-use via extension (no separate computer-use model required)
- Finance-focused tool access
- Persistent memory across sessions
- **Goal Mode:** keeps the desktop agent working until it reaches a user-defined objective; the user tracks progress, reviews deliverables, and redirects as needed. The feature is positioned for long-horizon, multi-step work.

## Strengths

- Most accessible CLI install among major coding agents
- Video-as-context is a genuinely novel input modality for coding
- Open-source + open-weight model means self-hosting is feasible for compliance-sensitive teams
- ACP support positions it for multi-agent integration patterns
- Kimi Work's 300-sub-agent ceiling is one of the largest reported local agent concurrencies

## Weaknesses / caveats

- Moonshot is a Chinese lab; some teams have sovereignty or regulatory constraints on Chinese-origin tooling
- Kimi Work desktop agent is early; finance-focused tool access scope not fully published
- ACP is an emerging standard; interoperability outside the Kimi ecosystem is limited at launch

## Recent changes

- [2026-06-19] Kimi Work adds Goal Mode for long-running desktop-agent tasks that continue until the objective is reached.
- [2026-06-09] Major update: 1-line CLI, video-as-context, ACP, plugins, IDE integration
- [2026-06-09] Kimi Work desktop agent launched alongside: 300 local sub-agents, browser-use, finance tools, persistent memory

## Sources

- [AINews — FrontierCode launch (June 9)](../sources/newsletters/ainews-frontiercode-june-2026.md)
- [Kimi Work Goal Mode and creative desktop agents](../sources/newsletters/kimi-goal-mode-creative-agents-2026-06.md)
