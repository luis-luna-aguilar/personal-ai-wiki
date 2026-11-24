---
title: State of Creative
type: state-of
domains: [creative]
tags: []
as_of: 2026-10-20
sources: [legacy-ai-tools-roadmap-xlsx, seedance-2, luma-dream-machine, heygen-homepage, genspark-slides, stitch-google, claude-design-anthropic-labs, ai-music-commercialization-2026-05-01, claude-creative-tool-connectors-2026-04-29, video-agents-ethan-he-june-2026, ainews-cosmos-nemotron-june-2026, ainews-ideogram-june-2026, powerpoint-agent-skill-failure-mode-2026-06, open-creative-workflows-2026-06, meta-muse-image-video-2026-07, kimi-goal-mode-creative-agents-2026-06, google-io-agents-agents-agents, ainews-new-ai-infra-unicorns-2026-05-22, bfl-flux-3-2026-07-24, ainews-fal-h3-max-live-2026-09-01, latent-space-runway-worldprompt-2026-09-25, suno-speech-beta-2026-10, claude-cowork-is-now-claude-2026-09-16, quiverai-arrow-2-launch-2026-09-16, quiverai-arrow-2-announcement-2026-09-16]
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
- **Fal H3 Max Live** — Fal optimized a post-trained MiniMax H3 video model 35x on its own inference engine, crossing faster-than-realtime continuous generation for a live, audience-steerable stream; content quality is still poor, the milestone is the infrastructure *(as of 2026-09-01)*
- **Palmier** — Mac-native video editor where Claude or Codex can generate, organize, and trim footage directly in-app; integrates leading video models such as Seedance 2.0, Kling V3, and Grok Imagine. Current evidence is newsletter coverage only *(as of 2026-06-19)*
- [Runway Aleph 2.0 / Edit Studio](../tools/runway.md) — Runway; lets users edit a single frame and propagate that edit through the rest of the video, which AINews frames as a practical productization of "reference-guided edit propagation." Current evidence is an AINews recap (linking Runway's launch post and a product-lead post); primary announcement not fetched *(as of 2026-05-22)*
- [Runway GWM Worlds 2](../tools/runway.md) — Runway; research preview streaming interactive worlds at 720p/24fps with 48kHz audio, steered by WorldPrompt (fixed first frame plus timestamped, live-promptable events). Open problems: error accumulation, long-term memory, realistic outcomes for unlikely actions. Competes with Genie 3, Odyssey-2 Pro and World Labs' RTFM *(as of 2026-09-25)*
- [FLUX 3](../tools/flux-3.md) — Black Forest Labs; unified image/video/audio/action-prediction architecture ("Self Flow"); native audio generation, video-to-video character continuity, agentic multi-shot clip chaining; companion FLUX3-mimic extends it to robot control (testing with Audi); open-weights Dev version planned *(as of 2026-07-24)*

### AI image generation

- [Ideogram 4.0](../models/ideogram-4.md) — Ideogram; 9.3B DiT; #8 overall Image Arena, #1 open image model; strong text rendering and structured layout control via JSON prompting; fp8/nf4 checkpoints with ComfyUI support; no commercial license *(as of 2026-06-04)*
- [Muse Image](../models/muse-spark.md) — Meta; launched inside Meta AI, Instagram Stories, and WhatsApp; Superhuman reports #2 on Arena text-to-image behind GPT-Image-2; uses agentic planning/self-refinement loop per AINews *(as of 2026-07-08)*
- [Nano Banana 2](../models/nano-banana-2.md) — Google; uses Gemini's world understanding plus real-time web search imagery to generate images reflecting current real-world conditions *(as of 2026-04-22)*
- **Krea 2 Raw / Turbo** — open-weight image model pair; Raw is positioned as an undistilled fine-tuning checkpoint, while Turbo is a distilled fast-inference checkpoint with reported day-0 diffusers, LoRA, and training-tool support *(as of 2026-06-24)*
- [Arrow 2](../models/arrow-2.md) — QuiverAI; vector model: writes editable SVG graphics rather than raster images (illustrations, diagrams, vectorization, micro-animations); the Arrow 2 Telos tier adds frontier-model refinement for harder briefs *(as of 2026-09-16)*

### AI avatar video

- [HeyGen](../tools/heygen.md) — avatar-video product centered on reusable synthetic presenters for communication and marketing workflows *(as of 2026-04-22)*

### UI generation

- [Stitch](../tools/stitch.md) — Google's design-to-interface generation surface, bridging prompts, references, and interface artifacts *(as of 2026-04-22)*

### Visual design & prototyping

- [Claude Design](../tools/claude-design.md) — Anthropic; collaborative prototype, slide, and marketing-asset tool with creative-suite connectors and `/design-sync` to Claude Code; since 2026-09-16 also works inside Claude conversations beside the new Claude Docs and Slides (beta) *(as of 2026-09-16)*
- [Genspark Slides](../tools/genspark-slides.md) — AI presentation generation inside Genspark's broader agent/content surface; current training evidence still cautions that polished enterprise decks need deep skill/tooling support and human review, not a thin prompt *(as of 2026-06-29)*
- **Adobe Firefly AI Assistant** — Adobe assistant that executes multi-step creative tasks across Premiere, Photoshop, InDesign, and other Adobe apps, with expansion planned to ChatGPT, Claude, Gemini, Copilot, and Slack. Current evidence is newsletter coverage only *(as of 2026-06-19)*
- **Figma Agent** — Figma; a native, in-canvas design agent (released 2026-05-20) that edits directly inside the canvas, built on a mix of Gemini Flash, Claude Sonnet, and Figma's own fine-tuned models; solves the blank-page problem for first-pass exploration but detail fidelity is weak per Every's hands-on review *(as of 2026-05-20)*
- [Impeccable](../tools/impeccable.md) — open-source design-agent skill system; encodes domain vocabulary, exact levels of control, and reusable evaluation language so agents make design decisions more reliably rather than one-shot prompting *(as of 2026-07-02)*

### AI music generation

- **Suno** — category anchor for AI-generated music with reported subscriber and revenue milestones; Speech (beta, open to all users) generates spoken voice and original background music together as one track; no dedicated tool page yet *(as of 2026-10-20)*
- **Udio** — category anchor alongside Suno; AI-generated music *(as of 2026-05-01)*
- **ElevenMusic** — ElevenLabs' new entrant to AI music generation *(as of 2026-05-01)*

## Recent changes

- [2026-10-20] Suno opened Speech (beta), billed as the first audio model that generates voice and music together as one track.
- [2026-09-25] Runway GWM Worlds 2 (research preview) turns its audio-video model into a real-time interactive world at 720p/24fps via WorldPrompt, autoregressive post-training and step distillation (about 50 → 4 denoising steps); Runway also showed an "interface world model" that renders software UIs as pixels.
- [2026-09-16] Claude Design moved into Claude conversations as Anthropic merged chat and Cowork, launching Claude Docs and Claude Slides beside it (all beta on paid plans).
- [2026-09-16] QuiverAI released [Arrow 2](../models/arrow-2.md) and Arrow 2 Telos, vector-graphics models that output editable SVGs, with a rebuilt app and a developer API platform.
- [2026-09-01] Fal's H3 Max Live crosses faster-than-realtime video generation (35x inference speedup over MiniMax H3's official endpoint), enabling a continuous, audience-steerable live-video product; Fal also launched Reference-to-Video for MiniMax H3 Max at up to real-time factor 1.
- [2026-07-24] Black Forest Labs launched FLUX 3: unified image/video/audio/action-prediction model, positioned against Seedance 2.0/Gemini Omni/Grok Imagine; companion FLUX3-mimic release extends it to robot control.
- [2026-07-08] Meta launched Muse Image into Meta AI, Instagram Stories, and WhatsApp and previewed Muse Video; AINews describes an agentic generation loop with planning, tool use, code execution, and self-refinement.
- [2026-06-29] Every's PowerPoint analysis adds a caution for slide agents: polished enterprise decks require supporting skills, scripts, references, and review loops.
- [2026-06-24] OpenArt Director and Krea 2 Raw/Turbo signal creative workflows splitting between conversational editing products and open fine-tuning ecosystems.
- [2026-06-19] Palmier and Adobe Firefly Assistant show creative tooling moving toward agentic desktop workflows: video editing and multi-app creative tasks executed from natural-language instructions.

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
- [Google I/O: Agents, Agents, Agents (Every mini-review of Figma's design agent)](../sources/newsletters/google-io-agents-agents-agents.md)
- [AINews — New AI Infra unicorns: Exa, Modal, TurboPuffer (Runway Aleph 2.0 recap)](../sources/newsletters/ainews-new-ai-infra-unicorns-2026-05-22.md)
- [AINews — Black Forest Labs FLUX 3](../sources/newsletters/bfl-flux-3-2026-07-24.md)
- [AINews — Fal's H3 Max Live breaks the infinite videogen barrier](../sources/newsletters/ainews-fal-h3-max-live-2026-09-01.md)
- [Latent Space — Runway's WorldPrompt and the engineering of real-time worlds](../sources/newsletters/latent-space-runway-worldprompt-2026-09-25.md)
- [Suno — Introducing Speech (beta)](../sources/articles/suno-speech-beta-2026-10.md)
- [Claude Cowork and chat are now one Claude](../sources/articles/claude-cowork-is-now-claude-2026-09-16.md)
- [QuiverAI — Introducing Arrow 2 and Arrow 2 Telos](../sources/articles/quiverai-arrow-2-launch-2026-09-16.md)
- [QuiverAI on X — Introducing Arrow 2](../sources/tweets/quiverai-arrow-2-announcement-2026-09-16.md)
