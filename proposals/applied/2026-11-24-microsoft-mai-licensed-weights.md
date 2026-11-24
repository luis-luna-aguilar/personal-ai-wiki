---
type: proposal
source: raw/articles/2026-11-24-microsoftai-news-introducing-mai-licensed-weights.md
sources:
  - raw/articles/2026-11-24-microsoftai-news-introducing-mai-licensed-weights.md
  - raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
status: pending
created: 2026-11-24
---

# Proposal: Microsoft MAI Licensed Weights and Ignite 2026

## Summary

### In short
Microsoft now sells the proprietary-data flywheel as a hyperscaler product. With MAI Licensed Weights, enterprises run Microsoft's model weights in their own Azure, fine-tune them on their own data, and decide when to upgrade. Tuned MAI coding models beat frontier models on narrow customer tasks at a fraction of the cost (AT&T: ahead of GPT-6.1 Sol at 1/50th the cost). The proposal updates **Proprietary data becomes model moat**, **Microsoft Copilot** and **MAI-Thinking-1**, and adds two source pages. One reason to hesitate: the source is partial, because Microsoft's Ignite blog and the MAI Code 2 post were not read, and the product is not yet available.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 17 November 2026, at its Ignite conference, Microsoft AI announced MAI Licensed Weights. Organizations can deploy Microsoft's own MAI models in their own Azure environment, adapt them with proprietary knowledge, control who can use them, and choose when to upgrade. Microsoft says it trains on a customer's data and adaptations only with express agreement. Its pitch is that the best model for a business is the one that does that business's tasks best at a viable cost, not the largest general model. It gives three customer results, all from tuned MAI Code 2 or Code 2 Flash models. AT&T beat GPT-6.1 Sol on standard 5G network-analysis tasks at 1/50th of the cost. Woven by Toyota got ready-to-merge fixes for MISRA coding-standard violations in 44% of the cases its frontier models had passed to humans, at under a tenth of the cost. Alaska Airlines raised the accuracy of its aircraft-maintenance report classification from 81% to 91%. Availability is "coming soon" through Microsoft's Frontier Company engagements.

Every's Grant Harvey sat in on a roundtable after Nadella's keynote. Nadella said he wants to turn the model business into a "database business." He argued that a world run by one model firm won't happen, because the world will demand more than one. On the product side, the full Office apps now run inside Copilot instead of Copilot sitting in an Office sidebar. Copilot Workspaces lets people and their agents work from shared context. Former team leads become individual contributors who manage agents on token budgets.

### What changes
The moat page's only productized example is Palantir AutoResearch, and the Copilot page stops at the September one-app launch.

- **Proprietary data becomes model moat** gains a Current-status bullet and a short "Hyperscaler version" section on MAI Licensed Weights and its three customer results. It also gets one Recent-changes entry. Page date moves to 18 November.
- **Microsoft Copilot** gains an Ignite bullet (Office inside Copilot, Copilot Workspaces, team leads managing agents on token budgets) and one Recent-changes entry. Page date moves to 18 November.
- **MAI-Thinking-1** gains one line under its family table naming MAI Code 2 and Code 2 Flash as the models behind licensed weights, plus one Recent-changes entry. Page date moves to 17 November.
- Two new source pages: Microsoft's announcement, and a story-specific page for the Ignite item in Every's 18 November newsletter.

### What to weigh
MAI Code 2 and Code 2 Flash were announced the same day in a separate post that was not fetched, so the proposal names them only as the base for the licensed-weights results and does not create a page for them. It also does not say whether they replace MAI-Code-1-Flash. Microsoft's Ignite blog was not fetched either, so the Copilot details rest on Every's account of the roundtable.

## Intended changes

- [ ] **Update** `wiki/trends/proprietary-data-becomes-model-moat.md` — add one Current-status bullet and a new `## Hyperscaler version: MAI Licensed Weights` section after the Palantir section; add one Recent-changes entry dated 2026-11-17; append two source ids and links; `as_of` and the Current-status stamp move to 2026-11-18
    > See draft below

- [ ] **Update** `wiki/tools/microsoft-copilot.md` — add one Current-status bullet; add one Recent-changes entry dated 2026-11-17 (list has 5 entries, no spill); append one source id and link; `as_of` and the Current-status stamp move to 2026-11-18
    > See draft below

- [ ] **Update** `wiki/models/mai-thinking-1.md` — add one line under the MAI family table; add one Recent-changes entry dated 2026-11-17; append one source id and link; `as_of` moves to 2026-11-17
    > See draft below

- [ ] **Create** `wiki/sources/articles/mai-licensed-weights-2026-11-17.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/every-nadella-ignite-own-model-2026-11-18.md` — story-specific source summary for the Ignite roundtable item

## Page drafts

### wiki/trends/proprietary-data-becomes-model-moat.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-11-18
sources: [market-for-making-ai-better, ainews-2026-04-21, ai-strategy-explicit-bets-2026-06, palantir-autoresearch-fine-tuning-ontology-2026-10-24, mai-licensed-weights-2026-11-17, every-nadella-ignite-own-model-2026-11-18]
```

Current status heading and new bullet (appended as the last bullet):

```
## Current status (as of 2026-11-18)

- Hyperscalers now sell the same bet: Microsoft's MAI Licensed Weights (Ignite, 2026-11-17) lets enterprises run and fine-tune MAI weights in their own Azure and choose when to upgrade; Satya Nadella says there should be "as many models as firms"
```

New section, inserted after `## Productized example: Palantir AutoResearch`:

```
## Hyperscaler version: MAI Licensed Weights

Microsoft's [MAI](../models/mai-thinking-1.md) Licensed Weights, announced at Ignite on 2026-11-17 and "coming soon" through its Frontier Company engagements, puts the flywheel inside a hyperscaler. Customers deploy MAI model weights in their own Azure environment, adapt them with proprietary data, control access, and decide when to upgrade; Microsoft says it trains on their data and adaptations only with express agreement. Its customer results all use tuned MAI Code 2 or Code 2 Flash models: AT&T beat GPT-6.1 Sol on standard 5G network-analysis tasks at 1/50th of the cost; Woven by Toyota got ready-to-merge MISRA coding-standard fixes in 44% of cases its frontier models had handed to humans, at under a tenth of the cost; Alaska Airlines raised maintenance-report classification accuracy from 81% to 91%. Nadella calls this turning the model business into a "database business". Compared with Palantir, which sells the loop around a model, Microsoft sells the base weights and the cloud they run in: the adaptation belongs to the customer, the base model and the infrastructure stay Microsoft's.
```

`## Recent changes` — adds one entry at the top (list has 4 entries, no spill):

```
- [2026-11-17] Added Microsoft's MAI Licensed Weights (Ignite) as the hyperscaler version of the flywheel: enterprises fine-tune and run MAI weights in their own Azure; AT&T, Woven by Toyota and Alaska Airlines results; Nadella's "as many models as firms".
```

`## Sources` — two links appended:

```
- [Microsoft AI — MAI Licensed Weights: Frontier performance you control](../sources/articles/mai-licensed-weights-2026-11-17.md)
- [Every — Microsoft's CEO Wants Every Company to Own Its Own Model](../sources/newsletters/every-nadella-ignite-own-model-2026-11-18.md)
```

### wiki/tools/microsoft-copilot.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-11-18
sources: [microsoft-copilot-agent-mode-office, microsoft-word-legal-agent, copilot-cowork-ga-june-2026, ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, every-copilot-seat-in-org-chart-2026-09-25, every-nadella-ignite-own-model-2026-11-18]
```

Current status heading and new bullet (inserted directly under the heading, before the one-app bullet):

```
## Current status (as of 2026-11-18)

- **Ignite (2026-11-17):** the full Office apps now run inside Copilot instead of Copilot sitting in an Office sidebar, and Copilot Workspaces lets people and their agents work from shared context; Nadella says former team leads become individual contributors who manage agents on token budgets (per Every's roundtable report)
```

`## Recent changes` — adds one entry at the top (list has 5 entries, no spill):

```
- [2026-11-17] Ignite: full Office apps run inside Copilot; Copilot Workspaces for shared human-agent context; Microsoft also launched MAI Licensed Weights (see [Proprietary data becomes model moat](../trends/proprietary-data-becomes-model-moat.md))
```

`## Sources` — one link appended:

```
- [Every — Microsoft's CEO Wants Every Company to Own Its Own Model](../sources/newsletters/every-nadella-ignite-own-model-2026-11-18.md)
```

### wiki/models/mai-thinking-1.md (updated)

Frontmatter (changed fields):

```
as_of: 2026-11-17
sources: [ainews-mai-build-june-2026, satya-nadella-no-priors-june-2026, ainews-spacexai-grok-46-and-grok-bot-2026-08-13, mai-licensed-weights-2026-11-17]
```

`## MAI family members` — one paragraph added directly after the table, before the audio-models paragraph:

```
Newer MAI coding models, MAI Code 2 and MAI Code 2 Flash (announced 2026-11-17), are the base for Microsoft's MAI Licensed Weights, which lets enterprises fine-tune and run MAI weights in their own Azure; see [Proprietary data becomes model moat](../trends/proprietary-data-becomes-model-moat.md). Their own specs are not yet captured here.
```

`## Recent changes` — adds one entry between the 2026-11-23 and 2026-08-13 entries (list has 3 entries, no spill):

```
- [2026-11-17] MAI Licensed Weights announced at Ignite, built on MAI Code 2 and Code 2 Flash; customers fine-tune and run the weights in their own Azure.
```

`## Sources` — one link appended:

```
- [Microsoft AI — MAI Licensed Weights: Frontier performance you control](../sources/articles/mai-licensed-weights-2026-11-17.md)
```

### wiki/sources/articles/mai-licensed-weights-2026-11-17.md (new)

```
---
title: 'Microsoft AI — MAI Licensed Weights: Frontier performance you control'
type: source
source_type: article
source_file: raw/articles/2026-11-24-microsoftai-news-introducing-mai-licensed-weights.md
url: https://microsoft.ai/news/introducing-mai-licensed-weights/
published: 2026-11-17
ingested: 2026-11-24
domains: [models]
---

# Microsoft AI — MAI Licensed Weights: Frontier performance you control

Microsoft AI's Ignite announcement of MAI Licensed Weights: enterprises deploy and customize Microsoft's MAI models in their own Azure environments, keep control over access and upgrades, and adapt the models with proprietary data. The post argues the best business model is the one that performs best on the tasks that matter at a viable cost, and backs it with three customer results.

## Influenced pages
- [Proprietary data becomes model moat](../../trends/proprietary-data-becomes-model-moat.md) — hyperscaler version of the data-to-owned-model flywheel
- [MAI-Thinking-1](../../models/mai-thinking-1.md) — MAI Code 2 and Code 2 Flash named as the licensed-weights base

## Key claims extracted
- MAI Licensed Weights lets organizations deploy and customize MAI models in their own Azure environments and decide when to upgrade
- Customer data and adaptations are used to train Microsoft's models only with express agreement
- AT&T: customized MAI Code 2 Flash and Code 2 beat GPT-6.1 Sol on standard 5G network-operations analytics at 1/50th of the cost; frontier-level on complex tasks at significantly lower cost
- Woven by Toyota: MAI Code 2 Flash fine-tuned on historical MISRA fixes produced ready-to-merge fixes in 44% of cases where existing frontier models needed human intervention, at under a tenth of the cost
- Alaska Airlines: MAI Code 2 Flash raised aircraft-maintenance report classification accuracy from 81.2% to 91.1% after tuning
- Availability: "coming soon" through Microsoft's Frontier Company engagements
```

### wiki/sources/newsletters/every-nadella-ignite-own-model-2026-11-18.md (new)

```
---
title: Every — Microsoft's CEO Wants Every Company to Own Its Own Model
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-18-microsofts-ceo-wants-every-company-to-own-its-own.md
published: 2026-11-18
ingested: 2026-11-24
domains: [models, agents]
---

# Every — Microsoft's CEO Wants Every Company to Own Its Own Model

Story-specific page for the lead item of Every's 2026-11-18 Context Window: Grant Harvey's report from a roundtable with Satya Nadella after his Ignite keynote on 2026-11-17.

## Influenced pages
- [Proprietary data becomes model moat](../../trends/proprietary-data-becomes-model-moat.md) — "as many models as firms", "database business"
- [Microsoft Copilot](../../tools/microsoft-copilot.md) — Office inside Copilot, Copilot Workspaces, agent-managing ICs

## Key claims extracted
- Nadella says a world that runs on one model firm won't happen; there should be "as many models as firms"
- Microsoft wants to turn its model business into a "database business": customers license MAI weights, run them in their own Azure, fine-tune on proprietary data, and decide when to upgrade
- AT&T's custom MAI model beat Sol 6.1 on standard 5G network tasks at one-fiftieth of the cost (per Microsoft)
- Every's Monologue: a two-person team replaced a ~1-trillion-parameter model with a fine-tuned one that is faster and far cheaper
- The full Office apps now run inside Copilot; Copilot Workspaces lets people and agents collaborate with shared context
- Former team leads become individual contributors who manage agents with token budgets
```

## Schema / vocabulary additions

None.

## Open questions

None.
