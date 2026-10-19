---
title: Agentic orchestration patterns
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-09-09
sources: [notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, harness-engineering-early-april, open-agent-orchestration-late-march, skills-and-plugin-packaging-late-march, harness-engineering-march, deep-agents-overview, goose-platform, googlecloudtech-adk-2-orchestration-patterns, agent-infrastructure-harness-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, production-agent-orchestration-2026-04-29, agent-html-artifacts-2026-05-13, aiewf-loops-debate-2026-07-03, shepherd-live-agent-rollback-2026-07-06, ai-code-review-eval-integrity-2026-06, token-tightening-ai-finops-2026-06, dashbench-code-review-understanding-2026-07, andy-matuschak-agent-loop-tempo-2026-07, ainews-new-ai-infra-unicorns-2026-05-22, cursor-agent-swarm-economics-2026-09-07, every-folder-is-the-agent-2026-09-04, cursor-self-driving-codebases-2026-09-09, ubereng-software-factory-2026-08-28]
---

# Agentic orchestration patterns

Reusable patterns for getting better behavior from one or more agents without depending on a single provider or model family. The central lesson from recent sources: simple harnesses, strong evals, explicit boundaries, and safer escalation logic often matter more than increasingly elaborate agent scaffolds. Loop-design patterns for a single agent live on [Agent loop design](agent-loop-design.md); topology patterns for running several agents together live on [Multi-agent coordination](multi-agent-coordination.md).

## Current patterns

### Context, isolation, and shared knowledge

- **Scoped context, not global context.** Inject only the files, rules, or project context a sub-agent actually needs; keep the rest out of the loop to avoid context bleed.
- **Shared storage, isolated execution.** Let agents collaborate through the same repo, files, or knowledge store while keeping compute sandboxes separate; this preserves coordination without forcing one giant mutable runtime.
- **Worktree-based parallelism.** Isolate concurrent agent work in separate branches/worktrees so supervision, diff review, and rollback stay manageable.
- **Folder-scoped specialization.** A durable folder plus instructions, skills, and accumulated context often works better than a "swarm" of generic agents sharing one giant context. Every's Cora GM runs 44 specialized agents as folders (each a project directory with a CLAUDE.md/AGENT.md, skills, and months of accumulated knowledge), routed by a small file-based dispatch layer: a daemon watches for spawn requests, a lead agent writes subtasks as files, workers in the right folders pick them up and report back by writing files, and the daemon polls status every 60 seconds. The justification is Anthropic's multi-agent research (an Opus lead with Sonnet sub-agents beat a single Opus agent by 90% on research tasks, at 15x the tokens, and most coding parallelizes worse than research), and the rule is "you can't vibe orchestrate": build a flow, use it yourself, and trust it before handing it to autonomous dispatch. *Source: Every, "The Folder Is the Agent" (2026-09-04)*
- **Domain language and decision records.** Shared domain vocabulary (DDD-style bounded contexts) and architecture decision records make large codebases more navigable for agents and humans alike (Matt Pocock).
- **Externalize the knowledge layer.** Graphs, wikis, and maintained context stores can stabilize long-running work better than repeatedly rebuilding understanding from raw files alone. See [Knowledge architectures](../concepts/knowledge-architectures.md) for the wiki's vocabulary for these stores.
- **AI Context Graph: grounding agents in a queryable knowledge graph.** Instead of blind code search, ground agents in a natural-language-queryable graph of the organization's actual systems. Uber's spans 24 million nodes and 80 million edges (86 node types, 117 edge types) across 30+ internal systems: services, teams, incident logs, PRs, architecture docs, deployments, datasets, and historical table-usage queries. On an identical prompt to the same model, the grounded agent found the right table (used by 50+ analysts) in 38 seconds; the ungrounded agent spent 20+ minutes in service code, spawned 2 subagents, hit 3 errors, and wrongly concluded the dataset was unqueryable. *Source: Uber Engineering, "Running a Software Factory Efficiently at Uber Scale" (2026-08-28)*
- **Artifact-backed agent collaboration.** The concrete form of shared storage with isolated execution: agents exchange work through an artifact store (a cloud dataset bucket or shared filesystem), each in its own isolated environment. Agent Collabs does this with Hugging Face dataset buckets as storage and Spaces as per-agent execution, so agents on different frameworks collaborate without coupling their runtimes.
- **Sandboxed executors for evidence-producing steps.** If a step needs real code execution, parsing, tests, or transformations, run it in an isolated workspace with explicit limits instead of asking the model to simulate execution in text.

### Harness, packaging, and tool design

- **CLI-first execution.** For many serious agent workflows, the command line remains the most composable surface because permissions, files, worktrees, and logs stay legible. Notion's AI team decides MCP versus a tighter custom integration per workflow rather than defaulting to either.
- **Hosted packaging for repeatable agents.** One-click or prepackaged agents can make a reusable workflow distributable across a team without each user rebuilding the harness from scratch.
- **Package the workflow, not just the tool.** Teams increasingly bundle skills, hooks, MCP wiring, rules, and slash commands into something installable so one person's working agent setup becomes another person's starting point.
- **Skills as the reusable unit.** Sharing skills rather than only code, "thin harness, fat skills, fat code", and composable skills with progressive disclosure are covered on [Agent skill methodology](../training/agent-skill-methodology.md).
- **Hook the workflow, don't just describe it.** If a step must happen reliably, wire it into the harness or hook layer instead of leaving it as a prompt suggestion.
- **Harnesses and hosts are separating.** Deep Agents-style systems package planning, filesystem context, subagents, permissions, and memory into a batteries-included harness for specialized agent behavior. Goose-style systems package provider setup, MCP, and desktop/CLI/API surfaces into a local agent host product. Those are different layers, and teams should not confuse framework choice with host-surface choice.
- **Cross-language delegation through a common protocol.** In larger organizations, useful agent systems often span Python, TypeScript, Go, and Java teams; protocolized handoff matters more than assuming one language or one repo owns the whole workflow. Google's ADK 2.0 makes the enterprise case: reliable orchestration comes from structural control over sequence, handoff, and execution boundaries, not more detailed prompts.
- **Tool set clarity over prompt complexity.** Give the model a small set of clear, powerful tools and let it choose, rather than hardcoding which tool runs at each step: "If you give a reasoning model simple, powerful tools, it can handle situations you never thought to code for." More sophisticated prompt sequencing cannot substitute for a clean tool set. Hoop's Stella Garber built an agent-native product this way in under 10 hours with the Claude API and Slack. *Source: Every (June 2026)*
- **Code-mode: batch tool calls into one script instead of one model turn each.** Standard MCP tool use costs a full model turn per action, so one multi-step task (e.g. a SQL query needing 2-5 status polls) burns several turns on protocol overhead. Code-mode lets the model write a script that runs the whole sequence in a subprocess and returns only a summary. On identical tasks run both ways, even minimal responses used over 50% fewer tokens (savings come from cutting schema init, multi-turn polling, and redundant reasoning, not large payloads), and bulk/N-turn workflows over 90%, since an N-turn loop collapses into one script execution. *Source: Uber Engineering, "Running a Software Factory Efficiently at Uber Scale" (2026-08-28)*

### Evaluation and review

- **Evaluator separation.** Use a distinct evaluator or verifier for long-running work; generators routinely overrate their own output (Anthropic's long-running-agent work splits planner, generator, and evaluator for this reason). A community-built example for OpenAI's Codex CLI ([donvito/codex-astra-luna-orchestrator](https://github.com/donvito/codex-astra-luna-orchestrator/)) pins this in config: GPT-6 Astra plans, orchestrates, and reviews while GPT-5.6 Luna executes across explorer/worker/tester/researcher subagents; even on the cheaper "Plus" variant, where Luna also takes over orchestration, review stays pinned to Astra, so the reviewing model never wrote the code.
- **Failure-aware replanning.** Don't blindly retry. Feed structured failure metadata back into the orchestrator so it can generate a different plan.
- **Eval-driven simplification.** Prefer the simplest harness that passes evals. A cleaner representation layer and stronger verification often beat "smarter-looking" orchestration.
- **Review artifacts over raw transcripts.** For complex agent work, ask for purpose-built review artifacts (HTML explainers, annotated diffs, comparison grids, one-off editors) when a human needs to inspect options, tune values, or export structured decisions back into the workflow. For pull requests, see [AI PR and code review](ai-pr-code-review.md).
- **Review standards as repo context.** Put team-specific AI review criteria in Markdown near the code so code-review agents can apply local rules rather than generic style advice. This becomes more important as PR review becomes a distinct agent workflow with its own evals and replay datasets.
- **Review lenses.** No single review lens catches everything; stacking several imperfect, decorrelated reviewers (full transcript vs. output-only vs. codebase-only; different underlying models) compounds toward much higher reliability than one "best" reviewer, the way self-driving systems exceed human reliability without any single perfect sensor.

### Escalation, culture, and process

- **Ambiguity gates.** When the cost of guessing wrong is high, stop and ask instead of auto-continuing. Good for architecture forks, destructive operations, or underspecified user requests. Garry Tan's "confusion protocol" productizes this.
- **Demos over memos.** Prototype working flows behind flags or internal demos before locking in a long design-document process.
- **Self-rebuild culture.** In fast-moving agent systems, teams must be willing to replace their own scaffolding repeatedly as model and environment capabilities change.
- **Deploy where the user already works.** The fastest path to agent adoption is integrating into the existing workflow surface (Slack, email, existing dashboards) rather than requiring users to learn a new app. The agent becomes a service within the existing context, not a parallel system to context-switch into. *Source: Hoop/Stella Garber case study, Every (June 2026)*

### Production, cost, and reliability

- **Config-driven agent deployment.** Production agent frameworks are packaging sandboxing, auth, RBAC (Role-Based Access Control — who can do what), credential handling, and frontend configuration into deployable manifests (such as a `deepagents.toml` file). Without this, every new agent project rebuilds sandboxes, credential storage, and access rules from scratch.
- **Local-first browser agents.** For tasks that can be fully executed client-side, agents run entirely in the browser — no cloud handoff, no server-side compute. This cuts latency, cost, and privacy surface, complementing rather than replacing cloud-backed agents.
- **Durable workflow execution.** Checkpoint state (memory, partial outputs, tool results) after each major step and resume from checkpoint, so a crash doesn't restart an hours-long workflow. Mistral Workflows, OpenAI Agents SDK, and similar runtimes are standardizing this as expected infrastructure.
- **Cost-aware loop primitives.** Use scripts for deterministic work, run small pilots before dynamic workflows that may spawn many agents, choose cheaper/faster models for routine parts, and monitor `/usage`, `/goal`, and `/workflows` breakdowns. See [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) for the fuller routing framework.
- **Software factories.** End-to-end agent pipelines (dark/light factory split, control layer first, the software-factory loop, PRs closed by default in AI-native OSS) live on [Software factory](software-factory.md).
- **Economic loop discipline.** Token usage is now a monitored production metric. Long-running loops should have task budgets, effort settings, stop conditions, retry limits, checkpoints, definitions of done, opt-in heavy reasoning, and cache-hit monitoring. Teams should review shipped output and human review cost, not just whether the loop burned tokens.
- **Live-state rollback and forking.** Tools such as [Shepherd](../tools/shepherd.md) suggest a new primitive for agent work: checkpoint a run, rewind to a known-good state, fork an alternate trajectory, and keep the useful branch instead of restarting the whole session.

## Where these patterns surfaced

Patterns name their source inline where one company or practitioner is the main evidence; full provenance is under `## Sources`. Software-factory examples (Vercel AI SDK, Astro/Flue, tldraw, Sierra, Cursor, Warp Oz) moved with those patterns to [Software factory](software-factory.md).

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
- Generic AI review on large PRs creates noise unless review standards, diff scope, trigger points, and reviewer-comprehension artifacts are controlled.
- **Partial-control loop churn.** The human tries to delegate more than a fast pair-programming loop but still remains responsible for planning, technical guidance, and review. The result can be multiple half-understood agent threads rather than real leverage.
- Calling a one-shot fan-out pipeline a loop when no feedback signal drives a next cycle
- Running loops without naming the signal that closes them, which turns "autonomy" into unbounded execution

## Recent changes

- [2026-10-19] Split the software-factory patterns (dark/light factory, control layer before software factory, software factory loop, PRs closed by default) and the World's Fair FDE examples out to [Software factory](software-factory.md); moved the three skills bullets to [Agent skill methodology](../training/agent-skill-methodology.md); cut "Where these patterns surfaced" to a pointer after folding its unique facts (Notion's MCP-vs-custom call, Garry Tan's confusion protocol, Pocock's domain language and ADRs, Anthropic's planner/generator/evaluator split, ADK 2.0's structural-control thesis) into the pattern bullets.
- [2026-09-09] Extended evaluator separation with a community Codex config (donvito/codex-astra-luna-orchestrator) that pins the reviewer role to a different model than the writer on both subscription tiers. (The rest of this source's content — Cursor's harness-evolution lessons and the swarm-coordination-failures extension — landed on [Multi-agent coordination](multi-agent-coordination.md) instead, since that page now holds the bullet they extend.)
- [2026-09-09] Split loop-design patterns into [Agent loop design](agent-loop-design.md) and multi-agent topology patterns into [Multi-agent coordination](multi-agent-coordination.md); regrouped the remaining patterns under `###` subheads (context/isolation, harness/packaging, evaluation/review, escalation/culture, production/cost).
- [2026-09-07] Added the review-lenses pattern.
- [2026-09-04] Extended folder-scoped specialization with a concrete 44-agent dispatch-layer implementation (daemon, status/orchestrate commands, file-based worker reporting) and Anthropic's multi-agent-research numbers (90% better / 15x tokens for Opus-lead + Sonnet-subagent research tasks).
- [2026-08-28] Added the AI Context Graph pattern (grounding agents in a queryable graph of internal systems instead of blind code search — Uber's version: 24M nodes/80M edges, 38-second grounded vs. 20+-minute-and-3-errors ungrounded on an identical prompt) and Code-mode (batching tool calls into one subprocess script instead of one model turn per call — >50% token reduction on minimal responses, >90% on bulk workflows).
- [2026-07-08] Linked PR review artifacts and repo-local review standards to the dedicated AI PR/code-review workflow.
- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.

## Related

- [Agent loop design](agent-loop-design.md) — loop-first design, taxonomy, tempo, and stop-criteria patterns for a single agent's own loop
- [Multi-agent coordination](multi-agent-coordination.md) — topology, routing, and coordination patterns for running several agents together; Cursor's swarm failure modes and fixes are on [Long-running agent swarms](long-running-agent-swarms.md)
- [Harness (agent)](../concepts/harness.md) — harness architecture; this page covers the reusable operating patterns built on top of it
- [Agent Labs vs Model Labs](../concepts/agent-labs-vs-model-labs.md) — the model-neutrality argument behind harness-level model routing
- [Software factory](software-factory.md) — end-to-end agent pipelines: light/dark split, control layer first, PRs closed by default
- [Agent skill methodology](../training/agent-skill-methodology.md) — skills as the reusable unit: sharing skills, thin harness / fat skills, progressive disclosure, and how to author them

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
- [Google Cloud's ADK 2.0 orchestration patterns](../sources/tweets/googlecloudtech-adk-2-orchestration-patterns.md)
- [Agent infrastructure, harness engineering, and collaborative agent systems](../sources/newsletters/agent-infrastructure-harness-2026-05-01.md)
- [AI-managed orchestration and local browser agents](../sources/newsletters/ai-managed-orchestration-local-browser-agents-2026-04-28.md)
- [Production agent orchestration primitives](../sources/newsletters/production-agent-orchestration-2026-04-29.md)
- [Agent-generated HTML artifacts](../sources/tweets/agent-html-artifacts-2026-05-13.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Shepherd live agent rollback tweet](../sources/tweets/shepherd-live-agent-rollback-2026-07-06.md)
- [AI code review and benchmark integrity](../sources/newsletters/ai-code-review-eval-integrity-2026-06.md)
- [Token tightening and AI FinOps](../sources/newsletters/token-tightening-ai-finops-2026-06.md)
- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
- [Andy Matuschak on coding-agent loop tempo](../sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
- [Cursor — Agent swarms and the new model economics](../sources/articles/cursor-agent-swarm-economics-2026-09-07.md)
- [Cursor — Towards self-driving codebases](../sources/articles/cursor-self-driving-codebases-2026-09-09.md)
- [Uber Engineering — Running a Software Factory Efficiently at Uber Scale](../sources/tweets/ubereng-software-factory-2026-08-28.md)
