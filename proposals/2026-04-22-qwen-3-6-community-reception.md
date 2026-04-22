---
type: proposal
source: raw/newsletters/2026-04-22-ainews-openai-launches-gpt-image-2.md
status: pending
created: 2026-04-22
---

# Proposal: Qwen 3.6 community reception + Max Preview signal

## Summary

AINews LocalLlama recap sharpens the Qwen 3.6 35B-A3B niche with real community usage data: preferred for coding/tool calling/agentic tasks, but Gemma 4 26B wins for creative writing, translation, and conversation. Separately: Qwen 3.6 Max Preview went live on Qwen Chat (community estimates 600-700B parameters), scored highest AA-Intelligence Index among Chinese models (52), and community consensus says it won't be open-sourced. Kimi K2.6 is now being treated as an 85% Opus replacement for practical tasks.

## Intended changes

- [ ] **Update** `wiki/models/qwen-3-6-35b-a3b.md` — add community reception data and Max Preview note; update as_of
    > **Replace `## Current status (as of 2026-04-21)` block:**
    > ```
    > ## Current status (as of 2026-04-22)
    >
    > - 35B-parameter A3B mixture-of-experts model viable on roughly 24GB-class local hardware
    > - The "practical local-agent threshold" framing started in the late-February Qwen 3.5 medium release cycle and sharpened further by the 3.6 framing
    > - Community niche (April 2026 LocalLlama data): strong for coding, tool calling, and agentic tasks; Gemma 4 26B outperforms it for creative writing, translation, and conversation
    > - Positioned as a practical local-agent baseline rather than a research novelty or general-purpose assistant
    > - Broad framing: local agent workflows are getting good enough to handle easy and medium-difficulty tasks without relying on proprietary models
    > ```
    >
    > **Add `## Qwen 3.6 Max Preview (proprietary tier)` section:**
    > ```
    > ## Qwen 3.6 Max Preview (proprietary tier)
    >
    > Qwen 3.6 Max Preview went live on Qwen Chat (chat.qwen.ai) in April 2026. Community estimates: 600-700B parameters, based on prior 397B Qwen 3.6 Plus lineage. Highest AA-Intelligence Index among Chinese models (score: 52 as of April 2026). Community consensus: unlikely to be open-sourced — Alibaba has historically kept Max-tier models proprietary; their largest open-sourced version is roughly 122B parameters. API access with multi-step workflow support is coming.
    > ```
    >
    > **Update `as_of` to `2026-04-22`** and add `ainews-2026-04-22` to `sources` frontmatter.
    >
    > **Add to `## Recent changes` (or create it):**
    > ```
    > ## Recent changes
    > - [2026-04-22] Added community reception niche data (coding/tools > creative/translation); added Qwen 3.6 Max Preview section (proprietary, 600-700B est., top Chinese AA-Intelligence Index)
    > ```

- [ ] **Update** `wiki/state-of/models.md` — add Qwen niche note and Kimi/Opus community signal to Coding models section
    > **Update the `[[models/qwen-3-6-35b-a3b]]` line in `### Coding models`:**
    > ```
    > Before:
    > - [[models/qwen-3-6-35b-a3b]] — Alibaba; the practical local-agent-threshold story started in the late-February Qwen 3.5 medium cycle and sharpened further by the later 3.6 framing *(as of 2026-02-25)*
    >
    > After:
    > - [[models/qwen-3-6-35b-a3b]] — Alibaba; community niche: preferred for coding/tool calling/agent work; Gemma 4 26B leads for creative/translation/conversation; Qwen 3.6 Max Preview (600-700B est.) is now live on Qwen Chat but unlikely open-sourced *(as of 2026-04-22)*
    > ```
    >
    > **Update the `[[models/kimi-k2-6]]` line:**
    > ```
    > Before:
    > - [[models/kimi-k2-6]] — Moonshot AI; open-weight 1T-param MoE; open-source SOTA claims: HLE w/ tools 54.0, SWE-Bench Pro 58.6, SWE-bench Multilingual 76.7, BrowseComp 83.2; 4K+ tool calls, 12+ hour continuous runs *(as of 2026-04-21)*
    >
    > After:
    > - [[models/kimi-k2-6]] — Moonshot AI; open-weight 1T-param MoE; SOTA coding/agent benchmark claims; 4K+ tool calls, 12+ hour runs; community now treating it as an Opus 4.7 replacement for ~85% of practical tasks *(as of 2026-04-22)*
    > ```
    >
    > **Add to `## Recent changes`:**
    > ```
    > - [2026-04-22] Qwen 3.6 35B-A3B niche sharpened: strong for coding/tools, weaker for creative/translation. Qwen 3.6 Max Preview live but likely proprietary-only
    > - [2026-04-22] Kimi K2.6: community framing as practical Opus 4.7 replacement for ~85% of tasks
    > ```
