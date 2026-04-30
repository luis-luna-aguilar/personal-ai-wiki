---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-24
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents, agentic-thinking-lin, curiosity-driven-imagination, openai-agents-sdk-evolution, ainews-2026-04-21, ainews-2026-04-22, claude-cowork-launch, every-managed-agents-vibe-check, claude-design-launch, orca-homepage, anthropic-platform-expansion-april-2026, coding-agent-control-planes, claude-productivity-surfaces, open-agent-orchestration-late-march, proof-agent-native-documents, cursor-cloud-agents-march, cursor-cloud-agents-february, google-adk, openai-deep-research, gemini-deep-research-max, futurehouse-homepage, uipath-maestro-introduction, anthropic-mcp, google-a2a, legacy-ai-tools-roadmap-xlsx, microsoft-foundry-agents-2026, google-cloud-next-2026, superhuman-2026-04-23, awsai-cowork-bedrock-2026-04-23, microsoft-copilot-agent-mode-office, claude-managed-agents-memory, agentic-devops-deep-research]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

_Coding agents (Claude Code, Codex, Cursor) are tracked in [Coding](../history/state-of/coding.md)._

## Subcategories

### Agent orchestration

Platforms, surfaces, and patterns for running, supervising, or routing AI agents — spanning hosted runtimes, human-supervision UIs, and multi-model coordination within a single agentic task.

- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; desktop knowledge-work agent with Live Artifacts; VM-backed local-first execution; scheduled and persistent tasks *(as of 2026-04-21)*
- [Codex](../tools/codex.md) (Workspace Agents) — OpenAI; Codex-powered shareable team agents in Slack and ChatGPT; scheduled/background execution; Business/Enterprise/Edu/Teachers rollout *(as of 2026-04-23)*
- [Orca](../tools/orca.md) — open-source desktop surface for supervising multiple coding agents across isolated worktrees, with live status, diff review, and CI visibility *(as of 2026-04-21)*
- [Claude Managed Agents](../tools/claude-managed-agents.md) — Anthropic's hosted runtime; separates session, harness, sandbox, and now file-backed built-in memory with shared stores and auditability *(as of 2026-04-24)*
- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; agentic default mode inside Word, Excel, and PowerPoint; takes multi-step native actions in documents, worksheets, and presentations while users stay in control *(as of 2026-04-22)*
- [Microsoft Foundry Hosted Agents](../tools/microsoft-foundry-agents.md) — Microsoft; hosted runtime with per-session VM isolation, persistent filesystems, Entra Agent ID governance, MCP Toolbox, and multi-framework support *(as of 2026-04-23)*
- [OpenAI Agents SDK](../tools/openai-agents-sdk.md) — model-native harness with native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as of 2026-04-15)*
- [UiPath Maestro](../tools/uipath-maestro.md) — enterprise orchestration for agents, robots, and people; stronger fit for operational process flows than pure research workloads *(as of 2026-04-22)*
- [Advisor strategy](../workflows/advisor-strategy.md) — small executor (Sonnet/Haiku) drives the loop; escalates to Opus only when stuck; +2.7% SWE-bench Multilingual, −11.9% cost vs Sonnet alone *(as of 2026-04-09)*

### Agent frameworks

SDKs and development kits for building custom agents with tools, multi-agent patterns, and runtime scaffolding.

- [Google ADK](../tools/google-adk.md) — Google; open-source ADK now positioned as the developer layer inside Gemini Enterprise Agent Platform; Agent Studio adds a low-code wrapper, and Model Garden expands the surrounding stack to 200+ models *(as of 2026-04-23)*
- [Hermes Agent](../tools/hermes-agent.md) — NousResearch; open-source; four-layer memory, stateless sub-agent parallelism, LLM-driven replanning; 100K+ GitHub stars; 118 bundled skills *(as of 2026-04-22)*

### Deep research tools

Longer-horizon research agents that plan, search, read, synthesize, and return multi-step research outputs rather than answer in one pass. See [Deep Research (concept)](../concepts/deep-research.md) for the category concept.

- [OpenAI Deep Research](../tools/openai-deep-research.md) — OpenAI's productized deep research agent; available via ChatGPT and API *(as of 2026-04-22)*
- [Gemini Deep Research](../tools/gemini-deep-research.md) — Gemini Deep Research and Deep Research Max; most fully benchmarked public implementation (93.3% DeepSearchQA, 85.9% BrowseComp on Max tier); MCP support for internal data *(as of 2026-04-22)*

### Agentic DevOps

Agent-compatible infrastructure tools and control planes for provisioning, diagnosing, operating, and verifying live systems through repeatable, auditable interfaces.

- [Stripe CLI](../tools/stripe-cli.md) — early provisioning/control-plane example: provision services across providers, sync credentials back to the environment, and manage upgrades or billing from a CLI designed for humans or agents *(as of 2026-04-09)*
- [Kagent](../tools/kagent.md) — Kubernetes-native agent runtime / governance layer with MCP tool servers, tracing, and human-in-the-loop control *(as of 2026-04-24)*
- [K8sGPT](../tools/k8sgpt.md) — Kubernetes diagnosis and triage surface that turns cluster problems into agent-usable plain-English context *(as of 2026-04-24)*
- [Skyflo](../tools/skyflo.md) — approval-gated AI control layer for Kubernetes and CI/CD; strongest current example of explicit mutate-with-approval ops design *(as of 2026-04-24)*
- [Checkly](../tools/checkly.md) — outside-in post-deploy verification via synthetic monitoring and Playwright-based checks *(as of 2026-04-24)*

### Agent-native documents

Document surfaces built for humans and agents to collaborate inside the same working artifact, with revision, provenance, and comments happening in-place instead of around pasted AI output.

- [Proof](../tools/proof.md) — Every's web document editor is the clearest current example of the "agent-native document" thesis: plans, memos, and working docs are treated as shared human/AI artifacts with provenance, comments, and tracked edits built into the document itself *(as of 2026-03-15)*

### Autonomous research agents

Agents that close the full research loop end-to-end — reading literature, collecting data, running experiments, evaluating results, and iterating — with minimal human steering between steps.

- [HF ml-intern](../tools/hf-ml-intern.md) — Hugging Face; open-source ML post-training research loop agent; reads papers, collects datasets, launches training jobs, evaluates, and iterates; GPQA 10% → 32% in <10 hours on Qwen3-1.7B *(as of 2026-04-22)*

### Science agent platforms

Platforms built to support literature-driven or discovery-oriented scientific work, without necessarily closing the full autonomous experiment loop end to end.

- [FutureHouse](../tools/futurehouse.md) — science-agent platform aimed at research and discovery workflows, distinct from generic chat assistants with science demos *(as of 2026-04-22)*

## Recent changes

- [2026-04-24] Broadened `agentic-devops` from provisioning-only CLI workflows toward a fuller infrastructure-operations stack: diagnosis, approval-gated mutation, and post-deploy verification
- [2026-04-24] Claude Managed Agents added built-in file-backed memory with shared stores, audit logs, and rollback controls; Anthropic's hosted-runtime story is becoming a more opinionated durable-agent platform
- [2026-04-22] Microsoft Copilot's agentic mode in Word, Excel, and PowerPoint reached GA/default status; Microsoft is now pushing agent behavior directly into Office's core work canvas, not only hosted runtimes like Foundry
- [2026-04-23] Added OpenAI Workspace Agents under `Agent orchestration`; Codex-powered shareable team agents in Slack and ChatGPT land the same day as Google's enterprise agent-platform push
- [2026-04-23] Google Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; ADK now sits inside a fuller enterprise stack with Agent Studio, Workspace Intelligence GA, and Knowledge Catalog
- [2026-04-23] Added [Microsoft Foundry Hosted Agents](../tools/microsoft-foundry-agents.md) under `Agent orchestration`; Microsoft is now a serious enterprise hosted-agent platform contender with VM-per-session isolation, persistent resume, and a fuller governance stack
- [2026-04-23] Added [Skillify — Agent Reliability Pattern](../workflows/skillify-agent-reliability.md); Garry Tan's 10-step "thin harness / fat skills" agent reliability pattern — most detailed published treatment of agent skill architecture and failure prevention
- [2026-04-22] Added `Agent frameworks` with [Google ADK](../tools/google-adk.md); active framework layer should be represented directly instead of forced into orchestration-only categories; [Hermes Agent](../tools/hermes-agent.md) reclassified here from agent-orchestration
- [2026-04-22] Added `Deep research tools`; restructured as concept ([Deep Research (concept)](../concepts/deep-research.md)) + individual tool pages ([OpenAI Deep Research](../tools/openai-deep-research.md), [Gemini Deep Research](../tools/gemini-deep-research.md))
- [2026-04-22] Added `Science agent platforms` with [FutureHouse](../tools/futurehouse.md); science-agent infrastructure deserves a slot between orchestration and full autonomous research
- [2026-04-22] Added [UiPath Maestro](../tools/uipath-maestro.md) under `Agent orchestration`; enterprise orchestration for agents and robots broadens the category beyond hosted agent runtimes
- [2026-04-22] Added `Autonomous research agents` subcategory; [HF ml-intern](../tools/hf-ml-intern.md) is the first publicly verified agent to close the full ML post-training loop end-to-end
- [2026-04-22] Google Deep Research Max scores (93.3% DeepSearchQA) and HF ml-intern autonomous loop mark the emergence of a distinct "full-stack research agent" tier — see [Gemini](../tools/gemini.md) and [HF ml-intern](../tools/hf-ml-intern.md)
- [2026-04-22] Added `Agent-native documents` to capture document surfaces built for shared human/agent drafting; [Proof](../tools/proof.md) is the first example
- [2026-04-21] Added [Orca](../tools/orca.md) under `Agent orchestration`; worktree-first desktop supervision layer for Claude Code, Codex, and similar agents
- [2026-03-31] Backfilled late-March signal: open-agent stacks were already converging on CLI-first execution, worktree coordination, and packaged reusable agents before the April orchestration/control-plane wave became clearer
- [2026-04-21] Added earlier Anthropic productivity-surface precursor: Claude for Word beta helps explain Cowork / Live Artifacts as expansion of an existing direction
- [2026-04-15] Anthropic's Managed Agents now reads as part of a broader platform cluster: hosted runtime, custom agents, and Claude Code long-running monitor/loop patterns
- [2026-04-14] Cursor 3.1 added tiled multi-agent supervision and stronger control-plane UX, reinforcing the shift from AI-enhanced IDEs toward agent workspaces
