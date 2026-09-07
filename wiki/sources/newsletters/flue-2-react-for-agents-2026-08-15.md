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
