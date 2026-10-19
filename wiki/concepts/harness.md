---
title: Harness (agent)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-09
sources: [agentic-thinking-lin, langchain-better-harness, openai-agents-sdk-evolution, notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, claude-code-leak-architecture, harness-engineering-early-april, skills-and-plugin-packaging-late-march, harness-engineering-march, harness-debate-march, shopify-latent-space-april-2026, agent-infrastructure-harness-2026-05-01, mattpocock-dictionary-of-ai-coding, model-harness-fit-2026-05-13, gas-city-software-factory-2026-05, cloudflare-glasswing-2026-05, loopcraft-june-2026, aiewf-loops-debate-2026-07-03, autoresearch-agent-recipes-2026-07, claude-tag-slack-agent-2026-06, gray-swan-ai-security-2026-06, effective-feedback-compute-harness-2026-05, code-as-agent-harness-paper, aiewf-2026-five-trends-latentspace, zawinskis-law-multiagents-2026-08-08, flue-2-react-for-agents-2026-08-15, ainews-poolside-nvidia-2026-08-21, engineering-team-cost-of-codex-2026-08-19, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, primeintellect-prime-agent-2026-08-05, ainews-fal-h3-max-live-2026-09-01, ainews-muse-spark-13-2026-09-03, every-folder-is-the-agent-2026-09-04, ainews-navier-stokes-2026-09-09]
---

# Harness (agent)

The scaffolding that wraps an AI model and turns it into an agent capable of acting in the world. A harness defines *what* the model can do (tools, APIs, memory), *how* it reasons and plans (system prompt, instructions, routing logic), and *what environment* it operates in (browser, terminal, code sandbox, external services).

The analogy to model training is explicit in the field: just as training data shapes a model, the harness shapes an agent's behavior. As [LangChain's Better-Harness](../sources/tweets/langchain-better-harness.md) frames it: `harness + evals + harness engineering → better agent` mirrors `model + training data + gradient descent → better model`.

## What a harness includes

- **System prompt & instructions** — behavioral constraints, task framing, output format rules
- **Tool suite** — which tools the model can call, their descriptions, when to use them
- **Orchestration logic** — how the agent loops, when it escalates, how sub-agents are coordinated
- **Execution environment** — browser, terminal, code sandbox, API layers, memory systems
- **Storage / compute boundary** — durable shared context (repos, filesystems, knowledge stores) kept separate from isolated execution sandboxes, so agents collaborate without sharing one unsafe runtime
- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended; see [Agent evals](agent-evals.md) for the taxonomy of eval categories and the trajectory-vs-result distinction
- **Context-shaping layer** — practical systems increasingly treat repo state, recent edits, local instructions, and memory retrieval policy as part of the harness boundary, not as incidental prompt stuffing
- **Reusable operating modules** — skills, hook scripts, slash commands, plugin bundles, and agent recipes act as composable pieces of the harness; an agent recipe bundles harness, model choices, evals, judges, failure history, and signal-processing logic so a workflow can be reproduced.
- **Deployment manifest and access controls** — production harnesses increasingly package sandboxing, auth, RBAC (Role-Based Access Control — the rules that define which users and agents have permission to perform which operations), credential management, and frontend configuration into deployable artifacts; concrete implementations are on [Agent runtime platforms](agent-runtime-platforms.md).
- **Control layer** — permissions, approvals, cost ceilings, stop conditions, recovery, and review routing around an agent loop. The 2026 AI Engineer Survey reported high agent adoption but primitive safeguards, making the control layer part of harness design rather than a product afterthought.
- **Live-run recovery** — checkpointing, rollback, and forking of agent state so a failed trajectory can be repaired without discarding all context.

## Why it matters

In the reasoning era, the competitive edge was in model training — better RL, stronger feedback signals. In the agentic era, as [Junyang Lin argues](../sources/articles/agentic-thinking-lin.md), the edge is in the harness: environment quality, prompt precision, tool design, and the ability to iterate on behavior without retraining the model. Harness engineering is increasingly treated as a first-class discipline.

Lilian Weng's arc shows the shift: her 2023 essay described an agent as planning, memory, and tool use; her 2026 "Harness Engineering for Self-Improvement" argues the surrounding system (workflow, context, permissions, evaluation, persistent state, continuous improvement) now matters as much as the model (per Latent Space's AI Engineer World's Fair 2026 recap). Two vendor voices add that the harness should shrink as models improve: Anthropic's Thariq Shihipar calls Claude Fable "grown, not designed," with a spiky "capability overhead" a harness should not hard-code around, and OpenAI's Joe Gershenson (Core Agent team, ChatGPT Work and Codex) expects harness engineering to keep "finding ways to give the model more degrees of freedom" now that harnesses went mainstream in late 2025.

The March 5, 2026 "Is Harness Engineering real?" debate ("big model" collapses scaffolding vs "big harness" keeps the production advantage) did not produce a winner, but it made the harness a legible competitive surface; [Harness vs model](harness-vs-model.md) holds the numbers. The runtime, governance, and distribution layer around the harness (managed platforms, fleet control, plugin and skill packaging) is on [Agent runtime platforms](agent-runtime-platforms.md).

## What good harness engineering looks like

Operating patterns built on a harness (ambiguity gates, scoped context, failure-aware replanning, hooks, the dark/light factory split, worker topologies) live on [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md), [Software factory](../workflows/software-factory.md), [Agent loop design](../workflows/agent-loop-design.md), and [Multi-agent coordination](../workflows/multi-agent-coordination.md). What follows is specific to harness *architecture*:

### Memory, context, and repo awareness

- **Layered memory** keeps durable knowledge, topic files, and live-session context separate instead of forcing everything into one rolling transcript.
- **Repo-state awareness** gives the agent current branch, recent commits, and file-level state so it acts on the real workspace instead of a stale abstract summary.

### Reliability, review, security, and measurement

- **Permission boundaries** stay explicit. Good harnesses make it legible when the agent is allowed to act, when it must ask, and where risky execution is isolated.
- **Cache-efficient subagent parallelism** lets worker agents inherit enough shared context to be useful without rebuilding the full setup cost every time.
- **Critique loops and multi-model review** over flat parallel dispatch: a generator, a separate critic model, and a redo pass beat equivalent compute spent on parallel independent agents (Shopify, at scale; slower but more reliable where correctness is checkable). Sending the same code to Claude, Codex, and Kimi in parallel finds different bugs than running one model three times, at higher parallel token spend.
- **CI/CD as part of the harness boundary**: at high agent throughput (e.g. 30% MoM PR growth), deployment and verification become the bottleneck, so harness design must cover the downstream pipeline, not only the generation loop.
- **Measure effective feedback, not only activity.** Token counts, tool counts, and trace length are weak proxies; Effective Feedback Compute argues the useful signal is whether the harness gives the model actionable feedback that improves the next step.
- **Security boundary as harness boundary.** Tool-using agents read untrusted content, hold private context, and take actions, so a production harness must define identity, permissions, data-exfiltration boundaries, guardrails, red-team tests, and audit trails as part of the architecture — see [Prompt injection](prompt-injection.md).

### Design principles

- **Model neutrality by design.** Make the model a configurable parameter, not a hardcoded dependency: routing, context packaging, and evaluation live in the harness layer, not in model-specific prompt tricks. The evaluation layer can be decoupled too; see [Agent improvement loop](agent-improvement-loop.md) for LangSmith Engine. See [Agent Labs vs Model Labs](agent-labs-vs-model-labs.md) for the moat argument.
- **Code as the operational substrate, not just output.** A May 2026 survey ("Code as Agent Harness," arXiv:2605.18747) frames code as the shared medium connecting agent reasoning, acting, and environment modeling, not merely the agent's output. It organizes harness design in three layers: the code interface linking reasoning/action/environment; harness mechanisms (planning, memory, tool use, feedback-driven control); and scaling to multi-agent settings, where shared code artifacts support coordination, review, and verification.
- **Runtime, fleet, and distribution concerns** (managed-agent platforms, isolates vs containers, LLM proxies, enterprise MCP auth, agent-friendly CLIs, cookbooks and plugin packaging) are on [Agent runtime platforms](agent-runtime-platforms.md).

### Self-modifying and recursive harnesses

Self-rewriting harnesses (Headlong, exo, JIT-Agent, Prime Agent, HarnessDev, Better-Harness, Harness²) are on [Automated harness optimization](automated-harness-optimization.md); Harvey and Baseten's recursive due-diligence harness is on [Harness vs model](harness-vs-model.md).

## Harness vs folder-level context

- **Folder-level context** packages what the agent knows: codebase, instructions, skills, conventions, and durable local memory
- **Harness** packages how the agent operates: loop logic, tools, routing, retries, and evaluation

The two are related but not identical, and the vocabulary is not yet standardized. Many real-world "agent" improvements come from better context packaging rather than fancier orchestration.

## Ecosystem signals

Context-editing research lives on [Agent memory](agent-memory.md) and skill-retrieval findings on [Agent skill methodology](../training/agent-skill-methodology.md). Recent harness product signals: openJiuwen's fixed-model result is on [Harness vs model](harness-vs-model.md); Miles (RL-as-a-service) is on [RL harness quality](rl-harness-quality.md) and DeepSeek's plugin-contract changes on [Agent runtime platforms](agent-runtime-platforms.md); Google's Gemini team named new "AGY" harness patterns for iterative coding, document review, long formal proofs, and self-verification; and several independent voices (@omarsar0, @dejavucoder) named "harness engineering" a core, distinct AI-engineering skill.

## Caveats

- The term has no single agreed definition across the field. Some sources use it narrowly (just the prompt + tool config); others include the full execution environment and orchestration layer.
- This page reflects the broader definition, consistent with [Lin's essay](../sources/articles/agentic-thinking-lin.md) and [LangChain's Better-Harness](../sources/tweets/langchain-better-harness.md) framing.

## Recent changes

- [2026-10-19] Moved JIT-Agent and Prime Agent to [Automated harness optimization](automated-harness-optimization.md); model-harness fit and model-specific profiles to [Harness vs model](harness-vs-model.md); the OpenAI Agents SDK example, deployment-manifest implementations, and org-embedded identity to [Agent runtime platforms](agent-runtime-platforms.md); CommerceAgentBench to [Agent evals](agent-evals.md).
- [2026-10-19] Split runtime, fleet, and distribution material (tooling/fleet and managed-platform subsections, Cloudflare isolates, cloud-resident agents, late-March packaging) out to [Agent runtime platforms](agent-runtime-platforms.md); moved the skill-wiki and context-editing research to [Agent memory](agent-memory.md), Skill Lift, T3 Code's instruction-file result, and the Retrieval-Invoked Actual-Use Effect to [Agent skill methodology](../training/agent-skill-methodology.md), and the Harvey + Baseten harness-swap numbers, openJiuwen's fixed-model result, and FSM trace induction to [Harness vs model](harness-vs-model.md); trimmed "Why it matters", gave the Claude Platform GA fact a body home on Agent runtime platforms, and folded LangChain's deepagents primitives into the deployment-manifest bullet.
- [2026-10-19] Split the self-modifying harness bullet (Headlong, exo), "Harness continual learning", and the HarnessDev finding out to [Automated harness optimization](automated-harness-optimization.md), which also takes the new Harness² material.
- [2026-09-09] Split "RL harness quality" into [RL harness quality](rl-harness-quality.md), and "Harness vs model" plus the model/harness co-evolution theory into [Harness vs model](harness-vs-model.md); moved the 1,902-run multi-agent coordination study to [Multi-agent coordination](../workflows/multi-agent-coordination.md); renamed three date-named research-cluster headings to evergreen names and added `###` subheads to "What good harness engineering looks like".
- [2026-09-04] Added Harvey + Baseten's RLM due-diligence harness (23%→62% rubric pass rate via harness swap, +15-33 points from harness-specific post-training) and LangChain deepagents' subagent-forking and managed-connection primitives.
- [2026-09-01] Added a harness/context-engineering research cluster: WikiSkill/SKILL.state, ContextPilot, HarnessDev, the Retrieval-Invoked Actual-Use Effect paper, openJiuwen, and Miles.
- [2026-08-29] Added Google's skill-wiki ablation result (wiki carries most of the gain; skills transfer cross-model-family), T3 Code's agents.md/claude.md fine-tuning result, Google's AGY harness patterns, and the cloud-resident-agent shift (Claude Code `/resume`, Kimi Code Remote Control, OpenAI appshots, Ollama-hosted GLM-5.3-Flash backend); also added JIT-Agent, FSM trace induction, Hermes Agent's real-Chrome-profile browsing, Claude Managed Agents + Vercel Chat SDK cookbook, and CommerceAgentBench.
- [2026-08-25] Added NVIDIA's Skill Lift metric, two self-modifying agent harnesses (Headlong, exo), a single-harness-standardization position paper, and Anthropic's enterprise-managed MCP connector auth.
- [2026-08-21] Added DeepSeek Harness (DSH)/Cordis and TrueFoundry's open-source TrueForge as new harness-as-competitive-layer examples; Claude Platform reaches GA for computer use, browser tool, Skills API, and Files API, plus an AG-UI adapter; added harness continual learning (guarded harness evolution) as a new harness-research finding; added OpenAI's Joe Gershenson on harnesses simplifying as models improve, and a solo builder's specialist-Codex-agent-roster example.
- [2026-08-15] Flue 2 (Fred Schott, Astro creator) launched as a second concrete "harness is foundational, not a feature" framework alongside eve — React-style Agent Hooks that let an agent re-render its own tools/state on every turn.

## Related

- [Flue](../tools/flue.md) — Fred Schott's agent framework; React-style Agent Hooks built on the Pi minimal harness, a second concrete "harness as foundational" example alongside eve
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — the pattern catalog for context packaging, harness/packaging, and evaluation patterns built on top of a harness
- [Agent loop design](../workflows/agent-loop-design.md) — patterns for one agent's own loop
- [Multi-agent coordination](../workflows/multi-agent-coordination.md) — topology patterns for running several agents together
- [Harness vs model](harness-vs-model.md) — how much of a benchmark score comes from the harness rather than the model, with the concrete numbers
- [RL harness quality](rl-harness-quality.md) — the specific case where a harness doubles as an RL training environment
- [Agent evals](agent-evals.md) — taxonomy of agent evaluation categories and why trajectory quality matters alongside final results
- [Agent improvement loop](agent-improvement-loop.md) — the loop for improving a harness systematically via traces, evals, and targeted changes
- [Skillify — Agent Reliability Pattern](../workflows/skillify-agent-reliability.md) — pattern for encoding agent failures as permanent tested skills; "thin harness / fat skills" architecture
- [Prompt injection](prompt-injection.md) — the concrete security attack the harness security boundary defends against
- [Ontologies as agent guardrails](ontology-agent-guardrails.md) — a distinct, formally rule-based control mechanism that sits inside the harness's control/evaluation layer alongside prompts, evals, and permission logic
- [Agent runtime platforms](agent-runtime-platforms.md) — managed platforms, execution runtimes, fleet governance, and distribution around the harness
- [Automated harness optimization](automated-harness-optimization.md) — systems that improve the harness automatically: hill-climbing with evals, per-task refinement, self-modifying harnesses

## Sources

- [From 'Reasoning' Thinking to 'Agentic' Thinking by Junyang Lin](../sources/articles/agentic-thinking-lin.md)
- ["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/tweets/langchain-better-harness.md)
- [The next evolution of the Agents SDK](../sources/articles/openai-agents-sdk-evolution.md)
- [Notion's Token Town / software factory discussion](../sources/newsletters/notion-token-town.md)
- [AINews — The Two Sides of OpenClaw (harness section)](../sources/newsletters/ainews-openclaw-2026-04-18.md)
- [Garry Tan on ambiguity gates / confusion protocol](../sources/tweets/garrytan-confusion-protocol.md)
- [Matt Pocock on shared language, bounded contexts, and ADRs](../sources/tweets/matt-pocock-ddd-adr.md)
- [Harness engineering patterns](../sources/newsletters/harness-engineering-patterns.md)
- [Is harness engineering real?](../sources/newsletters/harness-debate-march.md)
- [Claude Code leak architecture lessons](../sources/newsletters/claude-code-leak-architecture.md)
- [Harness engineering in early April](../sources/newsletters/harness-engineering-early-april.md)
- [Skills and plugin packaging in late March](../sources/newsletters/skills-and-plugin-packaging-late-march.md)
- [Harness engineering in mid-March](../sources/newsletters/harness-engineering-march.md)
- [Shopify AI phase transition — Latent Space podcast (April 2026)](../sources/newsletters/shopify-latent-space-april-2026.md)
- [Agent infrastructure, harness engineering, and collaborative agent systems](../sources/newsletters/agent-infrastructure-harness-2026-05-01.md)
- [Matt Pocock — Dictionary of AI Coding](../sources/repos/mattpocock-dictionary-of-ai-coding.md)
- [Model-harness fit as coding-agent moat](../sources/newsletters/model-harness-fit-2026-05-13.md)
- [Inside the 100-agent Software Factory — Gas City](../sources/newsletters/gas-city-software-factory-2026-05.md)
- [Project Glasswing: what Mythos showed us — Cloudflare](../sources/articles/cloudflare-glasswing-2026-05.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Autoresearch and agent recipes](../sources/newsletters/autoresearch-agent-recipes-2026-07.md)
- [Claude Tag Slack-native agent launch](../sources/newsletters/claude-tag-slack-agent-2026-06.md)
- [Gray Swan on AI-native security and prompt injection](../sources/newsletters/gray-swan-ai-security-2026-06.md)
- [Effective Feedback Compute and harness profiles](../sources/newsletters/effective-feedback-compute-harness-2026-05.md)
- [Code as Agent Harness (arXiv:2605.18747)](../sources/articles/code-as-agent-harness-paper.md)
- [5 Trends That Defined AI Engineering at World's Fair 2026 — Latent Space](../sources/newsletters/aiewf-2026-five-trends-latentspace.md)
- [AINews — Zawinski's Law of MultiAgents](../sources/newsletters/zawinskis-law-multiagents-2026-08-08.md)
- [React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue](../sources/newsletters/flue-2-react-for-agents-2026-08-15.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
- [Prime Intellect — Introducing Prime Agent](../sources/tweets/primeintellect-prime-agent-2026-08-05.md)
