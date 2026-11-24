---
title: Agent runtime platforms
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-09-30
sources: [thecode-april-22-2026, ainews-2026-04-22, shopify-claude-code-bessemer-2026-05, ainews-andrew-ng-ai-engineering-2026-08-25, ainews-openai-agi-bar-2026-08-28, ainews-openai-shuts-off-cursor-2026-08-29, skills-and-plugin-packaging-late-march, agent-infrastructure-harness-2026-05-01, ainews-navier-stokes-2026-09-09, claude-tag-slack-agent-2026-06, ainews-fal-h3-max-live-2026-09-01, latent-space-thariq-claude-code-next-era-2026-09-29, claudedevs-cloud-sessions-ga-2026-09-23, devin-cloud-in-your-terminal-2026-09-21, ainews-codex-cloud-environments-2026-09-30]
---

# Agent runtime platforms

The infrastructure layer underneath and around an agent [harness](harness.md): where agents execute, how a fleet of them is governed, and how a working harness setup gets packaged and distributed to other people. Work that custom harnesses used to implement by hand (sandboxing, background execution, credential refresh, connector auth, cost routing) is moving into hosted platforms, open self-hostable alternatives, and enterprise control planes. The harness decides how one agent behaves; the runtime platform decides where it runs, who it is allowed to act as, and how many copies of it an organization can afford.

## Current status (as of 2026-09-30)

- Execution has moved into hosted managed-agent platforms, bring-your-own-harness runtimes, model-lab agent APIs, and durable open harnesses; see [Agent execution runtimes](agent-execution-runtimes.md).
- Enterprises are putting control planes (LLM proxies, IdP-managed connector auth) above individual tool harnesses.
- Harness setups are distributed as plugins, skills folders, and cookbooks rather than rebuilt per project.
- Cloud sessions that outlive the laptop, with handoff back to a local checkout, became standard across Claude Code, Devin and Codex in late September 2026.

## Execution runtimes

Where agents actually execute (isolates versus containers, managed-agent platform primitives, bring-your-own-harness microVM runtimes, OpenAI's Agents API, open harnesses such as TrueForge and DSH, and durable cloud-native harnesses such as Pi Durable and Stacklok's Mecatl) now has its own page: [Agent execution runtimes](agent-execution-runtimes.md).

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

- [2026-11-23] Split: "Execution runtimes" and "Durable and cloud-native harnesses" moved to [Agent execution runtimes](agent-execution-runtimes.md), with their Current-status bullets and Recent-changes entries.
- [2026-10-19] Added the OpenAI Agents SDK harness/compute separation (now on [Agent execution runtimes](agent-execution-runtimes.md)), deployment-manifest implementations (deepagents.toml, Agent Collabs, deepagents primitives), and org-embedded agent identity, moved from [Harness (agent)](harness.md).
- [2026-10-19] Page created, split out of [Harness (agent)](harness.md): its "Tooling, protocol, and fleet management" and "Managed platforms, distribution, and evaluation" subsections, the Cloudflare isolates bullet, the cloud-resident-agents paragraph, and the late-March packaging paragraph from "Why it matters", and the Claude Platform GA fact (previously only in Harness's Recent changes).
- [2026-09-30] Cloud-resident agents: Claude Code cloud sessions GA, Devin Cloud in the terminal with two-way `/handoff` and `devin ssh`, Codex cloud environments; Anthropic's "cloud brain, local hands" direction.

## Related

- [Agent execution runtimes](agent-execution-runtimes.md) — sandboxes, isolates, managed-agent primitives, agent APIs, and durable harnesses (split from this page)
- [Harness (agent)](harness.md) — what the harness itself includes and what good harness design looks like; this page covers the runtime, governance, and distribution layer around it
- [Claude Managed Agents](../tools/claude-managed-agents.md) and [Gemini](../tools/gemini.md) — the two leading managed-agent platform implementations
- [Agent Labs vs Model Labs](agent-labs-vs-model-labs.md) — why harness and platform ownership is a competitive moat
- [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md) — the operating patterns run on top of these platforms

## Sources

- [The Code newsletter — 2026-04-22 (Cursor/SpaceX, Claude Code recap, CLI design)](../sources/newsletters/thecode-april-22-2026.md)
- [AINews — 2026-04-22 (GPT-Image-2, Hermes, Deep Research Max)](../sources/newsletters/ainews-2026-04-22.md)
- [Skills and plugin packaging in late March](../sources/newsletters/skills-and-plugin-packaging-late-march.md)
- [Shopify Claude Code fleet patterns — Bessemer conference synthesis](../sources/articles/shopify-claude-code-bessemer-2026-05.md)
- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
- [AINews — OpenAI to reach AGI bar by end-2026](../sources/newsletters/ainews-openai-agi-bar-2026-08-28.md)
- [AINews — OpenAI shuts off Cursor](../sources/newsletters/ainews-openai-shuts-off-cursor-2026-08-29.md)
- [Agent infrastructure, harness engineering, and collaborative agent systems](../sources/newsletters/agent-infrastructure-harness-2026-05-01.md)
- [[AINews] OpenAI reports Navier-Stokes singularity find in 88 hours using Astra-next, roughly 10,000 agents and 130B tokens](../sources/newsletters/ainews-navier-stokes-2026-09-09.md)
- [Claude Tag Slack-native agent launch](../sources/newsletters/claude-tag-slack-agent-2026-06.md)
- [Latent Space — Claude Code's Next Era (Thariq Shihipar)](../sources/newsletters/latent-space-thariq-claude-code-next-era-2026-09-29.md)
- [ClaudeDevs — Cloud sessions out of research preview](../sources/tweets/claudedevs-cloud-sessions-ga-2026-09-23.md)
- [Cognition — Bringing Devin Cloud to your terminal](../sources/articles/devin-cloud-in-your-terminal-2026-09-21.md)
- [AINews — Codex cloud environments](../sources/newsletters/ainews-codex-cloud-environments-2026-09-30.md)
