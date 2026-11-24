---
title: Agent execution runtimes
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-11-23
sources: [cloudflare-computer-launch-2026-09-07, gemini-managed-agents-2026-07, claude-managed-agents-updates-2026-05, ainews-poolside-nvidia-2026-08-21, digitalocean-managed-agents-public-preview-2026-09-22, latent-space-openai-api-agents-api-2026-09-30, ainews-openai-devday-2026-dots-2026-09-30, ainews-death-of-params-glm-53-2026-08-20, ainews-openai-agi-bar-2026-08-28, openai-agents-sdk-evolution, ainews-pi-10-pi-durable-2026-10-02, ainews-pi-durable-harness-rl-2026-10-06, latent-space-stacklok-mecatl-2026-10-07, openai-background-mode-docs-2026-11]
---

# Agent execution runtimes

Where an agent actually runs: the sandboxes, isolates, microVMs, hosted platforms, and durable workflow engines underneath an agent [harness](harness.md). This is the execution slice of the [agent runtime platforms](agent-runtime-platforms.md) layer; fleet governance, distribution, and cloud-resident agents stay on that page. The trend is that work custom harnesses used to do by hand (sandboxing, background execution, credential refresh, crash recovery) is becoming product infrastructure, either hosted by a vendor or rebuilt as open server software.

## Current status (as of 2026-11-23)

- Hosted managed-agent platforms ([Claude Managed Agents](../tools/claude-managed-agents.md), [Gemini](../tools/gemini.md)) now ship MCP tool connectivity, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution as product primitives.
- Open harnesses are matching managed platforms on quality at lower cost, so the managed/self-hosted choice is becoming an economics question.
- Runtime design is shifting from container-per-agent toward lighter isolates, with containers reserved for work that needs a real toolchain.
- Open-source harnesses are being rebuilt to run as server infrastructure: the agent loop is split from its state and its execution environment so sessions survive crashes and can be governed centrally ([Pi](../tools/pi.md) Durable, Stacklok's [Mecatl](../tools/mecatl.md)).
- Model labs now ship their own harness as an API: OpenAI's Agents API gives developers the Codex harness with computer use and compaction built in.

## Execution runtimes

- **Isolates over containers as the default agent-runtime primitive.** Cloudflare's open-source `@cloudflare/computer` argues container-per-agent doesn't scale to hundreds of millions of concurrent agents, and gives agents a durable shared filesystem across two swappable execution backends: fast, cheap isolates (Cloudflare Workers/Durable Objects) for file/git/data work, and full-Linux containers only when npm, native binaries, or a real toolchain are actually needed. Target: containers handle under 10% of an agent's work.
- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution — a sign that "harness" is becoming product infrastructure, not only application code. Claude Managed Agents added self-hosted sandboxes and MCP tunnels in May 2026, and in August 2026 Claude Platform reached GA for computer use, the browser tool, the Skills API, and the Files API, plus an AG-UI adapter for Managed Agents.
- **Bring-your-own-harness managed runtimes.** [DigitalOcean Managed Agents](../tools/digitalocean-managed-agents.md) (public preview, September 2026) sells the runtime without a harness of its own: Claude Code, Codex CLI, OpenCode, or a custom container runs in a pausable, forkable microVM session, and tools go through a separate MCP gateway that brokers credentials at call time, so they never enter the sandbox.
- **Model-lab agent APIs.** OpenAI's Agents API (DevDay, 2026-09-29) packages the Codex harness, including the same computer-use implementation the models are trained on, and runs OpenAI's own Codex Security and meeting-notes features. The lower-level Responses API gained async tool calls (the model keeps reasoning while a tool runs), mid-turn steering over WebSockets, guaranteed 30-minute cache hits with a paid 12-hour tier in preview for single long-lived agent threads, cache pre-warming, and server-side compaction at a token threshold, with a manual `/compact` that big coding agents prefer. API lead Nikunj Handa calls the right level of abstraction (memory, storage) an open question. By November 2026 background mode covers multi-step agent runs: the application sends each turn as an asynchronous request, learns of completion by webhook or polling, and links follow-ups with a `continuation_id`; choosing a `2h` or `8h` completion window cuts token prices 30% or 40%, and these windows replace Flex processing on new models ([OpenAI discounted async processing](../workflows/async-discounted-processing.md)).
- **Open harnesses matching managed-agent quality at lower cost.** TrueFoundry's MIT-licensed, self-hostable TrueForge harness reportedly matched Claude Managed Agents on Opus 4.8 using ~30% fewer tokens on a 14-task enterprise benchmark, and cut cost ~75% on GLM-5.2 versus a frontier model — harness quality compensating for model cost.
- **Plugin-native harness runtimes.** DeepSeek Harness (DSH) is an intentionally thin shell over a plugin system called Cordis, where even the agent loop itself is a plugin — beta users reportedly shipped 100+ community plugins and filed 400+ issues in under a week, illustrating how far extensibility can push down into a runtime's own control loop. DeepSeek's harness later took on breaking plugin-contract changes.
- **Real-session browsing.** [Hermes Agent](../tools/hermes-agent.md) can browse using a managed copy of the user's real Chrome profile and logins, collapsing auth friction — and raising the importance of scoped-permission design at the harness layer.
- **Harness separate from compute.** OpenAI's April 15, 2026 Agents SDK post gives a concrete vendor example of the broad definition: configurable memory, sandbox-aware orchestration, Codex-like filesystem tools, MCP, skills, AGENTS.md, shell, and `apply_patch`. It keeps the harness separate from compute so credentials stay outside execution sandboxes and runs survive sandbox failure via snapshotting and rehydration.

## Durable and cloud-native harnesses

- **Checkpoint every step.** [Pi](../tools/pi.md) Durable rebuilds a minimal coding harness around a small task-based workflow engine: each step is a checkpointed task, so agents and subagents resume from their exact state after a crash. Storage is pluggable (memory, SQLite, JSONL), the same code runs on Bun or Cloudflare Durable Objects, and app state stored beside the transcript lets several people or UIs watch and steer one agent.
- **Separate the loop from everything it touches.** Stacklok's open-source [Mecatl](../tools/mecatl.md), from Kubernetes co-creators Craig McLuckie and Joe Beda, keeps the agent loop independent of the client, model provider, state store, and execution environment. Their argument is that desktop-first harnesses run loop, tools, and session state in one process, so "lift and shift" into a VM or sandbox breaks lifecycle tasks such as pausing an agent safely while it waits for a person. Session state and memory move from JSONL files on disk into managed systems, and agent conversations become company records governed like email. This is the open-source counterpart of the OpenAI Agents SDK's harness/compute split above.
- **The surrounding control plane.** Stacklok pairs Mecatl with ToolHive (running and governing MCP servers on Kubernetes) and an AI gateway for access control, budgets, reporting, and provider routing. The gateway deliberately does not pick models per task; McLuckie wants that choice made inside the harness, which has more context.

## Recent changes

- [2026-11-23] Page created, split out of [Agent runtime platforms](agent-runtime-platforms.md): its "Execution runtimes" and "Durable and cloud-native harnesses" sections and the matching Current-status bullets.
- [2026-11-23] Added Responses API background mode for multi-step agent runs (continuation IDs, webhook or polling) with discounted `2h`/`8h` completion windows replacing Flex on new models.
- [2026-10-19] Added the OpenAI Agents SDK harness/compute separation, moved from [Harness (agent)](harness.md).
- [2026-10-07] Added a "Durable and cloud-native harnesses" section: Pi Durable's checkpointed workflow engine and Stacklok's Mecatl (loop separated from client, model, state, and execution), plus Stacklok's ToolHive and AI-gateway control plane.
- [2026-09-30] Added model-lab agent APIs: OpenAI's Agents API (Codex harness with computer use and built-in compaction) and the Responses API's async tools, mid-turn steering, cache guarantees and pre-warming.
- [2026-09-22] Added bring-your-own-harness managed runtimes: DigitalOcean Managed Agents runs customer harnesses in microVM sessions behind a credential-brokering MCP gateway.
- [2026-09-07] Added Cloudflare's `@cloudflare/computer`: isolates-over-containers as the default agent-runtime primitive, with a shared filesystem across two swappable execution backends.

## Related

- [Agent runtime platforms](agent-runtime-platforms.md) — the wider layer: fleet governance, tooling and distribution, cloud-resident agents
- [Harness (agent)](harness.md) — what the harness itself includes; this page covers where it executes
- [Claude Managed Agents](../tools/claude-managed-agents.md) and [Gemini](../tools/gemini.md) — the two leading managed-agent platform implementations

## Sources

- [Cloudflare — Your agent needs a computer, not a container](../sources/articles/cloudflare-computer-launch-2026-09-07.md)
- [Gemini managed agents in the API](../sources/newsletters/gemini-managed-agents-2026-07.md)
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [AINews — NVIDIA's Poolside reverse execuhire (Claude Platform GA)](../sources/newsletters/ainews-poolside-nvidia-2026-08-21.md)
- [DigitalOcean — Introducing Managed Agents](../sources/articles/digitalocean-managed-agents-public-preview-2026-09-22.md)
- [Latent Space — OpenAI's API stack after DevDay (Nikunj Handa)](../sources/newsletters/latent-space-openai-api-agents-api-2026-09-30.md)
- [AINews — OpenAI DevDay 2026: dots and platform changes](../sources/newsletters/ainews-openai-devday-2026-dots-2026-09-30.md)
- [AINews — Death of Params: GLM 5.3](../sources/newsletters/ainews-death-of-params-glm-53-2026-08-20.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [The next evolution of the Agents SDK](../sources/articles/openai-agents-sdk-evolution.md)
- [AINews — Pi 1.0 and Pi Durable](../sources/newsletters/ainews-pi-10-pi-durable-2026-10-02.md)
- [AINews — Pi Durable design and multi-harness RL](../sources/newsletters/ainews-pi-durable-harness-rl-2026-10-06.md)
- [Latent Space — Can a cloud-native harness make agents reliable beyond the desktop? (Stacklok)](../sources/newsletters/latent-space-stacklok-mecatl-2026-10-07.md)
- [OpenAI API docs — Background mode](../sources/articles/openai-background-mode-docs-2026-11.md)
