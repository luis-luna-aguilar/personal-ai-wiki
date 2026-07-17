---
type: proposal
source:
  - raw/newsletters/2026-05-27-esmfold2-the-bitter-lesson-is-coming-for-protein.md
  - raw/newsletters/2026-05-28-ainews-cognition-raises-1b-in-26b-series-d.md
status: pending
created: 2026-07-08
---

# Proposal: ESMFold2 and protein world models

## Summary

The approved ESMFold2 signal is a strong science update. It should add a protein-model entry to the science dashboard and update the AI-in-science trend around general transformer scaling, protein interactions, and data-rich scientific world models.

## Intended changes

- [ ] **Update** `wiki/state-of/science.md` - add protein models / molecular biology subcategory with ESMFold2.
- [ ] **Update** `wiki/trends/ai-in-science.md` - add protein world-model signal.
- [ ] **Create** `wiki/sources/newsletters/esmfold2-protein-world-model-2026-05.md` - source summary.

## Page drafts

### wiki/state-of/science.md (updated sections)

```md
---
as_of: 2026-05-27
sources: [..., esmfold2-protein-world-model-2026-05]
---

## Subcategories

### Protein models and molecular biology

AI systems that model protein structure, interaction, and design as scientific infrastructure rather than generic chat assistance.

- **ESMFold2** - BioHub / Alex Rives; open scientific engine for protein prediction, interaction modeling, design, and discovery; source coverage emphasizes antibody interactions, inference-time scaling, and a 6.8B-protein atlas with 1.1B predicted structures *(as of 2026-05-27)*

## Recent changes

- [2026-05-27] Added protein models and molecular biology subcategory with ESMFold2 as an open protein-world-model signal.
```

### wiki/trends/ai-in-science.md (updated sections)

```md
---
as_of: 2026-05-27
sources: [..., esmfold2-protein-world-model-2026-05]
---

## Current status (as of 2026-05-27)

Add:

- ESMFold2 adds a protein-world-model signal: general transformer scaling and diverse protein data are being applied to structure prediction, protein interactions, antibody tasks, and design/discovery workflows.

## Protein world models

ESMFold2 is a useful biology counterpoint to purely lab-automation stories. The source frames it as an open engine trained on diverse protein data, with reported strengths on protein interactions and antibodies, plus inference-time scaling across cancer and immunology targets.

The practical importance is the same as other science-agent infrastructure: better models are only useful if they plug into data, verification, and downstream discovery loops. ESMFold2's atlas and open licensing make it a durable signal to watch, but the wiki should distinguish source-reported performance from broad clinical or wet-lab validation.

## Recent changes

- [2026-05-27] Added ESMFold2 as a protein-world-model signal: open protein prediction/design engine, antibody interaction strength, and atlas-scale structure predictions.
```

### wiki/sources/newsletters/esmfold2-protein-world-model-2026-05.md (new)

```md
---
title: ESMFold2 - The bitter lesson is coming for protein
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-27-esmfold2-the-bitter-lesson-is-coming-for-protein.md
url: https://www.latent.space/p/esmfold2
published: 2026-05-27
ingested: 2026-07-08
domains: [science]
---

# ESMFold2 - The bitter lesson is coming for protein

Latent Space covers ESMFold2 as an open scientific engine for protein prediction, interaction modeling, design, and discovery. The source emphasizes the role of general transformer scaling, diverse protein data, antibody tasks, inference-time scaling, and atlas-scale predicted structures.

## Influenced pages

- [State of Science](../../state-of/science.md) - new protein-model subcategory
- [AI in Science](../../trends/ai-in-science.md) - protein world-model trend update

## Key claims extracted

- ESMFold2 is positioned as an open engine for protein prediction, design, and discovery.
- Source coverage reports strong performance on protein interactions, especially antibodies.
- The source cites a 6.8B-protein atlas and 1.1B predicted structures.
```

## Open questions

- Should ESMFold2 later receive a dedicated `models/` page, or is a science dashboard/trend update enough for now?
