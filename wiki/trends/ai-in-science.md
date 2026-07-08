---
title: AI in Science
type: trend
domains: [science]
tags: []
as_of: 2026-07-06
sources: [noetik-cancer-trials, gpt-rosalind-launch, self-driving-lab-radical-ai, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07]
---

# AI in Science

AI is increasingly moving from generic scientific assistance toward domain-specific scientific reasoning systems. The strongest current signal in this wiki is biology and drug discovery: models are being positioned not just as literature copilots, but as systems that infer treatment response, model tumor environments, or support translational medicine workflows.

## Current status (as of 2026-04-21)

- Noetik is presented as using large multimodal tumor datasets and transformer models to predict treatment response and improve cancer-trial selection
- The company reportedly signed a $50M GSK deal tied to this stack
- OpenAI launched GPT-Rosalind as a frontier reasoning model for biology, drug discovery, and translational medicine
- Translational medicine here means moving from lab and data insight toward practical clinical use, such as deciding which therapies, biomarkers, or trial designs are most likely to work in patients
- The pattern is shifting from "AI helps researchers" to "specialized models target a scientific bottleneck directly"
- Anthropic's Claude Science signal reinforces a platform-first strategy in science AI: build tools for analysis, visualization, traceability, reviewer-agent verification, scientific databases, and lab/HPC compute, then dogfood them on real preclinical and partner research workflows.
- The hard part is not only hypothesis generation. Biological feedback is slow and expensive, so evaluation and verification workflows become the bottleneck the platform must solve.

## Self-driving labs

The self-driving lab (SDL) is an architecture that closes the loop between AI hypothesis generation and physical experimentation — removing the human from the serial bottleneck of: hypothesize → lab → wait → analyze → repeat.

**How it works (Radical AI):**
1. An "AI scientist" (combining scientific knowledge, computational techniques, and human intuition encoded at setup) generates and prioritizes hypotheses
2. Automated robotics synthesize and characterize materials from those hypotheses in parallel
3. Results feed back into the AI scientist, which updates its priors and generates the next round
4. Research campaigns run simultaneously rather than serially

**Key results (Radical AI, as of 2026-06-17):**
- 1,200 alloys synthesized and characterized in 6 months — ~10× the pace of DARPA/GE MACH (which targeted 500 alloys/year with human researchers)
- 300 novel materials proposed by the AI scientist; 10 found to have novel state-of-the-art properties now in further development
- AI scientist expanded into elemental families no previous published research had explored
- Scales toward ~100 new alloys tested and characterized per day

**Infrastructure as bottleneck (Anthropic science blog, June 9 2026):**
Anthropic argues AI has advanced faster in coding than biology not because of intelligence limits, but because biological databases and scientific tooling were not built for agent use. The bottleneck is infrastructure and interface design, not raw model capability — an argument that parallels why self-driving labs invest heavily in robotic integration and data pipelines, not just model selection.

**Open-source tooling:**
- TorchSim — PyTorch-based molecular dynamics simulation framework (spun out to a non-profit)
- MATRIX / MATRIX-PT — open benchmark for autonomous SDL evaluation + model trained on that benchmark; improving reasoning for materials also improved biological systems reasoning (unexpected transfer result)

## Recent changes

- [2026-07-06] Claude Science public beta confirms a science-workflow platform layer: reproducible artifacts, persistent kernels, 60+ scientific databases, scientific connectors, and local/HPC compute integration.
- [2026-07-01] Official Claude Science announcement adds reviewer agents, BioNeMo/Boltz/OpenFold-style integrations, and Manifold Bio / Allen Institute / UCSF case studies.
- [2026-07-05] Claude Science and Anthropic's internal drug programs reframed science agents as dogfooded workflow platforms, not only model demos.
- [2026-06-17] Added self-driving labs section: Radical AI achieving ~10× DARPA/GE MACH pace in alloys; infrastructure-as-bottleneck framing from Anthropic science blog
- [2026-04-21] Added biology and drug-discovery productization signals: Noetik and GPT-Rosalind
- [2026-04-10] Page seeded from Superhuman AI newsletter overview of AI-driven scientific breakthroughs

## Sources

- [The Self-Driving Lab — Joseph Krause, Radical AI](../sources/newsletters/self-driving-lab-radical-ai.md)
- [Latent Space — Noetik and cancer-trial failure](../sources/newsletters/noetik-cancer-trials.md)
- [GPT-Rosalind launch](../sources/tweets/gpt-rosalind-launch.md)
- [Claude Science beta](../sources/articles/claude-science-beta-2026-07-06.md)
- [Claude Science AI workbench announcement](../sources/articles/claude-science-workbench-2026-07.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
