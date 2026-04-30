---
title: DeepSeek V4 Preview
type: source
source_type: article
source_file: raw/articles/2026-04-24-huggingfaceco-blog-deepseekv4.md
url: https://huggingface.co/blog/deepseekv4
published: 2026-04-24
ingested: 2026-04-24
domains: [models, coding, agents]
---

# DeepSeek V4 Preview

Technical writeup of DeepSeek V4's release, focused on why the model matters for agent workloads rather than just headline benchmark numbers. The central claim is that DeepSeek is attacking the long-context economics problem directly: lower KV-cache footprint, lower per-token inference cost at depth, and post-training choices explicitly tuned for tool-using agents.

## Influenced pages

- [DeepSeek V4](../../models/deepseek-v4.md) — new page for the release
- [Models](../../history/state-of/models.md) — new `Coding models` entry
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — extends the trend into long-context open agent systems

## Key claims extracted

- DeepSeek V4 ships as V4-Pro and V4-Flash with 1M-token context
- V4 is explicitly framed for long-running agent workflows, not only general chat
- Relative to DeepSeek-V3.2, long-context inference uses much less KV cache and fewer FLOPs per token
- Agent-specific shaping includes preserved reasoning across tool turns, a dedicated tool-call schema, and RL infrastructure for sandboxed tool-use training
- Reported agent benchmarks are competitive with frontier closed models even if not category-leading across every metric
