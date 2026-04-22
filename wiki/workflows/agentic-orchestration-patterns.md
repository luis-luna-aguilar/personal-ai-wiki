---
title: Agentic orchestration patterns
type: workflow
domains: [agents]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-04-21
sources: [notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, harness-engineering-early-april, open-agent-orchestration-late-march, skills-and-plugin-packaging-late-march, harness-engineering-march]
---

# Agentic orchestration patterns

Reusable patterns for getting better behavior from one or more agents without depending on a single provider or model family. The central lesson from recent sources: simple harnesses, strong evals, explicit boundaries, and safer escalation logic often matter more than increasingly elaborate agent scaffolds.

## Current patterns

- **Ambiguity gates.** When the cost of guessing wrong is high, stop and ask instead of auto-continuing. Good for architecture forks, destructive operations, or underspecified user requests.
- **CLI-first execution.** For many serious agent workflows, the command line remains the most composable surface because permissions, files, worktrees, and logs stay legible.
- **Scoped context, not global context.** Inject only the files, rules, or project context a sub-agent actually needs; keep the rest out of the loop to avoid context bleed.
- **Shared storage, isolated execution.** Let agents collaborate through the same repo, files, or knowledge store while keeping compute sandboxes separate; this preserves coordination without forcing one giant mutable runtime.
- **Worktree-based parallelism.** Isolate concurrent agent work in separate branches/worktrees so supervision, diff review, and rollback stay manageable.
- **Folder-scoped specialization.** A durable folder plus instructions, skills, and accumulated context often works better than a "swarm" of generic agents sharing one giant context.
- **Hosted packaging for repeatable agents.** One-click or prepackaged agents can make a reusable workflow distributable across a team without each user rebuilding the harness from scratch.
- **Package the workflow, not just the tool.** Teams increasingly bundle skills, hooks, MCP wiring, rules, and slash commands into something installable so one person's working agent setup becomes another person's starting point.
- **Share skills, not just code.** Reusable skills increasingly package the fuzzy operating judgment that teams want many agents to inherit.
- **Hook the workflow, don't just describe it.** If a step must happen reliably, wire it into the harness or hook layer instead of leaving it as a prompt suggestion.
- **Externalize the knowledge layer.** Graphs, wikis, and maintained context stores can stabilize long-running work better than repeatedly rebuilding understanding from raw files alone.
- **Evaluator separation.** Use a distinct evaluator or verifier for long-running work; generators routinely overrate their own output.
- **Failure-aware replanning.** Don't blindly retry. Feed structured failure metadata back into the orchestrator so it can generate a different plan.
- **Loop controls that are first-class.** Long-running agent work needs explicit pause, resume, rewind, and transparent-session controls rather than fragile prompt conventions.
- **Eval-driven simplification.** Prefer the simplest harness that passes evals. A cleaner representation layer and stronger verification often beat "smarter-looking" orchestration.
- **Thin harness, fat skills, fat code.** Put fuzzy human-like operating judgment into reusable skills and deterministic work into code, while keeping the harness itself small and legible.
- **Demos over memos.** Prototype working flows behind flags or internal demos before locking in a long design-document process.
- **Self-rebuild culture.** In fast-moving agent systems, teams must be willing to replace their own scaffolding repeatedly as model and environment capabilities change.

## Where these patterns surfaced

- Notion's AI team describes repeated rebuilds, internal-first prototyping, and careful decisions about when to use MCP versus tighter custom integrations.
- AINews' synthesis frames the current frontier as "simple harness, strong evals, model-agnostic scaffolding."
- Garry Tan's "confusion protocol" example shows ambiguity gating as a productized safety and productivity pattern.
- Matt Pocock's DDD/ADR framing suggests domain language and decision records make large codebases more navigable for both humans and agents.
- Every's "folder is the agent" framing argues that stable context packaging, not swarm complexity, is often the real source of specialization.
- Anthropic's long-running-agent story reinforces planner/generator/evaluator separation and the need for external verification.
- Late-March OpenClaw / Plus One coverage reinforced CLI-first execution, one-click packaging, and worktree-style coordination as practical open-agent product directions before the later April orchestration wave.
- Late-March coding-agent coverage suggests a clear packaging race: marketplaces and skill bundles are becoming the transport layer for agent behavior across teams.
- Practitioner commentary also suggests "skill" does not mean the same thing everywhere: some ecosystems package reference-heavy technical instructions, while others package more open-ended problem-solving approaches.

## Failure modes

- Letting all agents share one bloated context by default
- Asking a generator to be its own evaluator on subjective tasks
- Retrying the same failed plan with slightly different wording
- Confusing visible complexity in the harness with actual robustness
- Treating orchestrator complexity as a substitute for stable context packaging
- Confusing more agents with more leverage when the human review bottleneck does not move
- Building cool tools with no concrete user journey or evaluation target

## Sources

- [[sources/newsletters/notion-token-town]]
- [[sources/newsletters/ainews-openclaw-2026-04-18]]
- [[sources/tweets/garrytan-confusion-protocol]]
- [[sources/tweets/matt-pocock-ddd-adr]]
- [[sources/newsletters/harness-engineering-patterns]]
- [[sources/newsletters/harness-engineering-early-april]]
- [[sources/newsletters/open-agent-orchestration-late-march]]
- [[sources/newsletters/skills-and-plugin-packaging-late-march]]
- [[sources/newsletters/harness-engineering-march]]
