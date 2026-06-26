---
title: Loopcraft and agent-native architecture (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-16-we-built-our-own-agent-native-tool-it-overhauled.md
published: 2026-06-16
ingested: 2026-06-17
domains: [agents, coding]
---

# Loopcraft and agent-native architecture (June 2026)

Three converging sources crystallized a design paradigm: the right unit of AI work is a loop, not a prompt. AINews named this "Loopcraft"; Satya Nadella's 60M-view essay framed it as "frontier ecosystem over frontier model"; Every's Hoop case study provided a concrete build example.

## Influenced pages

- [AI-native product building](../../training/ai-native-product-building.md) — Hoop case study, loop-first principle
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — loop-first, tool clarity, deploy-where-users-work patterns

## Key claims extracted

- "You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents." (Steipete)
- Satya Nadella essay: "frontier ecosystem, not just frontier model" — build a learning loop where human capital + token capital compound
- Hoop (Stella Garber) built agent-native customer discovery tool in <10 hours with Claude API + Slack; handled unanticipated scenarios because tools were clear and model was allowed to reason
- Core stack: Next.js, ShadCN, Supabase, Claude API; Slack as the interface surface
- Key quote: "If you give a reasoning model simple, powerful tools, it can handle situations you never thought to code for"
- Deviated from agent-native only for operations that were genuinely simpler as traditional code
