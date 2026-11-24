---
title: Latent Space — How Anthropic's dynamic workflows coordinate Claude agents
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-12-how-anthropics-dynamic-workflows-coordinate-claud.md
url: https://www.latent.space/p/claude-dynamic-workflows
published: 2026-10-12
ingested: 2026-10-20
domains: [agents]
---

# Latent Space — How Anthropic's dynamic workflows coordinate Claude agents

Latent Space writeup of an AI Engineer NYC workshop (12 October 2026) where Anthropic's CJ Avilla and Harrison Stall explained dynamic workflows ("flows") for Claude Managed Agents, announced the previous Friday. Flows began in Claude Code as "a harness for every task"; in Managed Agents the lead agent plans and writes an orchestration program, replacing the developer-configured coordinator and roster. A stock-watchlist demo showed a scan phase across isolated-context agents and a review phase. Most of the writeup is the audience Q&A on budgets, self-improvement, visibility, and cost.

## Influenced pages

- [Claude Managed Agents](../../tools/claude-managed-agents.md) — dynamic workflows bullet
- [Multi-agent coordination](../../workflows/multi-agent-coordination.md) — orchestration-as-code pattern and workshop details
- [State of Agents](../../state-of/agents.md) — Managed Agents leader line

## Key claims extracted

- Flows: "a new type of multiagent orchestration, built for your most ambitious workloads"; Claude chooses the organization of agents and can orchestrate its own topology
- The lead agent creates a plan, then writes an orchestration program that launches agents, collects results, and manages information flow; preconfigured subagents can still be passed in the agent config
- How many agents a task gets is governed by "evals and lower defaults"; ambitious tasks need explicit encouragement to parallelize
- The model does not know its budget while running; developers can set a session budget
- Dreaming (research preview) reads a memory store plus past transcripts and produces a reorganized store; suggested for making repeated flows cheaper
- Self-improving flows are not built in; hill-climbing and dreaming were suggested
- The Console graphs every lead-to-subagent payload
- Subagents share a filesystem; developers cannot make one subagent message another through the API
- Flows cost "much more" than a single agent but were "much more effective at finding all of the details" in the demo
