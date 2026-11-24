---
title: Agent runtime platforms
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-10-07
sources: [thecode-april-22-2026, ainews-2026-04-22, shopify-claude-code-bessemer-2026-05, ainews-death-of-params-glm-53-2026-08-20, ainews-poolside-nvidia-2026-08-21, ainews-andrew-ng-ai-engineering-2026-08-25, gemini-managed-agents-2026-07, claude-managed-agents-updates-2026-05, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, cloudflare-computer-launch-2026-09-07, skills-and-plugin-packaging-late-march, openai-agents-sdk-evolution, agent-infrastructure-harness-2026-05-01, ainews-navier-stokes-2026-09-09, claude-tag-slack-agent-2026-06, ainews-fal-h3-max-live-2026-09-01, latent-space-thariq-claude-code-next-era-2026-09-29, claudedevs-cloud-sessions-ga-2026-09-23, devin-cloud-in-your-terminal-2026-09-21, ainews-codex-cloud-environments-2026-09-30, ainews-pi-10-pi-durable-2026-10-02, ainews-pi-durable-harness-rl-2026-10-06, latent-space-stacklok-mecatl-2026-10-07, latent-space-openai-api-agents-api-2026-09-30, ainews-openai-devday-2026-dots-2026-09-30, digitalocean-managed-agents-public-preview-2026-09-22]
---

# Agent runtime platforms

The infrastructure layer underneath and around an agent [harness](harness.md): where agents execute, how a fleet of them is governed, and how a working harness setup gets packaged and distributed to other people. Work that custom harnesses used to implement by hand (sandboxing, background execution, credential refresh, connector auth, cost routing) is moving into hosted platforms, open self-hostable alternatives, and enterprise control planes. The harness decides how one agent behaves; the runtime platform decides where it runs, who it is allowed to act as, and how many copies of it an organization can afford.

## Current status (as of 2026-10-07)

- Hosted managed-agent platforms ([Claude Managed Agents](../tools/claude-managed-agents.md), [Gemini](../tools/gemini.md)) now ship MCP tool connectivity, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution as product primitives.
- Open harnesses are matching managed platforms on quality at lower cost, so the managed/self-hosted choice is becoming an economics question.
- Runtime design is shifting from container-per-agent toward lighter isolates, with containers reserved for work that needs a real toolchain.
- Enterprises are putting control planes (LLM proxies, IdP-managed connector auth) above individual tool harnesses.
- Cloud sessions that outlive the laptop, with handoff back to a local checkout, became standard across Claude Code, Devin and Codex in late September 2026.
- Open-source harnesses are being rebuilt to run as server infrastructure: the agent loop is split from its state and its execution environment so sessions survive crashes and can be governed centrally ([Pi](../tools/pi.md) Durable, Stacklok's [Mecatl](../tools/mecatl.md)).
- Model labs now ship their own harness as an API: OpenAI's Agents API gives developers the Codex harness with computer use and compaction built in.

## Execution runtimes

- **Isolates over containers as the default agent-runtime primitive.** Cloudflare's open-source `@cloudflare/computer` argues container-per-agent doesn't scale to hundreds of millions of concurrent agents, and gives agents a durable shared filesystem across two swappable execution backends: fast, cheap isolates (Cloudflare Workers/Durable Objects) for file/git/data work, and full-Linux containers only when npm, native binaries, or a real toolchain are actually needed. Target: containers handle under 10% of an agent's work.
- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution — a sign that "harness" is becoming product infrastructure, not only application code. Claude Managed Agents added self-hosted sandboxes and MCP tunnels in May 2026, and in August 2026 Claude Platform reached GA for computer use, the browser tool, the Skills API, and the Files API, plus an AG-UI adapter for Managed Agents.
- **Bring-your-own-harness managed runtimes.** [DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) (public preview, September 2026) sells the runtime without a harness of its own: Claude Code, Codex CLI, OpenCode, or a custom container runs in a pausable, forkable microVM session, and tools go through a separate MCP gateway that brokers credentials at call time, so they never enter the sandbox.
- **Model-lab agent APIs.** OpenAI's Agents API (DevDay, 2026-09-29) packages the Codex harness, including the same computer-use implementation the models are trained on, and runs OpenAI's own Codex Security and meeting-notes features. The lower-level Responses API gained async tool calls (the model keeps reasoning while a tool runs), mid-turn steering over WebSockets, guaranteed 30-minute cache hits with a paid 12-hour tier in preview for single long-lived agent threads, cache pre-warming, and server-side compaction at a token threshold, with a manual `/compact` that big coding agents prefer. API lead Nikunj Handa calls the right level of abstraction (memory, storage) an open question.
- **Open harnesses matching managed-agent quality at lower cost.** TrueFoundry's MIT-licensed, self-hostable TrueForge harness reportedly matched Claude Managed Agents on Opus 4.8 using ~30% fewer tokens on a 14-task enterprise benchmark, and cut cost ~75% on GLM-5.2 versus a frontier model — harness quality compensating for model cost.
- **Plugin-native harness runtimes.** DeepSeek Harness (DSH) is an intentionally thin shell over a plugin system called Cordis, where even the agent loop itself is a plugin — beta users reportedly shipped 100+ community plugins and filed 400+ issues in under a week, illustrating how far extensibility can push down into a runtime's own control loop. DeepSeek's harness later took on breaking plugin-contract changes.
- **Real-session browsing.** [Hermes Agent](../tools/hermes-agent.md) can browse using a managed copy of the user's real Chrome profile and logins, collapsing auth friction — and raising the importance of scoped-permission design at the harness layer.
- **Harness separate from compute.** OpenAI's April 15, 2026 Agents SDK post gives a concrete vendor example of the broad definition: configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP, skills, AGENTS.md, shell, and `apply_patch`. It keeps the harness separate from compute so credentials stay outside execution sandboxes and runs survive sandbox failure via snapshotting and rehydration.

## Durable and cloud-native harnesses

- **Checkpoint every step.** [Pi](../tools/pi.md) Durable rebuilds a minimal coding harness around a small task-based workflow engine: each step is a checkpointed task, so agents and subagents resume from their exact state after a crash. Storage is pluggable (memory, SQLite, JSONL), the same code runs on Bun or Cloudflare Durable Objects, and app state stored beside the transcript lets several people or UIs watch and steer one agent.
- **Separate the loop from everything it touches.** Stacklok's open-source [Mecatl](../tools/mecatl.md), from Kubernetes co-creators Craig McLuckie and Joe Beda, keeps the agent loop independent of the client, model provider, state store, and execution environment. Their argument is that desktop-first harnesses run loop, tools, and session state in one process, so "lift and shift" into a VM or sandbox breaks lifecycle tasks such as pausing an agent safely while it waits for a person. Session state and memory move from JSONL files on disk into managed systems, and agent conversations become company records governed like email. This is the open-source counterpart of the OpenAI Agents SDK's harness/compute split above.
- **The surrounding control plane.** Stacklok pairs Mecatl with ToolHive (running and governing MCP servers on Kubernetes) and an AI gateway for access control, budgets, reporting, and provider routing. The gateway deliberately does not pick models per task; McLuckie wants that choice made inside the harness, which has more context.

## Fleet management and governance

- **LLM proxy as the fleet management layer.** At org scale (Shopify, 23K engineers), routing all AI coding-tool traffic through a centralized LLM proxy creates a control plane for cost, model choice, and policy enforcement without requiring per-tool reconfiguration. The proxy sits above the individual tool harness and below the model.
- **Enterprise-managed MCP auth.** Anthropic rolled out enterprise-managed authentication for MCP connectors, centralizing authorization through the org's identity provider so end users no longer perform per-tool OAuth for connectors like Asana, Atlassian, Figma, Notion, Slack, and Supabase — moving MCP connector auth from a per-user click-through into IT-governed infrastructure.
- **Standardize on one harness, not bespoke orchestration graphs.** A position paper argues enterprises should pick a single reusable coding-agent harness rather than building bespoke orchestration per team, since harness choice can matter more for outcomes than model choice.
- **Deployment manifests.** LangChain's `deepagents.toml` manifest packages sandboxing, auth, RBAC, credentials, and frontend config into one deployable artifact; Agent Collabs uses Hugging Face dataset buckets (shared storage) plus Spaces (isolated execution) so heterogeneous agents collaborate without sharing one mutable runtime. LangChain later added `deepagents` primitives for this layer: subagent forking that passes a supervisor's context down to its subagents, and managed connections that abstract OAuth/token/consent flows for either agent-owned or user-owned identities.
- **Org-embedded identity and permissioning.** Slack-native and team-channel agents need a legible identity, scoped access to channels/tools/data, audit trails, and memory boundaries that match how the organization partitions work; otherwise the harness becomes an organizational risk surface (unclear accountability, prompt-injection exposure, budget opacity, channel noise).

## Tooling and distribution

- **Agent-friendly CLI design.** Tools built for human interactive use break agent pipelines: interactive prompts stall agents, undocumented flags require inference, and missing non-interactive modes force workarounds. Agent-facing CLI tools should be non-interactive by default, expose all behaviors through explicit flags, and document internal conventions. This applies equally to the tools the agent calls and to the CLIs agents themselves expose.
- **DSPy 3.2** (April 2026) as a harness-engineering toolchain: adds Reinforced Language Model (RLM) improvements, optimizer chaining, and LiteLLM decoupling. Relevant for teams iterating on harness prompts and orchestration logic using programmatic optimization.
- **Packaging the operating judgment.** Teams do not only want a good harness inside one project; they want reusable packaging for the fuzzy operating judgment that makes the harness good. That is why plugin marketplaces, skills folders, and installable bundles keep surfacing across coding-agent ecosystems (late March 2026 onward).
- **Managed-agent cookbooks as harness distribution.** Claude Managed Agents' Vercel Chat SDK cookbook packages a harness pattern as a reusable recipe rather than bespoke integration work. Perplexity separately added Agent API connectors for GitHub, Slack, Google Drive, and Datadog.

## Cloud-resident agents

Several practitioners describe local CLI agents giving way to cloud-resident "persistent computer" agents with shared context and memory across sessions: Claude Code shipped `/resume` for desktop terminal-session continuity, Kimi Code added experimental Remote Control, OpenAI introduced "appshots" for richer app-context grounding, and Ollama began positioning a hosted GLM-5.3-Flash backend as a private cloud harness endpoint for Claude, OpenCode, and Hermes (late August 2026).

By late September 2026 this was the default shape for the leading coding agents. Claude Code cloud sessions left research preview on 23 September (`claude --cloud`, plus web, mobile and desktop). Devin Cloud reached the terminal on 21 September: `/handoff` moves a task from the local CLI to a dedicated cloud VM and back onto a local branch, and `devin ssh` opens the agent's VM as a dev environment. Codex added cloud environments that keep running with the laptop closed. Anthropic calls the next step "cloud brain, local hands": one cloud-resident agent holds the reasoning, does the work in a cloud sandbox or on the user's machine when it is online, and shows progress through hosted artifacts with their own database. [Devin Outposts](../tools/devin.md) already splits a cloud planning loop from execution on customer machines.

## Recent changes

- [2026-10-19] Added the OpenAI Agents SDK harness/compute separation, deployment-manifest implementations (deepagents.toml, Agent Collabs, deepagents primitives), and org-embedded agent identity, moved from [Harness (agent)](harness.md).
- [2026-10-19] Page created, split out of [Harness (agent)](harness.md): its "Tooling, protocol, and fleet management" and "Managed platforms, distribution, and evaluation" subsections, the Cloudflare isolates bullet, the cloud-resident-agents paragraph, and the late-March packaging paragraph from "Why it matters", and the Claude Platform GA fact (previously only in Harness's Recent changes).
- [2026-10-07] Added a "Durable and cloud-native harnesses" section: Pi Durable's checkpointed workflow engine and Stacklok's Mecatl (loop separated from client, model, state, and execution), plus Stacklok's ToolHive and AI-gateway control plane.
- [2026-09-30] Cloud-resident agents: Claude Code cloud sessions GA, Devin Cloud in the terminal with two-way `/handoff` and `devin ssh`, Codex cloud environments; Anthropic's "cloud brain, local hands" direction.
- [2026-09-30] Added model-lab agent APIs: OpenAI's Agents API (Codex harness with computer use and built-in compaction) and the Responses API's async tools, mid-turn steering, cache guarantees and pre-warming.
- [2026-09-22] Added bring-your-own-harness managed runtimes: DigitalOcean Managed Agents runs customer harnesses in microVM sessions behind a credential-brokering MCP gateway.
- [2026-09-07] Added Cloudflare's `@cloudflare/computer`: isolates-over-containers as the default agent-runtime primitive, with a shared filesystem across two swappable execution backends.

## Related

- [Harness (agent)](harness.md) — what the harness itself includes and what good harness design looks like; this page covers the runtime, governance, and distribution layer around it
- [Claude Managed Agents](../tools/claude-managed-agents.md) and [Gemini](../tools/gemini.md) — the two leading managed-agent platform implementations
- [Agent Labs vs Model Labs](agent-labs-vs-model-labs.md) — why harness and platform ownership is a competitive moat
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — the operating patterns run on top of these platforms

## Sources

- [The Code newsletter — 2026-04-22 (Cursor/SpaceX, Claude Code recap, CLI design)](../sources/newsletters/thecode-april-22-2026.md)
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [Skills and plugin packaging in late March](../sources/newsletters/skills-and-plugin-packaging-late-march.md)
- [Shopify Claude Code fleet patterns — Bessemer conference synthesis](../sources/articles/shopify-claude-code-bessemer-2026-05.md)
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [Gemini managed agents in the API](../sources/newsletters/gemini-managed-agents-2026-07.md)
- [AINews — Death of Params: GLM 5.3](../sources/newsletters/ainews-death-of-params-glm-53-2026-08-20.md)
- [AINews — NVIDIA's Poolside reverse execuhire (Claude Platform GA)](../sources/newsletters/ainews-poolside-nvidia-2026-08-21.md)
- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
- [Cloudflare — Your agent needs a computer, not a container](../sources/articles/cloudflare-computer-launch-2026-09-07.md)
- [The next evolution of the Agents SDK](../sources/articles/openai-agents-sdk-evolution.md)
- [Agent infrastructure, harness engineering, and collaborative agent systems](../sources/newsletters/agent-infrastructure-harness-2026-05-01.md)
- [[AINews] OpenAI reports Navier-Stokes singularity find in 88 hours using Astra-next, roughly 10,000 agents and 130B tokens](../sources/newsletters/ainews-navier-stokes-2026-09-09.md)
- [Claude Tag Slack-native agent launch](../sources/newsletters/claude-tag-slack-agent-2026-06.md)
- [Latent Space — Claude Code's Next Era (Thariq Shihipar)](../sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md)
- [ClaudeDevs — Cloud sessions out of research preview](../sources/tweets/claudedevs-cloud-sessions-ga-2026-09-23.md)
- [Cognition — Bringing Devin Cloud to your terminal](../sources/articles/devin-cloud-in-your-terminal-2026-09-21.md)
- [AINews — Codex cloud environments](../sources/newsletters/ainews-codex-cloud-environments-2026-09-30.md)
- [AINews — Pi 1.0 and Pi Durable](../sources/newsletters/ainews-pi-10-pi-durable-2026-10-02.md)
- [AINews — Pi Durable design and multi-harness RL](../sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md)
- [Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)](../sources/newsletters/latent-space-stacklok-mecatl-2026-10-07.md)
- [Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)](../sources/newsletters/latent-space-openai-api-agents-api-2026-09-30.md)
- [AINews — OpenAI DevDay 2026: dots and platform changes](../sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md)
- [DigitalOcean — Introducing Managed Agents](../sources/articles/digitalocean-managed-agents-public-preview-2026-09-22.md)
