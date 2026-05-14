---
title: AI work delegation modes
type: training
domains: [agents]
tags: [agentic]
as_of: 2026-05-13
sources: [ai-work-splitting-2026-05-10, task-routing-cost-discipline-2026-05-13]
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

## Failure modes

- **Delegating judgment-dependent work**: agent produces confident-sounding output that misses the point; no one caught it because it wasn't reviewed carefully
- **Collaborating on delegatable work**: human micromanages step-by-step when the agent could complete the task autonomously; wastes the human's time without improving the output
- **Unclear success criterion at handoff**: agent loops or produces superficially correct but substantively wrong output; criterion ambiguity at the start propagates to the end

## Evidence from practice

- Framework synthesized from Anthropic's Claude platform team's guidance on designing agent workflows, reported by Every (May 2026)
- Anthropic's Claude Managed Agents documentation for "Define outcomes" (May 2026) formalizes the delegation-mode approach at the platform level

## Open questions

- How do you handle tasks that start as collaboration but transition to delegation mid-work (e.g., once the approach is agreed on)?
- Does team size change the optimal split? (Small teams tend toward collaboration; larger orgs toward structured delegation)

## Sources

- [AI work splitting in two — Every](../sources/newsletters/ai-work-splitting-2026-05-10.md)
- [Task routing and cost discipline — May 2026](../sources/newsletters/task-routing-cost-discipline-2026-05-13.md)
