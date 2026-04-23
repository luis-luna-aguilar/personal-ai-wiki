---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-04-23
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents, agentic-thinking-lin, curiosity-driven-imagination, openai-agents-sdk-evolution, ainews-2026-04-21, ainews-2026-04-22, claude-cowork-launch, every-managed-agents-vibe-check, claude-design-launch, orca-homepage, anthropic-platform-expansion-april-2026, coding-agent-control-planes, claude-productivity-surfaces, open-agent-orchestration-late-march, proof-agent-native-documents, cursor-cloud-agents-march, cursor-cloud-agents-february, google-adk, openai-deep-research, gemini-deep-research-max, futurehouse-homepage, uipath-maestro-introduction, anthropic-mcp, google-a2a, legacy-ai-tools-roadmap-xlsx, microsoft-foundry-agents-2026, google-cloud-next-2026]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

_Coding agents (Claude Code, Codex, Cursor) are tracked in [[state-of/coding]]._

## Subcategories

### Agent orchestration

Platforms, surfaces, and patterns for running, supervising, or routing AI agents — spanning hosted runtimes, human-supervision UIs, and multi-model coordination within a single agentic task.

- [[tools/claude-cowork]] — Anthropic; desktop knowledge-work agent with Live Artifacts; VM-backed local-first execution; scheduled and persistent tasks *(as of 2026-04-21)*
- [[tools/cursor]] — cloud-agent supervision layer: agents run remotely, test their own work, return videos for human review *(as of 2026-03-06)*
- [[tools/orca]] — open-source desktop surface for supervising multiple coding agents across isolated worktrees, with live status, diff review, and CI visibility *(as of 2026-04-21)*
- [[tools/claude-managed-agents]] — Anthropic's hosted runtime; separates session, harness, and sandbox; platform backbone behind a broader Anthropic agent stack *(as of 2026-04-15)*
- [[tools/microsoft-foundry-agents]] — Microsoft; hosted runtime with per-session VM isolation, persistent filesystems, Entra Agent ID governance, MCP Toolbox, and multi-framework support *(as of 2026-04-23)*
- [[tools/openai-agents-sdk]] — model-native harness with native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as of 2026-04-15)*
- [[tools/uipath-maestro]] — enterprise orchestration for agents, robots, and people; stronger fit for operational process flows than pure research workloads *(as of 2026-04-22)*
- [[workflows/advisor-strategy]] — small executor (Sonnet/Haiku) drives the loop; escalates to Opus only when stuck; +2.7% SWE-bench Multilingual, −11.9% cost vs Sonnet alone *(as of 2026-04-09)*

### Agent frameworks

SDKs and development kits for building custom agents with tools, multi-agent patterns, and runtime scaffolding.

- [[tools/google-adk]] — Google; open-source ADK now positioned as the developer layer inside Gemini Enterprise Agent Platform; Agent Studio adds a low-code wrapper, and Model Garden expands the surrounding stack to 200+ models *(as of 2026-04-23)*
- [[tools/hermes-agent]] — NousResearch; open-source; four-layer memory, stateless sub-agent parallelism, LLM-driven replanning; 100K+ GitHub stars; 118 bundled skills *(as of 2026-04-22)*

### Deep research tools

Longer-horizon research agents that plan, search, read, synthesize, and return multi-step research outputs rather than answer in one pass. See [[concepts/deep-research]] for the category concept.

- [[tools/openai-deep-research]] — OpenAI's productized deep research agent; available via ChatGPT and API *(as of 2026-04-22)*
- [[tools/gemini-deep-research]] — Gemini Deep Research and Deep Research Max; most fully benchmarked public implementation (93.3% DeepSearchQA, 85.9% BrowseComp on Max tier); MCP support for internal data *(as of 2026-04-22)*

### Agentic DevOps

Agent-compatible tools that let a model provision external services and receive credentials through a repeatable CLI workflow instead of clicking through SaaS dashboards.

- [[tools/stripe-cli]] — Stripe explicitly pitches the CLI `projects` flow for "you or your agents": provision services across providers, sync credentials back to the environment, and manage upgrades or billing from the CLI *(as of 2026-04-09)*

### Agent-native documents

Document surfaces built for humans and agents to collaborate inside the same working artifact, with revision, provenance, and comments happening in-place instead of around pasted AI output.

- [[tools/proof]] — Every's web document editor is the clearest current example of the "agent-native document" thesis: plans, memos, and working docs are treated as shared human/AI artifacts with provenance, comments, and tracked edits built into the document itself *(as of 2026-03-15)*

### Autonomous research agents

Agents that close the full research loop end-to-end — reading literature, collecting data, running experiments, evaluating results, and iterating — with minimal human steering between steps.

- [[tools/hf-ml-intern]] — Hugging Face; open-source ML post-training research loop agent; reads papers, collects datasets, launches training jobs, evaluates, and iterates; GPQA 10% → 32% in <10 hours on Qwen3-1.7B *(as of 2026-04-22)*

### Science agent platforms

Platforms built to support literature-driven or discovery-oriented scientific work, without necessarily closing the full autonomous experiment loop end to end.

- [[tools/futurehouse]] — science-agent platform aimed at research and discovery workflows, distinct from generic chat assistants with science demos *(as of 2026-04-22)*

## Recent changes

- [2026-04-23] Google Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; ADK now sits inside a fuller enterprise stack with Agent Studio, Workspace Intelligence GA, and Knowledge Catalog
- [2026-04-23] Added [[tools/microsoft-foundry-agents]] under `Agent orchestration`; Microsoft is now a serious enterprise hosted-agent platform contender with VM-per-session isolation, persistent resume, and a fuller governance stack
- [2026-04-23] Added [[workflows/skillify-agent-reliability]]; Garry Tan's 10-step "thin harness / fat skills" agent reliability pattern — most detailed published treatment of agent skill architecture and failure prevention
- [2026-04-22] Added `Agent frameworks` with [[tools/google-adk]]; active framework layer should be represented directly instead of forced into orchestration-only categories; [[tools/hermes-agent]] reclassified here from agent-orchestration
- [2026-04-22] Added `Deep research tools`; restructured as concept ([[concepts/deep-research]]) + individual tool pages ([[tools/openai-deep-research]], [[tools/gemini-deep-research]])
- [2026-04-22] Added `Science agent platforms` with [[tools/futurehouse]]; science-agent infrastructure deserves a slot between orchestration and full autonomous research
- [2026-04-22] Added [[tools/uipath-maestro]] under `Agent orchestration`; enterprise orchestration for agents and robots broadens the category beyond hosted agent runtimes
- [2026-04-22] Added `Autonomous research agents` subcategory; [[tools/hf-ml-intern]] is the first publicly verified agent to close the full ML post-training loop end-to-end
- [2026-04-22] Google Deep Research Max scores (93.3% DeepSearchQA) and HF ml-intern autonomous loop mark the emergence of a distinct "full-stack research agent" tier — see [[tools/gemini]] and [[tools/hf-ml-intern]]
- [2026-02-25] Cursor's cloud-agent rollout already showed the orchestration-ui pattern in product form: remote agent computers, self-verification, and video artifacts for human review
- [2026-03-06] Cursor's cloud-agent walkthrough made the category's supervision thesis explicit before the later 3.1 control-plane polish: remote agents, review videos, and human oversight over many workers
- [2026-04-22] Added `Agent-native documents` to capture document surfaces built for shared human/agent drafting; [[tools/proof]] is the first example
- [2026-04-21] Added [[tools/orca]] under `Agent orchestration`; worktree-first desktop supervision layer for Claude Code, Codex, and similar agents
- [2026-03-31] Backfilled late-March signal: open-agent stacks were already converging on CLI-first execution, worktree coordination, and packaged reusable agents before the April orchestration/control-plane wave became clearer
- [2026-04-21] Added earlier Anthropic productivity-surface precursor: Claude for Word beta helps explain Cowork / Live Artifacts as expansion of an existing direction
- [2026-04-15] Anthropic's Managed Agents now reads as part of a broader platform cluster: hosted runtime, custom agents, and Claude Code long-running monitor/loop patterns
- [2026-04-14] Cursor 3.1 added tiled multi-agent supervision and stronger control-plane UX, reinforcing the shift from AI-enhanced IDEs toward agent workspaces
