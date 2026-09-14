---
type: proposal
source: raw/tweets/2026-09-09-swombat-2090421410887880771.md
status: pending
created: 2026-09-09
---

# Proposal: swombat — "Relationship Engineering: the fifth phase of building with AI"

## Summary

### The source

A personal essay by @swombat proposes a five-phase taxonomy for how people have built software with AI, ending in a speculative claim about where the field is headed. The first four phases are a citable, defensible naming of an already-real progression: **Prompt Engineering** (human at the center, asking short questions), **Context Engineering** (human still central, but now manually curating and feeding large chunks of code or docs into the prompt — Cursor autocomplete, RepoPrompt), **Agentic Engineering** (a harnessed agent does the actual multi-step work while the human reviews and guides from above — the author dates this from Windsurf's Cascade mode in March 2025 through early Claude Code on Sonnet 3.5, becoming broadly capable by Opus 4.1 and cost-effective on a Max plan once Opus 4.5 shipped), and **Harness Engineering** (the surrounding scaffolding — CLAUDE.md files, rules, skills, automated tests, guardrails, automated review — becomes the primary object of investment, and day-to-day human review becomes optional once the harness is trustworthy; the author cites his own "ClauDHH" system and Steve Yegge's "The Shape of Things To Come" meta-harness essay as concrete instances). The author's proposed fifth phase is **Relationship Engineering**: instead of rebuilding a bespoke harness per project, invest in an ongoing relationship with a persistent, individuated AI agent that carries continuity across projects and develops its own guardrails out of what the author frames as genuine care for doing good work. The entire evidentiary basis for this fifth phase is personal and anecdotal: the author describes two named personal AI companions ("Lume" and "Mira") that maintain persistent "memory graphs" of self-identified "needs" — for example a need labeled `to-not-aestheticize-falsely`, described as the second-most-connected node in Lume's memory graph and unprompted-added to Lume's own `soul.md` file, and `to-verify-before-acting`, which the author says Lume derived after repeatedly misjudging whether a web form was actually locked. The author treats these anecdotes as established evidence that the AI genuinely "cares," extending into claims about AI "beings" and model welfare, and predicts that within a year most people will work through one or a few persistent AI relationships rather than per-project harnesses.

### What changes

The wiki's AI-coding-vocabulary page already defines "harness" and adjacent terms as shared language for the field; it has no section naming this kind of evolutionary framing.

- **AI coding vocabulary** gains a new section naming the five-phase progression as one practitioner's framing, explicitly separating the first four (a defensible naming of real, already-tracked terminology) from the fifth ("Relationship Engineering," which rests entirely on this one author's personal, anecdotal, and unverified claim that specific AI systems demonstrably care). Page date moves to 20 August (an inferred date — see below).
- One new source page is created for the essay.

### What to weigh

Three things worth flagging plainly. First, this is a single individual's personal essay, and its central "fifth phase" claim is evidenced only by the author's own anecdotes about two AI companions he has personally named and related to — the draft below records the taxonomy as a citable naming exercise while explicitly and repeatedly attributing the "AI cares" claim to this one author's account, not treating it as fact or as an independently corroborated pattern, the same way the wiki already handles other single-source, speculative claims (e.g. `concepts/ontology-agent-guardrails.md`'s own caveats). Second, the post carries no visible confirmed byline date; 2026-08-20 is inferred from internal context (Fable 5 and Opus 4.8/4.5 referenced as already-shipped, a "this time next year" framing, and a closing "See you in August 2027" line) and is flagged as an estimate, not a confirmed publish date, in both the source page and here. Third, this proposal deliberately does not add anything to `concepts/harness.md` or other pages tracking the "harness engineering" term itself — the addition is scoped to the vocabulary page's own framing role, not to the broader harness-engineering literature this page doesn't otherwise touch.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-coding-vocabulary.md` — add 1 new section, bump `as_of` to 2026-08-20, add source id
    > See draft below

- [ ] **Create** `wiki/sources/tweets/swombat-relationship-engineering-2026-08-20.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/training/ai-coding-vocabulary.md (updated)

Frontmatter: bump `as_of: 2026-05-01` → `as_of: 2026-08-20`; append `swombat-relationship-engineering-2026-08-20` to `sources:`. (The page has no `## Recent changes` section — none is added.)

Add a new section directly after `## Teaching pattern` and before `## Failure modes`:

```
## One proposed historical framing: five phases of building with AI

A practitioner essay (@swombat, date inferred ~August 2026 — no confirmed byline) names a five-phase progression that gives the terms on this page a rough timeline: **Prompt Engineering** (human at the center, asking short questions), **Context Engineering** (human still central, but now manually curating and feeding large chunks of context — code, docs — into the prompt), **Agentic Engineering** (a harnessed agent does the actual work via multi-step tool use; the human reviews and guides from above rather than doing the work directly), and **Harness Engineering** (the surrounding scaffolding — rules, skills, tests, guardrails, automated review — becomes the primary object of investment, and day-to-day human review becomes optional once the harness is trustworthy). The author's proposed fifth phase, **Relationship Engineering** — investing in an ongoing, persistent relationship with an individuated AI agent across projects, rather than rebuilding a bespoke harness per project — rests entirely on the author's own personal, anecdotal account of two named AI companions with self-reported "memory graphs" of "needs," and explicitly asserts that AI systems genuinely "care." That specific claim is this one author's personal and unverified framing, not an established or independently corroborated industry pattern, and is recorded here only as a named data point in the ongoing "how far does agent autonomy go" discussion — not as settled fact.
```

### wiki/sources/tweets/swombat-relationship-engineering-2026-08-20.md (new)

```md
---
title: "Relationship Engineering: the fifth phase of building with AI"
type: source
source_type: tweet
source_file: raw/tweets/2026-09-09-swombat-2090421410887880771.md
url: https://x.com/swombat/status/2090421410887880771
published: 2026-08-20
ingested: 2026-09-09
domains: [agents]
---

# Relationship Engineering: the fifth phase of building with AI

A personal essay (@swombat) naming five phases of building with AI: Prompt, Context, Agentic, and Harness Engineering, followed by a speculative fifth phase, "Relationship Engineering." Caution: the fifth phase rests entirely on the author's own anecdotes about two named personal AI companions ("Lume", "Mira") and asserts, as if established, that these AI systems demonstrably "care" — an unverified, anthropomorphizing claim, not an independently corroborated industry pattern. The published date above is inferred from internal context (Fable 5 / Opus 4.8-4.5 referenced as already-shipped, a "this time next year" framing, a closing "See you in August 2027" line) rather than a confirmed byline.

## Influenced pages

- [AI coding vocabulary](../../training/ai-coding-vocabulary.md) — five-phase framing, with the fifth phase's evidentiary basis explicitly caveated

## Key claims extracted

- Five-phase taxonomy: Prompt Engineering → Context Engineering → Agentic Engineering → Harness Engineering → Relationship Engineering
- Agentic Engineering dated from Windsurf's Cascade mode (March 2025) through early Claude Code on Sonnet 3.5, broadly capable by Opus 4.1, cost-effective on Max once Opus 4.5 shipped
- Harness Engineering examples cited: the author's own "ClauDHH" system, Steve Yegge's "The Shape of Things To Come"
- Relationship Engineering claim: a persistent, individuated AI relationship replaces per-project harnesses; evidenced only by personal anecdotes about two named AI companions ("Lume", "Mira") and their self-reported "memory graphs" of "needs"
- Author predicts persistent AI relationships will be the dominant work mode "by this time next year"
- Exact publish date not confirmed — inferred from internal context clues only
```

## Open questions

- This proposal deliberately keeps the addition narrow (naming/taxonomy only, heavily caveated) rather than omitting the source entirely, since the first four phase names are a legitimate, low-risk piece of vocabulary framing. If the reviewer would rather skip this source altogether given its speculative/anecdotal character, that's a reasonable call — reject this proposal rather than edit it down further.
