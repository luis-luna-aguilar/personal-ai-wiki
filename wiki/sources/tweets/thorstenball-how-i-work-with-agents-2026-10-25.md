---
title: 'Thorsten Ball (@thorstenball) — How I work with Agents'
type: source
source_type: tweet
source_file: raw/tweets/2026-10-28-thorstenball-2114386050638336082.md
url: https://x.com/thorstenball/status/2114386050638336082
published: 2026-10-25
ingested: 2026-10-28
domains: [coding, agents]
---

# Thorsten Ball (@thorstenball) — How I work with Agents

An X Article by Thorsten Ball, an engineer at Amp (Sourcegraph's coding agent), posted 25 October 2026 and listing fifteen working practices "as of October 2026" (about 900K views). The common thread is to supervise outcomes and evidence rather than method: use the newest models, describe what you want rather than how, give agents sight of and tools for the whole software lifecycle, demand irrefutable proof, work asynchronously with scheduled wake-ups, leave context management to compaction, treat shared threads as company memory, and review only high-blast-radius code.

## Influenced pages

- [AI delegation management](../../training/ai-delegation-management.md) — strongest model, what-not-how, no manual context management, irrefutable proof, agent-built iteration tools, async work and wake-ups
- [Software factory](../../workflows/software-factory.md) — "Lifecycle legibility" subsection; dissent on the slop failure mode
- [AI PR and code review](../../workflows/ai-pr-code-review.md) — review by blast radius and four gating questions
- [Agent skill methodology](../../training/agent-skill-methodology.md) — blind control/treatment check on agent use of AGENTS.md, skills, and docs
- [Company brain](../../concepts/company-brain.md) — Amp's commit-linked shared threads as company memory
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — Amp's shared threads added to the Company brain row's examples
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "company memory" mapped to Company brain

## Key claims extracted

- Use the latest models: a model wrong 10% of the time does not say which 10%, so weaker models cost repeated attempts ("Who's still using Opus 4.5?")
- Stop worrying about slop: not convinced current agents add it, or that the result is unmaintainable if they do
- Prompt the what, not the how (e.g. "make the bytecode compiler and VM as fast as you can; do not stop until it's 2x faster")
- Make the whole SDLC legible: tool calls stopped hallucinations; let agents run end to end, read production logs, deploy, watch rollouts, cut releases, flip flags, triage bugs, and email customers
- Amp's team has custom plugins for bug reports, emailing users, "is our system healthy?", and granting feature flags
- Eval agentic knowledge: spawn five blind agents, control vs. treatment, to see whether AGENTS.md files, skills, scripts, and docs are used
- Local dev feels poor: agents need to install and run anything; remote machines avoid local resource conflicts in end-to-end testing
- Let agents build iteration tools ("20 variations and a little page to combine and test them"; "four theories on why this is slow, then check all four")
- Ask for irrefutable proof (end-to-end walkthroughs, demo videos, before/after numbers); put "this is not evidence" in AGENTS.md; called the biggest game changer
- Don't wait for agents, let them wait on you: bigger, batched, asynchronous tasks
- Automations, schedules, wake-ups, and heartbeats are a killer feature ("check the logs in 2hrs", "check every day at 9am")
- Stop managing context manually: compaction works; one thread = one task; threads range from 3 to 3,714 messages
- Threads are company memory in Amp: shared, connected to git commits, reduce duplicate work
- Don't let agents write for humans, except debugging steps, incident reports, and some mechanical docs
- Review only high-blast-radius code: fewer than five central files and database migrations; gate the rest on "does it work, do I understand it at the arrows-in-a-diagram level, was it tested end to end, can I change it in a month"
