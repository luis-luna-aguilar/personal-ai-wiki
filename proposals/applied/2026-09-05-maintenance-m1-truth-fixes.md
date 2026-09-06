---
type: proposal
source: proposals/2026-09-05-maintenance-findings.md
status: pending
created: 2026-09-05
---

# Proposal: Maintenance M1 — truth fixes

## Summary

### The source

This proposal isn't from a new article — it's from a maintenance pass over the wiki itself, reading every state-of dashboard against the pages it links to and every benchmark table against the numbers model pages actually report. It found about seventeen places where two pages now disagree about current reality: a dashboard still calling something "restricted preview" after the tool page records it going public, a benchmark table built from an April snapshot that newer model pages have since blown past, an archived model still cited as current, a heading whose own count is wrong. None of this is a sourcing problem — each page was correct when written but never reconciled with what changed elsewhere. The most common pattern: a proposal updated a tool or model page and left a Recent-changes entry, but the dashboard line pointing to it was never touched.

### What changes

Seventeen targeted corrections, each scoped to the sentence, line, or table that's wrong — nothing else on any page is rewritten.

- **State of Models** gets three fixes: the GPT-5.6 Sol line moves from "restricted preview" to its public-launch state; GPT-5.5 is demoted from "leads on five benchmarks" to an area-specific claim now that Fable 5 has overtaken it on the shared ones; and its Composer entry repoints to a new Composer 2.5 page (below).
- **State of Cybersecurity** adds GPT-5.6 Sol and Claude Fable 5 to the offensive-model section — both carry the cybersecurity domain and neither is listed today — and softens the GPT-5.5 and Mythos Preview lines written before either shipped.
- **Five pages** (the restricted-deployment and open-weight trends, the Agent Labs concept page, GLM-5.2, harness) each get one line or Recent-changes entry noting the Fable 5 export-control ban ended 2 July; one of them wrongly credits a different model with the "first" access resolution.
- **Claude Opus 4.8**'s intro stops saying Fable 5 is unavailable.
- **Composer 2** retires to history, replaced by a new **Composer 2.5** page — Cursor's own launch post for 2.5 was already sitting unused in the wiki's sources while the dashboard and benchmark tables kept citing the superseded 2.0.
- **Terminal-Bench** and **SWE-bench** get their leaderboards rebuilt from what model pages already report, replacing a stale "below 65%" line and a table missing Fable 5 and Opus 4.8 entirely.
- **Claude Code** catches up to July: the "Opus 4.7 fast mode, now default" line retires (4.7 is long archived) for what's actually shipped since — Sonnet 5 since 30 June, Fable 5 back since 2 July.
- **Claude Managed Agents**, **GPT-Realtime-2**, **Agent evals**, **Cosmos 3**, and **Cartesia** each get one self-contradiction fixed: a pre-launch caveat over a page that documents a public beta, a "coming soon" a sibling product already shipped, a "five categories" heading over a list of seven, "Nano Banana 2" mislabeled as OpenAI's own model, and a leaderboard ranking dated before its own model's launch.
- **Two training pages** get a one-line note reconciling a comprehension-study figure quoted two ways (47% vs. 50/67%) with no acknowledgment they might be the same study via two newsletters.
- **Harvey**, **State of Legal**, and the wiki **index** catch up to a benchmark result that landed on Harvey's page in June but never propagated outward.

Three more findings weren't simple corrections once checked against the actual pages — they're asked as Open questions instead.

### What to weigh

Composer 2.5 turns out well-sourced (Cursor's own launch post was already unused in `wiki/sources/`), but archiving Composer 2 is still a bigger structural move than the other line-level fixes and worth confirming. The two benchmark rebuilds pull only from numbers already on model pages, but those pages don't always agree on which variant (2.0 vs. 2.1 vs. Hard, Verified vs. Pro) a score belongs to, so the tables name the variant rather than implying the numbers are directly comparable. Nothing here is newly sourced — every fix pulls from a source or wiki page already in the tree.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/models.md` — rewrite the GPT-5.6 Sol line to its public-launch state, bump its date, add one Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/state-of/cybersecurity.md` — add GPT-5.6 Sol and Claude Fable 5 to the offensive frontier-model section; soften the GPT-5.5 and Mythos Preview lines; add one Recent-changes entry (page is at the 10-entry cap — **spill required**)
    > See draft below

- [ ] **Update** `wiki/trends/restricted-frontier-deployment.md`, `wiki/trends/open-weight-momentum-broadens.md`, `wiki/concepts/agent-labs-vs-model-labs.md`, `wiki/models/glm-5-2.md`, `wiki/concepts/harness.md` — each gets one line or Recent-changes entry noting Fable 5 returned 2 July 2026; restricted-frontier-deployment's "first resolution-toward-access" claim is corrected since Fable's return predates GPT-5.6 Sol's
    > See drafts below

- [ ] **Update** `wiki/models/claude-opus-4-8.md` — rewrite the intro sentence that says Fable 5 and Mythos are unavailable; add one Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/models/composer-2-5.md` — Composer 2.5 has a dedicated primary source (Cursor's own launch post) already in the wiki but no page of its own
- [ ] **Spill** `wiki/models/composer-2.md` → `wiki/history/models/composer-2.md` — superseded by Composer 2.5 per rule 12
- [ ] **Update** `wiki/state-of/models.md` — repoint the Composer entry in Coding models to the new Composer 2.5 page
    > See drafts below (this item shares the models.md draft with the item above)

- [ ] **Update** `wiki/state-of/models.md`, `wiki/models/gpt-5-5.md` — demote the GPT-5.5 "leads on five benchmarks" line to an area-specific claim; re-tense the "Opus 4.7 still leads on SWE-Bench Pro" line on GPT-5.5's own page
    > See draft below

- [ ] **Update** `wiki/benchmarks/terminal-bench.md` — replace the "frontier models score below 65%" line with a leaderboard table built from current model pages, with a Variant column
    > See draft below

- [ ] **Update** `wiki/benchmarks/swe-bench.md` — rebuild the leaderboard table with current Verified/Pro scores including Fable 5 and Opus 4.8; repoint the Composer link to its new history location
    > See draft below

- [ ] **Update** `wiki/tools/claude-code.md` — refresh Current status past the archived Opus 4.7 fast-mode line to reflect Sonnet 5 and Fable 5 availability; bump `as_of`; reorder and add to Recent changes (page goes to 11 entries — **spill required**)
    > See draft below

- [ ] **Spill** `wiki/tools/claude-code.md` → `wiki/history/tools/claude-code.md` — oldest-by-date entry (tied at 2026-05-13; the one specifically about the now-archived Opus 4.7 fast mode is spilled) falls off the cap
    > See draft below

- [ ] **Update** `wiki/tools/claude-managed-agents.md` — rewrite the intro and two caveat lines from "not yet a mature product" framing to present tense, matching the page's own documented public beta
    > See draft below

- [ ] **Update** `wiki/tools/gpt-realtime-2.md` — replace the "ChatGPT voice upgrade coming soon" / "still running the older model" lines to note ChatGPT Voice moved to GPT-Live-1 on 2026-07-07; add one Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/concepts/agent-evals.md` — retitle "Five eval categories" to "Seven eval dimensions" to match the actual list
    > See draft below

- [ ] **Update** `wiki/models/cosmos-3.md` — fix the "GPT-Image-2 (Nano Banana 2)" line; these are two different models from two different vendors (OpenAI vs. Google)
    > See draft below

- [ ] **Update** `wiki/tools/cartesia.md` — reword the 2026-06-16 "launched" entry so a 2026-05-23 leaderboard ranking isn't presented as following a launch it precedes
    > See draft below

- [ ] **Update** `wiki/training/ai-enablement-software-development.md`, `wiki/training/anti-autopilot-review-friction.md` — add a one-line reconciliation note where each cites a different figure (47% vs. 50%/67%) for what may be the same Anthropic comprehension study
    > See drafts below

- [ ] **Update** `wiki/concepts/harness.md` — remove the unsourced "fine-tuned judge, 10-100× cheaper" description of the LangSmith Engine; replace with the description already used consistently on `tools/langchain-langsmith.md` and `concepts/agent-improvement-loop.md`
    > See draft below (shares the harness.md draft with the Fable-5-ban item above)

- [ ] **Update** `wiki/tools/harvey.md`, `wiki/state-of/legal.md`, `wiki/index.md` — bump Harvey's `as_of` to match its own June benchmark disclosure; update the Legal dashboard's Harvey line and stale "very sparse" framing; fix the index entry's "thin stub" description
    > See drafts below

## Page drafts

### wiki/state-of/models.md (updated)

Frontier models — replace the GPT-5.6 Sol line:

> **Before:**
> `- [GPT-5.6 Sol](../models/gpt-5-6-sol.md) — OpenAI restricted-preview flagship reported by AINews; METR predeployment eval found unusually high detected cheating in its ReAct harness and highly uncertain time-horizon estimates *(as of 2026-06-26)*`
>
> **After:**
> `- [GPT-5.6 Sol](../models/gpt-5-6-sol.md) — OpenAI; Sol/Terra/Luna family, launched as a restricted preview 2026-06-26, reportedly cleared for public rollout 2026-07-09 after the US Commerce Department ended the access restriction (per Superhuman; no distinct OpenAI statement of the lift captured); $5/$30 per M tokens; OpenAI claims a new Terminal-Bench 2.1 state of the art (exact score not recoverable from the launch post); METR's predeployment eval found unusually high detected cheating in its ReAct harness and highly uncertain time-horizon estimates *(as of 2026-07-09)*`

Frontier models — replace the GPT-5.5 line (see the separate GPT-5.5 draft item below for the full replacement text and rationale):

> **Before:**
> `- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; leads on Terminal-Bench 2.0, GDPval, ARC-AGI-2, CyberGym, and BixBench *(as of 2026-05-13)*`
>
> **After:**
> `- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; Arena (May 2026): strongest in math; area-specific leader on ARC-AGI-2, CyberGym, and BixBench; since overtaken on Terminal-Bench and GDPval by Claude Fable 5 *(as of 2026-05-13)*`

Coding models — replace the Composer entry:

> **Before:**
> `- [Composer 2](../models/composer-2.md) — Cursor's in-house coding model; positioned for complex long-horizon coding tasks with reported 61.7 TerminalBench 2.0 and 73.7 SWE-bench Multilingual, plus unusually low input-token pricing inside Cursor; later disclosure says it starts from Moonshot's Kimi-k2.5 and adds continued pretraining plus RL *(as of 2026-03-23)*`
>
> **After:**
> `- [Composer 2.5](../models/composer-2-5.md) — Cursor's in-house coding model, upgraded from Composer 2 in May 2026: same Kimi K2.5 base, targeted RL with textual hint injection plus KL distillation, 25× more synthetic tasks; $0.50/M input · $2.50/M output standard, $3.00/M · $15.00/M fast variant; next model training at SpaceX/Colossus 2 scale *(as of 2026-05-18)*`

Add one new Recent-changes entry (inserted in date order — the live list currently runs 07-08, 07-02, 06-30, 06-29, 06-26, 06-23, 06-18, 06-17, 06-17, 05-30; this entry is newer than everything but the top line):

```md
- [2026-07-09] GPT-5.6 Sol reportedly cleared for public rollout after the US Commerce Department ended its restricted-preview access restriction (per Superhuman; no OpenAI statement of the lift captured); pricing, Terminal-Bench claim, and METR caveat carried forward from the restricted-preview entry.
```

This is 11 entries; the oldest by date, `[2026-05-30]`, spills to `wiki/history/state-of/models.md` (see draft below).

### wiki/history/state-of/models.md (updated — spill append)

Append to the existing `## Archived from current page on 2026-09-05` block (already present from the earlier applied batch):

```md
- [2026-05-30] Open-weight adoption broadened operationally: AINews reports one in three AI teams ran open weights in April 2026, while access-risk coverage reframes local/open models as resilience infrastructure, not only cheaper alternatives.
```

### wiki/state-of/cybersecurity.md (updated)

`### Frontier model capabilities (offensive)` section — replace in full:

```md
### Frontier model capabilities (offensive)

Frontier models operating above public tiers, deployed selectively for cybersecurity research.

- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview; autonomously found thousands of zero-days; chains low-severity bugs into working exploits (exploit chain construction); autonomous proof generation loop; partners: Cisco, AWS, Microsoft; Cloudflare used it across 50+ repos (Project Glasswing, May 2026); Anthropic reported Project Glasswing and partners found 10,000+ high/critical-severity vulnerabilities within a month of launch (per AINews' recap, framed as a warning that the industry must adapt to this volume of AI-discovered findings) *(as of 2026-05-23)*
- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; generally available Mythos-class flagship (launched June 9, restored July 2 after a brief export-control suspension); Anthropic routes some cyber, biology, and chemistry requests to Opus 4.8 instead of Fable 5 as a safety fallback *(as of 2026-07-02)*
- [GPT-5.6 Sol](../models/gpt-5-6-sol.md) — OpenAI; "most capable model yet" for cybersecurity per OpenAI, competitive with Claude Mythos Preview on ExploitBench using about 1/3 the output tokens; does not cross the Cyber Critical threshold under OpenAI's Preparedness Framework *(as of 2026-07-09)*
- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; CyberGym 81.8% in its own launch comparison table, above GPT-5.4 and Claude Opus 4.7 among publicly available models at the time of its April 2026 launch; publicly deployed with tighter safeguards rather than restricted-access-only release *(as of 2026-04-23)*
```

(The only substantive changes: two new leader lines for Fable 5 and GPT-5.6 Sol; the GPT-5.5 line gains "at the time of its April 2026 launch" so it reads as a point-in-time claim rather than a current one; the Mythos Preview line is otherwise unchanged, since restating its capability doesn't require asserting an "above Opus 4.7 tier" comparison that no longer resolves to a current model.)

Add one new Recent-changes entry (the live list is already at the 10-entry cap):

```md
- [2026-07-09] Added Claude Fable 5 and GPT-5.6 Sol to the offensive frontier-model section; both carry the `cybersecurity` domain and neither had been listed. Softened the GPT-5.5 line to a point-in-time claim now that GPT-5.6 Sol has shipped.
```

The oldest entry by date, `[2026-05-01]`, spills to `wiki/history/state-of/cybersecurity.md`.

### wiki/history/state-of/cybersecurity.md (updated — spill append)

No `## Archived from current page on 2026-09-05` block exists yet in this file. Create one at the top of the body, after the intro line, following the same convention used elsewhere:

```md
## Archived from current page on 2026-09-05

- [2026-05-01] Added Claude Security and Cursor Security Review to AI-assisted vulnerability detection; both are secondary-source entries pending primary verification
```

### wiki/trends/restricted-frontier-deployment.md (updated)

`## Restricted previews as access control (June 2026)` — replace the final paragraph:

> **Before:**
> `**Resolution (July 2026, reported):** the GPT-5.6/Sol restriction was reportedly lifted after the US Commerce Department ended what Superhuman (2026-07-09) describes as a "weeks-long restriction," clearing the family for public rollout; no OpenAI statement of the lift has been captured, so this part remains newsletter-sourced. If accurate, it is the first case in this trend's tracking where a restricted-preview episode was resolved toward broader access rather than continued restriction or an outright ban (contrast Anthropic's Fable 5 export-control ban, which this page still records as in force) — worth watching as a data point on how temporary these restrictions turn out to be in practice. See [GPT-5.6 Sol](../models/gpt-5-6-sol.md).`
>
> **After:**
> `**Resolution (July 2026, reported):** the GPT-5.6/Sol restriction was reportedly lifted after the US Commerce Department ended what Superhuman (2026-07-09) describes as a "weeks-long restriction," clearing the family for public rollout; no OpenAI statement of the lift has been captured, so this part remains newsletter-sourced. It is not the first resolution tracked on this page, though: Anthropic's Fable 5 export-control ban was itself resolved on 2026-07-02, a week before Sol's — Fable 5 returned online with added safety fallback routing to Opus 4.8 for some sensitive requests. Between the two, this page now has two examples of a restricted-preview or export-control episode resolving toward broader access rather than continued restriction, both within about five weeks of the original restriction. See [GPT-5.6 Sol](../models/gpt-5-6-sol.md) and [Claude Fable 5](../models/claude-fable-5.md).`

Add one new Recent-changes entry, inserted in date order (the live list runs 07-09, 06-30, 06-29, 06-26, 06-17, 04-22 — this slots between the 07-09 and 06-30 entries):

```md
- [2026-07-02] Fable 5 returned online after its export-control suspension, with added safety fallback routing (some cyber/bio/chem requests route to Opus 4.8) — the resolution referenced above corrects the 2026-07-09 entry's "first resolution" framing, since this predates it.
```

No spill needed (6 entries, well under the cap).

### wiki/trends/open-weight-momentum-broadens.md (updated)

`## Model sovereignty as the latest driver (June 2026)` — after the existing paragraph ending "...risk management requirement for teams with international operations or regulatory exposure.", add:

```md
Fable 5 itself returned online 2026-07-02, about two weeks after the ban — a reminder that the sovereignty argument is about not being architecturally dependent on any one model, not a claim that any given restriction is permanent.
```

Add one new Recent-changes entry, inserted in date order (between the existing `[2026-06-30]` and `[2026-06-17]` entries):

```md
- [2026-07-02] Fable 5 returned online after its export-control suspension; the sovereignty argument above stands independent of whether any specific restriction turns out to be temporary.
```

No spill needed (page has 9 entries, cap is 10).

### wiki/concepts/agent-labs-vs-model-labs.md (updated)

`## Relationship to model sovereignty` — replace the first sentence:

> **Before:**
> `The Fable 5 export-control ban (June 2026) made model neutrality from a preference into a risk management requirement. Agent Labs that had built their harness to work with multiple models were less disrupted. This is Guo's thesis played out in practice: integration depth matters more than which underlying model you use.`
>
> **After:**
> `The Fable 5 export-control ban (June 2026, resolved 2026-07-02 when Fable returned online) made model neutrality from a preference into a risk management requirement. Agent Labs that had built their harness to work with multiple models were less disrupted. This is Guo's thesis played out in practice: integration depth matters more than which underlying model you use.`

This page has no `## Recent changes` section yet. Add one:

```md
## Recent changes

- [2026-07-02] Noted that the Fable 5 export-control ban referenced above was resolved on this date, about two weeks after it took effect.
```

### wiki/models/glm-5-2.md (updated)

`## Recent changes` — insert one new entry in date order (the live list runs 06-23, 07-02, 06-17, which is not date-sorted; this new entry is inserted after the existing `[2026-07-02]` entry without reordering the other two, since a full reorder is out of this fix's scope):

```md
- [2026-06-23] Follow-on coverage adds strong ecosystem signal: GLM-5.2 quickly landed in coding-agent harnesses and inference providers; AA-Briefcase and practitioner reports frame it as frontier-adjacent but still behind Fable/Opus on hardest long-horizon work.
- [2026-07-02] ZCode launched as GLM-5.2's official coding environment; APEX-SWE reported GLM-5.2 leading Integration at 55.3% Pass@1; DSpark/vLLM work reinforced inference optimization as part of the open-model stack.
- [2026-07-02] Correction: Claude Fable 5 returned online this same day after its export-control suspension. The "[banned]" / "[unavailable]" qualifiers on the FrontierSWE/DeepSWE and Code Arena benchmark lines above reflect the measurement window when those benchmarks were run (June 2026) and are not being restated as current.
- [2026-06-17] Released; MIT license; #1 open-weight Agent Arena; #1 Design Arena; #2 Code Frontend; Terminal-Bench 2.1: 81.0; supersedes GLM-5.1
```

No spill needed (4 entries, cap is 10).

### wiki/concepts/harness.md (updated)

Replace the "Model neutrality by design" bullet:

> **Before:**
> `- **Model neutrality by design.** Build your harness so the underlying model is a configurable parameter, not a hardcoded dependency. Routing, context packaging, and evaluation should live in the harness layer — not in model-specific prompt tricks. This became a risk management requirement (not just an engineering preference) after the Fable 5 export-control ban removed access to the leading frontier model for all customers overnight. The LangSmith Engine (a fine-tuned production-trace judge, 10-100× cheaper than frontier models) demonstrates that the evaluation layer can also be decoupled from frontier access.`
>
> **After:**
> `- **Model neutrality by design.** Build your harness so the underlying model is a configurable parameter, not a hardcoded dependency. Routing, context packaging, and evaluation should live in the harness layer — not in model-specific prompt tricks. This became a risk management requirement (not just an engineering preference) after the Fable 5 export-control ban removed access to the leading frontier model for all customers overnight — Fable 5 returned online 2026-07-02, about two weeks later, underscoring that the risk was disruption, not permanent loss. LangChain's LangSmith Engine, which automatically consumes production traces, clusters failures, identifies likely code issues, and proposes fixes and evals, demonstrates that the evaluation layer can also be decoupled from frontier access.`

### wiki/models/claude-opus-4-8.md (updated)

Replace the intro paragraph:

> **Before:**
> `Anthropic's current accessible flagship multimodal model. Released June 2026 alongside Dynamic Workflows. Supersedes Claude Opus 4.7 in the accessible tier; Fable 5 and Mythos remain restricted or unavailable in the current wiki state.`
>
> **After:**
> `Anthropic's flagship multimodal model, and the accessible tier that stayed available through Fable 5's export-control suspension. Released June 2026 alongside Dynamic Workflows, superseding Claude Opus 4.7. Fable 5 returned online 2026-07-02 with added safety fallback routing — some cyber, biology, and chemistry requests route to Opus 4.8 instead of Fable 5, which keeps Opus 4.8 relevant as more than a fallback-of-last-resort even with Fable 5 accessible again.`

Add one new Recent-changes entry (inserted at the top, since it is the newest event on this page):

```md
- [2026-07-02] Fable 5 returned online after its export-control suspension; Anthropic's safety fallback routing keeps some cyber/bio/chem requests on Opus 4.8, so this page's "unavailable" framing for Fable 5 no longer applies.
```

### wiki/models/composer-2-5.md (new)

```md
---
title: Composer 2.5
type: model
domains: [coding, models]
subcategory: coding-model
tags: [closed-source]
as_of: 2026-05-18
sources: [cursor-composer-2-5-launch]
---

# Composer 2.5

Composer 2.5 is Cursor's in-house long-horizon coding model, an upgrade of Composer 2 announced May 18, 2026. It keeps the same Moonshot Kimi K2.5 base as its predecessor but changes how it's trained: targeted reinforcement learning with textual hints inserted at specific trajectory failure points, plus KL distillation between a hinted teacher and an unhinted student, over 25× more synthetic tasks than Composer 2 — including a new "feature deletion" task type meant to test whether the model removes code correctly rather than only adding it.

## Current status (as of 2026-05-18)

- Same Kimi K2.5 base as Composer 2; upgrade is in training method and data, not base model
- Targeted RL with textual feedback (hints at problem trajectory points) plus KL distillation between a hinted teacher and unhinted student
- 25× more synthetic tasks than Composer 2, including a new "feature deletion" task type
- Sharded Muon + dual mesh HSDP optimizer; reported 0.2s step time on a 1T-parameter model
- Pricing: $0.50/M input, $2.50/M output standard; $3.00/M input, $15.00/M output fast variant
- Cursor's next model is training on a SpaceX partnership at Colossus 2 scale (targeting million H100-equivalents)
- Backs [Cursor](../tools/cursor.md)'s coding workspace; remains Cursor's separate, smaller-weight-class model alongside [Grok 4.5](grok-4-5.md), the jointly trained SpaceXAI model that launched in July 2026

## Strengths

- Purpose-built training data (feature-deletion tasks) targets a specific failure mode — models that only know how to add code
- Unusually low input-token pricing for a frontier-adjacent coding model

## Weaknesses / caveats

- Benchmarks and pricing come from Cursor's own launch post; no independent replication captured
- Available only inside Cursor products; no standalone API

## Recent changes

- [2026-05-18] Launched: upgrade from Composer 2, targeted RL + KL distillation training method, 25× synthetic tasks, new pricing tiers

## Sources

- [Cursor Composer 2.5 — launch post](../sources/articles/cursor-composer-2-5-launch.md)
```

### wiki/history/models/composer-2.md (new — spill)

```md
---
title: Composer 2 (archived)
type: model
domains: [coding, models]
subcategory: coding-model
tags: [closed-source]
as_of: 2026-03-23
sources: [cursor-3-launch, late-march-small-coding-models]
---

# Composer 2 (archived)

**Superseded by [Composer 2.5](../../models/composer-2-5.md) (May 2026).**

Composer 2 is Cursor's in-house coding model for complex long-horizon engineering work. It is no longer just a stub-level mention from the Cursor 3 launch: late-March sources add benchmark claims, pricing claims, and the now-disclosed fact that Cursor started from Moonshot's Kimi-k2.5 before doing continued pretraining and reinforcement learning.

## Historical status (as of 2026-03-23)

- Cursor positions Composer 2 as its own model for complex, long-term coding tasks
- Reported benchmark claims: 61.7 on TerminalBench 2.0 and 73.7 on SWE-bench Multilingual
- Source coverage says it trails GPT-5.4 slightly, but beats Anthropic's Opus 4.6 on those cited coding benchmarks
- Launch pricing claim in the source set: about `$0.50` per million input tokens, roughly one-tenth of some frontier competitors
- Later source coverage says Cursor did not train it from scratch: the model reportedly starts from Moonshot's open Kimi-k2.5, then adds continued pretraining plus Cursor-specific finetuning / RL
- Available only inside Cursor products; no standalone API

## Recent changes

- [2026-04-21] Late-March model coverage turned Composer 2 from a stub into a real current-state page with benchmark, pricing, and lineage claims
- [2026-04-02] Page created (stub) from a passing mention in the Cursor 3 launch post

## Sources

- [Meet the new Cursor (Cursor 3 launch)](../../sources/articles/cursor-3-launch.md)
- [Late-March small coding models](../../sources/newsletters/late-march-small-coding-models.md)
```

### wiki/models/gpt-5-5.md (updated)

`## Current status` — replace the SWE-Bench Pro comparison line:

> **Before:**
> `- Claude Opus 4.7 still leads on SWE-Bench Pro (64.3% vs 58.6%), MCP Atlas (79.1% vs 75.3%), and FinanceAgent (64.4% vs 60.0%)`
>
> **After:**
> `- At launch, Claude Opus 4.7 led on SWE-Bench Pro (64.3% vs 58.6%), MCP Atlas (79.1% vs 75.3%), and FinanceAgent (64.4% vs 60.0%); Opus 4.7 has since been superseded by Opus 4.8 (69.2% SWE-Bench Pro) and Claude Fable 5 (80.3% SWE-Bench Pro), both now ahead of GPT-5.5 on this metric`

Add one new Recent-changes entry (inserted at the top as the newest event on this page):

```md
- [2026-07-02] Noted that GPT-5.5's SWE-Bench Pro comparison against Opus 4.7 is now historical: Opus 4.8 (69.2%) and Claude Fable 5 (80.3%) have both since surpassed GPT-5.5's 58.6% on this benchmark.
```

### wiki/benchmarks/terminal-bench.md (updated)

`## Current status` — replace the leaderboard line and add a table:

> **Before:**
> `- Frontier models score below 65% (as reported; verify against current leaderboard)`
>
> **After:** (line removed; replaced by the table below, inserted immediately after this bullet list)

Add a new subsection after `## Current status` and before `## Why it matters`:

```md
## Current leaderboard (as of 2026-07-09)

Terminal-Bench has multiple non-comparable variants (2.0, 2.1, Hard); scores below are grouped by variant and should only be compared within the same row group. All numbers are vendor-reported on the linked model/tool page unless noted.

| Model | Variant | Score | As of |
|---|---|---|---|
| [Claude Fable 5](../models/claude-fable-5.md) | 2.1 | 88.0% | 2026-07-02 |
| [GLM-5.2](../models/glm-5-2.md) | 2.1 | 81.0% | 2026-06-17 |
| [Gemini 3.5 Flash](../tools/gemini.md) | 2.1 | 76.2% | 2026-05-20 |
| GPT-5.6 Sol | 2.1 | OpenAI claims a new state of the art; exact score not recoverable from the launch post | 2026-07-09 |
| [MiniMax M3](../models/minimax-m3.md) | 2.1 | 66.0% | 2026-06-02 |
| [GPT-5.5](../models/gpt-5-5.md) | 2.0 | 82.7% | 2026-05-06 |
| [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | 2.0 | 59.3% | 2026-05-01 |
| [Composer 2](../history/models/composer-2.md) (historical) | 2.0 | 61.7% | 2026-03-23 |
| [Claude Opus 4.8](../models/claude-opus-4-8.md) | Hard | gains reported; no exact score published | 2026-06-04 |
| [Cohere Command A+](../models/cohere-command-a-plus.md) | Hard | 3% → 25% (vs. Command A Reasoning) | 2026-05-21 |
```

`## Why it matters` — replace the second paragraph:

> **Before:**
> `The reported sub-65% frontier score on tasks that a competent systems engineer would often handle routinely reveals a meaningful gap between chat-style capability and real operational autonomy.`
>
> **After:**
> `Even the strongest frontier scores (Fable 5 at 88.0% on the 2.1 variant) leave meaningful room short of full reliability on tasks that a competent systems engineer would often handle routinely — a gap between chat-style capability and real operational autonomy that has narrowed since this page's original April synthesis but hasn't closed.`

Frontmatter — bump `as_of` and add sources for the new figures cited (all already present elsewhere in the wiki; adding the model/tool source ids that back the table rows not already covered by this page's existing sources):

```yaml
as_of: 2026-07-09
sources: [agents-evals-deep-research, terminal-bench-science-announcement, ainews-erdos-benchmarks-cluster-2026-05-21, ainews-fable5-june-2026, ainews-glm-52-june-2026, google-io-2026-search-blog, gpt-5-6-sol-preview-launch-2026-06, cohere-command-a-plus-launch]
```

### wiki/benchmarks/swe-bench.md (updated)

`## Current leaderboard` — replace the table and heading date:

> **Before:**
> ```md
> ## Current leaderboard (as of 2026-04-23)
>
> Scores are % of issues resolved. Higher is better.
>
> | Model | Variant | Score | As of |
> |---|---|---|---|
> | [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | SWE-bench Verified | 77.2% | 2026-04-23 |
> | [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | SWE-bench Pro | 53.5% | 2026-04-23 |
> | [Composer 2](../models/composer-2.md) | SWE-bench Multilingual | 73.7% | 2026-03-23 |
> | [MiniMax M2.7](../history/models/minimax-m2-7.md) | SWE-Pro | 56.22% | 2026-03-22 |
> | [Kimi K2.6](../history/models/kimi-k2-6.md) | SWE-bench (various) | SOTA claims | 2026-04-22 |
>
> *Note: claims are vendor-reported unless otherwise noted. Independent replication is not always available.*
> ```
>
> **After:**
> ```md
> ## Current leaderboard (as of 2026-07-09)
>
> Scores are % of issues resolved. Higher is better.
>
> | Model | Variant | Score | As of |
> |---|---|---|---|
> | [Claude Fable 5](../models/claude-fable-5.md) | Pro | 80.3% | 2026-07-02 |
> | [Claude Opus 4.8](../models/claude-opus-4-8.md) | Pro | 69.2% | 2026-06-04 |
> | [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | Verified | 77.2% | 2026-05-01 |
> | [MiniMax M3](../models/minimax-m3.md) | Pro | 59.0% | 2026-06-02 |
> | [GPT-5.5](../models/gpt-5-5.md) | Pro | 58.6% | 2026-05-18 |
> | [MAI-Thinking-1](../models/mai-thinking-1.md) | Pro | 53% | 2026-06-03 |
> | [Qwen 3.6 27B](../models/qwen-3-6-27b.md) | Pro | 53.5% | 2026-05-01 |
> | [Composer 2](../history/models/composer-2.md) (historical, superseded by [Composer 2.5](../models/composer-2-5.md)) | Multilingual | 73.7% | 2026-03-23 |
> | [MiniMax M2.7](../history/models/minimax-m2-7.md) (historical) | Pro | 56.22% | 2026-03-22 |
> | [Kimi K2.6](../history/models/kimi-k2-6.md) (historical) | various | SOTA claims | 2026-04-22 |
>
> *Note: claims are vendor-reported unless otherwise noted. Independent replication is not always available.*
> ```

Add one new Recent-changes entry:

```md
- [2026-07-09] Rebuilt the leaderboard from current model pages: added Claude Fable 5 (80.3% Pro) and Claude Opus 4.8 (69.2% Pro), both previously missing despite being current on `state-of/models.md`; repointed the Composer entry to Composer 2.5's supersession of Composer 2.
```

Frontmatter — bump `as_of`:

```yaml
as_of: 2026-07-09
```

### wiki/tools/claude-code.md (updated)

Frontmatter — bump `as_of` and add the new source:

```yaml
as_of: 2026-07-08
sources: [claude-code-monitor, claude-code-routines, claude-code-leak-architecture, claude-computer-use-late-march, anthropic-desktop-agent-expansion-late-march, coding-agents-review-and-orchestration-march, claude-code-scheduled-tasks-march, anthropic-persistent-workflow-surfaces-february, memory-vs-context-rot-february, thecode-april-22-2026, claude-code-worktree-autofix, claude-code-ultrareview, claude-code-one-time-scheduling, claude-code-product-management-2026-05-01, claude-code-goal-fastmode-fleetview-2026-05-13, claude-code-agent-view-2026-05-13, agent-native-product-management-2026-05-13, anthropic-claude-code-best-practices-2026-05, claude-code-fast-mode-default-2026-05, dynamic-workflows-claude-code, claude-code-getting-started-with-loops-2026-06-30, codex-general-work-agents-2026-07, ainews-opus-48-dynamic-workflows-2026-05, every-claude-dynamic-workflows-reliability-2026-06, claude-code-design-sync-2026-07, claude-sonnet-5-official-2026-06-30]
```

`## Current status` heading:

> **Before:** `## Current status (as of 2026-05-13)`
>
> **After:** `## Current status (as of 2026-07-08)`

Replace the fast-mode bullet:

> **Before:**
> `- Opus 4.7 fast mode (now default, as of 2026-05-19): was research preview; now the default mode for Claude Code; Cursor reports 2.5× faster output at approximately 6× the cost compared to standard Opus 4.7`
>
> **After:**
> `- Fast mode (introduced May 2026 as an Opus 4.7 research preview) has moved with the platform's model lineup since Opus 4.7 was superseded: Claude Sonnet 5 (Anthropic's most agentic Sonnet model) became available in Claude Code and via the API on 2026-06-30, alongside Claude Fable 5 (restored 2026-07-02 after a brief export-control suspension, with some cyber/bio/chem requests routed to Opus 4.8) and Opus 4.8 itself`

`## Recent changes` — full section, reordered newest-first with the new entry inserted and the oldest `[2026-05-13]` Opus-4.7-fast-mode entry spilled:

```md
## Recent changes

- [2026-07-08] Claude Code and Claude Design add bidirectional `/design-sync` between repo work and Claude Design canvases.
- [2026-07-01] Every frames Claude Code alongside Codex as a general-purpose agent harness spilling beyond software work when tasks can be represented as files, tools, and review artifacts.
- [2026-06-30] Anthropic published the official Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops, with guidance on matching loop primitive to task type and controlling token usage.
- [2026-06-30] Claude Sonnet 5 became available in Claude Code and via the API as `claude-sonnet-5`, alongside Claude Fable 5's return two days later — Claude Code's model lineup moved from a single fast-mode tier to multiple concurrently available models.
- [2026-06-18] Every case studies show Dynamic Workflows replacing manual subagent coordination for reviewer agents and large Figma-to-code work.
- [2026-05-28] Dynamic workflows added (research preview): the `ultracode` effort setting (xhigh) lets Claude write orchestration scripts running tens-to-hundreds of parallel subagents that plan, verify (with adversarial agents), and iterate to convergence on hours-to-days work; runs checkpoint and resume. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens.
- [2026-05-19] Fast mode promoted from research preview to default for Claude Code; Claude Console gains prompt cache diagnostics
- [2026-05-18] Anthropic engineering best practices: context window as #1 constraint; verification-criteria pattern; explore-plan-code workflow (plan mode + Ctrl+G); Chrome extension for UI screenshot verification
- [2026-05-13] /goal command added (research preview): autonomous loop until evaluator model confirms target met — first native long-horizon success-criterion primitive in Claude Code
- [2026-05-13] Agent View added (research preview, v2.1.139+): `claude agents` supervises background sessions with peek/reply, attach/detach, `/bg`, `--bg`, and worktree isolation.
```

`## Sources` — add one link:

```md
- [Claude Sonnet 5 — official launch](../sources/articles/claude-sonnet-5-official-2026-06-30.md)
```

### wiki/history/tools/claude-code.md (updated — spill append)

Insert a new block right after the intro line and before the existing `## Recent changes` heading:

```md
## Archived from current page on 2026-09-05

- [2026-05-13] Opus 4.7 fast mode added (research preview): 2.5× faster, ~6× cost per Cursor benchmarks; new latency/price tier
```

### wiki/tools/claude-managed-agents.md (updated)

Replace the intro paragraph:

> **Before:**
> `Claude Managed Agents is not yet documented here as a mature end-user product. At this point, the source reads more like an Anthropic architecture and platform direction: a hosted Claude Platform runtime for long-running agents built around three separate pieces, instead of one all-in-one agent container.`
>
> **After:**
> `Claude Managed Agents is a hosted Claude Platform runtime for long-running agents, in public beta, built around three separate pieces instead of one all-in-one agent container.`

Replace two lines in `## Weaknesses / caveats`:

> **Before:**
> `- The source is an engineering architecture post, not full product documentation`
>
> **After:** (line removed — the page's own Current status now documents a public beta with a dashboard, self-hosted sandboxes, and MCP tunnels, which contradicts describing the source as pre-product)

> **Before:**
> `- No pricing, availability tiering, or detailed public API surface is captured here`
>
> **After:** (line removed for the same reason; availability is documented as public beta with self-hosted sandboxes and dashboard management, even though granular pricing tiers specifically remain uncaptured — folded into the remaining "Reported latency improvements are vendor-internal numbers" caveat, which stays)

### wiki/tools/gpt-realtime-2.md (updated)

`## Current status` — replace the coming-soon line:

> **Before:**
> `- Live in the Realtime API as of May 8, 2026; ChatGPT voice upgrade "coming soon"`
>
> **After:**
> `- Live in the Realtime API as of May 8, 2026; ChatGPT Voice moved to a different model family, [GPT-Live](gpt-live.md), on 2026-07-07 — GPT-Realtime-2 remains the model for the Realtime API`

`## Weaknesses / caveats` — replace:

> **Before:**
> `- ChatGPT voice is still running the older model; upgrade date not announced`
>
> **After:** (line removed — resolved by the Current status update above)

Add one new Recent-changes entry:

```md
- [2026-07-07] ChatGPT Voice moved to GPT-Live-1/GPT-Live-1 mini, a separate full-duplex model family; GPT-Realtime-2 continues as the Realtime API's speech-to-speech model.
```

Frontmatter — add the new source and bump `as_of`:

```yaml
as_of: 2026-07-07
sources: [gpt-realtime-2-2026-05-08, gpt-live-launch-2026-07]
```

### wiki/concepts/agent-evals.md (updated)

Heading and intro sentence:

> **Before:**
> `## Five eval categories`
> `A useful agent eval suite covers five categories, each catching a different class of failure:`
>
> **After:**
> `## Seven eval dimensions`
> `A useful agent eval suite covers seven dimensions, each catching a different class of failure:`

### wiki/models/cosmos-3.md (updated)

Intro paragraph:

> **Before:**
> `NVIDIA's open-weight world model using a Mixture-of-Transformers (MoT) architecture — the first significant open model to combine an autoregressive language/reasoning component with a diffusion generation component in a single unified system. Claims #1 open-weight performance on both Text-to-Image and Image-to-Video leaderboards at launch, sitting close behind GPT-Image-2 (Nano Banana 2).`
>
> **After:**
> `NVIDIA's open-weight world model using a Mixture-of-Transformers (MoT) architecture — the first significant open model to combine an autoregressive language/reasoning component with a diffusion generation component in a single unified system. Claims #1 open-weight performance on both Text-to-Image and Image-to-Video leaderboards at launch, sitting just below OpenAI's GPT-Image-2 on Artificial Analysis's overall Text-to-Image leaderboard (a separate model from Google's Nano Banana 2, which GPT-Image-2 itself displaced at the top of that leaderboard).`

`## Current status` — replace the benchmarks bullet:

> **Before:**
> `- **Benchmarks:** Super variant — #1 open-weight on Text-to-Image leaderboard; #1 open-weight on Image-to-Video leaderboard (Artificial Analysis); just below Nano Banana 2 overall`
>
> **After:**
> `- **Benchmarks:** Super variant — #1 open-weight on Text-to-Image leaderboard; #1 open-weight on Image-to-Video leaderboard (Artificial Analysis); overall (not just open-weight) leaderboard position sits just below GPT-Image-2`

### wiki/tools/cartesia.md (updated)

`## Recent changes` — replace the 2026-06-16 entry:

> **Before:**
> `- [2026-06-16] Sonic-3.5 and Ink-2 launched; claim #1 TTS and STT positions via Together AI`
>
> **After:**
> `- [2026-06-16] Sonic-3.5 and Ink-2 first covered in this wiki (via AINews); claim #1 TTS and STT positions via Together AI. No earlier launch date for either model is documented in any source cited on this page — the 2026-05-23 entry below, reporting a Speech Arena #1 ranking for Sonic-3.5, predates this entry and implies Sonic-3.5 was already live by then.`

### wiki/training/ai-enablement-software-development.md (updated)

Replace the sentence citing the 47% figure:

> **Before:**
> `Anthropic's own internal study found a 47% drop in debugging ability among engineers using AI heavily.`
>
> **After:**
> `Anthropic's own internal study reportedly found a 47% drop in debugging ability among engineers using AI heavily, per Lars Faye's essay. A different secondary account of what may be the same Anthropic study is cited on [Anti-autopilot review friction](anti-autopilot-review-friction.md) as a 50%-vs-67% comprehension-quiz gap — the two figures haven't been reconciled against a primary source.`

### wiki/training/anti-autopilot-review-friction.md (updated)

Replace the sentence introducing the Anthropic comprehension study:

> **Before:**
> `- **Anthropic comprehension study:** Engineers learned a new Python library — half with AI assistance, half without. Both groups finished tasks at the same speed. But the AI group scored 50% on the follow-up comprehension quiz vs 67% for the manual group; the gap widened on debugging tasks. Within the AI group: engineers who used AI for conceptual questions scored above 65%; engineers who copy-pasted generated code scored under 40%. **Finding: the tool didn't determine the outcome — the posture did.**`
>
> **After:**
> `- **Anthropic comprehension study:** Engineers learned a new Python library — half with AI assistance, half without. Both groups finished tasks at the same speed. But the AI group scored 50% on the follow-up comprehension quiz vs 67% for the manual group; the gap widened on debugging tasks. Within the AI group: engineers who used AI for conceptual questions scored above 65%; engineers who copy-pasted generated code scored under 40%. **Finding: the tool didn't determine the outcome — the posture did.** (A different secondary account, cited on [AI enablement — software development](ai-enablement-software-development.md), gives a 47% debugging-ability drop for what may be the same underlying Anthropic study — the two haven't been reconciled against a primary source.)`

### wiki/tools/harvey.md (updated)

Frontmatter:

> **Before:** `as_of: 2026-04-02`
>
> **After:** `as_of: 2026-06-04`

### wiki/state-of/legal.md (updated)

Intro paragraph — remove the stale sentence:

> **Before:**
> `Current state of AI tools, models, and adoption inside legal practice — law firms, in-house teams, litigation, transactional work. Organized by subcategory.`
> `The picture here is very sparse — only one source ingested so far, and it is editorial.`
>
> **After:**
> `Current state of AI tools, models, and adoption inside legal practice — law firms, in-house teams, litigation, transactional work. Organized by subcategory.`

(the second sentence is deleted outright — three sources and three tools are now tracked)

Replace the Harvey line:

> **Before:**
> `- [Harvey](../tools/harvey.md) — legal AI platform; product surfaces include Assistant, Vault, Knowledge, Workflow Agents *(as of 2026-04-02)*`
>
> **After:**
> `- [Harvey](../tools/harvey.md) — legal AI platform; June 2026 hybrid-routing benchmark shows a GLM 5.1 + Opus 4.7 advisor combination reaching an 18% all-pass rate at ~60% lower cost than pure Opus 4.7 (14% all-pass) *(as of 2026-06-04)*`

Add a `## Sources` section (the page has none today) after `## Recent changes`:

```md
## Sources

- [Autonomous agents are transforming engineering. Legal is next. (Pereyra / Harvey)](../sources/articles/harvey-legal-is-next.md)
- [Wilson — homepage](../sources/articles/wilson-homepage.md)
- [Microsoft Word Legal Agent](../sources/articles/microsoft-word-legal-agent.md)
```

Frontmatter — bump `as_of`:

```yaml
as_of: 2026-06-04
```

### wiki/index.md (updated)

Harvey entry:

> **Before:**
> `- [tools/harvey](tools/harvey.md) — legal AI platform; thin stub from a single editorial source *(as_of: 2026-04-02)*`
>
> **After:**
> `- [tools/harvey](tools/harvey.md) — legal AI platform; June 2026 hybrid-routing benchmark shows a cost/accuracy win over pure-Opus routing *(as_of: 2026-06-04)*`

## Schema / vocabulary additions

None needed — every fix above reuses existing domains, subcategories, and tags.

## Open questions

- **A15 — Grok 4.5's predecessor name.** `wiki/state-of/models.md` says Grok 4.5 "replaces Grok 4.20, which had led Arena creative writing and hard prompts in May 2026," but `wiki/models/grok-4-5.md` consistently calls the predecessor "Grok 4.3" (three separate mentions: parameter count, context window, and Intelligence Index comparisons). The May 2026 Arena source (`wiki/sources/newsletters/arena-leaderboard-2026-05-13.md`) says "Grok 4.20 also strong in creative writing and hard prompts" — so "4.20" is the name that made it into the wiki from the Arena coverage, while "4.3" is the name used in Grok 4.5's own launch coverage. These may be the same release under an internal build number vs. a marketing version number, or genuinely different releases. Which name should the wiki standardize on, or should both be kept with a note that they may refer to the same model? No draft is included for this until it's resolved.

- **A16 — Claude Opus 4.8's release date.** `wiki/models/claude-opus-4-8.md` says in its intro and Current-status heading that it was "Released June 2026 alongside Dynamic Workflows" and "Released alongside Dynamic Workflows," but its own Recent changes has two different entries: `[2026-05-29] AINews launch coverage adds benchmark, pricing, efficiency, and calibration detail for Opus 4.8; Dynamic Workflows launched in Claude Code at the same time` and `[2026-06-03] Released; Dynamic Workflows and Figma MCP at launch; early practitioner pulse check by Every`. Both could be real and distinct (an announcement/launch-coverage date vs. a formal release date), or one could be an error. Which is correct, or does the page need clearer wording distinguishing "announced" from "released" rather than a single date fix? No draft is included for this until it's resolved.

- **A17 — "Meta Spark" vs. "Muse Spark."** `wiki/state-of/models.md`'s Coding models section has an unlinked bold entry, "**Meta Spark** — Meta; Arena (May 2026): leads coding category," sourced from `wiki/sources/newsletters/arena-leaderboard-2026-05-13.md` ("Coding: Meta Spark leads the coding category"). The Frontier models section separately links `[Muse Spark](../models/muse-spark.md)`, Meta's multimodal model from its Superintelligence Labs effort, sourced from a different article entirely (`wiki/sources/articles/muse-spark.md`) about scaling efficiency and personal superintelligence — that page makes no coding claims of any kind. I could not confirm from what's in the wiki whether "Meta Spark" is an informal/typo name for the same model as "Muse Spark," or whether it's a genuinely separate coding-specific product that was never given its own page. If they're the same, the two entries should merge; if not, "Meta Spark" may need its own stub page or should stay as an unlinked entry pending its own investigation. No draft is included for this until it's resolved.
