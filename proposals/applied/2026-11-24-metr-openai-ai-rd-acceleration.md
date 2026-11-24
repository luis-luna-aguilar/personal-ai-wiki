---
type: proposal
source: raw/articles/2026-11-24-metrorg-blog-2026-11-05-anthropic-ai-rd-acceleration-assessm.md
sources:
  - raw/articles/2026-11-24-metrorg-blog-2026-11-05-anthropic-ai-rd-acceleration-assessm.md
  - raw/articles/2026-11-24-openaicom-index-research-acceleration-jagged-frontier.md
  - raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
status: pending
created: 2026-11-24
---

# Proposal: METR's Anthropic assessment and OpenAI's November acceleration report

## Summary

### In short
AI is now measurably speeding up AI research: METR, given inside access, estimates Anthropic is improving its models about twice as fast as in 2024–25, mostly because of its own AI use, and sees no bottleneck stopping further compounding. OpenAI's November report shows uneven uplift: agents now finish 46% of two-to-four-hour research tasks alone, though OpenAI does not yet claim its capability index is accelerating. The proposal adds both to AGI timeline claims and the disclosure norm to AI governance and policy. One reason to hesitate: AGI timeline claims was built for leaders' dated milestones, so this widens its scope and takes it near its length limit.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
METR, the independent evaluator, spent August to October 2026 inside Anthropic with unusual access: internal metrics on pretraining and reinforcement learning, compute by domain, internal benchmark scores, speed-up analyses and staff interviews. Its 5 November report concludes that Anthropic is likely improving its models on well-specified tasks at about twice its March 2024 to October 2025 rate, with a plausible range of 1.3x to 3x. The clearest public evidence is AECI, Anthropic's version of the Epoch Capabilities Index, which has grown 1.9 times faster since October 2025. METR ruled out faster compute scaling as the cause, attributes perhaps 80% of today's acceleration to Anthropic's own AI use (mostly assistance, not autonomous work), and found no bottleneck for the next year. The catch is that Anthropic redacted most of the evidence METR found most informative. An Every newsletter adds that the AI 2027 forecasters read the result as putting the world five months ahead of their timeline.

OpenAI's report of 18 November is its second on the subject. Between March and October, agents' success without human help rose from 23% to 46% on research tasks of two to four hours, but "jagged": 79% for monitoring training runs, 25% for inference code. The median researcher now uses $2,400 of agent time a day at list prices, the top tenth $23,000. Its internal capability index rose 16.4 points a year against Epoch's 14-point trend, and OpenAI says it is still watching for acceleration. It repeats that labs should be required to report indicators of recursive self-improvement, noting that Anthropic, Google DeepMind and METR now publish such measurements.

### What changes
AGI timeline claims currently tracks only lab leaders' dated milestones, with OpenAI's September report (intern goal reached, March 2028 target) as the newest; nothing measures acceleration from outside.

- **AGI timeline claims** gains two signals, METR on Anthropic and OpenAI's November report; the September bullet drops its adoption figures, which the November numbers replace. Two Recent-changes entries; page date moves to 18 November.
- **AI governance and policy** records that the disclosure call has become a practice across labs, and that METR's redactions show its limit. One Recent-changes entry; page date moves to 18 November.
- **Index** descriptions and dates for both pages.
- Three source pages: METR, OpenAI, and an Every story page.

### What to weigh
The main judgment is scope and length. AGI timeline claims was built to track lab leaders' dated milestones; adding outside and lab-published measurements widens it to the evidence behind those claims, rather than starting a separate page, and brings its body to about 1,300 words, just inside the warning band above its 1,200-word ceiling, so no split is proposed now. The METR report was read in full except its long methodology appendices. The Every issue of 19 November, also on the triage signal, is not used: OpenAI's own report replaces it and gives $23,000 rather than its rounded $25,000.

## Intended changes

- [ ] **Update** `wiki/trends/agi-timeline-claims.md` — intro sentence widened to cover acceleration measurements; September bullet trimmed; two new Current-signal bullets; one What-to-watch bullet; adds two Recent-changes entries dated 2026-11-18 and 2026-11-05 (eight entries, no spill); three source ids and three Sources links appended; `as_of` 2026-09-06 → 2026-11-18
- [ ] **Update** `wiki/trends/ai-governance-and-policy.md` — Current-signal paragraph and stamp updated; one paragraph appended to "Labs calling for mandatory progress disclosure"; adds one Recent-changes entry dated 2026-11-18 (five entries, no spill); two source ids and two Sources links appended; `as_of` 2026-09-29 → 2026-11-18
- [ ] **Update** `wiki/index.md` — descriptions and dates for both trend pages
- [ ] **Create** `wiki/sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md`
- [ ] **Create** `wiki/sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md`
- [ ] **Create** `wiki/sources/newsletters/every-metr-ai-2027-ahead-2026-11-13.md` — story page for the Every item

## Page drafts

### wiki/trends/agi-timeline-claims.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-11-18
sources: [... existing ids ..., metr-anthropic-ai-rd-acceleration-2026-11-05, openai-research-acceleration-jagged-frontier-2026-11-18, every-metr-ai-2027-ahead-2026-11-13]
```

Intro paragraph — append one sentence at the end:

```
It also tracks measurements of how much AI is speeding up AI research itself, the evidence these claims increasingly rest on.
```

`## Current signal` — replace the 2026-09-06 OpenAI bullet with:

```
- **OpenAI confirms the "automated research intern" goal reached, names a March 2028 target for a full automated AI researcher (as of 2026-09-06):** OpenAI's own research-acceleration report states it has "now reached the goal, announced last fall, of having an automated research intern by September of this year" and that it is "making strong progress toward creating an automated AI researcher by March of 2028" — the first specific date attached to that longer-term milestone. Its adoption figures are replaced by the November report below. See [Research acceleration: The view inside OpenAI](../sources/articles/openai-research-acceleration-2026-09-06.md).
```

`## Current signal` — append two bullets at the end of the list:

```
- **METR measures AI-driven acceleration at Anthropic: about 2x (as of 2026-11-05):** After a high-access assessment inside Anthropic (12 August to 29 October), METR concluded Anthropic is likely improving its models on well-specified tasks at about twice its March 2024–October 2025 rate (plausible range 1.3x to 3x). Scores on AECI, Anthropic's version of the Epoch Capabilities Index, have grown 1.9x faster since October 2025, and training-compute growth did not speed up; the measured acceleration is smaller when other labs' models are included, partly because Anthropic's earlier growth lagged the industry frontier. METR attributes perhaps 80% of the current acceleration to Anthropic's own AI use, mostly assistance rather than autonomous work, and found no clear bottleneck for the next 12 months, so further compounding is a significant risk. Anthropic redacted most of the evidence METR found most informative. The AI 2027 authors read the result as putting the world about five months ahead of their forecast. See [METR's assessment](../sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md).
- **OpenAI's November report: jagged uplift, acceleration not yet claimed (as of 2026-11-18):** From March to October, agents' success without human help rose from 23% to 46% on two-to-four-hour research tasks and from 13% to 35% on four-to-eight-hour ones, unevenly: 79% for monitoring training runs, 25% for inference code. Median researcher agent use reached $2,400 a day at list prices (90th percentile $23,000). OpenAI's internal capability index has risen 16.4 points a year since August 2025, against Epoch's 14-point trend; OpenAI is still watching for acceleration. People came up with nearly all key ideas behind GPT-6 Astra and GPT-6.2 Astra; GPT-6.2 Astra's pretraining is the first where Codex was credited with insights. See [Research acceleration: The jagged frontier](../sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md).
```

`## What to watch` — append one bullet:

```
- Whether outside acceleration assessments like METR's spread to other labs, and whether OpenAI's capability index starts to bend upward the way Anthropic's has
```

`## Recent changes` — adds two entries at the top (eight entries, no spill):

```
- [2026-11-18] OpenAI's second research-acceleration report: agents now complete 46% of two-to-four-hour research tasks alone (23% in March), uplift is uneven by task, and OpenAI does not yet claim its capability index is accelerating; September adoption figures replaced.
- [2026-11-05] METR's high-access assessment finds Anthropic improving its models about 2x faster than in 2024–25 (range 1.3x–3x), mostly due to its own AI use, with no bottleneck in sight; most supporting evidence redacted by Anthropic.
```

`## Sources` — appends three links:

```
- [METR — Independent assessment of AI R&D acceleration at Anthropic](../sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md)
- [Research acceleration: The jagged frontier](../sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md)
- [Every — METR finding and AI 2027 reaction (Nov 13)](../sources/newsletters/every-metr-ai-2027-ahead-2026-11-13.md)
```

### wiki/trends/ai-governance-and-policy.md (updated)

Frontmatter (changed fields only):

```
as_of: 2026-11-18
sources: [... existing ids ..., metr-anthropic-ai-rd-acceleration-2026-11-05, openai-research-acceleration-jagged-frontier-2026-11-18]
```

`## Current signal (as of 2026-09-29)` → `## Current signal (as of 2026-11-18)`; in its second paragraph, replace the sentence `On 2026-09-06 OpenAI repeated its position that AI companies should be *required* to publicly track their progress toward recursive self-improvement.` with:

```
On 2026-09-06 and again on 2026-11-18 OpenAI repeated its position that AI companies should be *required* to publicly track their progress toward recursive self-improvement, by which point labs and METR had begun publishing such measurements.
```

`## Labs calling for mandatory progress disclosure` — append one paragraph:

```
OpenAI's 18 November follow-up repeats the call, now phrased as tracking and publicly reporting "indicators of recursive self-improvement," and points to a measurement norm forming across labs: Anthropic has published three internal acceleration reports, Google DeepMind's Gemini 4 Argon safety report tracks the share of AI-written code, and METR published an outside assessment of Anthropic on 5 November. METR's report also shows the limit of disclosure through a third party: Anthropic redacted most of the evidence METR relied on, so METR says the public has to lean on its judgment rather than weigh the evidence itself, and Anthropic dropped the planned check of its compute split between capabilities and safety midway through. The measurements are summarised on [AGI timeline claims](agi-timeline-claims.md).
```

`## Recent changes` — adds one entry at the top (five entries, no spill):

```
- [2026-11-18] OpenAI repeats its call for mandatory reporting of recursive-self-improvement indicators as Anthropic, Google DeepMind and METR publish acceleration measurements; METR's Anthropic assessment (2026-11-05) shows the limit of third-party disclosure, with most key evidence redacted.
```

`## Sources` — appends two links:

```
- [METR — Independent assessment of AI R&D acceleration at Anthropic](../sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md)
- [Research acceleration: The jagged frontier](../sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md)
```

### wiki/index.md (updated)

Replace the two trend lines with:

```
- [trends/agi-timeline-claims](trends/agi-timeline-claims.md) — dated, named AGI/major-capability-milestone claims from lab leadership (OpenAI's Astra/Pachocki, Altman's December 2026 estimate) and measurements of AI speeding up AI R&D (METR's ~2x at Anthropic, OpenAI's jagged-frontier report), plus the "chart psychosis" benchmark-framing critique for reading such claims; distinct from restricted-deployment withholding *(as_of: 2026-11-18)*
- [trends/ai-governance-and-policy](trends/ai-governance-and-policy.md) — pressure for governments to actively steer AI development (disclosure mandates and the emerging practice of publishing AI R&D acceleration measurements, pre-release review, equity-stake proposals, "Pacing the Frontier" embedded evaluators, UN Security Council session) rather than leaving it to labs and market forces *(as_of: 2026-11-18)*
```

### wiki/sources/articles/metr-anthropic-ai-rd-acceleration-2026-11-05.md (new)

```
---
title: "METR — Independent Assessment of AI R&D Acceleration at Anthropic in October 2026"
type: source
source_type: article
source_file: raw/articles/2026-11-24-metrorg-blog-2026-11-05-anthropic-ai-rd-acceleration-assessm.md
url: https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/
published: 2026-11-05
ingested: 2026-11-24
domains: [models]
---

# METR — Independent Assessment of AI R&D Acceleration at Anthropic in October 2026

METR's report on a high-access evaluation inside Anthropic (12 August to 29 October 2026) of how much AI is accelerating Anthropic's own AI development. Anthropic had redaction rights and used them on most of the evidence METR found most informative; METR lists what it could and could not discuss.

## Influenced pages

- [AGI timeline claims](../../trends/agi-timeline-claims.md) — outside measurement of ~2x acceleration at Anthropic
- [AI governance and policy](../../trends/ai-governance-and-policy.md) — third-party acceleration reporting and the limits redaction puts on it

## Key claims extracted

- As of October 2026, Anthropic is likely improving its models on well-specified tasks at ~2x its March 2024–October 2025 rate; would not be surprised by 1.3x or 3x
- AECI (Anthropic's version of the Epoch Capabilities Index) has grown 1.9x faster since October 2025 [95% CI 1.5–2.8x]: about two years of historical progress in one
- Acceleration was not caused by faster growth in training compute
- Perhaps ~80% of the current acceleration is due to AI; late-2025 acceleration likely had non-AI causes too
- R&D is accelerated mainly through AI assistance rather than autonomous contributions, with signs autonomous work will grow
- No clear bottleneck (algorithms, training compute, experiment compute, data) found for the next 12 months; significant risk of further acceleration
- AECI acceleration estimates range 1.1x–2.9x depending on modelling assumptions, and are lower when non-Anthropic models are included; Anthropic's pre-2025 growth lagged the industry frontier
- Anthropic cancelled the planned verification of its compute allocation between capabilities and safety midway through the engagement
- Limitations cut both ways: AECI's focus on verifiable tasks and possible benchmark overfitting vs. lagging, sparse data points
```

### wiki/sources/articles/openai-research-acceleration-jagged-frontier-2026-11-18.md (new)

```
---
title: "Research acceleration: The jagged frontier"
type: source
source_type: article
source_file: raw/articles/2026-11-24-openaicom-index-research-acceleration-jagged-frontier.md
url: https://openai.com/index/research-acceleration-jagged-frontier/
published: 2026-11-18
ingested: 2026-11-24
domains: [models, agents]
---

# Research acceleration: The jagged frontier

OpenAI's second report on how coding agents are changing its own research, organised as inputs (agent use), process (delegation, success rates, researcher views) and outputs (code, experiments, an internal capability index). Its headline is that uplift is real but uneven by task, and humans remain central.

## Influenced pages

- [AGI timeline claims](../../trends/agi-timeline-claims.md) — November acceleration data, replacing the September adoption figures
- [AI governance and policy](../../trends/ai-governance-and-policy.md) — repeated call for mandatory reporting of RSI indicators; cross-lab measurement norm

## Key claims extracted

- Agent success without intervention, March → October: 23% → 46% on 2–4-hour tasks, 13% → 35% on 4–8-hour tasks
- By task: 79% monitoring training runs, 72% answering technical questions, 35% launching training runs, 29% building eval/RL/agent environments, 25% inference and serving code
- Median researcher agent use $2,400/day at API list prices (up 62% from September); 90th percentile $23,000/day (up 105%)
- Agent workdays per researcher rose from 0.5 to 5.7; over two-thirds of researchers peak at four or more concurrent agents daily
- API-equivalent agent spend is about twice non-equity research compensation; internal deployment is 2% of research compute
- Survey (101 staff): median researcher would trade 40% of team headcount or 30% of team compute to keep frontier coding agents for three months
- Safety and Alignment had the largest absolute increase in documented research effort (+77% workweeks, January–September)
- OpenAI ECI frontier up 16.4 points/year since August 2025 vs. Epoch's 14 points/year trend; no claim of acceleration yet
- Key ideas behind GPT-6 Astra and GPT-6.2 Astra came from people; for GPT-6.2 Astra pretraining, researchers credited Codex with insights
- Repeats that labs should be required to track and publicly report indicators of recursive self-improvement; cites Anthropic's three reports, Gemini 4 Argon's safety report and METR's assessment
```

### wiki/sources/newsletters/every-metr-ai-2027-ahead-2026-11-13.md (new)

```
---
title: "Every — METR's acceleration finding and the AI 2027 reaction (Nov 13)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
published: 2026-11-13
ingested: 2026-11-24
domains: [models]
---

# Every — METR's acceleration finding and the AI 2027 reaction (Nov 13)

A news item in Every's "Your Attention Is AI's New Bottleneck" issue summarising METR's Anthropic assessment and the AI 2027 authors' reaction.

## Influenced pages

- [AGI timeline claims](../../trends/agi-timeline-claims.md) — AI 2027 authors' "five months ahead" reading

## Key claims extracted

- METR: Anthropic's models are improving about twice as fast as from March 2024 to October 2025, mostly because Anthropic uses its own AI
- The AI 2027 authors say this puts the world about five months ahead of their timeline
- Every's take: if models had a six-month shelf life, METR's estimate suggests it may now be closer to three months
```

## Schema / vocabulary additions

None.

## Open questions

None.
