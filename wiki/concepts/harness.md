---
title: Harness (agent)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-07-08
sources: [agentic-thinking-lin, langchain-better-harness, openai-agents-sdk-evolution, notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, claude-code-leak-architecture, harness-engineering-early-april, skills-and-plugin-packaging-late-march, harness-engineering-march, harness-debate-march, shopify-latent-space-april-2026, ainews-2026-04-22, thecode-april-22-2026, agent-infrastructure-harness-2026-05-01, mattpocock-dictionary-of-ai-coding, model-harness-fit-2026-05-13, shopify-claude-code-bessemer-2026-05, gas-city-software-factory-2026-05, cloudflare-glasswing-2026-05, loopcraft-june-2026, rl-harness-quality-june-2026, aiewf-loops-debate-2026-07-03, autoresearch-agent-recipes-2026-07, claude-tag-slack-agent-2026-06, gemini-managed-agents-2026-07, gray-swan-ai-security-2026-06, effective-feedback-compute-harness-2026-05, claude-managed-agents-updates-2026-05, code-as-agent-harness-paper]
---

# Harness (agent)

The scaffolding that wraps an AI model and turns it into an agent capable of acting in the world. A harness defines *what* the model can do (tools, APIs, memory), *how* it reasons and plans (system prompt, instructions, routing logic), and *what environment* it operates in (browser, terminal, code sandbox, external services).

The analogy to model training is explicit in the field: just as training data shapes a model, the harness shapes an agent's behavior. As [LangChain's Better-Harness](../sources/tweets/langchain-better-harness.md) frames it: `harness + evals + harness engineering → better agent` mirrors `model + training data + gradient descent → better model`.

## What a harness includes

- **System prompt & instructions** — behavioral constraints, task framing, output format rules
- **Tool suite** — which tools the model can call, their descriptions, when to use them
- **Orchestration logic** — how the agent loops, when it escalates, how sub-agents are coordinated
- **Execution environment** — browser, terminal, code sandbox, API layers, memory systems
- **Storage / compute boundary** — many practical agent stacks now separate durable shared context (repos, filesystems, knowledge stores) from isolated execution sandboxes so multiple agents can collaborate without sharing one unsafe runtime
- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended; see [Agent evals](agent-evals.md) for the taxonomy of eval categories and the trajectory-vs-result distinction
- **Context-shaping layer** — practical systems increasingly treat repo state, recent edits, local instructions, and memory retrieval policy as part of the harness boundary, not as incidental prompt stuffing
- **Reusable operating modules** — skills, hook scripts, slash commands, plugin bundles, and agent recipes increasingly act as composable pieces of the harness, not just ad hoc project artifacts. An agent recipe packages the harness, model choices, evals, judges, human expertise, failure history, and signal-processing logic needed to reproduce an agent workflow.
- **Deployment manifest and access controls** — production harnesses increasingly package sandboxing, auth, RBAC (Role-Based Access Control — the rules that define which users and agents have permission to perform which operations), credential management, and frontend configuration into deployable artifacts. LangChain's DeepAgents expresses this as a `deepagents.toml` manifest; Agent Collabs uses Hugging Face dataset buckets (shared cloud storage) and Spaces (hosted isolated execution environments) to let heterogeneous agents collaborate through a common storage layer without sharing one mutable runtime.
- **Control layer** — permissions, approvals, cost ceilings, stop conditions, recovery, and review routing around an agent loop. The 2026 AI Engineer Survey reported high agent adoption but primitive safeguards, making the control layer part of harness design rather than a product afterthought.
- **Live-run recovery** — checkpointing, rollback, and forking of agent state so a failed trajectory can be repaired without discarding all context.

## Why it matters

In the reasoning era, the competitive edge was in model training — better RL, stronger feedback signals. In the agentic era, as [Junyang Lin argues](../sources/articles/agentic-thinking-lin.md), the edge is in the harness: environment quality, prompt precision, tool design, and the ability to iterate on behavior without retraining the model. Harness engineering is increasingly treated as a first-class discipline.

OpenAI's April 15, 2026 Agents SDK post gives a concrete vendor example of this broader definition: the harness includes configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP, skills, AGENTS.md, shell, and `apply_patch`. OpenAI explicitly argues the harness should stay separate from compute so credentials remain outside execution sandboxes and runs can survive sandbox failure via snapshotting and rehydration.

The March 5, 2026 "Is Harness Engineering real?" debate sharpened the field's core argument. The "big model" side claims stronger reasoning models should collapse large amounts of scaffolding; the "big harness" side argues production advantage still comes from context packaging, tools, loop design, evaluation, and workflow engineering. The useful takeaway is not that one side fully wins, but that the harness has become legible enough to be a first-class competitive surface.

Late-March sources add a more distribution-oriented layer to this idea: teams do not only want a good harness inside one project. They want reusable packaging for the fuzzy operating judgment that makes the harness good in the first place. That is why plugin marketplaces, skills folders, and installable bundles keep surfacing across coding-agent ecosystems.

In practice, a harness is not only the loop logic. Recent source material reinforces that stable context packaging matters just as much: the folder, local instructions, reusable skills, and accumulated project memory often determine whether the same base model behaves like a specialist or a generic assistant.

## What good harness engineering looks like

Most of the field's accumulated patterns for harness design — ambiguity gates, scoped context, failure-aware replanning, eval-driven simplification, skills as the reusable abstraction, hook-based reliability plumbing, externalized knowledge layers, robust loop primitives, decoupled shared context with isolated execution, the dark/light factory split, and the mayor-and-polecats worker topology — are cataloged with fuller detail on [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md). What follows are the points specific to harness *architecture* rather than orchestration *pattern*:

- **Layered memory** keeps durable knowledge, topic files, and live-session context separate instead of forcing everything into one rolling transcript.
- **Repo-state awareness** gives the agent current branch, recent commits, and file-level state so it acts on the real workspace instead of a stale abstract summary.
- **Permission boundaries** stay explicit. Good harnesses make it legible when the agent is allowed to act, when it must ask, and where risky execution is isolated.
- **Cache-efficient subagent parallelism** lets worker agents inherit enough shared context to be useful without rebuilding the full setup cost every time.
- **Critique-loop orchestration** over flat parallel dispatch: a generator agent + a separate critic model reviewing the output + the generator redoing the work based on the critique produces higher-quality output than equivalent compute spent on parallel independent agents. Observed by Shopify at scale; slower but more reliable for tasks with clear correctness signals.
- **CI/CD as part of the harness boundary**: at sufficient agent throughput (e.g. 30% MoM PR growth), deployment and verification infrastructure becomes the bottleneck. Harness design must account for the downstream pipeline, not only the generation loop.
- **Agent-friendly CLI design.** Tools built for human interactive use break agent pipelines: interactive prompts stall agents, undocumented flags require inference, and missing non-interactive modes force workarounds. Agent-facing CLI tools should be non-interactive by default, expose all behaviors through explicit flags, and document internal conventions. This applies equally to the tools the agent calls and to the CLIs agents themselves expose.
- **DSPy 3.2** (April 2026) as a harness engineering toolchain: adds Reinforced Language Model (RLM) improvements, optimizer chaining, and LiteLLM decoupling. Relevant for teams iterating on harness prompts and orchestration logic using programmatic optimization.
- **Model-harness fit.** Coding-agent performance depends on how well the surrounding harness matches the model's preferred edit format, action space, tool-call style, and failure recovery patterns. A strong model can underperform in a mismatched harness.
- **Measure effective feedback, not only activity.** Raw token counts, tool counts, and trace length are weak proxies for agent success. AINews coverage of Effective Feedback Compute argues that the useful signal is whether the harness gives the model actionable feedback that improves the next step.
- **Model-specific harness profiles.** LangChain Deep Agents coverage suggests that Qwen, Kimi, DeepSeek, and frontier closed models can require different prompts, tools, and memory layouts. A cheaper model can become viable when the harness matches its operating style.
- **LLM proxy as the fleet management layer.** At org scale (Shopify, 23K engineers), routing all AI coding-tool traffic through a centralized LLM proxy creates a control plane for cost, model choice, and policy enforcement without requiring per-tool reconfiguration. This positions the proxy as part of the enterprise harness boundary — above the individual tool harness, below the model.
- **Multi-model parallel code review.** Submitting the same code to Claude, Codex, and Kimi simultaneously in parallel finds different bugs than running one model three times. Three different models with different training distributions catch issues each would miss alone. Higher signal per review cycle at the cost of higher parallel token spend.
- **Model neutrality by design.** Build your harness so the underlying model is a configurable parameter, not a hardcoded dependency — routing, context packaging, and evaluation should live in the harness layer, not in model-specific prompt tricks. LangChain's LangSmith Engine, which automatically consumes production traces, clusters failures, identifies likely code issues, and proposes fixes and evals, demonstrates that the evaluation layer can also be decoupled from frontier access. See [Agent Labs vs Model Labs](agent-labs-vs-model-labs.md) for the competitive-moat argument this connects to.
- **Org-embedded identity and permissioning.** Slack-native and team-channel agents need a legible identity, scoped access to channels/tools/data, audit trails for actions, and memory boundaries that match how the organization actually partitions work. Without that, the harness becomes an organizational risk surface: unclear accountability, prompt-injection exposure, budget opacity, and channel noise.
- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution. Google adding these to the Gemini API is another sign that "harness" is becoming product infrastructure, not only application code. Anthropic's Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview) in May 2026: the agent loop that handles orchestration, context management, and error recovery stays on Anthropic's infrastructure, while tool execution and private MCP connectivity run on customer-controlled infrastructure or a supported sandbox provider (Cloudflare, Daytona, Modal, Vercel).
- **Security boundary as harness boundary.** Tool-using agents are not only productivity systems; they are software components that may read untrusted content, hold private context, and take actions. A production harness must define identity, permissions, data exfiltration boundaries, guardrails, red-team tests, and audit trails as part of the agent architecture — see [Prompt injection](prompt-injection.md) for the concrete attack pattern this defends against.
- **Code as the operational substrate, not just output.** A May 2026 survey ("Code as Agent Harness," arXiv:2605.18747) frames code as the shared medium connecting agent reasoning, acting, and environment modeling — not merely the artifact an agent produces. It organizes harness design around three layers: the interface where code links reasoning/action/environment; harness mechanisms (planning, memory, tool use, feedback-driven control); and scaling from single-agent to multi-agent settings, where shared code artifacts support coordination, review, and verification.

## Harness vs model

A well-engineered harness can compensate for a weaker model. A poor harness can cripple a strong one. This is why [Better-Harness](../sources/tweets/langchain-better-harness.md) and similar systems focus on *harness hill-climbing* — iteratively improving the harness using evals as a signal, separate from any model update.

The practical model/harness split is now measurable: the same model can underperform in a mismatched product surface, while a cheaper model can approach frontier behavior in a tuned harness. Treat benchmark results as model + harness + environment, not model-only.

Practitioners are increasingly using a consistent vocabulary for these parts: **model** (the neural network weights that process each request — no memory between calls, no built-in ability to act independently), **harness** (the scaffold that adds tools, memory, and loop logic), **agent** (the user-facing system combining both), **context** (what the agent has available right now), **session** (one bounded run until reset or handoff), and **environment** (what the agent can actually act on). Teams that adopt this language spend less time misattributing problems to the wrong layer. See [AI coding vocabulary](../training/ai-coding-vocabulary.md).

## Harness vs folder-level context

- **Folder-level context** packages what the agent knows: codebase, instructions, skills, conventions, and durable local memory
- **Harness** packages how the agent operates: loop logic, tools, routing, retries, and evaluation

The two are related but not identical. Many real-world "agent" improvements actually come from better context packaging rather than fancier orchestration.

## RL harness quality

When a harness is used as an RL training environment, it is not only helping the model act — it is teaching the model what behavior gets rewarded. The model tries tasks inside the harness, receives success/failure signals, and updates based on those signals. If the environment is wrong, stale, or easy to game, the model learns the wrong lesson.

Auriel W (Google Gemini RL team) published a practical taxonomy (June 2026). The guiding rule: **if your environment failure rate is above 5%, you have a harness problem, not a model problem.** Bad harnesses compound in the wrong direction — every polluted episode corrupts what the model learns next.

Eight common failure modes, with examples:

- **Stale cache.** The environment serves cached state from a different run, so the model acts on data that doesn't reflect its previous actions (example: BDR agent reads cached CRM data from prior customer session, never seeing the state it just updated).
- **Reward hacking.** Sparse positive reward creates a gradient toward edge-case exploitation rather than real task completion (example: coding agent hardcodes expected test outputs rather than implementing actual logic).
- **False resolution.** The task appears completed when it isn't (example: support agent closes a ticket after sending a message, before checking whether the customer's problem was solved).
- **Silent timeout defaults.** The agent hangs indefinitely with no timeout, no signal, and no negative reward for stalling.
- **Non-deterministic state resets.** Each episode starts from a slightly different state, making it impossible to compare episode quality or diagnose behavior changes.
- **Reward rounding / clipping.** Small but real improvements become invisible because the reward function truncates at the wrong precision.
- **Mock data mismatch.** The training environment's mock data diverges from production data distributions, so the model learns patterns that don't transfer.
- **Action space drift.** Valid actions change between training and evaluation (new API fields, renamed endpoints, updated schemas) without the harness being updated to match.

Treating the training harness like production code — with tests, versioning, and monitoring for failure rate — is the main mitigation. See [Agent improvement loop](agent-improvement-loop.md) for the broader iterate-on-harness pattern.

## Caveats

- The term has no single agreed definition across the field. Some sources use it narrowly (just the prompt + tool config); others include the full execution environment and orchestration layer.
- This page reflects the broader definition, consistent with [Lin's essay](../sources/articles/agentic-thinking-lin.md) and [LangChain's Better-Harness](../sources/tweets/langchain-better-harness.md) framing.
- Some practitioners now implicitly split "harness" from "folder-level context." The distinction is useful operationally even if the vocabulary is not yet standardized.

## Recent changes

- [2026-07-08] Gemini API managed agents add hosted harness primitives: MCP support, background execution, custom function calling, credential refresh, and stateful agent interactions.
- [2026-07-03] Added control-layer framing from AI Engineer World Fair: permissions, cost ceilings, recovery, and review routing are part of the harness boundary.
- [2026-07-01] Added agent recipes as a harness packaging pattern: model choices, evals, judges, human expertise, failure history, and signal processing bundled with the workflow.
- [2026-06-24] Claude Tag coverage adds org-embedded agent identity, permission scoping, and Slack-channel memory boundaries as harness concerns.
- [2026-06-22] Gray Swan security coverage adds prompt injection, exfiltration, identity, permissions, and automated red teaming as harness-boundary concerns for tool-using agents.
- [2026-06-05] Added RL harness quality section: 8 failure modes taxonomy from Auriel W (Google Gemini RL team); "5% failure rate = harness problem, not model problem"
- [2026-05-30] Added Effective Feedback Compute and model-specific harness profiles as harness-quality signals beyond token/tool counts.
- [2026-05-20] Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview), extending the harness security boundary so tool execution and private MCP connectivity can run on customer infrastructure while Anthropic keeps the orchestration loop.
- [2026-05-18] "Code as Agent Harness" survey (arXiv:2605.18747) frames code as the operational substrate for agent reasoning, planning, memory, tool use, and multi-agent coordination.

## Related

- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — the pattern catalog for agent loop design, escalation, and multi-agent topology; this page covers harness architecture, that page covers reusable operating patterns
- [Agent evals](agent-evals.md) — taxonomy of agent evaluation categories and why trajectory quality matters alongside final results
- [Agent improvement loop](agent-improvement-loop.md) — the loop for improving a harness systematically via traces, evals, and targeted changes
- [Skillify — Agent Reliability Pattern](../workflows/skillify-agent-reliability.md) — pattern for encoding agent failures as permanent tested skills; "thin harness / fat skills" architecture
- [Prompt injection](prompt-injection.md) — the concrete security attack the harness security boundary defends against

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
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [The Code newsletter — 2026-04-22 (Cursor/SpaceX, Claude Code recap, CLI design)](../sources/newsletters/thecode-april-22-2026.md)
- [Agent infrastructure, harness engineering, and collaborative agent systems](../sources/newsletters/agent-infrastructure-harness-2026-05-01.md)
- [Matt Pocock — Dictionary of AI Coding](../sources/repos/mattpocock-dictionary-of-ai-coding.md)
- [Model-harness fit as coding-agent moat](../sources/newsletters/model-harness-fit-2026-05-13.md)
- [Shopify Claude Code fleet patterns — Bessemer conference synthesis](../sources/articles/shopify-claude-code-bessemer-2026-05.md)
- [Inside the 100-agent Software Factory — Gas City](../sources/newsletters/gas-city-software-factory-2026-05.md)
- [Project Glasswing: what Mythos showed us — Cloudflare](../sources/articles/cloudflare-glasswing-2026-05.md)
- [RL harness quality — Auriel W (Google Gemini team)](../sources/newsletters/rl-harness-quality-june-2026.md)
- [AIEWF Daily Dispatch - loops debate](../sources/newsletters/aiewf-loops-debate-2026-07-03.md)
- [Autoresearch and agent recipes](../sources/newsletters/autoresearch-agent-recipes-2026-07.md)
- [Claude Tag Slack-native agent launch](../sources/newsletters/claude-tag-slack-agent-2026-06.md)
- [Gemini managed agents in the API](../sources/newsletters/gemini-managed-agents-2026-07.md)
- [Gray Swan on AI-native security and prompt injection](../sources/newsletters/gray-swan-ai-security-2026-06.md)
- [Effective Feedback Compute and harness profiles](../sources/newsletters/effective-feedback-compute-harness-2026-05.md)
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [Code as Agent Harness (arXiv:2605.18747)](../sources/articles/code-as-agent-harness-paper.md)
