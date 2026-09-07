---
type: proposal
source: raw/newsletters/2026-08-10-i-vibe-coded-a-security-risk.md
status: pending
created: 2026-09-07
---

# Proposal: Vibe-coded security risk — task crossover and the illusion of explanatory depth

## Summary

### The source

An Every staff writer, self-described as a "baby vibe coder," recounts building an app called Tastemaker with Claude Opus 4.5, then wiring in an MCP connector so Claude Code or Codex could pull the app's style guide directly from an agent session. Before shipping, she asked a software-engineer friend whether the connector was risky; he told her an authenticated API only ever does what it's asked, but a backend agent that manages access is a different matter, since it decides who gets in. She relayed a "make sure you do the safe version" instruction to Claude, tested that the feature worked, and shipped it. Weeks later, she pointed a newer model — GPT-5.6 Sol — at the same code for an unrelated second opinion, and it found a public, unauthenticated registration route into the live connector. No evidence surfaced of anyone exploiting it, but the feature came down while the team investigated. She frames the failure through OpenAI's "task crossover" research (AI enabling people to do work outside their normal occupation — 16.8% of a studied 800K work-related ChatGPT messages) compounding with the psychological "illusion of explanatory depth": watching an agent's fluent, followable reasoning creates false confidence that the right questions were already asked and answered.

### What changes

`training/ai-delegation-management.md` gains a new bullet under `## Failure modes` naming this exact compound failure — happy-path-only testing plus the illusion of explanatory depth when a non-expert delegates security-relevant work — with her stated mitigations (learn the field's basics, get a human expert review, don't let the same AI's self-assessment be the only evidence of safety). One new `## Recent changes` entry records it; page date moves to 10 August. One new source page summarizes the essay.

### What to weigh

This is a single first-person anecdote from one Every writer, not a study or incident report — useful as a concrete, well-told failure-mode case, but it shouldn't be read as representative or measured. Nothing else beyond the sourcing noted above.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-delegation-management.md` — new Failure-modes bullet, new Recent-changes entry, as_of bump, sources merge
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/vibe-coded-security-risk-2026-08-10.md` — source summary

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

```md
---
title: AI delegation management
type: training
domains: [agents, training]
tags: [agentic]
as_of: 2026-08-10
sources: [management-as-ai-superpower-2026-07, andy-matuschak-agent-loop-tempo-2026-07, design-layer-framework-2026-08-04, vibe-coded-security-risk-2026-08-10]
---
```

`## Failure modes` gains a new bullet (after the existing "Constraint drift" bullet):

```md
- **Happy-path-only testing plus the illusion of explanatory depth.** A non-expert who tests only the intended-use path, then reads an agent's fluent, followable reasoning and mistakes "I can follow this" for "the right questions were asked," ships work whose adversarial cases were never checked. Case in point: a writer built and shipped an MCP connector for a small app with Claude's help, tested that it worked, and only learned it had a public, unauthenticated registration route when a second model reviewed the same code cold weeks later. Mitigation: learn the field's basics before delegating consequential work, get a human expert review, and don't let the same system's self-assessment be the only evidence a feature is safe.
```

`## Recent changes` gains a new first entry (list stays well under the recent-changes cap, no spill needed):

```md
- [2026-08-10] Added a failure-mode case study on happy-path-only testing plus the illusion of explanatory depth (a vibe-coded MCP connector security hole).
```

`## Sources` gains one new line:

```md
- [I Vibe Coded a Security Risk](../sources/newsletters/vibe-coded-security-risk-2026-08-10.md)
```

### wiki/sources/newsletters/vibe-coded-security-risk-2026-08-10.md (new)

```md
---
title: I Vibe Coded a Security Risk
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-10-i-vibe-coded-a-security-risk.md
url: https://every.to/working-overtime/i-vibe-coded-a-security-risk
published: 2026-08-10
ingested: 2026-09-07
domains: [training]
---

# I Vibe Coded a Security Risk

Every staff writer Katie Parrott describes vibe-coding an MCP connector into her small app Tastemaker with Claude's help, shipping it after only testing that it worked, and later discovering — via an unrelated second opinion from GPT-5.6 Sol — that the connector had a public, unauthenticated registration route. She frames the failure through OpenAI's "task crossover" research and the psychological "illusion of explanatory depth," and lands on three personal rules: learn the field's basics first, get a human expert review, and don't let the same AI's self-assessment be the only evidence a feature is safe.

## Influenced pages

- [training/ai-delegation-management](../../training/ai-delegation-management.md) — new Failure-modes case study on happy-path testing and the illusion of explanatory depth

## Key claims extracted

- OpenAI's "task crossover" research: 16.8% of a studied ~800,000 work-related ChatGPT messages involved doing work outside the user's normal occupation
- A GPT-5.6 Sol review found a live, public, unauthenticated registration route into a Claude-built MCP connector; no evidence surfaced of exploitation before it was pulled
- Psychological framing: the "illusion of explanatory depth" — people feel they understand a mechanism until asked to explain it step by step; AI's fluent explanations make it easy to skip that check
```

## Open questions

- None.
