---
title: Agentic orchestration patterns
type: workflow
domains: [agents]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-07-06
sources: [notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, harness-engineering-early-april, open-agent-orchestration-late-march, skills-and-plugin-packaging-late-march, harness-engineering-march, deep-agents-overview, goose-platform, googlecloudtech-adk-2-orchestration-patterns, agent-infrastructure-harness-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, production-agent-orchestration-2026-04-29, agent-html-artifacts-2026-05-13, gas-city-software-factory-2026-05, dynamic-workflows-claude-code, loopcraft-june-2026, aiewf-loops-debate-2026-07-03, shepherd-live-agent-rollback-2026-07-06, claude-code-getting-started-with-loops-2026-06-30]
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
- **Harnesses and hosts are separating.** Deep Agents-style systems package planning, filesystem context, subagents, permissions, and memory into a batteries-included harness for specialized agent behavior. Goose-style systems package provider setup, MCP, and desktop/CLI/API surfaces into a local agent host product. Those are different layers, and teams should not confuse framework choice with host-surface choice.
- **Demos over memos.** Prototype working flows behind flags or internal demos before locking in a long design-document process.
- **Self-rebuild culture.** In fast-moving agent systems, teams must be willing to replace their own scaffolding repeatedly as model and environment capabilities change.
- **Hybrid graph orchestration.** When some steps must never be skipped or reordered, represent the workflow as a graph with deterministic nodes and AI-driven nodes instead of leaving the whole procedure inside prompt text.
- **Coordinator-specialist routing.** Replace "god agents" with a coordinator that routes between smaller specialists with narrower context, tools, and responsibilities.
- **Composable skills with progressive disclosure.** Skills work best as small, reusable units with clear interfaces; load their full context only when invoked so agents can have broad capability surfaces without always paying the token cost.
- **Cross-language delegation through a common protocol.** In larger organizations, useful agent systems often span Python, TypeScript, Go, and Java teams; protocolized handoff matters more than assuming one language or one repo owns the whole workflow.
- **Sandboxed executors for evidence-producing steps.** If a step needs real code execution, parsing, tests, or transformations, run it in an isolated workspace with explicit limits instead of asking the model to simulate execution in text.
- **Config-driven agent deployment.** Production agent frameworks are packaging sandboxing, auth, RBAC (Role-Based Access Control — who can do what), credential handling, and frontend configuration into deployable manifests (such as a `deepagents.toml` file). Without this, each developer writes the same custom setup from scratch for every new agent project: spinning up sandboxes, storing credentials safely, and configuring who has access to what.
- **Artifact-backed agent collaboration.** Multi-agent work is more durable when agents exchange work through a shared storage layer — such as a cloud dataset bucket or shared filesystem — rather than sharing a single runtime. Each agent runs in its own isolated environment and coordinates through the artifact store. Agent Collabs demonstrates this with Hugging Face: dataset buckets serve as shared storage, and Hugging Face Spaces provide each agent's isolated execution environment, letting agents built on different frameworks collaborate without coupling their runtimes.
- **Model-pool routing by an AI-managed orchestrator.** Rather than hardcoding which model handles which task, a coordinator layer (e.g., Sakana Conductor) selects from a pool of available models based on the task type, cost, and current model availability. The coordinator decides routing; specialized models handle execution.
- **Local-first browser agents.** For tasks that can be fully executed client-side, agents run entirely in the browser — no cloud handoff, no server-side compute. This reduces latency, cost, and privacy surface. The pattern is emerging as a complement to (not a replacement for) cloud-backed agents in orchestrated systems.
- **Durable workflow execution.** Production agent workflows should survive process crashes and infrastructure interruptions. Checkpointing state (memory, partial outputs, tool results) after each major step and supporting resume-from-checkpoint prevents restarting an hours-long workflow from scratch. Mistral Workflows, OpenAI Agents SDK, and similar runtimes are standardizing this as expected infrastructure.
- **Review artifacts over raw transcripts.** For complex agent work, ask for purpose-built review artifacts (HTML explainers, annotated diffs, comparison grids, one-off editors) when a human needs to inspect options, tune values, or export structured decisions back into the workflow.
- **Dark factory / light factory.** Split agentic workflows into a **light** layer (planning, review, and human-agent interaction stay visible) and a **dark** layer (clearly defined execution runs in the background without human monitoring). As trust builds in the dark layer's output, more work moves out of the visible layer. Distinct from simple background execution: the light/dark split is a deliberate architectural boundary, not just async scheduling. *Source: Gas City workshop, Every (2026-05-19)*
- **Mayor + polecats (one pet + many cattle).** One persistent, named supervisor agent (the "mayor") that a human interacts with directly. The mayor routes work to many anonymous, disposable worker agents ("polecats") that each handle one scoped task and shut down. The human manages one conversation; the mayor manages coordination and worker lifecycle. Workers don't accumulate context or interfere with each other — fresh start per task. *Source: Gas City workshop, Every (2026-05-19)*
- **Loop-first design.** Before writing a single prompt, define what a successful loop looks like: trigger → goal condition → tool set → escalation. The loop is the unit of work, not the prompt. A well-designed loop handles variance you never predicted; a prompt just handles the case you imagined. *Source: Steipete/AINews, Satya Nadella essay, Hoop case study (June 2026)*
- **Loop taxonomy before loop complexity.** Anthropic's Claude Code team defines loops as agents repeating cycles of work until a stop condition is met, then separates four levels: turn-based loops hand off the check, goal-based loops hand off the stop condition, time-based loops hand off the trigger, and proactive loops hand off the prompt for recurring well-defined work. Use the lightest loop that fits the task.
- **Explicit stop criteria.** Goal-based and proactive loops work best when "done" is deterministic: tests pass, Lighthouse score clears a threshold, queue is empty, PR merges, or a turn cap is reached. Vague "make it better" loops increase both cost and drift.
- **Cost-aware loop primitives.** Use scripts for deterministic work, run small pilots before dynamic workflows that may spawn many agents, choose cheaper/faster models for routine parts, and monitor `/usage`, `/goal`, and `/workflows` breakdowns.
- **Control layer before software factory.** The AI Engineer World Fair loops debate sharpened the current constraint: loops are already useful, but the field has not settled the control layer for permissions, cost ceilings, review bottlenecks, and recovery. Treat "software factory" as a destination, not a starting architecture.
- **Economic loop discipline.** Token usage is now a monitored production metric. Long-running loops should have task budgets, effort settings, stop conditions, and retry limits; teams cannot buy their way out of weak task decomposition with more tokens.
- **Live-state rollback and forking.** Tools such as [Shepherd](../tools/shepherd.md) suggest a new primitive for agent work: checkpoint a run, rewind to a known-good state, fork an alternate trajectory, and keep the useful branch instead of restarting the whole session.
- **Tool set clarity over prompt complexity.** Give the model a small set of clear, powerful tools and let it reason about which to use. Don't hardcode which tool gets called at each step. "If you give a reasoning model simple, powerful tools, it can handle situations you never thought to code for." More sophisticated prompt sequencing cannot substitute for a clean tool set. *Source: Stella Garber/Hoop, Every (June 2026)*
- **Deploy where the user already works.** The fastest path to agent adoption is integrating into the existing workflow surface (Slack, email, existing dashboards) rather than requiring users to learn a new app. The agent becomes a service within the existing context, not a parallel system to context-switch into. *Source: Hoop/Stella Garber case study, Every (June 2026)*

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
- Current framework docs make a layer split more explicit than earlier commentary did: Deep Agents is an agent harness, while Goose is a local agent product with desktop, CLI, API, provider, and MCP surfaces.
- Google's ADK 2.0 thread makes an enterprise version of the same thesis concrete: reliable orchestration comes from structural control over sequence, handoff, and execution boundaries, not just more detailed prompts.
- Anthropic's dynamic workflows (Claude Code, research preview) productize the plan→fan-out→verify→converge loop: Claude writes orchestration scripts running tens-to-hundreds of parallel subagents, with adversarial agents trying to break each finding before it surfaces, durable checkpoint/resume, and coordination held outside the conversation so the plan survives as the task grows. The Bun Zig→Rust rewrite is the cited large-scale example.
- Anthropic's Claude Code loop taxonomy turns loop choice into an operating decision: use normal turn-based prompts for exploration, `/goal` for deterministic exits, `/loop` or `/schedule` for time-triggered checks, and proactive routines only when the work is recurring and well-defined.
- Every's Hoop case study (June 2026): Stella Garber built an agent-native product in under 10 hours using simple Claude API + Slack integration; the key insight was tool clarity over prompt complexity — the agent found solutions the team hadn't thought to code for.
- Satya Nadella's June 2026 X essay (60M views) frames the loop as the primary product: build a learning loop where human capital and token capital compound, not just pick the best model.
- AINews coined "Loopcraft" (June 2026) to name the paradigm: designing loops that prompt agents rather than prompting agents directly.

## Failure modes

- Letting all agents share one bloated context by default
- Asking a generator to be its own evaluator on subjective tasks
- Retrying the same failed plan with slightly different wording
- Confusing visible complexity in the harness with actual robustness
- Treating orchestrator complexity as a substitute for stable context packaging
- Confusing more agents with more leverage when the human review bottleneck does not move
- Building cool tools with no concrete user journey or evaluation target
- Encoding mandatory workflow order only in natural-language instructions and expecting the model not to compress or reorder the procedure over time
- Building one giant "do everything" agent instead of separating specialists with narrower permissions and clearer handoff boundaries

## Recent changes

- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.
- [2026-07-03] AI Engineer World Fair loop debate: agents are moving from hype to control-layer problems; surveys report widespread agent use but primitive controls and review bottlenecks.
- [2026-06-30] Anthropic published the Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops.

## Sources

- [Notion's Token Town / software factory discussion](../sources/newsletters/notion-token-town.md)
- [AINews — The Two Sides of OpenClaw (harness section)](../sources/newsletters/ainews-openclaw-2026-04-18.md)
- [Garry Tan on ambiguity gates / confusion protocol](../sources/tweets/garrytan-confusion-protocol.md)
- [Matt Pocock on shared language, bounded contexts, and ADRs](../sources/tweets/matt-pocock-ddd-adr.md)
- [Harness engineering patterns](../sources/newsletters/harness-engineering-patterns.md)
- [Harness engineering in early April](../sources/newsletters/harness-engineering-early-april.md)
- [Open-agent orchestration in late March](../sources/newsletters/open-agent-orchestration-late-march.md)
- [Skills and plugin packaging in late March](../sources/newsletters/skills-and-plugin-packaging-late-march.md)
- [Harness engineering in mid-March](../sources/newsletters/harness-engineering-march.md)
- [Deep Agents overview](../sources/articles/deep-agents-overview.md)
- [Goose platform overview](../sources/articles/goose-platform.md)
- [Agent infrastructure, harness engineering, and collaborative agent systems](../sources/newsletters/agent-infrastructure-harness-2026-05-01.md)
- [AI-managed orchestration and local browser agents](../sources/newsletters/ai-managed-orchestration-local-browser-agents-2026-04-28.md)
- [Production agent orchestration primitives](../sources/newsletters/production-agent-orchestration-2026-04-29.md)
- [Agent-generated HTML artifacts](../sources/tweets/agent-html-artifacts-2026-05-13.md)
- [Inside the 100-agent Software Factory — Gas City](../sources/newsletters/gas-city-software-factory-2026-05.md)
- [Introducing dynamic workflows in Claude Code](../sources/articles/dynamic-workflows-claude-code.md)
- [Loopcraft and agent-native architecture — June 2026 digest](../sources/newsletters/loopcraft-june-2026.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Shepherd live agent rollback tweet](../sources/tweets/shepherd-live-agent-rollback-2026-07-06.md)
- [Getting started with loops](../sources/articles/claude-code-getting-started-with-loops-2026-06-30.md)
