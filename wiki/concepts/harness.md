---
title: Harness (agent)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-06-17
sources: [agentic-thinking-lin, langchain-better-harness, openai-agents-sdk-evolution, notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, claude-code-leak-architecture, harness-engineering-early-april, skills-and-plugin-packaging-late-march, harness-engineering-march, harness-debate-march, shopify-latent-space-april-2026, ainews-2026-04-22, thecode-april-22-2026, agent-infrastructure-harness-2026-05-01, mattpocock-dictionary-of-ai-coding, model-harness-fit-2026-05-13, shopify-claude-code-bessemer-2026-05, gas-city-software-factory-2026-05, cloudflare-glasswing-2026-05, loopcraft-june-2026]
---

# Harness (agent)

The scaffolding that wraps an AI model and turns it into an agent capable of acting in the world. A harness defines *what* the model can do (tools, APIs, memory), *how* it reasons and plans (system prompt, instructions, routing logic), and *what environment* it operates in (browser, terminal, code sandbox, external services).

The analogy to model training is explicit in the field: just as training data shapes a model, the harness shapes an agent's behavior. As [LangChain's Better-Harness](../sources/articles/langchain-better-harness.md) frames it: `harness + evals + harness engineering → better agent` mirrors `model + training data + gradient descent → better model`.

## What a harness includes

- **System prompt & instructions** — behavioral constraints, task framing, output format rules
- **Tool suite** — which tools the model can call, their descriptions, when to use them
- **Orchestration logic** — how the agent loops, when it escalates, how sub-agents are coordinated
- **Execution environment** — browser, terminal, code sandbox, API layers, memory systems
- **Storage / compute boundary** — many practical agent stacks now separate durable shared context (repos, filesystems, knowledge stores) from isolated execution sandboxes so multiple agents can collaborate without sharing one unsafe runtime
- **Evaluation layer** — evals and traces that measure whether the agent behaves as intended; see [Agent evals](agent-evals.md) for the taxonomy of eval categories and the trajectory-vs-result distinction
- **Context-shaping layer** — practical systems increasingly treat repo state, recent edits, local instructions, and memory retrieval policy as part of the harness boundary, not as incidental prompt stuffing
- **Reusable operating modules** — skills, hook scripts, slash commands, and plugin bundles increasingly act as composable pieces of the harness, not just ad hoc project artifacts
- **Deployment manifest and access controls** — production harnesses increasingly package sandboxing, auth, RBAC (Role-Based Access Control — the rules that define which users and agents have permission to perform which operations), credential management, and frontend configuration into deployable artifacts. LangChain's DeepAgents expresses this as a `deepagents.toml` manifest; Agent Collabs uses Hugging Face dataset buckets (shared cloud storage) and Spaces (hosted isolated execution environments) to let heterogeneous agents collaborate through a common storage layer without sharing one mutable runtime.

## Why it matters

In the reasoning era, the competitive edge was in model training — better RL, stronger feedback signals. In the agentic era, as [Junyang Lin argues](../sources/articles/agentic-thinking-lin.md), the edge is in the harness: environment quality, prompt precision, tool design, and the ability to iterate on behavior without retraining the model. Harness engineering is increasingly treated as a first-class discipline.

OpenAI's April 15, 2026 Agents SDK post gives a concrete vendor example of this broader definition: the harness includes configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP, skills, AGENTS.md, shell, and `apply_patch`. OpenAI explicitly argues the harness should stay separate from compute so credentials remain outside execution sandboxes and runs can survive sandbox failure via snapshotting and rehydration.

The March 5, 2026 "Is Harness Engineering real?" debate sharpened the field's core argument. The "big model" side claims stronger reasoning models should collapse large amounts of scaffolding; the "big harness" side argues production advantage still comes from context packaging, tools, loop design, evaluation, and workflow engineering. The useful takeaway is not that one side fully wins, but that the harness has become legible enough to be a first-class competitive surface.

Late-March sources add a more distribution-oriented layer to this idea: teams do not only want a good harness inside one project. They want reusable packaging for the fuzzy operating judgment that makes the harness good in the first place. That is why plugin marketplaces, skills folders, and installable bundles keep surfacing across coding-agent ecosystems.

In practice, a harness is not only the loop logic. Recent source material reinforces that stable context packaging matters just as much: the folder, local instructions, reusable skills, and accumulated project memory often determine whether the same base model behaves like a specialist or a generic assistant.

## What good harness engineering looks like

- **Ambiguity gates** stop the agent to ask for clarification at forks where guessing wrong is expensive, instead of turning every step into a confirmation dialog.
- **Scoped context** gives each sub-agent only the files, tools, and instructions it needs, which reduces context bleed and instruction collisions.
- **Failure-metadata replanning** treats errors as structured input to a new plan, rather than blindly retrying the same approach with slightly different wording.
- **Eval-driven simplification** keeps the harness as simple as possible while it still passes the target evals; cleaner interfaces and stronger verification often beat more elaborate scaffolding.
- **Layered memory** keeps durable knowledge, topic files, and live-session context separate instead of forcing everything into one rolling transcript.
- **Repo-state awareness** gives the agent current branch, recent commits, and file-level state so it acts on the real workspace instead of a stale abstract summary.
- **Permission boundaries** stay explicit. Good harnesses make it legible when the agent is allowed to act, when it must ask, and where risky execution is isolated.
- **Cache-efficient subagent parallelism** lets worker agents inherit enough shared context to be useful without rebuilding the full setup cost every time.
- **Skills as the reusable abstraction** let teams share operating judgment as modules instead of only sharing code snippets or prompts.
- **Hook-based reliability plumbing** invokes the right capability at the right moment instead of hoping the model notices a textual instruction.
- **Externalized knowledge layers** help the harness retrieve the right context without dumping everything into the prompt.
- **Robust loop primitives** give agents a clean way to keep going, pause, rewind, and resume without relying on awkward prompt hacks like reissuing "loop forever" in a brittle session.
- **Decoupled shared context with isolated execution** lets teams of agents coordinate through the same source of truth while keeping actual runs sandboxed and failure-contained.
- **Critique-loop orchestration** over flat parallel dispatch: a generator agent + a separate critic model reviewing the output + the generator redoing the work based on the critique produces higher-quality output than equivalent compute spent on parallel independent agents. Observed by Shopify at scale; slower but more reliable for tasks with clear correctness signals.
- **CI/CD as part of the harness boundary**: at sufficient agent throughput (e.g. 30% MoM PR growth), deployment and verification infrastructure becomes the bottleneck. Harness design must account for the downstream pipeline, not only the generation loop.
- **Agent-friendly CLI design.** Tools built for human interactive use break agent pipelines: interactive prompts stall agents, undocumented flags require inference, and missing non-interactive modes force workarounds. Agent-facing CLI tools should be non-interactive by default, expose all behaviors through explicit flags, and document internal conventions. This applies equally to the tools the agent calls and to the CLIs agents themselves expose.
- **DSPy 3.2** (April 2026) as a harness engineering toolchain: adds Reinforced Language Model (RLM) improvements, optimizer chaining, and LiteLLM decoupling. Relevant for teams iterating on harness prompts and orchestration logic using programmatic optimization.
- **Model-harness fit.** Coding-agent performance depends on how well the surrounding harness matches the model's preferred edit format, action space, tool-call style, and failure recovery patterns. A strong model can underperform in a mismatched harness.
- **LLM proxy as the fleet management layer.** At org scale (Shopify, 23K engineers), routing all AI coding-tool traffic through a centralized LLM proxy creates a control plane for cost, model choice, and policy enforcement without requiring per-tool reconfiguration. This positions the proxy as part of the enterprise harness boundary — above the individual tool harness, below the model.
- **Dark/light factory split.** Separate the parts of your workflow where humans and agents collaborate (planning, design, review) — the "light" side — from the parts where agents execute clearly defined work on their own in the background — the "dark" side. As trust in agent output increases, more work can migrate from light to dark. Gas City runs ~100 agents in the dark while the human interaction surface stays small and visible.
- **One pet, many cattle (mayor + polecats).** One persistent named supervisor agent ("mayor") you interact with directly coordinates anonymous disposable worker agents ("polecats") that each execute one job and shut down. Instead of managing 100 agents individually, you manage one conversation while the mayor routes work. Workers stay context-clean because they start fresh per task.
- **Multi-model parallel code review.** Submitting the same code to Claude, Codex, and Kimi simultaneously in parallel finds different bugs than running one model three times. Three different models with different training distributions catch issues each would miss alone. Higher signal per review cycle at the cost of higher parallel token spend.
- **Narrow-scope parallel agents outperform exhaustive single agents in high-coverage tasks.** Cloudflare's Project Glasswing harness (8 stages, ~50 concurrent Mythos Preview agents) demonstrates this at security-research scale: each agent has one tightly scoped attack class + one target area; an independent adversarial agent validates but cannot emit new findings; root-cause deduplication collapses variant findings. The Trace stage further splits "is this buggy?" from "can an attacker reach this bug?" — a clean instance of decomposing a compound question into two separately answerable ones.
- **Model neutrality by design.** Build your harness so the underlying model is a configurable parameter, not a hardcoded dependency. Routing, context packaging, and evaluation should live in the harness layer — not in model-specific prompt tricks. This became a risk management requirement (not just an engineering preference) after the Fable 5 export-control ban removed access to the leading frontier model for all customers overnight. The LangSmith Engine (a fine-tuned production-trace judge, 10-100× cheaper than frontier models) demonstrates that the evaluation layer can also be decoupled from frontier access.

## Harness vs model

A well-engineered harness can compensate for a weaker model. A poor harness can cripple a strong one. This is why [Better-Harness](../sources/articles/langchain-better-harness.md) and similar systems focus on *harness hill-climbing* — iteratively improving the harness using evals as a signal, separate from any model update.

Practitioners are increasingly using a consistent vocabulary for these parts: **model** (the neural network weights that process each request — no memory between calls, no built-in ability to act independently), **harness** (the scaffold that adds tools, memory, and loop logic), **agent** (the user-facing system combining both), **context** (what the agent has available right now), **session** (one bounded run until reset or handoff), and **environment** (what the agent can actually act on). Teams that adopt this language spend less time misattributing problems to the wrong layer. See [AI coding vocabulary](../training/ai-coding-vocabulary.md).

## Harness vs folder-level context

- **Folder-level context** packages what the agent knows: codebase, instructions, skills, conventions, and durable local memory
- **Harness** packages how the agent operates: loop logic, tools, routing, retries, and evaluation

The two are related but not identical. Many real-world "agent" improvements actually come from better context packaging rather than fancier orchestration.

## Caveats

- The term has no single agreed definition across the field. Some sources use it narrowly (just the prompt + tool config); others include the full execution environment and orchestration layer.
- This page reflects the broader definition, consistent with [Lin's essay](../sources/articles/agentic-thinking-lin.md) and [LangChain's Better-Harness](../sources/articles/langchain-better-harness.md) framing.
- Some practitioners now implicitly split "harness" from "folder-level context." The distinction is useful operationally even if the vocabulary is not yet standardized.

## Related

- [Agent evals](agent-evals.md) — taxonomy of agent evaluation categories and why trajectory quality matters alongside final results
- [Agent improvement loop](agent-improvement-loop.md) — the loop for improving a harness systematically via traces, evals, and targeted changes
- [Skillify — Agent Reliability Pattern](../workflows/skillify-agent-reliability.md) — pattern for encoding agent failures as permanent tested skills; "thin harness / fat skills" architecture

## Sources

- [From 'Reasoning' Thinking to 'Agentic' Thinking by Junyang Lin](../sources/articles/agentic-thinking-lin.md)
- ["Better Harness: A Recipe for Harness Hill-Climbing with Evals" — LangChain](../sources/articles/langchain-better-harness.md)
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
