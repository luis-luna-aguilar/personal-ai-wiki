---
title: Company brain
type: concept
domains: [agents]
tags: [knowledge-cluster]
as_of: 2026-09-09
sources: [lovable-future-of-saas-2026-08-26, cloudflare-os-launch-2026-09-07, femke-plantinga-company-brains-2026-08-27, cerebras-knowledge-base, dhravyashah-supermemory-company-brain-2026-07-28]
---

# Company brain

A "company brain" is a per-organization system that gives an agent (or many agents) persistent access to a company's context, tools, and institutional memory, so it can act with the accumulated judgment of the organization rather than starting fresh in every conversation. The pattern is recurring across independent teams building genuinely different systems that converge on the same shape. In the [Knowledge architectures](knowledge-architectures.md) matrix it is the organization-scope *system*, not a single store: it contains a [knowledge layer](knowledge-layer.md) (compiled content), [agent memory](agent-memory.md) (what agents learned), tool access (often through [MCP](mcp.md)), and a refresh loop.

## Also called

Org brain, GBrain (Garry Tan's implementation), "the agent's brain" (Every's phrasing for interconnected Notion databases), content brain and brand brain (function-scope instances limited to marketing).

## Current status (as of 2026-09-09)

A widely-shared survey of 9 real implementations (Slite's Femke Plantinga, August 2026) found every one doing the same four things: **getting signals** (pulling in new information from connected tools), **remembering** (deciding what's worth keeping), **dreaming & pruning** (periodically reconciling and discarding stale material), and **speaking & searching** (surfacing what it knows back to people and other agents). Named examples: Garry Tan's GBrain (email/calendar into a git repo, nightly re-linking and stale-flagging), mem0 (an explicit-write memory library, ranks fresh over idle facts), Letta (agents decide what's worth keeping; a second agent tidies memory in the background), Zep/Graphiti (a knowledge graph with a clock — facts get an end date instead of being overwritten), Sylph (a content brain living entirely in git; the agent reads human edits to learn what it got wrong), a plain Claude-Code-plus-git DIY setup ("what most engineering teams actually do"), Pletor (a brand brain for marketing, human-gated rule changes), Gorgias Cortex (12,000 markdown nodes, nightly self-correcting PRs from wrong answers), and Slite Agent (watches ~20 connected tools for staleness, routes diffs to page owners, human-approved).

Four larger production examples show the pattern scaling into full platforms rather than personal tools:

- **Supermemory Company Brain (July 2026):** Supermemory — until now tracked here only via its underlying [agent memory](agent-memory.md) tech — packaged a full company-brain product: invite its bot into a Slack workspace and it backfills up to three months of channel history plus whatever tools get connected, then answers sales/engineering/HR/research questions, tags other bots to execute work, and runs scheduled automations (e.g. a daily priority brief); a companion plugin carries the same knowledge outside Slack into Claude Code, Codex, and other tools. Vendor self-report via the founder's own X Article — no independent verification.
- **Lovable's "capabilities" pivot (August 2026):** Lovable ($13.3B valuation) repositions from an app-builder toward a per-organization orchestrating agent. Discrete functions from a published app are exposed as callable tools through a hosted MCP server, so an agent can invoke the function directly instead of a human opening the app; credentials stay server-side in a connector gateway, with per-user permissions preserved via short-lived scoped keys. See [Model Context Protocol](mcp.md) for the protocol layer this depends on.
- **Cloudflare OS (open-sourced August 2026):** a per-person agent workspace combining an isolated code-execution runtime, a new security/governance framework, and a platform for personal, shareable, modifiable apps. Built on a hard lesson from its own internal-only first version: MCP-server tool access alone tells you which tools an agent can call, not which underlying resources it has *observed* — so sharing a dashboard built from sensitive data could otherwise leak that data to someone who couldn't access it directly. Cloudflare's fix, Gatekeepers (service-specific proxies that hold credentials, enforce fine-grained policy, and log every read), plus an observation log that follows data through everything an agent later produces from it, so downstream sharing and cross-agent handoffs get checked against what was actually observed, not just what tool was called. Every generated app runs as its own lightweight Worker with independent state; sharing a "blueprint" gives someone your app's code without your data, conversation history, or credentials.
- **Cerebras Knowledge:** an internal tool fielding 15,000+ questions/day three months after launch, built around one shared Postgres table of embeddings, summaries, and metadata fed by per-source connectors (Slack, wiki/Confluence, code repos, netlists, custom databases) so anything ingested is immediately queryable through the same interface. Retrieval fuses six parallel search lists — full-text, embedding, thread-summary, code-graph, wiki-vector, and Slack full-text — with reciprocal rank fusion before a small reranker model picks the final top ten. The same retrieval primitives are exposed as narrow, LLM-free MCP tools (search, search_slack, search_code, who_knows) rather than one black-box "answer this question" endpoint, so Claude Code or any MCP client owns the orchestration itself; "projects" scope a user's default search to their team's own sources instead of the whole company corpus.

## Why it matters

The four-function convergence (signals, memory, pruning, retrieval) suggests "company brain" is becoming a recognizable architecture pattern, not just a marketing label. It is worth tracking as its own concept because it is the *composition*: [MCP](mcp.md) is the tool-exposure protocol several of these systems use, [agent memory](agent-memory.md) is the lifecycle mechanics behind "remembering" and "dreaming & pruning", and the [knowledge layer](knowledge-layer.md) is the compiled content that "speaking & searching" serves. None of those three alone is a company brain.

## Recent changes

- [2026-09-09] Added Cerebras Knowledge as a production example: one shared Postgres embeddings table across Slack/wiki/code/custom sources, six-way retrieval fusion via reciprocal rank fusion, and narrow LLM-free MCP tools that let the calling client (e.g. Claude Code) own orchestration instead of one black-box answer endpoint.
- [2026-09-09] Terminology reorganization: added the `## Also called` alias line, stated the page's position in the new [Knowledge architectures](knowledge-architectures.md) hub (an organization-scope system composed of a knowledge layer, agent memory, and tool access), and rewrote the Related lines to agree with it.
- [2026-09-07] Page created, split out of a single bullet on [MCP](mcp.md) once Cloudflare OS and a 9-implementation survey joined Lovable's capabilities pivot as independent examples of the same pattern.
- [2026-07-28] Added Supermemory Company Brain as a production example: a Slack-resident bot built on Supermemory's agent-memory tech, with cross-tool (Claude Code/Codex) access and scheduled automations. Vendor self-report via the founder's X Article, no independent verification.

## Related

- [Knowledge architectures](knowledge-architectures.md) — the hub that places this page against knowledge layers, agent memory, and ontologies
- [Knowledge layer](knowledge-layer.md) — the compiled, human-legible content a company brain serves; GBrain's git repo and Gorgias Cortex's markdown nodes are knowledge layers
- [Agent memory](agent-memory.md) — the per-agent lifecycle mechanics (extract, dedupe, reconcile, expire) behind "remembering" and "dreaming & pruning"
- [Model Context Protocol](mcp.md) — the tool-exposure protocol Lovable's capabilities and several company-brain implementations build on

## Sources

- [Latent Space — Lovable: The Future of SaaS Is Apps That Agents Can Use](../sources/newsletters/lovable-future-of-saas-2026-08-26.md)
- [Cloudflare — Cloudflare OS: an open platform for agents, apps, and work](../sources/articles/cloudflare-os-launch-2026-09-07.md)
- [Femke Plantinga on X — 9 company-brain architectures compared](../sources/tweets/femke-plantinga-company-brains-2026-08-27.md)
- [Cerebras — How We Built Our Knowledge Base](../sources/articles/cerebras-knowledge-base.md)
- [Dhravya Shah on X — How to Build Your Company Brain in 5 Minutes](../sources/tweets/dhravyashah-supermemory-company-brain-2026-07-28.md)
