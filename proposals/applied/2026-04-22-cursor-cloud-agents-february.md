---
type: proposal
source: raw/newsletters/2026-02-26-cursor-agents-get-their-own-computers.md
status: pending
created: 2026-04-22
---

# Proposal: Cursor cloud agents in late February

## Summary

The March 6 walkthrough already captured Cursor's supervision-first thesis, but this earlier late-February cluster adds a useful "arrival" moment: cloud agents in isolated VMs, demo videos, and self-testing were already concrete product behavior before the later articulation got cleaner. This is mostly a reinforcing ingest, not a structural rewrite.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — add late-February rollout context so the page reflects both the rollout moment and the later March explanation
- [x] **Update** `wiki/state-of/agents.md` — note that the orchestration-ui pattern was visible in the product before the March 6 deep-dive
- [x] **Create** `wiki/sources/newsletters/cursor-cloud-agents-february.md` — source summary page

## Page drafts

### wiki/tools/cursor.md (updated snippet)

```markdown
## Current status (as of 2026-04-14)

- Late-February launch coverage already described the practical surface that the March 6 walkthrough later explained more cleanly: isolated cloud computers, self-testing agents, and video demos as review artifacts
...

## Recent changes

- [2026-02-25] Cursor cloud agents rolled out with isolated VMs, self-testing, and demo-video review before the later March walkthrough made the product thesis explicit
- [2026-03-06] Cloud-agents walkthrough made Cursor's thesis explicit: remote agents should test their own changes, return demo videos, and hand humans a supervision surface instead of just a diff
...
```

### wiki/state-of/agents.md (updated snippet)

```markdown
## Recent changes

- [2026-02-25] Cursor's cloud-agent rollout already showed the orchestration-ui pattern in product form: remote agent computers, self-verification, and video artifacts for human review
```

### wiki/sources/newsletters/cursor-cloud-agents-february.md (new)

```markdown
---
title: Cursor cloud agents in late February
type: source
source_type: newsletter
source_file: raw/newsletters/2026-02-26-cursor-agents-get-their-own-computers.md
published: 2026-02-26
ingested: 2026-04-22
domains: [coding, agents]
---

# Cursor cloud agents in late February

This source cluster captures the rollout moment for Cursor's cloud-agent model before the later March walkthrough made the product thesis more explicit. The notable ingredients are isolated virtual machines, self-testing agents, and video demos as first-pass review artifacts.

## Influenced pages

- [[tools/cursor]] — adds earlier rollout context for the cloud-agent shift
- [[state-of/agents]] — reinforces the supervision-layer reading of Cursor

## Key claims extracted

- Cursor agents run in isolated cloud computers rather than only in the local editor
- Agents can operate UIs, run tests, and host servers while they work
- Review increasingly happens through video demos, screenshots, and logs rather than diffs alone
- The product direction points toward supervising remote workers, not only using AI inside an editor
```

## Open questions

- None.
