# State of Agents — History

- [2026-05-05] Model-pool routing and local-first browser agents emerge as a two-tier orchestration pattern: AI-managed orchestrators route across model pools at the top; local browser agents handle tasks client-side without cloud handoff
- [2026-05-01] Production harness engineering expanding into deployment manifests, auth, RBAC, credential management, and artifact-backed multi-agent collaboration — beyond loop logic and evals alone

- [2026-04-21] Added [Claude Cowork](../../tools/claude-cowork.md) under `Agent orchestration UIs`; desktop-first knowledge-work agent with Live Artifacts
- [2026-04-21] Added [Hermes Agent](../../tools/hermes-agent.md) under `Agent orchestration`; 100K stars, substantive orchestration patterns from AINews breakdown
- [2026-04-15] Added [OpenAI Agents SDK](../../tools/openai-agents-sdk.md) under `agent-orchestration` after ingesting OpenAI's Agents SDK evolution post.
- [2026-04-10] Added [Agentic thinking](../../concepts/agentic-thinking.md) — Junyang Lin's essay on the shift from reasoning to agentic thinking
- [2026-04-09] Added `agent-orchestration` with [Claude Managed Agents](../../tools/claude-managed-agents.md) after ingesting Anthropic's Managed Agents architecture post.
- [2026-04-09] Added `agentic-devops` subcategory with [Stripe CLI](../../tools/stripe-cli.md) after ingesting the `projects.dev` landing page
- [2026-04-09] Added `model-orchestration` subcategory with [Advisor strategy](../../workflows/advisor-strategy.md) after ingesting Anthropic's advisor-strategy launch post.
- [2026-04-02] First content for this page. Added `agent-orchestration-ui` subcategory with Cursor after ingesting the Cursor 3 launch post.
- [2025-03-06] Added [Curiosity-driven imagination](../../concepts/curiosity-driven-imagination.md) — paper pattern for agents that recover from broken plans by exploring, learning new steps, and turning them into guided rewards
## Archived from current page on 2026-05-19

- [2026-05-13] Frontier labs increasingly show up as deployment-service firms: enterprise value is shifting toward workflow templates, context, permissions, evals, and handoffs around model access.
- [2026-05-13] Added `Persistent coding agents` subcategory: always-on agents with long-term memory, self-initiated contact, and self-pruning skill libraries; Hermes Agent and OpenClaw (with security advisory) are the first entries
- [2026-05-13] Native real-time voice / interaction models arrive: Thinking Machines Lab TML-Interaction-Small (276B, 200ms audio, 0.4s response, mid-sentence interrupts) and Google Magic Pointer (Gemini OS-level cursor for Googlebook) move AI from chat-in-a-window toward ambient real-time co-presence
- [2026-05-12] METR long-horizon benchmark: Claude Mythos Preview 50% success at 16+ hours (breaks current scale); 80% reliability threshold ~3 human-hours (Gemini 3.1 Pro ~1.5 hours); METR cautions duration is a difficulty proxy, not wall-clock time
- [2026-05-11] OpenClaw supply chain attack (341 malicious registry entries); Microsoft enterprise warning; reinforces the memory-ownership question for persistent-agent deployments
- [2026-05-05] Mistral Workflows (public preview): production-agent orchestration primitives now a shipped product — durable execution, state persistence, streaming, subagent coordination, and session resumption; signals these are table-stakes for hosted agent runtimes
- [2026-05-05] Manus Cloud Computer introduces persistent Ubuntu environments for agents — SSH/web-terminal access, pre-installed tools, state that survives across sessions; contrasts with per-task ephemeral container model
- [2026-05-05] Inference inflection framing: agent infrastructure needs extend beyond GPU compute to CPU orchestration, sandbox, browser, and execution capacity — compound infrastructure requirements

## Archived from current page on 2026-05-13

- [2026-05-01] Codex Workspace Agents positioning sharpened: secondary newsletter coverage now frames Codex as a horizontal computer-work agent (docs, sheets, slides, research, planning, connected apps), not only software engineering; added to State of Computer Use as a horizontal entrant
- [2026-04-24] Broadened `agentic-devops` from provisioning-only CLI workflows toward a fuller infrastructure-operations stack: diagnosis, approval-gated mutation, and post-deploy verification
- [2026-04-24] Claude Managed Agents added built-in file-backed memory with shared stores, audit logs, and rollback controls; Anthropic's hosted-runtime story is becoming a more opinionated durable-agent platform
- [2026-04-22] Microsoft Copilot's agentic mode in Word, Excel, and PowerPoint reached GA/default status; Microsoft is now pushing agent behavior directly into Office's core work canvas, not only hosted runtimes like Foundry
- [2026-04-23] Added OpenAI Workspace Agents under `Agent orchestration`; Codex-powered shareable team agents in Slack and ChatGPT land the same day as Google's enterprise agent-platform push
- [2026-04-23] Google Cloud Next '26: Gemini Enterprise Agent Platform replaces Vertex AI; ADK now sits inside a fuller enterprise stack with Agent Studio, Workspace Intelligence GA, and Knowledge Catalog
- [2026-04-23] Added [Microsoft Foundry Hosted Agents](../../tools/microsoft-foundry-agents.md) under `Agent orchestration`; Microsoft is now a serious enterprise hosted-agent platform contender with VM-per-session isolation, persistent resume, and a fuller governance stack
- [2026-04-23] Added [Skillify — Agent Reliability Pattern](../../workflows/skillify-agent-reliability.md); Garry Tan's 10-step "thin harness / fat skills" agent reliability pattern — most detailed published treatment of agent skill architecture and failure prevention
- [2026-04-22] Added `Agent frameworks` with [Google ADK](../../tools/google-adk.md); active framework layer should be represented directly instead of forced into orchestration-only categories; [Hermes Agent](../../tools/hermes-agent.md) reclassified here from agent-orchestration
- [2026-04-22] Added `Deep research tools`; restructured as concept ([Deep Research (concept)](../../concepts/deep-research.md)) + individual tool pages ([OpenAI Deep Research](../../tools/openai-deep-research.md), [Gemini Deep Research](../../tools/gemini-deep-research.md))
- [2026-04-22] Added `Science agent platforms` with [FutureHouse](../../tools/futurehouse.md); science-agent infrastructure deserves a slot between orchestration and full autonomous research
- [2026-04-22] Added [UiPath Maestro](../../tools/uipath-maestro.md) under `Agent orchestration`; enterprise orchestration for agents and robots broadens the category beyond hosted agent runtimes
- [2026-04-22] Added `Autonomous research agents` subcategory; [HF ml-intern](../../tools/hf-ml-intern.md) is the first publicly verified agent to close the full ML post-training loop end-to-end
- [2026-04-22] Google Deep Research Max scores (93.3% DeepSearchQA) and HF ml-intern autonomous loop mark the emergence of a distinct "full-stack research agent" tier — see [Gemini](../../tools/gemini.md) and [HF ml-intern](../../tools/hf-ml-intern.md)
- [2026-04-22] Added `Agent-native documents` to capture document surfaces built for shared human/agent drafting; [Proof](../../tools/proof.md) is the first example
- [2026-04-21] Added [Orca](../../tools/orca.md) under `Agent orchestration`; worktree-first desktop supervision layer for Claude Code, Codex, and similar agents
- [2026-03-31] Backfilled late-March signal: open-agent stacks were already converging on CLI-first execution, worktree coordination, and packaged reusable agents before the April orchestration/control-plane wave became clearer
- [2026-04-21] Added earlier Anthropic productivity-surface precursor: Claude for Word beta helps explain Cowork / Live Artifacts as expansion of an existing direction
- [2026-04-15] Anthropic's Managed Agents now reads as part of a broader platform cluster: hosted runtime, custom agents, and Claude Code long-running monitor/loop patterns
- [2026-04-14] Cursor 3.1 added tiled multi-agent supervision and stronger control-plane UX, reinforcing the shift from AI-enhanced IDEs toward agent workspaces
