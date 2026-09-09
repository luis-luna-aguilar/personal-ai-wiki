---
title: Flue
type: tool
domains: [agents]
subcategory: agent-framework
tags: [agentic]
as_of: 2026-09-01
sources: [flue-2-react-for-agents-2026-08-15, latent-space-pr-not-welcome-2026-09-01]
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

## Contribution policy (as of 2026-09-01)

Flue auto-closes external pull requests and converts them into issues or discussions instead — Schott's contributor guide frames this as preventing "drive-by AI slop PRs" while still channeling community input through discussion. Once a direction is decided in the issue or discussion, agents are deployed for research, design, implementation, and initial review. A concrete instance of the "PRs closed by default" pattern — see [Agentic orchestration patterns](../workflows/agentic-orchestration-patterns.md).

## Recent changes

- [2026-09-01] Contribution policy detailed: Flue auto-closes external PRs, converting them into issues/discussions instead; agents handle research, design, implementation, and initial review once a direction is chosen.
- [2026-08-15] Flue 2 released — first stable release, introduces the Agent Hooks pattern (16 built-in hooks) built on Pi.

## Sources

- [React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue](../sources/newsletters/flue-2-react-for-agents-2026-08-15.md)
- [PRs NOT Welcome — Latent Space](../sources/newsletters/latent-space-pr-not-welcome-2026-09-01.md)
