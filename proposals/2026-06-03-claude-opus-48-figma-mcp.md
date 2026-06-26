---
type: proposal
source: raw/newsletters/2026-06-03-opus-48-is-smart-enough-to-get-in-your-way.md
status: pending
created: 2026-06-24
---

# Proposal: Claude Opus 4.8 — Figma MCP + hallucination patterns (Every pulse check)

## Summary

Every published a practitioner pulse check on Claude Opus 4.8. Key findings: Figma MCP enables bidirectional code-to-design and design-to-code workflows; Dynamic Workflows released alongside Opus 4.8; a documented hallucination of a security warning (hallucinated the concern, then hallucinated an explanation for the hallucination); team split on whether 4.8 or GPT-5.5 in Codex is the better daily driver.

## Intended changes

- [x] **Create** `wiki/models/claude-opus-4-8.md` — new model page (version bump from 4.7)
    > See draft below

- [x] **Update** `wiki/models/claude-opus-4-7.md` — add superseded note pointing to 4.8 in Recent changes
    > **Add to Recent changes:**
    > `- [2026-06-03] Superseded by Claude Opus 4.8; see [Claude Opus 4.8](claude-opus-4-8.md)`

- [x] **Update** `wiki/state-of/models.md` — add Claude Opus 4.8 entry (note: current page as_of 2026-06-17 still references 4.7 as the accessible Anthropic flagship; 4.8 should be noted alongside)
    > **In frontier multimodal section, update the Claude Opus 4.7 line to:**
    > `- [Claude Opus 4.8](../models/claude-opus-4-8.md) — Anthropic; current accessible flagship (4.7 superseded); Dynamic Workflows; Figma MCP bidirectional code↔design; hallucination risk on security warnings documented *(as of 2026-06-03)*`
    >
    > **Add to Recent changes:**
    > `- [2026-06-03] Claude Opus 4.8 released with Dynamic Workflows; Figma MCP bidirectional code↔design; documented hallucination pattern: invented security warning, then invented explanation for the invention`

- [x] **Create** `wiki/sources/newsletters/every-opus-48-june-2026.md` — source summary
    > See draft below

## Page drafts

### wiki/models/claude-opus-4-8.md (new)

````md
---
title: Claude Opus 4.8
type: model
domains: [models]
subcategory: frontier-multimodal-model
tags: [anthropic, closed-source]
as_of: 2026-06-03
sources: [every-opus-48-june-2026]
---

# Claude Opus 4.8

Anthropic's current accessible flagship multimodal model. Released June 2026 alongside Dynamic Workflows. Supersedes Claude Opus 4.7 in the accessible tier (Fable 5 and Mythos remain restricted). Early practitioner reports describe it as detail-oriented and reliable for complex tasks, but slower and occasionally prone to hallucinating plausible-sounding security concerns.

## Current status (as of 2026-06-03)

- Released alongside **Dynamic Workflows** (the `ultracode` agent orchestration pattern)
- **Figma MCP bidirectional integration:** code-to-design (live web page → Figma canvas export) and design-to-code (Figma design → agent-generated PR)
- Strengths: detail-oriented, stronger recall in long threads, effective use of 1M context window, complex multi-step coding
- Documented failure mode: **hallucinated security warning** — invented a prompt-injection concern that didn't exist, then invented a plausible explanation for why it had invented the concern (meta-hallucination pattern)
- Practitioner split: some strongly prefer for writing/coding; others keep using GPT-5.5 in Codex for speed and harness integration
- Slower and higher token burn than 4.7 for equivalent tasks

## Strengths

- Complex reasoning and long-context tasks where correctness matters more than speed
- Multi-step coding pipelines benefiting from Dynamic Workflows
- Figma MCP enables design-code loop without context switching

## Weaknesses / caveats

- Security warning hallucination: documented case of Claude inventing a prompt-injection alert, then fabricating a rationale for the alert — a compounding hallucination that's hard to detect
- Higher cost and slower than GPT-5.5 for straightforward tasks
- Figma chat-mode has a "diverge/converge" ceiling on open-ended design (explored but not solved)

## Recent changes

- [2026-06-03] Released; Dynamic Workflows and Figma MCP at launch; hallucination pattern documented; early practitioner pulse check by Every

## Sources

- [Every — Claude Opus 4.8 pulse check (June 3)](../../sources/newsletters/every-opus-48-june-2026.md)
````

### wiki/sources/newsletters/every-opus-48-june-2026.md (new)

````md
---
title: '"Opus 4.8 Is Smart Enough to Get in Your Way" — Every (June 3)'
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-03-opus-48-is-smart-enough-to-get-in-your-way.md
published: 2026-06-03
ingested: 2026-06-24
domains: [models, coding]
---

# "Opus 4.8 Is Smart Enough to Get in Your Way" — Every (June 3)

Every team pulse check on Claude Opus 4.8. Multi-author: Andrey ("more stable, reliable, less dumb" for writing/coding), Lee Knowlton (hallucinated security warning), and others maintaining GPT-5.5/Codex as primary. Covers Figma MCP bidirectional workflow and Dynamic Workflows alongside the model launch.

## Influenced pages

- [Claude Opus 4.8](../../models/claude-opus-4-8.md) — new page

## Key claims extracted

- Claude Opus 4.8 released alongside Dynamic Workflows
- Figma MCP: code-to-design (live page → Figma) + design-to-code (Figma design → agent PR) — bidirectional
- Hallucination pattern: Lee Knowlton — Claude invented a prompt-injection security warning that didn't exist, then invented an explanation for why it had invented the warning
- Strengths: detail-oriented, stronger recall in long threads, effective 1M context use, complex coding
- Weaknesses: slower, higher token burn, Figma chat has "diverge/converge" ceiling for open-ended design
- Team split: Andrey strongly prefers 4.8 for writing/coding; others keep GPT-5.5 in Codex for speed
- Figma: "not worried about SaaSpocalypse" — AI expanded developer base; chat-based design has a ceiling
````

## Open questions

- The state-of/models.md (as_of 2026-06-17) still references "Claude Opus 4.7" as the accessible Anthropic flagship. If 4.8 launched June 3, the June 17 update should have reflected this. Was 4.8 considered a minor update that wasn't tracked separately? Should the 4.7 and 4.8 pages be merged, or is the version distinction meaningful?
	- We need to displace 4.7, archive it. Also, the hallucination problem is general to all LLMs, so noting this security hallucination is not worth its own page. Remove that from these notes, lets keep them about the model capabilities.
