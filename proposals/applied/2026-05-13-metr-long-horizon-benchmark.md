---
type: proposal
sources:
  - raw/newsletters/2026-05-12-the-fallacy-of-the-16-hour-agent.md
status: pending
created: 2026-05-13
---

# Proposal: METR long-horizon benchmark — Claude Mythos Preview breaks the 16-hour scale

## Summary

METR published an update to its time-horizon task benchmark. Claude Mythos Preview achieves 50% success on tasks rated at "16+ hours" of human-equivalent work — the top of the current scale. At the more operationally useful 80% reliability threshold, Mythos handles tasks worth ~3 human hours (vs ~1.5 hours for the nearest competitor, Gemini 3.1 Pro). METR cautions that "duration" is a proxy for task difficulty, not wall-clock time.

## Intended changes

- [x] **Update** `wiki/models/claude-mythos-preview.md` — add METR long-horizon benchmark data; update `as_of` and `sources`
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add long-horizon reliability data to the agents page Recent changes
    > **Append to Recent changes:**
    > `- [2026-05-12] METR long-horizon benchmark: Claude Mythos Preview 50% success at 16+ hours (breaks current scale); 80% reliability threshold ~3 human-hours (Gemini 3.1 Pro ~1.5 hours); METR cautions duration is a difficulty proxy, not wall-clock time`

- [x] **Create** `wiki/sources/newsletters/metr-long-horizon-2026-05-12.md`
    > See draft below

## Page drafts

### wiki/models/claude-mythos-preview.md — diff snippets

**Frontmatter `as_of`:**
> **Before:** `as_of: 2026-04-22`
> **After:** `as_of: 2026-05-12`

**Frontmatter `domains`:**
> **Before:** `domains: [models, cybersecurity]`
> **After:** `domains: [models, cybersecurity, agents]`

**Frontmatter `sources` — append:**
> Add `metr-long-horizon-2026-05-12`

**Current status — replace the `## Current status (as of 2026-04-22)` header and bullets with:**
```markdown
## Current status (as of 2026-05-12)

- Not publicly available; accessible only via Anthropic's Project Glasswing partner program
- Used to autonomously identify thousands of zero-day vulnerabilities in every major OS and web browser — without human steering
- Partners confirmed: Cisco, AWS, Microsoft
- Substantially outperforms Claude Opus 4.6 on the CyberGym benchmark

## METR long-horizon benchmark (May 2026)

METR's time-horizon task benchmark measures how reliably an AI model can complete tasks that METR rates by how long an equivalent task would take a human software engineer.

- **50% success at "16+ hours"** — Mythos Preview is the first model to hit 50% at the top category of METR's current scale, effectively breaking the ceiling
- **80% reliability threshold ≈ 3 human-hours** — at the more operationally useful 80% bar (the point where the agent succeeds reliably enough to delegate without close supervision), Mythos handles tasks worth roughly 3 hours of human-equivalent work
- **Nearest competitor: Gemini 3.1 Pro at ~1.5 human-hours** at the 80% threshold
- **Duration is a difficulty proxy** — METR cautions that the "hours" metric measures task complexity, not literal wall-clock time; AI agents complete these tasks faster than the human baseline
```

**Recent changes — prepend before `## Sources`:**
> **Add section header and entries:**
```markdown
## Recent changes

- [2026-05-12] METR long-horizon benchmark: 50% at 16+ hours (breaks scale ceiling); 80% reliability threshold ~3 human-hours; Gemini 3.1 Pro closest competitor at ~1.5 hours
- [2026-04-22] Initial page created from Project Glasswing; cybersecurity capabilities documented
```

**Sources — append:**
```
- [METR long-horizon benchmark — The Fallacy of the 16-Hour Agent](../sources/newsletters/metr-long-horizon-2026-05-12.md)
```

### wiki/sources/newsletters/metr-long-horizon-2026-05-12.md (new)

```markdown
---
title: METR long-horizon benchmark update — May 2026
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-12-the-fallacy-of-the-16-hour-agent.md
published: 2026-05-12
ingested: 2026-05-13
domains: [models, agents]
---

# METR long-horizon benchmark update — May 2026

The newsletter "The Fallacy of the 16-Hour Agent" reports METR's update to its time-horizon task benchmark, focusing on Claude Mythos Preview's results and the interpretive nuances of the benchmark's "duration" metric.

## Influenced pages

- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — METR benchmark data added
- [State of Agents](../../state-of/agents.md) — long-horizon reliability note added to Recent changes

## Key claims extracted

- Claude Mythos Preview achieves 50% success on METR tasks rated as "16+ hours" human-equivalent — first model to reach the top of the current scale
- At 80% reliability, Mythos handles tasks worth ~3 human-hours of equivalent work
- Gemini 3.1 Pro is the nearest competitor at ~1.5 human-hours at the 80% threshold
- METR explicitly cautions: "duration" is a proxy for task difficulty (complexity, scope, number of steps), not literal wall-clock time — AI agents complete these tasks considerably faster than the human baseline
- The 80% threshold is the operationally relevant number: it represents reliable-enough performance to delegate without close supervision
- Perplexity's agent skill methodology is also covered in this newsletter (see separate proposal)
```

