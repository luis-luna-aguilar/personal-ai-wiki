---
type: proposal
source: internal — synthesized from raw/newsletters/2026-04-13-the-folder-is-the-agent.md, raw/tweets/2026-04-13-xcom-garrytanstatus2043566215927328.md, raw/newsletters/2026-04-14-cursor-changes-how-you-code-with-agents.md, raw/newsletters/2026-04-14-ainews-top-local-models-list-april-2026.md
status: pending
created: 2026-04-13
---

# Proposal: Harness engineering patterns

## Summary

The wiki already has a `harness` concept page and a high-level `agentic-orchestration-patterns` workflow. This batch adds a more operational layer to both: folder-scoped context as the real unit of specialization, planner/generator/evaluator separation for long-running work, and Garry Tan's "fat skills / fat code / thin harness" framing.

This is a refinement proposal, not a new-page proposal.

## Intended changes

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add folder-scoped context packaging, evaluator separation, and thin-harness framing
  > See full draft below.

- [x] **Update** `wiki/concepts/harness.md` — sharpen the concept with "folder as agent" and the distinction between stable context packaging vs orchestration logic
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/harness-engineering-patterns.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/workflows/agentic-orchestration-patterns.md (replacement draft)

```markdown
---
title: Agentic orchestration patterns
type: workflow
domains: [agents]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-04-13
sources: [notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns]
---

# Agentic orchestration patterns

Reusable patterns for getting better behavior from one or more agents without depending on a single provider or model family. The central lesson from recent sources remains the same: simple harnesses, strong evals, explicit boundaries, and safer escalation logic matter more than increasingly elaborate agent scaffolds.

## Current patterns

- **Ambiguity gates.** When the cost of guessing wrong is high, stop and ask instead of auto-continuing.
- **Scoped context, not global context.** Inject only the files, rules, or project context a sub-agent actually needs; keep the rest out of the loop.
- **Folder-scoped specialization.** A durable folder plus instructions, skills, and accumulated context often works better than a "swarm" of generic agents sharing one giant context.
- **Evaluator separation.** Use a distinct evaluator or verifier for long-running work; generators routinely overrate their own output.
- **Failure-aware replanning.** Don't blindly retry. Feed structured failure metadata back into the orchestrator so it can generate a different plan.
- **Eval-driven simplification.** Prefer the simplest harness that passes evals.
- **Thin harness, fat skills, fat code.** Put fuzzy human-like operating judgment into reusable skills and deterministic work into code, while keeping the harness itself small and legible.
- **Demos over memos.** Prototype working flows before locking in a large design-doc process.
- **Self-rebuild culture.** Replace scaffolding aggressively as models improve.

## Where these patterns surfaced

- Every's "folder is the agent" framing argues that stable context packaging, not swarm complexity, is often the real source of specialization.
- Garry Tan's "fat skills / fat code / thin harness" framing gives a compact design rule for where to put behavior.
- Anthropic's long-running-agent story reinforces planner/generator/evaluator separation and the need for external verification.
- AINews' synthesis frames the frontier as filesystems, bash, memory, permissions, retries, evals, and subagents treated as first-class surface.

## Failure modes

- Letting all agents share one bloated context by default
- Asking a generator to be its own evaluator on subjective tasks
- Treating orchestrator complexity as a substitute for stable context packaging
- Confusing more agents with more leverage when the human review bottleneck does not move

## Sources

- [[sources/newsletters/notion-token-town]]
- [[sources/newsletters/ainews-openclaw-2026-04-18]]
- [[sources/tweets/garrytan-confusion-protocol]]
- [[sources/tweets/matt-pocock-ddd-adr]]
- [[sources/newsletters/harness-engineering-patterns]]
```

### wiki/concepts/harness.md (updated snippet)

```markdown
## Why it matters

In practice, a harness is not only the loop logic. Recent source material reinforces that stable context packaging matters just as much: the folder, local instructions, reusable skills, and accumulated project memory often determine whether the same base model behaves like a specialist or a generic assistant.

## Harness vs folder-level context

- **Folder-level context** packages what the agent knows: codebase, instructions, skills, conventions, and durable local memory
- **Harness** packages how the agent operates: loop logic, tools, routing, retries, and evaluation

The two are related but not identical. Many real-world "agent" improvements actually come from better context packaging rather than fancier orchestration.
```

### wiki/sources/newsletters/harness-engineering-patterns.md (new)

```markdown
---
title: Harness engineering patterns
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-13-the-folder-is-the-agent.md
ingested: 2026-04-13
domains: [agents, coding]
---

# Harness engineering patterns

This source summary groups several closely aligned signals about how agents should be structured. The shared takeaway is that robust agent behavior comes from explicit context packaging, evaluator separation, and a thin orchestration layer rather than from maximal swarm complexity.

## Influenced pages

- [[workflows/agentic-orchestration-patterns]] — adds folder-scoped specialization, evaluator separation, and thin-harness framing
- [[concepts/harness]] — clarifies the distinction between context packaging and loop logic

## Key claims extracted

- A project folder plus durable instructions and skills can function as the real unit of specialization for an agent
- Long-running work benefits from planner/generator/evaluator separation instead of one model grading itself
- "Fat skills / fat code / thin harness" is a useful design heuristic for where behavior should live
- Filesystems, memory, permissions, retries, evals, and subagents are increasingly treated as first-class agent surface
```

