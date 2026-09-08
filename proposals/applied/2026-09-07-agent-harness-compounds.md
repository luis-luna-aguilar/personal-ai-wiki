---
type: proposal
source: raw/newsletters/2026-08-22-the-evolution-of-the-agent-harness.md
status: pending
created: 2026-09-07
---

# Proposal: The agent harness keeps compounding — co-evolution theory, self-modifying harnesses, and enterprise MCP auth

## Summary

### The source

A Latent Space essay argues that the "harness matters as much as the model" thesis this wiki already tracks isn't a static fact but a repeating cycle: train, absorb, shed. As models get RL-trained inside their own harness — learning to call tools, manage their own context window, compact their own history — they absorb capabilities the harness used to have to supply externally, and engineers then delete the now-redundant scaffolding: Anthropic reportedly cut 80% of Claude Code's system prompt this way. The essay walks the history in stages — ReAct in 2022 as a pure prompting trick with no real harness yet; AutoGPT and BabyAGI handing full autonomy to models that weren't remotely ready for it; the IDE-era retreat to human-in-the-loop that followed; and Claude Code in February 2025 as the moment the model finally got reliable enough that handing the loop back to it worked. Its prediction for what comes next: once the model absorbs everything computer-facing, the harness doesn't disappear, it inverts — becoming the interface that governs a human's attention instead, deciding when an agent may interrupt someone, what it can decide alone, and what needs a person's approval.

A second source, the same AINews issue already referenced by a companion proposal, adds concrete, same-week evidence that harness engineering is an active research and product battleground right now: NVIDIA argues static structural checks on an agent "skill" barely predict whether it actually helps (Spearman ρ = 0.14 against judged task quality) and proposes measuring "Skill Lift" — the completion-quality delta of running the same task with and without the skill — instead. Two new open-source projects, Headlong and exo, push self-modification into the harness itself: Headlong runs a continuously-thinking agent that stores its own trajectories and can repair its own bugs unattended, while exo adds an append-only event log and rollback-safe sandboxing so an agent can rewrite its own prompts and tools without corrupting durable state. A position paper argues enterprises should standardize on one reusable coding-agent harness rather than bespoke orchestration graphs per team. And Anthropic shipped enterprise-managed authentication for MCP connectors, moving per-tool OAuth click-throughs into IT-governed, identity-provider-backed infrastructure.

### What changes

The wiki's `concepts/harness.md` page already argues the harness is a first-class competitive surface with its own architecture patterns; this adds the theory of *why* that keeps happening and *what's coming next*, plus concrete August 2026 infrastructure evidence.

- **Harness (agent)** gains a new "co-evolution" section (the train → absorb → shed cycle, the ReAct-through-Claude-Code history, and the "attention interface" future thesis) plus four new bullets under its harness-engineering-patterns list (Skill Lift, Headlong/exo, single-harness standardization, enterprise MCP auth). Page date moves to 22 August.
- Because the page's Recent-changes list is already at its 10-entry cap, the oldest entry (the June 5 RL-harness-quality-taxonomy note) spills to `wiki/history/concepts/harness.md`.
- New source page for the Latent Space harness essay; a second source page (the AINews issue) may already exist by the time this is applied, created by a companion proposal — if so, this proposal's Influenced-pages line gets appended to it rather than creating a duplicate.

### What to weigh

The "80% of Claude Code's system prompt deleted" figure and the ARC-AGI-3 tripling-via-harness-change figure are both attributed to named individuals/teams in secondary reporting (a conference quote and an OpenAI-relayed result), not primary technical writeups — treated here as reported claims, consistent with how the rest of this page already handles similar attributions. The "attention interface" framing is one essay's forward-looking argument, not an established pattern yet, so it's presented as a thesis rather than current state.

## Intended changes

- [x] **Approve all**

- [ ] **Update** `wiki/concepts/harness.md` — add co-evolution section and four new engineering-pattern bullets, bump as_of, add Recent-changes entry
    > See draft below

- [ ] **Spill** `wiki/concepts/harness.md` → `wiki/history/concepts/harness.md` — oldest Recent-changes entry (2026-06-05) falls off the 10-entry cap
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/latent-space-agent-harness-evolution-2026-08-22.md` — source summary
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md` — source summary
    > See draft below

## Page drafts

### wiki/concepts/harness.md (updated)

> **Frontmatter:** `as_of: 2026-08-21` → `as_of: 2026-08-25`; append `latent-space-agent-harness-evolution-2026-08-22` and `ainews-andrew-ng-ai-engineering-2026-08-25` to `sources:`.

> New section, inserted after `## Harness continual learning and multi-agent coordination research (August 2026)` and before `## Caveats`:

```md
## The model/harness co-evolution theory (August 2026)

A widely-shared Latent Space essay argues the "harness matters" era follows a predictable cycle rather than being a permanent architecture choice: train → absorb → shed → repeat. As models get RL-trained inside their own harness (tool calling, compaction, memory management), they absorb capabilities the harness used to have to supply externally, and the harness sheds that scaffolding once the model no longer needs it — Anthropic reportedly deleted 80% of Claude Code's system prompt this way. The essay traces the model/harness "gap" through stages: ReAct as pure prompting with no real harness yet (October 2022); AutoGPT/BabyAGI handing full autonomy to models not remotely ready for it (spring 2023); the IDE-era retreat to human-in-the-loop that followed; and Claude Code's February 2025 "curves cross" moment, where the model finally got reliable enough to be handed the loop back. Its prediction for what comes next: once the model absorbs everything computer-facing, the harness doesn't disappear — it inverts, becoming the interface that governs a person's attention instead of the model's actions, deciding when an agent may interrupt someone, what it can decide alone, and what needs approval, since human attention (not tokens) is the resource that stays scarce. Two 2026-08 data points anchor the "harness still matters enormously today" half of the argument: Harness-Bench found a 23.8-point score swing (52.4→76.2) running one model through different harnesses on the same 106 tasks, and OpenAI tripled GPT-5.6 Sol's ARC-AGI-3 score (13.3%→38.3%) through harness changes (retained reasoning + compaction) alone, with no model change.
```

> New bullets appended to `## What good harness engineering looks like`:

```md
- **Skill Lift over structural skill checks.** NVIDIA argues static checks on an agent "skill" barely predict usefulness (Spearman ρ=0.14 against judged quality); the better metric is Skill Lift — run the same task with and without the skill under identical conditions and score the delta in completed work.
- **Self-modifying, persistent harnesses.** Two open-source projects push recursive self-improvement into the harness itself: Headlong stores agent trajectories as a DAG of jsonl files and runs a self-guided inner loop continuously rather than only on request (reported a 48-minute unattended self-debugging repair, at $1-2/hr background-thinking cost); exo adds an append-only event log, a swappable executor, and a snapshot/rollback-capable sandbox so an agent can rewrite its own prompts/tools/memory without corrupting durable state.
- **Standardize on one harness, not bespoke orchestration graphs.** A position paper argues enterprises should pick a single reusable coding-agent harness rather than building bespoke orchestration per team, since harness choice can matter more for outcomes than model choice.
- **Enterprise-managed MCP auth.** Anthropic rolled out enterprise-managed authentication for MCP connectors, centralizing authorization through the org's identity provider so end users no longer perform per-tool OAuth for connectors like Asana, Atlassian, Figma, Notion, Slack, and Supabase — moving MCP connector auth from a per-user click-through into IT-governed infrastructure.
```

> **Recent changes:** add as the newest entry (adds one entry; enforce the cap by spilling the current oldest, 2026-06-05):
```md
- [2026-08-25] Added the model/harness co-evolution framing (ReAct → AutoGPT → Cursor → Claude Code "curves cross," train→absorb→shed cycle) and its "attention interface" future thesis; added NVIDIA's Skill Lift metric, two self-modifying agent harnesses (Headlong, exo), a single-harness-standardization position paper, and Anthropic's enterprise-managed MCP connector auth.
```

> **Sources** (append):
```md
- [The Evolution of the Agent Harness](../sources/newsletters/latent-space-agent-harness-evolution-2026-08-22.md)
- [AINews — Andrew Ng gets into AI Engineering](../sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md)
```

### wiki/history/concepts/harness.md (updated)

> Adds a new archive block above the existing ones (spills the current oldest live entry):

```md
## Archived from current page on 2026-09-07

- [2026-06-05] Added RL harness quality section: 8 failure modes taxonomy from Auriel W (Google Gemini RL team); "5% failure rate = harness problem, not model problem"
```

### wiki/sources/newsletters/latent-space-agent-harness-evolution-2026-08-22.md (new)

```md
---
title: The Evolution of the Agent Harness
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-22-the-evolution-of-the-agent-harness.md
url: https://www.latent.space/p/attention-interface
published: 2026-08-22
ingested: 2026-09-07
domains: [agents]
---

# The Evolution of the Agent Harness

A Latent Space essay arguing model and harness capability co-evolve in a train → absorb → shed cycle, walking the history from ReAct through Claude Code's February 2025 "curves cross" moment, and predicting the harness's next role is governing human attention rather than model action.

## Influenced pages

- [Harness (agent)](../../concepts/harness.md) — new co-evolution section, "attention interface" thesis

## Key claims extracted

- Harness-Bench: same model through different harnesses on the same 106 tasks scored 52.4-76.2 (23.8-point spread)
- OpenAI tripled GPT-5.6 Sol's ARC-AGI-3 score (13.3%→38.3%) via harness changes (retained reasoning + compaction) alone
- Anthropic reportedly deleted 80% of Claude Code's system prompt as the model absorbed what it used to specify
- Predicts harnesses will next become "attention interfaces" governing when an agent may interrupt a human and what it can decide alone

### wiki/sources/newsletters/ainews-andrew-ng-ai-engineering-2026-08-25.md (new)

```md
---
title: "AINews — Andrew Ng gets into AI Engineering"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-25-ainews-andrew-ng-gets-into-ai-engineering.md
url: https://www.latent.space/p/ainews-andrew-ng-gets-into-ai-engineering
published: 2026-08-25
ingested: 2026-09-07
domains: [agents, training]
---

# AINews — Andrew Ng gets into AI Engineering

AINews issue leading with Andrew Ng's DeepLearning.AI relaunch around four "AI Engineering" skills, plus a Twitter/Reddit recap covering harness-design research (NVIDIA's Skill Lift metric, Headlong, exo, single-harness standardization), Anthropic's enterprise-managed MCP auth, continued Qwen3.8-27B momentum, and cost-normalized agent benchmarks (GLM-5.3 vs. Fable, Sol Max vs. Fable Max, Cline's Ox Alpha token-efficiency comparison). Two companion proposals also draw on this same issue.

## Influenced pages

- [Harness (agent)](../../concepts/harness.md) — Skill Lift, Headlong/exo, single-harness standardization, enterprise MCP auth bullets
- [AI Engineering skills](../../training/ai-engineering-skills.md) — new page, primary source for the Andrew Ng skills taxonomy
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — cost-normalized DeepSWE/Cline benchmark evidence

## Key claims extracted

- Andrew Ng relaunches DeepLearning.AI around four AI Engineering skills, based on 10,000+ job postings plus hiring-manager/recruiter interviews
- NVIDIA: structural skill checks correlate with judged usefulness at only Spearman ρ=0.14; proposes "Skill Lift" (task-completion delta with/without a skill) instead
- Headlong: open-source persistent/continuously-thinking agent harness; DAG-based trajectory storage; 48-minute unattended self-debugging repair reported; $1-2/hr background-thinking cost
- exo: harness for recursive self-improvement with an append-only event log and rollback-safe sandbox
- Anthropic enterprise-managed auth for MCP connectors (Asana, Atlassian, Canva, Datadog, Figma, Notion, Slack, Supabase), centralized via org identity provider
- Qwen3.8-27B: #9 on Code Arena: WebDev (1595 points), only model in its size class in the top 10
- Cost-normalized benchmarks: GLM-5.3 completes 5x more DeepSWE work than Fable 5 per fixed $100 budget; GPT-5.6 Sol Max 72.7% on DeepSWE v1.1 for $6.47/task vs. Fable 5 Max 69.7% for $21.63/task; Cline's Ox Alpha solved a bugfix using ~3x fewer output tokens than Fable
```

## Open questions

- The "80% of system prompt deleted" and "tripled ARC-AGI-3 via harness alone" figures come from a conference quote and OpenAI-relayed result respectively, not primary writeups — acceptable as reported claims consistent with this page's existing sourcing standard, but flagging in case a primary source surfaces later that should supersede them.
	- Ok.