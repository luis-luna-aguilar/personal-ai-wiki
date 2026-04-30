---
title: Garry Tan — How to really stop your agents from making the same mistakes (Skillify)
type: source
source_type: tweet
source_file: raw/tweets/2026-04-23-garrytan-2046876981711769720.md
url: https://x.com/garrytan/status/2046876981711769720
published: 2026-04-23
ingested: 2026-04-23
domains: [agents]
---

# Garry Tan — How to really stop your agents from making the same mistakes (Skillify)

Full-length essay published as a tweet thread by Garry Tan (YC CEO). Describes the "Skillify" pattern for making agent failures structurally non-repeating via a 10-step quality checklist. Introduces the "thin harness / fat skills" architecture and the "latent vs deterministic work" distinction. Builds on his OpenClaw/GBrain personal agent system. Compares to NousResearch's Hermes Agent (which does skill creation but lacks the testing layer).

## Influenced pages

- [Skillify — Agent Reliability Pattern](../../workflows/skillify-agent-reliability.md) — new workflow page; primary source

## Key claims extracted

- "Thin harness / fat skills": model intelligence builds deterministic tools that constrain the model
- Latent vs deterministic work: the key failure mode is deterministic work done in LLM space
- 10-step Skillify checklist: SKILL.md, deterministic code, unit tests, integration tests, LLM evals, resolver trigger, resolver eval, DRY audit, smoke test, brain filing
- check-resolvable: first run on 40+ skills found 15% unreachable ("dark skills")
- Hermes creates skills automatically but without the test/eval coverage — comparison case
- GBrain SkillPacks: portable bundles installable into any agent setup
