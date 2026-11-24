---
title: AI in Science
type: trend
domains: [science]
tags: []
as_of: 2026-09-22
sources: [self-driving-lab-radical-ai, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07, openai-erdos-unit-distance-2026-05, lila-sciences-automated-wet-lab-2026-07-16, anthropic-riemann-hypothesis-2026-08-11, gdm-reshuffle-discovery-loop-2026-08-06, john-platt-google-era-2026-09-22, model-hardware-standard-research-preview-2026-08-27]
---

# AI in Science

AI is increasingly moving from generic scientific assistance toward domain-specific scientific reasoning systems, workflow platforms, and closed experimental loops. This page is the hub for cross-domain science AI: science-agent platforms, self-driving labs, and general patterns such as optimizing any scoreable problem. Domain clusters with their own momentum have their own pages: [AI in Biology](ai-in-biology.md) and [AI in Mathematics](ai-in-mathematics.md).

## Current status (as of 2026-09-22)

- The pattern is shifting from "AI helps researchers" to "specialized models target a scientific bottleneck directly"
- Anthropic's Claude Science signal reinforces a platform-first strategy in science AI: build tools for analysis, visualization, traceability, reviewer-agent verification, scientific databases, and lab/HPC compute, then dogfood them on real preclinical and partner research workflows.
- The hard part is not only hypothesis generation. Biological feedback is slow and expensive, so evaluation and verification workflows become the bottleneck the platform must solve.
- Biology and drug discovery remain the densest cluster (tumor-response models, GPT-Rosalind, protein world models, virtual cells, AI-native drug design, Anthropic's agent-found ART system, genomic language models) — see [AI in Biology](ai-in-biology.md).
- The domain-specific-reasoning pattern is not limited to biology: pure-mathematics results (OpenAI's Erdős disproof, Anthropic's Riemann Hypothesis bound) now form their own cluster — see [AI in Mathematics](ai-in-mathematics.md).
- "Optimize anything scoreable" is emerging as a reusable science pattern (Google ERA).
- A wave of senior technical leadership left a model lab for AI-driven science ventures: Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, and Quoc Le departed Google DeepMind to found Discovery Loop, a Public Benefit Corporation automating ML, science, and engineering research ("autoresearch"), backed by Radical Ventures, Khosla Ventures, Lightspeed, Kleiner Perkins, Doerr Capital, and Google itself. A DeepMind leadership reshuffle accompanied the move: after 16 years as CEO, Demis Hassabis became Chair of GDM and Chief Scientist of Alphabet, while CTO Koray Kavukcuoglu took over as SVP running Gemini, frontier research, and product.

## Biology and drug discovery

Biology material (protein world models, virtual cell models, AI-native drug design, Anthropic's ART discovery, and genomic language models with their biosecurity stakes) now lives on [AI in Biology](ai-in-biology.md). This page keeps the cross-domain platforms and loops those results run on.

## Optimizing anything scoreable (Google ERA)

Google's Empirical Research Assistance (ERA), described by John Platt, reduces any science problem with a written score function to a search: the LLM keeps a tree of past experiment notebooks and mutates the promising ones, a close cousin of Monte Carlo tree search. It went from not working on Gemini 2.0 to working well on 2.5, has produced at least ten papers, and found the missing model for the reflected-sunlight half of contrail warming, a counterfactual problem that had stalled Platt's team for two years. The hard part moves to writing the score. ERA yields predictive models; checking that they are descriptive stays with the scientist. Platt: "It's a power tool. It can slice your fingers off."

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

**A shared instrument standard (Anthropic, as of 2026-08-27):** much of a self-driving lab's cost is bespoke instrument integration. Anthropic's [Model Hardware Standard](../concepts/model-hardware-standard.md) research preview, developed with HHMI Janelia, gives microscopes, liquid handlers, and robot arms a common driver so one agent can run several in parallel; Tecan, QIAGEN, Danaher, MBF Bioscience, and Automata are building support.

## Recent changes

- [2026-10-21] Biology material (protein world models, virtual cells, AI-native drug design, ART, genomic language models) split out into a new dedicated page, [AI in Biology](ai-in-biology.md), at the user's request.
- [2026-09-22] Added Google's ERA (Empirical Research Assistance): tree search over Gemini-mutated notebooks for any problem with a score function; 10+ papers, contrail counterfactual solved.
- [2026-09-07] Pure-mathematics signals (OpenAI's Erdős disproof, Anthropic's Riemann Hypothesis bound) split out into a new dedicated page, [AI in Mathematics](ai-in-mathematics.md), at the user's request.
- [2026-08-27] Anthropic's [Model Hardware Standard](../concepts/model-hardware-standard.md) research preview (with HHMI Janelia): a common driver so agents can discover, run, and coordinate lab instruments; Tecan, QIAGEN, Danaher, MBF Bioscience, and Automata building support.
- [2026-08-11] Anthropic reported an unreleased research Claude variant improved a Riemann Hypothesis-related bound (proportion of zeta zeros proven on the critical line: 41.6% → 67.2%), via ~31M output tokens of retries/exploration — a second pure-math signal alongside OpenAI's Erdős disproof; not yet independently verified.
- [2026-08-06] Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, and Quoc Le left Google DeepMind to found autoresearch startup Discovery Loop; accompanied by a DeepMind leadership reshuffle (Hassabis to Chair of GDM/Chief Scientist of Alphabet, Kavukcuoglu to SVP of DeepMind)
- [2026-07-16] Added Lila Sciences as a second self-driving-lab signal: cross-domain automated wet lab, 10T+ validated scientific reasoning tokens, ~2,500x gas-sorption speedup
- [2026-07-06] Claude Science public beta confirms a science-workflow platform layer: reproducible artifacts, persistent kernels, 60+ scientific databases, scientific connectors, and local/HPC compute integration.

## Sources

- [The Self-Driving Lab — Joseph Krause, Radical AI](../sources/newsletters/self-driving-lab-radical-ai.md)
- [Claude Science beta](../sources/articles/claude-science-beta-2026-07-06.md)
- [Claude Science AI workbench announcement](../sources/articles/claude-science-workbench-2026-07.md)
- [Every - A Tale of Two Models](../sources/newsletters/every-tale-of-two-models-2026-07-05.md)
- [OpenAI model disproves the Erdős planar unit-distance conjecture](../sources/articles/openai-erdos-unit-distance-2026-05.md)
- [Latent Space — The Lab of the Future Should Feel Like a Data Center (Lila Sciences)](../sources/newsletters/lila-sciences-automated-wet-lab-2026-07-16.md)
- [AINews — Anthropic's Riemann Hypothesis bound improvement](../sources/newsletters/anthropic-riemann-hypothesis-2026-08-11.md)
- [AINews — Jeff, Sanjay, Oriol, and Quoc depart DeepMind; Discovery Loop founded](../sources/newsletters/gdm-reshuffle-discovery-loop-2026-08-06.md)
- [Latent Space — John Platt on Google's ERA](../sources/newsletters/john-platt-google-era-2026-09-22.md)
- [Anthropic — Previewing the Model Hardware Standard](../sources/articles/model-hardware-standard-research-preview-2026-08-27.md)
