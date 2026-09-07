---
type: proposal
source: raw/articles/2026-09-07-everyto-context-window-an-engineering-team-for-the-cost-of-c.md
status: pending
created: 2026-09-07
---

# Proposal: A solo builder runs a "team" of specialist Codex agents

## Summary

### The source
The email digest captured only a paywalled teaser of Every's "An Engineering Team for the Cost of Codex," so the full article was fetched directly. It profiles Naveen Naidu, the one-person team behind Monologue (Every's dictation app), who now manages his product more like an engineering-team lead than a solo developer. His "engineers" are custom Codex projects: dedicated engineer agents across disciplines, a customer-support agent, and a growth-strategist agent, each with its own `AGENTS.md`, skills, folders, memory, and codebase context that turns it into a specialist. Until recently these worked in isolation — Naveen manually copied Markdown files and instructions between projects whenever a task spanned agents. GPT-5.6 changed that: Naveen can now instruct one agent to hand context directly to another project and kick off a task there, the agent equivalent of a direct report passing an assignment to a coworker, and Codex marks the handoff text as "Sent by Codex from another chat." A worked example: his customer-support agent (which reads live tickets from Fin) handled an audio-echo bug report by opening a separate worktree, fixing the issue, and creating a pull request. The article also includes a "Steal this workflow" recipe — a "dispatch desk" pattern for triaging incoming work inside each project (keep one thread per project for incoming tasks, decide what the agent can resolve itself, and route specialized work to the right project with a template handoff prompt) — and a short quote from Joe Gershenson, who leads OpenAI's Core Agent team for ChatGPT Work and Codex: harnesses went mainstream in late 2025 as frontier models became capable enough to need heavy scaffolding, but "the high-level trend in harness engineering will be finding ways to give the model more degrees of freedom" as models keep improving.

### What changes
The wiki's AI-delegation-management page already tracks spec-first delegation and layered access control for always-on agents, but has no worked example yet of one person running several named, persistent specialist agents as a "team."

- **AI delegation management** gains a new Proven-patterns entry describing the specialist-agent-roster pattern and the "dispatch desk" triage recipe, plus a Recent-changes entry. Page date moves to 19 August (the article's original newsletter date).
- **Harness (agent)** gets one added sentence in its "Why it matters" section, citing Gershenson's quote as a second named-practitioner voice (alongside Anthropic's Thariq Shihipar) arguing harnesses should get simpler, not more complex, as models improve.
- New source page for the fetched article.

### What to weigh
This is a single small-scale example (a one-person company), not a benchmarked or widely-replicated pattern — it earns its place as a concrete worked example of a pattern the wiki already tracks conceptually (specialist sub-agents with persistent identity/context), not as new independent evidence that the pattern works at scale.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/training/ai-delegation-management.md` — new Proven-patterns entry, Recent-changes entry, as_of bump
    > See draft below

- [ ] **Update** `wiki/concepts/harness.md` — one sentence added to "Why it matters"
    > See draft below

- [ ] **Create** `wiki/sources/articles/engineering-team-cost-of-codex-2026-08-19.md` — source summary

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

```md
Frontmatter changes: as_of: 2026-08-19; sources: append engineering-team-cost-of-codex-2026-08-19

## Proven patterns (new bullet, appended)

- **Run a roster of named specialist agents, not one generalist.** Every profiled Naveen Naidu, the one-person team behind the Monologue app, who manages distinct Codex-project "agents" — engineer agents by discipline, a customer-support agent, a growth-strategist agent — each configured with its own `AGENTS.md`, skills, memory, and codebase context that turns it into a specialist. GPT-5.6 let him move from manually copying context between projects to instructing one agent to hand context directly to another and kick off a task there — the agent equivalent of a direct report passing an assignment to a coworker. Worked example: his support agent (reading live tickets from Fin) handled a bug report by opening a separate worktree, fixing the issue, and opening a PR, without Naveen relaying anything by hand. **Dispatch-desk triage recipe:** keep one thread per project to handle incoming tasks (don't spin up a new thread per ticket); decide upfront what the agent can resolve itself versus route elsewhere; when a request needs another specialist, tell the current agent which project should take it and what's needed back, using a short handoff template ("Review this issue, create a new worktree in [project] to [complete the task], and [produce the deliverable]"). (Naveen Naidu / Every, Aug 2026)

## Recent changes (new entry, prepended)

- [2026-08-19] Added the specialist-agent-roster pattern and dispatch-desk triage recipe from a solo builder running several named Codex "team members," each with its own AGENTS.md, skills, and memory.
```

### wiki/concepts/harness.md (updated)

```md
## Why it matters (one sentence appended at the end of the existing paragraph)

... OpenAI's Joe Gershenson, who leads the Core Agent team for ChatGPT Work and Codex, makes a related point from the vendor side: harnesses went mainstream in late 2025 once frontier models became capable of handling a wide range of tasks autonomously, but "the high-level trend in harness engineering will be finding ways to give the model more degrees of freedom" as models keep improving — a second named-practitioner voice, alongside Anthropic's Thariq Shihipar, arguing the harness should shrink rather than grow as the underlying model gets stronger.
```

### wiki/sources/articles/engineering-team-cost-of-codex-2026-08-19.md (new)

```md
---
title: An Engineering Team for the Cost of Codex
type: source
source_type: article
source_file: raw/articles/2026-09-07-everyto-context-window-an-engineering-team-for-the-cost-of-c.md
url: https://every.to/context-window/an-engineering-team-for-the-cost-of-codex
published: 2026-08-19
ingested: 2026-09-07
domains: [agents]
---

# An Engineering Team for the Cost of Codex

Every profile of Naveen Naidu (Monologue's solo builder), who runs a roster of specialist Codex agents — each a separate project with its own AGENTS.md, skills, memory, and codebase context — that hand work to each other directly since GPT-5.6. Includes a "dispatch desk" triage workflow recipe and a quote from OpenAI's Joe Gershenson (Core Agent team lead) on harnesses simplifying as models improve. Originally surfaced via Every's 2026-08-19 daily email, whose captured copy was a paywalled teaser; this summary is drawn from the full fetched article.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — new Proven-patterns entry
- [Harness (agent)](../../concepts/harness.md) — Gershenson quote added to "Why it matters"

## Key claims extracted

- Naveen Naidu (Monologue) runs distinct Codex "agents" (engineers by discipline, support, growth), each its own project with custom AGENTS.md, skills, memory, codebase context
- GPT-5.6 enabled direct cross-project agent handoffs (previously manual); Codex marks handed-off text as "Sent by Codex from another chat"
- Dispatch-desk pattern: one triage thread per project, decide what the agent can resolve itself, route specialized work with a handoff template
- Joe Gershenson (OpenAI, Core Agent team lead for ChatGPT Work/Codex): harnesses went mainstream late 2025; trend is toward giving models more degrees of freedom as they improve
```

## Open questions

None.
