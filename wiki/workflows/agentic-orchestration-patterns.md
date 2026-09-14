---
title: Agentic orchestration patterns
type: workflow
domains: [agents, coding]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-09-09
sources: [notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, harness-engineering-early-april, open-agent-orchestration-late-march, skills-and-plugin-packaging-late-march, harness-engineering-march, deep-agents-overview, goose-platform, googlecloudtech-adk-2-orchestration-patterns, agent-infrastructure-harness-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, production-agent-orchestration-2026-04-29, agent-html-artifacts-2026-05-13, gas-city-software-factory-2026-05, aiewf-loops-debate-2026-07-03, shepherd-live-agent-rollback-2026-07-06, software-factories-fde-2026-07, ai-code-review-eval-integrity-2026-06, token-tightening-ai-finops-2026-06, dashbench-code-review-understanding-2026-07, andy-matuschak-agent-loop-tempo-2026-07, ainews-new-ai-infra-unicorns-2026-05-22, aiewf-2026-five-trends-latentspace, cursor-agent-swarm-economics-2026-09-07, latent-space-pr-not-welcome-2026-09-01, every-folder-is-the-agent-2026-09-04, cursor-self-driving-codebases-2026-09-09, ubereng-software-factory-2026-08-28]
---

# Agentic orchestration patterns

Reusable patterns for getting better behavior from one or more agents without depending on a single provider or model family. The central lesson from recent sources: simple harnesses, strong evals, explicit boundaries, and safer escalation logic often matter more than increasingly elaborate agent scaffolds. Loop-design patterns for a single agent live on [Agent loop design](agent-loop-design.md); topology patterns for running several agents together live on [Multi-agent coordination](multi-agent-coordination.md).

## Current patterns

### Context, isolation, and shared knowledge

- **Scoped context, not global context.** Inject only the files, rules, or project context a sub-agent actually needs; keep the rest out of the loop to avoid context bleed.
- **Shared storage, isolated execution.** Let agents collaborate through the same repo, files, or knowledge store while keeping compute sandboxes separate; this preserves coordination without forcing one giant mutable runtime.
- **Worktree-based parallelism.** Isolate concurrent agent work in separate branches/worktrees so supervision, diff review, and rollback stay manageable.
- **Folder-scoped specialization.** A durable folder plus instructions, skills, and accumulated context often works better than a "swarm" of generic agents sharing one giant context. A concrete production instance: Every's Cora GM runs 44 specialized agents as folders (each a project directory with a CLAUDE.md/AGENT.md, skills, and months of accumulated institutional knowledge), routed by a small dispatch layer — a daemon watches a directory for spawn requests, a lead agent breaks a task into subtasks and writes each as a file, worker agents in the right folders pick them up and report back by writing files, and the daemon polls status every 60 seconds. Two slash commands cover most interaction: a cross-project status briefing, and a task-kickoff command that spawns the lead and workers. He cites Anthropic's own multi-agent research to justify the approach — an Opus lead with Sonnet sub-agents beat a single Opus agent by 90% on research tasks, but multi-agent setups burn 15x more tokens, and most coding tasks parallelize worse than research does — and states the hard-won rule plainly: "you can't vibe orchestrate." Build a flow, use it yourself, and trust it before handing it to autonomous dispatch. *Source: Every, "The Folder Is the Agent" (2026-09-04)*
- **Externalize the knowledge layer.** Graphs, wikis, and maintained context stores can stabilize long-running work better than repeatedly rebuilding understanding from raw files alone. See [Knowledge architectures](../concepts/knowledge-architectures.md) for the wiki's vocabulary for these stores.
- **AI Context Graph: grounding agents in a queryable knowledge graph.** Rather than leaving agents to discover context via blind code search, ground them in a unified, queryable graph of the organization's actual systems. Uber's version spans 24 million nodes and 80 million edges across 86 node types and 117 edge types, integrating 30+ internal systems (services, teams, incident logs, PRs, architecture docs, deployments, datasets, historical table-usage queries) and answerable in natural language. The measured gap is stark: on an identical prompt to the same model, the graph-grounded agent identified the right table (used by 50+ analysts) and answered in 38 seconds, while the ungrounded agent spent 20+ minutes inspecting service code, spawned 2 subagents, hit 3 errors, and concluded — incorrectly — that the dataset was unqueryable. *Source: Uber Engineering, "Running a Software Factory Efficiently at Uber Scale" (2026-08-28)*
- **Artifact-backed agent collaboration.** Multi-agent work is more durable when agents exchange work through a shared storage layer — such as a cloud dataset bucket or shared filesystem — rather than sharing a single runtime. Each agent runs in its own isolated environment and coordinates through the artifact store. Agent Collabs demonstrates this with Hugging Face: dataset buckets serve as shared storage, and Hugging Face Spaces provide each agent's isolated execution environment, letting agents built on different frameworks collaborate without coupling their runtimes.
- **Sandboxed executors for evidence-producing steps.** If a step needs real code execution, parsing, tests, or transformations, run it in an isolated workspace with explicit limits instead of asking the model to simulate execution in text.

### Harness, packaging, and tool design

- **CLI-first execution.** For many serious agent workflows, the command line remains the most composable surface because permissions, files, worktrees, and logs stay legible.
- **Hosted packaging for repeatable agents.** One-click or prepackaged agents can make a reusable workflow distributable across a team without each user rebuilding the harness from scratch.
- **Package the workflow, not just the tool.** Teams increasingly bundle skills, hooks, MCP wiring, rules, and slash commands into something installable so one person's working agent setup becomes another person's starting point.
- **Share skills, not just code.** Reusable skills increasingly package the fuzzy operating judgment that teams want many agents to inherit.
- **Hook the workflow, don't just describe it.** If a step must happen reliably, wire it into the harness or hook layer instead of leaving it as a prompt suggestion.
- **Thin harness, fat skills, fat code.** Put fuzzy human-like operating judgment into reusable skills and deterministic work into code, while keeping the harness itself small and legible.
- **Harnesses and hosts are separating.** Deep Agents-style systems package planning, filesystem context, subagents, permissions, and memory into a batteries-included harness for specialized agent behavior. Goose-style systems package provider setup, MCP, and desktop/CLI/API surfaces into a local agent host product. Those are different layers, and teams should not confuse framework choice with host-surface choice.
- **Composable skills with progressive disclosure.** Skills work best as small, reusable units with clear interfaces; load their full context only when invoked so agents can have broad capability surfaces without always paying the token cost.
- **Cross-language delegation through a common protocol.** In larger organizations, useful agent systems often span Python, TypeScript, Go, and Java teams; protocolized handoff matters more than assuming one language or one repo owns the whole workflow.
- **Tool set clarity over prompt complexity.** Give the model a small set of clear, powerful tools and let it reason about which to use. Don't hardcode which tool gets called at each step. "If you give a reasoning model simple, powerful tools, it can handle situations you never thought to code for." More sophisticated prompt sequencing cannot substitute for a clean tool set. *Source: Stella Garber/Hoop, Every (June 2026)*
- **Code-mode: batch tool calls into one script instead of one model turn each.** Standard MCP tool use costs a full model turn per action — emit a request, load the raw response into context, process it, repeat — so a single multi-step task (e.g. one SQL query needing 2-5 status polls) burns several turns on protocol overhead alone. Code-mode instead lets the model write a script that runs the whole sequence in a subprocess and returns only a summary to the model's context. Measured on identical tasks run both ways: even minimal responses saw token use drop over 50% (the savings come from cutting schema init, multi-turn polling, and redundant reasoning, not from avoiding large payloads), and bulk/N-turn workflows compounded that to over 90%, since an N-model-turn loop collapses into a single script execution. *Source: Uber Engineering, "Running a Software Factory Efficiently at Uber Scale" (2026-08-28)*

### Evaluation and review

- **Evaluator separation.** Use a distinct evaluator or verifier for long-running work; generators routinely overrate their own output. A community-built example for OpenAI's Codex CLI ([donvito/codex-astra-luna-orchestrator](https://github.com/donvito/codex-astra-luna-orchestrator/)) pins this at the config level: GPT-6 Astra plans/orchestrates and reviews, while GPT-5.6 Luna executes across explorer/worker/tester/researcher subagent roles — critically, the reviewer role stays pinned to Astra even on the cheaper "Plus" plan variant (where Luna at max reasoning takes over the orchestrator role too), so the model that reviews code is never the same model that wrote it, on either tier.
- **Failure-aware replanning.** Don't blindly retry. Feed structured failure metadata back into the orchestrator so it can generate a different plan.
- **Eval-driven simplification.** Prefer the simplest harness that passes evals. A cleaner representation layer and stronger verification often beat "smarter-looking" orchestration.
- **Review artifacts over raw transcripts.** For complex agent work, ask for purpose-built review artifacts (HTML explainers, annotated diffs, comparison grids, one-off editors) when a human needs to inspect options, tune values, or export structured decisions back into the workflow. For pull requests, see [AI PR and code review](ai-pr-code-review.md).
- **Review standards as repo context.** Put team-specific AI review criteria in Markdown near the code so code-review agents can apply local rules rather than generic style advice. This becomes more important as PR review becomes a distinct agent workflow with its own evals and replay datasets.
- **Review lenses.** No single review lens catches everything; stacking several imperfect, decorrelated reviewers (full transcript vs. output-only vs. codebase-only; different underlying models) compounds toward much higher reliability than one "best" reviewer, the way self-driving systems exceed human reliability without any single perfect sensor.

### Escalation, culture, and process

- **Ambiguity gates.** When the cost of guessing wrong is high, stop and ask instead of auto-continuing. Good for architecture forks, destructive operations, or underspecified user requests.
- **Demos over memos.** Prototype working flows behind flags or internal demos before locking in a long design-document process.
- **Self-rebuild culture.** In fast-moving agent systems, teams must be willing to replace their own scaffolding repeatedly as model and environment capabilities change.
- **Deploy where the user already works.** The fastest path to agent adoption is integrating into the existing workflow surface (Slack, email, existing dashboards) rather than requiring users to learn a new app. The agent becomes a service within the existing context, not a parallel system to context-switch into. *Source: Hoop/Stella Garber case study, Every (June 2026)*

### Production, cost, and reliability

- **Config-driven agent deployment.** Production agent frameworks are packaging sandboxing, auth, RBAC (Role-Based Access Control — who can do what), credential handling, and frontend configuration into deployable manifests (such as a `deepagents.toml` file). Without this, each developer writes the same custom setup from scratch for every new agent project: spinning up sandboxes, storing credentials safely, and configuring who has access to what.
- **Local-first browser agents.** For tasks that can be fully executed client-side, agents run entirely in the browser — no cloud handoff, no server-side compute. This reduces latency, cost, and privacy surface. The pattern is emerging as a complement to (not a replacement for) cloud-backed agents in orchestrated systems.
- **Durable workflow execution.** Production agent workflows should survive process crashes and infrastructure interruptions. Checkpointing state (memory, partial outputs, tool results) after each major step and supporting resume-from-checkpoint prevents restarting an hours-long workflow from scratch. Mistral Workflows, OpenAI Agents SDK, and similar runtimes are standardizing this as expected infrastructure.
- **Dark factory / light factory.** Split agentic workflows into a **light** layer (planning, review, and human-agent interaction stay visible) and a **dark** layer (clearly defined execution runs in the background without human monitoring). As trust builds in the dark layer's output, more work moves out of the visible layer. Distinct from simple background execution: the light/dark split is a deliberate architectural boundary, not just async scheduling. *Source: Gas City workshop, Every (2026-05-19)*
- **Cost-aware loop primitives.** Use scripts for deterministic work, run small pilots before dynamic workflows that may spawn many agents, choose cheaper/faster models for routine parts, and monitor `/usage`, `/goal`, and `/workflows` breakdowns. See [Cost-aware AI task routing](../training/cost-aware-ai-task-routing.md) for the fuller routing framework.
- **Control layer before software factory.** The AI Engineer World Fair loops debate sharpened the current constraint: loops are already useful, but the field has not settled the control layer for permissions, cost ceilings, review bottlenecks, and recovery. Treat "software factory" as a destination, not a starting architecture.
- **Software factory loop.** Long-running agents can cover planning, design, coding, testing, review, deployment, maintenance, and feedback, while humans supervise interfaces, policies, escalation, and customer-specific workflow fit rather than editing every artifact.
- **PRs closed by default, software factories instead.** Several AI-native OSS projects now auto-close external human pull requests rather than reviewing them as code, routing incoming issues through their own agent pipelines instead: Vercel's AI SDK factory (20M+ weekly npm downloads) authors 25-35% of merged PRs and closes 70-80% of issues, four weeks after deployment; Astro's auto-triage system reversed years of unmanageable issue backlog into a routine weekly task; [Flue](../tools/flue.md) goes further, auto-converting every external PR into an issue or discussion. The framing from tldraw's Steve Ruiz and Ghostty's Mitchell Hashimoto: once agents can implement a well-specified issue, a human PR is no longer more valuable than the issue that specifies it — so large OSS projects increasingly limit community contribution to reporting, discussion, and perspective rather than code.
- **Economic loop discipline.** Token usage is now a monitored production metric. Long-running loops should have task budgets, effort settings, stop conditions, retry limits, checkpoints, definitions of done, opt-in heavy reasoning, and cache-hit monitoring. Teams should review shipped output and human review cost, not just whether the loop burned tokens.
- **Live-state rollback and forking.** Tools such as [Shepherd](../tools/shepherd.md) suggest a new primitive for agent work: checkpoint a run, rewind to a known-good state, fork an alternate trajectory, and keep the useful branch instead of restarting the whole session.

## Where these patterns surfaced

- Latent Space's "PRs Not Welcome" feature documents three production software factories (Vercel AI SDK, Astro/Flue, tldraw) that closed PRs to humans and routed contributions through their own agents instead.
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
- Every's Hoop case study (June 2026): Stella Garber built an agent-native product in under 10 hours using simple Claude API + Slack integration; the key insight was tool clarity over prompt complexity — the agent found solutions the team hadn't thought to code for.
- AI Engineer World's Fair 2026 gave the software-factory/FDE pattern concrete named examples: Sierra's Natalie Meurer described forward-deployed-engineer work as managing "all the integrations and all the teams that contribute to the agent"; Cursor's Pauline Brunet framed FDE engagements around a "strict ROI" bar so customers don't turn the agents off after the engagement ends; Warp CEO Zach Lloyd described Oz, a new software-factory platform where organizations choose which lifecycle stages to automate and where humans stay in the loop for high-risk changes.

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

- [2026-09-09] Extended evaluator separation with a community Codex config (donvito/codex-astra-luna-orchestrator) that pins the reviewer role to a different model than the writer on both subscription tiers. (The rest of this source's content — Cursor's harness-evolution lessons and the swarm-coordination-failures extension — landed on [Multi-agent coordination](multi-agent-coordination.md) instead, since that page now holds the bullet they extend.)
- [2026-09-09] Split loop-design patterns into [Agent loop design](agent-loop-design.md) and multi-agent topology patterns into [Multi-agent coordination](multi-agent-coordination.md); regrouped the remaining patterns under `###` subheads (context/isolation, harness/packaging, evaluation/review, escalation/culture, production/cost).
- [2026-08-28] Added the AI Context Graph pattern (grounding agents in a queryable graph of internal systems instead of blind code search — Uber's version: 24M nodes/80M edges, 38-second grounded vs. 20+-minute-and-3-errors ungrounded on an identical prompt) and Code-mode (batching tool calls into one subprocess script instead of one model turn per call — >50% token reduction on minimal responses, >90% on bulk workflows).
- [2026-09-07] Added the review-lenses pattern.
- [2026-09-04] Extended folder-scoped specialization with a concrete 44-agent dispatch-layer implementation (daemon, status/orchestrate commands, file-based worker reporting) and Anthropic's multi-agent-research numbers (90% better / 15x tokens for Opus-lead + Sonnet-subagent research tasks).
- [2026-09-01] Added the "PRs closed by default" software-factory pattern with three named production examples (Vercel AI SDK, Astro/Flue, tldraw) and their concrete PR/issue-closure numbers.
- [2026-07-14] Added named AI Engineer World's Fair 2026 detail to the software-factory/FDE pattern: named FDE examples (Sierra, Cursor, Warp Oz).
- [2026-07-08] Linked PR review artifacts and repo-local review standards to the dedicated AI PR/code-review workflow.
- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.

## Related

- [Agent loop design](agent-loop-design.md) — loop-first design, taxonomy, tempo, and stop-criteria patterns for a single agent's own loop
- [Multi-agent coordination](multi-agent-coordination.md) — topology, routing, and coordination-failure patterns for running several agents together
- [Harness (agent)](../concepts/harness.md) — harness architecture; this page covers the reusable operating patterns built on top of it
- [Agent Labs vs Model Labs](../concepts/agent-labs-vs-model-labs.md) — the model-neutrality argument behind harness-level model routing
- [Agent skill methodology](../training/agent-skill-methodology.md) — how to author the skills referenced in the "share skills, not just code" and progressive-disclosure patterns above

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
- [Inside the 100-agent Software Factory — Gas City](../sources/newsletters/gas-city-software-factory-2026-05.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Shepherd live agent rollback tweet](../sources/tweets/shepherd-live-agent-rollback-2026-07-06.md)
- [Software factories and forward-deployed agent engineering](../sources/newsletters/software-factories-fde-2026-07.md)
- [AI code review and benchmark integrity](../sources/newsletters/ai-code-review-eval-integrity-2026-06.md)
- [Token tightening and AI FinOps](../sources/newsletters/token-tightening-ai-finops-2026-06.md)
- [DashBench and understanding-preserving AI code review](../sources/newsletters/dashbench-code-review-understanding-2026-07.md)
- [Andy Matuschak on coding-agent loop tempo](../sources/tweets/andy-matuschak-agent-loop-tempo-2026-07.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
- [5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space](../sources/newsletters/aiewf-2026-five-trends-latentspace.md)
- [Cursor — Agent swarms and the new model economics](../sources/articles/cursor-agent-swarm-economics-2026-09-07.md)
- [Cursor — Towards self-driving codebases](../sources/articles/cursor-self-driving-codebases-2026-09-09.md)
- [Uber Engineering — Running a Software Factory Efficiently at Uber Scale](../sources/tweets/ubereng-software-factory-2026-08-28.md)
