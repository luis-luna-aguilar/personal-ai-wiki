---
type: proposal
source: raw/newsletters/2026-05-18-claude-mythos-breaks-into-apples-m5.md
status: pending
created: 2026-05-18
---

# Proposal: AI stack fungibility + "AI psychosis" warning (Hashimoto)

## Summary

Mitchell Hashimoto (HashiCorp founder) articulated two signals in the same newsletter: (1) AI agents make tech stacks fungible — Bun merged 1M lines Zig→Rust in days; stack choice is now a quarterly project, not a decade-long commitment. (2) "AI psychosis" — a named failure mode where teams ship bugs relying on AI to fix them, eroding system comprehensibility. Simon Willison confirmed a parallel case.

_Note: this proposal and `proposals/2026-05-18-karpathy-coding-agent-failure-modes.md` both update `wiki/training/ai-enablement-software-development.md`. Apply in either order; each adds distinct content._

## Intended changes

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — update `as_of`, add source to frontmatter, add stack fungibility to Proven patterns, add AI psychosis to Failure modes, add Recent changes section
    > **`as_of`:** `2026-05-13` → `2026-05-18`
    >
    > **Sources frontmatter:** add `ai-stack-fungibility-hashimoto-2026-05`
    >
    > **Add to `## Proven patterns`:**
    >
    > ```md
    > - **Stack fungibility.** AI agents make language and framework choice reversible at scale not previously possible. Bun merged 1M lines Zig→Rust in days using AI agents; Cloudflare reproduced Next.js API in a week; Ladybird JS engine C++→Rust in 14 days; one team rewrote mobile apps in React Native with a planned revert path. Hashimoto: "Tech stack is no longer a decade-long commitment — now a quarterly project." Language/framework lock-in arguments weaken substantially; migration risk can be hedged cheaply.
    > ```
    >
    > **Add to `## Failure modes`:**
    >
    > ```md
    > - **AI psychosis.** Named by Hashimoto (May 2026): teams adopt a "MTTR is all you need" mindset — shipping bugs faster, relying on AI to fix them in production, while system comprehensibility degrades over time. Root cause: optimizing for mean time to recovery rather than mean time between failures. Symptom: no single person can fully understand the system; AI becomes load-bearing for every incident. Counter: continue requiring humans to understand what they ship; use AI to accelerate comprehension, not replace it.
    > ```
    >
    > **Add `## Recent changes` section at end of page (before `## See also`):**
    >
    > ```md
    > ## Recent changes
    >
    > - [2026-05-18] Stack fungibility pattern: tech stack choice is now a quarterly project (Bun Zig→Rust in days); "AI psychosis" failure mode: MTTR-only mindset erodes system comprehensibility (Hashimoto)
    > ```

- [x] **Create** `wiki/sources/newsletters/ai-stack-fungibility-hashimoto-2026-05.md`
    > See draft below

## Page drafts

### wiki/sources/newsletters/ai-stack-fungibility-hashimoto-2026-05.md (new)

```md
---
title: AI stack fungibility and AI psychosis — Hashimoto (newsletter)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-18-claude-mythos-breaks-into-apples-m5.md
published: 2026-05-18
ingested: 2026-05-18
domains: [coding, training]
---

# AI stack fungibility and AI psychosis — Hashimoto (newsletter)

Newsletter coverage of two signals from Mitchell Hashimoto (HashiCorp founder). First: Bun merged 1M lines of Zig→Rust in days using AI agents, leading Hashimoto to conclude that tech stack choice is now a quarterly project rather than a decade-long commitment. Supporting cases: Cloudflare reproduced Next.js API in a week; Ladybird JS engine C++→Rust in 14 days; one company rewrote mobile apps in React Native with a revert plan. Second: Hashimoto named "AI psychosis" — companies shipping bugs and relying on AI to fix them in production, eroding system comprehensibility; framed as the "MTTR is all you need" failure mode. Simon Willison confirmed the React Native migration case. Source file also covers the Claude Mythos / Apple M5 story.

## Influenced pages

- [AI enablement — software development](../../training/ai-enablement-software-development.md) — stack fungibility (Proven patterns), AI psychosis (Failure modes)

## Key claims extracted

- Bun merged 1M lines Zig→Rust in days using AI agents
- Hashimoto: "Tech stack is no longer a decade-long commitment — now a quarterly project"
- Cloudflare: reproduced Next.js API in a week
- Ladybird JS engine: C++→Rust in 14 days
- One team: React Native rewrite with planned revert path (Willison confirmed)
- AI psychosis: MTTR-only mindset; system comprehensibility erodes as bugs are shipped and fixed by AI
```
