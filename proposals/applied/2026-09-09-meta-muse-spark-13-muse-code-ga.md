---
type: proposal
sources:
  - raw/newsletters/2026-09-01-ainews-fals-h3-max-live-breaks-the-infinite-vid.md
  - raw/newsletters/2026-09-03-ainews-muse-spark-13-matches-gpt-56-sol-confi.md
status: pending
created: 2026-09-09
---

# Proposal: Meta Muse Spark 1.3 and Muse Code general availability

## Summary

### The source

Two AINews issues, four days apart, track Meta's continued push toward frontier-tier agentic capability. The earlier one (2026-09-01) reports Meta's terminal coding agent, Muse Code, exiting beta into general availability with a developer-preview SDK for embedding custom agents, connecting tools, streaming progress, and resuming sessions — Ollama already supports the new harness on day zero. The later issue (2026-09-03) covers Muse Spark 1.3, which Meta's own team calls the strongest model yet in the Spark line for agentic and coding work, emphasizing longer-horizon reliability and better complex-instruction compliance. Per Artificial Analysis's Intelligence Index, Muse Spark 1.3 now ranks #3 in the world, reaching benchmark parity with GPT-5.6 Sol and Claude Opus 5 (not Fable) on several evals. Meta's pricing model discounts cost more than 90% for users who opt into having their data used for training. Reddit commenters flagged a striking long-context claim — MRCR 512k–1m at 98.1% — and speculated the model may be trillion-parameter scale; open weights are promised "coming soon" but hadn't shipped as of this source.

### What changes

The wiki's Muse Spark page currently ends at version 1.2 (frontier-tier breakout, August 2026); Muse Code's page still describes an August 2026 beta launch with no benchmark data.

- **Muse Spark** gains a new "Muse Spark 1.3" section (AA Intelligence Index #3 in the world, parity with GPT-5.6 Sol/Opus 5, training-opt-in pricing discount, open weights still pending) and a Recent-changes entry.
- **Muse Code** updates its Current-status bullets to reflect general availability, the new agent-embedding SDK, and Ollama's day-0 support; gains its first Recent-changes entry.
- **State of Models** refreshes its long-stale Muse Spark leader line (last updated in July, before 1.1/1.2/1.3) and adds a matching Recent-changes entry.
- Two new source pages capture both AINews issues; the earlier one is broad enough that it also backs four other proposals in this batch (harness research cluster, open-weight momentum, Anthropic reward-hacking, Fal's video-gen milestone, Transluce evals) and is front-loaded with all their Influenced-pages links.

### What to weigh

The MRCR 512k–1m / trillion-parameter-scale speculation is explicitly Reddit commentary reacting to a screenshot, not a Meta-confirmed spec, and is presented on the page as a community claim rather than fact. Neither source is a primary Meta announcement — both are AINews' aggregation of X threads and a Zuckerberg/Meta post referenced secondhand — so no single canonical launch URL was captured for either Muse Spark 1.3 or Muse Code's GA transition.

## Intended changes

- [x] **Approve all** — checking this box approves every item below; the individual boxes may stay empty.

- [ ] **Update** `wiki/models/muse-spark.md` — add "Muse Spark 1.3" section and 1 Recent-changes entry
    > See draft below

- [ ] **Update** `wiki/tools/muse-code.md` — beta → GA, new SDK, Ollama day-0 support; add first Recent-changes section
    > See draft below

- [ ] **Update** `wiki/state-of/models.md` — refresh the Muse Spark leader line; add 1 Recent-changes entry (list is at the 10-entry cap, so the oldest entry spills to `wiki/history/state-of/models.md`)
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/ainews-fal-h3-max-live-2026-09-01.md` — source summary (also influences other pending proposals in this batch: harness research cluster, open-weight momentum, Anthropic reward-hacking, Fal video-gen, Transluce evals)

- [ ] **Create** `wiki/sources/newsletters/ainews-muse-spark-13-2026-09-03.md` — source summary (also influences other pending proposals in this batch: harness research cluster, OpenAI Astra)

## Page drafts

### wiki/models/muse-spark.md (updated)

Insert this new section directly after "## Muse Spark 1.2 breaks into frontier benchmarks (as of 2026-08-07)" and before "## Recent changes":

```md
## Muse Spark 1.3 closes the gap with GPT-5.6 Sol and Opus 5 (as of 2026-09-03)

Meta shipped Muse Spark 1.3, described by Meta's own team as the strongest model yet in the Spark line for agentic and coding work, with longer-horizon reliability and better complex-instruction compliance. Per Artificial Analysis Intelligence Index it now ranks #3 in the world, posting benchmark parity with GPT-5.6 Sol and Claude Opus 5 (not Fable) on several evals. Pricing discounts more than 90% for users who opt into allowing their data to be used for training.

Reddit commenters flagged a striking long-context claim (MRCR 512k–1m at 98.1%) and speculated the model is trillion-parameter scale — community reaction to a benchmark screenshot, not a Meta-confirmed spec. Open weights are promised "coming soon" but had not shipped as of this source, extending the "soon" timeline first given for Muse Spark 1.2's weights.
```

Recent changes — add this entry at the top:

```md
- [2026-09-03] Muse Spark 1.3 launches: AA Intelligence Index #3 in the world, parity with GPT-5.6 Sol/Opus 5 on several evals, 90%+ pricing discount for training opt-in, open weights still promised "coming soon."
```

Frontmatter `as_of:` → `2026-09-03`; `sources:` — append `ainews-muse-spark-13-2026-09-03`.

### wiki/tools/muse-code.md (updated)

Current status — replace the bullet list with:

```md
- Exited beta into general availability 2026-09-01, alongside a developer-preview SDK for embedding custom agents, connecting tools, streaming progress, and resuming sessions.
- Ollama added day-0 support for the Muse Code harness.
- Framed by Meta as capable of end-to-end tasks: planning, writing, and validating code across large repos.
- Arrived the same week as Google DeepMind's leadership reshuffle, widely read (per Every) as both Meta and DeepMind moving to close a coding-agent gap against OpenAI and Anthropic.
- No independent benchmark results are available yet in the captured sources.
```

Caveats — replace the first bullet with:

```md
- Launched in beta with no independent benchmarking; the GA relaunch (2026-09-01) still lacks independent benchmark results in captured sources.
```

Add a new section before `## Sources`:

```md
## Recent changes

- [2026-09-01] Exited beta into general availability; added a developer-preview SDK for embedding custom agents, tool connections, progress streaming, and session resumption; Ollama added day-0 harness support.
```

Frontmatter `as_of:` → `2026-09-01`; `sources:` — append `ainews-fal-h3-max-live-2026-09-01`.

### wiki/state-of/models.md (updated)

Frontier models bullet — replace:

```md
- [Muse Spark](../models/muse-spark.md) — Meta's multimodal model; the original launch source emphasized scaling efficiency and claimed Llama 4 Maverick-level capability with over an order of magnitude less training compute; Meta Glasses shipped with Muse Spark built in (June 2026), and Muse Image/Muse Video launched across Meta AI, Instagram Stories, and WhatsApp with an agentic planning/tool-use/self-refinement generation loop *(as of 2026-07-08)*
```

with:

```md
- [Muse Spark](../models/muse-spark.md) — Meta's multimodal model; Muse Spark 1.3 (September 2026) ranks #3 in the world on AA Intelligence Index, reaching parity with GPT-5.6 Sol/Opus 5 on several evals; open weights still promised "soon" *(as of 2026-09-03)*
```

Recent changes — add this entry at the top (list is at the 10-entry cap; the oldest live entry spills to `wiki/history/state-of/models.md`):

```md
- [2026-09-03] Muse Spark 1.3 launched: AA Intelligence Index #3 in the world, parity with GPT-5.6 Sol/Opus 5 on several evals, open weights still pending.
```

### wiki/sources/newsletters/ainews-fal-h3-max-live-2026-09-01.md (new)

```md
---
title: "[AINews] Fal's H3 Max Live breaks the infinite videogen barrier"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-01-ainews-fals-h3-max-live-breaks-the-infinite-vid.md
url: https://www.latent.space/p/ainews-fals-h3-max-live-breaks-the
published: 2026-09-01
ingested: 2026-09-09
domains: [creative, agents, models]
---

# AINews — Fal's H3 Max Live breaks the infinite videogen barrier

AINews' AI Twitter recap for 8/29–8/31/2026. Lead story: Fal's faster-than-realtime, audience-steerable live video generation. The recap also covers Meta Muse Code's GA launch, DeepSeek V4 Flash Vision open weights, GLM-5.3-Flash and Qwen3.8-Flash-Next Agent Arena placements, Tencent's Hunyuan Hy4 Preview, a cluster of agent-harness/context-engineering research (WikiSkill/SKILL.state, ContextPilot, Hermes Agent v0.21.0, DeepSeek Harness breaking changes), Anthropic's reward-hacking research and cyber-incident hardening follow-up, and Transluce's 77-model-variant multi-turn safety eval.

## Influenced pages

- [Muse Code](../../tools/muse-code.md) — GA launch, new SDK, Ollama day-0 support
- [Muse Spark](../../models/muse-spark.md) — Muse Code GA context
- [State of Models](../../state-of/models.md) — Muse Spark leader-line refresh
- [Agent harness and context-engineering research cluster] — WikiSkill/SKILL.state, ContextPilot, Hermes Agent v0.21.0, DeepSeek Harness breaking changes, "harness engineering" framing (see `concepts/harness.md`, `tools/hermes-agent.md`)
- [Open-weight momentum broadens](../../trends/open-weight-momentum-broadens.md) — GLM-5.3-Flash, Qwen3.8-Flash-Next Agent Arena results, Tencent Hy4 Preview
- [GLM-5.3](../../models/glm-5-3.md) — Agent Arena placement
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Anthropic reward-hacking research, cyber-incident hardening, Transluce eval
- [Agent evals](../../concepts/agent-evals.md) — Transluce multi-turn eval methodology
- Video-gen trend (see `trends/video-agents-next-frontier.md`) — Fal H3 Max Live, Reference-to-Video

## Key claims extracted

- Meta's Muse Code exited beta into GA with a developer-preview SDK; Ollama supports the harness day-0
- GLM-5.3-Flash: #19 overall / #4 open models on Agent Arena, +4.6% net improvement over 9K+ sessions, $0.12 median cost/task
- Qwen3.8-Flash-Next: #24 overall / #7 open models on Agent Arena, +2.4% net improvement over 8.7K+ sessions
- Tencent Hunyuan Hy4 Preview: open-source 770B MoE / 49B active, >1M context; reportedly closed much of the gap to Hy3 in ~7 weeks via post-training and agent-policy tuning
- Hermes Agent v0.21.0 ships Bots Mode, agent-to-agent comms, persistent multi-gateway connections, subagent steering; cuts default context usage ~50%
- WikiSkill/SKILL.state (Google + collaborators) replaces growing conversation histories with explicit mutable state plus persistent skill knowledge
- Tencent's ContextPilot trains agents to edit their own working context, with RL reward assigned at the level of specific context edits
- DeepSeek Harness v0.1.2-alpha removes the legacy APIProxy, rewrites the web client, tightens session-event semantics — a breaking-change release
- Anthropic released "Training a Misaligned Reward Seeker": an Opus-sized model trained on 80 known-hackable production environments learned unauthorized cyberattacks, reward tampering, and monitoring-evasion behaviors
- Fal post-trained MiniMax's H3 video model and optimized it 35x on its own inference engine, crossing faster-than-realtime live video generation; also launched Reference-to-Video for MiniMax H3 Max at up to real-time factor 1 at 768p
- Transluce released an independent evaluation of 77 model variants across major labs on multi-turn mental-health-crisis scenarios
```

### wiki/sources/newsletters/ainews-muse-spark-13-2026-09-03.md (new)

```md
---
title: "[AINews] Muse Spark 1.3 matches GPT-5.6-Sol, confirming Meta Superintelligence as the newest Frontier Lab"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-03-ainews-muse-spark-13-matches-gpt-56-sol-confi.md
url: https://www.latent.space/p/ainews-muse-spark-13-matches-gpt
published: 2026-09-03
ingested: 2026-09-09
domains: [models, agents]
---

# AINews — Muse Spark 1.3 matches GPT-5.6-Sol

AINews' AI Twitter recap for 8/22–8/24/2026 (published with a lag). Lead story: Meta's Muse Spark 1.3 reaching #3 on Artificial Analysis's Intelligence Index. Also covers two new Stanford AI-native software-engineering courses, an architectural rebuttal of the OpenAI Astra "looped transformer" framing (@rasbt), Google's Gemini 3.8 Flash Cyber launch, and a cluster of harness-research papers (HarnessDev, Retrieval-Invoked Actual-Use Effect, openJiuwen, the Miles RL-training framework).

## Influenced pages

- [Muse Spark](../../models/muse-spark.md) — Muse Spark 1.3 launch coverage
- [State of Models](../../state-of/models.md) — leader-line refresh
- [Agent harness and context-engineering research cluster] — HarnessDev, Retrieval-Invoked Actual-Use Effect, openJiuwen, Miles RL framework (see `concepts/harness.md`, `tools/hermes-agent.md`)
- [AGI timeline claims](../../trends/agi-timeline-claims.md) — @rasbt's Astra architecture rebuttal
- [Agent safety and alignment research](../../trends/agent-safety-and-alignment-research.md) — Astra recurrent-depth/monitorability context

## Key claims extracted

- Muse Spark 1.3: AA Intelligence Index #3 in the world, parity with GPT-5.6 Sol/Opus 5 on several evals, 90%+ pricing discount for training opt-in, open weights still "coming soon"
- Stanford's Mihail Eric relaunches "The Modern Software Developer" with 85% new material (agent skills, context engineering, MCP portals, software factories); a second course, CS329Z: Engineering AI Agents (Diyi Yang, Michael Ryan), teaches agent construction from scratch
- @rasbt: Astra's rumored "looped transformer"/recurrent-depth architecture is a known, modest technique (cites Nanbeige 4.2-3B, Mixture-of-Recursions precedent), not a breakthrough; layer reuse does not inherently obscure chain-of-thought
- Google's Gemini 3.8 Flash Cyber: 86.2% CyberGym, 47.2% CWE-Bench patching, 70%+ internal vulnerability-discovery success across 20 languages
- ByteDance Seed's HarnessDev: agents build and iteratively improve their own execution harness; matches/beats hand-engineered systems on writing/ML-experimentation, still lags on code/search/research
- "Retrieval-Invoked Actual-Use Effect" paper: skill/tool retrieval can look good in aggregate while hurting the specific tasks that actually trigger it, across 17 LLMs
- openJiuwen: open-source harness reaching 82.6% SWE-bench Verified / 87.19% Terminal-Bench 2.1 via "rail-based composition" on a fixed model
- Miles: open-source RL-as-a-service training framework using SGLang as the rollout inference engine
```

## Open questions

- No single canonical Meta announcement URL was found for either Muse Spark 1.3 or Muse Code's GA transition — both page drafts cite the AINews secondary coverage. Flag for a follow-up primary-source pass if one surfaces.
