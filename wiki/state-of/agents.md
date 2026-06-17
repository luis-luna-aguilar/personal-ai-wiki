---
title: State of Agents
type: state-of
domains: [agents]
tags: []
as_of: 2026-06-10
sources: [cursor-3-launch, advisor-strategy, stripe-cli, managed-agents, agentic-thinking-lin, curiosity-driven-imagination, openai-agents-sdk-evolution, ainews-2026-04-21, ainews-2026-04-22, claude-cowork-launch, every-managed-agents-vibe-check, claude-design-launch, orca-homepage, anthropic-platform-expansion-april-2026, coding-agent-control-planes, claude-productivity-surfaces, open-agent-orchestration-late-march, proof-agent-native-documents, cursor-cloud-agents-march, cursor-cloud-agents-february, google-adk, openai-deep-research, gemini-deep-research-max, futurehouse-homepage, uipath-maestro-introduction, anthropic-mcp, google-a2a, legacy-ai-tools-roadmap-xlsx, microsoft-foundry-agents-2026, google-cloud-next-2026, superhuman-2026-04-23, awsai-cowork-bedrock-2026-04-23, microsoft-copilot-agent-mode-office, claude-managed-agents-memory, agentic-devops-deep-research, agent-infrastructure-harness-2026-05-01, codex-for-work-2026-05-01, ai-managed-orchestration-local-browser-agents-2026-04-28, inference-inflection-agent-runtime-2026-04-30, persistent-cloud-computers-agents-2026-05-01, production-agent-orchestration-2026-04-29, hermes-openclaw-persistent-agents-2026-05-11, metr-long-horizon-2026-05-12, thinking-machines-interaction-2026-05-12, frontier-labs-deployment-services-2026-05-13, multica-repo, notion-external-agents-api-may-2026, langchain-interrupt-may-2026, devin-auto-triage-2026-05, papercliping]
---

# State of Agents

Current state of agentic systems — tool use, multi-step autonomy, orchestration frameworks. Organized by subcategory. Multiple leaders per subcategory are expected.

_Coding-agent leadership is tracked in [Coding](../state-of/coding.md). This page only includes coding-adjacent systems when they are also relevant as agent orchestration, framework, or deployment surfaces._

## Subcategories

### Agent orchestration

Platforms, surfaces, and patterns for running, supervising, or routing AI agents — spanning hosted runtimes, human-supervision UIs, and multi-model coordination within a single agentic task.

- [Claude Cowork](../tools/claude-cowork.md) — Anthropic; desktop knowledge-work agent with Live Artifacts; VM-backed local-first execution; now also the substrate for Claude for Small Business (15 workflows, QuickBooks/PayPal/DocuSign) and Claude for Legal (12 workflows) *(as of 2026-05-14)*
- [Codex](../tools/codex.md) (Workspace Agents) — OpenAI; shareable team agents in Slack and ChatGPT for scheduling, research, drafting, coding, and data analysis; now positioned as a broader computer-work agent (docs, sheets, slides, browser flows, connected apps) beyond software engineering *(as of 2026-05-01)*
- [Orca](../tools/orca.md) — open-source desktop surface for supervising multiple coding agents across isolated worktrees, with live status, diff review, and CI visibility *(as of 2026-04-21)*
- [Claude Managed Agents](../tools/claude-managed-agents.md) — Anthropic's hosted runtime; separates session, harness, sandbox, and now file-backed built-in memory with shared stores and auditability *(as of 2026-04-24)*
- [Microsoft Copilot](../tools/microsoft-copilot.md) — Microsoft; agentic default mode inside Word, Excel, and PowerPoint; takes multi-step native actions in documents, worksheets, and presentations while users stay in control *(as of 2026-04-22)*
- [Microsoft Foundry Hosted Agents](../tools/microsoft-foundry-agents.md) — Microsoft; hosted runtime with per-session VM isolation, persistent filesystems, Entra Agent ID governance, MCP Toolbox, and multi-framework support *(as of 2026-04-23)*
- [OpenAI Agents SDK](../tools/openai-agents-sdk.md) — model-native harness with native sandbox execution, durable checkpoint / rehydration, and provider-neutral manifests *(as of 2026-04-15)*
- [UiPath Maestro](../tools/uipath-maestro.md) — enterprise orchestration for agents, robots, and people; stronger fit for operational process flows than pure research workloads *(as of 2026-04-22)*
- [Multica](../tools/multica.md) — open-source; vendor-neutral managed agents platform; assign GitHub-style issues to agent CLIs (Claude Code, Codex, Copilot, and 8 others); Squads for leader-delegated routing; reusable skill compounding *(as of 2026-05-18)*
- [Paperclip](../tools/paperclip.md) — open-source (MIT), self-hosted; org-chart model: agents get titles, reporting lines, monthly budgets, and heartbeat schedules; Kubernetes deployment for hosted agents; governance keeps humans as the board of directors; 69.9k GitHub stars *(as of 2026-06-10)*
- [Advisor strategy](../workflows/advisor-strategy.md) — small executor (Sonnet/Haiku) drives the loop; escalates to Opus only when stuck; +2.7% SWE-bench Multilingual, −11.9% cost vs Sonnet alone *(as of 2026-04-09)*

### Agent frameworks

SDKs and development kits for building custom agents with tools, multi-agent patterns, and runtime scaffolding.

- [Google ADK](../tools/google-adk.md) — Google; open-source ADK now positioned as the developer layer inside Gemini Enterprise Agent Platform; Agent Studio adds a low-code wrapper, and Model Garden expands the surrounding stack to 200+ models *(as of 2026-04-23)*
- [Hermes Agent](../tools/hermes-agent.md) — NousResearch; open-source; brain+muscle architecture, Kanban supervision dashboard, weekly automated skill pruning, local-first memory, and 118 bundled skills *(as of 2026-05-13)*
- [LangChain / LangSmith](../tools/langchain-langsmith.md) — LangChain; open-source agent framework and observability platform; LangSmith Engine closes the trace→improvement loop automatically; SmithDB is a purpose-built agent-trace database *(as of 2026-05-15)*

### Persistent coding agents

Always-on background coding services that maintain memory across months, can initiate contact (Telegram, Discord, etc.), and manage their own skill libraries. Distinct from session-scoped coding agents.

- [Hermes Agent](../tools/hermes-agent.md) — NousResearch; open-source; brain+muscle architecture (separate reasoning and execution layers); Kanban supervision dashboard; weekly automated skill pruning; local-first memory *(as of 2026-05-13)*
- **OpenClaw** — viral open-source framework (345K stars); deep messaging-app integrations; **security advisory (May 2026):** 341 malicious registry entries planted in coordinated attack; Microsoft recommends enterprise customers avoid on work machines *(as of 2026-05-13)*
- [Devin Auto-Triage](../tools/devin.md) — Cognition; always-on persistent agent that monitors Slack channels and investigates bugs as reported; parent Devin filters noise and dispatches focused sub-sessions; shared long-term memory for deduplication across repeat reports; early users (Modal) describe it as more useful than homegrown triage automations *(as of 2026-05-19)*

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
- [Notion](../tools/notion.md) — Notion; External Agents API lets Claude Code, Cursor, Codex, Devin, Warp, and Decagon operate directly inside Notion as a shared context layer; Workers run in secure sandbox; CLI; free through August 2026 on Business/Enterprise *(as of 2026-05-14)*

### Autonomous research agents

Agents that close the full research loop end-to-end — reading literature, collecting data, running experiments, evaluating results, and iterating — with minimal human steering between steps.

- [HF ml-intern](../tools/hf-ml-intern.md) — Hugging Face; open-source ML post-training research loop agent; reads papers, collects datasets, launches training jobs, evaluates, and iterates; GPQA 10% → 32% in <10 hours on Qwen3-1.7B *(as of 2026-04-22)*

### Science agent platforms

Platforms built to support literature-driven or discovery-oriented scientific work, without necessarily closing the full autonomous experiment loop end to end.

- [FutureHouse](../tools/futurehouse.md) — science-agent platform aimed at research and discovery workflows, distinct from generic chat assistants with science demos *(as of 2026-04-22)*

## Recent changes

- [2026-05-19] Devin Auto-Triage: Cognition ships always-on session-persistent bug triage agent; Slack monitoring + parent/child Devin structure + long-term deduplication memory
- [2026-05-14] Anthropic launched Claude for Small Business and Claude for Legal on Cowork: 27 one-click agentic workflows; first direct vertical automation bundles targeting end-users rather than developers
- [2026-05-18] Multica launches
- [2026-05-15] LangChain Interrupt cluster: SmithDB (purpose-built agent trace DB, 12-15× faster, DataFusion+Vortex), LangSmith Engine (trace→cluster→fix loop), LangChain Labs (continual learning from production traces, Prime Intellect partnership) as open-source managed-agents platform: agents are first-class project-board members, not just CLI tools; Squads abstraction routes work through a leader agent; skills compound across sessions
- [2026-05-14] Notion External Agents API: Claude Code, Cursor, Codex, Devin, Warp, Decagon can now operate inside Notion workspaces via secure Workers sandbox — Notion joins Proof as an agent-native document surface


