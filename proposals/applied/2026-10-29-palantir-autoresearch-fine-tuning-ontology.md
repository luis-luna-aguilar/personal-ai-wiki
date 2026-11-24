---
type: proposal
source: raw/papers/2026-10-29-palantir-autoresearch-fine-tuning-ontology.md
status: pending
created: 2026-10-29
---

# Proposal: Palantir — AutoResearch and the Fine-Tuning Ontology

## Summary

### In short

Palantir is selling post-training as a factory that turns a company's operational records into model weights the company owns and can license: an agent searches data mixtures, techniques and settings against held-back real cases, and every experiment is kept as an asset. The proposal adds a Palantir AutoResearch tool page, a weights-level autoresearch section on Agent improvement loop, a productized example on the proprietary-data moat trend, a State of Agents line, and a term-map row recording "Fine-Tuning Ontology" as a vendor name. The one reason to hesitate: the knowledge-architectures hub, already at 111% of its length ceiling, grows to about 118%.

[[#Open questions|Open questions: 2 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

Palantir published a 22-page whitepaper, "AutoResearch and the Fine-Tuning Ontology", dated by its PDF metadata to 24 October 2026. It describes two linked products. AutoResearch is an agent that runs post-training (the extra training that specializes an already-trained model) for an institution: the team names a workflow worth improving, picks the records in Palantir Foundry that carry signal for it (repair tickets, manuals, fault records, tool logs), sets success criteria and a budget, and the agent turns those records into training examples, generates synthetic ones for gaps, tries different techniques and settings, and keeps the cheapest paths that score best. The Fine-Tuning Ontology is where all of that lands: a versioned store of training datasets, codified training recipes (from simple imitation of good examples, through learning from pairs of better and worse answers, to reinforcement learning on judged attempts), and the resulting model weights, each with lineage, cost and evaluation scores. Palantir pitches the weights and datasets as assets the "sovereign institution" owns and can deploy, rent, sell or white-label.

The paper walks through one notional example in eleven steps, with illustrative numbers. A CNC machine raises a spindle-overheating alarm; the model must recommend the action that clears it, and success means coolant flow above 8 L/min, temperature below 75 °C for 30 minutes and no recurrence. Each past case with a measured outcome becomes an "episode". A tenth is held back, split by machine, site, fault type and period so no candidate can score by recognizing a case. Recipes mixing real and synthetic episodes are logged before they run and scored against preset thresholds; the best misses on hot-ambient faults, so those cases are upweighted and training extended. The promoted model goes live behind a human-approval gate, and every accepted, overridden or failed recommendation becomes a new episode.

### What changes

The wiki treats autoresearch as agents improving an agent system's harness, tracks one post-training agent (Hugging Face's open-source ml-intern), and reserves "ontology" in its knowledge hub for formal rules that check what an agent asserts.

- New page `wiki/tools/palantir-autoresearch.md`, in the autonomous-research-agent subcategory, recording "Fine-Tuning Ontology" as Palantir's name for a training-asset registry.
- **State of Agents** gains a Palantir AutoResearch line next to ml-intern and one Recent-changes entry; the list is at its cap, so the Grok Bot entry of 13 August moves to history. Page date moves to 24 October.
- **Agent improvement loop** gains a short section on autoresearch over model weights, condensing the eleven steps. Page date moves to 24 October.
- **Proprietary data becomes model moat** gains Palantir as the first productized version of its data-to-owned-model flywheel, including licensing datasets and weights. Page date moves to 24 October.
- **Knowledge architectures** gains one term-map row saying the Fine-Tuning Ontology is not a knowledge architecture. Page date moves to 24 October.
- One new source page that explains the paper and its worked example in plain language.

### What to weigh

The date is inferred: the PDF does not print one, so 24 October comes from its creation metadata (the server reports a later modification on 28 October). The hub row pushes an already-long page further past its ceiling; the split is offered in Open questions rather than forced. AutoResearch gets a tool page because no existing page can hold a Palantir product; it sits with research agents, not knowledge platforms, since its "ontology" stores training assets, not knowledge for agents.

## Intended changes

- [ ] **Create** `wiki/tools/palantir-autoresearch.md` — new tool page, subcategory `autonomous-research-agent`
- [ ] **Update** `wiki/state-of/agents.md` — add one line at the end of `### Autonomous research agents`; adds one Recent-changes entry dated 2026-10-24 at the top (10 → 11, over the cap of 10); append `palantir-autoresearch-fine-tuning-ontology-2026-10-24` to frontmatter `sources:`; `as_of` 2026-10-19 → 2026-10-24
- [ ] **Spill** `wiki/state-of/agents.md` → `wiki/history/state-of/agents.md` — spills the oldest Recent-changes entry (expected: `[2026-08-13] Grok Bot launched…`) under a new `## Archived from current page on <apply date>` block
- [ ] **Update** `wiki/concepts/agent-improvement-loop.md` — one Current-status bullet, one new `## Autoresearch over model weights` section after `## Automated harness optimization`, one `## Related` line; adds one Recent-changes entry dated 2026-10-24 (7 → 8, no spill); append source id and link; `as_of` and status heading 2026-07-29 → 2026-10-24
- [ ] **Update** `wiki/trends/proprietary-data-becomes-model-moat.md` — one Current-status bullet and one new `## Productized example: Palantir AutoResearch` section after `## Why it matters`; adds one Recent-changes entry dated 2026-10-24 (3 → 4, no spill); append source id and link; `as_of` and status heading 2026-06-30 → 2026-10-24
- [ ] **Update** `wiki/concepts/knowledge-architectures.md` — one term-map row after the `"one ontology"` row; adds one Recent-changes entry dated 2026-10-24 (7 → 8, no spill); append source id and link; `as_of` 2026-10-19 → 2026-10-24
- [ ] **Update** `wiki/index.md` — add the tool page under Tools; tools count 103 → 104, total 253 → 254
- [ ] **Create** `wiki/sources/papers/palantir-autoresearch-fine-tuning-ontology-2026-10-24.md` — source summary (paper format)

## Page drafts

### wiki/tools/palantir-autoresearch.md (new)

```
---
title: Palantir AutoResearch
type: tool
domains: [agents]
subcategory: autonomous-research-agent
tags: [closed-source, agentic]
as_of: 2026-10-24
sources: [palantir-autoresearch-fine-tuning-ontology-2026-10-24]
---

# Palantir AutoResearch

Palantir's agent for running post-training on an institution's own data inside Palantir Foundry. A team names the workflow to improve, picks the Foundry records that carry signal for it, and sets success criteria and model, data, compute and budget limits. AutoResearch turns the records into training examples and evaluations, generates synthetic examples for gaps, searches data mixtures, techniques and hyperparameters, and keeps the best-scoring, lowest-cost candidates. Everything it produces is stored in what Palantir calls the **Fine-Tuning Ontology**: a versioned registry of training datasets, codified training recipes, and model weights, with lineage, cost and evaluation scores. Despite the name, it is not an ontology in the wiki's rule-layer sense (see [Knowledge architectures](../concepts/knowledge-architectures.md)).

## Current status (as of 2026-10-24)
- Described in a 22-page whitepaper; the worked example and its numbers are notional
- Techniques codified as runnable training code with hyperparameter priors: SFT, LoRA/QLoRA, DPO, KTO, ORPO, SimPO, PPO, GRPO, RLAIF, distillation and others, plus a selector that recommends a method from the objective
- Evaluation on held-back episodes split by asset, site, fault family and period; candidates are promoted only when they clear preset thresholds
- Deployed models sit behind a human-approval gate for safety-critical or low-confidence actions; accepted, overridden and failed recommendations become new training data
- Datasets and weights are positioned as institution-owned assets to deploy, rent, sell or white-label

## Weaknesses / caveats
- Runs only on Palantir Foundry; no pricing, availability or customer results in the source

## Recent changes
- [2026-10-24] Page created from Palantir's AutoResearch and Fine-Tuning Ontology whitepaper.

## Related
- [HF ml-intern](hf-ml-intern.md) — open-source post-training agent that works from papers and public Hub datasets rather than an institution's operational records
- [Agent improvement loop](../concepts/agent-improvement-loop.md) — the same evaluate-and-iterate loop, applied to weights rather than the harness
- [Proprietary data becomes model moat](../trends/proprietary-data-becomes-model-moat.md) — Palantir's "sovereign institution" means owning the trained weights and datasets, not the vendor independence tracked on [Model sovereignty](../trends/model-sovereignty.md)

## Sources
- [Palantir — AutoResearch and the Fine-Tuning Ontology](../sources/papers/palantir-autoresearch-fine-tuning-ontology-2026-10-24.md)
```

### wiki/state-of/agents.md (updated)

Frontmatter (changed fields only; `sources:` appends `palantir-autoresearch-fine-tuning-ontology-2026-10-24` at the end of the live list):

```
as_of: 2026-10-24
```

`### Autonomous research agents` — new line appended after the HF ml-intern line:

```
- [Palantir AutoResearch](../tools/palantir-autoresearch.md) — Palantir; closed post-training agent inside Palantir Foundry that trains models on an institution's own operational records and keeps datasets, recipes and weights as owned assets (the "Fine-Tuning Ontology") *(as of 2026-10-24)*
```

`## Recent changes` — adds one entry at the top; the oldest entry (`[2026-08-13] Grok Bot launched…`) leaves the list (see Spill draft):

```
- [2026-10-24] Added [Palantir AutoResearch](../tools/palantir-autoresearch.md) to Autonomous research agents: post-training on an institution's own Foundry records, with datasets and weights kept as licensable assets.
- [2026-10-19] Added [Helix Foundry](../tools/helix-foundry.md) to Knowledge platforms: HelixDB's local-first data workspace that joins a company's data sources into one graph and answers with SQL cited to versioned snapshots.
- [2026-10-19] Devin added to Agentic DevOps: Devin Oncall (GA) investigates and mitigates production incidents, 100% end-to-end on SREGym-Lite; the Agent orchestration line now names Oncall Responders as Auto-Triage's successor.
- [2026-10-14] Added `Agent web data extraction` subcategory with [Expand Fetch](../tools/expand-fetch.md): agent-oriented fetch API with trained Markdown (Iris) and hidden-JSON (X-Ray) models; vendor-run MDBench 74.1% vs Exa 55.3%, Firecrawl 27.2%.
- [2026-10-09] Added [Harness²](../tools/harness2.md) to Agent frameworks: Google's open-source recursive harnessing framework, frozen weights, up to +11.5 points on WorkBuddy-Bench.
- [2026-10-07] Added [Mecatl](../tools/mecatl.md) to Agent frameworks: Stacklok's open-source cloud-native harness, built by Kubernetes co-creators Craig McLuckie and Joe Beda.
- [2026-10-06] Added [Pi](../tools/pi.md) to Agent frameworks: Pi 1.0 and Pi Durable (checkpointed, crash-resuming harness on Bun or Cloudflare Durable Objects).
- [2026-09-09] Utopia (DeepLethe) added under Knowledge platforms: open-source bitemporal knowledge graph / ontology engine with an agent harness over MCP.
- [2026-09-09] Added Mastra to Agent frameworks: YC-backed open-source TypeScript framework combining an agent abstraction with an explicit graph-based workflow engine, human-in-the-loop suspend/resume, and Observational Memory.
- [2026-09-09] Added a `Knowledge platforms` subcategory (new `knowledge-platform` schema entry) and moved [OpenWiki](../tools/openwiki.md) into it from Agent frameworks, as part of the knowledge-cluster terminology reorganization anchored on [Knowledge architectures](../concepts/knowledge-architectures.md).
```

### wiki/history/state-of/agents.md (updated)

Appended at the end of the file:

```

## Archived from current page on <apply date>

- [2026-08-13] Grok Bot launched (xAI/SpaceXAI): "AI teammates with their own cloud computers," a new entrant in the AI-teammate category alongside Claude Tag.
```

### wiki/concepts/agent-improvement-loop.md (updated)

Frontmatter (changed fields only; `sources:` appends `palantir-autoresearch-fine-tuning-ontology-2026-10-24` at the end of the live list):

```
as_of: 2026-10-24
```

`## Current status (as of 2026-10-24)` — heading date changes; one bullet appended after the Cline/Kimi K3 bullet:

```
- **Autoresearch over weights (October 2026):** Palantir describes [AutoResearch](../tools/palantir-autoresearch.md), which runs the same evaluate-and-iterate loop on model training instead of the harness — see the section below
```

New section inserted after `## Automated harness optimization`:

```
## Autoresearch over model weights

The loop can also change the model rather than the harness. Palantir's [AutoResearch](../tools/palantir-autoresearch.md) whitepaper (October 2026) walks one notional workflow through it: fix the single decision the model makes and the rule that says whether its action worked; turn past cases with a measured outcome into "episodes"; hold back a tenth, split by machine, site, fault type and period so no candidate scores by recognizing a case; build versioned mixtures of real and synthetic episodes; log each recipe (base model, mixture, technique, hyperparameters) before it runs; score candidates against thresholds set in advance; change the mixture, synthetic data or settings to fix the failure mode the scores name; promote a model behind a human-approval gate; and feed accepted, overridden and failed recommendations back as new episodes. The holdout rule is the eval-suite hygiene below applied to training data. [HF ml-intern](../tools/hf-ml-intern.md) runs a similar loop from papers and public datasets.
```

`## Related` — one line appended:

```
- [Palantir AutoResearch](../tools/palantir-autoresearch.md) — the loop applied to model weights: episodes from operational records, held-back evals, iterated training recipes
```

`## Recent changes` — adds one entry at the top (7 → 8, no spill):

```
- [2026-10-24] Added autoresearch over model weights: Palantir's AutoResearch loop from operational episodes through held-back evals and iterated training recipes to a gated deployment that feeds overrides back as training data.
```

`## Sources` — appends one link:

```
- [Palantir — AutoResearch and the Fine-Tuning Ontology](../sources/papers/palantir-autoresearch-fine-tuning-ontology-2026-10-24.md)
```

### wiki/trends/proprietary-data-becomes-model-moat.md (updated)

Frontmatter (changed fields only; `sources:` appends `palantir-autoresearch-fine-tuning-ontology-2026-10-24` at the end of the live list):

```
as_of: 2026-10-24
```

`## Current status (as of 2026-10-24)` — heading date changes; one bullet appended:

```
- The flywheel is being sold as a product: Palantir's AutoResearch (October 2026) turns an institution's operational records into training sets and specialized models, and treats both as owned assets that can be licensed or white-labeled
```

New section inserted after `## Why it matters`:

```
## Productized example: Palantir AutoResearch

Palantir's whitepaper on [AutoResearch](../tools/palantir-autoresearch.md) is the most complete vendor version of this trend's flywheel. Records from ERP, MES, CRM, quality and maintenance systems, plus the decisions people made and whether they worked, become versioned training datasets with lineage and security markings. An agent searches training recipes against held-back real cases, and the resulting weights are registered with their data, recipe, cost and scores. Every production recommendation that is accepted, overridden or fails becomes new training data. Palantir offers three paths for the outputs: deploy them in the institution's own workflows, or rent, sell or white-label the datasets and weights to other organizations. That matches this page's open question about where the moat sits: Palantir's answer is the dataset, the evaluation set and the production loop together, kept as one owned asset.
```

`## Recent changes` — adds one entry at the top (3 → 4, no spill):

```
- [2026-10-24] Added Palantir AutoResearch as a productized version of the data-to-owned-model flywheel, including licensing and white-labeling of datasets and weights.
```

`## Sources` — appends one link:

```
- [Palantir — AutoResearch and the Fine-Tuning Ontology](../sources/papers/palantir-autoresearch-fine-tuning-ontology-2026-10-24.md)
```

### wiki/concepts/knowledge-architectures.md (updated)

Frontmatter (changed fields only; `sources:` appends `palantir-autoresearch-fine-tuning-ontology-2026-10-24` at the end of the live list):

```
as_of: 2026-10-24
```

`## Term map` — one new row inserted directly after the `"one ontology" over company data, local-first data workspace` row:

```
| Fine-Tuning Ontology | not a knowledge architecture | Palantir's name for a versioned registry of training datasets, training recipes, and model weights with lineage and access controls, produced by [Palantir AutoResearch](../tools/palantir-autoresearch.md). It stores training assets, not knowledge for agents to read, and has no machine-checked rules, so it is not the ontology row's sense; a vendor name only. It is built on the Palantir Foundry Ontology (object types and links over ERP, MES and CRM records), which is the sense of the `"one ontology"` row above at organization scope |
```

`## Recent changes` — adds one entry at the top (7 → 8, no spill):

```
- [2026-10-24] Recorded Palantir's "Fine-Tuning Ontology" as a vendor name for a registry of training datasets, recipes, and weights, outside this cluster and not the ontology row's sense.
```

`## Sources` — appends one link:

```
- [Palantir — AutoResearch and the Fine-Tuning Ontology](../sources/papers/palantir-autoresearch-fine-tuning-ontology-2026-10-24.md)
```

### wiki/index.md (updated)

`## Tools` — one line added after the `tools/openwiki` line:

```
- [tools/palantir-autoresearch](tools/palantir-autoresearch.md) — Palantir's post-training agent in Palantir Foundry: trains specialized models on an institution's own operational records and keeps datasets, recipes and weights as owned, licensable assets (marketed as the "Fine-Tuning Ontology") *(as_of: 2026-10-24)*
```

`## Page count` — two lines change:

```
- tools: 104
**Total content pages: 254.**
```

### wiki/sources/papers/palantir-autoresearch-fine-tuning-ontology-2026-10-24.md (new)

```
---
title: Palantir — AutoResearch and the Fine-Tuning Ontology
type: source
source_type: paper
source_file: raw/papers/2026-10-29-palantir-autoresearch-fine-tuning-ontology.md
url: https://www.palantir.com/assets/xrfr7uokpv1b/71GBpNOzMizxDnonP5d7ea/67a9967e58df7b8703269d0b60a33401/AutoResearch_and_the_Fine-Tuning_Ontology.pdf
published: 2026-10-24
ingested: 2026-10-29
domains: [agents, models]
---

# Palantir — AutoResearch and the Fine-Tuning Ontology

A 22-page Palantir whitepaper. The publication date is the PDF's creation date; the document prints none.

## The plain-language thesis

A general model does not know your machines, your tickets, or which repairs actually worked. Your systems do. Palantir's claim is that an agent can do the fine-tuning work a research team would do, using those records, and that the datasets, recipes and weights it produces should be treated as assets the company owns, deploys, and can even sell.

## The problem it addresses

Specializing a model is a search problem. Which past records carry the signal? How much synthetic data to add? Which training method fits the task? Which base model and settings? Each try costs compute, and it is easy to fool yourself by testing on cases the model has already seen. Most organizations lack the staff to run that search carefully.

## The two pieces

- **AutoResearch** is the agent. The team names the workflow, picks the relevant records in Palantir Foundry, sets success criteria and limits on model, data, compute and budget. The agent turns records into examples and evaluations, generates synthetic examples, tries recipes, drops weak directions with small cheap probes before committing to expensive runs, and logs every attempt with its data, method, results and cost.
- **The Fine-Tuning Ontology** is where the outputs live: training datasets (versioned, with lineage, evaluation splits and security markings), techniques (Palantir's training code with starting hyperparameters from past runs, plus a selector that suggests a method), and models (registered with data mixture, recipe, cost and scores). Despite the name, it is a registry of training assets, not a rule system.

The paper sorts training methods into three plain jobs:
- **Imitate** (supervised fine-tuning, SFT): show the model correct examples until it reproduces them exactly. Good for getting complex tool calls formatted right.
- **Contrast** (Direct Preference Optimization, DPO): show pairs of a better and a worse answer so the model prefers the right one over a near miss. Good for cutting needless refusals.
- **Explore** (Group Relative Policy Optimization, GRPO): let the model try several approaches, have a judge model score them, and reinforce the ones that beat the group average. Good for open-ended, multi-step problems with no single correct path.

## Worked example (notional numbers from the paper)

1. **Define the decision.** Recommend the action that clears a spindle-overheating alarm (E214) on a CNC machine. Success: coolant flow above 8 L/min, temperature below 75 °C for 30 minutes, alarm does not return.
2. **Represent it as episodes.** An episode is the case (machine, fault, readings), the action someone took, and the readings that followed. Example: CNC-042, E214, "replace coolant filter", then 10.2 L/min and 72 °C. Only episodes with a measured outcome can be trained on.
3. **Pass the records in.** Fault records, tickets, readings, procedures and manuals form the cross-section: 41,200 episodes. Contradictory, incomplete or leaked cases are set aside.
4. **Hold back the test set.** Split 80/10/10 before any training, along machine, site, fault family and period, so 4,100 evaluation episodes come from machines the model never saw.
5. **Mix real and synthetic data.** Mix A uses successes only; Mix B successes and failures; Mix C is 45% tickets, 15% procedures, 40% synthetic, with rare faults upweighted. Each mixture is versioned.
6. **Assemble recipes.** A recipe is one base model, one mixture, one technique and its settings (for example base-c, Mix C, LoRA SFT, rank 32, 3 epochs, learning rate 2e-4), logged before it runs.
7. **Evaluate every candidate.** The best run reaches 88% correct actions, 94% load-test pass, 0.8% unsafe recommendations.
8. **Iterate to the threshold.** Thresholds were 0.90 fix rate, 0.97 load pass, 0.02 recurrence, 0.010 unsafe; three candidates (0.71, 0.83, 0.88 fix rate) all fall short. The scores name the failure: 76% on high-ambient-temperature faults and 6% over-replacement. So those episodes are upweighted, synthetic cases of degraded filters at 34 °C are generated, LoRA rank goes from 32 to 64, and training runs two more epochs.
9. **Deploy behind a gate.** A model that clears every threshold is promoted. It recommends an action, cites the procedure, and escalates when unsure; a human must approve when the action is safety-critical or confidence is low.
10. **Learn from live operations.** Each production case becomes a new episode: accepted (flow 10.1 L/min, pass), overridden (engineer inspects the coolant pump instead), or failed (87 °C, alarm still active). Overrides and failures carry the most signal and go back to step 3.
11. **Own the asset.** The institution now holds the model (diag-agent v2.0) and its weights, dataset mixture C v3.2, 4,900 synthetic episodes, the 4,100-episode evaluation set, the recipe, and 38 experiments with results, which it can deploy, sell, rent or white-label.

## Why this is useful for our projects

- **The episode is the unit.** Anyone fine-tuning, or even just building evals, can copy it: input, action taken, measured outcome. If the outcome is not recorded, the case is not usable training data, which says what to start logging today.
- **Split the holdout along the axis you fear leaking.** Splitting by machine, site and period, not at random, is the cheap protection against a model that memorizes cases.
- **Write the recipe down before running it.** Logging each experiment's data, method, cost and score in advance keeps the search honest and makes the result reproducible.
- **Overrides are the best data.** A human-approval gate is both a safety control and the richest source of next-round training examples.
- **The same loop works without training.** Teams that only change prompts or harnesses can reuse the episode, holdout and threshold discipline unchanged.

## Influenced pages

- [Palantir AutoResearch](../../tools/palantir-autoresearch.md) — new tool page
- [State of Agents](../../state-of/agents.md) — new line under Autonomous research agents
- [Agent improvement loop](../../concepts/agent-improvement-loop.md) — autoresearch over model weights
- [Proprietary data becomes model moat](../../trends/proprietary-data-becomes-model-moat.md) — productized example of the flywheel
- [Knowledge architectures](../../concepts/knowledge-architectures.md) — "Fine-Tuning Ontology" recorded as a vendor name outside the cluster

## Key claims extracted

- AutoResearch automates post-training on an institution's data in Palantir Foundry, within set model, data, compute and budget limits
- Each iteration records data, method, model changes, evaluation results, compute use and cost
- The Fine-Tuning Ontology holds three asset classes: datasets, techniques, models (weights)
- Codified techniques include continued pretraining, full and LoRA SFT, QLoRA, prompt tuning, distillation, rejection sampling, ORPO, KTO, SimPO, DPO, PPO, RLAIF and GRPO, with hyperparameter priors (LoRA rank, learning rate, epochs, DPO β, GRPO group size, real-to-synthetic ratio)
- Datasets are published with schema, lineage, evaluation splits and security markings; personal and sensitive data are removed before external licensing
- Models are registered with full lineage and can be deployed, rented, sold or white-labeled

## Limits

- All figures in the worked example are notional; the paper reports no customer results, benchmarks, pricing or availability
- The product requires Palantir Foundry
```

## Schema / vocabulary additions

None.

## Open questions

- The knowledge-architectures hub moves from about 111% to about 118% of its 1,200-word ceiling. Split it now by moving `## Term map` to its own page (for example `concepts/knowledge-architectures-term-map.md`), with the hub keeping the three axes and the matrix and pointing to the map? Below 150%, so this is optional.
	- Split now
- The new row maps the Palantir Foundry Ontology itself (object types, properties and links over a company's ERP, MES and CRM records, plus recorded decisions) to the `"one ontology"` sense at organization scope, as a hedge inside the note. Keep it as a note until a source describes the Foundry Ontology directly (assumed), or give it its own matrix row now?
	- keep it as note
