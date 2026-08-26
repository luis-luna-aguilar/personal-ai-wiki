---
type: proposal
source: raw/newsletters/2026-05-20-google-io-agents-agents-agents.md
status: pending
created: 2026-08-25
---

# Proposal: Figma's in-canvas design agent, Runway Aleph 2.0, and Cartesia Sonic-3.5's second #1 ranking

## Summary
Three lightweight-ingest creative/voice signals: Figma shipped a native in-canvas design agent (no existing Figma page); Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video (no existing Runway page); and Cartesia's Sonic-3.5 picked up a second independent #1 TTS ranking (Artificial Analysis Speech Arena), corroborating the existing Together AI claim on `tools/cartesia.md`.

## Intended changes

- [x] **Update** `wiki/state-of/creative.md` — add Figma bullet under "Visual design & prototyping" and Runway bullet under "AI video generation"; add one combined Recent changes entry
    > See draft below. `as_of` stays 2026-07-08 (both new sources are older).

- [x] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — the page's Recent changes section is already at 11 entries (over the config cap of 10, predating this proposal); adding one more entry makes 12. Spilling the two oldest (both dated 2026-04-22) brings it back to 10.
    > See draft below. `wiki/history/state-of/creative.md` does not yet exist — this creates it.

- [x] **Update** `wiki/tools/cartesia.md` — add the Artificial Analysis Speech Arena #1 ranking for Sonic-3.5 as a second independent benchmark; soften the "limited independent validation" caveat (now Ink-2-specific); add a Recent changes entry
    > See draft below. `as_of` stays 2026-06-16 (new source is older).

- [x] **Create** `wiki/sources/newsletters/every-figma-agent-2026-05.md` — source summary
- [x] **Create** `wiki/sources/newsletters/ainews-new-ai-infra-unicorns-2026-05.md` — source summary (Runway detail only; the newsletter is a broader infra digest)
- [x] **Create** `wiki/sources/newsletters/ainews-all-model-labs-agent-labs-2026-05.md` — source summary (Cartesia detail only; the newsletter is a broader digest)

## Page drafts

### wiki/state-of/creative.md (updated)

Frontmatter changes (sources list only; `as_of` unchanged at 2026-07-08):

```yaml
sources: [legacy-ai-tools-roadmap-xlsx, seedance-2, luma-dream-machine, heygen-homepage, genspark-slides, stitch-google, claude-design-anthropic-labs, ai-music-commercialization-2026-05-01, claude-creative-tool-connectors-2026-04-29, video-agents-ethan-he-june-2026, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, powerpoint-agent-skill-failure-mode-2026-06, open-creative-workflows-2026-06, meta-muse-image-video-2026-07, kimi-goal-mode-creative-agents-2026-06, every-figma-agent-2026-05, ainews-new-ai-infra-unicorns-2026-05]
```

`### AI video generation` (full subsection, new bullet appended):

```md
### AI video generation

- [NVIDIA Cosmos 3 Super](../models/cosmos-3.md) — NVIDIA; #1 open-weight Image-to-Video; Mixture-of-Transformers architecture (autoregressive reasoner + diffusion generator); full weights released via Cosmos Coalition with Runway *(as of 2026-06-02)*
- [Seedance 2.0](../tools/seedance-2.md) — ByteDance Seed's multimodal audio-video generation product; strongest distinction is synchronized audio-video creative output *(as of 2026-04-22)*
- [Dream Machine](../tools/dream-machine.md) — Luma's broader generative-video and editing surface *(as of 2026-04-22)*
- **Grok Imagine Agent** — xAI; early beta; first public video agent implementation: LLM plans and iterates using video generation as a tool, calling FFmpeg and editing tools for post-processing; long-form video as a sequence of planned, generated, and edited clips *(as of 2026-06-01)*
- **OpenArt Director** — conversational "vibe directing" product for generating and editing clips up to five minutes with consistent characters, voiceover, music, and captions; current evidence is newsletter coverage pending primary-source fetch *(as of 2026-06-24)*
- **Muse Video** — Meta Superintelligence Labs preview; paired with Muse Image and described in AINews as using agentic planning, tool use, code execution, and self-refinement before rendering *(as of 2026-07-08)*
- **Palmier** — Mac-native video editor where Claude or Codex can generate, organize, and trim footage directly in-app; integrates leading video models such as Seedance 2.0, Kling V3, and Grok Imagine. Current evidence is newsletter coverage only *(as of 2026-06-19)*
- **Runway Aleph 2.0 / Edit Studio** — Runway; lets users edit a single frame and propagate that edit through the rest of the video, supporting multishot sequences up to 30 seconds at 1080p while preserving the rest of the scene; a productized version of "reference-guided edit propagation." Current evidence is AINews recap of Runway's own launch posts, not an independently fetched primary announcement *(as of 2026-05-22)*
```

`### Visual design & prototyping` (full subsection, new bullet appended):

```md
### Visual design & prototyping

- [Claude Design](../tools/claude-design.md) — Anthropic; research preview for collaborative prototype, slide, one-pager, and marketing-asset creation; powered by Opus 4.7; brand onboarding from codebase + design files; Pro/Max/Team/Enterprise; connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume now reported *(as of 2026-04-29, secondary coverage)*
- [Genspark Slides](../tools/genspark-slides.md) — AI presentation generation inside Genspark's broader agent/content surface; current training evidence still cautions that polished enterprise decks need deep skill/tooling support and human review, not a thin prompt *(as of 2026-06-29)*
- **Adobe Firefly AI Assistant** — Adobe assistant that executes multi-step creative tasks across Premiere, Photoshop, InDesign, and other Adobe apps, with expansion planned to ChatGPT, Claude, Gemini, Copilot, and Slack. Current evidence is newsletter coverage only *(as of 2026-06-19)*
- **Figma Agent** — Figma; a native, in-canvas design agent that edits directly inside the canvas (switching component states, restyling layouts, generating new screens), built on a mix of Gemini Flash, Claude Sonnet, and Figma's own fine-tuned models; follows Figma opening its canvas to external MCP-connected agents (Claude Code, Cursor, Codex) in March 2026. Current evidence is a single newsletter mini-review (Every); the raw newsletter capture itself contained mostly link-tracking markup rather than article body text, so treat feature detail as provisional pending a primary Figma announcement *(as of 2026-05-20)*
```

Updated `## Recent changes` (full section, new entry added at top, two oldest entries removed — see Spill draft below):

```md
## Recent changes

- [2026-05-22] Figma shipped a native in-canvas design agent (Gemini Flash + Claude Sonnet + Figma fine-tuned models) and Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video; both are newsletter-sourced, no-existing-page signals pending primary confirmation.
- [2026-07-08] Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp and previewed Muse Video; AINews describes an agentic generation loop with planning, tool use, code execution, and self-refinement.
- [2026-06-19] Palmier and Adobe Firefly Assistant show creative tooling moving toward agentic desktop workflows: video editing and multi-app creative tasks executed from natural-language instructions.
- [2026-06-29] Every's PowerPoint analysis adds a caution for slide agents: polished enterprise decks require supporting skills, scripts, references, and review loops.
- [2026-06-24] OpenArt Director and Krea 2 Raw/Turbo signal creative workflows splitting between conversational editing products and open fine-tuning ecosystems.
- [2026-06-01] Video agents thesis: Ethan He (ex-NVIDIA Cosmos, ex-xAI) argues video model intelligence comes from LLMs not video training; Grok Imagine Agent beta is first public video agent; evolution mirrors coding → coding agents
- [2026-05-05] Claude creative tool connectors: Anthropic reported connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume — Claude moving from artifact generation into creative-production tool integration (secondary coverage)
- [2026-06-04] Ideogram 4.0: #1 open image model (Arena #8 overall); JSON layout control; strong text/branding capabilities; fp8/nf4 checkpoints, ComfyUI support
- [2026-06-02] NVIDIA Cosmos 3: Mixture-of-Transformers architecture; #1 open-weight Image-to-Video and Text-to-Image; full weights + data released via Cosmos Coalition with Runway
- [2026-05-01] Added `AI music generation` subcategory; ElevenMusic, Suno, and Udio are the named entrants per Superhuman newsletter; AI-created artists reportedly reaching Billboard charts; rightsholder economics flagged as emerging pressure
```

### wiki/history/state-of/creative.md (new)

```md
# State of Creative — History

## Archived from current page on 2026-08-25

- [2026-04-22] Created the `creative` domain and added initial pages for video generation, avatar video, UI generation, and slides workflows from the legacy workbook exception
- [2026-04-22] Added `Visual design & prototyping` subcategory; [Claude Design](../../tools/claude-design.md) full launch via Anthropic Labs
```

### wiki/tools/cartesia.md (updated)

Frontmatter changes (sources list only; `as_of` unchanged at 2026-06-16):

```yaml
sources: [cartesia-voice-june-2026, ainews-all-model-labs-agent-labs-2026-05]
```

`## Current status` through `## Sources` (full sections, replaces existing):

```md
## Current status (as of 2026-06-16)

- **Sonic-3.5** — streaming TTS; claims #1 by Together AI benchmark; also ranks #1 on Artificial Analysis's Speech Arena (Elo 1218, 42 languages, ~82ms end-to-end first-audio latency in production) — a second independent benchmark corroborating the leadership claim; sub-90ms latency; strong on structured utterances (IDs, codes, alphanumeric strings)
- **Ink-2** — streaming STT; claims #1 by Together AI benchmark; sub-90ms latency; 42 languages; same structured-utterance strength as Sonic-3.5
- Both available now via API

## Strengths

- Sub-90ms latency positions it for real-time conversational agents
- Structured-utterance handling (IDs, codes) is a practical differentiator for voice agents that read alphanumeric strings aloud or transcribe them
- 42 languages covers broad international deployment
- Sonic-3.5's TTS leadership claim is now cross-validated by a second independent benchmark (Artificial Analysis Speech Arena, in addition to Together AI)

## Weaknesses / caveats

- Ink-2's #1 STT claim still rests only on the Together AI benchmark; independent third-party validation is limited on that side
- Newsletter coverage only; primary Cartesia documentation not fetched

## Recent changes

- [2026-05-23] Cartesia Sonic-3.5 ranked #1 on Artificial Analysis's Speech Arena (Elo 1218, 42 languages, ~82ms end-to-end first-audio latency in production), corroborating the earlier Together AI #1 claim from a second independent evaluator.
- [2026-06-16] Sonic-3.5 and Ink-2 launched; claim #1 TTS and STT positions via Together AI

## Sources

- [Cartesia voice models — June 2026](../sources/newsletters/cartesia-voice-june-2026.md)
- [AINews — All Model Labs are now Agent Labs (May 23)](../sources/newsletters/ainews-all-model-labs-agent-labs-2026-05.md)
```

### wiki/sources/newsletters/every-figma-agent-2026-05.md (new)

```md
---
title: Figma ships a native in-canvas design agent (Every mini-review)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-20-google-io-agents-agents-agents.md
url: https://every.to/context-window/google-i-o-agents-agents-agents
published: 2026-05-20
ingested: 2026-08-25
domains: [creative]
---

# Figma ships a native in-canvas design agent (Every mini-review)

Every's "Google I/O: Agents, Agents, Agents" newsletter included a short "Mini-Vibe Check" on a new Figma agent that lives inside the canvas and edits directly — switching component states, restyling layouts, and generating new screens — built on a mix of Gemini Flash, Claude Sonnet, and Figma's own fine-tuned models. It follows Figma opening its canvas to external MCP-connected agents (Claude Code, Cursor, Codex) in March 2026. **Caveat:** the saved raw capture of this newsletter is mostly Every's link-tracking markup; the substantive description above could not be independently re-verified from the raw file's visible body text, only from the subject-line teaser and general knowledge of the item as summarized in the digest triage. Treat as provisional pending a primary Figma announcement or a cleaner re-fetch.

## Influenced pages
- [State of Creative](../../state-of/creative.md) — added as a new bullet under "Visual design & prototyping"

## Key claims extracted
- Figma agent lives inside the canvas and edits directly (component states, layout restyling, new-screen generation)
- Built on a mix of Gemini Flash, Claude Sonnet, and Figma's own fine-tuned models
- Follows Figma's March 2026 move to open its canvas to external MCP-connected coding agents
```

### wiki/sources/newsletters/ainews-new-ai-infra-unicorns-2026-05.md (new)

```md
---
title: "Runway Aleph 2.0 / Edit Studio (from AINews: New AI Infra unicorns)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa-modal-turbop.md
url: https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa
published: 2026-05-22
ingested: 2026-08-25
domains: [creative]
---

# Runway Aleph 2.0 / Edit Studio (from AINews: New AI Infra unicorns)

This AINews digest is mostly about AI infrastructure funding (Turbopuffer, Exa, Modal, Hark) and research threads, but it also reports that Runway launched Aleph 2.0 and a new Edit Studio, letting users edit a single frame and propagate that edit through the rest of a video, supporting multishot sequences up to 30 seconds at 1080p while preserving the rest of the scene. Framed as a practical productization of "reference-guided edit propagation."

## Influenced pages
- [State of Creative](../../state-of/creative.md) — added as a new bullet under "AI video generation"

## Key claims extracted
- Runway Aleph 2.0 + Edit Studio: single-frame edits propagate through the rest of a video
- Supports multishot sequences up to 30 seconds at 1080p
- Positioned around targeted edits that preserve the rest of the scene, not full regeneration
```

### wiki/sources/newsletters/ainews-all-model-labs-agent-labs-2026-05.md (new)

```md
---
title: "Cartesia Sonic-3.5 tops Speech Arena (from AINews: All Model Labs are now Agent Labs)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
url: https://www.latent.space/p/ainews-all-model-labs-are-now-agent
published: 2026-05-23
ingested: 2026-08-25
domains: [voice]
---

# Cartesia Sonic-3.5 tops Speech Arena (from AINews: All Model Labs are now Agent Labs)

This AINews digest covers a broad "model labs are becoming agent labs" theme (MCP going stateless, DeepSeek's permanent V4-Pro discount, Project Glasswing cybersecurity findings), and separately reports that Artificial Analysis ranked Cartesia's Sonic-3.5 as the new #1 TTS model on its Speech Arena, citing an Elo of 1218, support for 42 languages, and strong naturalness/transcript-following; Cartesia claims ~82ms end-to-end first-audio latency in production.

## Influenced pages
- [Cartesia](../../tools/cartesia.md) — added as a second independent benchmark corroborating the existing Together AI #1 TTS claim

## Key claims extracted
- Cartesia Sonic-3.5 ranked #1 on Artificial Analysis's Speech Arena, Elo 1218
- 42 languages, strong naturalness and transcript-following
- ~82ms end-to-end first-audio latency claimed in production
```

## Open questions
- Figma and Runway are both single-newsletter, no-primary-source signals with no existing wiki page. Per "new page only when justified," I've added both as bolded no-link entries in `state-of/creative.md` rather than creating `tools/figma.md` / `tools/runway.md`. Revisit if a fuller primary source (official announcement, product page) surfaces for either.
- `state-of/creative.md`'s Recent changes section was already over the 10-entry cap (11 entries) before this proposal — unrelated to any of the five signals being processed today. I've folded the fix into this proposal's spill (two oldest 2026-04-22 entries move to a new `wiki/history/state-of/creative.md`), but flagging in case you'd rather have that over-cap cleanup done as its own separate step.
- Cartesia's frontmatter uses `subcategory: voice-model` (singular) but `wiki/_schema/subcategories.md` declares the valid slug as `voice-models` (plural). This is a pre-existing mismatch, not something this proposal touches — worth a separate tag-compliance pass.
