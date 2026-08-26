---
type: proposal
source: raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md
status: pending
created: 2026-08-25
---

# Proposal: OpenAI model disproves 80-year-old Erdős unit-distance conjecture

## Summary
An internal OpenAI general-purpose reasoning model disproved the 1946 Erdős planar unit-distance conjecture, producing a construction that beats the long-assumed "square grid" upper bound; the result was verified by external mathematicians (Noga Alon, Tim Gowers, Arul Shankar, Jacob Tsimerman) who called it a milestone. **Verification note:** I confirmed the core claim, the general-purpose-model framing, and the mathematician quotes directly against OpenAI's own announcement page. OpenAI's page does **not** disclose a model name/version, run duration, or dollar cost — the specific "<32 hours" / "<$1,000" / "speculated GPT-5.6" figures circulating in AINews/Twitter recap are **not corroborated by OpenAI** and should be treated as unverified secondary speculation. See Open Questions.

## Intended changes

- [x] **Update** `wiki/state-of/science.md` — add a bullet under "Frontier models used in science"; add a Recent changes entry (`as_of` unchanged, 2026-07-06 remains the newest source-backed claim)
    > See draft below.

- [x] **Update** `wiki/trends/ai-in-science.md` — add a bullet noting the domain broadening beyond biology into pure mathematics; add a Recent changes entry (`as_of` unchanged, 2026-07-06 remains the newest source-backed claim)
    > See draft below.

- [x] **Spill** `wiki/state-of/science.md` → `wiki/history/state-of/science.md` — adding a new Recent changes entry pushes the section from 10 to 11; the oldest entry ("Added `Science agent platforms`...") spills to history.
    > See draft below.

- [x] **Create** `wiki/sources/articles/openai-erdos-unit-distance-2026-05.md` — source summary, anchored to OpenAI's primary announcement

## Page drafts

### wiki/state-of/science.md (updated)

Frontmatter changes (sources list only; `as_of` unchanged at 2026-07-06):

```yaml
sources: [curiosity-driven-imagination, noetik-cancer-trials, gpt-rosalind-launch, futurehouse-homepage, legacy-ai-tools-roadmap-xlsx, openai-gpt-5-5-launch, ai-co-mathematician-2026-05-13, genesis-ai-gene-26-5-2026-05-09, self-driving-lab-radical-ai, axiom-math-june-2026, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07, esmfold2-protein-world-model-2026-05, openai-erdos-unit-distance-2026-05]
```

`### Frontier models used in science` (full subsection, new bullet added):

```md
### Frontier models used in science

General-purpose frontier models whose published evaluation or reported use now makes them relevant to practical scientific-research work, even if they are not science-only products.

- [GPT-5.5](../models/gpt-5-5.md) — OpenAI; BixBench 80.5%, meaningful GeneBench gains over GPT-5.4, and launch examples spanning bioinformatics analysis, theorem proving, and early research assistance *(as of 2026-04-23)*
- **AI Co-Mathematician** — Google DeepMind; asynchronous, stateful research workbench for mathematicians; supports ideation, literature discovery, computational analysis, theorem verification, and formal proof outputs; 48% on FrontierMath Tier 4 (research-level math above olympiad-style, authored by 64 mathematicians); paper: arxiv.org/abs/2605.06651 *(as of 2026-05-13)*
- **OpenAI internal reasoning model** — an unnamed general-purpose reasoning model (not a math-specialized or scaffolded system) disproved the Erdős planar unit-distance conjecture (1946), a well-known open problem in discrete geometry, discovering a construction that beats the long-assumed "square grid" upper bound. Verified by external mathematicians (Noga Alon, Tim Gowers, Arul Shankar, Jacob Tsimerman), who called it a milestone in AI mathematics; a companion paper by external mathematicians accompanies the result. OpenAI's own announcement discloses no model name/version, run duration, or cost — secondary newsletter coverage speculated "<32 hours," "<$1,000," and a "GPT-5.6" lineage, none of which OpenAI's page corroborates *(as of 2026-05-20, OpenAI primary source)*
```

Updated `## Recent changes` (full section, new entry added at top, oldest entry removed — see Spill draft below):

```md
## Recent changes

- [2026-05-20] OpenAI's internal general-purpose reasoning model disproved the 1946 Erdős planar unit-distance conjecture; verified by external mathematicians (Alon, Gowers, Shankar, Tsimerman) who called it a milestone in AI mathematics. OpenAI's own announcement discloses no model name, runtime, or cost — the "<32h / <$1,000 / GPT-5.6" figures circulating in secondary coverage are unverified speculation, not OpenAI claims.
- [2026-05-27] Added protein models and molecular biology subcategory with ESMFold2 as an open protein-world-model signal.
- [2026-07-06] Claude Science entered the science-agent-platform set; Anthropic confirms public beta with reproducible artifacts, persistent kernels, 60+ scientific databases, and compute/tool integrations.
- [2026-07-01] Claude Science official announcement adds reviewer agents, artifact rendering, scientific model integrations, and Manifold Bio / Allen Institute / UCSF case studies.
- [2026-07-05] Anthropic's internal drug programs make evaluation/verification feedback loops the Claude Science strategy point to watch.
- [2026-06-03] Added formal verification subcategory; Axiom Math: 12/12 Putnam 2025, 99% ProofGen vs o3's 4.9%; AXLE open-source Lean toolkit; $200M / $1.6B; thesis: formal verification = scalable RL reward signal
- [2026-06-17] Added `Self-driving labs` subcategory; Radical AI: ~10× DARPA/GE MACH pace; AI scientist proposed 300 new materials, 10 with novel state-of-the-art properties; TorchSim and MATRIX open-sourced
- [2026-05-09] Added `Robotics` subcategory; Genesis AI GENE-26.5 (full-stack multi-manufacturer robot model + 5-finger hand) goes viral; "embodiment gap" framing introduced
- [2026-05-13] Added AI Co-Mathematician (Google DeepMind): 48% FrontierMath Tier 4; asynchronous stateful workbench for mathematicians; physics-intern (related) boosted Gemini 3.1 Pro from 17.7% → 31.4% on CritPt via specialized subagent decomposition
- [2026-04-23] Added `Frontier models used in science` with [GPT-5.5](../models/gpt-5-5.md); OpenAI is now making explicit science-performance claims rather than only general-reasoning claims
```

(Note: the previous last entry — `[2026-04-22] Added `Science agent platforms` with [FutureHouse]...` — is removed here and spilled to history, keeping the section at 10 entries.)

### wiki/history/state-of/science.md (updated — append only)

Append this line to the existing `## Archived from current page on 2026-08-25` section at the top of the file (do not create a duplicate header, do not reformat the rest of the file):

```md
- [2026-04-22] Added `Science agent platforms` with [FutureHouse](../../tools/futurehouse.md) as the first productized science-agent signal from the legacy workbook exception
```

### wiki/trends/ai-in-science.md (updated)

Frontmatter changes (sources list only; `as_of` unchanged at 2026-07-06):

```yaml
sources: [noetik-cancer-trials, gpt-rosalind-launch, self-driving-lab-radical-ai, claude-science-beta-2026-07-06, every-tale-of-two-models-2026-07-05, claude-science-workbench-2026-07, esmfold2-protein-world-model-2026-05, openai-erdos-unit-distance-2026-05]
```

Add one bullet to `## Current status (as of 2026-04-21)` (full list, new bullet appended at the end):

```md
## Current status (as of 2026-04-21)

- Noetik is presented as using large multimodal tumor datasets and transformer models to predict treatment response and improve cancer-trial selection
- The company reportedly signed a $50M GSK deal tied to this stack
- OpenAI launched GPT-Rosalind as a frontier reasoning model for biology, drug discovery, and translational medicine
- Translational medicine here means moving from lab and data insight toward practical clinical use, such as deciding which therapies, biomarkers, or trial designs are most likely to work in patients
- The pattern is shifting from "AI helps researchers" to "specialized models target a scientific bottleneck directly"
- Anthropic's Claude Science signal reinforces a platform-first strategy in science AI: build tools for analysis, visualization, traceability, reviewer-agent verification, scientific databases, and lab/HPC compute, then dogfood them on real preclinical and partner research workflows.
- The hard part is not only hypothesis generation. Biological feedback is slow and expensive, so evaluation and verification workflows become the bottleneck the platform must solve.
- ESMFold2 adds a protein-world-model signal: general transformer scaling and diverse protein data are being applied to structure prediction, protein interactions, antibody tasks, and design/discovery workflows.
- The domain-specific-reasoning pattern is not limited to biology: an OpenAI general-purpose reasoning model (not a math-specialized system) disproved the 1946 Erdős planar unit-distance conjecture, verified by external mathematicians — see [State of Science](../state-of/science.md) for detail and sourcing caveats.
```

Updated `## Recent changes` (full section, new entry added at top):

```md
## Recent changes

- [2026-05-20] Added an OpenAI Erdős unit-distance result as evidence the "specialized scientific reasoning" pattern extends beyond biology into pure mathematics; verified against OpenAI's own announcement (model name, runtime, and cost are not disclosed by OpenAI, despite secondary-source speculation).
- [2026-05-27] Added ESMFold2 as a protein-world-model signal: open protein prediction/design engine, antibody interaction strength, and atlas-scale structure predictions.
- [2026-07-06] Claude Science public beta confirms a science-workflow platform layer: reproducible artifacts, persistent kernels, 60+ scientific databases, scientific connectors, and local/HPC compute integration.
- [2026-07-01] Official Claude Science announcement adds reviewer agents, BioNeMo/Boltz/OpenFold-style integrations, and Manifold Bio / Allen Institute / UCSF case studies.
- [2026-07-05] Claude Science and Anthropic's internal drug programs reframed science agents as dogfooded workflow platforms, not only model demos.
- [2026-06-17] Added self-driving labs section: Radical AI achieving ~10× DARPA/GE MACH pace in alloys; infrastructure-as-bottleneck framing from Anthropic science blog
- [2026-04-21] Added biology and drug-discovery productization signals: Noetik and GPT-Rosalind
- [2026-04-10] Page seeded from Superhuman AI newsletter overview of AI-driven scientific breakthroughs
```

### wiki/sources/articles/openai-erdos-unit-distance-2026-05.md (new)

```md
---
title: OpenAI model disproves the Erdős planar unit-distance conjecture
type: source
source_type: article
source_file: raw/articles/2026-08-25-openaicom-index-model-disproves-discrete-geometry-conjecture.md
url: https://openai.com/index/model-disproves-discrete-geometry-conjecture/
published: 2026-05-20
ingested: 2026-08-25
domains: [science, models]
---

# OpenAI model disproves the Erdős planar unit-distance conjecture

An internal OpenAI general-purpose reasoning model — not a math-specialized or scaffolded system — disproved the planar unit-distance conjecture Paul Erdős posed in 1946, producing an infinite family of constructions that beat the long-assumed "square grid" upper bound (n^(1+δ) unit-distance pairs for some fixed δ > 0; a later refinement by Princeton's Will Sawin gives δ = 0.014). The proof was checked by a group of external mathematicians, who co-authored a companion paper. This source page is anchored to OpenAI's own announcement (confirmed via a direct browser read after the automated fetch hit a Cloudflare bot-check page — see the note in the raw file), not to secondary AINews/Twitter recap.

**Verification note:** OpenAI's page discloses no model name/version, run duration, or dollar cost. The "an internal model, speculated GPT-5.6, running for <32 hours / <$1,000" framing that circulated in AINews and on Twitter is secondary speculation, not an OpenAI claim, and is not corroborated on the primary page.

## Influenced pages
- [State of Science](../../state-of/science.md) — added as a new bullet under "Frontier models used in science," explicitly flagging the unverified secondary-source figures
- [AI in Science](../../trends/ai-in-science.md) — added as evidence the domain-specific-reasoning pattern extends beyond biology into pure mathematics

## Key claims extracted
- Disproves the "square grid is optimal" belief about the planar unit-distance problem (Erdős, 1946); yields ≥ n^(1+δ) unit-distance pairs for infinitely many n, δ > 0 (later refined to δ = 0.014 by Will Sawin)
- Produced by a general-purpose reasoning model, explicitly not a math-specialized or scaffolded system, as part of a broader effort testing frontier models on a collection of Erdős problems
- Verified by external mathematicians (Noga Alon, Tim Gowers, Arul Shankar, Jacob Tsimerman); a companion paper accompanies the result; Gowers: "a milestone in AI mathematics... I would have recommended acceptance without any hesitation" (for the Annals of Mathematics)
- Framed by OpenAI as the first time a prominent open problem central to a subfield of mathematics has been solved autonomously by AI, with an explicit caveat that "expertise becomes more valuable, not less" and that humans still choose problems and interpret results
- No model name/version, run duration, or dollar cost is disclosed on OpenAI's page — the "<32 hours," "<$1,000," and "GPT-5.6" figures are secondary AINews/Twitter speculation only

## Secondary coverage (for context, not primary evidence)
- `raw/newsletters/2026-05-21-ainews-openai-gpt-next-disproves-80-year-old-erd.md` — AINews recap; source of the unverified time/cost/model-version speculation
- `raw/newsletters/2026-05-22-ainews-new-ai-infra-unicorns-exa-modal-turbop.md` — brief follow-on discussion
- `raw/newsletters/2026-05-21-meet-the-autonomous-growth-agent.md` — one-line consumer-angle mention
```

## Open questions
- **Flagging as requested:** the core claim (disproof, verification, general-purpose-model framing, named mathematician endorsements) is confirmed against OpenAI's own page. The specific "<32 hours," "<$1,000," and "GPT-5.6" details are **not** — they trace only to AINews/Twitter speculation and should not be repeated as settled fact. Recommend treating them as unverified if this comes up again.
- Should this also get a `wiki/benchmarks/` or `wiki/concepts/` entry (e.g., a "math-discovery" or "AI-assisted proof" concept page), given the wiki already has `formal-verification` (Axiom Math) as an adjacent but distinct subcategory (formal/Lean-checked proofs vs. this informally-but-professionally-verified result)? Left as a bullet on existing pages for now given a single event with one primary source.
