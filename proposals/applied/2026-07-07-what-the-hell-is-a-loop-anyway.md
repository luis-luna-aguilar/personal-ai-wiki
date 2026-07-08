---
type: proposal
source: "tmp/What the hell is a loop, anyway?.md"
status: pending
created: 2026-07-07
---

# Proposal: What the hell is a loop, anyway?

## Summary

Aparna Dhinakaran, with Seldo, argues that "loop" is currently overloaded in AI engineering and separates the term into at least four architectures: execution loops, task/Ralph loops, product/software-factory loops, and system/autoresearch loops. The article's useful contribution is not another claim that loops matter, but a cleaner map of what each loop iterates on, what closes it, where humans sit, and why fan-out pipelines such as Agentic MapReduce should not be called loops unless feedback feeds a next cycle.

## Intended changes

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add a concise four-layer loop taxonomy, Ralph/fresh-context task-loop pattern, oversight-loop warning, and pipeline-vs-loop distinction.
    > **Frontmatter:** add `what-the-hell-is-a-loop-anyway` to `sources:`; keep `as_of: 2026-07-06` because the existing Shepherd source is newer than this 2026-07-04 article.
    >
    > **Current patterns additions:**
    > ```markdown
    > - **Four-layer loop stack.** "Loop" now refers to at least four different architectures: execution loops iterate the agent's act-observe cycle inside one task; task loops restart one agent against one spec until an artifact satisfies tests; product loops run the software lifecycle around a codebase and backlog; system loops improve the prompts, harnesses, models, and evals behind the primary system.
    > - **Fresh-context task loops.** Ralph loops deliberately spend extra tokens by restarting a coding agent against the same specification in a fresh context window on each iteration. The goal is to avoid context rot and compaction drift; the loop should close on spec compliance and passing tests, not on the agent's self-assessment.
    > - **Oversight loop as the human layer.** Autonomy is not one global switch. Execution, task, product, and system loops can each have different human checkpoints, but the top-level loop that sets goals, allocates budgets, and culls work should remain explicit rather than disappearing into "full auto" rhetoric.
    > - **Pipeline versus loop.** Fan-out patterns such as Agentic MapReduce are useful topologies inside loops, but dispatch → gather → validate is only a pipeline unless the result feeds back into another cycle with a named signal.
    > ```
    >
    > **Where surfaced addition:**
    > ```markdown
    > - Dhinakaran and Seldo's loop map separates execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops, giving each a different iterated object, exit signal, and human role.
    > ```
    >
    > **Failure modes additions:**
    > ```markdown
    > - Calling a one-shot fan-out pipeline a loop when no feedback signal drives a next cycle
    > - Running loops without naming the signal that closes them, which turns "autonomy" into unbounded execution
    > ```
    >
    > **Recent changes addition:**
    > ```markdown
    > - [2026-07-04] Dhinakaran and Seldo map loop discourse into execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops; they emphasize exit signals and per-loop autonomy dials.
    > ```
    >
    > **Sources addition:**
    > ```markdown
    > - [What the hell is a loop, anyway?](../sources/articles/what-the-hell-is-a-loop-anyway.md)
    > ```

- [x] **Create** `wiki/sources/articles/what-the-hell-is-a-loop-anyway.md` — source summary.
    > See draft below.

## Page drafts

### wiki/sources/articles/what-the-hell-is-a-loop-anyway.md (new)

```markdown
---
title: "What the hell is a loop, anyway?"
type: source
source_type: article
source_file: "tmp/What the hell is a loop, anyway?.md"
url: https://x.com/aparnadhinak/status/2073492320159510869
published: 2026-07-04
ingested: 2026-07-07
domains: [agents, coding]
---

# What the hell is a loop, anyway?

Aparna Dhinakaran, with Seldo, argues that AI engineering discourse is using "loop" to mean several different architectures. The article separates execution loops, task/Ralph loops, product/software-factory loops, and system/autoresearch loops, then adds an oversight layer where humans set goals, budgets, and culling criteria. The practical point is that each loop needs a named object of iteration, a closing signal, and a deliberate autonomy setting.

## Influenced pages

- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — adds a clearer loop taxonomy, Ralph task-loop pattern, oversight-loop framing, and pipeline-vs-loop distinction.

## Key claims extracted

- The same "loop" language currently covers at least four architectures: agent execution, single-spec task restarts, product/software-factory lifecycles, and system/autoresearch improvement loops.
- A Ralph loop restarts a coding agent against the same specification in a fresh context window each iteration, trading token cost for less context rot and clearer single-artifact completion.
- Product/software-factory loops iterate on a codebase and backlog, with external signals such as issues, production logs, user feedback, review outcomes, and monitoring.
- System/autoresearch loops improve the primary system itself: prompts, harnesses, model choices, evals, and even eval design.
- Agentic MapReduce is better understood as a fan-out topology or pipeline unless outputs feed back into another cycle.
- The top oversight loop is where goals, budgets, and culling decisions live; human agency should be explicit there even when lower loops become more autonomous.
```

## Schema / vocabulary additions

None.

## Open questions

- The source file currently lives in `tmp/`; should it be moved into `raw/articles/` before applying, or is the clipped `tmp/` path acceptable for this source summary?
	- Tmp is not acceptable, move it under the wiki standards.
