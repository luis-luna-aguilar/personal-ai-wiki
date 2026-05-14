---
type: proposal
sources:
  - raw/newsletters/2026-05-10-ai-work-is-splitting-in-two.md
status: pending
created: 2026-05-13
---

# Proposal: "AI Work Is Splitting in Two" — delegation vs. collaboration modes

## Summary

Every's newsletter synthesizes a framework from Anthropic's platform team: knowledge work is bifurcating into (1) judgment-dependent work that still requires human steering at each step (collaboration mode), and (2) well-scoped autonomous work you can fully delegate to an agent with a clear success criterion (delegation mode). The practical shift: the question is no longer "can I use AI here?" but "which mode — steered or autonomous — fits this task?"

## Intended changes

- [x] **Create** `wiki/training/ai-work-delegation-modes.md` — new training page
    > See draft below

- [x] **Create** `wiki/sources/newsletters/ai-work-splitting-2026-05-10.md`
    > See draft below

- [x] **Update** `wiki/index.md` — add entry for `training/ai-work-delegation-modes`

## Page drafts

### wiki/training/ai-work-delegation-modes.md (new)

```markdown
---
title: AI work delegation modes
type: training
tags: [agents, workflows]
as_of: 2026-05-10
sources: [ai-work-splitting-2026-05-10]
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
```

### wiki/sources/newsletters/ai-work-splitting-2026-05-10.md (new)

```markdown
---
title: AI work is splitting in two — Every synthesizes Anthropic platform team framework
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-10-ai-work-is-splitting-in-two.md
published: 2026-05-10
ingested: 2026-05-13
domains: [agents]
---

# AI work is splitting in two — Every synthesizes Anthropic platform team framework

Every newsletter dated May 10, 2026. Primary URL: https://every.to/context-window/ai-work-is-splitting-in-two

## Influenced pages

- [AI work delegation modes](../../training/ai-work-delegation-modes.md) — new training page created

## Key claims extracted

- Framework source: Anthropic's Claude platform team (reported via Every)
- Core claim: knowledge work is bifurcating into judgment-dependent (human-steered) and well-scoped autonomous (delegate-and-verify) categories
- Old question: "can I use AI here?"
- New question: "which mode — human-steered or autonomous — fits this task?"
- Delegation mode requires a clear, verifiable success criterion stated upfront
- Collaboration mode requires human judgment at each step; delegation produces misses
- Anthropic's "Define outcomes" platform documentation formalizes the delegation approach
- Every framing: this bifurcation is actively shaping how teams structure agent workflows in 2026
```

