---
type: proposal
sources:
  - raw/newsletters/2026-06-17-copilot-cowork-becomes-generally-available.md
  - raw/newsletters/2026-06-17-ainews-glm-52-the-top-frontend-coding-model-in.md
status: pending
created: 2026-06-17
---

# Proposal: SpaceX acquires Cursor + Cursor Origin launch

## Summary

SpaceX exercised a previously announced option to acquire Cursor in a $60B all-stock deal. A jointly trained model is coming to both Cursor and Grok Build. Cursor also launched Origin — a git/code hosting product designed for agent workloads. This creates a vertically integrated coding stack (xAI model + Cursor IDE + Origin code hosting) competing directly with Claude Code + Anthropic and Codex + OpenAI.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — add SpaceX acquisition, Cursor Origin, jointly trained model
- [x] **Update** `wiki/tools/grok-build.md` — note jointly trained model from SpaceX/Cursor collaboration
- [x] **Update** `wiki/state-of/coding.md` — update Cursor entry; add recent change
- [x] **Create** `wiki/sources/newsletters/spacex-cursor-june-2026.md` — source summary

## Page drafts

### wiki/tools/cursor.md (updated sections)

> **Frontmatter: update `as_of` to 2026-06-17; add `spacex-cursor-june-2026` to sources.**

> **Add new section after "Cursor SDK" section:**

```markdown
## SpaceX acquisition and Cursor Origin (June 2026)

SpaceX exercised a previously announced option to acquire Cursor in an all-stock $60B deal. Key implications:

- **Jointly trained model.** SpaceX/xAI and Cursor have been co-training a new model that will power both Cursor and Grok Build.
- **Cursor Origin.** Launched alongside the acquisition news: a git/code hosting product built for agent workloads. Features merge conflict handling optimized for agent-generated commits, MCP/API extensibility, team-agent collaboration surfaces, and audit trails. Designed as the natural storage layer for autonomous agent work.
- **Vertical integration.** The combined stack is model (xAI jointly trained) + IDE (Cursor) + code hosting (Origin), competing with Claude Code + Anthropic (model + terminal agent) and Codex + OpenAI (model + cloud agent).
```

> **Current status section — update header date and add bullet:**

> **Before:** `## Current status (as of 2026-04-14)`
> **After:** `## Current status (as of 2026-06-17)`

> **Add to Current status bullet list:**
```
- **SpaceX acquisition (June 2026):** $60B all-stock deal; model co-training with xAI underway; expected to power both Cursor and Grok Build
- **Cursor Origin (June 2026):** agent-native git/code hosting; MCP/API extensible; team-agent collaboration and merge conflict handling built for autonomous agent commits
```

> **Add to ## Recent changes (prepend):**
```
- [2026-06-17] SpaceX acquires Cursor in $60B all-stock deal; Cursor Origin launched (agent-native git/code hosting); jointly trained model with xAI coming to Cursor and Grok Build
```

> **Spill oldest entry from Recent changes to `wiki/history/tools/cursor.md` if cap exceeded.**

### wiki/tools/grok-build.md (updated sections)

> **Frontmatter: update `as_of` to 2026-06-17; add `spacex-cursor-june-2026` to sources.**

> **Current status — add bullet:**
```
- **Jointly trained model (June 2026):** SpaceX/xAI is co-training a new model with Cursor that will power Grok Build; expected to represent a significant capability upgrade from the current xAI model backend
```

> **Add to ## Recent changes:**
```
- [2026-06-17] Grok Build to receive jointly trained model from SpaceX/Cursor collaboration
```

### wiki/state-of/coding.md (updated section)

> **Agentic coding workspace — update Cursor entry:**

> **Before:**
```
- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK now exposes the runtime headlessly for CI, automations, cloud VMs, and embedded product agents; 35% of Cursor's internal PRs from cloud agents *(as of 2026-04-30)*
```
> **After:**
```
- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting; jointly trained model with xAI coming *(as of 2026-06-17)*
```

> **Add to ## Recent changes (prepend):**
```
- [2026-06-17] SpaceX acquires Cursor ($60B all-stock); Cursor Origin launched (agent-native git/code hosting); jointly trained xAI model coming to both Cursor and Grok Build — completes a model + IDE + hosting vertical stack
```

> **Update `as_of` to 2026-06-17 and add `spacex-cursor-june-2026` to sources.**

### wiki/sources/newsletters/spacex-cursor-june-2026.md (new)

````md
---
title: SpaceX acquires Cursor + Cursor Origin launch (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-17-copilot-cowork-becomes-generally-available.md
published: 2026-06-17
ingested: 2026-06-17
domains: [coding, agents]
---

# SpaceX acquires Cursor + Cursor Origin launch (June 2026)

Coverage of the $60B SpaceX/Cursor all-stock acquisition and the launch of Cursor Origin, an agent-native git/code hosting product.

## Influenced pages

- [Cursor](../../tools/cursor.md) — acquisition, Origin, jointly trained model
- [Grok Build](../../tools/grok-build.md) — jointly trained model note
- [State of Coding](../../state-of/coding.md) — Cursor entry updated

## Key claims extracted

- SpaceX exercised previously announced option; $60B all-stock deal
- Jointly trained model from SpaceX/xAI + Cursor; will power both Cursor and Grok Build
- Cursor Origin: agent-native git/code hosting with merge conflict handling, MCP/API, team-agent collaboration
- SpaceX IPO same week: $2.1T valuation (largest IPO on record)
````
