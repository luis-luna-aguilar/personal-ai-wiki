---
title: Skillify — Agent Reliability Pattern
type: workflow
domains: [agents]
subcategory: agentic-orchestration-patterns
tags: [agentic]
as_of: 2026-04-23
sources: [garrytan-skillify-2026-04-23]
---

# Skillify — Agent Reliability Pattern

A workflow for turning every agent failure into a permanent, tested skill that makes the failure structurally impossible to repeat. Coined and published by Garry Tan (YC CEO) based on his production experience with his personal AI agent system (OpenClaw/GBrain).

The underlying architecture is "thin harness / fat skills": the model reasons in latent space to build deterministic tools, and those tools then constrain the model so it can't make the same mistake twice.

## The pattern

### Core loop

1. Agent fails at a task
2. Diagnose: was this latent work (judgment) done in deterministic space, or deterministic work (predictable, scriptable) done in latent space?
3. If deterministic work was done the wrong way: extract it into a skill + script
4. The skill (markdown procedure) tells the agent how to approach the task; the script does the work without LLM calls
5. Add tests so the failure is structurally impossible to repeat

### Latent vs deterministic work distinction

The most practical concept in the pattern:
- **Latent work:** requires judgment, context, creativity — must be done in LLM space
- **Deterministic work:** same input always produces same output (timestamp math, calendar lookup, grep) — should be done in script space, never LLM space

When an agent does deterministic work in latent space, it will fail intermittently. The fix is always a script + skill.

### The 10-step Skillify checklist

When a failure is promoted to a skill:

1. `SKILL.md` — the contract (name, triggers, rules)
2. Deterministic code — `scripts/*.mjs` (no LLM for what code can do)
3. Unit tests — vitest (pure functions, fixture data)
4. Integration tests — live endpoints, real data
5. LLM evals — quality and correctness (LLM-as-judge, 35+ per skill daily)
6. Resolver trigger — entry in `AGENTS.md` routing table
7. Resolver eval — verify the trigger actually routes correctly
8. `check-resolvable` + DRY audit — ensure skill is reachable and non-duplicate
9. E2E smoke test — full pipeline, end to end
10. Brain filing rules — where outputs get stored

A feature that doesn't pass all ten is not a skill. It's just code that happens to work today.

### Resolver (routing table)

A resolver (`AGENTS.md`) maps intent phrases to skills. Two key failure modes:
- **False negative:** the skill should fire but doesn't (trigger description wrong or missing)
- **False positive:** the wrong skill fires (trigger descriptions overlap)

Resolver evals test both: deterministic structural tests (is the mapping in the table?) AND LLM routing tests (does the model actually pick the right skill?).

### check-resolvable

A meta-test that walks the full chain: `AGENTS.md` resolver → `SKILL.md` → script. Finds skills that exist in the filesystem but have no path from the resolver ("dark skills"). First run on a real 40+ skill setup found 6 unreachable skills (15% of the system's capabilities were dark).

## Skillify as a verb

In practice: prototype in conversation → see it work → say "skillify" → the agent runs the full 10-step checklist automatically. The ad-hoc session becomes permanent infrastructure in one word.

## Why it matters

Most agent systems have no recovery mechanism: the agent apologizes, and two weeks later the same failure recurs from a different entry point. Skillify creates a structural fix: the failure becomes impossible, not just less likely.

The pattern is not specific to any particular harness or model. The 10-step checklist can be adapted to any agent system that supports persistent context, tool/script execution, and some form of eval loop.

## Related

- [Harness (agent)](../concepts/harness.md) — the thin harness is the other half of the "thin harness / fat skills" duality
- [Agent improvement loop](../concepts/agent-improvement-loop.md) — complementary improvement loop; operates at the harness/eval layer rather than the skill/script layer; the two approaches address different failure modes
- [Agentic orchestration patterns](agentic-orchestration-patterns.md) — overlapping concern: agent reliability and recovery patterns
- [gstack](../tools/gstack.md) — Garry Tan's Claude Code config (related system; gstack is the Claude Code layer, GBrain/OpenClaw is the personal agent layer where Skillify lives)
- [Hermes Agent](../tools/hermes-agent.md) — NousResearch's `skill_manage` tool does skill creation but without the test/eval coverage; the essay explicitly discusses Hermes as a comparison case

## Sources

- [Garry Tan — How to really stop your agents from making the same mistakes (Skillify)](../sources/tweets/garrytan-skillify-2026-04-23.md)
