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
- [Knowledge term map](../../concepts/knowledge-term-map.md) — "Fine-Tuning Ontology" recorded as a vendor name outside the cluster

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
