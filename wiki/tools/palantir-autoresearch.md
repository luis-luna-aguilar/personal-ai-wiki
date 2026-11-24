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
