---
title: Devin Docs — Dynamic Workflows
type: source
source_type: article
source_file: raw/articles/2026-10-20-docsdevinai-work-with-devin-dynamic-workflows.md
url: https://docs.devin.ai/work-with-devin/dynamic-workflows
published: 2026-10-13
ingested: 2026-10-20
domains: [agents, coding]
---

# Devin Docs — Dynamic Workflows

Cognition's documentation page for Devin Dynamic Workflows, announced by @devindevelopers on 13 October 2026 (`raw/tweets/2026-10-13-devindevelopers-2109887510184964285.md`, which only links here). A dynamic workflow is a deterministic Python script, written and run by Devin, that orchestrates a team of Devin sessions; every agent call is recorded, so runs are observable and resumable. The page covers when to use a workflow, the authoring primitives, where agents run, the determinism rules that make resume work, cost, and saving a workflow as a skill.

## Influenced pages

- [Devin](../../tools/devin.md) — Dynamic Workflows subsection
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — orchestration-as-code pattern

## Key claims extracted

- Use a workflow for wide fan-out with a combine step (roughly 5+ independent units) or a staged pipeline (e.g. audit → fix → verify); not for mechanical codemods, one or two sessions, or tightly coupled or small sequential work
- Primitives: `register_workflow`, `agent(prompt, phase, schema)` returning a schema-shaped dict, `pipeline(items, stages…)` with no barrier between stages, `parallel([...])`, `log()`
- Each agent is by default a separate Devin session on its own VM, handing code off through git branches; can be pinned to the parent's VM (shared working tree, lower concurrency) or to a cheaper mode such as Devin Lite
- On resume the script re-executes from the top; each agent call is keyed by a hash of prompt, schema, and settings, so completed calls replay and only unfinished work runs; scripts must not depend on time, randomness, generated IDs, environment variables, filesystem state, or network responses
- Editing a prompt re-runs that agent and everything downstream; maximum run budget is seven days; failed agents are handled by the script (skip, default, retry, fail)
- Runs are auto-approved by default; enterprise admins must enable the feature
- One run can use far more ACUs than a single session; test on a slice first
- A working workflow can be committed as a skill (`workflow.py` plus `SKILL.md`)
