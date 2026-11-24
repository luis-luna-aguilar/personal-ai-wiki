---
title: AI in Biology
type: trend
domains: [science]
tags: []
as_of: 2026-09-24
sources: [noetik-cancer-trials, gpt-rosalind-launch, esmfold2-protein-world-model-2026-05, xaira-x-cell-causal-virtual-cell-2026-07-21, chai-discovery-bioai-phase-shift-2026-08-11, anthropic-claude-art-enzyme-system-2026-09, ainews-claude-art-amodei-2026-09-24, ainews-art-critique-2026-09-25, radical-numerics-genomic-lms-biosecurity-2026-09-23]
---

# AI in Biology

Split out from [AI in Science](ai-in-science.md) because biology and drug discovery are the densest cluster in the science trend. Models are positioned not just as literature copilots but as systems that infer treatment response, model proteins and cells, design molecules, read and write DNA, and now originate discovery candidates for human labs to test. Cross-domain science platforms (Claude Science), self-driving labs, and Google's ERA stay on AI in Science.

## Current status (as of 2026-09-24)

- Noetik is presented as using large multimodal tumor datasets and transformer models to predict treatment response and improve cancer-trial selection
- The company reportedly signed a $50M GSK deal tied to this stack
- OpenAI launched GPT-Rosalind as a frontier reasoning model for biology, drug discovery, and translational medicine
- Translational medicine here means moving from lab and data insight toward practical clinical use, such as deciding which therapies, biomarkers, or trial designs are most likely to work in patients
- ESMFold2 adds a protein-world-model signal: general transformer scaling and diverse protein data are being applied to structure prediction, protein interactions, antibody tasks, and design/discovery workflows.
- Chai Discovery ($4B valuation) reports four major pharma tools deals since January — Lilly, Novartis, argenx, and an expanded Eli Lilly program — as structural models give way to binding models that support real molecule design, not just prediction
- Agent swarms produced the first genome-mining discovery claim in this wiki: Anthropic's ART phage system, found by ~950 Claude agents and confirmed only as far as "transcribed into short RNAs" (see below).
- Genomic language models raise the biosecurity stakes of the same capability gains (see below).

## Protein world models

ESMFold2 is a useful biology counterpoint to purely lab-automation stories. The source frames it as an open engine trained on diverse protein data, with reported strengths on protein interactions and antibodies, plus inference-time scaling across cancer and immunology targets.

The practical importance is the same as other science-agent infrastructure: better models are only useful if they plug into data, verification, and downstream discovery loops. ESMFold2's atlas and open licensing make it a durable signal to watch, but the wiki should distinguish source-reported performance from broad clinical or wet-lab validation.

## Agent swarms as discoverers (Anthropic ART)

Anthropic's new life-sciences lab (Bay Area, BSL-1/2 only, all bench work by humans) gave Claude one high-level prompt: search a DNA database for interesting reverse transcriptases (RTs, enzymes that copy RNA into DNA). About 950 agents ran for 21 hours on 210M tokens, gathered 200,000+ RTs, nominated 3,500 candidate systems and wrote reports on the 20 strongest. One agent noticed that a known RT in jumbo bacteriophages sits beside an accessory gene and a long array of evenly spaced DNA repeats, a CRISPR-like layout nobody had described. Anthropic calls the system ART (array-associated reverse transcriptases).

- **Validated so far:** human-run experiments (expression in E. coli plus RNA-seq) show the array is transcribed into distinct short RNAs. Function is unknown; there is no evidence yet of programmable editing.
- **Reception:** Amodei called it PhD-worthy but of unclear significance; community critics said it is not AlphaFold- or CRISPR-scale; a Stanford team independently described a distinct RT system with a non-coding array.
- **Workflow lesson:** with hundreds to thousands of reports per campaign, the lab now studies which hypotheses scientists choose to test and feeds that "taste" back into Claude's instructions. Work runs in Claude Science and Claude Code, sometimes with a harness that coordinates many parallel sessions.

## Genomic language models and biosecurity

Genomic language models read and write DNA directly. Evo-family models were used by an Arc/Stanford team to generate whole bacteriophage genomes that were synthesized into working viruses. Radical Numerics (Eric Nguyen, Evo / Evo 2) reports in-context optimization: shown RNA aptamers ranked from low to high score, the model continues the trajectory toward better sequences, which Nguyen frames as chain-of-thought in DNA. His view is that biosecurity defense is currently losing the arms race and must keep pace by pushing the frontier, not by holding it back.

## Virtual cell models

Most RNA-expression models (the dominant "Virtual Cell" approach, built on datasets like the Chan Zuckerberg Institute's 168M-cell CELLxGENE) describe correlations between cell types and states, but can't reliably predict what happens if you change a gene's expression — because gene expression changes are highly correlated and rarely tell you what causes what.

**Xaira's causal counterpoint (as of 2026-07-21):** Xaira Therapeutics' earlier RNA-expression model plateaued around 1.5B parameters — a sign the ceiling was the information in the training data, not model size or compute. Their fix, X-Atlas, is built from CRISPR experiments that perturb one gene at a time, producing data rich enough to establish actual causal (not merely correlational) gene-expression relationships. The resulting model, X-Cell, resumed scaling with added parameters and compute once trained on this richer data — Xaira reports it beats the linear baseline that had outperformed prior virtual-cell models.

## AI-native drug design (Chai Discovery)

Most AI-for-pharma startups have historically ended up building their own drug pipelines rather than selling tools, because convincing a pharma partner to license a tool required proof only a real pipeline could provide. Chai Discovery's cofounders trace a shift starting around January 2026's JPM Healthcare conference: the underlying models crossed a threshold from structural prediction (a molecule's shape) to binding prediction (how strongly two molecules bind), which unlocks actual molecule design rather than analysis. That reframes drug discovery closer to an engineering problem — getting good candidate molecules "right out of the gate" cuts the iteration time that otherwise requires years of lab trial and error, such as engineering an antibody to trigger a precise molecular cascade.

Chai's product bet is UX-driven: a CAD-like molecule editor ("Photoshop for molecules") built from tight partner feedback loops rather than a chatbot interface. Since June 2026, that approach has produced three further major deals on top of the January wave — Lilly, Novartis, argenx, and an expanded existing Eli Lilly program — with Chai now valued at $4B, two years after founding.

## Recent changes

- [2026-10-21] Page split out from [AI in Science](ai-in-science.md): protein world models, virtual cells, AI-native drug design, ART, and genomic language models moved here.
- [2026-09-24] Anthropic's life-sciences lab reported ART, a CRISPR-like phage reverse-transcriptase system found by ~950 Claude agents (21 hours, 210M tokens); array confirmed transcribed into short RNAs, function unknown; critics and Amodei both call its significance unclear.
- [2026-09-23] Added genomic language models and biosecurity: Radical Numerics reports in-context DNA optimization and argues defense is losing the arms race.
- [2026-08-11] Added Chai Discovery as an AI-native drug-design signal: structural-to-binding-model shift, CAD-style molecule editor, four pharma deals since January (Lilly, Novartis, argenx, expanded Eli Lilly program), $4B valuation
- [2026-07-21] Added Xaira Therapeutics' X-Cell/X-Atlas as a causal counterpoint to correlational RNA-expression virtual-cell models

## Sources

- [Latent Space — Noetik and cancer-trial failure](../sources/newsletters/noetik-cancer-trials.md)
- [GPT-Rosalind launch](../sources/tweets/gpt-rosalind-launch.md)
- [ESMFold2 - The bitter lesson is coming for protein](../sources/newsletters/esmfold2-protein-world-model-2026-05.md)
- [Latent Space — Causal Models Need Causal Data (Xaira X-Cell)](../sources/newsletters/xaira-x-cell-causal-virtual-cell-2026-07-21.md)
- [Latent Space — The BioAI Phase Shift (Chai Discovery)](../sources/newsletters/chai-discovery-bioai-phase-shift-2026-08-11.md)
- [Anthropic — Claude discovers a novel enzyme system](../sources/articles/anthropic-claude-art-enzyme-system-2026-09.md)
- [AINews — Claude's ART phage system and Amodei's framing](../sources/newsletters/ainews-claude-art-amodei-2026-09-24.md)
- [AINews — Community critique of the ART result](../sources/newsletters/ainews-art-critique-2026-09-25.md)
- [Latent Space — Eric Nguyen: bio-security is an AI arms race](../sources/newsletters/radical-numerics-genomic-lms-biosecurity-2026-09-23.md)
