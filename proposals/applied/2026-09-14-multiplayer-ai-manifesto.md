---
type: proposal
source: raw/articles/2026-09-14-multiplayer-aicom.md
status: pending
created: 2026-09-14
---

# Proposal: The Multiplayer AI Manifesto — new concept "Multiplayer AI"

## Summary

### In short
AI's value compounds when a team shares the same agents and sessions instead of working in private chats. In a Harvard Business School field experiment, teams using AI reached top-decile work 15.1% of the time, against 7.7% for individuals using AI. Sergey Karayev's manifesto turns this into five principles: never copy-paste between chats, work in visible sessions, turn corrections into reusable skills, never make a person relay what an agent knows, and keep every artifact resumable. Shared sessions should only access what every participant can see. Creates `concepts/multiplayer-ai.md`. Hesitate only if you'd rather extend **Company brain** than open a new concept page.

[[#Open questions|Open questions: none.]]

### The source

Sergey Karayev — co-builder of a shared-agent-session product called Superconductor — published a manifesto in September 2026 arguing that today's AI usage is stuck "single-player": each person works alone in a private chat window, and the most a team can do to collaborate is send around a read-only transcript link. He frames "multiplayer AI" as people on the same team working with the *same* agents in shared sessions with shared learnings, and cites Y Combinator's Fall 2026 Requests for Startups as already naming this a distinct category. The manifesto is structured as five principles for what a genuinely multiplayer product would look like, none of which any current platform fully satisfies by the author's own admission: never copy-and-paste (agents live next to the work and everyone involved can talk to the same one, rather than routing through a private chat and re-pasting results); work with the door open (shared, visible sessions spread good practice the way Shopify's Slack-public River agent does, versus best practices staying trapped in one person's closed chat); continuously improve (a correction should become a reusable skill, a repeated workflow should become a tracked benchmark); people are not routers (a human should never be the one relaying an answer an agent already has); and nothing starts from scratch (every artifact keeps a resumable agent session, so a new hire can pick up a months-old project on day one). He backs the collaboration argument with an independently published Harvard Business School field experiment (776 Procter & Gamble professionals): individuals using AI hit 7.7% top-decile-quality output and teams using AI hit 15.1%, against a 5.1%/8.7% baseline without AI — meaning AI and teamwork compounded rather than substituted for each other. A second section lays out six implementation considerations for anyone building or buying this: agents shouldn't run on individual laptops (unreachable by teammates, tied to one device, over-scoped to that person's access); every agent needs to be firewalled against prompt injection rather than trusted with blanket access; shared-session permissions should be the intersection of what everyone in the session can see, not the union; teams should stay provider-agnostic given how often a provider throttles, restricts, or retires model access; and governance means being able to answer, a year later, which agent ran, who asked it to, what data it touched, and what changed. The manifesto closes by naming Buzz, Claude Tag, QM, Superconductor, and Viktor as platforms it plans to compare against these principles.

### What changes

Nothing in the wiki currently names this exact idea, though two existing pages already describe partial implementations of it under different framing.

- New page `concepts/multiplayer-ai.md`: defines the term, lists the five principles and six implementation considerations, cites the HBS collaboration-plus-AI data point, and flags that the manifesto's own author co-built one of the products (Superconductor) it will eventually be compared against.
- **Company brain** and **Company-wide AI enablement** are not edited directly, but the new page's `## Related` section cross-links to both: to [Company brain](../wiki/concepts/company-brain.md) as the persistent-memory half of team-wide agent systems (distinct from multiplayer AI's live-session-sharing and governance focus), and to the existing thread-per-task chat orchestration pattern on [Company-wide AI enablement](../wiki/training/company-wide-ai-enablement.md) (Buzz, Claude Home Base) as a concrete partial implementation of the "never copy-and-paste" principle.
- `wiki/index.md` gains the new page under Concepts, and the concepts page count moves from 28 to 29 (total 223 → 224).
- One new source page is created for the manifesto.

### What to weigh

The main call is scope. The proposal opens a new concept page instead of extending **Company brain** or **Company-wide AI enablement**, because neither covers live shared sessions or their permissions and governance. No tool page for Superconductor was created, because the source gives only its name.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/concepts/multiplayer-ai.md` — new concept page
    > See draft below

- [ ] **Update** `wiki/index.md` — add new concept page entry, bump concepts count 28→29 and total 223→224
    > See draft below

- [ ] **Create** `wiki/sources/articles/multiplayer-ai-manifesto-2026-09-14.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/concepts/multiplayer-ai.md (new)

```md
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
```

### wiki/index.md (updated)

In `## Concepts`, insert a new line directly after the `concepts/company-brain` entry:

```
- [concepts/multiplayer-ai](concepts/multiplayer-ai.md) — teams working with the same AI agents in shared sessions and shared learnings, instead of siloed private chats; five-principle rubric plus implementation considerations *(as_of: 2026-09-14)*
```

In `## Page count`, update:

```
- concepts: 29
```

and:

```
**Total content pages: 224.**
```

### wiki/sources/articles/multiplayer-ai-manifesto-2026-09-14.md (new)

```md
---
title: "The Multiplayer AI Manifesto"
type: source
source_type: article
source_file: raw/articles/2026-09-14-multiplayer-aicom.md
url: https://multiplayer-ai.com/
ingested: 2026-09-14
domains: [agents]
---

# "The Multiplayer AI Manifesto"

A September 2026 manifesto by Sergey Karayev (co-builder of Superconductor) arguing that AI usage today is "single-player" — private chats with no way to genuinely collaborate — and proposing five principles plus six implementation considerations for what a true "multiplayer AI" product would look like. Cites an HBS field experiment on AI-plus-teamwork outcomes and names five platforms (Buzz, Claude Tag, QM, Superconductor, Viktor) it plans to compare against the rubric.

## Influenced pages

- [Multiplayer AI](../../concepts/multiplayer-ai.md) — new concept page

## Key claims extracted

- "Multiplayer AI" = people on the same team working with the same agents in shared sessions with shared learnings, vs. siloed individual chats
- Y Combinator names "Multiplayer AI" as a Fall 2026 Requests for Startups category
- Five principles: never copy-and-paste; work with the door open; continuously improve; people are not routers; nothing starts from scratch
- Six implementation considerations: agents don't belong on laptops; firewall every agent; permissions should be the intersection of participants' access, not the union; stay provider-agnostic; governance must answer who/what/when a year later; team must own its accumulated learnings/skills/evals regardless of build/buy/open-source choice
- HBS field experiment (776 P&G professionals, Dell'Acqua et al., 2025): individual+AI 7.7% top-decile output, team+AI 15.1%, vs. 5.1% (individual, no AI) and 8.7% (team, no AI)
- Shopify's River agent is Slack-public specifically to spread best practices ("work with the door open")
- Names Buzz, Claude Tag, QM, Superconductor, and Viktor as platforms to be compared against the five principles; author co-built Superconductor
- No vendor or internal platform is claimed to currently satisfy all five principles
```

## Open questions

- None.
