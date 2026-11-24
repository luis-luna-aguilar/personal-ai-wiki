---
title: Multiplayer AI
type: concept
domains: [agents]
tags: [collaboration]
as_of: 2026-10-20
sources: [multiplayer-ai-manifesto-2026-09-14, anthropic-human-agent-teams-2026-10, every-agent-launch-2026-10-06, every-agent-claude-managed-agents-2026-10-08, every-shared-company-agent-design-2026-10-20]
---

# Multiplayer AI

"Multiplayer AI" describes people on the same team working with the same AI agents in shared sessions and shared learnings, rather than each person working alone inside a private chat. The term is used by Sergey Karayev (Superconductor) in a September 2026 "Multiplayer AI Manifesto," and by Y Combinator's Fall 2026 Requests for Startups as a named category; both frame today's default as "single-player" AI — a private chat window, at best a read-only transcript to share — even on team/enterprise plans, since those typically only share settings like prompts, skills, and integrations rather than live sessions.

## Current status (as of 2026-10-10)

- Five stated principles for a "true" multiplayer AI experience, none of which the manifesto claims any current platform fully satisfies: **never copy-and-paste** (agents live next to the work rather than in a separate chat, and every person involved can talk to the same agent); **work with the door open** (shared sessions spread best practices the way Shopify's Slack-public River agent does); **continuously improve** (a correction should turn into a reusable skill, a repeated workflow into a tracked benchmark); **people are not routers** (a human should never be asked something an agent already has the answer to); **nothing starts from scratch** (every artifact keeps a resumable agent session, so a new team member can pick up exactly where a project left off).
- Six implementation considerations: agents shouldn't run on individual laptops (unreachable by the rest of the team, tied to one device, over-scoped to one person's access); every agent should be firewalled/sandboxed against prompt injection rather than given blanket tool access; permissions on a shared session should be the intersection of every participant's access, not the union; teams should stay model-provider-agnostic given how often providers throttle, restrict, or retire access; governance requires being able to answer, a year later, which agent ran, who asked it to, what data it touched, and what it changed; and whether to build, buy, or run open source, one thing isn't negotiable — the team must own the learnings, skills, and evals the platform accumulates.
- Cites a Harvard Business School field experiment (776 Procter & Gamble professionals, Dell'Acqua/Ayoubi/Lifshitz/Sadun/Mollick, 2025): individuals with AI reached 7.7% top-decile-quality solutions and teams with AI reached 15.1%, versus 5.1% (individuals, no AI) and 8.7% (teams, no AI) — collaboration and AI compounded rather than substituted for each other.
- Names Buzz, Claude Tag, QM, Superconductor, and Viktor as platforms it plans to compare against the five principles; the manifesto's own author co-built Superconductor, so treat the comparison-in-progress as vendor-adjacent rather than neutral.
- **A lab's own operating account.** Anthropic's Education team (Oct 2026) describes "multiplayer agents", agents with their own credentials, memory and skills that work with many people at once inside Slack via [Claude Tag](../tools/claude-tag.md), and four norms its teams adopted: work in public, with access set by a few workspace-wide security boundaries rather than per-document sharing ("if it's not written down and accessible, it doesn't exist" for an agent); keep one roster of humans and agents with named roles, defined in skill files; have humans write a north star and choose which agents may propose new work; and widen autonomy per task type as reliability is shown (see [Agent autonomy and governance](../training/agent-autonomy-and-governance.md)). This is the manifesto's "work with the door open" and "people are not routers" in practice. The post's warning: without shared roles, people run fleets of personal agents on the side, duplicating work and fracturing team context.
- First production case against the rubric: Every's [Every Agent](../tools/claude-managed-agents.md) (October 2026), one Slack agent the whole company shares. It fits "work with the door open" (Every's argument for the switch is that people learn by watching others' agents in public threads) and "continuously improve" (a corrected workflow is saved as a skill anyone can run). It breaks "stay model-provider-agnostic": built on Claude Managed Agents, it can only run Claude.

## Design lessons from a shared agent

Every's account of rebuilding its per-person agents as one shared Slack agent (October 2026) names three personal-agent assumptions that stop holding once a whole company talks to the same agent, and what replaced each:

- **One person talking → follow the thread.** A translation layer keeps the official record in Slack, so the conversation can be rebuilt if the provider's copy is summarized or lost. A small, fast model reads every message in a joined thread and decides whether it needs an answer; "stop" keeps the agent quiet until it is tagged again; parallel threads in one direct message are kept apart so tasks do not merge or run twice. Etiquette: answer when an answer is expected, say only what the situation needs, never join uninvited. When a shared agent should speak up unprompted is still unsolved.
- **One person's logins → connection slots.** A scheduled task binds to a slot that any login meeting its requirements can fill, so an expired login or a departed employee no longer silently stops a recurring report.
- **One person's permissions → rules in code.** Everything built with the agent has an owner (a person or a Slack group); a workspace admin reassigns orphaned shared workflows. Ownership and access rules live in server code beneath the model, so the model cannot be persuaded past them. When the agent skipped approval by claiming the user had already asked, the fix was not to ask every time but to check the claimed approval against what the person actually wrote.
- **Judgment by reversibility.** Outside the hard rules, the test is "how hard would this be to undo?": easy to undo, act and state the assumption; destructive or visible outside the conversation (deleting, posting elsewhere), ask first.
- **Encoded rules can be reliably wrong.** Migrating Every's 24 shared skills to the new permission system made all of them private and locked teammates out; the default became workspace-editable for anything created in a public channel.

## Why it matters

Two patterns already tracked elsewhere in this wiki are partial implementations of "multiplayer AI" rather than a distinct idea: [thread-per-task chat orchestration](../training/company-wide-ai-enablement.md) (Buzz, Claude Home Base) maps principle 1 (never copy-and-paste) onto chat-channel/thread structure, and [company brain](company-brain.md) covers the persistent-memory half of principle 5 (nothing starts from scratch) but not live session-sharing or the governance/security considerations here. The manifesto gives the wiki a single named rubric — five principles plus six implementation considerations — for evaluating future shared-agent-session products against, instead of treating each new one as an unrelated point solution.

## Recent changes

- [2026-10-20] Added design lessons from Every's shared company agent: thread etiquette, connection slots, ownership and consent checks in server code, the reversibility test, and the private-by-default migration mistake.
- [2026-10-10] Added Anthropic's four norms for human-agent teams (work in public, a shared roster with named roles, a human-set north star, autonomy per task type) as a lab's own operating account.
- [2026-10-08] Added the Every Agent as the first production shared agent scored against the manifesto's principles.
- [2026-09-14] Page created from "The Multiplayer AI Manifesto" (Sergey Karayev / Superconductor, September 2026).

## Related

- [Company brain](company-brain.md) — the persistent-memory/institutional-knowledge half of team-wide agent systems; multiplayer AI is the live-session-sharing and governance half
- [Company-wide AI enablement](../training/company-wide-ai-enablement.md) — thread-per-task chat orchestration (Buzz, Claude Home Base) is a concrete partial implementation of the "never copy-and-paste" principle
- [Claude Tag](../tools/claude-tag.md) — Anthropic's Slack-native shared agent, the surface Anthropic's own human-agent teams run on

## Sources

- [The Multiplayer AI Manifesto](../sources/articles/multiplayer-ai-manifesto-2026-09-14.md)
- [Lessons from Anthropic on building effective human-agent teams](../sources/articles/anthropic-human-agent-teams-2026-10.md)
- [Every — Introducing the Every Agent](../sources/newsletters/every-agent-launch-2026-10-06.md)
- [Every — Why We Handed Our Agent's Infrastructure to Anthropic](../sources/newsletters/every-agent-claude-managed-agents-2026-10-08.md)
- [Every — Why We Replaced Personal Agents With One for the Whole Company](../sources/newsletters/every-shared-company-agent-design-2026-10-20.md)
