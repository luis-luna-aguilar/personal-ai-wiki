---
type: proposal
source: raw/newsletters/2026-05-19-ainews-how-to-land-a-job-at-a-frontier-lab-on-p.md
status: pending
created: 2026-05-19
---

# Proposal: Codex new workflow integrations — Zoom plugin, keep-Mac-awake, mobile improvements

## Summary

Minor Codex update: (1) Zoom plugin for meeting-context handoffs — agents can receive context from meetings directly; (2) "keep your Mac awake" support so longer-running jobs continue from the phone app without the laptop sleeping; (3) additional mobile/desktop remote execution improvements. Extends the remote mobile supervision story already tracked in the wiki.

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add Zoom plugin, keep-awake support, and mobile improvements to `## Current status`; update `## Recent changes`
    > See diff below

- [x] **Create** `wiki/sources/newsletters/codex-zoom-mobile-2026-05.md` — source summary

## Page drafts

### wiki/tools/codex.md — additions to `## Current status`

Add after the existing mobile preview bullet:

```md
- Zoom plugin (May 2026): agents can receive meeting context directly from Zoom — handoff pattern for meeting → task delegation without manual copy-paste
- "Keep Mac awake" support: longer-running Codex jobs continue without interruption when supervising from the phone app; prevents laptop sleep from terminating sessions
```

Update `as_of` in frontmatter to `2026-05-19`.

Add to `## Recent changes`:

```
- [2026-05-19] Zoom plugin (meeting-to-task context handoffs), keep-Mac-awake for long-running remote sessions, additional mobile remote-execution improvements
```

### wiki/sources/newsletters/codex-zoom-mobile-2026-05.md (new)

```md
---
title: Codex Zoom plugin + keep-Mac-awake — AINews (May 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-19-ainews-how-to-land-a-job-at-a-frontier-lab-on-p.md
url: https://twitter.com/OpenAIDevs
published: 2026-05-19
ingested: 2026-05-19
domains: [coding]
---

# Codex Zoom plugin + keep-Mac-awake — AINews (May 2026)

Minor Codex workflow update covered in AINews: Zoom plugin for meeting-context handoffs; "keep your Mac awake" support for long-running jobs supervised from the phone app; additional mobile/desktop remote execution improvements.

## Influenced pages

- [Codex](../../tools/codex.md) — Zoom plugin, keep-awake, mobile improvements

## Key claims extracted

- Zoom plugin: meeting context → agent task without manual handoff
- Keep Mac awake: long-running sessions survive when user is on phone app
- Additional mobile/desktop remote execution improvements (details thin in source)
```
