---
type: proposal
source: raw/newsletters/2026-05-18-claude-mythos-breaks-into-apples-m5.md
status: pending
created: 2026-05-18
---

# Proposal: Claude Mythos defeats Apple M5 Memory Integrity Enforcement

## Summary

A small research team (Calif, Vietnam) used restricted-access Claude Mythos Preview to bypass Apple's Memory Integrity Enforcement (MIE) on M5 silicon in under 5 days — the first public kernel memory corruption exploit on M5 hardware. Human expertise was still essential for the MIE bypass itself; Mythos accelerated bug surfacing dramatically. Anthropic and Calif are co-developing a patch; report was hand-delivered to Apple HQ.

## Intended changes

- [x] **Update** `wiki/models/claude-mythos-preview.md` — update `as_of`, add source to frontmatter, add M5 MIE section, add Recent changes entry
    > **`as_of`:** `2026-05-12` → `2026-05-18`
    >
    > **Sources frontmatter:** add `claude-mythos-m5-bypass-2026-05`
    >
    > **Add new section after `## METR long-horizon benchmark (May 2026)`:**
    >
    > ```md
    > ## Apple M5 MIE bypass (May 2026)
    >
    > - Calif research team (Vietnam) used Mythos Preview to defeat Apple's Memory Integrity Enforcement (MIE) — Apple's strongest-ever hardware security layer, first shipped on M5
    > - Timeline: under 5 days from start to first public kernel memory corruption exploit on M5 silicon
    > - Human expertise was essential for the MIE bypass itself; Mythos's role was surfacing bugs extremely quickly
    > - Access was restricted (non-public Mythos Preview); Calif + Anthropic are co-developing a patch; report delivered in person to Apple Cupertino
    > - Signal: "Apple built MIE in a world before Mythos Preview" — hardware defenses designed before frontier AI may need reassessment
    > - Broader pattern: small teams + frontier AI can now match security research throughput that previously required entire organizations
    > ```
    >
    > **Add to Recent changes (top):**
    > `- [2026-05-18] Apple M5 MIE bypass: Calif team + Mythos Preview defeated Memory Integrity Enforcement in <5 days — first public kernel memory corruption on M5; small team + frontier AI matches org-scale security research throughput`

- [x] **Update** `wiki/state-of/models.md` — update Mythos entry to reflect M5 result
    > **Before:** `- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview model; autonomously identifies zero-days at scale in major OSes and browsers; used in Project Glasswing with partners Cisco, AWS, Microsoft; not publicly available *(as of 2026-04-22)*`
    > **After:** `- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview model; autonomously identifies zero-days at scale; Calif team used it to defeat Apple M5 Memory Integrity Enforcement in <5 days (May 2026); Project Glasswing partners: Cisco, AWS, Microsoft; not publicly available *(as of 2026-05-18)*`

- [x] **Create** `wiki/sources/newsletters/claude-mythos-m5-bypass-2026-05.md`
    > See draft below

## Page drafts

### wiki/sources/newsletters/claude-mythos-m5-bypass-2026-05.md (new)

```md
---
title: Claude Mythos breaks into Apple M5 — newsletter coverage
type: source
source_type: newsletter
source_file: raw/newsletters/2026-05-18-claude-mythos-breaks-into-apples-m5.md
published: 2026-05-18
ingested: 2026-05-18
domains: [models, cybersecurity]
---

# Claude Mythos breaks into Apple M5 — newsletter coverage

Newsletter coverage of the Calif research team's use of Claude Mythos Preview to bypass Apple's Memory Integrity Enforcement (MIE) on M5 silicon. The team — a small group based in Vietnam — defeated Apple's strongest-ever hardware security layer in under 5 days, producing the first public kernel memory corruption exploit on M5 hardware. Human expertise remained essential for the MIE bypass itself; Mythos dramatically accelerated bug surfacing. Mythos access was restricted (non-public preview). Anthropic and Calif are co-developing a patch; the report was hand-delivered to Apple headquarters in Cupertino. Secondary content also covers AI stack fungibility and the "AI psychosis" failure mode from Mitchell Hashimoto.

## Influenced pages

- [Claude Mythos Preview](../../models/claude-mythos-preview.md) — M5 MIE bypass section added
- [State of Models](../../state-of/models.md) — Mythos entry updated
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — stack fungibility + AI psychosis (separate proposal)

## Key claims extracted

- Calif team + Mythos Preview defeated Apple M5 MIE in under 5 days
- First public kernel memory corruption on M5 silicon
- Human expertise still essential for MIE bypass itself
- Access was restricted Mythos Preview (not public)
- Anthropic + Calif co-developing patch; report delivered to Apple Cupertino
- Framing: "Apple built MIE in a world before Mythos Preview"
- Pattern: small teams + frontier AI = org-scale security research throughput
```
