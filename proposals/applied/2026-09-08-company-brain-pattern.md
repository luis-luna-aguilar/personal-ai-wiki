---
type: proposal
sources:
  - raw/articles/2026-09-07-blogcloudflarecom-cloudflare-os.md
  - raw/tweets/2026-09-07-femke_plantinga-2092918452423983363.md
status: pending
created: 2026-09-08
---

# Proposal: The "company brain" pattern keeps multiplying

## Summary

### The source

Cloudflare open-sourced a new version of **Cloudflare OS**, a per-person agent workspace grounded in a company's own context and skills, built from three parts: an agent workspace with an isolated code-execution runtime; a new security/governance framework (Gatekeepers — service-specific proxies that hold credentials, enforce policy, and record what an agent has read; an observation log that follows data even after an agent turns it into a shared dashboard, so sharing the dashboard can't leak the underlying resource to someone unauthorized); and a platform for personal, modifiable apps that anyone can build and share, each running as its own lightweight Worker with independent state. Cloudflare rebuilt from an internal-only first version after finding that plain MCP-server tool access wasn't enough — it tells you which tools an agent can call, not which underlying resources it has *observed*, which broke naive workspace-sharing once people started actually sharing apps and outputs. Separately, a widely-shared tweet thread from Slite's Femke Plantinga surveyed nine real "company brain" implementations in production — Garry Tan's GBrain, mem0, Letta, Zep/Graphiti, a git-only content system called Sylph, a plain Claude-Code-plus-git DIY setup ("what most engineering teams actually do"), a brand-asset system called Pletor, Gorgias's in-house Cortex (12,000 markdown nodes, nightly self-correcting PRs), and Slite's own Agent — and found every one of them doing the same four things: getting signals, remembering, dreaming and pruning, and speaking and searching.

### What changes

`concepts/mcp.md` already carries a bullet on Lovable's "capabilities"/company-brain pivot from the prior digest. With Cloudflare OS and this nine-implementation survey, there are now three independent, structurally similar examples of the same pattern — enough, this proposal argues, to justify pulling "company brain" out into its own concept page rather than letting it keep growing as a single bullet on the MCP page. This proposal creates `concepts/company-brain.md`, trims the MCP page's Lovable bullet down to a one-line cross-link, and adds a Recent-changes entry to `concepts/mcp.md` noting the move.

### What to weigh

This is the clearest restructuring judgment call in this batch, flagged below: the alternative is simply continuing to grow the MCP-page bullet with each new example, which is less disruptive but risks the MCP page accumulating content that isn't really about the protocol itself. Splitting out now, while there are only three examples, is a bet that this pattern keeps recurring; if it turns out to be a one-off cluster, the new page will look thin.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Create** `wiki/concepts/company-brain.md` — three independent examples (Lovable, Cloudflare OS, the 9-implementation survey) justify splitting this out of `concepts/mcp.md`
    > See draft below

- [ ] **Update** `wiki/concepts/mcp.md` — trim the Lovable "capabilities" bullet to a cross-link, add Recent-changes entry noting the split
    > See draft below

- [ ] **Create** `wiki/sources/articles/cloudflare-os-launch-2026-09-07.md` — source summary

- [ ] **Create** `wiki/sources/tweets/femke-plantinga-company-brains-2026-08-27.md` — source summary

## Page drafts

### wiki/concepts/company-brain.md (new)

```md
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
```

### wiki/concepts/mcp.md (updated)

```md
---
as_of: 2026-09-07
sources: [..., cloudflare-os-launch-2026-09-07, femke-plantinga-company-brains-2026-08-27]
---

## Current status (as of 2026-06-29)

(... existing bullets unchanged, EXCEPT replace the Lovable bullet with: ...)

- **Lovable's "capabilities" pivot (August 2026)** repositions Lovable toward a per-organization orchestrating agent — see [Company brain](company-brain.md) for this pattern in full, including Cloudflare OS and a 9-implementation survey that converged on the same architecture.

## Recent changes

- [2026-09-07] Split the "company brain" pattern (Lovable's capabilities pivot, plus Cloudflare OS and a 9-implementation survey) out into its own page, [Company brain](company-brain.md), now that three independent examples share the same architecture.
- (... existing entries follow ...)
```

### wiki/sources/articles/cloudflare-os-launch-2026-09-07.md (new)

```md
---
title: "Cloudflare OS: an open platform for agents, apps, and work"
type: source
source_type: article
source_file: raw/articles/2026-09-07-blogcloudflarecom-cloudflare-os.md
url: https://blog.cloudflare.com/cloudflare-os/
ingested: 2026-09-08
domains: [agents]
---

# Cloudflare OS: an open platform for agents, apps, and work

Cloudflare open-sources a rebuilt version of Cloudflare OS: a per-person agent workspace with an isolated execution runtime, a Gatekeeper-based security/governance framework tracking what agents have observed, and a platform for personal, shareable, modifiable apps.

## Influenced pages

- [Company brain](../../concepts/company-brain.md) — full architecture description

## Key claims extracted

- Three parts: agent workspace, security/governance framework (Gatekeepers, observation log), personal-app platform
- Rebuilt because plain MCP tool-access control doesn't track what an agent has *observed*, only which tools it can call
- Every app runs as an independent lightweight Worker; sharing a "blueprint" gives code without data/credentials
- Available today, open source, deployable into any Cloudflare account
```

### wiki/sources/tweets/femke-plantinga-company-brains-2026-08-27.md (new)

```md
---
title: "Femke Plantinga on X: \"Everyone's suddenly building company brains\""
type: source
source_type: tweet
source_file: raw/tweets/2026-09-07-femke_plantinga-2092918452423983363.md
url: https://x.com/femke_plantinga/status/2092918452423983363?s=12
published: 2026-08-27
ingested: 2026-09-08
domains: [agents]
---

# Femke Plantinga — 9 "company brain" architectures compared

A survey (via Slite) of 9 real "company brain" implementations, finding every one does the same four things: getting signals, remembering, dreaming & pruning, speaking & searching.

## Influenced pages

- [Company brain](../../concepts/company-brain.md) — the 9-implementation survey and its four-function framing

## Key claims extracted

- 9 named examples: GBrain, mem0, Letta, Zep/Graphiti, Sylph, DIY (Claude Code + git), Pletor, Gorgias Cortex, Slite Agent
- Common architecture: getting signals, remembering, dreaming & pruning, speaking & searching
- Companion free ebook with architecture notes from 149 real teams
```
