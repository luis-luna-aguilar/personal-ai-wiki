---
type: proposal
source: raw/articles/2026-10-20-substackcom-redirect-4e32e96d-f7e4-41b5-afbf-24e57a2f87d5.md
sources:
  - raw/articles/2026-10-20-substackcom-redirect-4e32e96d-f7e4-41b5-afbf-24e57a2f87d5.md
  - raw/newsletters/2026-09-24-ainews-meta-connect-2026-muse-glasses-voice-v.md
  - raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
  - raw/newsletters/2026-09-22-an-oscar-two-asteroids-and-the-algorithm-in-yo.md
  - raw/newsletters/2026-09-23-bio-security-is-an-ai-arms-race-eric-nguyen-ce.md
triage: proposals/triage/2026-09-21-to-2026-09-30-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: AI for science — Claude agents find the ART phage system, Google's ERA, genomic language models

## Summary

### In short
Agent swarms can now originate a biological discovery, not just assist one, but the human lab step still decides what it means. About 950 Claude agents mined 200,000+ reverse transcriptases in 21 hours and flagged an unnoticed CRISPR-like system whose function is still unknown; Google's ERA shows the same pattern for any problem with a written score. The proposal adds three short sections to AI in Science, two lines to State of Science, and five source pages. Reason to hesitate: AI in Science would land near 133% of its length ceiling, so a split is offered.

[[#Open questions|Open questions: 2 to answer.]]

### The source
In late September Anthropic announced a new life-sciences research group with its own Bay Area lab (low biosafety levels only, all bench work done by humans). Its first result: given one high-level prompt, roughly 950 Claude agents spent 21 hours and 210 million tokens combing a DNA database for reverse transcriptases, enzymes that copy RNA into DNA. They gathered over 200,000, nominated 3,500 candidate systems and wrote reports on 20. One agent noticed, next to an already-known enzyme in a jumbo bacteriophage (a large virus that infects bacteria), a long array of evenly spaced DNA repeats and an extra gene. The layout resembles a CRISPR array, the feature that makes CRISPR programmable. Anthropic named it ART (array-associated reverse transcriptases). Human-run experiments showed the array is transcribed into distinct short RNAs, but its function is unknown. Anthropic says so plainly, Dario Amodei called it PhD-worthy but of unclear significance, commenters stressed it is nowhere near AlphaFold or CRISPR scale, and a Stanford team independently described a related system. The post also says the lab now studies which agent reports scientists choose to test, and feeds that "taste" back into Claude's instructions.

Two Latent Space episodes round out the cluster. John Platt explained Google's Empirical Research Assistance (ERA): once a science problem has a score function, Gemini keeps a tree of experiment notebooks and keeps mutating the promising ones. It stopped failing and started working between Gemini 2.0 and 2.5, has produced at least ten papers, and cracked a contrail-warming problem that had stalled Platt's team for two years. His warning: "It's a power tool. It can slice your fingers off." Eric Nguyen of Radical Numerics (Evo, Evo 2) argued that genomic language models now improve DNA designs in context, and that biosecurity defense is losing the race.

### What changes
AI in Science currently runs to 11 August and covers drug design, virtual cells and self-driving labs, but no agent-originated discovery and nothing on biosecurity.

- **AI in Science** gains two status bullets and three short sections: the ART result with its caveats, ERA as the "optimize anything scoreable" pattern, and genomic language models with the biosecurity argument. Three Recent-changes entries are added and the three oldest spill to history. Page date moves to 24 September.
- **State of Science** adds Anthropic's life-sciences lab and Google ERA as lines under Science agent platforms, plus one Recent-changes entry. The oldest entry spills to history. Page date moves to 24 September.
- Five new source pages: the Anthropic post, two AINews stories (the announcement with Amodei's framing, and the community critique), the Platt episode, and the Nguyen episode.

### What to weigh
The Anthropic post carries no date. The proposal dates it 23 September, the last day covered by the AINews issue that reported it, although the linked bioRxiv preprint ID carries 5 October. The Nguyen source is a short episode teaser that describes the aptamer result only in a quote, so it stays one paragraph.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/ai-in-science.md` — two status bullets, three new sections (ART, ERA, genomic language models), frontmatter sources merged, `as_of` 2026-08-11 → 2026-09-24; Recent changes adds three entries dated 2026-09-24, 2026-09-23 and 2026-09-22
    > See draft below

- [ ] **Spill** `wiki/trends/ai-in-science.md` → `wiki/history/trends/ai-in-science.md` — the live list is at the cap of 10; spills the three oldest entries (expected: 2026-06-17, 2026-07-01, 2026-07-05)

- [ ] **Update** `wiki/state-of/science.md` — two new lines under Science agent platforms, sources merged, `as_of` 2026-07-06 → 2026-09-24; Recent changes adds one entry dated 2026-09-24
    > See draft below

- [ ] **Spill** `wiki/state-of/science.md` → `wiki/history/state-of/science.md` — list at the cap of 10; spills the oldest entry (expected: 2026-04-23)

- [ ] **Create** `wiki/sources/articles/anthropic-claude-art-enzyme-system-2026-09.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-claude-art-amodei-2026-09-24.md`
- [ ] **Create** `wiki/sources/newsletters/ainews-art-critique-2026-09-25.md`
- [ ] **Create** `wiki/sources/newsletters/john-platt-google-era-2026-09-22.md`
- [ ] **Create** `wiki/sources/newsletters/radical-numerics-genomic-lms-biosecurity-2026-09-23.md`

## Page drafts

### wiki/trends/ai-in-science.md (updated)

Frontmatter changes:

```
as_of: 2026-09-24
sources: [...existing..., anthropic-claude-art-enzyme-system-2026-09, ainews-claude-art-amodei-2026-09-24, ainews-art-critique-2026-09-25, john-platt-google-era-2026-09-22, radical-numerics-genomic-lms-biosecurity-2026-09-23]
```

Current status heading and two bullets appended to the end of the list:

```
## Current status (as of 2026-09-24)

...existing bullets...
- Agent swarms produced the first genome-mining discovery claim in this wiki: Anthropic's ART phage system, found by ~950 Claude agents and confirmed only as far as "transcribed into short RNAs" (see below).
- "Optimize anything scoreable" is emerging as a reusable science pattern (Google ERA), while genomic language models raise the biosecurity stakes of the same capability gains.
```

New sections, inserted after `## Protein world models`:

```
## Agent swarms as discoverers (Anthropic ART)

Anthropic's new life-sciences lab (Bay Area, BSL-1/2 only, all bench work by humans) gave Claude one high-level prompt: search a DNA database for interesting reverse transcriptases (RTs, enzymes that copy RNA into DNA). About 950 agents ran for 21 hours on 210M tokens, gathered 200,000+ RTs, nominated 3,500 candidate systems and wrote reports on the 20 strongest. One agent noticed that a known RT in jumbo bacteriophages sits beside an accessory gene and a long array of evenly spaced DNA repeats, a CRISPR-like layout nobody had described. Anthropic calls the system ART (array-associated reverse transcriptases).

- **Validated so far:** human-run experiments (expression in E. coli plus RNA-seq) show the array is transcribed into distinct short RNAs. Function is unknown; there is no evidence yet of programmable editing.
- **Reception:** Amodei called it PhD-worthy but of unclear significance; community critics said it is not AlphaFold- or CRISPR-scale; a Stanford team independently described a distinct RT system with a non-coding array.
- **Workflow lesson:** with hundreds to thousands of reports per campaign, the lab now studies which hypotheses scientists choose to test and feeds that "taste" back into Claude's instructions. Work runs in Claude Science and Claude Code, sometimes with a harness that coordinates many parallel sessions.

## Optimizing anything scoreable (Google ERA)

Google's Empirical Research Assistance (ERA), described by John Platt, reduces any science problem with a written score function to a search: the LLM keeps a tree of past experiment notebooks and mutates the promising ones, a close cousin of Monte Carlo tree search. It went from not working on Gemini 2.0 to working well on 2.5, has produced at least ten papers, and found the missing model for the reflected-sunlight half of contrail warming, a counterfactual problem that had stalled Platt's team for two years. The hard part moves to writing the score. ERA yields predictive models; checking that they are descriptive stays with the scientist. Platt: "It's a power tool. It can slice your fingers off."

## Genomic language models and biosecurity

Genomic language models read and write DNA directly. Evo-family models were used by an Arc/Stanford team to generate whole bacteriophage genomes that were synthesized into working viruses. Radical Numerics (Eric Nguyen, Evo / Evo 2) reports in-context optimization: shown RNA aptamers ranked from low to high score, the model continues the trajectory toward better sequences, which Nguyen frames as chain-of-thought in DNA. His view is that biosecurity defense is currently losing the arms race and must keep pace by pushing the frontier, not by holding it back.
```

Recent changes: adds three entries at the top (newest first), then spills the three oldest:

```
## Recent changes

- [2026-09-24] Anthropic's life-sciences lab reported ART, a CRISPR-like phage reverse-transcriptase system found by ~950 Claude agents (21 hours, 210M tokens); array confirmed transcribed into short RNAs, function unknown; critics and Amodei both call its significance unclear.
- [2026-09-23] Added genomic language models and biosecurity: Radical Numerics reports in-context DNA optimization and argues defense is losing the arms race.
- [2026-09-22] Added Google's ERA (Empirical Research Assistance): tree search over Gemini-mutated notebooks for any problem with a score function; 10+ papers, contrail counterfactual solved.
- [2026-09-07] Pure-mathematics signals (OpenAI's Erdős disproof, Anthropic's Riemann Hypothesis bound) split out into a new dedicated page, [AI in Mathematics](ai-in-mathematics.md), at the user's request.
- [2026-08-11] Added Chai Discovery as an AI-native drug-design signal: structural-to-binding-model shift, CAD-style molecule editor, four pharma deals since January (Lilly, Novartis, argenx, expanded Eli Lilly program), $4B valuation
- [2026-08-11] Anthropic reported an unreleased research Claude variant improved a Riemann Hypothesis-related bound (proportion of zeta zeros proven on the critical line: 41.6% → 67.2%), via ~31M output tokens of retries/exploration — a second pure-math signal alongside OpenAI's Erdős disproof; not yet independently verified.
- [2026-08-06] Jeff Dean, Sanjay Ghemawat, Oriol Vinyals, and Quoc Le left Google DeepMind to found autoresearch startup Discovery Loop; accompanied by a DeepMind leadership reshuffle (Hassabis to Chair of GDM/Chief Scientist of Alphabet, Kavukcuoglu to SVP of DeepMind)
- [2026-07-21] Added Xaira Therapeutics' X-Cell/X-Atlas as a causal counterpoint to correlational RNA-expression virtual-cell models
- [2026-07-16] Added Lila Sciences as a second self-driving-lab signal: cross-domain automated wet lab, 10T+ validated scientific reasoning tokens, ~2,500x gas-sorption speedup
- [2026-07-06] Claude Science public beta confirms a science-workflow platform layer: reproducible artifacts, persistent kernels, 60+ scientific databases, scientific connectors, and local/HPC compute integration.
```

Sources section: appends five links:

```
- [Anthropic — Claude discovers a novel enzyme system](../sources/articles/anthropic-claude-art-enzyme-system-2026-09.md)
- [AINews — Claude's ART phage system and Amodei's framing](../sources/newsletters/ainews-claude-art-amodei-2026-09-24.md)
- [AINews — Community critique of the ART result](../sources/newsletters/ainews-art-critique-2026-09-25.md)
- [Latent Space — John Platt on Google's ERA](../sources/newsletters/john-platt-google-era-2026-09-22.md)
- [Latent Space — Eric Nguyen: bio-security is an AI arms race](../sources/newsletters/radical-numerics-genomic-lms-biosecurity-2026-09-23.md)
```

### wiki/history/trends/ai-in-science.md (updated)

Appended at the end (the actual spill is whatever is oldest at apply time):

```
## Archived from current page on <apply date>

- [2026-07-05] Claude Science and Anthropic's internal drug programs reframed science agents as dogfooded workflow platforms, not only model demos.
- [2026-07-01] Official Claude Science announcement adds reviewer agents, BioNeMo/Boltz/OpenFold-style integrations, and Manifold Bio / Allen Institute / UCSF case studies.
- [2026-06-17] Added self-driving labs section: Radical AI achieving ~10× DARPA/GE MACH pace in alloys; infrastructure-as-bottleneck framing from Anthropic science blog
```

### wiki/state-of/science.md (updated)

Frontmatter changes:

```
as_of: 2026-09-24
sources: [...existing..., anthropic-claude-art-enzyme-system-2026-09, john-platt-google-era-2026-09-22]
```

Two lines appended under `### Science agent platforms`:

```
- **Anthropic life-sciences lab** — Claude agent swarms mine genomic databases and file reports for human-run lab tests; ~950 agents flagged the ART phage system (function unknown) — see [AI in Science](../trends/ai-in-science.md) *(as of 2026-09-23)*
- **Google ERA** (Empirical Research Assistance) — Gemini tree search over experiment notebooks for any problem with a score function; 10+ papers *(as of 2026-09-22)*
```

Recent changes: adds one entry at the top, then spills the oldest:

```
## Recent changes

- [2026-09-24] Added Anthropic's life-sciences lab (Claude agents found the ART phage system, function still unknown) and Google's ERA (score-function tree search) to Science agent platforms.
- [2026-07-06] Claude Science entered the science-agent-platform set; Anthropic confirms public beta with reproducible artifacts, persistent kernels, 60+ scientific databases, and compute/tool integrations.
- [2026-07-05] Anthropic's internal drug programs make evaluation/verification feedback loops the Claude Science strategy point to watch.
- [2026-07-01] Claude Science official announcement adds reviewer agents, artifact rendering, scientific model integrations, and Manifold Bio / Allen Institute / UCSF case studies.
- [2026-06-17] Added `Self-driving labs` subcategory; Radical AI: ~10× DARPA/GE MACH pace; AI scientist proposed 300 new materials, 10 with novel state-of-the-art properties; TorchSim and MATRIX open-sourced
- [2026-06-03] Added formal verification subcategory; Axiom Math: 12/12 Putnam 2025, 99% ProofGen vs o3's 4.9%; AXLE open-source Lean toolkit; $200M / $1.6B; thesis: formal verification = scalable RL reward signal
- [2026-05-27] Added protein models and molecular biology subcategory with ESMFold2 as an open protein-world-model signal.
- [2026-05-20] Added OpenAI's unnamed general-purpose reasoning model to `Frontier models used in science`: disproved the 1946 Erdős planar unit-distance conjecture, verified by external mathematicians (Alon, Gowers, Shankar, Tsimerman); OpenAI discloses no model name, runtime, or cost
- [2026-05-13] Added AI Co-Mathematician (Google DeepMind): 48% FrontierMath Tier 4; asynchronous stateful workbench for mathematicians; physics-intern (related) boosted Gemini 3.1 Pro from 17.7% → 31.4% on CritPt via specialized subagent decomposition
- [2026-05-09] Added `Robotics` subcategory; Genesis AI GENE-26.5 (full-stack multi-manufacturer robot model + 5-finger hand) goes viral; "embodiment gap" framing introduced
```

### wiki/history/state-of/science.md (updated)

Appended at the end:

```
## Archived from current page on <apply date>

- [2026-04-23] Added `Frontier models used in science` with [GPT-5.5](../../models/gpt-5-5.md); OpenAI is now making explicit science-performance claims rather than only general-reasoning claims
```

### wiki/sources/articles/anthropic-claude-art-enzyme-system-2026-09.md (new)

```
---
title: Anthropic — Claude discovers a novel enzyme system
type: source
source_type: article
source_file: raw/articles/2026-10-20-substackcom-redirect-4e32e96d-f7e4-41b5-afbf-24e57a2f87d5.md
url: https://substack.com/redirect/4e32e96d-f7e4-41b5-afbf-24e57a2f87d5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0
published: 2026-09-23
ingested: 2026-10-20
domains: [science]
---

# Anthropic — Claude discovers a novel enzyme system

Anthropic introduces its life-sciences research group and lab and reports its first result: ~950 Claude agents, given one high-level prompt, mined over 200,000 reverse transcriptases and flagged ART, a phage system pairing a known RT with an accessory gene and a CRISPR-like repeat array. Lab tests show the array is transcribed into short RNAs; function is unknown. The post is undated; the date is inferred from AINews coverage (bioRxiv preprint linked).

## Influenced pages
- [AI in Science](../../trends/ai-in-science.md) — new ART section and status bullet
- [State of Science](../../state-of/science.md) — Anthropic life-sciences lab line

## Key claims extracted
- ~950 agents, 21 hours, 210M tokens; 200,000+ RTs → 3,500 candidates → 20 reports
- ART: RT + accessory gene + long array of evenly spaced repeats, found mainly in bacteriophages
- Array expressed as distinct short RNAs; function and any editing utility unknown
- Lab is BSL-1/2 only; all bench work done by humans; Claude Science and Claude Code plus a parallel-session harness
- The lab studies which agent hypotheses scientists pick to test and feeds that taste back into Claude's instructions
- Feng Zhang called the RNA-repeat arrays "genuinely intriguing"
```

### wiki/sources/newsletters/ainews-claude-art-amodei-2026-09-24.md (new)

```
---
title: AINews — Claude's ART phage system and Amodei's framing
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-24-ainews-meta-connect-2026-muse-glasses-voice-v.md
url: https://www.latent.space/p/ainews-meta-connect-2026-muse-glasses
published: 2026-09-24
ingested: 2026-10-20
domains: [science]
---

# AINews — Claude's ART phage system and Amodei's framing

AINews story covering Anthropic's ART announcement (news of 22–23 September) and Dario Amodei's thread on it.

## Influenced pages
- [AI in Science](../../trends/ai-in-science.md) — ART reception and the Stanford parallel

## Key claims extracted
- Humans ran Claude-proposed experiments: expression in E. coli plus RNA-seq
- Amodei: PhD-worthy, unclear significance; AI-for-bio on the same weak-to-superhuman curve as math
- A Stanford team independently described a distinct RT system with a non-coding array
```

### wiki/sources/newsletters/ainews-art-critique-2026-09-25.md (new)

```
---
title: AINews — Community critique of the ART result
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-25-ainews-the-future-of-latent-space.md
url: https://www.latent.space/p/ainews-the-future-of-latent-space
published: 2026-09-25
ingested: 2026-10-20
domains: [science]
---

# AINews — Community critique of the ART result

Reddit recap in AINews on Anthropic's ART claim: commenters were cautiously positive about agent hypothesis generation but stressed the limits of the lab evidence.

## Influenced pages
- [AI in Science](../../trends/ai-in-science.md) — reception caveat in the ART section

## Key claims extracted
- Not comparable to AlphaFold 2 or CRISPR-level functional discovery
- No evidence yet of programmable gene editing or a CRISPR-like mechanism
- Read as evidence that agents can contribute original hypotheses for human validation
```

### wiki/sources/newsletters/john-platt-google-era-2026-09-22.md (new)

```
---
title: 'Latent Space — John Platt on AI for science and Google''s ERA'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-22-an-oscar-two-asteroids-and-the-algorithm-in-yo.md
url: https://www.latent.space/p/john-platt
published: 2026-09-22
ingested: 2026-10-20
domains: [science]
---

# Latent Space — John Platt on AI for science and Google's ERA

Podcast notes with Google's John Platt. Core idea: many science problems reduce to a "scoreable task", and Google's Empirical Research Assistance (ERA) automates the search for code that maximizes the score.

## Influenced pages
- [AI in Science](../../trends/ai-in-science.md) — new ERA section
- [State of Science](../../state-of/science.md) — Google ERA line

## Key claims extracted
- ERA: an LLM keeps a tree of experiment notebooks and mutates promising ones; a cousin of Monte Carlo tree search; grew out of an "auto-Kaggle" idea
- Step change between Gemini 2.0 (did not work) and 2.5 (works well); at least ten papers
- Solved the reflected-sunlight half of a contrail-warming counterfactual that stalled the team for two years
- ERA gives predictive models; the scientist must check they are descriptive ("a power tool… can slice your fingers off"); Goodhart's law applies
```

### wiki/sources/newsletters/radical-numerics-genomic-lms-biosecurity-2026-09-23.md (new)

```
---
title: 'Latent Space — Bio-security is an AI arms race (Eric Nguyen, Radical Numerics)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-23-bio-security-is-an-ai-arms-race-eric-nguyen-ce.md
url: https://www.latent.space/p/bio-security-is-an-ai-arms-race-eric
published: 2026-09-23
ingested: 2026-10-20
domains: [science]
---

# Latent Space — Bio-security is an AI arms race (Eric Nguyen, Radical Numerics)

Short episode notes with Eric Nguyen (Evo, Evo 2; now Radical Numerics) on genomic language models and biosecurity.

## Influenced pages
- [AI in Science](../../trends/ai-in-science.md) — new genomic language models and biosecurity section

## Key claims extracted
- Evo-family models were used by an Arc/Stanford team to generate whole phage genomes synthesized into functional viruses
- Long-context architectures (StripedHyena) made DNA-scale modeling possible about three years ago
- In-context optimization: shown RNA aptamers ranked by score, the model continues toward better sequences ("chain-of-thought in DNA")
- Nguyen: biosecurity defense is currently losing; the answer is to push the frontier so defense keeps pace
```

## Schema / vocabulary additions

None.

## Open questions

- With these additions AI in Science reaches about 1,600 body words (~133% of its 1,200 ceiling). Split the biology material (Protein world models, Virtual cell models, AI-native drug design, ART, genomic language models) into a new `trends/ai-in-biology.md`, leaving AI in Science as a short hub with self-driving labs and ERA? (Assumed: not in this proposal.)
- Should ERA also get a one-line pointer in [Agent improvement loop](../wiki/concepts/agent-improvement-loop.md) as the "optimize anything scoreable" case? (Assumed no: ERA improves solutions to a problem, not the agent.)
