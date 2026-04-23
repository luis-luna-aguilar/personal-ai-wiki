---
type: proposal
sources:
  - raw/tweets/2026-04-22-addyosmani-2040132221328388418.md
  - raw/tweets/2026-04-22-lennysan-2039845666680176703.md
status: pending
created: 2026-04-22
---

# Proposal: Agentic cognitive overhead — the underreported cost of parallel agent management

## Summary

Multiple converging sources describe a new kind of cognitive load specific to running parallel AI agents: holding multiple problem contexts simultaneously, making continuous judgment calls, and absorbing the anxiety of not knowing what each agent is quietly getting wrong. Addy Osmani frames it as "personal ceiling" work — finding your individual maximum is itself a skill. This is a distinct failure mode from the AI work intensification pattern already on the page.

## Intended changes

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add cognitive overhead as a distinct failure mode and guidance
    > **Add to `## Failure modes`:**
    > ```markdown
    > - **Parallel agent cognitive overhead is underestimated.** Running multiple coding agents simultaneously amplifies cognitive load in a new way: you hold multiple problem contexts in your head, make judgment calls continuously, and absorb anxiety about what each agent may be quietly getting wrong. Addy Osmani: "more agents running doesn't mean more of *you* available." Simon Willison: running 4 agents in parallel, wiped out by 11am. This is distinct from general AI work intensification — it's specific to the multi-agent supervision model and doesn't improve automatically with practice. Over-spinning agents degrades judgment quality.
    > ```
    >
    > **Add to `## Current guidance`:**
    > ```markdown
    > - Find your personal ceiling for parallel agent sessions and treat it like a deep-focus work budget. Time-box agentic sessions rather than running open-ended parallel threads. Tighter scope per agent reduces the per-thread cognitive overhead dramatically (Addy Osmani).
    > ```

- [x] **Create** `wiki/sources/tweets/agentic-cognitive-overhead.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/tweets/agentic-cognitive-overhead.md (new)

```md
---
title: Agentic cognitive overhead — personal ceiling for parallel agents
type: source
source_type: tweet
source_file: raw/tweets/2026-04-22-addyosmani-2040132221328388418.md
url: https://x.com/addyosmani/status/2040132221328388418
published: 2026-04-22
ingested: 2026-04-22
domains: [coding, agents]
---

# Agentic cognitive overhead — personal ceiling for parallel agents

Two converging sources. Addy Osmani: "more agents running doesn't mean more of you available" — proposes time-boxing agentic sessions and finding your personal ceiling as a learned skill. Lenny/Willison: 4 parallel agents leads to being wiped out by 11am — AI exhaustion is real and underestimated.

## Influenced pages

- [[training/ai-enablement-software-development]] — cognitive overhead failure mode and guidance added

## Key claims extracted

- Parallel agents require holding multiple problem contexts simultaneously
- Continuous judgment calls + anxiety about quiet failures = new cognitive labor
- "Personal ceiling" for parallel agents is a skill to develop, not a fixed limit
- Time-boxing agentic sessions like deep focus work reduces overhead
- Tighter scope per agent significantly changes per-thread cognitive load
- Simon Willison: 4 parallel agents, wiped out by 11am (consistent testimony from a prolific practitioner)
```
