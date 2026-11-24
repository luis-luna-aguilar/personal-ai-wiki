---
type: proposal
source: raw/articles/2026-11-24-anthropiccom-news-accenture-embedded-evaluation.md
sources:
  - raw/articles/2026-11-24-anthropiccom-news-accenture-embedded-evaluation.md
  - raw/articles/2026-11-24-aievaluatorforumorg-initiatives-minimum-operating-conditions.md
  - raw/articles/2026-11-24-darioamodeicom-post-we-must-pace-the-frontier.md
  - raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
status: pending
created: 2026-11-24
---

# Proposal: Third-party frontier evaluation — Anthropic and Accenture, AEF-1, and the rest of Amodei's pacing plan

## Summary

### In short
Independent evaluation of frontier models now has real money behind it but no settled rules for independence: Anthropic and Accenture each expect to put at least $1B over five years into embedded evaluators, while the closest thing to rules is the AI Evaluator Forum's AEF-1 checklist. Amodei's essay also spells out pacing steps two and three, coordination among democratic labs and then with China. The proposal updates Agent safety and alignment research and AI governance and policy, and adds four source pages. The one reason to hesitate: the safety page lands at about 110% of its length ceiling, at the top of the warning band.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
In mid-September 2026 Dario Amodei published "We Must Pace the Frontier", a personal essay arguing that AI building AI has sped progress up since the summer and that capability gains must be slowed so safety work can keep up. It sets out three steps. First, embedded evaluators: outside teams with employee-like access who verify a lab keeps its safety commitments and report incidents, which Anthropic commits to on its own. Second, democratic coordination: labs in democratic countries agree common safety standards and limits on the rate of progress, ideally through regulation, and in parallel through voluntary standards that need a narrow US antitrust waiver. He prefers pacing by capability checkpoints (a model able to do X must come with evidence of alignment) over caps on inputs such as compute. Third, global coordination with China, ranked from feasible to unlikely: bans on narrow uses such as bioweapons, mutual pre-release testing, a speed limit on self-improvement, a full pause.

On 18 September Anthropic named its first embedded-evaluation partner: Accenture, with the work led by its specialist unit Faculty. Anthropic pays Accenture directly because pooled or government funding does not exist yet. The deal is non-exclusive, and METR is piloting the approach on its own funding. AINews reported the reaction as mixed to hostile: critics doubted a consulting firm should red-team models, and Transluce said the conditions for independence are the real question.

Those conditions are what AEF-1 addresses. First published in December 2025 and promoted by the Forum the week of the essay, it is a checklist that evaluators publish with their results, covering access, conflicts of interest, analytic autonomy, transparency and sensitive information. METR, Transluce, SecureBio and Fangcun AI have used it, and the EU AI Office has endorsed key provisions.

### What changes
Before this, the wiki recorded only the first step of the pacing plan (embedded evaluators) and nothing on who would do the evaluating or under what rules.

- **Agent safety and alignment research** gains one bullet on the Accenture deal, its funding model and reception, and AEF-1; one "What to watch" item; one Recent-changes entry dated 18 September. Page date stays 15 November.
- **AI governance and policy** gains one paragraph on steps two and three of the plan and the Accenture partner, a rewritten "What to watch" item, and two Recent-changes entries (14 and 18 September). Page date stays 18 November.
- Four new source pages: the Anthropic post, the AEF-1 page, the essay, and the AINews reaction item.

### What to weigh
The essay carries no date; 14 September is inferred because the AI Evaluator Forum reacted to "recent statements" that day and AINews covered it on the 15th. The AEF-1 adoption list (including the EU AI Office endorsement) comes from the Forum's page as fetched on 24 November, with no date on the endorsement.

## Intended changes

- [ ] **Update** `wiki/trends/agent-safety-and-alignment-research.md` — add one bullet at the end of `### Alignment research and evaluation`; add one "What to watch" item; add three source ids to frontmatter and three links to body Sources; adds one Recent-changes entry dated 2026-09-18 (list goes from 8 to 9, no spill); `as_of` unchanged (2026-11-15)
    > See draft below

- [ ] **Update** `wiki/trends/ai-governance-and-policy.md` — add one paragraph to `## Frontier lab employees push for a "pacing" mechanism`, directly after the Thariq paragraph and before the UN Security Council paragraph; replace the "Pacing the Frontier" "What to watch" item; add two source ids and links; adds two Recent-changes entries dated 2026-09-18 and 2026-09-14 (list goes from 5 to 7, no spill); `as_of` unchanged (2026-11-18)
    > See draft below

- [ ] **Create** `wiki/sources/articles/anthropic-accenture-embedded-evaluation-2026-09-18.md` — source summary

- [ ] **Create** `wiki/sources/articles/aef-1-minimum-operating-conditions.md` — source summary

- [ ] **Create** `wiki/sources/articles/amodei-we-must-pace-the-frontier-2026-09-14.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/ainews-accenture-evaluation-reaction-2026-09-19.md` — source summary (story-specific page for this newsletter)

## Page drafts

### wiki/trends/agent-safety-and-alignment-research.md (updated)

Frontmatter `sources:` — append `anthropic-accenture-embedded-evaluation-2026-09-18, aef-1-minimum-operating-conditions, ainews-accenture-evaluation-reaction-2026-09-19`. `as_of` unchanged.

New bullet, appended at the end of `### Alignment research and evaluation` (after the Anthropic and UK AISI bullet):

```
- **Third-party evaluation gets funding and a baseline standard (September 2026):** Anthropic partnered with Accenture, its first step toward embedding outside evaluators with employee-like access (see [AI governance and policy](ai-governance-and-policy.md)). Accenture's AI unit Faculty leads the red-teaming, alignment assessments and safeguard testing, and each company expects to invest at least $1B over five years. Anthropic pays Accenture directly because no pooled or government funding exists; the deal is non-exclusive, METR is piloting the approach on its own funding, and no standard yet says what embedded evaluators may see or how they report. Critics asked whether a consulting firm should red-team models; Transluce said the conditions for independence are the real issue. The nearest thing to those conditions is the AI Evaluator Forum's AEF-1 (version 1, December 2025): a published checklist of minimum conditions on access, conflicts of interest, analytic autonomy, transparency and sensitive information. METR, Transluce, SecureBio and Fangcun AI have used it, and the EU AI Office has endorsed key provisions for the independence rules of the General-Purpose AI Code of Practice.
```

`## What to watch` — append one item:

```
- Which further embedded evaluators Anthropic names, whether other labs sign similar deals, and whether AEF-1 or another standard becomes the test of their independence
```

`## Recent changes` — adds one entry dated 2026-09-18, inserted between the 2026-09-29 and 2026-09-08 entries:

```
- [2026-09-18] Anthropic and Accenture (Faculty-led) partner on embedded frontier-model evaluation, each expecting to invest at least $1B over five years; AI Evaluator Forum's AEF-1 recorded as the baseline for evaluator independence.
```

`## Sources` — append:

```
- [Anthropic — Partnering with Accenture on embedded evaluation](../sources/articles/anthropic-accenture-embedded-evaluation-2026-09-18.md)
- [AI Evaluator Forum — AEF-1: Minimum Operating Conditions for Independent Third-Party AI Evaluations](../sources/articles/aef-1-minimum-operating-conditions.md)
- [AINews — Reaction to the Anthropic–Accenture evaluation partnership](../sources/newsletters/ainews-accenture-evaluation-reaction-2026-09-19.md)
```

### wiki/trends/ai-governance-and-policy.md (updated)

Frontmatter `sources:` — append `amodei-we-must-pace-the-frontier-2026-09-14, anthropic-accenture-embedded-evaluation-2026-09-18`. `as_of` unchanged.

New paragraph in `## Frontier lab employees push for a "pacing" mechanism`, inserted directly after the paragraph that begins "Dario Amodei's "Pacing the Frontier" post moved the idea toward a proposal" and before the UN Security Council paragraph:

```
Amodei's essay "We Must Pace the Frontier" (September 2026) lays out three steps. Embedded evaluators come first and are the one Anthropic is taking alone; its first partner is Accenture, through its Faculty unit (see [Agent safety and alignment research](agent-safety-and-alignment-research.md)). Step two, **democratic coordination**, has frontier companies in democratic countries agree common safety standards and limits on the rate of unchecked progress. Amodei prefers regulation covering every US frontier company; in parallel, companies would set standards voluntarily, which needs a narrow US antitrust waiver. He favours pacing by capability checkpoints (a model with a given capability must come with certified alignment evidence from evals, interpretability or audits of training environments) over limits on inputs such as compute, which he considers easier to game. Step three, **global coordination**, means democracies trying to coordinate with authoritarian governments, chiefly China, while taking verification seriously. He ranks possible agreements by difficulty: bans on narrow dangerous uses such as bioweapons; mutual pre-release testing for acute risks through a global standards body; a SALT-style speed limit on recursive self-improvement; and a full pause, which he thinks unlikely soon. Because pacing inside democracies is capped by the US lead over China, he pairs it with chip export controls.
```

`## What to watch` — replace the item:

> **Before:** `- Whether "Pacing the Frontier" moves beyond embedded evaluators at one lab to binding coordination between labs or governments, given the US rejection of a global regulator`

```
- Whether pacing moves beyond embedded evaluators to Amodei's steps two and three: regulation or voluntary standards among US labs (which need an antitrust waiver), and any US–China agreement, starting with the narrow-use bans and pre-release testing he calls feasible, given the US rejection of a global regulator
```

`## Recent changes` — adds two entries, inserted between the 2026-09-29 and 2026-09-06 entries (newest first):

```
- [2026-09-18] Anthropic names Accenture (led by its Faculty unit) as the first embedded-evaluator partner; both expect to invest at least $1B over five years.
- [2026-09-14] Amodei's "We Must Pace the Frontier" details steps two (democratic coordination: regulation or antitrust-waived voluntary standards, capability checkpoints) and three (global coordination with China, from narrow-use bans to a self-improvement speed limit).
```

`## Sources` — append:

```
- [Dario Amodei — We Must Pace the Frontier](../sources/articles/amodei-we-must-pace-the-frontier-2026-09-14.md)
- [Anthropic — Partnering with Accenture on embedded evaluation](../sources/articles/anthropic-accenture-embedded-evaluation-2026-09-18.md)
```

### wiki/sources/articles/anthropic-accenture-embedded-evaluation-2026-09-18.md (new)

```
---
title: Anthropic — Partnering with Accenture on embedded evaluation
type: source
source_type: article
source_file: raw/articles/2026-11-24-anthropiccom-news-accenture-embedded-evaluation.md
url: https://www.anthropic.com/news/accenture-embedded-evaluation
published: 2026-09-18
ingested: 2026-11-24
domains: [agents, models]
---

# Anthropic — Partnering with Accenture on embedded evaluation

Anthropic's announcement of its first embedded-evaluation partner, the first step of the pacing plan in Dario Amodei's "We Must Pace the Frontier". Faculty, Accenture's specialist AI business, will evaluate and red-team Anthropic's models, run alignment assessments and test safeguards, with employee-like access. Publication date taken from Anthropic's announcement post on X (18 September 2026).

## Influenced pages
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — third-party evaluation bullet
- [AI governance and policy](../../trends/ai-governance-and-policy.md) — first embedded-evaluator partner named

## Key claims extracted
- Anthropic and Accenture each expect to invest at least $1B over five years in independent-evaluation capacity
- Faculty leads the work: model evaluation and red-teaming, alignment assessments, safeguard testing
- Embedded evaluators get access comparable to an employee's: watch training, follow deployment decisions, talk to staff, report incidents
- No standards yet exist for what embedded evaluators may access or how they report; no settled funding system
- Anthropic funds Accenture directly; long-term it wants pooled or government funding (per its June Advanced AI Framework)
- METR and other nonprofits are in dialogue to pilot embedded evaluation with their own funding
- Partnership is non-exclusive on both sides; more evaluators to be announced
```

### wiki/sources/articles/aef-1-minimum-operating-conditions.md (new)

```
---
title: 'AI Evaluator Forum — AEF-1: Minimum Operating Conditions for Independent Third-Party AI Evaluations'
type: source
source_type: article
source_file: raw/articles/2026-11-24-aievaluatorforumorg-initiatives-minimum-operating-conditions.md
url: https://aievaluatorforum.org/initiatives/minimum-operating-conditions
published: 2025-12-04
ingested: 2026-11-24
domains: [agents, models]
---

# AI Evaluator Forum — AEF-1

The AI Evaluator Forum's first standard: a minimum floor of operating conditions for independent third-party AI evaluations, with a checklist evaluators publish alongside their results (documenting any conditions not met, and why). Version 1 is dated 4 December 2025; the Forum promoted it again on 14 September 2026 in response to the embedded-evaluator proposals. The adoption list was read from the page as fetched on 2026-11-24.

## Influenced pages
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — AEF-1 as the baseline for evaluator independence

## Key claims extracted
- Five principles: sufficient access and resources; minimized conflicts of interest; analytic autonomy; transparent methods and results; protection of sensitive information
- Conditions include safe harbor, contingent-compensation and recusal rules, editorial control, no contingent release of results, and redaction disclaimers
- Used by Transluce (mental-health evaluation of 77 model variants, Aug 2026), METR (Frontier Risk Report, May 2026), SecureBio (GPT-6 Astra biosecurity pre-release assessment, Sep 2026) and Fangcun AI (loss-of-control and manipulation evaluation, Oct 2026)
- The EU AI Office has endorsed key AEF-1 provisions as a way to comply with the independence provisions of the General-Purpose AI Code of Practice
```

### wiki/sources/articles/amodei-we-must-pace-the-frontier-2026-09-14.md (new)

```
---
title: Dario Amodei — We Must Pace the Frontier
type: source
source_type: article
source_file: raw/articles/2026-11-24-darioamodeicom-post-we-must-pace-the-frontier.md
url: https://darioamodei.com/post/we-must-pace-the-frontier
published: 2026-09-14
ingested: 2026-11-24
domains: [models, agents]
---

# Dario Amodei — We Must Pace the Frontier

Personal essay by Anthropic's CEO arguing that capability gains must be slowed so risk prevention can keep up, because AI-driven self-improvement has sped progress since the summer and the OpenAI–Hugging Face incident showed agents acting far outside their task. It proposes a three-step pacing plan. The page carries no date; 2026-09-14 is inferred from the AI Evaluator Forum's same-day response and AINews coverage on 2026-09-15.

## Influenced pages
- [AI governance and policy](../../trends/ai-governance-and-policy.md) — steps two and three of the pacing plan

## Key claims extracted
- Step 1, embedded evaluators: ongoing employee-like access for third-party teams (e.g. METR) to verify safety practices, report incidents and assess training pipelines; Anthropic commits unilaterally
- Step 2, democratic coordination: common safety standards and limits on unchecked progress among labs in democracies; regulation covering all US frontier companies preferred, voluntary standards in parallel with a narrow US antitrust waiver
- Preferred pacing mechanism: capability checkpoints (capability X requires certified alignment properties from evals, interpretability, training-environment audits); input limits such as compute considered more gameable
- Pacing within democracies is capped by the US lead over China; paired with chip and equipment export controls
- Step 3, global coordination, four levels by difficulty: narrow-use bans (bioweapons), mutual pre-release testing via a global standards body, a SALT-style speed limit on recursive self-improvement, a full pause (unlikely soon)
```

### wiki/sources/newsletters/ainews-accenture-evaluation-reaction-2026-09-19.md (new)

```
---
title: AINews — Reaction to the Anthropic–Accenture evaluation partnership
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
url: https://www.latent.space/p/ainews-here-are-6-clones-of-jev-in
published: 2026-09-19
ingested: 2026-11-24
domains: [agents]
---

# AINews — Reaction to the Anthropic–Accenture evaluation partnership

The "AI Safety, Evaluation Governance" item of the 19 September 2026 AINews issue, covering the Anthropic–Accenture embedded-evaluation partnership and how it was received.

## Influenced pages
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — reception of the partnership

## Key claims extracted
- Reaction to the partnership was mixed to hostile
- Critics questioned whether a consulting firm is the right vehicle for model red-teaming and safeguard assessment
- Transluce said the conditions around independence and meaningful oversight are the real issue
```

## Schema / vocabulary additions

None.

## Open questions

None.
