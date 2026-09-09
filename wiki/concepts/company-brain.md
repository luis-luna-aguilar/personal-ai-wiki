---
title: Company brain
type: concept
domains: [agents]
tags: []
as_of: 2026-09-07
sources: [lovable-future-of-saas-2026-08-26, cloudflare-os-launch-2026-09-07, femke-plantinga-company-brains-2026-08-27]
---

# Company brain

A "company brain" is a per-organization system that gives an agent (or many agents) persistent access to a company's context, tools, and institutional memory, so it can act with the accumulated judgment of the organization rather than starting fresh in every conversation. The pattern is recurring across independent teams building genuinely different systems that converge on the same shape.

## Current status (as of 2026-09-07)

A widely-shared survey of 9 real implementations (Slite's Femke Plantinga, August 2026) found every one doing the same four things: **getting signals** (pulling in new information from connected tools), **remembering** (deciding what's worth keeping), **dreaming & pruning** (periodically reconciling and discarding stale material), and **speaking & searching** (surfacing what it knows back to people and other agents). Named examples: Garry Tan's GBrain (email/calendar into a git repo, nightly re-linking and stale-flagging), mem0 (an explicit-write memory library, ranks fresh over idle facts), Letta (agents decide what's worth keeping; a second agent tidies memory in the background), Zep/Graphiti (a knowledge graph with a clock — facts get an end date instead of being overwritten), Sylph (a content brain living entirely in git; the agent reads human edits to learn what it got wrong), a plain Claude-Code-plus-git DIY setup ("what most engineering teams actually do"), Pletor (a brand brain for marketing, human-gated rule changes), Gorgias Cortex (12,000 markdown nodes, nightly self-correcting PRs from wrong answers), and Slite Agent (watches ~20 connected tools for staleness, routes diffs to page owners, human-approved).

Two larger production examples show the pattern scaling into full platforms rather than personal tools:

- **Lovable's "capabilities" pivot (August 2026):** Lovable ($13.3B valuation) repositions from an app-builder toward a per-organization orchestrating agent. Discrete functions from a published app are exposed as callable tools through a hosted MCP server, so an agent can invoke the function directly instead of a human opening the app; credentials stay server-side in a connector gateway, with per-user permissions preserved via short-lived scoped keys. See [Model Context Protocol](mcp.md) for the protocol layer this depends on.
- **Cloudflare OS (open-sourced August 2026):** a per-person agent workspace combining an isolated code-execution runtime, a new security/governance framework, and a platform for personal, shareable, modifiable apps. Built on a hard lesson from its own internal-only first version: MCP-server tool access alone tells you which tools an agent can call, not which underlying resources it has *observed* — so sharing a dashboard built from sensitive data could otherwise leak that data to someone who couldn't access it directly. Cloudflare's fix, Gatekeepers (service-specific proxies that hold credentials, enforce fine-grained policy, and log every read), plus an observation log that follows data through everything an agent later produces from it, so downstream sharing and cross-agent handoffs get checked against what was actually observed, not just what tool was called. Every generated app runs as its own lightweight Worker with independent state; sharing a "blueprint" gives someone your app's code without your data, conversation history, or credentials.

## Why it matters

The four-function convergence (signals, memory, pruning, retrieval) suggests "company brain" is becoming a recognizable architecture pattern, not just a marketing label — worth watching as a distinct concept from [MCP](mcp.md) (the tool-exposure protocol several of these systems use) and from general [agent memory](agent-memory.md) (the lifecycle mechanics one layer of a company brain implements).

## Recent changes

- [2026-09-07] Page created, split out of a single bullet on [MCP](mcp.md) once Cloudflare OS and a 9-implementation survey joined Lovable's capabilities pivot as independent examples of the same pattern.

## Related

- [Model Context Protocol](mcp.md) — the tool-exposure protocol Lovable's capabilities and several company-brain implementations build on
- [Agent memory](agent-memory.md) — the lifecycle mechanics (extraction, dedupe, retrieval, staleness) that "remembering" and "dreaming & pruning" implement

## Sources

- [Latent Space — Lovable: The Future of SaaS Is Apps That Agents Can Use](../sources/newsletters/lovable-future-of-saas-2026-08-26.md)
- [Cloudflare — Cloudflare OS: an open platform for agents, apps, and work](../sources/articles/cloudflare-os-launch-2026-09-07.md)
- [Femke Plantinga on X — 9 company-brain architectures compared](../sources/tweets/femke-plantinga-company-brains-2026-08-27.md)
