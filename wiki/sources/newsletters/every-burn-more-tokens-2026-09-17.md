---
title: "Why You Should Burn More Tokens — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-17-why-you-should-burn-more-tokens.md
url: https://every.to/context-window/why-you-should-burn-more-tokens
published: 2026-09-17
ingested: 2026-11-24
domains: [agents]
---

# Why You Should Burn More Tokens — Every

Laura Entis's Context Window edition on how Every handles large AI bills without hard budgets: expensive experiments are encouraged but reviewed afterwards, a card-refill alert works as an early-warning system, and one uncapped agent swarm burned 4.5 billion tokens before its owner rebuilt it with limits. Also includes a token-audit prompt, Marcus Moretti's model-matching workflow, and the team's current model choices. A 20 September Every recap (`raw/newsletters/2026-09-20-copy-our-homework.md`) repeats the same points.

## Influenced pages

- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — uncapped-swarm case and its fix
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — refill alert and three post-run questions; uncapped fan-out failure mode

## Key claims extracted

- Dan Shipper uses more than three times the tokens of anyone else at Every; low spend is a "smoke signal" that people may be thinking too small
- No universal spending limit; after an expensive run, ask whether it was worth it and whether a similar result could be had more cheaply
- Arielle Shipper keeps a $500 ChatGPT auto-refill with a Slack alert per top-up; rapid top-ups prompt a look at the usage leaderboard
- Three post-run questions: what did it cost, what did it buy, what did we learn
- Every is building a skill for per-employee AI-spending P&L statements; Mike Taylor is building personal benchmarks to show which cheaper models handle recurring tasks
- Randy Counsman's manager/implementer/subagent/judge swarm ran 1.5 days, used 4.5B tokens, produced a "very janky" Blender model; layers passed growing context even for status checks
- Fix: drop the implementer, cap the orchestrator at five Sol subagents, pause for feedback, give the judge a reference image
