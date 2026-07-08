---
title: State of Science
type: state-of
domains: [science]
tags: []
as_of: 2026-07-06
sources: [curiosity-driven-imagination, noetik-cancer-trials, gpt-rosalind-launch, futurehouse-homepage, legacy-ai-tools-roadmap-xlsx, openai-gpt-5-5-launch, ai-co-mathematician-2026-05-13, genesis-ai-gene-26-5-2026-05-09, self-driving-lab-radical-ai, axiom-math-june-2026, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07]
---

# State of Science

Current state of AI applied to scientific research — data analysis at scale, experiment automation, and accelerating discovery across domains.

## Subcategories

### Science agent platforms

Tools built to run or supervise literature-driven, hypothesis-oriented, or discovery-oriented scientific workflows.

- [FutureHouse](../tools/futurehouse.md) — science-agent platform aimed at research and discovery workflows rather than generic assistant use *(as of 2026-04-22)*
- [Claude Science](../tools/claude-science.md) — Anthropic beta science workbench for analysis, database search, reproducible artifacts, reviewer agents, scientific visualizations, 60+ databases, BioNeMo/Boltz/OpenFold-style integrations, and local/HPC compute; case studies now include Manifold Bio, Allen Institute, and UCSF workflows *(as of 2026-07-01)*

### Robotics

AI models and hardware designed for physical manipulation — robots that can handle unstructured real-world tasks rather than scripted factory paths.

- **Genesis AI GENE-26.5** — French startup; full-stack model that can pilot robots from multiple manufacturers; paired with a 5-finger human-like robotic hand; closes the "embodiment gap" by enabling collection of higher-fidelity physical training data; demo: cracking eggs, Rubik's Cube, piano *(as of 2026-05-09)*

### Self-driving labs

Closed-loop systems where an AI scientist generates hypotheses and automated robotic labs execute and characterize experiments — removing the human from the serial experimental loop.

- **Radical AI** — materials science; AI scientist + robotic synthesis + active learning loop; 1,200 alloys characterized in 6 months (~10× DARPA/GE MACH pace); 300 novel materials tested, 10 with SOTA properties; TorchSim and MATRIX open-sourced *(as of 2026-06-17)*

### Frontier models used in science

General-purpose frontier models whose published evaluation or reported use now makes them relevant to practical scientific-research work, even if they are not science-only products.

- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; BixBench 80.5%, meaningful GeneBench gains over GPT-5.4, and launch examples spanning bioinformatics analysis, theorem proving, and early research assistance *(as of 2026-04-23)*
- **AI Co-Mathematician** — Google DeepMind; asynchronous, stateful research workbench for mathematicians; supports ideation, literature discovery, computational analysis, theorem verification, and formal proof outputs; 48% on FrontierMath Tier 4 (research-level math above olympiad-style, authored by 64 mathematicians); paper: arxiv.org/abs/2605.06651 *(as of 2026-05-13)*

### Formal verification and theorem proving

AI systems that generate or verify formal mathematical proofs, providing machine-checkable correctness signals for RL training.

- [Axiom Math](../tools/axiom-math.md) — 7-month-old startup; 12/12 Putnam 2025; 99% ProofGen (Verina) vs o3 at 4.9%; AXLE open-source interactive Lean toolkit; $200M Series A / $1.6B valuation; thesis: verifiable proofs = scalable RL reward signal *(as of 2026-06-03)*

## Recent changes

- [2026-07-06] Claude Science entered the science-agent-platform set; Anthropic confirms public beta with reproducible artifacts, persistent kernels, 60+ scientific databases, and compute/tool integrations.
- [2026-07-01] Claude Science official announcement adds reviewer agents, artifact rendering, scientific model integrations, and Manifold Bio / Allen Institute / UCSF case studies.
- [2026-07-05] Anthropic's internal drug programs make evaluation/verification feedback loops the Claude Science strategy point to watch.
- [2026-06-03] Added formal verification subcategory; Axiom Math: 12/12 Putnam 2025, 99% ProofGen vs o3's 4.9%; AXLE open-source Lean toolkit; $200M / $1.6B; thesis: formal verification = scalable RL reward signal
- [2026-06-17] Added `Self-driving labs` subcategory; Radical AI: ~10× DARPA/GE MACH pace; AI scientist proposed 300 new materials, 10 with novel state-of-the-art properties; TorchSim and MATRIX open-sourced
- [2026-05-09] Added `Robotics` subcategory; Genesis AI GENE-26.5 (full-stack multi-manufacturer robot model + 5-finger hand) goes viral; "embodiment gap" framing introduced
- [2026-05-13] Added AI Co-Mathematician (Google DeepMind): 48% FrontierMath Tier 4; asynchronous stateful workbench for mathematicians; physics-intern (related) boosted Gemini 3.1 Pro from 17.7% → 31.4% on CritPt via specialized subagent decomposition
- [2026-04-23] Added `Frontier models used in science` with [GPT-5.5](../models/gpt-5-5.md); OpenAI is now making explicit science-performance claims rather than only general-reasoning claims
- [2026-04-22] Added `Science agent platforms` with [FutureHouse](../tools/futurehouse.md) as the first productized science-agent signal from the legacy workbook exception
- [2026-04-21] Biology and drug discovery emerge as the strongest current productization signal: Noetik's tumor-response models and OpenAI's GPT-Rosalind
