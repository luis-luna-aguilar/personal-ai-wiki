---
type: proposal
source: raw/newsletters/2026-07-16-the-lab-of-the-future-should-feel-like-a-data-ce.md
status: pending
created: 2026-09-06
---

# Proposal: Lila Sciences' automated wet lab and Xaira's causal virtual-cell model

## Summary

### The source
Two Latent Space podcast-summary newsletters extend the wiki's AI-in-science thread. The first (July 16) covers Lila Sciences, a Flagship Pioneering spinout whose CTO Andy Beam and CSO Rafa Gómez-Bombarelli describe a fully automated, 24/7 robotic wet lab running biology, chemistry, drug discovery, and materials science simultaneously — the pitch is "the lab of the future should feel like a data center." They've generated over 10 trillion experimentally-validated scientific reasoning tokens so far, and Gómez-Bombarelli's team rebuilt a gas-sorption measurement to run roughly 2,500x faster by treating instruments as nodes on a graph rather than serial lab steps. The second (July 21) covers Xaira Therapeutics' X-Cell, presented by newly-promoted Chief Discovery Officer Ci Chu and Chief AI Scientist Bo Wang. Their earlier RNA-expression model (built on Bo Wang's own scGPT lineage) plateaued around 1.5B parameters — a sign the bottleneck was the *information* in the training data, not model size or compute, since existing databases like CELLxGENE only capture correlations between cell states, not what causes what. Xaira's answer was X-Atlas: a dataset built from CRISPR experiments that perturb one gene at a time, which lets a model learn actual causal gene-expression relationships instead of correlations, letting the resulting X-Cell model resume scaling with parameters and compute.

### What changes
The wiki's AI-in-science trend page already tracks self-driving labs (Radical AI's alloy-discovery pace) and protein world models (ESMFold2) as two threads of domain-specific scientific reasoning.

- **AI in Science** gains two new data points: a "Lila Sciences" addition under Self-driving labs (cross-domain automated wet lab, the 10T-token figure, the 2,500x gas-sorption speedup) and a new "Virtual cell models" section covering Xaira's X-Cell/X-Atlas as a named causal counterpoint to the correlational RNA-expression models the field has defaulted to. Page date moves to 21 July; Recent changes reaches its 10-entry cap with these two additions, so no spill is needed yet.
- Two new source pages, one per newsletter.

### What to weigh
Both newsletters are podcast summaries rather than papers or company announcements — the specific numbers (10T tokens, 2,500x speedup, the 1.5B-parameter plateau, ~30x more information) come from the guests' own claims on the podcast, not an independently verifiable benchmark or paper. Treat these as reported claims from the people building the systems, not confirmed third-party results.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/ai-in-science.md` — add Lila Sciences to Self-driving labs, add a new Virtual cell models section for Xaira X-Cell, two new Recent-changes entries, bump `as_of`, merge new source ids
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/lila-sciences-automated-wet-lab-2026-07-16.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/xaira-x-cell-causal-virtual-cell-2026-07-21.md` — source summary

## Page drafts

### wiki/trends/ai-in-science.md (updated)

Frontmatter changes:
```
as_of: 2026-07-21
sources: [noetik-cancer-trials, gpt-rosalind-launch, self-driving-lab-radical-ai, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07, esmfold2-protein-world-model-2026-05, openai-erdos-unit-distance-2026-05, lila-sciences-automated-wet-lab-2026-07-16, xaira-x-cell-causal-virtual-cell-2026-07-21]
```

New content, appended to the end of `## Self-driving labs` (after the "Open-source tooling" bullets):
```
**A second automated lab (Lila Sciences, as of 2026-07-16):** Flagship Pioneering spinout Lila Sciences runs a fully automated, 24/7 robotic wet lab spanning biology, chemistry, drug discovery, and materials science simultaneously — the same lab, same AI, across domains Radical AI treats separately. Lila has generated over 10 trillion experimentally-validated scientific reasoning tokens so far, and rebuilt a gas-sorption measurement to run roughly 2,500x faster by treating lab instruments as nodes on a graph rather than serial steps. Lila's stated goal is a general scientific reasoner, not an automation tool: they report breadth (small-molecule chemistry priors transferring to materials science) outperforming domain-specific models sample-for-sample.
```

New section, inserted after `## Protein world models` and before `## Self-driving labs`:
```
## Virtual cell models

Most RNA-expression models (the dominant "Virtual Cell" approach, built on datasets like the Chan Zuckerberg Institute's 168M-cell CELLxGENE) describe correlations between cell types and states, but can't reliably predict what happens if you change a gene's expression — because gene expression changes are highly correlated and rarely tell you what causes what.

**Xaira's causal counterpoint (as of 2026-07-21):** Xaira Therapeutics' earlier RNA-expression model plateaued around 1.5B parameters — a sign the ceiling was the information in the training data, not model size or compute. Their fix, X-Atlas, is built from CRISPR experiments that perturb one gene at a time, producing data rich enough to establish actual causal (not merely correlational) gene-expression relationships. The resulting model, X-Cell, resumed scaling with added parameters and compute once trained on this richer data — Xaira reports it beats the linear baseline that had outperformed prior virtual-cell models.
```

New entries, prepended to `## Recent changes` (list stays newest-first; this brings the page to its 10-entry cap):
```
- [2026-07-21] Added Xaira Therapeutics' X-Cell/X-Atlas as a causal counterpoint to correlational RNA-expression virtual-cell models
- [2026-07-16] Added Lila Sciences as a second self-driving-lab signal: cross-domain automated wet lab, 10T+ validated scientific reasoning tokens, ~2,500x gas-sorption speedup
```

New lines, appended to `## Sources`:
```
- [Latent Space — The Lab of the Future Should Feel Like a Data Center (Lila Sciences)](../sources/newsletters/lila-sciences-automated-wet-lab-2026-07-16.md)
- [Latent Space — Causal Models Need Causal Data (Xaira X-Cell)](../sources/newsletters/xaira-x-cell-causal-virtual-cell-2026-07-21.md)
```

### wiki/sources/newsletters/lila-sciences-automated-wet-lab-2026-07-16.md (new)

```md
---
title: "Latent Space — The Lab of the Future Should Feel Like a Data Center (Lila Sciences)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-16-the-lab-of-the-future-should-feel-like-a-data-ce.md
published: 2026-07-16
ingested: 2026-09-06
domains: [science]
---

# Latent Space — The Lab of the Future Should Feel Like a Data Center (Lila Sciences)

Latent Space's podcast summary with Lila Sciences' CTO Andy Beam and CSO Rafa Gómez-Bombarelli describes a fully automated, 24/7 robotic wet lab spanning biology, chemistry, drug discovery, and materials science simultaneously, aimed at a general scientific superintelligence rather than narrow automation. Lila has generated over 10 trillion experimentally-validated scientific reasoning tokens and rebuilt a gas-sorption measurement to run roughly 2,500x faster.

## Influenced pages

- [AI in Science](../../trends/ai-in-science.md) — new self-driving-lab data point alongside Radical AI

## Key claims extracted

- Lila Sciences runs one automated wet lab across biology, chemistry, drug discovery, and materials science simultaneously.
- Over 10 trillion experimentally-validated scientific reasoning tokens generated so far.
- A gas-sorption measurement was rebuilt to run ~2,500x faster.
- Lila reports breadth (small-molecule priors transferring to materials science) beating domain-specific models sample-for-sample.
```

### wiki/sources/newsletters/xaira-x-cell-causal-virtual-cell-2026-07-21.md (new)

```md
---
title: "Latent Space — Causal Models Need Causal Data (Xaira X-Cell)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-21-causal-models-need-causal-data-xairas-x-cell-mo.md
published: 2026-07-21
ingested: 2026-09-06
domains: [science]
---

# Latent Space — Causal Models Need Causal Data (Xaira X-Cell)

Latent Space's podcast summary with Xaira Therapeutics' Chief Discovery Officer Ci Chu and Chief AI Scientist Bo Wang describes X-Cell, a virtual-cell model trained on X-Atlas — a dataset built from CRISPR experiments that perturb one gene at a time to establish causal, not merely correlational, gene-expression relationships. Xaira's prior RNA-expression model had plateaued around 1.5B parameters; the richer causal data let scaling resume.

## Influenced pages

- [AI in Science](../../trends/ai-in-science.md) — new "Virtual cell models" section, positioned as a causal counterpoint to correlational RNA-expression models

## Key claims extracted

- Xaira's earlier RNA-expression model plateaued around 1.5B parameters, an information-ceiling signal rather than a compute or parameter limit.
- X-Atlas is built from CRISPR experiments perturbing one gene at a time, to establish causal gene-expression relationships.
- X-Cell, trained on X-Atlas, resumed scaling with parameters and compute and reportedly beats the prior linear baseline.
- Most existing virtual-cell models (built on datasets like CELLxGENE) capture correlation, not causation, in gene expression.
```

## Open questions
None.
