---
type: proposal
source: raw/articles/2026-10-20-openaicom-index-sharing-ai-progress-in-mathematics.md
sources:
  - raw/articles/2026-10-20-openaicom-index-sharing-ai-progress-in-mathematics.md
  - raw/newsletters/2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishe.md
  - raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
triage: proposals/triage/2026-10-01-to-2026-10-10-ai-digest.md
status: pending
created: 2026-10-20
---

# Proposal: OpenAI releases 722 math manuscripts; mathematicians push back

## Summary

### In short
AI mathematics has moved from single headline proofs to bulk output, and checking that output is now the bottleneck. On 6 October OpenAI published 722 manuscripts from an unreleased model, averaging about three hours of ChatGPT Pro compute each, including a claimed "quasi-Riemann hypothesis". Within two days three were withdrawn, 14 revised, and a mathematicians' group urged colleagues to stop working with OpenAI. The proposal adds this to AI in mathematics and updates State of Science, plus three source pages. Hesitation: AI in mathematics would sit at about 112% of its length ceiling.

[[#Open questions|Open questions: 1 to answer.]]

### The source
OpenAI's post "Sharing AI progress in mathematics" (6 October 2026) is short. It says an internal frontier model produced "a broad range of new mathematical results", published in a GitHub repository with protocols for revisions and citations, with Lean formalizations (computer-checked proofs) for many of them, ten summaries of the model's reasoning, and statistics on attempted problems. It says OpenAI consulted the Institute for Advanced Study's independent advisory group on how to release them. An update dated 15 October adds $5 million to a new Simons Foundation initiative to help mathematicians examine and build on AI-produced results. The model remains unreleased.

AINews fills in the scale and the reaction. On 7 October it reported 722 manuscripts in 372 families of related results, drawn from about 4,000 research problems. Commentators singled out a "quasi-Riemann hypothesis" and no-Siegel-zeros results (deep claims about how prime numbers are distributed), integer multiplication faster than n log n, and a uniqueness result for a 3D elastic inverse problem open since 1994. The mathematician Levent Alpöge called it "the most significant moment in mathematical history". About 20% of the results are disproofs or counterexamples. AINews contrasts the cost with OpenAI's September Navier-Stokes claim, which took 88 hours and 10,000 agents. By 8 October the follow-up issue reported three papers withdrawn and 14 revised, a README conceding that unformalized results "could have issues", and a statement from the Association for Human Mathematics urging mathematicians to stop working with OpenAI. Terence Tao reposted it, and it was widely misattributed to him. Outside work had already begun: a 21-page simplified quasi-Riemann proof and Lean-checked improvements on one of the problems.

### What changes
The wiki's AI in mathematics page tracks single results (Erdős, Riemann bound, Fermat formalization, Navier-Stokes) and Tao's "proof indigestion" warning, but nothing at this volume. State of Science still describes OpenAI's model only by the May Erdős disproof.

- **AI in mathematics** gains a bullet under Claimed results for the 722-manuscript release and its fallout, one sentence in Why it matters on review capacity, and two Recent-changes entries (6 and 15 October). Page date moves to 15 October.
- **State of Science** rewrites the OpenAI internal-model line to include the release, adds one Recent-changes entry, and moves the oldest entry (23 April) to history. Page date moves to 15 October.
- Three source pages: OpenAI's post and one per AINews story. The post was saved as a new raw file via the logged-in browser because the normal fetcher hit a block page.

### What to weigh
The specific results (quasi-Riemann, n log n multiplication, the 1994 inverse problem) and the 722/372/4,000 counts come from AINews' summary of commentators and the repository. OpenAI's post doesn't list them, and the repository itself wasn't read. The page length is the other call: the addition is kept short, but the page goes from 101% to about 112% of its ceiling, so a split is offered below.

## Intended changes

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/trends/ai-in-mathematics.md` — new Claimed-results bullet, one Why-it-matters sentence, Current status heading date; adds two Recent-changes entries dated 2026-10-15 and 2026-10-06 (7 → 9, under cap); `as_of` → 2026-10-15; appends three source ids and links

- [ ] **Update** `wiki/state-of/science.md` — replaces the OpenAI internal reasoning model line; adds one Recent-changes entry dated 2026-10-06; `as_of` → 2026-10-15; appends three source ids

- [ ] **Spill** `wiki/state-of/science.md` → `wiki/history/state-of/science.md` — list is at the cap of 10; the oldest entry ([2026-04-23] GPT-5.5 subcategory) moves to history

- [ ] **Create** `wiki/sources/articles/openai-sharing-ai-progress-in-mathematics-2026-10-06.md` — source page for OpenAI's post

- [ ] **Create** `wiki/sources/newsletters/ainews-openai-722-math-manuscripts-2026-10-07.md` — source page for the 7 October release story

- [ ] **Create** `wiki/sources/newsletters/ainews-openai-math-release-pushback-2026-10-08.md` — source page for the 8 October fallout story

## Page drafts

### wiki/trends/ai-in-mathematics.md (updated)

Frontmatter changes:

```
as_of: 2026-10-15
sources: [openai-erdos-unit-distance-2026-05, anthropic-riemann-hypothesis-2026-08-11, every-our-agents-ourselves-2026-08-30, ainews-navier-stokes-2026-09-09, anthropic-flt-formalization-2026-09-09, openai-sharing-ai-progress-in-mathematics-2026-10-06, ainews-openai-722-math-manuscripts-2026-10-07, ainews-openai-math-release-pushback-2026-10-08]
```

Heading change: `## Current status (as of 2026-09-09)` → `## Current status (as of 2026-10-15)`

New last bullet under `### Claimed results`:

```
- **OpenAI publishes 722 manuscripts from an unreleased model (2026-10-06):** a GitHub repository of results in 372 families, from about 4,000 attempted research problems at roughly three hours of ChatGPT Pro compute each, with Lean formalizations for many proofs. Highlights cited by commentators include a "quasi-Riemann hypothesis", integer multiplication faster than n log n, and a 3D elastic inverse problem open since 1994; about 20% are disproofs or counterexamples. Within two days three papers were withdrawn and 14 revised, and the Association for Human Mathematics urged mathematicians to stop working with OpenAI. OpenAI then pledged $5M to a Simons Foundation initiative to help mathematicians examine AI-produced results.
```

Appended to the end of the `## Why it matters` paragraph:

```
The 722-manuscript release (2026-10-06) turns that caveat into a capacity problem: when one release produces hundreds of papers, expert review, not discovery, sets the pace.
```

Recent changes (adds two entries at the top; 7 → 9):

```
- [2026-10-15] OpenAI adds $5M for a Simons Foundation initiative to help mathematicians examine and build on AI-produced results, including its 722-manuscript release.
- [2026-10-06] OpenAI releases 722 math manuscripts from an unreleased internal model (about 3 hours of ChatGPT Pro compute per result); within two days 3 were withdrawn and 14 revised, and the Association for Human Mathematics urged mathematicians to stop working with OpenAI.
```

Sources (appends three lines):

```
- [OpenAI — Sharing AI progress in mathematics](../sources/articles/openai-sharing-ai-progress-in-mathematics-2026-10-06.md)
- [AINews — OpenAI releases 722 math manuscripts](../sources/newsletters/ainews-openai-722-math-manuscripts-2026-10-07.md)
- [AINews — pushback on OpenAI's math release](../sources/newsletters/ainews-openai-math-release-pushback-2026-10-08.md)
```

### wiki/state-of/science.md (updated)

Frontmatter: `as_of: 2026-10-15`; append `openai-sharing-ai-progress-in-mathematics-2026-10-06`, `ainews-openai-722-math-manuscripts-2026-10-07`, `ainews-openai-math-release-pushback-2026-10-08` to `sources:`.

> **Before:** `- **OpenAI internal reasoning model** — OpenAI; unnamed general-purpose reasoning model (not math-specialized or scaffolded) disproved Erdős's 1946 planar unit-distance conjecture; proof verified by external mathematicians (Alon, Gowers, Shankar, Tsimerman) with a companion paper *(as of 2026-05-20)*`

```
- **OpenAI internal reasoning models** — OpenAI; unreleased general-purpose models behind the Erdős unit-distance disproof (May, externally verified) and a 722-manuscript release of research results (October; 3 withdrawn and 14 revised within two days, contested by the Association for Human Mathematics); see [AI in mathematics](../trends/ai-in-mathematics.md) *(as of 2026-10-15)*
```

Recent changes (adds one entry at the top; the oldest entry spills):

```
- [2026-10-06] OpenAI's internal-model line updated for its 722-manuscript math release: about 3 hours of ChatGPT Pro compute per result, 3 papers withdrawn and 14 revised within two days, and a mathematicians' call to stop working with OpenAI.
```

### wiki/history/state-of/science.md (updated)

Appends a new block (or extends a same-day block at apply time):

```
## Archived from current page on <apply date>

- [2026-04-23] Added `Frontier models used in science` with [GPT-5.5](../../models/gpt-5-5.md); OpenAI is now making explicit science-performance claims rather than only general-reasoning claims
```

### wiki/sources/articles/openai-sharing-ai-progress-in-mathematics-2026-10-06.md (new)

```
---
title: OpenAI — Sharing AI progress in mathematics
type: source
source_type: article
source_file: raw/articles/2026-10-20-openaicom-index-sharing-ai-progress-in-mathematics.md
url: https://openai.com/index/sharing-ai-progress-in-mathematics/
published: 2026-10-06
ingested: 2026-10-20
domains: [science]
---

# OpenAI — Sharing AI progress in mathematics

OpenAI's short announcement of a GitHub release of mathematical results from an unreleased internal frontier model. It describes the release format (revision and citation protocols, Lean formalizations for many proofs, ten reasoning summaries, compute estimates and attempt statistics) and says the release followed advice from the Institute for Advanced Study's advisory group. An update dated 15 October adds a $5M contribution to a Simons Foundation initiative for examining AI-produced results.

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — release format, compute, Simons funding
- [State of Science](../../state-of/science.md) — OpenAI internal-model line

## Key claims extracted

- Results from an internal frontier model released in a GitHub repository with protocols for paper revisions and citations
- Lean formalizations for many proofs, with more to follow
- Ten summaries of the model's reasoning, compute estimates in ChatGPT Pro usage, and attempt statistics published
- Average result used the equivalent of roughly three hours of ChatGPT Pro thinking
- Release informed by the IAS Advisory Group on Mathematics and AI
- OpenAI says it is working to responsibly release the model
- Update, 2026-10-15: $5M to a Simons Foundation initiative (workshops, conferences, programs) plus model and compute access for supported researchers
```

### wiki/sources/newsletters/ainews-openai-722-math-manuscripts-2026-10-07.md (new)

```
---
title: AINews — OpenAI releases 722 math manuscripts
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-07-ainews-quasi-riemann-hypothesis-openai-publishe.md
url: https://www.latent.space/p/ainews-quasi-riemann-hypothesis-openai
published: 2026-10-07
ingested: 2026-10-20
domains: [science]
---

# AINews — OpenAI releases 722 math manuscripts

AINews' lead story on OpenAI's release of 722 mathematical manuscripts from an unreleased internal model, with the scale of the effort, the results commentators singled out, early praise, and early skepticism.

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — scale, highlighted results, disproof share
- [State of Science](../../state-of/science.md) — OpenAI internal-model line

## Key claims extracted

- 722 manuscripts in 372 families, from about 4,000 research problems, about 3 hours of ChatGPT Pro compute per result
- Highlighted results (not independently verified): quasi-Riemann hypothesis, no-Siegel-zeros, integer multiplication faster than n log n, 3D elastic inverse-problem uniqueness open since 1994, partial progress near Riemann/Hodge/BSD
- Levent Alpöge: "the most significant moment in mathematical history"; also noted scooping and conflict-of-interest problems
- About 20% of results are disproofs or counterexamples
- Contrast: OpenAI's Navier-Stokes claim took 88 hours and 10,000 agents
- Skepticism: Will Depue expects some results not to survive scrutiny; François Chollet asks whether math/code gains generalize to non-verifiable domains
```

### wiki/sources/newsletters/ainews-openai-math-release-pushback-2026-10-08.md (new)

```
---
title: AINews — pushback on OpenAI's math release
type: source
source_type: newsletter
source_file: raw/newsletters/2026-10-08-ainews-not-much-happened-today.md
url: https://www.latent.space/p/ainews-not-much-happened-today-60f
published: 2026-10-08
ingested: 2026-10-20
domains: [science]
---

# AINews — pushback on OpenAI's math release

AINews' follow-up on the credibility pushback against OpenAI's 722-manuscript release: withdrawals, revisions, the formalization gap, a mathematicians' statement against working with OpenAI, and the first outside follow-on work.

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — withdrawals, AHM statement, verification burden
- [State of Science](../../state-of/science.md) — OpenAI internal-model line

## Key claims extracted

- Three papers withdrawn and 14 revised within two days
- README conceded unformalized results "could have issues"; critics questioned releasing proofs without full Lean checks
- Association for Human Mathematics urged mathematicians to stop working with OpenAI; Terence Tao reposted it and it was widely misattributed to him
- Reddit discussion framed expert review capacity, often unpaid, as the main bottleneck
- Follow-on: Shiva Kintali's 21-page simplified quasi-Riemann proof for c=1/48; outside work on OpenAI problem #109 with kernel-checked Lean certificates
```

## Schema / vocabulary additions

None.

## Open questions

- AI in mathematics would be about 112% of its 1,200-word ceiling after this change. Split it now, for example by moving the "Verification and formalization" section (Tao's proof indigestion, the Fermat formalization, math tooling) to a new `trends/ai-math-verification.md`, or leave it until the next addition?
