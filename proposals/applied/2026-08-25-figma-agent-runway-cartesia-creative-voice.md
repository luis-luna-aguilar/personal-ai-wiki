---
type: proposal
sources:
  - raw/newsletters/2026-05-20-google-io-agents-agents-agents.md
  - raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa-modal-turbop.md
  - raw/newsletters/2026-05-23-ainews-all-model-labs-are-now-agent-labs.md
status: pending
created: 2026-08-25
---

# Proposal: Figma's in-canvas design agent, Runway Aleph 2.0, and Cartesia Sonic-3.5's second #1 ranking

## Summary

### The source

Between 20 and 23 May 2026, three newsletters delivered three creative-tooling signals. Every's Google I/O issue carried Katie Parrott's "Mini-Vibe Check" of Figma's new agent: a native assistant that edits the canvas directly — switching component states, restyling layouts, generating screens — built on Gemini Flash, Claude Sonnet and Figma's own fine-tuned models, two months after Figma opened its canvas to MCP-connected coding agents. Three Every staff had a day with it. Verdict: it gets a designer from blank page to first pass, but tabs render wrong, buttons double up, output is sometimes low-res, there is no reference-image input, and it ignores your design system.

AINews supplied the rest. On 22 May it reported Runway's Aleph 2.0 and Edit Studio: edit one frame and the change propagates through the whole video. On 23 May it relayed Artificial Analysis ranking Cartesia's Sonic-3.5 the #1 text-to-speech model on its Speech Arena (Elo 1218, 42 languages), alongside Cartesia's own claim of ~82ms to first audio in production — a vendor number, not an AA measurement.

### What changes

The creative dashboard lists neither Figma nor Runway, and the Cartesia page rests on one Together AI benchmark with a "limited independent validation" caveat.

- **State of Creative** gains a Figma Agent bullet under visual design and a Runway bullet under video, both unlinked and marked newsletter-sourced; no leader line is replaced or demoted. One combined Recent changes entry dated 22 May goes in and the list is re-sorted newest-first — it was out of order. Page date stays at 8 July, since both sources are older.
- That list was already over its ten-entry cap at eleven, so the two oldest entries (both 22 April) move to a new `history/state-of/creative.md`.
- **Cartesia** gains the Speech Arena ranking as a second independent benchmark plus the latency claim, separately attributed; the caveat narrows to Ink-2 only. A 23 May entry sits below the existing 16 June one; page date stays at 16 June.
- Three source pages, one per newsletter; the Every one has no URL because the raw capture holds only tracking links.

### What to weigh

No primary source was fetched — Runway and Cartesia are AINews recaps, Figma is Every's hands-on rather than Figma's announcement; the dashboard already carries such bullets, but you may want a fetch first. Narrowing Cartesia's caveat treats one extra leaderboard as enough; keep the broader wording if you disagree. Left for maintenance: the dashboard's 12 source links against 16 ids, Cartesia's singular `voice-model` subcategory, and its "launched" entry dated after the ranking.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [x] **Update** `wiki/state-of/creative.md` — add Figma bullet under "Visual design & prototyping" and Runway bullet under "AI video generation"; add one combined Recent changes entry dated 2026-05-22 and re-sort the whole Recent changes list newest-first (the live list is currently misordered); append two source ids to frontmatter and two matching links to `## Sources`
    > See draft below. `as_of` stays 2026-07-08 (both new sources are older).

- [x] **Spill** `wiki/state-of/creative.md` → `wiki/history/state-of/creative.md` — the page's Recent changes section is already at 11 entries (over the config cap of 10, predating this proposal); adding one more entry makes 12. Spilling the two oldest (both dated 2026-04-22) brings it back to 10.
    > See draft below. `wiki/history/state-of/creative.md` does not yet exist — this creates it.

- [x] **Update** `wiki/tools/cartesia.md` — add the Artificial Analysis Speech Arena #1 ranking for Sonic-3.5 as a second independent benchmark (AINews-reported) and Cartesia's own ~82ms latency claim; soften the "limited independent validation" caveat (now Ink-2-specific); add a [2026-05-23] Recent changes entry below the existing [2026-06-16] entry; add second source id and `## Sources` link
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
- **Runway Aleph 2.0 / Edit Studio** — Runway; lets users edit a single frame and propagate that edit through the rest of the video, which AINews frames as a practical productization of "reference-guided edit propagation." Current evidence is an AINews recap (linking Runway's launch post and a product-lead post); primary announcement not fetched *(as of 2026-05-22)*
```

`### Visual design & prototyping` (full subsection, new bullet appended):

```md
### Visual design & prototyping

- [Claude Design](../tools/claude-design.md) — Anthropic; research preview for collaborative prototype, slide, one-pager, and marketing-asset creation; powered by Opus 4.7; brand onboarding from codebase + design files; Pro/Max/Team/Enterprise; connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume now reported *(as of 2026-04-29, secondary coverage)*
- [Genspark Slides](../tools/genspark-slides.md) — AI presentation generation inside Genspark's broader agent/content surface; current training evidence still cautions that polished enterprise decks need deep skill/tooling support and human review, not a thin prompt *(as of 2026-06-29)*
- **Adobe Firefly AI Assistant** — Adobe assistant that executes multi-step creative tasks across Premiere, Photoshop, InDesign, and other Adobe apps, with expansion planned to ChatGPT, Claude, Gemini, Copilot, and Slack. Current evidence is newsletter coverage only *(as of 2026-06-19)*
- **Figma Agent** — Figma; a native, in-canvas design agent released 2026-05-20 that edits directly inside the canvas (switching component states, restyling layouts, generating new screens), built on a mix of Gemini Flash, Claude Sonnet, and Figma's own fine-tuned models; follows Figma opening its canvas to external MCP-connected agents (Claude Code, Cursor, Codex) in March 2026. Per Every's one-day hands-on mini-review: solves the blank-page problem for first-pass exploration and layout starts, but detail fidelity is weak (misrendered tabs, doubled buttons, low-res output), there is no image/link reference input, and it does not draw on an existing design system. Current evidence is Every's review only; primary Figma announcement not fetched *(as of 2026-05-20)*
```

Updated `## Recent changes` (full section, replaces existing; new [2026-05-22] entry inserted in date order, whole list re-sorted newest-first, two oldest 2026-04-22 entries removed — see Spill draft below; 10 entries = cap):

```md
## Recent changes

- [2026-07-08] Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp and previewed Muse Video; AINews describes an agentic generation loop with planning, tool use, code execution, and self-refinement.
- [2026-06-29] Every's PowerPoint analysis adds a caution for slide agents: polished enterprise decks require supporting skills, scripts, references, and review loops.
- [2026-06-24] OpenArt Director and Krea 2 Raw/Turbo signal creative workflows splitting between conversational editing products and open fine-tuning ecosystems.
- [2026-06-19] Palmier and Adobe Firefly Assistant show creative tooling moving toward agentic desktop workflows: video editing and multi-app creative tasks executed from natural-language instructions.
- [2026-06-04] Ideogram 4.0: #1 open image model (Arena #8 overall); JSON layout control; strong text/branding capabilities; fp8/nf4 checkpoints, ComfyUI support
- [2026-06-02] NVIDIA Cosmos 3: Mixture-of-Transformers architecture; #1 open-weight Image-to-Video and Text-to-Image; full weights + data released via Cosmos Coalition with Runway
- [2026-06-01] Video agents thesis: Ethan He (ex-NVIDIA Cosmos, ex-xAI) argues video model intelligence comes from LLMs not video training; Grok Imagine Agent beta is first public video agent; evolution mirrors coding → coding agents
- [2026-05-22] Figma released a native in-canvas design agent (Gemini Flash + Claude Sonnet + Figma fine-tuned models; Every hands-on: good for first drafts, weak on detail fidelity) and Runway launched Aleph 2.0/Edit Studio for single-frame-edit propagation across video (AINews recap); both newsletter-sourced, no primary announcement fetched, no dedicated pages yet.
- [2026-05-05] Claude creative tool connectors: Anthropic reported connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume — Claude moving from artifact generation into creative-production tool integration (secondary coverage)
- [2026-05-01] Added `AI music generation` subcategory; ElevenMusic, Suno, and Udio are the named entrants per Superhuman newsletter; AI-created artists reportedly reaching Billboard charts; rightsholder economics flagged as emerging pressure
```

Updated `## Sources` (two links appended to the existing list; existing links unchanged):

```md
- [Kimi Work Goal Mode and creative desktop agents](../sources/newsletters/kimi-goal-mode-creative-agents-2026-06.md)
- [Figma ships a native in-canvas design agent (Every mini-review)](../sources/newsletters/every-figma-agent-2026-05.md)
- [Runway Aleph 2.0 / Edit Studio (from AINews: New AI Infra unicorns)](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05.md)
```

### wiki/history/state-of/creative.md (new — spill target)

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

- **Sonic-3.5** — streaming TTS; claims #1 by Together AI benchmark; per AINews, also ranked #1 on Artificial Analysis's Speech Arena (Elo 1218; AA cites 42 languages and strong naturalness/transcript-following) — a second independent benchmark corroborating the leadership claim; Cartesia itself claims ~82ms end-to-end first-audio latency in production; sub-90ms latency; strong on structured utterances (IDs, codes, alphanumeric strings)
- **Ink-2** — streaming STT; claims #1 by Together AI benchmark; sub-90ms latency; 42 languages; same structured-utterance strength as Sonic-3.5
- Both available now via API

## Strengths

- Sub-90ms latency positions it for real-time conversational agents
- Structured-utterance handling (IDs, codes) is a practical differentiator for voice agents that read alphanumeric strings aloud or transcribe them
- 42 languages covers broad international deployment
- Sonic-3.5's TTS leadership claim is cross-validated by a second independent benchmark (Artificial Analysis Speech Arena, in addition to Together AI), as reported by AINews

## Weaknesses / caveats

- Ink-2's #1 STT claim still rests only on the Together AI benchmark; independent third-party validation is limited on that side
- Newsletter coverage only; primary Cartesia documentation not fetched

## Recent changes

- [2026-06-16] Sonic-3.5 and Ink-2 launched; claim #1 TTS and STT positions via Together AI
- [2026-05-23] AINews reports Artificial Analysis ranked Sonic-3.5 #1 on its Speech Arena (Elo 1218, 42 languages); Cartesia separately claims ~82ms end-to-end first-audio latency in production. Second independent evaluator corroborating the Together AI #1 TTS claim.

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
# url: omitted — the raw email capture contains only every.to/emails/click tracking links; canonical article URL not recoverable
published: 2026-05-20
ingested: 2026-08-25
domains: [creative]
---

# Figma ships a native in-canvas design agent (Every mini-review)

Every's "Google I/O: Agents, Agents, Agents" newsletter (2026-05-20) includes a "Mini-Vibe Check: Figma agent" section by Katie Parrott. Figma released its own agent that lives inside the canvas and edits it directly — switching component states, restyling layouts, and generating new screens — built on a mix of Google's Gemini Flash, Anthropic's Claude Sonnet, and Figma's own fine-tuned models. It follows Figma opening its canvas to external MCP-connected coding agents (Claude Code, Cursor, Codex) in March 2026. Every got access a day before the announcement; three staff (head of marketing, a senior designer, a creative designer) spent a day testing it. Verdict: not yet a trustworthy design copilot, but it solves the blank-page problem for early exploration, layout starts, and iteration; it still needs better fidelity, stronger detail handling, and richer reference inputs. This is a secondary source (newsletter review); Figma's own announcement was not fetched.

## Influenced pages
- [State of Creative](../../state-of/creative.md) — added as a new bullet under "Visual design & prototyping"

## Key claims extracted
- Figma released a native in-canvas agent on 2026-05-20 that edits the canvas directly (component states, layout restyling, new-screen generation)
- Built on a mix of Gemini Flash, Claude Sonnet, and Figma's own fine-tuned models
- Follows Figma's March 2026 move to open its canvas to external MCP-connected coding agents (Claude Code, Cursor, Codex)
- What works (Every hands-on): specific prompts yield solid early explorations, copy is preserved well, quick visual-direction exploration and product-idea mockups
- What needs work (Every hands-on): tabs rendered improperly, buttons doubled up, components drifted out of alignment, some low-res output; no image/link attachment as visual reference; relies on prompt skill or an existing frame; does not draw on an existing design system
- Every's verdict: gets designers from zero to first pass; not dependable for production-detail work yet
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

This AINews digest is mostly about AI infrastructure funding (Turbopuffer, Exa, Modal) and research threads, but its multimodal section reports that Runway launched Aleph 2.0 and the new Edit Studio, letting users edit a single frame and propagate that edit through the rest of the video (linking Runway's post and a product-lead post). AINews frames it as a practical productization of the "reference-guided edit propagation" problem. Secondary source only; Runway's own announcement was not fetched, so no resolution, duration, or multishot specs are recorded here.

## Influenced pages
- [State of Creative](../../state-of/creative.md) — added as a new bullet under "AI video generation"

## Key claims extracted
- Runway launched Aleph 2.0 and Edit Studio (reported 2026-05-22)
- Users edit a single frame and the edit propagates through the rest of the video
- AINews positions it as a productization of "reference-guided edit propagation"
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

This AINews digest covers a broad "model labs are becoming agent labs" theme (MCP going stateless, DeepSeek's permanent V4-Pro discount, Project Glasswing cybersecurity findings), and separately reports that Artificial Analysis (@ArtificialAnlys) ranked Cartesia's Sonic-3.5 as the new #1 TTS model on its Speech Arena, citing an Elo of 1218, support for 42 languages, and strong naturalness/transcript-following. In the same paragraph AINews notes that Cartesia itself claims ~82ms end-to-end first-audio latency in production — a vendor claim, not an Artificial Analysis measurement. Secondary source; neither the Artificial Analysis post nor Cartesia's own page was fetched.

## Influenced pages
- [Cartesia](../../tools/cartesia.md) — added as a second independent benchmark corroborating the existing Together AI #1 TTS claim

## Key claims extracted
- Artificial Analysis ranked Cartesia Sonic-3.5 #1 TTS on its Speech Arena, Elo 1218 (per AINews, 2026-05-23)
- Artificial Analysis cites 42 languages and strong naturalness/transcript-following
- Cartesia claims ~82ms end-to-end first-audio latency in production (vendor claim)
```

## Open questions
- Figma and Runway are both single-newsletter, no-primary-source signals with no existing wiki page. Per "new page only when justified," I've added both as bolded no-link entries in `state-of/creative.md` rather than creating `tools/figma.md` / `tools/runway.md`. Revisit if a fuller primary source (official announcement, product page) surfaces for either. Note that the Every raw does contain the full Figma mini-review text (an earlier draft wrongly said the capture was tracking-markup only), so a `tools/figma.md` page would already be reasonably supportable if you want one.
- `state-of/creative.md`'s Recent changes section was already over the 10-entry cap (11 entries) before this proposal — unrelated to any of the five signals being processed today. I've folded the fix into this proposal's spill (two oldest 2026-04-22 entries move to a new `wiki/history/state-of/creative.md`), but flagging in case you'd rather have that over-cap cleanup done as its own separate step.
- Cartesia's frontmatter uses `subcategory: voice-model` (singular) but `wiki/_schema/subcategories.md` declares the valid slug as `voice-models` (plural). This is a pre-existing mismatch, not something this proposal touches — worth a separate tag-compliance pass.
