---
type: proposal
source: raw/newsletters/2026-05-20-anthropic-is-onto-something.md
status: pending
created: 2026-08-25
---

# Proposal: Anthropic agent infrastructure — sandboxes, MCP tunnels, Stainless acquisition, and the harness/agent-labs thesis

## Summary

### The source

On 20 May 2026, at Code with Claude London, Anthropic gave Claude Managed Agents **self-hosted sandboxes** (public beta): tool execution can run on the customer's servers or on Cloudflare, Daytona, Modal or Vercel while Anthropic still runs the agent loop. Alongside came **MCP tunnels** (research preview), a customer-deployed gateway that reaches private MCP servers over a single outbound connection, with no firewall ports opened. Two days earlier Anthropic bought Stainless, an SDK/CLI/MCP-server generator; no price was given — the "north of $300M" figure is The Information's, via Every.

MCP maintainer David Soria Parra announced the "2026-07-28" release candidate (a version label, not a date): the protocol goes stateless — no handshake, no session ID, any request can hit any server — and gains MCP Apps, Tasks, hardened auth and a deprecation policy. AINews framed the week with Greg Brockman's "the model alone is no longer the product", AI21 shutting its model team to pivot to agents, and DeepSeek building its first harness team. Also in the mix: the "Code as Agent Harness" survey (code as the medium linking agent reasoning, action and environment) and Cameron Wolfe's rule to go multi-agent only when tool sprawl forces it.

### What changes

The wiki knew about Managed Agents' hosted sandboxes and the Agent Labs thesis, but nothing on self-hosted execution, tunnels, Stainless or MCP's protocol history.

- **Claude Managed Agents** gains two status bullets and a Recent-changes entry; page date moves from 13 May to 20 May.
- **Harness** extends its platform-primitives bullet, which cited only Google's Gemini API, with Anthropic's split, and adds a code-as-substrate bullet from the survey. Two Recent-changes entries; the list is re-sorted. Date stays 8 July.
- **Model Context Protocol** gains the stateless RC and the Stainless deal (plus Alex Rattray's tool-design principles) and its first Recent changes section; the status heading is corrected to the page's existing 29 June date.
- **Agent Labs vs Model Labs** gains an evidence section — the Brockman/AI21/DeepSeek items plus swyx's counterpoint that harness–model co-training works *against* model neutrality — and its first Recent changes section. Date stays 11 June.
- **Agentic orchestration patterns** gains the single-agent-first pattern. Its Recent-changes list is at the ten-entry cap and the new entry is the oldest by date, so it goes straight to history; the existing ten stay, re-sorted. No leader lines or schema touched.
- Nine new source pages: three articles, two tweets, four newsletters.

### What to weigh

Both tweet source pages are thin: the fetches returned Substack redirects, so the text comes from the AINews recap, the URLs are profiles not permalinks, and the 22 May dates are inferred from the AINews issue. The Stainless price is secondary-only yet lands on the MCP page, caveated — decide whether it belongs. The spill rule archives this proposal's own orchestration entry; to keep it live, spill the 29 May entry instead (both orchestration drafts change).

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/tools/claude-managed-agents.md` — add self-hosted sandboxes (public beta) + MCP tunnels (research preview); bump `as_of` 2026-05-13 → 2026-05-20 and re-date the `## Current status` heading to match; add both new source ids to frontmatter and `## Sources`
    > See draft below

- [x] **Update** `wiki/concepts/harness.md` — extend the managed-agent-platform-primitives pattern with Anthropic's sandbox/tunnel split; add the "Code as Agent Harness" survey as a reinforcing framing
    > See draft below

- [x] **Update** `wiki/concepts/mcp.md` — add the MCP 2026-07-28 stateless release candidate and the Stainless acquisition; re-date the `## Current status` heading 04-23 → 06-29 to match the page's existing `as_of`; add a `## Recent changes` section (page currently has none); add all four new source ids to `## Sources`
    > See draft below

- [x] **Update** `wiki/concepts/agent-labs-vs-model-labs.md` — add Brockman/AI21/DeepSeek evidence that the Agent Labs thesis is accelerating; add a `## Recent changes` section (page currently has none)
    > See draft below

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — add a single-agent-first escalation-threshold pattern; re-sort the existing `## Recent changes` list newest-first (no entries added or removed on the live page — see Spill)
    > See draft below

- [x] **Spill** `wiki/workflows/agentic-orchestration-patterns.md` → `wiki/history/workflows/agentic-orchestration-patterns.md` — page is already at the 10-entry cap (confirmed by fresh read); the new `[2026-05-22]` entry would make 11 and is the oldest by date of the 11, so it is the one spilled: appended directly to history under the existing `## Archived from current page on 2026-08-25` header (verified present), and the `[2026-06-24]` token-tightening entry stays on the live page
    > See draft below

- [x] **Create** `wiki/sources/articles/anthropic-acquires-stainless.md` — source summary for Anthropic's official acquisition announcement

- [x] **Create** `wiki/sources/articles/claude-managed-agents-updates-2026-05.md` — source summary for Anthropic's self-hosted-sandboxes/MCP-tunnels blog post

- [x] **Create** `wiki/sources/articles/code-as-agent-harness-paper.md` — source summary for the arXiv survey

- [x] **Create** `wiki/sources/tweets/mcp-2026-07-28-stateless-rc.md` — source summary for the MCP maintainer's RC announcement

- [x] **Create** `wiki/sources/tweets/brockman-model-not-product.md` — source summary for Greg Brockman's tweet

- [x] **Create** `wiki/sources/newsletters/anthropic-is-onto-something.md` — source summary for The Code newsletter (2026-05-20)

- [x] **Create** `wiki/sources/newsletters/google-io-agents-agents-agents.md` — source summary for Every's newsletter (2026-05-20)

- [x] **Create** `wiki/sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md` — source summary for AINews (2026-05-23)

- [x] **Create** `wiki/sources/newsletters/ainews-new-ai-infra-unicorns-exa-modal-turbop.md` — source summary for AINews (2026-05-22), scoped only to the single-agent-first orchestration item

## Page drafts

### wiki/tools/claude-managed-agents.md (updated)

```md
---
title: Claude Managed Agents
type: tool
domains: [agents]
subcategory: agent-orchestration
tags: [anthropic, closed-source, agentic]
as_of: 2026-05-20
sources: [managed-agents, every-managed-agents-vibe-check, anthropic-platform-expansion-april-2026, claude-managed-agents-memory, anthropic-spacex-dreams-2026-05-07, claude-managed-agents-feature-parity-2026-05-13, claude-managed-agents-updates-2026-05, anthropic-is-onto-something]
---
```

Rename the status heading so it tracks the bumped `as_of` (the live page currently has both at 2026-05-13):

```md
## Current status (as of 2026-05-20)
```

Append to the end of that bullet list:

```md
- **Self-hosted sandboxes** (public beta, announced at Code with Claude London, May 2026): tool execution can run on the customer's own infrastructure or through a supported managed provider (Cloudflare, Daytona, Modal, Vercel), while Anthropic's hosted agent loop — orchestration, context management, error recovery — stays on Anthropic's side. Sensitive files, packages, and services never leave the customer's perimeter; the customer controls compute sizing and the runtime image.
- **MCP tunnels** (research preview): let Managed Agents reach MCP servers inside a private network without exposing them to the public internet. A lightweight gateway the customer deploys makes a single outbound connection — no inbound firewall rules, no public endpoints, traffic encrypted end to end. Supported in both Managed Agents and the Messages API; managed from Claude Console workspace settings by org admins.
```

Add to `## Recent changes` (new top entry):

```md
- [2026-05-20] Anthropic shipped self-hosted sandboxes (public beta) and MCP tunnels (research preview): tool execution can run on customer infrastructure or through Cloudflare/Daytona/Modal/Vercel while Anthropic keeps the orchestration loop; MCP tunnels reach private MCP servers without exposing them publicly.
```

Add to `## Sources` (one link per new frontmatter source id):

```md
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [The Code — Anthropic is onto something (2026-05-20)](../sources/newsletters/anthropic-is-onto-something.md)
```

### wiki/concepts/harness.md (updated)

Frontmatter `sources:` list — append `claude-managed-agents-updates-2026-05, code-as-agent-harness-paper` (as_of stays 2026-07-08; this new content is older than the page's current newest claim).

Update the existing "Managed-agent platform primitives" bullet under `## What good harness engineering looks like` (append a sentence, rest of bullet unchanged):

```md
- **Managed-agent platform primitives.** Hosted agent platforms are absorbing work that custom harnesses used to implement manually: tool connectivity through MCP, background execution, custom function calling, credential refresh, stateful interaction APIs, and sandboxed execution. Google adding these to the Gemini API is another sign that "harness" is becoming product infrastructure, not only application code. Anthropic's Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview) in May 2026: the agent loop that handles orchestration, context management, and error recovery stays on Anthropic's infrastructure, while tool execution and private MCP connectivity run on customer-controlled infrastructure or a supported sandbox provider (Cloudflare, Daytona, Modal, Vercel).
```

Add a new bullet at the end of the same list:

```md
- **Code as the operational substrate, not just output.** A May 2026 survey ("Code as Agent Harness," arXiv:2605.18747) frames code as the shared medium connecting agent reasoning, acting, and environment modeling — not merely the artifact an agent produces. It organizes harness design around three layers: the interface where code links reasoning/action/environment; harness mechanisms (planning, memory, tool use, feedback-driven control); and scaling from single-agent to multi-agent settings, where shared code artifacts support coordination, review, and verification.
```

Replace the whole `## Recent changes` list. The live list is not in date order (05-30, 07-08, 06-22, 07-01, 07-03, 06-24, 06-05); the two new entries are added and the nine entries are re-sorted newest-first, wording of the existing seven unchanged:

```md
## Recent changes

- [2026-07-08] Gemini API managed agents add hosted harness primitives: MCP support, background execution, custom function calling, credential refresh, and stateful agent interactions.
- [2026-07-03] Added control-layer framing from AI Engineer World Fair: permissions, cost ceilings, recovery, and review routing are part of the harness boundary.
- [2026-07-01] Added agent recipes as a harness packaging pattern: model choices, evals, judges, human expertise, failure history, and signal processing bundled with the workflow.
- [2026-06-24] Claude Tag coverage adds org-embedded agent identity, permission scoping, and Slack-channel memory boundaries as harness concerns.
- [2026-06-22] Gray Swan security coverage adds prompt injection, exfiltration, identity, permissions, and automated red teaming as harness-boundary concerns for tool-using agents.
- [2026-06-05] Added RL harness quality section: 8 failure modes taxonomy from Auriel W (Google Gemini RL team); "5% failure rate = harness problem, not model problem"
- [2026-05-30] Added Effective Feedback Compute and model-specific harness profiles as harness-quality signals beyond token/tool counts.
- [2026-05-20] Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview), extending the harness security boundary so tool execution and private MCP connectivity can run on customer infrastructure while Anthropic keeps the orchestration loop.
- [2026-05-18] "Code as Agent Harness" survey (arXiv:2605.18747) frames code as the operational substrate for agent reasoning, planning, memory, tool use, and multi-agent coordination.
```

Add to `## Sources`:

```md
- [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](../sources/articles/claude-managed-agents-updates-2026-05.md)
- [Code as Agent Harness (arXiv:2605.18747)](../sources/articles/code-as-agent-harness-paper.md)
```

### wiki/concepts/mcp.md (updated)

Frontmatter `sources:` list — append `mcp-2026-07-28-stateless-rc, anthropic-acquires-stainless, google-io-agents-agents-agents, ainews-all-model-labs-are-now-agent-labs` (as_of stays 2026-06-29; this new content is older than the page's current newest claim).

Re-date the status heading to match the page's existing frontmatter `as_of` (the live page says 04-23 while `as_of` is already 06-29; the new bullets are May-dated, so 06-29 remains the newest claim):

```md
## Current status (as of 2026-06-29)
```

Append to that bullet list:

```md
- MCP's 2026-07-28 release candidate makes the protocol stateless: no handshake, no session ID, and any request can hit any server instance. The RC also adds first-class extensions (MCP Apps, Tasks), auth hardening, and a formal deprecation policy. AINews reads statelessness as a big operational shift for server operators — easier scaling, simpler load balancing, fewer sticky-session concerns.
- Anthropic acquired Stainless (May 2026) — an SDK/CLI/MCP-server generation platform that Anthropic says hundreds of companies use, and whose former customers include OpenAI and Google per Every — to extend Claude's ability to connect to data and tools. Stainless CEO Alex Rattray had already argued publicly (Every's *AI & I* podcast) for MCP server design principles that make tools legible to agents: keep the tool count small, give tools precise names, and aim for tightly defined outputs.
```

Add a new `## Recent changes` section (page currently has none), inserted between `## Why it matters` and `## Sources`:

```md
## Recent changes

- [2026-05-22] MCP 2026-07-28 release candidate makes the protocol stateless (no handshake, no session ID, any request can hit any server instance); adds MCP Apps and Tasks as first-class extensions, auth hardening, and a formal deprecation policy.
- [2026-05-18] Anthropic acquired Stainless, an SDK/MCP-server generation platform used by hundreds of companies including former customers OpenAI and Google, to strengthen Claude's agent-facing developer tooling stack. Price undisclosed by Anthropic; reported by The Information at "north of $300M" via secondary coverage (unverified against a primary figure).
```

Add to `## Sources` (one link per new frontmatter source id):

```md
- [MCP 2026-07-28 release candidate — stateless protocol](../sources/tweets/mcp-2026-07-28-stateless-rc.md)
- [Anthropic acquires Stainless](../sources/articles/anthropic-acquires-stainless.md)
- [Every — Google I/O: Agents, Agents, Agents (Stainless / Rattray)](../sources/newsletters/google-io-agents-agents-agents.md)
- [AINews — All Model Labs are now Agent Labs (MCP RC recap)](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
```

### wiki/concepts/agent-labs-vs-model-labs.md (updated)

Frontmatter `sources:` list — append `brockman-model-not-product, ainews-all-model-labs-are-now-agent-labs` (as_of stays 2026-06-11; this new content is older than the page's current newest claim).

Add a new section after `## Relationship to model sovereignty` and before `## Sources`:

```md
## Evidence the shift is accelerating (May 2026)

- OpenAI President Greg Brockman: "the model alone is no longer the product" — AINews calls this a big reversal from a stance held almost uniformly by "Team Big Model" veterans, Brockman included.
- AI21 shuttered its model team and is pivoting to agents (per AINews).
- Even DeepSeek is building a "harness team" for the first time (per AINews).
- AINews (swyx) adds a counterpoint to the model-neutrality implication above: a lab that co-trains its model with its own harness can post-train the model to perform well only inside its closed agent, funnelling users toward that agent at the expense of its model/API business — a force that works *against* model neutrality.

## Recent changes

- [2026-05-22] Greg Brockman's "the model alone is no longer the product," AI21 shuttering its model team for an agents pivot, and DeepSeek building its first harness team reinforce the Agent Labs framing — even historically model-only labs are absorbing harness work.
```

Add to `## Sources`:

```md
- [Greg Brockman: "the model alone is no longer the product"](../sources/tweets/brockman-model-not-product.md)
- [AINews — All Model Labs are now Agent Labs](../sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md)
```

### wiki/workflows/agentic-orchestration-patterns.md (updated)

Frontmatter `sources:` list — append `ainews-new-ai-infra-unicorns-exa-modal-turbop` (as_of stays 2026-07-14; this new content is older than the page's current newest claim).

Add a new bullet to `## Current patterns`, placed after the existing "Coordinator-specialist routing" bullet:

```md
- **Single-agent-first escalation threshold.** Start with a single-agent system and only introduce manager/sub-agent or decentralized multi-agent topologies once tool sprawl or prompt bloat makes the single-agent design unmanageable — treat multi-agent orchestration as an escalation, not a default starting architecture. *Source: Cameron Wolfe (@cwolferesearch) synthesis via AINews, May 2026*
```

`## Recent changes`: the page is at the 10-entry cap and this ingest's entry is dated 2026-05-22, older than every existing entry, so it is the one that spills (see the history draft below) and no entry is added to or removed from the live page. Replace the list with the same ten entries re-sorted newest-first (the live order is 07-14, 06-29, 06-18, 05-29, 07-08, 07-08, 07-06, 07-04, 06-26, 06-24; wording unchanged):

```md
## Recent changes

- [2026-07-14] Expanded Agentic MapReduce from a passing mention into a full pattern entry: deterministic Plan/Shard/Map/Reduce (+Verify for Security Swarm) architecture, sourced from Cognition's engineering writeup, with three supporting whole-codebase-agent-limits research citations.
- [2026-07-08] Added loop-tempo selection from Andy Matuschak: fast controlled loops and slow delegated loops are easier to sustain than mid-speed partial-control loops.
- [2026-07-08] Linked PR review artifacts and repo-local review standards to the dedicated AI PR/code-review workflow.
- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.
- [2026-07-04] Dhinakaran and Seldo map loop discourse into execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops; they emphasize exit signals and per-loop autonomy dials.
- [2026-06-29] Added Sidekick multi-model harness pattern: persistent frontier + cheaper sidekick agents, cache-aware mid-session model switching at compaction boundaries; contrasted with per-call advisor/smart-friend escalation.
- [2026-06-26] Added AI review standards and review-noise failure mode from code-review workflow coverage.
- [2026-06-24] Token-tightening coverage adds AI FinOps controls: budgets, model routing, prompt caching, cheaper defaults, checkpoints, and outcome-based spend review.
- [2026-06-18] Every case studies add scripted-subagent orchestration as a practical Dynamic Workflows reliability pattern.
- [2026-05-29] Every updated compound engineering from a four-step loop to an eight-step loop that explicitly includes ideation and polish around the agentic work phase.
```

Add to `## Sources`:

```md
- [AINews — New AI infra unicorns: Exa, Modal, Turbopuffer](../sources/newsletters/ainews-new-ai-infra-unicorns-exa-modal-turbop.md)
```

### wiki/history/workflows/agentic-orchestration-patterns.md (updated)

Append to the existing `## Archived from current page on 2026-08-25` section (verified present; it currently holds three entries from an earlier same-day spill — append as a fourth bullet rather than creating a second dated header, and do not re-sort the existing history bullets):

```md
- [2026-05-22] Added single-agent-first escalation threshold: start single-agent, only add manager/sub-agent or decentralized multi-agent topologies once tool sprawl or prompt bloat becomes unmanageable (Cameron Wolfe synthesis via AINews).
```

### wiki/sources/articles/anthropic-acquires-stainless.md (new)

```md
---
title: Anthropic acquires Stainless
type: source
source_type: article
source_file: raw/articles/2026-08-25-anthropiccom-news-anthropic-acquires-stainless.md
url: https://www.anthropic.com/news/anthropic-acquires-stainless
published: 2026-05-18
ingested: 2026-08-25
domains: [agents]
---

# Anthropic acquires Stainless

Anthropic's official announcement confirming it acquired Stainless, an SDK/CLI/MCP-server generation platform founded in 2022 that has powered every official Anthropic SDK since the early API days and that Anthropic says hundreds of companies rely on. Anthropic frames the deal as extending Claude's ability to connect to data and tools. The announcement does not disclose a purchase price and does not name other Stainless customers.

## Influenced pages
- [Model Context Protocol](../../concepts/mcp.md) — added the acquisition and its tie to MCP-server design legibility

## Key claims extracted
- Acquisition announced 2026-05-18
- Stainless founded 2022; generates SDKs (TypeScript, Python, Go, Java, etc.), CLIs, and MCP servers from an API spec; "hundreds of companies" rely on it
- Anthropic states the goal is to "advance Claude's ability to connect to data and tools"
- No purchase price disclosed by Anthropic. The "north of $300 million" figure and the "former customers include OpenAI and Google" detail both come from Every's newsletter (citing The Information), not from this announcement — see the Every source page
```

### wiki/sources/articles/claude-managed-agents-updates-2026-05.md (new)

```md
---
title: "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels"
type: source
source_type: article
source_file: raw/articles/2026-08-25-claudecom-blog-claude-managed-agents-updates.md
url: https://claude.com/blog/claude-managed-agents-updates
published: 2026-05-20
ingested: 2026-08-25
domains: [agents]
---

# New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Anthropic's official Claude Managed Agents blog post announcing two features unveiled at Code with Claude London: self-hosted sandboxes (public beta) and MCP tunnels (research preview). Self-hosted sandboxes let a Managed Agent execute tools on the customer's own infrastructure or a supported managed provider (Cloudflare, Daytona, Modal, Vercel) while Anthropic's hosted agent loop still handles orchestration, context management, and error recovery. MCP tunnels let agents reach MCP servers inside a private network — via a lightweight customer-deployed gateway — without exposing them to the public internet.

## Influenced pages
- [Claude Managed Agents](../../tools/claude-managed-agents.md) — added self-hosted sandboxes and MCP tunnels to current status
- [Harness (agent)](../../concepts/harness.md) — extended the managed-agent-platform-primitives pattern with this example

## Key claims extracted
- Self-hosted sandboxes: public beta; MCP tunnels: research preview (request access via a Claude form)
- Supported sandbox providers: Cloudflare, Daytona, Modal, Vercel; named customer examples for three of them — Amplitude (Cloudflare), Clay (Daytona), Rogo (Vercel)
- Sandbox provisioning, resource sizing, and runtime image are controlled by the customer
- MCP tunnels supported in both Managed Agents and the Messages API; managed from Claude Console workspace settings by org admins
- No inbound firewall rules or public endpoints required for MCP tunnels; traffic is encrypted end to end
```

### wiki/sources/articles/code-as-agent-harness-paper.md (new)

```md
---
title: "Code as Agent Harness"
type: source
source_type: article
source_file: raw/articles/2026-08-25-arxivorg-abs-260518747.md
url: https://arxiv.org/abs/2605.18747
published: 2026-05-18
ingested: 2026-08-25
domains: [agents]
---

# Code as Agent Harness

An arXiv survey (submitted 2026-05-18, cs.CL/cs.AI) arguing that code is becoming the operational substrate for agent systems rather than only a final output. The paper organizes harness design around three layers: the harness interface (where code connects agents to reasoning, action, and environment modeling), harness mechanisms (planning, memory, tool use for long-horizon execution, plus feedback-driven control), and scaling the harness from single-agent to multi-agent settings, where shared code artifacts support coordination, review, and verification. It surveys applications across coding assistants, GUI/OS automation, embodied agents, scientific discovery, and enterprise workflows, and names open challenges including evaluation beyond final task success and regression-free harness improvement.

## Influenced pages
- [Harness (agent)](../../concepts/harness.md) — added as a research framing reinforcing code-centered harness design

## Key claims extracted
- Frames "code as agent harness": code as the operational substrate for reasoning, acting, environment modeling, and execution-based verification, not just a target output
- Three-layer structure: harness interface, harness mechanisms (planning/memory/tool use/feedback control), and multi-agent scaling
- Open challenges named: evaluation beyond final task success, verification under incomplete feedback, regression-free harness improvement, consistent shared state across agents, human oversight for safety-critical actions
- This is a synthesis/survey paper, not a benchmark result — its framing is a useful vocabulary, not an empirical claim about any specific system
```

### wiki/sources/tweets/mcp-2026-07-28-stateless-rc.md (new)

```md
---
title: "MCP 2026-07-28 release candidate: stateless protocol"
type: source
source_type: tweet
source_file: raw/tweets/2026-08-25-redirect-e9187825-ab02-42eb-ac5f-ad4d73f120dc.md
url: https://x.com/dsp_
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# MCP 2026-07-28 release candidate: stateless protocol

David Soria Parra (an MCP protocol maintainer) announced the release candidate for the MCP 2026-07-28 protocol revision. The headline change: MCP becomes stateless — no handshake, no session ID, and any request can hit any server instance. The RC also adds first-class extensions (MCP Apps, Tasks), auth hardening, and a proper deprecation policy. AINews's recap reads the statelessness as a big operational shift for infra teams (easier scaling, simpler load balancing, fewer sticky-session concerns).

## Influenced pages
- [Model Context Protocol](../../concepts/mcp.md) — added the stateless RC as a protocol-evolution update

## Key claims extracted
- MCP 2026-07-28 RC removes handshake and session-ID requirements; any request can hit any server instance
- Adds MCP Apps and Tasks as first-class protocol extensions
- Adds auth hardening and a "proper deprecation policy"
- The operational reading (easier scaling, simpler load balancing, fewer sticky sessions) is AINews's gloss, not part of the tweet text
- The "2026-07-28" string names the protocol revision, not its announcement date. The tweet text was captured only from the fetched page title (the raw file is a Substack redirect whose body is a reply, not the original post), so `url:` is the author's profile and `published:` is inferred from the AINews issue that carried it (2026-05-23, covering the prior day) — not read from the tweet itself. Grounded in an MCP maintainer's account, not an official MCP spec-repo changelog
```

### wiki/sources/tweets/brockman-model-not-product.md (new)

```md
---
title: 'Greg Brockman: "the model alone is no longer the product"'
type: source
source_type: tweet
source_file: raw/tweets/2026-08-25-redirect-319f79bc-9ba8-4279-9445-16881405c3d0.md
url: https://x.com/gdb
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# Greg Brockman: "the model alone is no longer the product"

OpenAI President Greg Brockman stated publicly that "the model alone is no longer the product" — cited by AINews as a big reversal from a position held almost uniformly by "Team Big Model" veterans, and as part of a broader pattern of Model Labs absorbing agent/harness work.

## Influenced pages
- [Agent Labs vs Model Labs](../../concepts/agent-labs-vs-model-labs.md) — added as reinforcing evidence for the thesis

## Key claims extracted
- Brockman: "the model alone is no longer the product" (the only text captured; the raw fetch is a Substack redirect whose body came back empty, so the quote is taken from the page title and the AINews recap)
- Framed by AINews as a reversal from his and peers' earlier position
- Contextualized by AINews alongside AI21 shuttering its model team (pivoting to agents) and DeepSeek building its first "harness team"
- `url:` is the author's profile (permalink not recovered) and `published:` is inferred from the AINews issue date (2026-05-23, covering the prior day), not read from the tweet
```

### wiki/sources/newsletters/anthropic-is-onto-something.md (new)

```md
---
title: "Anthropic is onto something"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-anthropic-is-onto-something.md
url: https://codenewsletter.ai/p/google-drops-gemini-3-5-flash-github-breached-via-a-malicious-extension
published: 2026-05-20
ingested: 2026-08-25
domains: [agents, cybersecurity]
---

# Anthropic is onto something

The Code newsletter (2026-05-20) covering Google I/O's Gemini 3.5 Flash / Antigravity 2.0 launch, Anthropic's self-hosted sandboxes and MCP tunnels for Claude Managed Agents, and GitHub's confirmation that a compromised employee device and poisoned VS Code extension led to the theft of internal repositories.

## Influenced pages
- [Claude Managed Agents](../../tools/claude-managed-agents.md) — self-hosted sandboxes / MCP tunnels (the "Code with Claude London" venue detail comes from this newsletter, not the Anthropic blog post)
- [State of Cybersecurity](../../state-of/cybersecurity.md) — GitHub breach entry

## Key claims extracted
- Anthropic rolled out self-hosted sandboxes (public beta) and MCP tunnels (research preview) for Claude Managed Agents at its Code with Claude event in London; points to the Anthropic blog post ingested separately
- Lists "Code as Agent Harness" (arXiv 2605.18747) as its trending paper; the paper is ingested from arXiv directly, so this newsletter is not cited on `concepts/harness.md`
- GitHub confirmed internal repos were stolen via a compromised employee device and a malicious/poisoned VS Code extension; attacker claimed ~3,800 repos, matching GitHub's own count
- Gemini 3.5 Flash and Antigravity 2.0 are covered but not re-ingested here — already tracked via other, more detailed sources per the triage note
```

### wiki/sources/newsletters/google-io-agents-agents-agents.md (new)

```md
---
title: "Google I/O: Agents, Agents, Agents"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-google-io-agents-agents-agents.md
url: https://every.to/context-window/google-i-o-agents-agents-agents
published: 2026-05-20
ingested: 2026-08-25
domains: [agents]
---

# Google I/O: Agents, Agents, Agents

Every's Context Window newsletter (2026-05-20) on Google I/O's agent-first announcements, Anthropic's reported ~$300M acquisition of Stainless, and a mini-Vibe Check of Figma's new in-canvas design agent.

## Influenced pages
- [Model Context Protocol](../../concepts/mcp.md) — Stainless acquisition and its MCP-server design-legibility angle

## Key claims extracted
- Anthropic acquired Stainless; terms weren't disclosed, and Every reports The Information put the price at "north of $300 million" (cross-checked against Anthropic's own announcement, which does not disclose price)
- Former Stainless customers include OpenAI and Google, "meaning Anthropic has acquired a developer tooling company used by its top rivals" (this detail is Every's, not in Anthropic's announcement)
- Stainless CEO Alex Rattray had, in an October *AI & I* podcast episode, outlined MCP server design principles for agent legibility: keep the number of tools small, give tools precise names, aim for tightly defined outputs
- Disclosure noted in the newsletter: Dan Shipper is a small investor in Stainless
- Figma's in-canvas design agent and the broader Google I/O agent announcements are not re-ingested here — out of scope for this proposal
```

### wiki/sources/newsletters/ainews-all-model-labs-are-now-agent-labs.md (new)

```md
---
title: "[AINews] All Model Labs are now Agent Labs"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
url: https://www.latent.space/p/ainews-all-model-labs-are-now-agent
published: 2026-05-23
ingested: 2026-08-25
domains: [agents, cybersecurity]
---

# [AINews] All Model Labs are now Agent Labs

AINews/Latent Space digest (2026-05-23) covering the "model alone is no longer the product" thesis (Greg Brockman, AI21's pivot, DeepSeek's new harness team), the MCP 2026-07-28 stateless release candidate, managed-sandbox primitives becoming first-class (Gemini Managed Agents + Interactions API, CoreWeave Sandboxes, Cloudsail), DeepSeek V4-Pro's permanent price cut, and Anthropic's Project Glasswing reporting 10,000+ high/critical-severity vulnerabilities found within a month.

## Influenced pages
- [Agent Labs vs Model Labs](../../concepts/agent-labs-vs-model-labs.md) — added Brockman/AI21/DeepSeek evidence
- [Model Context Protocol](../../concepts/mcp.md) — MCP stateless RC
- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — Glasswing 10,000+ vulnerabilities figure
- [State of Cybersecurity](../../state-of/cybersecurity.md) — Glasswing figure

## Key claims extracted
- Greg Brockman: "the model alone is no longer the product" — AINews calls it a big reversal from a stance held ~uniformly by "Team Big Model"; AI21 shuttered its model team to pivot to agents; "even the venerable DeepSeek" is building a "harness team" for the first time
- AINews's own counterpoint: models co-trained with harnesses "open the door for closing access to models even further" — a lab that post-trains its model to perform well only inside its closed-source agent can funnel users to that agent at the expense of its model/API business
- MCP 2026-07-28 RC is stateless (no handshake/session ID); adds MCP Apps/Tasks, auth hardening, deprecation policy; AINews reads statelessness as easier scaling, simpler load balancing, fewer sticky-session concerns
- Managed sandboxes as first-class primitives: Gemini Managed Agents + Interactions API, CoreWeave Sandboxes (public preview), Cloudsail (per-task Cloudflare sandboxes)
- Anthropic: Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities in essential software within a month of launch
- DeepSeek V4-Pro discount made permanent; Chinese open-weight models closing the gap — not re-ingested here, out of scope for this proposal
```

### wiki/sources/newsletters/ainews-new-ai-infra-unicorns-exa-modal-turbop.md (new)

```md
---
title: "[AINews] New AI Infra unicorns: Exa, Modal, TurboPuffer"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa-modal-turbop.md
url: https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa
published: 2026-05-22
ingested: 2026-08-25
domains: [agents]
---

# [AINews] New AI Infra unicorns: Exa, Modal, TurboPuffer

AINews/Latent Space digest (2026-05-22). Only the agent-orchestration guidance item is ingested here; the newsletter's broader coverage (Exa/Modal/Turbopuffer funding, Daytona compute-infra podcast highlights, the OpenAI Erdős math result discussion, Runway Aleph 2.0 / Edit Studio, Codex Thursday updates) is out of scope for this proposal and not re-ingested.

## Influenced pages
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — added single-agent-first escalation threshold

## Key claims extracted
- Cameron Wolfe (@cwolferesearch) synthesis: start with single-agent systems; only move to manager/sub-agent or decentralized multi-agent topologies once tool sprawl or prompt bloat becomes unmanageable
- Cognition's "sub-Devin" workflow reportedly compresses 2+ engineer-weeks of work into a couple of hours (practitioner anecdote via a Twitter reply, not independently verified)
```

## Schema / vocabulary additions

None required — all frontmatter uses existing controlled `domains` (`agents`, `cybersecurity`), and no new `subcategory` or `tags` values are introduced.

## Open questions

- **Stainless acquisition price is unverified.** Anthropic's own announcement (`https://www.anthropic.com/news/anthropic-acquires-stainless`, fetched directly) does not disclose a purchase price. The "~$300M" figure traces only to The Information via Every's newsletter recap. I've flagged this in both `concepts/mcp.md`'s new Recent-changes entry and the Stainless source-summary page. Treat the price as unconfirmed until a primary figure surfaces.
- **No dedicated `tools/stainless.md` page was created.** Stainless is now absorbed into Anthropic rather than an independently tracked product, so I folded its content into `concepts/mcp.md`. Flag if you'd prefer a standalone tool page instead (e.g. to track it as a discrete acquisition/integration story over time).
- **MCP 2026-07-28 RC sourcing is thin.** The only source is an MCP maintainer's tweet via an AINews recap (the direct tweet fetch returned a reply, not the original post body — the title metadata captured the original text). If you want this claim on firmer footing, worth checking the official MCP spec repo's changelog directly.
- **Orchestration spill choice.** The mechanical rule (spill the oldest by date) makes this ingest's own `[2026-05-22]` entry the one archived, so the live page never shows it. If you prefer the ingest to be visible, spill `[2026-05-29]` instead and keep `[2026-05-22]` at the bottom of the live list — both orchestration drafts would need that swap.
