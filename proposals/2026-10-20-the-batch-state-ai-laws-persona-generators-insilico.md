---
type: proposal
source: raw/newsletters/2026-04-17-meta-pivots-from-open-weights-big-pharma-bets-on.md
triage: proposals/triage/2026-10-19-raw-orphans-sweep.md
status: pending
created: 2026-10-20
---

# Proposal: The Batch, 17 April 2026 — US state AI laws, Persona Generators, Lilly–Insilico

## Summary

### In short
US AI regulation is being written state by state while the federal government tries to preempt it, and the wiki's governance page has no word on it. The Batch of 17 April counts over 100 state AI laws across 40 states and 1,500+ pending bills, against a December executive order threatening federal funds. The proposal adds that section to AI governance and policy, Google's Persona Generators to AI-simulated human populations, and Lilly's $2.75B Insilico deal to AI in Science, all dated 17 April. Meta's closed-model pivot is skipped as already covered. Hesitation: the source is six months old, so state-law details may have moved since.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
The Batch is DeepLearning.AI's weekly newsletter. Its 17 April 2026 issue ran four stories. The lead, Meta moving from open weights to the closed Muse Spark, is already on the wiki's Muse Spark page and is left out here.

The regulation story, drawing on The New York Times, describes a growing patchwork. More than 40 states are passing their own AI laws, with over 100 already enacted and more than 1,500 bills under consideration. California has the broadest set: catastrophic-risk assessments and incident reporting for advanced model developers, chatbot rules for minors, and watermarking of AI output from August. Colorado's 2024 high-risk-AI law, which takes effect in July, requires anti-discrimination safeguards, though business pressure may soften it. New York will require model makers with over $500M revenue to block bioweapon and autonomous-hacking misuse from January 2027. Minnesota, Ohio and Utah add narrower rules on deepfakes, insurers denying care by AI, and pricing. Against this, President Trump's December executive order threatens to withhold federal funds from states with "onerous" AI laws, and March guidelines sketch a federal framework. The Batch argues the rules should be national.

The research story covers Google's Persona Generators. Prompting an LLM to play a demographic tends to produce average answers. The authors instead used AlphaEvolve, Google's evolutionary code-search system, to evolve the code that writes 25 persona prompts per context, scoring each version on how widely the personas' questionnaire answers spread. The evolved generator covered 82% of possible responses, against 76% for NVIDIA's Nemotron Personas dataset and 46% for a memory-based generator. The pharma story reports Eli Lilly's deal worth up to $2.75B with Insilico Medicine, whose generative pipeline has produced 28 drug candidates, about half in clinical trials. It notes that no AI-discovered drug has yet been approved.

### What changes
The governance page covers economists' calls, the lab-employee pacing letter and disclosure mandates, but nothing on US state or federal law. The simulation page covers only Simile's post-trained digital twins. The science page covers Chai Discovery's pharma deals but not Insilico or clinical failure rates.

- **AI governance and policy** gains a section on the state-law patchwork and the federal preemption push, a What-to-watch item, and a Recent-changes entry dated 17 April. Page date stays 6 September.
- **AI-simulated human populations** gains a bullet on Persona Generators as a third route, between prompting and post-training, and a Recent-changes entry. Page date stays 22 August.
- **AI in Science** gains a short Insilico paragraph in its drug-design section. Its Recent-changes list is at the cap of 10 and the new 17 April entry is older than all of them, so it goes straight to history. Page date stays 11 August.
- Three source pages, one per story.

### What to weigh
Whether six-month-old material is still worth adding. The state laws and the federal order describe a contest that has surely moved since April, so the section is dated so readers can see its age. AI in Science lands at about 107% of its length ceiling after this, which is under the point where a split is needed.

## Intended changes

- [ ] **Update** `wiki/trends/ai-governance-and-policy.md` — new section "US states regulate while Washington pushes preemption (as of 2026-04-17)"; one What-to-watch bullet; adds one Recent-changes entry dated 2026-04-17 at the bottom (3 → 4, under cap); appends one source id and link; `as_of` unchanged (2026-09-06)

- [ ] **Update** `wiki/trends/synthetic-human-simulation.md` — one Current-signal bullet; adds one Recent-changes entry dated 2026-04-17 at the bottom (1 → 2); appends one source id and link; `as_of` unchanged (2026-08-22)

- [ ] **Update** `wiki/trends/ai-in-science.md` — one paragraph appended to "AI-native drug design (Chai Discovery)"; appends one source id and link; `as_of` unchanged (2026-08-11)

- [ ] **Spill** `wiki/trends/ai-in-science.md` → `wiki/history/trends/ai-in-science.md` — the live list is at the cap of 10 and the proposal's one new entry (dated 2026-04-17) is the oldest, so it goes directly to history

- [ ] **Create** `wiki/sources/newsletters/the-batch-us-state-ai-laws-2026-04-17.md`
- [ ] **Create** `wiki/sources/newsletters/the-batch-persona-generators-2026-04-17.md`
- [ ] **Create** `wiki/sources/newsletters/the-batch-lilly-insilico-2026-04-17.md`

## Page drafts

### wiki/trends/ai-governance-and-policy.md (updated)

Frontmatter: append `the-batch-us-state-ai-laws-2026-04-17` to `sources:`; `as_of` stays 2026-09-06.

New section, inserted before `## Why it matters`:

```
## US states regulate while Washington pushes preemption (as of 2026-04-17)

In the US, binding AI rules are arriving state by state rather than nationally. By April 2026, more than 40 states were passing their own laws: over 100 were already enacted and more than 1,500 bills were pending (The New York Times' tally, via The Batch). The rules diverge:

- **California** has the broadest set: catastrophic-risk assessments and serious-incident reporting for advanced model developers, chatbot limits around minors and self-harm, periodic "you are talking to AI" reminders, and mandatory invisible watermarking of AI output from August 2026.
- **Colorado's** 2024 high-risk-AI law (effective July 2026) requires developers and deployers of systems that decide on education, employment, finance, healthcare or housing to guard against algorithmic discrimination, document limitations and training data, and run annual impact assessments, which business pressure may soften.
- **New York** requires model makers with over $500M revenue to block bioweapon and autonomous-hacking misuse, audit that annually and report incidents, starting January 2027.
- **Minnesota, Ohio and Utah** add narrower rules: no AI denial of health-insurance claims without a doctor's review, limits on deepfakes and voice/likeness cloning, and (in Utah) a regulatory sandbox for testing new AI under supervision.

The federal government is pushing the other way. A December 2025 executive order threatens to withhold federal funds from states with "onerous" AI laws and urges Congress to preempt them, and March 2026 guidelines sketch a national framework centred on child protection and data-centre electricity costs. The practical result for builders is that one model can owe a bias audit in Colorado, watermarking in California and incident reporting in New York, while the federal government works to cancel all three.
```

What to watch — appended bullet:

```
- Whether Congress or the courts preempt state AI laws, or the state patchwork (California, Colorado, New York) becomes the de facto US regime
```

Recent changes — adds one entry at the bottom (oldest position):

```
- [2026-04-17] Added the US state-law patchwork (100+ laws in 40 states, 1,500+ bills; California, Colorado, New York rules) and the federal preemption push (December 2025 executive order threatening federal funds).
```

Sources — appended line:

```
- [The Batch — US states move forward with AI laws (17 April 2026)](../sources/newsletters/the-batch-us-state-ai-laws-2026-04-17.md)
```

### wiki/trends/synthetic-human-simulation.md (updated)

Frontmatter: append `the-batch-persona-generators-2026-04-17` to `sources:`; `as_of` stays 2026-08-22.

New bullet in `## Current signal`, inserted before "**The broader pattern:**":

```
- **Google's Persona Generators (April 2026), a third route between prompting and post-training:** instead of prompting a frontier model with demographics (which yields average answers) or post-training on real behavior (Simile), the researchers used AlphaEvolve to evolve the *code that writes persona prompts*, optimizing for how widely 25 personas' questionnaire answers spread along chosen axes such as risk tolerance or institutional trust. On held-out questionnaires the evolved generator covered 82% of possible responses, against 76% for NVIDIA's Nemotron Personas and 46% for a memory-based generator. The goal is coverage of the range, including outliers, not accuracy against any real individual.
```

Recent changes — adds one entry at the bottom:

```
- [2026-04-17] Added Google's Persona Generators: AlphaEvolve-optimized persona-prompt code covering 82% of possible questionnaire responses (Nemotron Personas 76%), a diversity-first alternative to digital twins.
```

Sources — appended line:

```
- [The Batch — Simulating diverse human cohorts (17 April 2026)](../sources/newsletters/the-batch-persona-generators-2026-04-17.md)
```

### wiki/trends/ai-in-science.md (updated)

Frontmatter: append `the-batch-lilly-insilico-2026-04-17` to `sources:`; `as_of` stays 2026-08-11.

Paragraph appended at the end of `## AI-native drug design (Chai Discovery)`:

```
**Pipeline-builder counterpoint (Insilico, as of 2026-04-17):** Eli Lilly agreed to pay Insilico Medicine up to $2.75B ($115M upfront) for rights to undisclosed preclinical drugs. Insilico's generative pipeline has produced 28 candidates, about half in clinical trials, reaching preclinical candidates in about 18 months instead of five to six years after testing 60–200 molecules each; its lead, Rentosertib for lung fibrosis, showed positive Phase 2a results. The caveat: no AI-discovered drug had yet been approved, and AI-designed drugs from BenevolentAI and Recursion have failed in Phase 2 like conventional ones.
```

Recent changes: no change to the live list (see Spill).

Sources — appended line:

```
- [The Batch — Big Pharma bets big on AI (Lilly–Insilico, 17 April 2026)](../sources/newsletters/the-batch-lilly-insilico-2026-04-17.md)
```

### wiki/history/trends/ai-in-science.md (updated)

Appends, under a new `## Archived from current page on <apply date>` header:

```
- [2026-04-17] Added Insilico Medicine's up-to-$2.75B Eli Lilly deal as a pipeline-builder counterpoint to Chai Discovery, with the caveat that no AI-discovered drug has yet been approved.
```

### wiki/sources/newsletters/the-batch-us-state-ai-laws-2026-04-17.md (new)

```
---
title: 'The Batch — US states move forward with AI laws (17 April 2026)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-17-meta-pivots-from-open-weights-big-pharma-bets-on.md
published: 2026-04-17
ingested: 2026-10-20
domains: [models, agents]
---

# The Batch — US states move forward with AI laws (17 April 2026)

DeepLearning.AI's The Batch, drawing on The New York Times, describes a growing patchwork of US state AI laws enacted despite the Trump administration's push for national rules, and argues that requirements should be set at the national level.

## Influenced pages

- [AI governance and policy](../../trends/ai-governance-and-policy.md) — US state-law patchwork and federal preemption section

## Key claims extracted

- More than 40 states are passing AI laws; 100+ laws already enacted by 40 states, 1,500+ bills under consideration
- California: catastrophic-risk assessments and serious-incident reporting for advanced model developers; chatbot limits for minors; watermarking of AI output from August 2026; 30 March executive order on state AI use
- Colorado: 2024 high-risk-AI law effective July 2026 (anti-discrimination, documentation, annual impact assessments), possibly softened under business pressure
- New York: from January 2027, model makers with $500M+ revenue must block bioweapon and autonomous-hacking misuse, audit annually, report incidents
- Minnesota, Ohio, Utah: deepfake, likeness, insurer-denial and pricing rules; Utah regulatory sandbox
- December 2025 executive order threatens federal funds for states with "onerous" AI laws and urges Congress to preempt; March 2026 federal guidelines focus on child protection and data-centre electricity prices
```

### wiki/sources/newsletters/the-batch-persona-generators-2026-04-17.md (new)

```
---
title: 'The Batch — Simulating diverse human cohorts (17 April 2026)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-17-meta-pivots-from-open-weights-big-pharma-bets-on.md
published: 2026-04-17
ingested: 2026-10-20
domains: [agents, models]
---

# The Batch — Simulating diverse human cohorts (17 April 2026)

The Batch summarizes Google's Persona Generators (Paglieri, Cross et al.): AlphaEvolve evolves the code that writes 25 persona prompts per context, optimizing for diversity of questionnaire answers rather than matching one demographic profile.

## Influenced pages

- [AI-simulated human populations](../../trends/synthetic-human-simulation.md) — Persona Generators bullet

## Key claims extracted

- Demographic prompting tends to produce average answers, not the human range
- Gemini 2.5 Pro generated 30 questionnaires (context, diversity axes, 1–5 agreement questions); Gemma 3-27B-IT answered as each persona via the Concordia simulation library
- AlphaEvolve ran 10 code versions in parallel for 500 iterations, maximizing six diversity metrics
- Held-out coverage of possible responses: 82% (Persona Generators) vs 76% (Nemotron Personas) vs 46% (Concordia memory generator)
```

### wiki/sources/newsletters/the-batch-lilly-insilico-2026-04-17.md (new)

```
---
title: 'The Batch — Big Pharma bets big on AI (Lilly–Insilico, 17 April 2026)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-04-17-meta-pivots-from-open-weights-big-pharma-bets-on.md
published: 2026-04-17
ingested: 2026-10-20
domains: [science]
---

# The Batch — Big Pharma bets big on AI (Lilly–Insilico, 17 April 2026)

The Batch reports Eli Lilly's deal worth up to $2.75B with Insilico Medicine and explains Insilico's generative target-finding and molecule-design pipeline, while noting that no AI-discovered drug has yet been approved.

## Influenced pages

- [AI in Science](../../trends/ai-in-science.md) — Insilico paragraph in the AI-native drug design section

## Key claims extracted

- Lilly pays $115M upfront, up to $2.75B with milestones, for exclusive rights to undisclosed preclinical drugs; third Lilly–Insilico agreement
- Insilico: 28 AI-developed candidates, about half in clinical trials; Rentosertib (IPF, TNIK target) positive Phase 2a; Garutadustat (IBD) entered Phase 2a January 2026
- PandaOmics ranks targets; Chemistry42 runs ~30 generative models in parallel; lead molecule after fewer than 80 compounds synthesized
- Target to preclinical candidate in ~18 months vs a typical five to six years, across 20+ programs (60–200 molecules each)
- No AI-discovered drug approved yet; 173 AI-enabled clinical programs as of mid-2025; 70% of Phase 2 candidates fail, including AI-designed ones from BenevolentAI and Recursion
```

## Schema / vocabulary additions

None.

## Open questions

- Is the Insilico paragraph worth adding to AI in Science, which already carries Chai's Lilly deals and sits near its length ceiling (assumed: yes, for the "no approved AI drug yet" caveat)?
