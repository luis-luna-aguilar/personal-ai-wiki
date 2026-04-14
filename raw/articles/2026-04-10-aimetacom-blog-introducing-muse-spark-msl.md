---
title: Introducing Muse Spark: Scaling Towards Personal Superintelligence
type: source
source_type: article
url: https://ai.meta.com/blog/introducing-muse-spark-msl
fetched: 2026-04-10
---

# Introducing Muse Spark: Scaling Towards Personal Superintelligence

To build personal superintelligence, our model’s capabilities should scale predictably and efficiently. Below, we share how we study and track Muse Spark's scaling properties along three axes: pretraining, reinforcement learning, and test-time reasoning.

**Pretraining**. The pretraining phase is where Muse Spark acquires its core multimodal understanding, reasoning, and coding abilities — the foundation that reinforcement learning and test-time compute build upon.

Over the last nine months, we rebuilt our pretraining stack with improvements to model architecture, optimization, and data curation. Together, these advancements increase the capability we can extract from every unit of compute. To rigorously evaluate our new recipe, we fit a scaling law to a series of small models and compare the training FLOPs required to hit a specific level of performance. The results are clear: we can reach the same capabilities with over an order of magnitude less compute than our previous model, Llama 4 Maverick. This improvement also makes Muse Spark significantly more efficient than the leading base models available for comparison.
