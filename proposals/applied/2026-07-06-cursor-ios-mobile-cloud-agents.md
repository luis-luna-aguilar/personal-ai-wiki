---
type: proposal
sources:
  - raw/articles/2026-07-06-cursorcom-blog-ios-mobile-app.md
  - raw/newsletters/2026-06-30-meta-upgrades-it-brain-scanning-model.md
  - raw/newsletters/2026-06-30-ainews-not-much-happened-today.md
  - raw/newsletters/2026-06-30-us-companies-are-using-chinese-models.md
status: pending
created: 2026-07-06
---

# Proposal: Cursor iOS and mobile cloud-agent control

## Summary
Cursor's iOS public beta makes always-on cloud agents and remote desktop agents controllable from a phone. This is a lightweight but useful update to Cursor's tool page and the coding state-of dashboard because it shows coding agents becoming mobile, persistent, and notification-driven.

## Intended changes

- [x] **Update** `wiki/tools/cursor.md` — add iOS app and remote/cloud-agent control.
    > **Add to Current status:** Cursor for iOS is in public beta for paid users, with support for launching always-on cloud agents, controlling agents running on a desktop, voice input, slash commands, push notifications, Live Activities, diff review, and PR follow-up from mobile.

- [x] **Update** `wiki/state-of/coding.md` — add Cursor mobile/cloud-agent control to the agentic-coding-workspace section.

- [x] **Create** `wiki/sources/articles/cursor-ios-mobile-app-2026-06.md` — official source summary.

## Updated Page Snippets

### `wiki/tools/cursor.md`

> **Before:**
> `- **Cursor 3** is the current shipped version, announced in the "Meet the new Cursor" post on cursor.com/blog`

> **After:**
> `- **Cursor 3** is the current shipped version, announced in the "Meet the new Cursor" post on cursor.com/blog`
> `- Cursor for iOS is in public beta for paid users, letting users launch always-on cloud agents, control desktop agents remotely, use voice and slash commands, receive push notifications/Live Activities, inspect diffs, follow up, and merge PRs from mobile.`

### `wiki/state-of/coding.md`

> **Before:**
> `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting; jointly trained model with xAI coming *(as of 2026-06-17)*`

> **After:**
> `- [Cursor](../tools/cursor.md) — Cursor 3 rebuilt as cloud-agent orchestration platform; SDK exposes the runtime headlessly; iOS beta adds mobile launch/control for always-on cloud and desktop agents; acquired by SpaceX ($60B, June 2026); Cursor Origin launched for agent-native code hosting *(as of 2026-06-30)*`

## Page Drafts

### `wiki/sources/articles/cursor-ios-mobile-app-2026-06.md` (new)

```md
---
title: Cursor iOS mobile app public beta
type: source
source_type: article
source_file: raw/articles/2026-07-06-cursorcom-blog-ios-mobile-app.md
url: https://cursor.com/blog/ios-mobile-app
published: 2026-06-30
ingested: 2026-07-06
domains: [coding, agents]
---

# Cursor iOS mobile app public beta

Cursor announced a native iOS app public beta for paid users. The app lets users launch always-on cloud agents or control agents running on their computer, with voice input, slash commands, push notifications, Live Activities, diff review, follow-up prompts, and PR merge workflows from mobile.

## Influenced pages
- [Cursor](../../tools/cursor.md) — mobile/cloud-agent control
- [State of Coding](../../state-of/coding.md) — Cursor entry refresh

## Key claims extracted
- Cursor mobile can launch cloud agents in isolated VMs.
- Users can remotely control local agents on a desktop from a phone.
- Mobile workflows include incident response, customer issues, screenshots/annotations as context, reviewing artifacts, inspecting diffs, and merging PRs.
```
