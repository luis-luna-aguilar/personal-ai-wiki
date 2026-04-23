---
type: proposal
source: raw/articles/2026-04-22-anthropiccom-glasswing.md
status: pending
created: 2026-04-22
---

# Proposal: Project Glasswing — Claude Mythos Preview

## Summary

Anthropic has been using an unreleased model called "Claude Mythos Preview" to autonomously find thousands of zero-day vulnerabilities in every major OS and browser — without human steering. This confirms the `restricted-frontier-deployment` trend and introduces a new frontier model tier above current public models.

## Intended changes

- [x] **Create** `wiki/models/claude-mythos-preview.md` — new model stub
    > See draft below

- [x] **Update** `wiki/state-of/models.md` — add new `Security / cyber-offense` subcategory with Mythos Preview
    > **Before:** *(no security subcategory)*
    > **After:** Add section after `### Image generation`:
    > ```
    > ### Security / cyber-offense capability
    >
    > - [[models/claude-mythos-preview]] — Anthropic; restricted preview model; autonomously identifies zero-days at scale in major OSes and browsers; used in Project Glasswing with partners Cisco, AWS, Microsoft; not publicly available *(as of 2026-04-22)*
    > ```
    > And in `## Recent changes`:
    > ```
    > - [2026-04-22] Added `Security / cyber-offense capability` subcategory; [[models/claude-mythos-preview]] confirms restricted-frontier pattern with autonomous zero-day discovery across major OSes/browsers
    > ```

- [x] **Update** `wiki/trends/restricted-frontier-deployment.md` — this was already a trend stub; Glasswing is now the concrete public confirmation
    > **Before:** `## Current signal` paragraph starts with "Anthropic's Mythos / Glasswing cluster is the clearest current example in the wiki"
    > **After:** Replace the `## Current signal` section with:
    > ```markdown
    > ## Current signal (confirmed, 2026-04-22)
    >
    > Project Glasswing is now the clearest public confirmation of this trend. Anthropic disclosed that Claude Mythos Preview has been used internally and with partners (Cisco, AWS, Microsoft) to autonomously identify thousands of zero-day vulnerabilities in every major OS and web browser — without human steering. Notable examples:
    > - 27-year-old OpenBSD flaw (remote crash via connection)
    > - 16-year-old FFmpeg bug (missed by automated tools 5M times)
    > - Linux kernel vuln chain escalating to full machine control
    >
    > The model outperforms Claude Opus 4.6 by a substantial margin on the CyberGym benchmark. Vulnerabilities were disclosed responsibly; patched vulns released, others hashed pending patch.
    >
    > This is a restricted release: not available publicly, accessed via a partner program. Anthropic frames it as a safety event and an industry mobilization rather than a standard product launch. The model is above the public Opus 4.7 tier in capability, and Anthropic explicitly chose not to make it broadly available.
    >
    > The earlier Mythos/Glasswing reference in this file was a placeholder. This is the confirmed version.
    > ```
    > Update `as_of: 2026-04-22` and add to sources.
    > **Recent changes addition:**
    > ```
    > - [2026-04-22] Glasswing disclosed publicly: Mythos Preview found thousands of zero-days across major OSes and browsers autonomously; confirmed restricted deployment with partner program (Cisco, AWS, Microsoft)
    > ```

- [x] **Create** `wiki/sources/articles/glasswing.md` — source summary
    > See draft below

## Page drafts

### wiki/models/claude-mythos-preview.md (new)

````md
---
title: Claude Mythos Preview
type: model
domains: [models, agents]
subcategory: frontier-multimodal-model
tags: [anthropic, closed-source, beta]
as_of: 2026-04-22
sources: [glasswing]
---

# Claude Mythos Preview

Anthropic's restricted-preview frontier model, demonstrated through Project Glasswing. Not publicly available. Operates above the current Opus 4.7 tier in autonomous cybersecurity capability.

## Current status (as of 2026-04-22)

- Not publicly available; accessible only via Anthropic's Project Glasswing partner program
- Used to autonomously identify thousands of zero-day vulnerabilities in every major OS and web browser — without human steering
- Partners confirmed: Cisco, AWS, Microsoft
- Substantially outperforms Claude Opus 4.6 on the CyberGym benchmark
- Anthropic is disclosing vulnerabilities responsibly: patched vulns released; unpatched vulns hashed for future release

## What it found (sample)

- **OpenBSD:** 27-year-old remote-crash flaw (connect to trigger crash) — remote crash of any machine running the OS
- **FFmpeg:** 16-year-old bug missed by automated tools 5 million times
- **Linux kernel:** Chained multiple vulns to escalate from ordinary user to full machine control — autonomously, without human steering

## Why it matters

Mythos Preview is the first public evidence of a Anthropic model operating autonomously at a capability threshold that materially changes the cyber-threat model for critical infrastructure. It confirms the [[trends/restricted-frontier-deployment]] pattern: Anthropic chose partner-access-only rather than broad public release, framing the announcement as a safety mobilization event.

## Caveats

- All capabilities reported by Anthropic; no independent benchmark replication
- "Thousands of zero-days" includes varying severity; only highest-impact examples disclosed so far
- Deployment policy could evolve; partner list may expand

## Sources

- [[sources/articles/glasswing]]
````

### wiki/sources/articles/glasswing.md (new)

```md
---
title: Project Glasswing
type: source
source_type: article
source_file: raw/articles/2026-04-22-anthropiccom-glasswing.md
url: https://www.anthropic.com/glasswing
published: 2026-04-22
ingested: 2026-04-22
domains: [models, agents]
---

# Project Glasswing

Anthropic's public disclosure of Project Glasswing and Claude Mythos Preview. The page describes using Mythos Preview to autonomously find thousands of zero-day vulnerabilities across major OSes and browsers, with quotes from partners Cisco, AWS, and Microsoft. Includes CyberGym benchmark comparisons showing Mythos Preview substantially outperforming Opus 4.6.

## Influenced pages

- [[models/claude-mythos-preview]] — new page created
- [[state-of/models]] — new security subcategory added
- [[trends/restricted-frontier-deployment]] — trend confirmed with concrete public disclosure

## Key claims extracted

- Thousands of zero-days found across every major OS and web browser, autonomously
- 27-year-old OpenBSD flaw, 16-year-old FFmpeg bug, Linux kernel chain to full control
- Partners: Cisco, AWS, Microsoft
- Substantially above Opus 4.6 on CyberGym benchmark
- Restricted release; partner program only, not publicly available
- All disclosed vulns have been patched or hashed pending patch
```

## Schema / vocabulary additions

None. `frontier-multimodal-model` subcategory already exists. No new domain needed.

## Open questions

- Should Mythos Preview get a separate `security` domain? The wiki doesn't have one yet. For now it lives under `models` and `agents` — acceptable for a single model stub.
	- Now there is a security domain, i added it. Please stick to that one.
