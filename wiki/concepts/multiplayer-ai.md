---
title: Multiplayer AI
type: concept
domains: [agents]
tags: [collaboration]
as_of: 2026-09-14
sources: [multiplayer-ai-manifesto-2026-09-14]
---

# Multiplayer AI

"Multiplayer AI" describes people on the same team working with the same AI agents in shared sessions and shared learnings, rather than each person working alone inside a private chat. The term is used by Sergey Karayev (Superconductor) in a September 2026 "Multiplayer AI Manifesto," and by Y Combinator's Fall 2026 Requests for Startups as a named category; both frame today's default as "single-player" AI — a private chat window, at best a read-only transcript to share — even on team/enterprise plans, since those typically only share settings like prompts, skills, and integrations rather than live sessions.

## Current status (as of 2026-09-14)

- Five stated principles for a "true" multiplayer AI experience, none of which the manifesto claims any current platform fully satisfies: **never copy-and-paste** (agents live next to the work rather than in a separate chat, and every person involved can talk to the same agent); **work with the door open** (shared sessions spread best practices the way Shopify's Slack-public River agent does); **continuously improve** (a correction should turn into a reusable skill, a repeated workflow into a tracked benchmark); **people are not routers** (a human should never be asked something an agent already has the answer to); **nothing starts from scratch** (every artifact keeps a resumable agent session, so a new team member can pick up exactly where a project left off).
- Six implementation considerations: agents shouldn't run on individual laptops (unreachable by the rest of the team, tied to one device, over-scoped to one person's access); every agent should be firewalled/sandboxed against prompt injection rather than given blanket tool access; permissions on a shared session should be the intersection of every participant's access, not the union; teams should stay model-provider-agnostic given how often providers throttle, restrict, or retire access; governance requires being able to answer, a year later, which agent ran, who asked it to, what data it touched, and what it changed; and whether to build, buy, or run open source, one thing isn't negotiable — the team must own the learnings, skills, and evals the platform accumulates.
- Cites a Harvard Business School field experiment (776 Procter & Gamble professionals, Dell'Acqua/Ayoubi/Lifshitz/Sadun/Mollick, 2025): individuals with AI reached 7.7% top-decile-quality solutions and teams with AI reached 15.1%, versus 5.1% (individuals, no AI) and 8.7% (teams, no AI) — collaboration and AI compounded rather than substituted for each other.
- Names Buzz, Claude Tag, QM, Superconductor, and Viktor as platforms it plans to compare against the five principles; the manifesto's own author co-built Superconductor, so treat the comparison-in-progress as vendor-adjacent rather than neutral.

## Why it matters

Two patterns already tracked elsewhere in this wiki are partial implementations of "multiplayer AI" rather than a distinct idea: [thread-per-task chat orchestration](../training/company-wide-ai-enablement.md) (Buzz, Claude Home Base) maps principle 1 (never copy-and-paste) onto chat-channel/thread structure, and [company brain](company-brain.md) covers the persistent-memory half of principle 5 (nothing starts from scratch) but not live session-sharing or the governance/security considerations here. The manifesto gives the wiki a single named rubric — five principles plus six implementation considerations — for evaluating future shared-agent-session products against, instead of treating each new one as an unrelated point solution.

## Recent changes

- [2026-09-14] Page created from "The Multiplayer AI Manifesto" (Sergey Karayev / Superconductor, September 2026).

## Related

- [Company brain](company-brain.md) — the persistent-memory/institutional-knowledge half of team-wide agent systems; multiplayer AI is the live-session-sharing and governance half
- [Company-wide AI enablement](../training/company-wide-ai-enablement.md) — thread-per-task chat orchestration (Buzz, Claude Home Base) is a concrete partial implementation of the "never copy-and-paste" principle

## Sources

- [The Multiplayer AI Manifesto](../sources/articles/multiplayer-ai-manifesto-2026-09-14.md)
