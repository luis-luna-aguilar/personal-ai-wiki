---
type: proposal
sources:
  - raw/newsletters/2026-05-15-you-can-now-access-codex-on-phone.md
  - raw/newsletters/2026-05-15-ainews-everything-is-conductor.md
  - raw/newsletters/2026-05-14-ainews-codex-rises-claude-meters-programmatic-u.md
status: pending
created: 2026-05-18
---

# Proposal: Codex mobile preview + enterprise push (May 2026)

## Summary

OpenAI shipped a mobile preview of Codex inside the ChatGPT app (iOS/Android): users can review diffs, approve commands, and steer running sessions from a phone while the heavy work runs on a laptop or devbox. Simultaneously OpenAI launched a 30-day enterprise switch promo (2 months free Codex), made Remote SSH generally available, added CI/CD hooks, and introduced scoped access tokens for Business/Enterprise. The Prime Intellect nanoGPT speedrun benchmark showed both Opus 4.7 (2,930 steps) and GPT-5.5 (2,950) beating the human baseline (2,990) after ~10K autonomous runs.

## Intended changes

- [x] **Update** `wiki/tools/codex.md` — add mobile preview, SSH GA, CI/CD hooks, scoped tokens, enterprise promo, nanoGPT result; update `as_of` to 2026-05-15; add Recent changes entry
    > **as_of:** `2026-05-13` → `2026-05-15`
    >
    > **Add to Current status (after existing bullets):**
    > ```
    > - **Mobile preview** (May 2026): Codex accessible from the ChatGPT iOS/Android app; users can start tasks, review diffs, approve commands, and steer running sessions remotely while the agent continues on a laptop or devbox
    > - Remote SSH now generally available for managed remote environments
    > - CI/CD hooks and scoped programmatic access tokens added for Business/Enterprise automation
    > - Enterprise switch promo: 2 months free Codex for teams switching from competitors within 30 days (launched May 14)
    > - nanoGPT speedrun (Prime Intellect, ~10K runs, ~14K H200 hours): both Opus 4.7 (2,930 steps) and GPT-5.5 (2,950) beat the human baseline (2,990); agents relied on existing human research and did not produce original ideas
    > ```
    >
    > **Add to Recent changes:**
    > `- [2026-05-15] Mobile preview in ChatGPT app: steer Codex sessions from iOS/Android while agent runs on devbox; Remote SSH GA; CI/CD hooks; scoped tokens; 30-day enterprise switch promo (2 months free)`

- [x] **Update** `wiki/state-of/coding.md` — update Codex line to mention mobile; add nanoGPT benchmark to Recent changes
    > **Before (terminal-coding-agent section):**
    > `- [Codex](../tools/codex.md) — OpenAI; cloud coding agent via CLI and ChatGPT, but current direction increasingly spills into browser work, documents, spreadsheets, and broader computer-use-style workflows *(as of 2026-04-24)*`
    >
    > **After:**
    > `- [Codex](../tools/codex.md) — OpenAI; cloud coding agent via CLI, ChatGPT, and now mobile (iOS/Android preview); remote SSH GA; direction increasingly spills into broader computer-work workflows *(as of 2026-05-15)*`
    >
    > **Add to Recent changes:**
    > `- [2026-05-15] Codex mobile preview: steer sessions from phone while agent runs on devbox; Remote SSH GA; enterprise 30-day switch promo (2 months free). Prime Intellect nanoGPT speedrun: both Opus 4.7 and GPT-5.5 beat human baseline in autonomous ML optimization (~10K runs)`

- [x] **Create** `wiki/sources/newsletters/codex-mobile-may-2026.md` — source summary

## Page drafts

### wiki/sources/newsletters/codex-mobile-may-2026.md (new)

```markdown
---
title: "Codex mobile preview + enterprise push — May 2026"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-15-you-can-now-access-codex-on-phone.md
published: 2026-05-15
ingested: 2026-05-18
domains: [coding, agents]
---

# Codex mobile preview + enterprise push — May 2026

OpenAI shipped Codex mobile access (iOS/Android), Remote SSH GA, CI/CD hooks, scoped access tokens, and a 30-day enterprise switch promotion. The Prime Intellect nanoGPT speedrun result showed autonomous agents (Opus 4.7 and GPT-5.5) surpassing the human baseline benchmark after 10K runs, with the caveat that they relied on existing human research.

## Influenced pages

- [Codex](../../tools/codex.md) — mobile preview, Remote SSH GA, tokens, promo, nanoGPT result
- [State of Coding](../../state-of/coding.md) — Codex line updated; nanoGPT milestone

## Key claims extracted

- Codex in ChatGPT iOS/Android app: review diffs, approve commands, steer sessions remotely
- Remote SSH for managed remote environments: now generally available
- CI/CD hooks for scanning prompts or adjusting settings per repo
- Scoped access tokens: integrate Codex into CI/CD workflows at team level (Business/Enterprise)
- 30-day enterprise promo: 2 months free for switchers
- nanoGPT speedrun (Prime Intellect): ~10K autonomous runs, ~14K H200 hours; Opus 4.7 → 2,930 steps, GPT-5.5 → 2,950, human baseline → 2,990; agents used existing research, not original ideas
```
