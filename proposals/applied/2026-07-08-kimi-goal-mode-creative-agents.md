---
type: proposal
source: raw/newsletters/2026-06-19-kimis-agent-now-works-247.md
status: pending
created: 2026-07-08
---

# Proposal: Kimi Work Goal Mode and creative desktop agents

## Summary

Moonshot added Goal Mode to Kimi Work, while Palmier and Adobe show agentic workflows entering creative desktop tools. This is a lightweight ingest updating Kimi Code/Kimi Work, agents, and creative state.

## Intended changes

- [x] **Update** `wiki/tools/kimi-code.md` — add Kimi Work Goal Mode.
- [x] **Update** `wiki/state-of/agents.md` — refresh Kimi Work under agent orchestration.
- [x] **Update** `wiki/state-of/creative.md` — add Palmier and Adobe Firefly Assistant as lightweight creative-agent signals.
- [x] **Create** `wiki/sources/newsletters/kimi-goal-mode-creative-agents-2026-06.md` — source summary.

## Page drafts

### wiki/tools/kimi-code.md (updated sections)

```md
---
title: Kimi Code
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: [moonshot-ai, open-source, open-weights]
as_of: 2026-06-19
sources: [ainews-frontiercode-june-2026, kimi-goal-mode-creative-agents-2026-06]
---

## Kimi Work (companion desktop agent)

Kimi Work is Moonshot's desktop agent product:
- Up to 300 local sub-agents running in parallel
- Browser-use via extension (no separate computer-use model required)
- Finance-focused tool access
- Persistent memory across sessions
- **Goal Mode:** keeps the desktop agent working until it reaches a user-defined objective; the user tracks progress, reviews deliverables, and redirects as needed. The feature is positioned for long-horizon, multi-step work.

## Recent changes

- [2026-06-19] Kimi Work adds Goal Mode for long-running desktop-agent tasks that continue until the objective is reached.
- [2026-06-09] Major update: 1-line CLI, video-as-context, ACP, plugins, IDE integration
```

### wiki/state-of/agents.md (updated sections)

```md
### Agent orchestration

- [Kimi Work](../tools/kimi-code.md) — Moonshot AI desktop agent companion to Kimi Code; Goal Mode keeps work running until a user-defined objective is reached, with progress tracking and redirection *(as of 2026-06-19)*

## Recent changes

- [2026-06-19] Kimi Work adds Goal Mode, a long-running desktop-agent loop that continues until the user-defined objective is reached.
- [2026-07-08] Google managed agents in the Gemini API add MCP support, background execution, custom function calling, and credential refresh, making hosted agent runtime features first-party Gemini primitives.
```

### wiki/state-of/creative.md (updated sections)

```md
### AI video generation

- **Palmier** — Mac-native video editor where Claude or Codex can generate, organize, and trim footage directly in-app; integrates leading video models such as Seedance 2.0, Kling V3, and Grok Imagine. Current evidence is newsletter coverage only *(as of 2026-06-19)*

### Visual design & prototyping

- **Adobe Firefly AI Assistant** — Adobe assistant that executes multi-step creative tasks across Premiere, Photoshop, InDesign, and other Adobe apps, with expansion planned to ChatGPT, Claude, Gemini, Copilot, and Slack. Current evidence is newsletter coverage only *(as of 2026-06-19)*

## Recent changes

- [2026-06-19] Palmier and Adobe Firefly Assistant show creative tooling moving toward agentic desktop workflows: video editing and multi-app creative tasks executed from natural-language instructions.
- [2026-07-08] Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp and previewed Muse Video; AINews describes an agentic generation loop with planning, tool use, code execution, and self-refinement.
```

### wiki/sources/newsletters/kimi-goal-mode-creative-agents-2026-06.md (new)

```md
---
title: Kimi Work Goal Mode and creative desktop agents
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-19-kimis-agent-now-works-247.md
url: https://www.superhuman.ai/
published: 2026-06-19
ingested: 2026-07-08
domains: [agents, creative]
tags: [moonshot-ai]
---

# Kimi Work Goal Mode and creative desktop agents

Superhuman reports that Moonshot AI added Goal Mode to Kimi Work, keeping the desktop agent running until it reaches a user-defined objective. The same issue reports Palmier's Mac-native AI video editor and Adobe Firefly AI Assistant's multi-step execution across Adobe creative apps.

## Influenced pages

- [Kimi Code](../../tools/kimi-code.md) — adds Kimi Work Goal Mode.
- [State of Agents](../../state-of/agents.md) — adds Kimi Work long-running agent signal.
- [State of Creative](../../state-of/creative.md) — adds lightweight Palmier and Adobe creative-agent entries.

## Key claims extracted

- Kimi Work Goal Mode keeps working until the task objective is reached.
- Users can track progress, review deliverables, and redirect the agent.
- Palmier is a Mac-native video editor where Claude or Codex can generate, organize, and trim footage in-app.
- Adobe Firefly AI Assistant can execute multi-step tasks across Premiere, Photoshop, InDesign, and related tools.
```

## Schema / vocabulary additions

None.
