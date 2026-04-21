---
type: proposal
sources:
  - raw/newsletters/2026-04-07-extreme-harness-engineering-1m-loc-1b-toksday.md
  - raw/tweets/2026-04-01-xcom-mattpocockukstatus203935061968.md
  - raw/tweets/2026-04-06-xcom-socialwithaayanstatus204119294.md
  - raw/articles/2026-04-06-tco-tlqjrhp3td.md
  - raw/articles/2026-04-06-tco-d8p3syy1an.md
  - raw/articles/2026-04-06-tco-mf5o0yst4t.md
  - raw/tweets/2026-04-06-xcom-hesamationstatus20408208344286.md
  - raw/newsletters/2026-04-07-strange-things-happening-in-ai.md
status: pending
created: 2026-04-21
---

# Proposal: Harness engineering in early April

## Summary

The wiki already has good harness and orchestration pages. This batch adds a more operational layer to them: hooks as reliability plumbing, skills as the shareable abstraction, knowledge-base layers as lightweight memory structure, and explicit agent coordination frameworks for long-running work.

This should update the existing pages rather than create a new concept.

## Intended changes

- [x] **Update** `wiki/concepts/harness.md` — add a practical note that skills, hooks, and knowledge layers are becoming standard harness components
  > See diff snippet below.

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add pattern bullets on shareable skills, hook-based triggers, and externalized knowledge layers
  > See diff snippet below.

- [x] **Create** `wiki/sources/newsletters/harness-engineering-early-april.md` — source summary page
  > See full draft below.

## Page drafts

### wiki/concepts/harness.md (updated snippet)

```markdown
## What a harness includes

- **System prompt & instructions** — behavioral constraints, task framing, output format rules
- **Tool suite** — which tools the model can call, their descriptions, when to use them
- **Orchestration logic** — how the agent loops, when it escalates, how sub-agents are coordinated
- **Execution environment** — browser, terminal, code sandbox, API layers, memory systems
- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended
- **Reusable operating modules** — skills, hook scripts, and lightweight knowledge layers increasingly act as composable pieces of the harness, not just ad hoc project artifacts

## What good harness engineering looks like

- **Skills as the reusable abstraction.** Teams are increasingly sharing operating judgment as skills or task modules instead of sharing only code snippets or prompts.
- **Hook-based reliability plumbing.** Event hooks can make agent behavior more deterministic by invoking the right capability at the right moment instead of hoping the model notices a textual instruction.
- **Externalized knowledge layers.** Folder-level graphs, wikis, or compacted memory layers help the harness retrieve the right context without dumping everything into the prompt.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated snippet)

```markdown
## Current patterns

- **Ambiguity gates.** When the cost of guessing wrong is high, stop and ask instead of auto-continuing. Good for architecture forks, destructive operations, or underspecified user requests.
- **Scoped context, not global context.** Inject only the files, rules, or project context a sub-agent actually needs; keep the rest out of the loop to avoid context bleed.
- **Folder-scoped specialization.** A durable folder plus instructions, skills, and accumulated context often works better than a "swarm" of generic agents sharing one giant context.
- **Share skills, not just code.** Reusable skills increasingly package the fuzzy operating judgment that teams want many agents to inherit.
- **Hook the workflow, don't just describe it.** If a step must happen reliably, wire it into the harness or hook layer instead of leaving it as a prompt suggestion.
- **Externalize the knowledge layer.** Graphs, wikis, and maintained context stores can stabilize long-running work better than repeatedly rebuilding understanding from raw files alone.
- **Evaluator separation.** Use a distinct evaluator or verifier for long-running work; generators routinely overrate their own output.
```

### wiki/sources/newsletters/harness-engineering-early-april.md (new)

```markdown
---
title: Harness engineering in early April
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-07-extreme-harness-engineering-1m-loc-1b-toksday.md
ingested: 2026-04-21
domains: [coding, agents]
---

# Harness engineering in early April

This source summary groups a cluster of early-April signals about operational agent scaffolding. The common theme is that useful agent systems are being assembled from reusable skills, hook layers, externalized knowledge structures, and explicit coordination patterns rather than from larger prompts alone.

## Influenced pages

- [[concepts/harness]] — expands the definition of the harness to include skills, hooks, and maintained knowledge layers
- [[workflows/agentic-orchestration-patterns]] — adds practical orchestration patterns seen in real coding-agent workflows

## Key claims extracted

- Teams are increasingly sharing skills as operating modules, not only code
- Hook systems are being used to make skill invocation and workflow steps more reliable
- Lightweight knowledge layers or graphs are emerging as practical context structure for long-running agents
- Coordination frameworks for AFK or parallel agents make the harness itself the main unit of leverage
```
