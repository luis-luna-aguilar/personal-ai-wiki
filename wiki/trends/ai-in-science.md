---
title: AI in Science
type: trend
domains: [science]
tags: []
as_of: 2026-08-06
sources: [noetik-cancer-trials, gpt-rosalind-launch, self-driving-lab-radical-ai, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07, esmfold2-protein-world-model-2026-05, openai-erdos-unit-distance-2026-05, lila-sciences-automated-wet-lab-2026-07-16, xaira-x-cell-causal-virtual-cell-2026-07-21, anthropic-riemann-hypothesis-2026-08-11, gdm-reshuffle-discovery-loop-2026-08-06]
---

# AI in Science

AI is increasingly moving from generic scientific assistance toward domain-specific scientific reasoning systems. The strongest current signal in this wiki is biology and drug discovery: models are being positioned not just as literature copilots, but as systems that infer treatment response, model tumor environments, or support translational medicine workflows.

## Current status (as of 2026-08-06)

- Noetik is presented as using large multimodal tumor datasets and transformer models to predict treatment response and improve cancer-trial selection
- The company reportedly signed a $50M GSK deal tied to this stack
- OpenAI launched GPT-Rosalind as a frontier reasoning model for biology, drug discovery, and translational medicine
- Translational medicine here means moving from lab and data insight toward practical clinical use, such as deciding which therapies, biomarkers, or trial designs are most likely to work in patients
- The pattern is shifting from "AI helps researchers" to "specialized models target a scientific bottleneck directly"
- Anthropic's Claude Science signal reinforces a platform-first strategy in science AI: build tools for analysis, visualization, traceability, reviewer-agent verification, scientific databases, and lab/HPC compute, then dogfood them on real preclinical and partner research workflows.
- The hard part is not only hypothesis generation. Biological feedback is slow and expensive, so evaluation and verification workflows become the bottleneck the platform must solve.
- ESMFold2 adds a protein-world-model signal: general transformer scaling and diverse protein data are being applied to structure prediction, protein interactions, antibody tasks, and design/discovery workflows.
- The domain-specific-reasoning pattern is not limited to biology: pure-mathematics results (OpenAI's Erdős disproof, Anthropic's Riemann Hypothesis bound) now form their own cluster — see [AI in Mathematics](ai-in-mathematics.md).
- A wave of senior technical leadership left a model lab for AI-driven science ventures: Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, and Quoc Le departed Google DeepMind to found Discovery Loop, a Public Benefit Corporation aimed at automating machine learning, science, and engineering research ("autoresearch"), backed by Radical Ventures, Khosla Ventures, Lightspeed, Kleiner Perkins, Doerr Capital — and Google itself. The move accompanied a DeepMind leadership reshuffle: after 16 years as CEO, Demis Hassabis became Chair of GDM and Chief Scientist of Alphabet, stepping back from day-to-day operations toward long-term strategy, AGI, and Isomorphic Labs, while CTO Koray Kavukcuoglu took over as SVP running Gemini, frontier research, and product.

## Protein world models

ESMFold2 is a useful biology counterpoint to purely lab-automation stories. The source frames it as an open engine trained on diverse protein data, with reported strengths on protein interactions and antibodies, plus inference-time scaling across cancer and immunology targets.

The practical importance is the same as other science-agent infrastructure: better models are only useful if they plug into data, verification, and downstream discovery loops. ESMFold2's atlas and open licensing make it a durable signal to watch, but the wiki should distinguish source-reported performance from broad clinical or wet-lab validation.

## Virtual cell models

Most RNA-expression models (the dominant "Virtual Cell" approach, built on datasets like the Chan Zuckerberg Institute's 168M-cell CELLxGENE) describe correlations between cell types and states, but can't reliably predict what happens if you change a gene's expression — because gene expression changes are highly correlated and rarely tell you what causes what.

**Xaira's causal counterpoint (as of 2026-07-21):** Xaira Therapeutics' earlier RNA-expression model plateaued around 1.5B parameters — a sign the ceiling was the information in the training data, not model size or compute. Their fix, X-Atlas, is built from CRISPR experiments that perturb one gene at a time, producing data rich enough to establish actual causal (not merely correlational) gene-expression relationships. The resulting model, X-Cell, resumed scaling with added parameters and compute once trained on this richer data — Xaira reports it beats the linear baseline that had outperformed prior virtual-cell models.

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

**A second automated lab (Lila Sciences, as of 2026-07-16):** Flagship Pioneering spinout Lila Sciences runs a fully automated, 24/7 robotic wet lab spanning biology, chemistry, drug discovery, and materials science simultaneously — the same lab, same AI, across domains Radical AI treats separately. Lila has generated over 10 trillion experimentally-validated scientific reasoning tokens so far, and rebuilt a gas-sorption measurement to run roughly 2,500x faster by treating lab instruments as nodes on a graph rather than serial steps. Lila's stated goal is a general scientific reasoner, not an automation tool: they report breadth (small-molecule chemistry priors transferring to materials science) outperforming domain-specific models sample-for-sample.

## Recent changes

- [2026-09-07] Pure-mathematics signals (OpenAI's Erdős disproof, Anthropic's Riemann Hypothesis bound) split out into a new dedicated page, [AI in Mathematics](ai-in-mathematics.md), at the user's request.
- [2026-08-11] Anthropic reported an unreleased research Claude variant improved a Riemann Hypothesis-related bound (proportion of zeta zeros proven on the critical line: 41.6% → 67.2%), via ~31M output tokens of retries/exploration — a second pure-math signal alongside OpenAI's Erdős disproof; not yet independently verified.
- [2026-08-06] Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, and Quoc Le left Google DeepMind to found autoresearch startup Discovery Loop; accompanied by a DeepMind leadership reshuffle (Hassabis to Chair of GDM/Chief Scientist of Alphabet, Kavukcuoglu to SVP of DeepMind)
- [2026-07-21] Added Xaira Therapeutics' X-Cell/X-Atlas as a causal counterpoint to correlational RNA-expression virtual-cell models
- [2026-07-16] Added Lila Sciences as a second self-driving-lab signal: cross-domain automated wet lab, 10T+ validated scientific reasoning tokens, ~2,500x gas-sorption speedup
- [2026-07-06] Claude Science public beta confirms a science-workflow platform layer: reproducible artifacts, persistent kernels, 60+ scientific databases, scientific connectors, and local/HPC compute integration.
- [2026-07-05] Claude Science and Anthropic's internal drug programs reframed science agents as dogfooded workflow platforms, not only model demos.
- [2026-07-01] Official Claude Science announcement adds reviewer agents, BioNeMo/Boltz/OpenFold-style integrations, and Manifold Bio / Allen Institute / UCSF case studies.
- [2026-06-17] Added self-driving labs section: Radical AI achieving ~10× DARPA/GE MACH pace in alloys; infrastructure-as-bottleneck framing from Anthropic science blog
- [2026-05-27] Added ESMFold2 as a protein-world-model signal: open protein prediction/design engine, antibody interaction strength, and atlas-scale structure predictions.

## Sources

- [The Self-Driving Lab — Joseph Krause, Radical AI](../sources/newsletters/self-driving-lab-radical-ai.md)
- [Latent Space — Noetik and cancer-trial failure](../sources/newsletters/noetik-cancer-trials.md)
- [GPT-Rosalind launch](../sources/tweets/gpt-rosalind-launch.md)
- [Claude Science beta](../sources/articles/claude-science-beta-2026-07-06.md)
- [Claude Science AI workbench announcement](../sources/articles/claude-science-workbench-2026-07.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
- [ESMFold2 - The bitter lesson is coming for protein](../sources/newsletters/esmfold2-protein-world-model-2026-05.md)
- [OpenAI model disproves the Erdős planar unit-distance conjecture](../sources/articles/openai-erdos-unit-distance-2026-05.md)
- [Latent Space — The Lab of the Future Should Feel Like a Data Center (Lila Sciences)](../sources/newsletters/lila-sciences-automated-wet-lab-2026-07-16.md)
- [Latent Space — Causal Models Need Causal Data (Xaira X-Cell)](../sources/newsletters/xaira-x-cell-causal-virtual-cell-2026-07-21.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- [AINews — Jeff, Sanjay, Oriol, and Quoc depart DeepMind; Discovery Loop founded](../sources/newsletters/gdm-reshuffle-discovery-loop-2026-08-06.md)
