---
type: proposal
source: raw/newsletters/2026-06-09-ainews-frontiercode-benchmarking-for-code-quali.md
status: pending
created: 2026-06-17
---

# Proposal: Kimi Code + Kimi Work

## Summary

Moonshot AI shipped two products in the same week as Fable 5 launch. Kimi Code: a major update to their open-source coding agent — 1-line CLI install, drag-and-drop video as coding context, ACP (Agent Communication Protocol) support, plugins, IDE integration. Kimi Work: a new desktop agent product with up to 300 local sub-agents, browser-use via extension, finance-focused tool access, and persistent memory. These are product/tool releases distinct from the Kimi K2.7-Code model (already in the wiki).

## Intended changes

- [x] **Create** `wiki/tools/kimi-code.md` — new tool page covering both Kimi Code and Kimi Work
    > See draft below

- [x] **Update** `wiki/state-of/coding.md` — add Kimi Code to terminal-coding-agent section
    > **Before** (end of terminal coding agent section, after Grok Build entry):
    > (no Kimi Code entry)
    > **After** (append new entry):
    > `- [Kimi Code](../tools/kimi-code.md) — Moonshot AI; open-source; 1-line CLI; video-as-coding-context; ACP support; IDE integration; powered by Kimi K2.7-Code model *(as of 2026-06-09)*`

- [x] (Source already created as `wiki/sources/newsletters/ainews-frontiercode-june-2026.md` in the FrontierCode proposal)

## Page drafts

### wiki/tools/kimi-code.md (new)

```md
---
title: Kimi Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [moonshot, open-source, open-weights]
as_of: 2026-06-09
sources: [ainews-frontiercode-june-2026]
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

- [2026-06-09] Major update: 1-line CLI, video-as-context, ACP, plugins, IDE integration
- [2026-06-09] Kimi Work desktop agent launched alongside: 300 local sub-agents, browser-use, finance tools, persistent memory

## Sources

- [AINews — FrontierCode launch (June 9)](../sources/newsletters/ainews-frontiercode-june-2026.md)
```
