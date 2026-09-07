---
type: proposal
source: raw/newsletters/2026-07-16-openais-new-model-for-cyber-attacks.md
status: pending
created: 2026-09-06
---

# Proposal: xAI open-sources Grok Build after an SSH-key upload scare

## Summary

### The source

A 2026-07-16 issue of The Code newsletter reports that developers caught xAI's Grok Build CLI coding agent uploading entire local directories — including SSH keys — to xAI's own servers. xAI disabled the offending feature and, in response, open-sourced the tool's full 844,530-line Rust codebase on GitHub, letting developers audit it, run it locally, and extend it with plugins and subagents. The newsletter reports this as a single short item alongside two unrelated launches (Thinking Machines' Inkling and OpenAI's GPT-Red, both covered in separate proposals) and gives no further detail on which feature caused the upload, how long it had been live, or whether any keys were confirmed misused.

### What changes

`tools/grok-build.md` currently describes Grok Build as an early-beta CLI agent with plan mode and parallel worktree subagents, most recently updated for the July 2026 Grok 4.5 launch — it has no record of this incident, since the original privacy scare was flagged in an earlier digest but never made it into a proposal.

- **Grok Build** gains a new caveat noting the incident and its resolution (feature disabled, full source opened), plus a Recent-changes entry dated 16 July. Page date moves to 16 July.
- **State of Cybersecurity** gains a new bullet under "AI-specific attack surfaces" — a coding agent silently uploading local secrets to its vendor's own servers, distinct from the page's existing prompt-injection and slopsquatting entries — plus a Recent-changes entry. Page date moves to 16 July, and because Recent changes is already one below cap, this entry pushes it to the cap exactly (no spill needed yet).
- One new source page for the newsletter.

### What to weigh

The newsletter is thin on specifics: no name for the offending feature, no timeline for how long directories were being uploaded, and no confirmation that any exposed keys were actually misused before the fix shipped. The proposal states only what's reported — the behavior, the fix, and the open-sourcing — and does not speculate about scope or impact beyond that.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/tools/grok-build.md` — add incident/resolution caveat, Recent-changes entry, bump as_of, merge source
    > See draft below

- [ ] **Update** `wiki/state-of/cybersecurity.md` — add "AI-specific attack surfaces" bullet for the incident, Recent-changes entry, bump as_of, merge source
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/spacexai-grok-build-open-source-2026-07-16.md` — source summary

## Page drafts

### wiki/tools/grok-build.md (updated)

Add to `## Weaknesses / caveats`:
```md
- **Security incident (resolved, July 2026):** developers caught Grok Build uploading entire local directories, including SSH keys, to xAI's servers. xAI disabled the offending feature and open-sourced the full 844,530-line Rust codebase on GitHub so developers can audit it, run it locally, and extend it with plugins and subagents.
```

Update frontmatter:
```yaml
as_of: 2026-07-16
sources: [grok-build-may-2026, spacex-cursor-june-2026, ainews-spacexai-grok-45-2026-07-09, spacexai-grok-build-open-source-2026-07-16]
```

Add to `## Recent changes` (top, newest first):
```md
- [2026-07-16] SSH-key upload incident: Grok Build was caught uploading entire local directories to xAI's servers; feature disabled, full 844,530-line Rust source opened on GitHub in response
```

### wiki/state-of/cybersecurity.md (updated)

Add to `### AI-specific attack surfaces`:
```md
- **Coding-agent local-data upload** — xAI's Grok Build CLI agent was caught uploading entire local directories, including SSH keys, to xAI's own servers; xAI disabled the feature and open-sourced the full agent (844,530 lines of Rust) so developers can audit what it does with local files. A different failure mode from indirect prompt injection: the risk here is an agent's own default behavior exfiltrating secrets to its vendor, not an attacker's injected instructions. See [Grok Build](../tools/grok-build.md). *(as of 2026-07-16)*
```

Update frontmatter:
```yaml
as_of: 2026-07-16
sources: [..., spacexai-grok-build-open-source-2026-07-16]
```
(append to the existing list; do not remove any current entries)

Add to `## Recent changes` (top, newest first):
```md
- [2026-07-16] Grok Build caught uploading entire local directories, including SSH keys, to xAI's servers; feature disabled and full Rust source (844,530 lines) opened on GitHub in response — added as a new coding-agent local-data-upload attack surface, distinct from prompt injection
```

### wiki/sources/newsletters/spacexai-grok-build-open-source-2026-07-16.md (new)

```md
---
title: "The Code — OpenAI's new model for cyber attacks"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-16-openais-new-model-for-cyber-attacks.md
published: 2026-07-16
ingested: 2026-09-06
domains: [cybersecurity, coding]
---

# The Code — OpenAI's new model for cyber attacks

The Code's 2026-07-16 issue covers three items: Thinking Machines' Inkling launch and OpenAI's GPT-Red (both in separate proposals), and — the item this page tracks — xAI's Grok Build being caught uploading local directories, including SSH keys, to xAI's servers, followed by the feature's removal and the full agent's open-sourcing on GitHub.

## Influenced pages

- [Grok Build](../../tools/grok-build.md) — incident/resolution caveat, Recent changes
- [State of Cybersecurity](../../state-of/cybersecurity.md) — new AI-specific attack surface bullet, Recent changes

## Key claims extracted

- Grok Build was caught uploading entire local directories, including SSH keys, to xAI's servers
- xAI disabled the offending feature and open-sourced the full agent: 844,530 lines of Rust, on GitHub
- Developers can now audit, run locally, and extend the agent with plugins and subagents
```

## Open questions

- Make sure to include in the Grok Build section that it is open source, thats very relevant if I need to research the codebase of a development harness.
