---
title: GLM-5.2
type: model
domains: [models, coding]
subcategory: coding-model
tags: [open-weights, agentic]
as_of: 2026-07-02
sources: [ainews-glm-52-june-2026, ainews-not-much-happened-2026-07-02, the-code-devin-security-2026-07-02, glm-52-frontier-adjacent-2026-06]
---

# GLM-5.2

Z.ai's June 2026 open-weight frontier model. MIT-licensed, 744B total / 40B active MoE, 1M context. Released opportunistically right after the Fable 5 export-control ban; positioned as the practical open alternative for teams that lost access to the strongest closed frontier models.

## Current status (as of 2026-06-17)

- MIT license; 744B total / 40B active MoE; 1M context window
- Two reasoning modes: high and max
- Pricing: $1.4 / $4.4 per million input / output tokens (same as GLM-5.1)
- **IndexShare:** reuses one sparse-attention indexer across four layers → 2.9× lower FLOPs at 1M context vs naive sparse attention
- **MTP (Multi-Token Prediction):** speculative decoding acceptance +20% over prior version
- **Anti-reward-hacking during RL training:** LLM judge blocked suspicious tool calls, returned dummy info, let trajectories continue — an unusually transparent description of RL reward gaming mitigation
- Z.ai launched [ZCode](../tools/zcode.md), an official coding environment for GLM-5.2 with BYOK support, cross-platform desktop availability, and long-running coding sessions.
- Mercor reported GLM-5.2 as the first open model to lead an APEX-SWE category, with 55.3% Pass@1 on Integration, while still not clearly surpassing the strongest closed frontier models overall.
- The ecosystem story now includes inference work: DSpark speculative decoding previews for GLM-5.2 and native vLLM DSpark support for DeepSeek-style models show speed/serving work becoming part of open-model competitiveness.

## Benchmarks (independent, June 2026)

- **FrontierSWE / DeepSWE:** #3 (behind Fable 5 [banned] and Opus 4.8)
- **Design Arena:** #1 (Fable 5 unavailable)
- **Agent Arena:** #10 overall / #1 open-weight
- **Code Arena (frontend):** #2 (behind Fable 5 [unavailable] → effectively #1 accessible)
- **Terminal-Bench 2.1:** 81.0 (vs 62.0 for GLM-5.1)

Practitioners described it as the first open-weight model they could comfortably substitute for Opus/GPT-class coding workflows. The timing — released immediately after Fable 5's suspension — amplified adoption intent.

## Strengths

- MIT license: no usage restrictions, self-hostable
- IndexShare enables genuine 1M-context use without prohibitive compute cost
- Strong independent benchmark validation (not just vendor-reported)
- Transparent RL training story

## Weaknesses / caveats

- FrontierSWE still behind Fable 5 and Opus 4.8 when Fable is available
- Benchmark positions reflect a week where the top closed model (Fable 5) was unavailable globally

## Ecosystem adoption and cost/performance (as of 2026-06-23)

Follow-on coverage described GLM-5.2 as the first open-weight model many practitioners treated as plausibly frontier-adjacent for daily coding and agent work. AINews reports:

- Artificial Analysis placed GLM-5.2 as the leading open-weight model and a strong cost/performance point on AA-Briefcase, behind Claude Fable 5 and Opus 4.8 for hard multi-week work.
- Practitioners described it as passing a "daily driver" or "frontier model that happens to be open" vibe check.
- Tooling moved quickly: Cline, dcode/deepagents, Baseten, Fireworks, AWS Marketplace, LangChain deepagents, Droid, Ollama/llama.cpp/Unsloth, and other providers or formats appeared in the launch window.
- The operational caveat remains substantial: self-hosting very large open-weight MoEs is still expensive and complex, so most teams will experience GLM-5.2 through hosted inference or agent-tool integrations rather than local hardware.

## Recent changes

- [2026-06-23] Follow-on coverage adds strong ecosystem signal: GLM-5.2 quickly landed in coding-agent harnesses and inference providers; AA-Briefcase and practitioner reports frame it as frontier-adjacent but still behind Fable/Opus on hardest long-horizon work.
- [2026-07-02] ZCode launched as GLM-5.2's official coding environment; APEX-SWE reported GLM-5.2 leading Integration at 55.3% Pass@1; DSpark/vLLM work reinforced inference optimization as part of the open-model stack.
- [2026-06-17] Released; MIT license; #1 open-weight Agent Arena; #1 Design Arena; #2 Code Frontend; Terminal-Bench 2.1: 81.0; supersedes GLM-5.1

## Sources

- [GLM-5.2 release coverage](../sources/newsletters/ainews-glm-52-june-2026.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [The Code - Cognition ships Devin for Security](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [GLM-5.2 frontier-adjacent open-weight signal](../sources/newsletters/glm-52-frontier-adjacent-2026-06.md)
