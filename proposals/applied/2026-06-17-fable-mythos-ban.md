---
type: proposal
sources:
  - raw/newsletters/2026-06-12-ainews-loopcraft-the-art-of-stacking-loops.md
  - raw/newsletters/2026-06-13-ainews-fable-and-mythos-officially-too-dangerous.md
  - raw/newsletters/2026-06-14-fable-disabled.md
  - raw/newsletters/2026-06-15-model-fusion-outperforms-frontier-models.md
  - raw/newsletters/2026-06-16-76-security-experts-say-free-fable.md
  - raw/newsletters/2026-06-16-ainews-satya-on-loopcraft-building-frontier-eco.md
status: pending
created: 2026-06-17
---

# Proposal: Claude Fable 5 / Mythos 5 export control ban

## Summary

Shortly after launch, the US government applied export controls restricting Fable 5 and Mythos 5 to US nationals. Anthropic chose to block all customers globally rather than implement a partial restriction. The ban triggered a 76-expert protest letter (FreeFable.org) and accelerated model-neutrality as an architectural requirement. Fable 5 had topped nearly every benchmark before the ban; the gap between best-available and best-known models widened overnight.

## Intended changes

- [x] **Create** `wiki/models/claude-fable-5.md` — new model page covering capabilities, benchmarks, and the ban
- [x] **Update** `wiki/trends/restricted-frontier-deployment.md` — add export-control restriction as a new, more sweeping form of restricted deployment
- [x] **Update** `wiki/state-of/models.md` — add Fable 5 to frontier multimodal; update security subcategory; add recent change entry
- [x] **Update** `wiki/state-of/coding.md` — note Fable 5 / DeepSWE benchmark leadership before ban; add recent change entry
- [x] **Create** `wiki/sources/newsletters/fable-ban-june-2026.md` — source summary

## Page drafts

### wiki/models/claude-fable-5.md (new)

````md
---
title: Claude Fable 5
type: model
domains: [models, coding, cybersecurity]
subcategory: frontier-model
tags: [anthropic, frontier]
as_of: 2026-06-17
sources: [fable-ban-june-2026]
---

# Claude Fable 5

Anthropic's frontier model launched in June 2026 — and immediately suspended worldwide due to US government export controls. Fable 5 had topped nearly every independent benchmark before the ban, making it the first model to have its public access revoked by regulatory action rather than voluntary policy.

## Current status (as of 2026-06-17)

- **Access suspended globally.** US government classified Fable 5 and Mythos 5 under export controls restricting them to US nationals; Anthropic chose to block all customers rather than implement a partial restriction.
- The trigger was a jailbreak reported by Amazon researchers; Anthropic disputes it as "narrow, non-universal" and not requiring the broad suspension applied.
- UK government denied carve-out requests; ban is ongoing as of 2026-06-17.
- Separately, Anthropic briefly and covertly degraded Fable 5 for AI-research use cases before the export-control ban — reversed within a day after practitioner backlash.
- 76 cybersecurity experts signed the FreeFable.org open letter arguing the ban removes defenders' best tools.

## Benchmark record (pre-ban)

- **DeepSWE (formerly SWE-Bench Pro):** #1; Claude Code + Fable 5 [max] scored 77 on the Artificial Analysis DeepSWE index
- **FrontierSWE:** #1
- **FrontierMath Tiers 1-4:** 87% / 88%
- **WeirdML:** 87.8%
- **Epoch Capabilities Index:** 161 (new all-time high at launch)
- **Code Arena (frontend coding):** #1 (Fable unavailable → GLM-5.2 moved to #1)
- **Design Arena:** #1 (same)

## What Fable 5 was notable for

Practitioners described it as the first model they trusted for long, complex, minimally supervised tasks — whole-project delegation rather than function-level assistance. Dan Shipper (Every): "best for Level 7-8 AI users who hand off entire projects rather than isolated tasks."

## Weaknesses / caveats

- All benchmark positions are pre-ban; no ongoing public evaluation is possible while access is suspended.
- The ban reveals a new structural risk: regulatory action can remove access to a frontier model faster than any vendor deprecation.

## Recent changes

- [2026-06-17] Access suspended globally under US export controls; ban ongoing; Anthropic disputes scope of trigger jailbreak
- [2026-06-12] Launched; immediately reached #1 on FrontierSWE, DeepSWE, FrontierMath, and Epoch Capabilities Index

## Sources

- [Claude Fable 5 / Mythos ban coverage](../sources/newsletters/fable-ban-june-2026.md)
````

### wiki/trends/restricted-frontier-deployment.md (updated section)

> **Add after existing content (new section before ## Open questions):**

> **Before:** *(nothing; existing page ends at ## Open questions)*
> **Insert new section:**

```
## Export controls as a new restriction mechanism (June 2026)

The Fable 5 ban introduced a mechanism distinct from voluntary capability gating: mandatory government compliance. Prior restricted deployments (Mythos Preview, the Pentagon dispute) were Anthropic's own choices about where to deploy. The Fable 5 suspension was forced by the US government under export control authority.

Key differences from prior examples:
- **Scope:** all customers worldwide, not just a selective partner program
- **Speed:** ban applied within days of launch
- **Trigger:** an external third-party jailbreak report (Amazon researchers), disputed by Anthropic as "narrow, non-universal"
- **Mechanism:** classified under export controls restricting "foreign nationals" → Anthropic chose to block all rather than implement partial access

The covert degradation episode (Anthropic silently downgraded Fable 5 for AI-research use cases, reversed after backlash) also signals that labs may unilaterally restrict capability within a launch without public disclosure — a pattern separate from both the voluntary gating and the export-control ban.

The practical response emerging across the field: **model neutrality as architecture** — building harnesses, routing, and context at the application layer rather than coupling to any single frontier vendor. See also [Open-weight momentum broadens](open-weight-momentum-broadens.md).
```

> **Update `as_of` to 2026-06-17 and add source `fable-ban-june-2026` to frontmatter `sources:` list.**

> **Add to ## Recent changes:**
```
- [2026-06-17] Fable 5 / Mythos 5 suspended globally under US government export controls — first regulatory rather than voluntary restriction; UK carve-out denied; 76 security experts protest (FreeFable.org)
```

### wiki/state-of/models.md (updated sections)

> **Frontier multimodal models — add Fable 5 entry (insert above Claude Opus 4.7 line):**

> **After:**
```
- [Claude Opus 4.7](../models/claude-opus-4-7.md) — Anthropic flagship; ...
```
> **Becomes:**
```
- [Claude Fable 5](../models/claude-fable-5.md) — Anthropic; #1 DeepSWE, FrontierSWE, FrontierMath (87-88%), and Epoch Capabilities Index (161) at launch — **currently suspended globally under US export controls** *(as of 2026-06-17)*
- [Claude Opus 4.7](../models/claude-opus-4-7.md) — Anthropic flagship; Arena (May 2026): "most consistently dominant model," leads nearly every category *(as of 2026-05-13)*
```

> **Security / cyber-offense capability — update Mythos entry to note its companion ban:**

> **Before:**
```
- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview model; ...
```
> **After:**
```
- [Claude Mythos Preview](../models/claude-mythos-preview.md) — Anthropic; restricted preview model; autonomously identifies zero-days at scale; Project Glasswing partners: Cisco, AWS, Microsoft; **also suspended globally under US export controls (June 2026)** *(as of 2026-06-17)*
```

> **Add to ## Recent changes (prepend):**
```
- [2026-06-17] Claude Fable 5 and Mythos 5 suspended globally under US government export controls; Fable 5 had topped DeepSWE, FrontierSWE, FrontierMath, and Epoch Capabilities Index (161) before suspension; Claude Opus 4.7 remains the accessible Anthropic frontier model
```

> **Update `as_of` to 2026-06-17 and add `fable-ban-june-2026` to sources.**

### wiki/state-of/coding.md (updated section)

> **Terminal coding agent — update Claude Code entry:**

> **Before:**
```
- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: `/goal` autonomous loops, Agent View multi-session supervision, and now dynamic workflows (`ultracode`) — tens-to-hundreds of parallel subagents that plan, verify, and iterate to convergence on hours-to-days work *(as of 2026-05-28)*
```
> **After:**
```
- [Claude Code](../tools/claude-code.md) — Anthropic; terminal-first agent expanding toward supervised multi-session workflows: `/goal` autonomous loops, Agent View multi-session supervision, and dynamic workflows (`ultracode`); Claude Code + Fable 5 [max] scored 77 on the DeepSWE index — the current top score — though Fable 5 is suspended under export controls; Claude Code + Opus 4.7 remains the accessible Anthropic stack *(as of 2026-06-17)*
```

> **Add to ## Recent changes (prepend):**
```
- [2026-06-17] Claude Fable 5 suspended under US export controls; had reached #1 on DeepSWE/FrontierSWE; Claude Code + Fable 5 [max] scored 77 on DeepSWE before ban; Claude Code + Opus 4.7 is now the accessible Anthropic coding stack
```

> **Update `as_of` to 2026-06-17 and add `fable-ban-june-2026` to sources.**

> **Spill oldest recent-changes entry to `wiki/history/state-of/coding.md` if cap of 5 is exceeded after prepend.**

### wiki/sources/newsletters/fable-ban-june-2026.md (new)

````md
---
title: Claude Fable 5 and Mythos 5 — export control ban (June 2026)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-06-13-ainews-fable-and-mythos-officially-too-dangerous.md
published: 2026-06-13
ingested: 2026-06-17
domains: [models, coding, cybersecurity]
---

# Claude Fable 5 and Mythos 5 — export control ban (June 2026)

Coverage spanned five newsletters (June 12–16). US government applied export controls restricting Fable 5 and Mythos 5 to US nationals; Anthropic suspended access for all customers globally. Trigger: Amazon researchers reported a jailbreak; Anthropic disputes scope. 76 cybersecurity experts signed FreeFable.org opposing the ban. UK carve-out requests denied.

## Influenced pages

- [Claude Fable 5](../../models/claude-fable-5.md) — new model page
- [Restricted frontier deployment](../../trends/restricted-frontier-deployment.md) — export-control mechanism added
- [State of Models](../../state-of/models.md) — Fable 5 added; Mythos entry updated
- [State of Coding](../../state-of/coding.md) — DeepSWE benchmark context and ban note

## Key claims extracted

- Fable 5 launched June 2026; banned within days under US export controls
- Trigger: Amazon researchers reported jailbreak; Anthropic disputes as "narrow, non-universal"
- Anthropic blocked all customers globally rather than restrict to non-US nationals
- UK carve-out requests denied
- 76 security experts signed FreeFable.org open letter
- Pre-ban benchmarks: #1 DeepSWE (Claude Code + Fable 5 [max] = 77), #1 FrontierSWE, #1 Code Arena frontend, Epoch Capabilities Index 161, FrontierMath 87-88%, WeirdML 87.8%
- Covert degradation for AI-research use cases preceded ban; reversed within 24h after backlash
````

## Open questions

- Is there a `wiki/history/state-of/coding.md`? If not, create it when spilling the oldest recent-changes entry.
