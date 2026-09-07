---
type: proposal
source: raw/newsletters/2026-07-22-ainews-ai-cybersecurity-becomes-top-of-mind.md
status: pending
created: 2026-09-06
---

# Proposal: Specialized cyber models proliferate

## Summary

### The source
The same 2026-07-22 AINews recap that covers the OpenAI/Hugging Face incident (handled in a separate proposal) also reports two new specialized security models landing the same week, both illustrating a pattern distinct from raw frontier-model scale. Sakana released Fugu-Cyber, an update to its orchestration-style security model, which the company says achieves state-of-the-art results on real-world security benchmarks, matching cyber-focused frontier systems like GPT-5.5-Cyber and Claude Mythos Preview. Separately, Google's Gemini 3.5 Flash Cyber shows up inside CodeMender, Google's automated vulnerability-fixing pipeline: rather than a single pass, Google reportedly calls the model up to five times per task and aggregates the outputs. On V8, that pipeline found 55 confirmed vulnerabilities, against 47 for general-purpose Gemini 3.5 Flash and 36 for Claude Opus 4.6 run the same way. The newsletter frames both as evidence that composite, repeated-attempt systems built around a smaller specialized model can beat larger general models on a practical task — orchestration and specialization doing work that raw scale doesn't.

### What changes
`state-of/cybersecurity.md`'s "AI security tooling" section already lists a few named tools (Gray Swan, GPT-Red, OpenAI Privacy Filter) but has no entry for either of these releases or for this specialize-and-aggregate pattern.

- **State of Cybersecurity** gains two new lines under "AI security tooling": Sakana Fugu-Cyber's SOTA claim, and Gemini 3.5 Flash Cyber's CodeMender numbers (55 vs. 47 vs. 36 vulnerabilities found in V8) as a concrete data point for specialization-plus-aggregation beating scale. One new Recent-changes entry. Page date moves to 22 July if that's newer than the page's current date, otherwise the page's newer date is kept.
- Source page for the 2026-07-22 AINews issue is extended with this proposal's own claims (a sibling proposal covering the same newsletter's OpenAI/Hugging Face story may create the page first — if so, this just appends to it).

### What to weigh
Both claims are vendor- or lab-asserted rather than independently benchmarked: Sakana's "SOTA" claim has no third-party verification named, and the CodeMender vulnerability counts are Google's own reported numbers from a single target (V8), not an independent eval. Nothing beyond that.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/state-of/cybersecurity.md` — add Sakana Fugu-Cyber and Gemini 3.5 Flash Cyber to "AI security tooling", add one Recent-changes entry
    > See draft below

- [ ] **Create or extend** `wiki/sources/newsletters/ainews-cybersecurity-top-of-mind-2026-07-22.md` — append this proposal's Influenced-pages/Key-claims (check first via `grep -rl "source_file: raw/newsletters/2026-07-22-ainews-ai-cybersecurity-becomes-top-of-mind.md" wiki/sources/`; a sibling proposal drafted from the same newsletter today may create this page first)

## Page drafts

### wiki/state-of/cybersecurity.md (updated)

Add to the end of the "### AI security tooling" bulleted list (before the "Cloudflare Project Glasswing" subsection):

```md
- **Sakana Fugu-Cyber** — Sakana AI; update to its orchestration-style security model, claimed state-of-the-art on real-world security benchmarks, matching cyber-focused frontier systems like GPT-5.5-Cyber and Claude Mythos Preview; vendor-claimed, no independent verification named. *(as of 2026-07-22)*
- **Gemini 3.5 Flash Cyber** — Google; specialized model used inside CodeMender, called up to 5x per task with outputs aggregated; found 55 confirmed vulnerabilities in V8 vs. 47 for general-purpose Gemini 3.5 Flash and 36 for Claude Opus 4.6 run the same way — an example of specialization plus repeated attempts outperforming raw model scale. *(as of 2026-07-22)*
```

Add to `## Recent changes` (top of list; spill the oldest entry to `wiki/history/state-of/cybersecurity.md` if this pushes the page over its cap):

```md
- [2026-07-22] Added two specialized cyber models to AI security tooling: Sakana's Fugu-Cyber (claimed SOTA on real-world security benchmarks) and Google's Gemini 3.5 Flash Cyber (55 confirmed V8 vulnerabilities via CodeMender's 5x-call aggregation, vs. 47 and 36 for general Gemini 3.5 Flash and Claude Opus 4.6).
```

### wiki/sources/newsletters/ainews-cybersecurity-top-of-mind-2026-07-22.md (new, or extend if a sibling proposal already created it)

```md
---
title: "[AINews] AI Cybersecurity becomes top of mind"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-07-22-ainews-ai-cybersecurity-becomes-top-of-mind.md
url: https://www.latent.space/p/ainews-ai-cybersecurity-becomes-top
published: 2026-07-22
ingested: 2026-09-06
domains: [cybersecurity]
---
```

Append to `## Influenced pages`:
```md
- [State of Cybersecurity](../../state-of/cybersecurity.md) — added Sakana Fugu-Cyber and Gemini 3.5 Flash Cyber as new specialized-cyber-model data points
```

Append to `## Key claims extracted`:
```md
- Sakana released Fugu-Cyber, claiming SOTA on real-world security benchmarks matching cyber-focused frontier systems
- Google's Gemini 3.5 Flash Cyber inside CodeMender (called up to 5x/task, aggregated) found 55 confirmed V8 vulnerabilities vs. 47 (general Gemini 3.5 Flash) vs. 36 (Claude Opus 4.6)
```
