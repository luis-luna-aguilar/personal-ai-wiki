---
type: proposal
sources:
  - raw/newsletters/2026-09-01-ainews-fals-h3-max-live-breaks-the-infinite-vid.md
  - raw/newsletters/2026-09-03-ainews-muse-spark-13-matches-gpt-56-sol-confi.md
status: pending
created: 2026-09-09
---

# Proposal: Agent harness and context-engineering research cluster

## Summary

### The source

Two AINews issues from the same week each carry a dense cluster of agent-harness and context-engineering research and product news. Google DeepMind and collaborators published WikiSkill / SKILL.state, which replaces ever-growing conversation histories with explicit mutable state plus persistent skill knowledge for better long-horizon accuracy at lower token cost. Tencent's ContextPilot trains agents to edit their own working context directly, with RL reward assigned at the level of individual context edits rather than final outcome. ByteDance Seed's HarnessDev has models build and then improve their own execution harness from a weak seed, finding — across six model families, four task domains, and 2,207 held-out instances — that self-evolved harnesses still lag hand-engineered systems on code, search, and research, but match or beat them on writing and ML experimentation. A companion paper on "Retrieval-Invoked Actual-Use Effect" warns that skill/tool retrieval can raise aggregate benchmark scores while actively hurting the specific tasks that trigger it, across 17 LLMs. On the production side, the open-source harness openJiuwen reached 82.6% SWE-bench Verified / 87.19% Terminal-Bench 2.1 through "rail-based composition," and Miles shipped as an open-source RL-as-a-service training framework built on SGLang. NousResearch's Hermes Agent shipped v0.21.0 in the same window — Bots Mode, agent-to-agent communication, persistent multi-gateway connections, subagent steering — while also cutting default context usage roughly 50%. DeepSeek's own harness took on breaking plugin-contract changes in a v0.1.2-alpha release. Multiple independent voices (@omarsar0, @dejavucoder) explicitly named "harness engineering" a core, distinct AI-engineering skill across both issues.

### What changes

- **Harness (agent)** gains a new dated research-cluster section synthesizing all six papers/releases above (WikiSkill/SKILL.state, ContextPilot, HarnessDev, the retrieval-effect paper, openJiuwen, Miles), plus a Recent-changes entry. The list is already at its 10-entry cap, so the oldest entry spills to history.
- **Hermes Agent** gains a new section on the v0.21.0 release and its context-usage reduction, plus a Recent-changes entry — the page currently only documents the v0.10.0 baseline from May.
- No new source pages: both raw newsletters are owned and summarized by the companion Muse Spark/Muse Code proposal in this same batch; this proposal references those source slugs directly.

### What to weigh

This is a synthesis signal spanning six distinct papers/releases rather than one story — each item gets one or two sentences on the harness page rather than its own subsection, consistent with how the page already compresses multi-item research weeks elsewhere. All six items come through AINews' aggregation of X threads rather than primary papers or release notes; none were independently fetched or verified beyond what the newsletters report. The Hermes Agent v0.21.0 changelog specifics (context-usage cut, feature list) likewise rest on the newsletter's characterization, not a fetched release note.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/harness.md` — add a research-cluster section; add 1 Recent-changes entry (list is at the 10-entry cap, so the oldest entry spills to `wiki/history/concepts/harness.md`)
    > See draft below

- [ ] **Update** `wiki/tools/hermes-agent.md` — add v0.21.0 section; add 1 Recent-changes entry
    > See draft below

## Page drafts

### wiki/concepts/harness.md (updated)

Insert this new section directly before `## Caveats`:

```md
## Context-engineering and harness research cluster (September 2026)

A cluster of harness/context-engineering research and product releases landed in the same week. WikiSkill / SKILL.state (Google DeepMind and collaborators) replaces ever-growing conversation histories with explicit mutable state plus persistent skill knowledge, reporting better long-horizon accuracy at lower cumulative token use. Tencent's ContextPilot trains agents to edit their own working context directly, assigning RL reward at the level of specific context edits rather than final task outcome — a more targeted credit-assignment scheme for long-horizon tasks. ByteDance Seed's HarnessDev has models build and then iteratively improve their own execution harness from a weak, runnable seed, scoring both stages on capability and execution-token cost; across six creator LLMs, four domains, and 2,207 held-out instances, self-evolved harnesses still lag mature human-engineered systems on code, search, and research, but match or exceed them on writing and ML experimentation — a caution that self-improving harnesses help unevenly, not universally. A "Retrieval-Invoked Actual-Use Effect" paper adds a sharper caution for skill/tool retrieval specifically: across 17 LLMs on coding and math, retrieval can raise aggregate scores while having a negative effect on the very tasks where it actually fires — aggregate lift is not proof a retrieval system is helping the tasks that use it. On the production side, openJiuwen (open-source) reaches 82.6% SWE-bench Verified / 87.19% Terminal-Bench 2.1 through "rail-based composition" on a fixed model, and Miles ships as an open-source RL-as-a-service training framework using SGLang as its rollout inference engine. Hermes Agent shipped v0.21.0 in the same window — see [Hermes Agent](../tools/hermes-agent.md) — while DeepSeek's own harness took on breaking plugin-contract changes. Multiple independent voices (@omarsar0, @dejavucoder) explicitly named "harness engineering" a core, distinct AI-engineering skill this week, echoing the framing this page has tracked since March 2026.
```

Recent changes — add this entry at the top (list is at the 10-entry cap; the oldest entry, `[2026-07-03] Added control-layer framing from AI Engineer World Fair...`, spills to `wiki/history/concepts/harness.md`):

```md
- [2026-09-01] Added a harness/context-engineering research cluster: WikiSkill/SKILL.state, ContextPilot, HarnessDev, the Retrieval-Invoked Actual-Use Effect paper, openJiuwen, and Miles.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `ainews-fal-h3-max-live-2026-09-01` and `ainews-muse-spark-13-2026-09-03`.

### wiki/tools/hermes-agent.md (updated)

Insert this new section directly after `## Compared to OpenClaw` and before `## Recent changes`:

```md
## v0.21.0 release (as of 2026-09-01)

Hermes Agent shipped a large feature release aimed at persistent, multi-agent workflows: Bots Mode, agent-to-agent communication, persistent multi-gateway connections, and subagent steering, plus broader connector access. A follow-up release note says the update also cut default context usage by roughly 50% — a concrete instance of context-efficiency becoming a first-class systems concern for the framework, alongside the broader [harness research cluster](../concepts/harness.md) from the same week.
```

Recent changes — add this entry at the top:

```md
- [2026-09-01] v0.21.0 ships Bots Mode, agent-to-agent comms, persistent multi-gateway connections, subagent steering, broader connector access; cuts default context usage ~50%.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `ainews-fal-h3-max-live-2026-09-01`.

## Open questions

None beyond the sourcing note above.
