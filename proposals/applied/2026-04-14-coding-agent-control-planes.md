---
type: proposal
source: internal — synthesized from raw/newsletters/2026-04-14-cursor-changes-how-you-code-with-agents.md, raw/newsletters/2026-04-14-ainews-top-local-models-list-april-2026.md, raw/newsletters/2026-04-10-ainews-ai-engineer-europe-2026.md
status: pending
created: 2026-04-14
---

# Proposal: Coding agent control planes

## Summary

This signal sharpens a pattern already present in the wiki: coding tools are increasingly differentiated by how they supervise many agents, not just by how well one model edits one file. Cursor 3.1's tiled agents window is the most concrete product change in this batch, while the supporting commentary frames orchestration, observability, and evaluator-backed long-running workflows as the new surface area.

The right move is to update existing coding and agent pages rather than create a new concept page.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — add Cursor 3.1's tiled Agents Window, branch selection for cloud agents, and stronger framing around supervision as product direction
  > See diff snippet below.

- [x] **Update** `wiki/state-of/coding.md` — refresh the Cursor line and recent-changes section to reflect the shift from IDE-plus-AI toward agent control planes
  > See diff snippet below.

- [x] **Update** `wiki/state-of/agents.md` — refresh Cursor's orchestration-UI line with the 3.1 control-plane update
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/coding-agent-control-planes.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/tools/cursor.md (updated snippet)

```markdown
---
title: Cursor
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [closed-source, agentic]
as_of: 2026-04-14
sources: [cursor-3-launch, cursor-pr-demos, cursor-bugbot-learning, coding-agent-control-planes]
---

## Current status (as of 2026-04-14)

- **Cursor 3.1** extends Cursor 3's agent-first workspace with a tiled Agents Window for managing multiple agents side by side
- Branch selection for cloud agents and improved search/filter controls make the cloud-agent layer feel more like a supervision surface than a background feature
- ...

## What's new in Cursor 3.1

- **Tiled Agents Window.** Run multiple coding agents in draggable panes and compare outputs without tab-switching
- **Saved layout.** The workspace remembers how the human wants to supervise ongoing agent work
- **Branch selection for cloud agents.** More explicit control over where remote work lands
- **Improved search filters.** Better navigation across the agent workspace

## Recent changes

- [2026-04-14] Cursor 3.1 added a tiled Agents Window, saved layouts, branch selection for cloud agents, and stronger supervision controls for parallel agent work
- [2026-04-10] Bugbot learned rules: ...
```

### wiki/state-of/coding.md (updated snippet)

```markdown
### Agentic coding workspace

- [[tools/cursor]] — Cursor 3.1 pushes the category further toward a true agent control plane: tiled multi-agent supervision, cloud-agent branch control, and stronger workspace-level orchestration *(as of 2026-04-14)*
- [[tools/orca]] — ...

## Recent changes

- [2026-04-14] Cursor 3.1 added tiled multi-agent supervision and stronger control-plane UX, reinforcing the shift from AI-enhanced IDEs toward agent workspaces
```

### wiki/state-of/agents.md (updated snippet)

```markdown
### Agent orchestration UIs

- [[tools/cursor]] — Cursor 3.1's tiled Agents Window, saved layouts, and cloud-agent branch control make the workspace feel increasingly like a human supervision layer for many coding agents rather than a single-agent IDE *(as of 2026-04-14)*
- ...
```

### wiki/sources/newsletters/coding-agent-control-planes.md (new)

```markdown
---
title: Coding agent control planes
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-14-cursor-changes-how-you-code-with-agents.md
ingested: 2026-04-14
domains: [coding, agents]
---

# Coding agent control planes

This source summary captures the shift from single-agent coding tools toward supervision layers for multiple concurrent agents. Cursor 3.1 is the clearest concrete example in the source set, while the surrounding commentary generalizes the pattern to orchestration, observability, and evaluator-backed long-running tasks.

## Influenced pages

- [[tools/cursor]] — adds Cursor 3.1's tiled multi-agent supervision UI
- [[state-of/coding]] — refreshes the current-state description of `agentic-coding-workspace`
- [[state-of/agents]] — strengthens Cursor's placement under `Agent orchestration UIs`

## Key claims extracted

- Cursor 3.1 adds a tiled Agents Window for supervising multiple coding agents in parallel
- Cloud-agent branch selection and improved file/search controls make remote agent work more explicit and controllable
- The broader commentary treats orchestration, observability, and evaluator-backed long-running workflows as the real differentiators in coding tools
```

## Schema / vocabulary additions

- None proposed.
