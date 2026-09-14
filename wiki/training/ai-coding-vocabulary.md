---
title: AI coding vocabulary
type: training
domains: [coding, agents]
tags: [agentic]
as_of: 2026-08-20
sources: [mattpocock-dictionary-of-ai-coding, swombat-relationship-engineering-2026-08-20]
---

# AI coding vocabulary

Teams using coding agents need shared language for the things that actually determine outcomes: the model, the harness, the session, the context window, the tools, the environment, and the handoff between runs.

## Current guidance

- Use **model** for what the provider actually serves: the neural network weights that process your input and return a response. A model has no memory between calls — it only knows what you send in each request. The word is often misused to describe the entire product experience; that whole system is the agent, built by wrapping a model in a harness.
- Use **agent** for the harnessed system a person interacts with: model plus tools, system prompt, environment, permissions, and loop behavior.
- Use **context** for the information the agent has available right now; distinguish it from durable memory and from the finite context window sent to the model.
- Use **session** for the bounded run that accumulates tool results and conversation history until it is cleared, compacted, or handed off.
- Use **harness** for the scaffolding around the model: tools, prompts, orchestration, context management, permission layers, and environment access.
- Use **environment** for what the agent can actually act on: the filesystem, browser, APIs, shell, and connected services.

## Teaching pattern

Start with the operational distinction: if two products use the same model but behave differently, the harness and environment explain the difference. This prevents teams from over-attributing success or failure to model choice alone.

## One proposed historical framing: five phases of building with AI

A practitioner essay (@swombat, date inferred ~August 2026 — no confirmed byline) names a five-phase progression that gives the terms on this page a rough timeline: **Prompt Engineering** (human at the center, asking short questions), **Context Engineering** (human still central, but now manually curating and feeding large chunks of context — code, docs — into the prompt), **Agentic Engineering** (a harnessed agent does the actual work via multi-step tool use; the human reviews and guides from above rather than doing the work directly), and **Harness Engineering** (the surrounding scaffolding — rules, skills, tests, guardrails, automated review — becomes the primary object of investment, and day-to-day human review becomes optional once the harness is trustworthy). The author's proposed fifth phase, **Relationship Engineering** — investing in an ongoing, persistent relationship with an individuated AI agent across projects, rather than rebuilding a bespoke harness per project — rests entirely on the author's own personal, anecdotal account of two named AI companions with self-reported "memory graphs" of "needs," and explicitly asserts that AI systems genuinely "care." That specific claim is this one author's personal and unverified framing, not an established or independently corroborated industry pattern, and is recorded here only as a named data point in the ongoing "how far does agent autonomy go" discussion — not as settled fact.

## Failure modes

- Calling every behavior "the model" and missing harness, tool, or context problems
- Treating a long session as memory instead of a context window slowly filling up
- Letting handoffs depend on chat history instead of durable artifacts

## Sources

- [Matt Pocock — Dictionary of AI Coding](../sources/repos/mattpocock-dictionary-of-ai-coding.md)
- [swombat — Relationship Engineering: the fifth phase of building with AI](../sources/tweets/swombat-relationship-engineering-2026-08-20.md)
