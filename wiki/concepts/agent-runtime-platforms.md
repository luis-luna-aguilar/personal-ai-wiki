---
title: Agent runtime platforms
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-07
sources: [thecode-april-22-2026, ainews-2026-04-22, shopify-claude-code-bessemer-2026-05, ainews-death-of-params-glm-53-2026-08-20, ainews-poolside-nvidia-2026-08-21, ainews-andrew-ng-ai-engineering-2026-08-25, gemini-managed-agents-2026-07, claude-managed-agents-updates-2026-05, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, cloudflare-computer-launch-2026-09-07, skills-and-plugin-packaging-late-march]
---

# Agent runtime platforms

The infrastructure layer underneath and around an agent [harness](harness.md): where agents execute, how a fleet of them is governed, and how a working harness setup gets packaged and distributed to other people. Work that custom harnesses used to implement by hand (sandboxing, background execution, credential refresh, connector auth, cost routing) is moving into hosted platforms, open self-hostable alternatives, and enterprise control planes. The harness decides how one agent behaves; the runtime platform decides where it runs, who it is allowed to act as, and how many copies of it an organization can afford.

## Current status (as of 2026-09-07)

- Hosted managed-agent platforms ([Claude Managed Agents](../tools/claude-managed-agents.md), [Gemini](../tools/gemini.md)) now ship MCP tool connectivity, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution as product primitives.
- Open harnesses are matching managed platforms on quality at lower cost, so the managed/self-hosted choice is becoming an economics question.
- Runtime design is shifting from container-per-agent toward lighter isolates, with containers reserved for work that needs a real toolchain.
- Enterprises are putting control planes (LLM proxies, IdP-managed connector auth) above individual tool harnesses.

## Execution runtimes

- **Isolates over containers as the default agent-runtime primitive.** Cloudflare's open-source `@cloudflare/computer` argues container-per-agent doesn't scale to hundreds of millions of concurrent agents, and gives agents a durable shared filesystem across two swappable execution backends: fast, cheap isolates (Cloudflare Workers/Durable Objects) for file/git/data work, and full-Linux containers only when npm, native binaries, or a real toolchain are actually needed. Target: containers handle under 10% of an agent's work.
- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution — a sign that "harness" is becoming product infrastructure, not only application code. Claude Managed Agents added self-hosted sandboxes and MCP tunnels in May 2026, and in August 2026 Claude Platform reached GA for computer use, the browser tool, the Skills API, and the Files API, plus an AG-UI adapter for Managed Agents.
- **Open harnesses matching managed-agent quality at lower cost.** TrueFoundry's MIT-licensed, self-hostable TrueForge harness reportedly matched Claude Managed Agents on Opus 4.8 using ~30% fewer tokens on a 14-task enterprise benchmark, and cut cost ~75% on GLM-5.2 versus a frontier model — harness quality compensating for model cost.
- **Plugin-native harness runtimes.** DeepSeek Harness (DSH) is an intentionally thin shell over a plugin system called Cordis, where even the agent loop itself is a plugin — beta users reportedly shipped 100+ community plugins and filed 400+ issues in under a week, illustrating how far extensibility can push down into a runtime's own control loop.
- **Real-session browsing.** [Hermes Agent](../tools/hermes-agent.md) can browse using a managed copy of the user's real Chrome profile and logins, collapsing auth friction — and raising the importance of scoped-permission design at the harness layer.

## Fleet management and governance

- **LLM proxy as the fleet management layer.** At org scale (Shopify, 23K engineers), routing all AI coding-tool traffic through a centralized LLM proxy creates a control plane for cost, model choice, and policy enforcement without requiring per-tool reconfiguration. The proxy sits above the individual tool harness and below the model.
- **Enterprise-managed MCP auth.** Anthropic rolled out enterprise-managed authentication for MCP connectors, centralizing authorization through the org's identity provider so end users no longer perform per-tool OAuth for connectors like Asana, Atlassian, Figma, Notion, Slack, and Supabase — moving MCP connector auth from a per-user click-through into IT-governed infrastructure.
- **Standardize on one harness, not bespoke orchestration graphs.** A position paper argues enterprises should pick a single reusable coding-agent harness rather than building bespoke orchestration per team, since harness choice can matter more for outcomes than model choice.

## Tooling and distribution

- **Agent-friendly CLI design.** Tools built for human interactive use break agent pipelines: interactive prompts stall agents, undocumented flags require inference, and missing non-interactive modes force workarounds. Agent-facing CLI tools should be non-interactive by default, expose all behaviors through explicit flags, and document internal conventions. This applies equally to the tools the agent calls and to the CLIs agents themselves expose.
- **DSPy 3.2** (April 2026) as a harness-engineering toolchain: adds Reinforced Language Model (RLM) improvements, optimizer chaining, and LiteLLM decoupling. Relevant for teams iterating on harness prompts and orchestration logic using programmatic optimization.
- **Packaging the operating judgment.** Teams do not only want a good harness inside one project; they want reusable packaging for the fuzzy operating judgment that makes the harness good. That is why plugin marketplaces, skills folders, and installable bundles keep surfacing across coding-agent ecosystems (late March 2026 onward).
- **Managed-agent cookbooks as harness distribution.** Claude Managed Agents' Vercel Chat SDK cookbook packages a harness pattern as a reusable recipe rather than bespoke integration work. Perplexity separately added Agent API connectors for GitHub, Slack, Google Drive, and Datadog.

## Cloud-resident agents

Several practitioners describe local CLI agents giving way to cloud-resident "persistent computer" agents with shared context and memory across sessions: Claude Code shipped `/resume` for desktop terminal-session continuity, Kimi Code added experimental Remote Control, OpenAI introduced "appshots" for richer app-context grounding, and Ollama began positioning a hosted GLM-5.3-Flash backend as a private cloud harness endpoint for Claude, OpenCode, and Hermes (late August 2026).

## Recent changes

- [2026-10-19] Page created, split out of [Harness (agent)](harness.md): its "Tooling, protocol, and fleet management" and "Managed platforms, distribution, and evaluation" subsections, the Cloudflare isolates bullet, the cloud-resident-agents paragraph, and the late-March packaging paragraph from "Why it matters", and the Claude Platform GA fact (previously only in Harness's Recent changes).
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
