---
title: AI work delegation modes
type: training
domains: [agents]
tags: [agentic]
as_of: 2026-08-27
sources: [ai-work-splitting-2026-05-10, task-routing-cost-discipline-2026-05-13, every-after-automation-2026-05, every-chatgpt-openclaw-guides-2026-08-27]
---

# AI work delegation modes

Knowledge work with AI is bifurcating into two distinct modes that require different human behaviors, tool choices, and success criteria.

## Current guidance

The shift: the question is no longer "can I use AI here?" but "which mode fits this task?"

**Delegation mode** (autonomous)
- The task has a clear, verifiable success criterion
- You can fully hand it off and check the result
- The agent can iterate without human steering between steps
- Examples: run all tests and fix failures, research a topic and produce a summary, convert this doc to another format
- Right tool: Claude Code /goal, Codex, Claude Managed Agents, OpenClaw (with appropriate security precautions)
- Human role: define the criterion upfront, review the output

**Collaboration mode** (human-steered)
- The task requires judgment at each step that only the human can supply
- Success depends on taste, relationship context, or evolving criteria
- Handing off entirely produces outputs that miss the point
- Examples: writing a difficult email, strategic decisions, creative direction, stakeholder negotiations
- Right tool: Claude chat, co-writing surfaces, Proof, any chat-first interface
- Human role: stay in the loop; steer, don't just prompt once and wait

## Proven patterns

- **Identify the mode before starting**: before opening any AI tool, ask whether the task has a clear success criterion you can delegate against. If yes, reach for an agent. If no, reach for a co-writer.
- **Don't confuse tools with modes**: Claude Code can be used in collaboration mode (iterating together on a design) and a chat model can be used in delegation mode (write me all the test cases for this function). Mode is about task shape, not tool choice.
- **Document your delegation criteria**: when you hand off to an agent, write down what "done" looks like before starting. The `/goal` syntax in Claude Code formalizes this.
- **Route by determinism and risk**: scripts for deterministic transformations, small models for cheap classification or drafting, frontier models for ambiguous synthesis, and humans for intent, taste, and accountability.
- **Match the surface to the assignment size, not just the mode.** Every's updated ChatGPT guide maps OpenAI's merged app onto delegation granularity: quick questions stay in Chat, longer assignments move to Work, and software jobs go to Codex. `/goal` gives a persistent objective; ChatGPT projects (cloud) vs. local-folder projects is itself a delegation-mode choice (cloud continuity vs. filesystem access); Scheduled Tasks (Work) and Codex thread automations cover the proactive-loop end of delegation mode.

## Failure modes

- **Delegating judgment-dependent work**: agent produces confident-sounding output that misses the point; no one caught it because it wasn't reviewed carefully
- **Collaborating on delegatable work**: human micromanages step-by-step when the agent could complete the task autonomously; wastes the human's time without improving the output
- **Unclear success criterion at handoff**: agent loops or produces superficially correct but substantively wrong output; criterion ambiguity at the start propagates to the end
- **Personal agents go stale without a maintenance team**: Every rolled back an "every employee gets an agent" experiment to team/company-owned agents because individually owned agents degraded once their owner stopped tending them. Even a "simple" delegation-mode automation can hide real maintenance cost — one of Every's PowerPoint-generation automations needed 24 skills and 18 scripts, and costs $62 in tokens per deck.

## Evidence from practice

- Framework synthesized from Anthropic's Claude platform team's guidance on designing agent workflows, reported by Every (May 2026)
- Anthropic's Claude Managed Agents documentation for "Define outcomes" (May 2026) formalizes the delegation-mode approach at the platform level
- Every's "After Automation" essay (Dan Shipper, May 2026) reframes delegation mode as "agent employees" — coworker agents you tag and ask to do work (Every's Claudie, Andy, Viktor) and embedded agents living inside a product workflow (Fin, which closed 40.1% of actionable customer-service conversations without a human in a recent week) — and reframes collaboration mode as the "human sandwich": a human frames the task, the agent collapses it, and a human judges and extends the result inside tools like Codex, Claude Code, and Claude Cowork.
- OpenClaw's pull-request volume (44,469 PRs by May 16, 2026; 12,430 since April 1 — versus Kubernetes' 5,200 PRs in all of 2022) is offered as evidence of how fast delegation-mode volume rises once a skill becomes cheaply available, independent of whether review capacity rises with it.
- **Every reverses its personal-agent default.** After months of running individual OpenClaw-style personal agents, Every found a stronger model still can't log in when a credential expires or notice a silently-broken integration — the maintenance burden falls entirely on the agent's owner. Their new default is a single shared "Every Agent" living in Slack: the whole company shares one agent, but each person works through their own connections and context. A personal Claw can still make sense for recurring work specific to one person who's willing to maintain it and doesn't need company-wide context.

## Open questions

- How do you handle tasks that start as collaboration but transition to delegation mid-work (e.g., once the approach is agreed on)?
- Does team size change the optimal split? (Small teams tend toward collaboration; larger orgs toward structured delegation)

## Related

- [Agent evals](../concepts/agent-evals.md) — the benchmark-framing half of Every's "After Automation" argument; this page covers the task-delegation half
- [AI-native product building](ai-native-product-building.md) — the "AI sandwich" pattern applied specifically to product-building work
- [Agents reshape organizations](../trends/agents-reshape-organizations.md) — the same framing applied at org-design scale

## Sources

- [AI work splitting in two — Every](../sources/newsletters/ai-work-splitting-2026-05-10.md)
- [Task routing and cost discipline — May 2026](../sources/newsletters/task-routing-cost-discipline-2026-05-13.md)
- [After Automation — Dan Shipper (Every)](../sources/articles/every-after-automation-2026-05.md)
- [Every — Our ChatGPT and OpenClaw Guides Just Got an Overhaul](../sources/newsletters/every-chatgpt-openclaw-guides-2026-08-27.md)
