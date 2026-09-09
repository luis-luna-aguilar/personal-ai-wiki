---
title: Model Context Protocol
type: concept
domains: [agents]
tags: [anthropic]
as_of: 2026-09-07
sources: [anthropic-mcp, legacy-ai-tools-roadmap-xlsx, anthropic-mcp-deployment-surfaces, openai-chatgpt-mcp-surfaces, anthropic-mcp-production-systems, agent-ready-saas-mcp-2026-06, mcp-2026-07-28-stateless-rc, anthropic-acquires-stainless, google-io-agents-agents-agents, ainews-all-model-labs-are-now-agent-labs, amd-acquires-taalas-2026-08-07, lovable-future-of-saas-2026-08-26, cloudflare-os-launch-2026-09-07, femke-plantinga-company-brains-2026-08-27]
---

# Model Context Protocol

Model Context Protocol, usually shortened to MCP, is an open protocol for exposing tools, resources, and prompts to AI hosts and agents through a standard interface. Anthropic introduced it, but the practical significance is broader: MCP turns many bespoke agent integrations into a reusable connector layer.

## Current status (as of 2026-06-29)

- Originated by Anthropic as an open standard for connecting assistants to external systems
- Increasingly treated as shared infrastructure rather than a vendor-specific feature
- Useful for both local and hosted agent systems because it standardizes tool discovery and invocation
- Anthropic's April 2026 guidance sharpens the practical choice: direct APIs fit narrow bespoke integrations, CLIs fit permissive local shell environments, and MCP fits reusable cross-client integrations with richer semantics
- Anthropic also argues that production agents increasingly run in the cloud, which makes remote MCP the compounding integration layer even when mature stacks still ship API, CLI, and MCP surfaces together
- Deployment surface now matters in practice, not just protocol support: Claude Desktop supports local MCP servers on the user's machine, while Anthropic's remote custom connectors are a separate cloud-brokered path
- OpenAI's current MCP docs center on remote MCP servers and connectors, and ChatGPT's current help docs frame user-built integrations as MCP-based apps/connectors rather than localhost-only desktop attachments
- MCP's 2026-07-28 release candidate makes the protocol stateless: no handshake, no session ID, and any request can hit any server instance. The RC also adds first-class extensions (MCP Apps, Tasks), auth hardening, and a formal deprecation policy. AINews reads statelessness as a big operational shift for server operators — easier scaling, simpler load balancing, fewer sticky-session concerns.
- Anthropic acquired Stainless (May 2026) — an SDK/CLI/MCP-server generation platform that Anthropic says hundreds of companies use, and whose former customers include OpenAI and Google per Every — to extend Claude's ability to connect to data and tools. Stainless CEO Alex Rattray had already argued publicly (Every's *AI & I* podcast) for MCP server design principles that make tools legible to agents: keep the tool count small, give tools precise names, and aim for tightly defined outputs.
- OpenAI introduced Agent Plugins (August 2026), an open cross-client standard built with AWS, Cursor, GitHub, and Vercel for packaging Agent Skills and MCP server configs into one shared format, with day-one support across Codex, ChatGPT, Cursor, GitHub Copilot, Kiro, and VS Code — another sign MCP-adjacent packaging is consolidating around shared tooling rather than per-vendor formats.

- **Lovable's "capabilities" pivot (August 2026)** repositions Lovable toward a per-organization orchestrating agent — see [Company brain](company-brain.md) for this pattern in full, including Cloudflare OS and a 9-implementation survey that converged on the same architecture.

## Why it matters

- Replaces one-off tool glue with a protocol-level integration surface
- Lets SaaS vendors expose a compressed, agent-facing product surface: one well-designed MCP server can be easier for agents to use than hundreds of raw API endpoints.
- Makes it easier for ecosystems to share integrations across hosts
- Helps separate the agent harness problem from the underlying model problem
- Complements [Agent2Agent (A2A)](a2a.md): MCP is about how one agent reaches tools and context, A2A is about how one agent delegates and coordinates with another
- It is increasingly not just a transport layer but a design surface: Anthropic now explicitly recommends remote servers, intent-grouped tools, richer semantics like inline UI and elicitation, and skills layered on top of MCP rather than treated as a separate concern
- In practice, MCP strategy now splits into local-first and remote-first deployment. Local MCP is the straightforward path for Claude Desktop; ChatGPT-style custom integrations currently point more toward publicly reachable remote MCP servers or connector/app surfaces

## Recent changes

- [2026-09-07] Split the "company brain" pattern (Lovable's capabilities pivot, plus Cloudflare OS and a 9-implementation survey) out into its own page, [Company brain](company-brain.md), now that three independent examples share the same architecture.
- [2026-08-26] Lovable pivots toward a "company brain" model: published apps expose discrete functions as MCP-callable capabilities, with credentials held server-side by a connector gateway rather than exposed to generated app code — a large, funded production example of MCP compressing a SaaS surface for agents.
- [2026-08-07] OpenAI launched Agent Plugins, an open cross-client standard for packaging Agent Skills and MCP server configs, with day-one support across Codex, ChatGPT, Cursor, GitHub Copilot, Kiro, and VS Code.
- [2026-05-22] MCP 2026-07-28 release candidate makes the protocol stateless (no handshake, no session ID, any request can hit any server instance); adds MCP Apps and Tasks as first-class extensions, auth hardening, and a formal deprecation policy.
- [2026-05-18] Anthropic acquired Stainless, an SDK/MCP-server generation platform used by hundreds of companies including former customers OpenAI and Google, to strengthen Claude's agent-facing developer tooling stack. Price undisclosed by Anthropic; reported by The Information at "north of $300M" via secondary coverage (unverified against a primary figure).

## Sources

- [Anthropic Model Context Protocol launch](../sources/articles/anthropic-mcp.md)
- [AI Tools & Roadmap legacy workbook](../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
- [Anthropic MCP deployment surfaces](../sources/articles/anthropic-mcp-deployment-surfaces.md)
- [OpenAI and ChatGPT MCP surfaces](../sources/articles/openai-chatgpt-mcp-surfaces.md)
- [Building agents that reach production systems with MCP](../sources/articles/anthropic-mcp-production-systems.md)
- [Agent-ready SaaS and MCP surfaces](../sources/newsletters/agent-ready-saas-mcp-2026-06.md)
- [MCP 2026-07-28 release candidate — stateless protocol](../sources/tweets/mcp-2026-07-28-stateless-rc.md)
- [Anthropic acquires Stainless](../sources/articles/anthropic-acquires-stainless.md)
- [Every — Google I/O: Agents, Agents, Agents (Stainless / Rattray)](../sources/newsletters/google-io-agents-agents-agents.md)
- [AINews — All Model Labs are now Agent Labs (MCP RC recap)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
- [AMD acquires Taalas](../sources/newsletters/amd-acquires-taalas-2026-08-07.md)
- [Latent Space — Lovable: The Future of SaaS Is Apps That Agents Can Use](../sources/newsletters/lovable-future-of-saas-2026-08-26.md)
- [Cloudflare — Cloudflare OS: an open platform for agents, apps, and work](../sources/articles/cloudflare-os-launch-2026-09-07.md)
- [Femke Plantinga on X — 9 company-brain architectures compared](../sources/tweets/femke-plantinga-company-brains-2026-08-27.md)
