---
type: proposal
source: raw/newsletters/2026-08-27-our-chatgpt-and-openclaw-guides-just-got-an-overha.md
status: pending
created: 2026-09-08
---

# Proposal: Every rewrites its ChatGPT and OpenClaw guides

## Summary

### The source

Every overhauled two of its practitioner guides in response to how the underlying tools changed, not the models. The Codex-for-Knowledge-Work guide is retitled "ChatGPT for Knowledge Work" and recast around OpenAI's Chat/Work/Codex split: quick questions stay in Chat, longer assignments move to Work, and software jobs go to Codex — with new coverage of `/goal` persistent objectives, the choice between ChatGPT projects (cloud-based) and local-folder projects, Scheduled Tasks vs. Codex thread automations, and a built-in browser with its own signed-in profile for tasks needing the user's existing sessions. Separately, Every's OpenClaw (personal messaging-native agent) guide changed its actual recommendation after months of running Claws themselves: a personal agent still can't handle an expired credential or notice a silently-broken integration on its own, so the maintenance burden falls entirely on its owner. Every's response is to shift toward a single shared "Every Agent" living in Slack — the whole company shares one agent, but each person works through their own connections and context — rather than recommending individual personal Claws by default.

### What changes

`training/ai-work-delegation-modes.md` already frames the practical question as "which mode fits this task" (autonomous delegation vs. human-steered collaboration) and names specific tools for each mode. This proposal adds the updated Chat/Work/Codex tool mapping and the OpenClaw recommendation reversal as two new items — one to "Proven patterns," one to "Evidence from practice" — and bumps `as_of` to 2026-08-27. The page has no existing "Recent changes" section, consistent with several other training pages, so this proposal doesn't add one.

### What to weigh

This content could equally have gone on `training/company-wide-ai-enablement.md` (which already tracks the shared-vs-personal-agent question via its "Buy, build, or rent" pattern) — this proposal places it on the more specifically tool-selection-focused delegation-modes page instead, since the Chat/Work/Codex split is fundamentally about matching a task to the right delegation surface. A reasonable alternative placement, not a forced one.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-work-delegation-modes.md` — add Chat/Work/Codex mapping and OpenClaw-to-shared-agent reversal, bump `as_of`
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/every-chatgpt-openclaw-guides-2026-08-27.md` — source summary

## Page drafts

### wiki/training/ai-work-delegation-modes.md (updated)

```md
---
as_of: 2026-08-27
sources: [ai-work-splitting-2026-05-10, task-routing-cost-discipline-2026-05-13, every-after-automation-2026-05, every-chatgpt-openclaw-guides-2026-08-27]
---

## Proven patterns

(... existing bullets unchanged ...)

- **Match the surface to the assignment size, not just the mode.** Every's updated ChatGPT guide maps OpenAI's merged app onto delegation granularity: quick questions stay in Chat, longer assignments move to Work, and software jobs go to Codex. `/goal` gives a persistent objective; ChatGPT projects (cloud) vs. local-folder projects is itself a delegation-mode choice (cloud continuity vs. filesystem access); Scheduled Tasks (Work) and Codex thread automations cover the proactive-loop end of delegation mode.

## Evidence from practice

(... existing bullets unchanged ...)

- **Every reverses its personal-agent default.** After months of running individual OpenClaw-style personal agents, Every found a stronger model still can't log in when a credential expires or notice a silently-broken integration — the maintenance burden falls entirely on the agent's owner. Their new default is a single shared "Every Agent" living in Slack: the whole company shares one agent, but each person works through their own connections and context. A personal Claw can still make sense for recurring work specific to one person who's willing to maintain it and doesn't need company-wide context.
```

### wiki/sources/newsletters/every-chatgpt-openclaw-guides-2026-08-27.md (new)

```md
---
title: "Our ChatGPT and OpenClaw Guides Just Got an Overhaul"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-27-our-chatgpt-and-openclaw-guides-just-got-an-overha.md
url: https://every.to/p/our-chatgpt-and-openclaw-guides-just-got-an-overhaul
published: 2026-08-27
ingested: 2026-09-08
domains: [training]
---

# Our ChatGPT and OpenClaw Guides Just Got an Overhaul

Every's Katie Parrott rewrites the Codex-for-Knowledge-Work guide as "ChatGPT for Knowledge Work" around the Chat/Work/Codex split, and reverses the OpenClaw guide's personal-agent-by-default recommendation in favor of a single shared Slack-based "Every Agent."

## Influenced pages

- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — Chat/Work/Codex mapping, OpenClaw-to-shared-agent reversal

## Key claims extracted

- ChatGPT for Knowledge Work: Chat (quick questions), Work (longer assignments), Codex (software jobs); `/goal`, ChatGPT vs. local-folder projects, Scheduled Tasks vs. Codex automations, built-in browser with signed-in profile
- OpenClaw guide reversal: personal agents can't handle expired credentials or silently-broken integrations; Every now defaults to a shared "Every Agent" in Slack over individual personal Claws
```
