---
title: Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform
type: source
source_type: article
source_file: raw/articles/2026-04-23-cloudgooglecom-blog-products-ai-machine-learning-introducing.md
url: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
published: 2026-04-23
ingested: 2026-04-23
domains: [agents, models]
---

# Google Cloud Next 2026 — TPU v8 and Gemini Enterprise Agent Platform

Google's Cloud Next 2026 announcements combined infrastructure and agent-platform moves into one vertically integrated story: TPU v8 for training and inference scale, and Gemini Enterprise Agent Platform as Google's successor to Vertex AI for building, governing, and optimizing enterprise agents.

## Influenced pages

- [Gemini](../../tools/gemini.md) — Gemini Enterprise Agent Platform details, model stack, and enterprise components
- [Google ADK](../../tools/google-adk.md) — ADK reframed as the open developer layer inside the broader platform
- [Compute infrastructure as decisive competitive moat](../../trends/compute-infrastructure.md) — TPU v8 hardware scale and competitive implications
- [Agents](../../history/state-of/agents.md) — Google strengthened in the enterprise agent-platform layer
- [Models](../../history/state-of/models.md) — Google clarified its active model stack across Gemini, Gemma, Lyria, and embeddings

## Key claims extracted

**Infrastructure**
- TPU 8t is Google's new training chip with roughly 3× compute per pod versus Ironwood
- TPU 8i is the new inference chip with 1,152 TPUs per pod for low-latency workloads
- Google claims TPU 8t clusters can scale to 1 million TPUs
- Gemini API throughput is now framed at 16 billion tokens per minute

**Platform**
- Gemini Enterprise Agent Platform replaces Vertex AI as Google's unified enterprise agent stack
- Agent Studio is the low-code build surface; ADK remains the open-code framework layer
- Model Garden now spans 200+ models
- Agent Garden, Agent Simulation, Agent Runtime, Agent Memory Bank, Agent Registry, Agent Gateway, Agent Identity, and Agent Optimizer round out the platform
- Workspace Intelligence GA, Knowledge Catalog, and Gemini Embedding 2 GA deepen the enterprise context layer

**Production deployments**
- Comcast Xfinity, L'Oréal, PayPal, Color Health, Payhawk, Burns & McDonnell, Geotab, and Gurunavi are presented as live or near-live reference deployments across customer support, payments, healthcare, finance, and enterprise data workflows
