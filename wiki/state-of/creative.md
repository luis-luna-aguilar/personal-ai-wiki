---
title: State of Creative
type: state-of
domains: [creative]
tags: []
as_of: 2026-07-08
sources: [legacy-ai-tools-roadmap-xlsx, seedance-2, luma-dream-machine, heygen-homepage, genspark-slides, stitch-google, claude-design-anthropic-labs, ai-music-commercialization-2026-05-01, claude-creative-tool-connectors-2026-04-29, video-agents-ethan-he-june-2026, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, powerpoint-agent-skill-failure-mode-2026-06, open-creative-workflows-2026-06, meta-muse-image-video-2026-07, kimi-goal-mode-creative-agents-2026-06]
---

# State of Creative

Current state of AI creative tools — video generation, avatar video, slide generation, and UI-generation surfaces. Organized by subcategory.

## Subcategories

### AI video generation

- [NVIDIA Cosmos 3 Super](../models/cosmos-3.md) — NVIDIA; #1 open-weight Image-to-Video; Mixture-of-Transformers architecture (autoregressive reasoner + diffusion generator); full weights released via Cosmos Coalition with Runway *(as of 2026-06-02)*
- [Seedance 2.0](../tools/seedance-2.md) — ByteDance Seed's multimodal audio-video generation product; strongest distinction is synchronized audio-video creative output *(as of 2026-04-22)*
- [Dream Machine](../tools/dream-machine.md) — Luma's broader generative-video and editing surface *(as of 2026-04-22)*
- **Grok Imagine Agent** — xAI; early beta; first public video agent implementation: LLM plans and iterates using video generation as a tool, calling FFmpeg and editing tools for post-processing; long-form video as a sequence of planned, generated, and edited clips *(as of 2026-06-01)*
- **OpenArt Director** — conversational "vibe directing" product for generating and editing clips up to five minutes with consistent characters, voiceover, music, and captions; current evidence is newsletter coverage pending primary-source fetch *(as of 2026-06-24)*
- **Muse Video** — Meta Superintelligence Labs preview; paired with Muse Image and described in AINews as using agentic planning, tool use, code execution, and self-refinement before rendering *(as of 2026-07-08)*
- **Palmier** — Mac-native video editor where Claude or Codex can generate, organize, and trim footage directly in-app; integrates leading video models such as Seedance 2.0, Kling V3, and Grok Imagine. Current evidence is newsletter coverage only *(as of 2026-06-19)*

### AI image generation

- [Ideogram 4.0](../models/ideogram-4.md) — Ideogram; 9.3B DiT; #8 overall Image Arena, #1 open image model; strong text rendering and structured layout control via JSON prompting; fp8/nf4 checkpoints with ComfyUI support; no commercial license *(as of 2026-06-04)*
- [Muse Image](../models/muse-spark.md) — Meta; launched inside Meta AI, Instagram Stories, and WhatsApp; Superhuman reports #2 on Arena text-to-image behind GPT-Image-2; uses agentic planning/self-refinement loop per AINews *(as of 2026-07-08)*
- **Krea 2 Raw / Turbo** — open-weight image model pair; Raw is positioned as an undistilled fine-tuning checkpoint, while Turbo is a distilled fast-inference checkpoint with reported day-0 diffusers, LoRA, and training-tool support *(as of 2026-06-24)*

### AI avatar video

- [HeyGen](../tools/heygen.md) — avatar-video product centered on reusable synthetic presenters for communication and marketing workflows *(as of 2026-04-22)*

### UI generation

- [Stitch](../tools/stitch.md) — Google's design-to-interface generation surface, bridging prompts, references, and interface artifacts *(as of 2026-04-22)*

### Visual design & prototyping

- [Claude Design](../tools/claude-design.md) — Anthropic; research preview for collaborative prototype, slide, one-pager, and marketing-asset creation; powered by Opus 4.7; brand onboarding from codebase + design files; Pro/Max/Team/Enterprise; connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume now reported *(as of 2026-04-29, secondary coverage)*
- [Genspark Slides](../tools/genspark-slides.md) — AI presentation generation inside Genspark's broader agent/content surface; current training evidence still cautions that polished enterprise decks need deep skill/tooling support and human review, not a thin prompt *(as of 2026-06-29)*
- **Adobe Firefly AI Assistant** — Adobe assistant that executes multi-step creative tasks across Premiere, Photoshop, InDesign, and other Adobe apps, with expansion planned to ChatGPT, Claude, Gemini, Copilot, and Slack. Current evidence is newsletter coverage only *(as of 2026-06-19)*

### AI music generation

- **Suno** — category anchor for AI-generated music with reported subscriber and revenue milestones; no dedicated tool page yet, pending primary source fetch *(as of 2026-05-01)*
- **Udio** — category anchor alongside Suno; AI-generated music *(as of 2026-05-01)*
- **ElevenMusic** — ElevenLabs' new entrant to AI music generation *(as of 2026-05-01)*

## Recent changes

- [2026-07-08] Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp and previewed Muse Video; AINews describes an agentic generation loop with planning, tool use, code execution, and self-refinement.
- [2026-06-19] Palmier and Adobe Firefly Assistant show creative tooling moving toward agentic desktop workflows: video editing and multi-app creative tasks executed from natural-language instructions.
- [2026-06-29] Every's PowerPoint analysis adds a caution for slide agents: polished enterprise decks require supporting skills, scripts, references, and review loops.
- [2026-06-24] OpenArt Director and Krea 2 Raw/Turbo signal creative workflows splitting between conversational editing products and open fine-tuning ecosystems.
- [2026-06-01] Video agents thesis: Ethan He (ex-NVIDIA Cosmos, ex-xAI) argues video model intelligence comes from LLMs not video training; Grok Imagine Agent beta is first public video agent; evolution mirrors coding → coding agents
- [2026-05-05] Claude creative tool connectors: Anthropic reported connectors for Adobe, Blender, Fusion, Ableton, Splice, SketchUp, Affinity, Resolume — Claude moving from artifact generation into creative-production tool integration (secondary coverage)
- [2026-06-04] Ideogram 4.0: #1 open image model (Arena #8 overall); JSON layout control; strong text/branding capabilities; fp8/nf4 checkpoints, ComfyUI support
- [2026-06-02] NVIDIA Cosmos 3: Mixture-of-Transformers architecture; #1 open-weight Image-to-Video and Text-to-Image; full weights + data released via Cosmos Coalition with Runway
- [2026-05-01] Added `AI music generation` subcategory; ElevenMusic, Suno, and Udio are the named entrants per Superhuman newsletter; AI-created artists reportedly reaching Billboard charts; rightsholder economics flagged as emerging pressure
- [2026-04-22] Created the `creative` domain and added initial pages for video generation, avatar video, UI generation, and slides workflows from the legacy workbook exception
- [2026-04-22] Added `Visual design & prototyping` subcategory; [Claude Design](../tools/claude-design.md) full launch via Anthropic Labs

## Sources

- [AI Tools & Roadmap legacy workbook](../sources/notes/legacy-ai-tools-roadmap-xlsx.md)
- [AI music commercialization — Superhuman 2026-05-01](../sources/newsletters/ai-music-commercialization-2026-05-01.md)
- [Claude creative tool connectors](../sources/newsletters/claude-creative-tool-connectors-2026-04-29.md)
- [Seedance 2.0 product page](../sources/articles/seedance-2.md)
- [Luma Dream Machine page](../sources/articles/luma-dream-machine.md)
- [HeyGen official page](../sources/articles/heygen-homepage.md)
- [Genspark Slides product page](../sources/articles/genspark-slides.md)
- [Google Stitch page](../sources/articles/stitch-google.md)
- [PowerPoint remains hard for agents](../sources/newsletters/powerpoint-agent-skill-failure-mode-2026-06.md)
- [Open creative workflows and vibe directing](../sources/newsletters/open-creative-workflows-2026-06.md)
- [Meta Muse Image and Muse Video](../sources/newsletters/meta-muse-image-video-2026-07.md)
- [Kimi Work Goal Mode and creative desktop agents](../sources/newsletters/kimi-goal-mode-creative-agents-2026-06.md)
