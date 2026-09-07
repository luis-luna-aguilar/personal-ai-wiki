---
type: proposal
source: raw/newsletters/2026-08-15-react-for-agents-astro-creator-brings-hooks-to-hi.md
status: pending
created: 2026-09-07
---

# Proposal: Flue 2 — "React for Agents"

## Summary

### The source

Latent Space's swyx interviewed Fred Schott — creator of the Astro web framework, whose company was acquired by Cloudflare in January — about Flue 2, the first stable release of his agent framework, Flue. Flue's foundation is React-style "Agent Hooks": an agent is represented by a JavaScript/TypeScript function that re-renders on every turn, before every model call, letting it manage its own state and dynamically attach tools, skills, and other capabilities as a conversation or workflow progresses. Flue 2 ships 16 built-in hooks (`useSkill()`, `useTool()`, `useSubagent()`) and supports custom ones. Schott's thinking evolved fast: Flue 1 (launched early May) naively ported file-based routing from web frameworks — "put your five agents in these five files" — but he found most Flue customers run one agent for their whole company, not many routed agents, so composability mattered more than routing, pulling the design toward React rather than Astro/Next.js. Flue is built on Pi, an open-source minimal harness Schott treats the way Astro treats Vite: a foundational, unopinionated layer he adds opinionated developer-facing features on top of. His central thesis, stated flatly: "there is no agent without a harness" — the harness isn't a feature bolted onto an agent, it's what makes something an agent at all. The project began as an issue-triage system inside the Astro repo and grew into wanting "the Claude Code experience, headless and hostable." Schott names Vercel's eve — already tracked in the wiki — as Flue's most direct competitor, both having launched this year with harness-as-foundation as the starting premise, versus "OG" frameworks (Vercel's AI SDK, Cloudflare's Agents SDK, Mastra) that are retrofitting harnesses onto pre-harness designs. Flue's differentiator from eve is host portability: Flue is explicitly "an open source framework for every host," while eve is optimized for (though not locked to) Vercel's own platform. A managed-agents hosting product, unlike LangChain's Managed Deep Agents, is explicitly not on Flue's roadmap — "we're just focused on building the best harness."

### What changes

The wiki has no page for Flue or Pi yet; `tools/eve.md` already covers Flue's direct competitor, and `concepts/harness.md` already tracks the "harness as foundational, not bolted-on" theme broadly.

- **New page** `tools/flue.md` — Fred Schott's agent framework, covering the Agent Hooks pattern, its Pi foundation, the file-routing-to-composability pivot from v1 to v2, and its host-portability contrast with eve.
- **Harness (agent)** gains one Recent-changes entry naming Flue 2 as a second concrete "harness is foundational, not a feature" example alongside eve, plus a link to the new Flue page under `## Related`. The oldest Recent-changes entry (2026-05-20, Claude Managed Agents sandboxes/MCP tunnels) spills to `wiki/history/concepts/harness.md` since the section is at its 10-entry cap.
- One new source page for the interview.

### What to weigh

The source is a single interview (Latent Space, one credible outlet, on-the-record quotes from Schott) rather than official Flue documentation — version numbers, hook counts, and the Pi relationship are all as Schott described them verbally, not verified against Flue's own docs or changelog. Pi itself (the minimal harness Flue is built on) doesn't get its own page here; it's mentioned only as context on the Flue page, consistent with reuse-first discipline — a dedicated Pi page would need its own primary source. Nothing else beyond the sourcing noted above.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Create** `wiki/tools/flue.md` — new agent-framework page for Flue 2
    > See draft below

- [ ] **Update** `wiki/concepts/harness.md` — add Recent-changes entry for Flue 2, link to new page under `## Related`, add source to frontmatter and `## Sources`
    > See draft below

- [ ] **Spill** `wiki/concepts/harness.md` → `wiki/history/concepts/harness.md` — oldest recent-change entry (2026-05-20, Claude Managed Agents sandboxes/MCP tunnels) falls off the 10-entry cap

- [ ] **Create** `wiki/sources/newsletters/flue-2-react-for-agents-2026-08-15.md` — source summary

## Page drafts

### wiki/tools/flue.md (new)

```md
---
title: Flue
type: tool
domains: [agents]
subcategory: agent-framework
tags: [agentic]
as_of: 2026-08-15
sources: [flue-2-react-for-agents-2026-08-15]
---

# Flue

Flue is Fred Schott's agent framework — Schott is the creator of the Astro web framework, acquired into Cloudflare in January 2026. Flue 2, its first stable release, is built around React-style "Agent Hooks": an agent is a JS/TS function that re-renders on every turn (before every model call), managing its own state and dynamically attaching tools, skills, and capabilities as a conversation progresses.

## Current status (as of 2026-08-15)

- Flue 2 ships 16 built-in hooks (`useSkill()`, `useTool()`, `useSubagent()`, plus custom hooks), authored in TypeScript.
- Built on top of Pi, an open-source minimal harness — Schott treats Pi's role as analogous to Vite underneath Astro: a foundational, unopinionated layer Flue adds developer-facing opinions on top of.
- Central thesis: "there is no agent without a harness" — the harness is fundamental to what an agent is, not a bolt-on feature.
- Pivoted from Flue 1's naive file-based routing ("five agents, five files") to a composability-first design after finding most customers run one agent for their whole company, not many routed agents.
- Positioned as an open-source, host-portable framework ("for every host") — the main differentiator from its closest competitor, [eve](eve.md), which is optimized for (though not locked to) Vercel's own platform.
- No managed-agents hosting product on the roadmap; Schott: "we're just focused on building the best harness."

## Strengths

- Composable, React-inspired hook model fits agents whose configuration needs to change mid-conversation (e.g. a support agent bringing in an account-management tool only after verifying a user).
- Host-neutral by design, unlike platform-optimized competitors.

## Weaknesses / caveats

- Current source is interview coverage, not official docs — version specifics and adoption scale are unverified beyond Schott's own account.
- Early-stage: Flue 2 is its first stable release; the file-routing-to-hooks pivot shows the design is still actively evolving.

## Recent changes

- [2026-08-15] Flue 2 released — first stable release, introduces the Agent Hooks pattern (16 built-in hooks) built on Pi.

## Sources

- [React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue](../sources/newsletters/flue-2-react-for-agents-2026-08-15.md)
```

### wiki/concepts/harness.md (updated)

Frontmatter `sources:` gains `flue-2-react-for-agents-2026-08-15` appended to the existing list.

`## Recent changes` — insert as the newest entry (before the current 2026-08-11 entry), then spill the oldest (2026-05-20) per the cap:

```md
## Recent changes

- [2026-08-15] Flue 2 (Fred Schott, Astro creator) launched as a second concrete "harness is foundational, not a feature" framework alongside eve — React-style Agent Hooks that let an agent re-render its own tools/state on every turn.
- [2026-08-11] Added SWE-bench Pro harness-swap data (23-52% on GLM-5.2, 15-36% on Gemma 4 26B, -0.05 harness-ranking rank correlation across models) and a Composio DeepSeek V4 Flash four-harness bake-off (Pi Agent cheapest and best-performing) as concrete numbers behind the harness-vs-model claim.
- [2026-07-14] Added the Lilian Weng 2023-vs-2026 essay contrast and Anthropic's "grown, not designed" framing, from AI Engineer World's Fair 2026 coverage.
- [2026-07-08] Gemini API managed agents add hosted harness primitives: MCP support, background execution, custom function calling, credential refresh, and stateful agent interactions.
- [2026-07-03] Added control-layer framing from AI Engineer World Fair: permissions, cost ceilings, recovery, and review routing are part of the harness boundary.
- [2026-07-01] Added agent recipes as a harness packaging pattern: model choices, evals, judges, human expertise, failure history, and signal processing bundled with the workflow.
- [2026-06-24] Claude Tag coverage adds org-embedded agent identity, permission scoping, and Slack-channel memory boundaries as harness concerns.
- [2026-06-22] Gray Swan security coverage adds prompt injection, exfiltration, identity, permissions, and automated red teaming as harness-boundary concerns for tool-using agents.
- [2026-06-05] Added RL harness quality section: 8 failure modes taxonomy from Auriel W (Google Gemini RL team); "5% failure rate = harness problem, not model problem"
- [2026-05-30] Added Effective Feedback Compute and model-specific harness profiles as harness-quality signals beyond token/tool counts.
<!-- spills: [2026-05-20] Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview)... -->
```

`## Related` — add one line:

```md
- [Flue](../tools/flue.md) — Fred Schott's agent framework; React-style Agent Hooks built on the Pi minimal harness, a second concrete "harness as foundational" example alongside eve
```

`## Sources` — append:

```md
- [React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue](../sources/newsletters/flue-2-react-for-agents-2026-08-15.md)
```

### wiki/history/concepts/harness.md (updated — spill target)

Append to the existing archive block (create `## Archived from current page on <apply date>` header if none exists yet at apply time):

```md
- [2026-05-20] Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview), extending the harness security boundary so tool execution and private MCP connectivity can run on customer infrastructure while Anthropic keeps the orchestration loop.
```

### wiki/sources/newsletters/flue-2-react-for-agents-2026-08-15.md (new)

```md
---
title: "React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-15-react-for-agents-astro-creator-brings-hooks-to-hi.md
url: https://www.latent.space/p/flue-2
published: 2026-08-15
ingested: 2026-09-07
domains: [agents]
---

# React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue

Latent Space interview with Fred Schott (Astro creator, now at Cloudflare) about Flue 2, the first stable release of his agent framework. Covers the React-style "Agent Hooks" pattern (16 built-in hooks, agents as re-rendering functions), the pivot away from file-based routing toward composability, Flue's Pi foundation, and its host-portability contrast with Vercel's eve.

## Influenced pages

- [Flue](../../tools/flue.md) — new page
- [Harness (agent)](../../concepts/harness.md) — Recent-changes entry, Related link

## Key claims extracted

- Flue 2 is Fred Schott's agent framework's first stable release, built around React-style "Agent Hooks."
- An agent in Flue is a JS/TS function that re-renders on every turn, before every model call.
- 16 built-in hooks ship in Flue 2: `useSkill()`, `useTool()`, `useSubagent()`, plus custom hooks.
- Flue is built on Pi, an open-source minimal harness.
- Flue 1 (early May 2026) used file-based routing; Flue 2 pivoted to composability after most customers turned out to run one agent, not many routed agents.
- Schott's thesis: "there is no agent without a harness."
- Vercel's eve is named as Flue's most direct competitor; Flue differentiates on host portability ("open source framework for every host").
- No managed-agents hosting product is on Flue's roadmap.
```
