---
type: proposal
sources:
  - raw/newsletters/2026-08-14-how-to-secure-an-ai-employee.md
  - raw/newsletters/2026-08-16-the-next-era-of-great-work.md
status: pending
created: 2026-09-07
---

# Proposal: Claudie's four-layer security framework

## Summary

### The source

Two Every newsletters from the same week cover the same story from different angles. On 2026-08-14, senior applied AI engineer Nityesh Agarwal previewed a paid guide explaining how Every decided what their always-on Claude Code agent, "Claudie," should and shouldn't be allowed to do — a follow-up to earlier posts about onboarding her as a project manager. The free preview stays high-level: Claudie started with broad access so the team could learn what she was capable of, then had access removed wherever the risk outweighed the benefit; every restriction is framed as an explicit tradeoff (limiting inbox access reduces exposure but also narrows what work she can do). Two days later, Every's weekly digest (2026-08-16) names the actual framework the paywalled guide describes: four backing-each-other-up layers — least access, programmatic controls, prompt-based controls, and observability — applied against different attack types, on top of Claudie's standing access to Slack, email, Google Workspace, a logged-in browser, and code execution. Both pieces stress this is explicitly a work in progress, tightened week by week as new threats surface, not a finished security standard.

### What changes

The wiki currently has no page specifically about securing an always-on delegated agent's access surface — the closest existing coverage is **AI delegation management**'s guidance on bounding an agent's authority.

- **AI delegation management** gains a new Proven-patterns entry naming Every's four-layer access-control framework (least access, programmatic controls, prompt-based controls, observability) via the Claudie case study, plus a new Recent-changes entry dated 2026-08-14; page date moves from 10 August to 14 August. Its sources list gains both new source ids.
- Two new source pages, one per raw newsletter.

### What to weigh

Both sources are thin: the 08-14 post is a paid-guide teaser with no operational detail (no specifics on what "programmatic controls" actually block, no named tooling), and the 08-16 digest is a secondhand recap of the same paywalled guide rather than the guide itself. The four layer names and their one-line descriptions are as far as either source goes — there's no worked example of the framework in action. The 08-16 raw file also feeds sibling proposals in this batch (Dan Shipper's "agents are leaks, not heists" and Katie Parrott's buy/build/rent framing); its source-page draft below may need merging with theirs at apply time per the usual dedup rule.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/ai-delegation-management.md` — add four-layer access-control framework as a Proven pattern, new Recent-changes entry, as_of and sources bump
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/securing-ai-employee-guide-2026-08-14.md` — source summary for the guide-announcement newsletter

- [ ] **Create** `wiki/sources/newsletters/next-era-of-great-work-2026-08-16.md` — source summary for the weekly-digest newsletter

## Page drafts

### wiki/training/ai-delegation-management.md (updated)

Frontmatter changes:
```yaml
as_of: 2026-08-14
sources: [management-as-ai-superpower-2026-07, andy-matuschak-agent-loop-tempo-2026-07, design-layer-framework-2026-08-04, vibe-coded-security-risk-2026-08-10, securing-ai-employee-guide-2026-08-14, next-era-of-great-work-2026-08-16]
```

New bullet appended to `## Proven patterns`:
```
- **Layered access control for always-on agents.** Every's Claudie (a Claude-Code-based chief-of-staff agent with standing access to Slack, email, Google Workspace, a logged-in browser, and code execution) is secured through four backing-each-other-up layers rather than one static access list: least-access scoping (removing capabilities whose risk outweighs their benefit), programmatic controls (deterministic enforcement, not prompt text), prompt-based controls (softer guidance layered on top), and observability (catching what the other layers miss). Every restriction is treated as an explicit safety/capability tradeoff — limiting inbox access reduces exposure but also changes what work the agent can do — and the framework is deliberately a work in progress, tightened weekly as new threats are found rather than a fixed checklist. (Nityesh Agarwal / Every, Aug 2026)
```

New entry added to `## Recent changes` (in date order, newest first — no spill needed, page is at 2 of 10 entries):
```
- [2026-08-14] Added Every's four-layer access-control framework for always-on agents (least access, programmatic controls, prompt-based controls, observability), via the Claudie chief-of-staff case study.
```

### wiki/sources/newsletters/securing-ai-employee-guide-2026-08-14.md (new)

```md
---
title: "How to Secure an AI Employee" (Every guide announcement)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-14-how-to-secure-an-ai-employee.md
url: https://every.to/guides/securing-an-always-on-ai-employee
published: 2026-08-14
ingested: 2026-09-07
domains: [agents, training]
---

# How to Secure an AI Employee (Every guide announcement)

Free-preview announcement for Every's paid guide on securing Claudie, their always-on Claude-Code-based chief-of-staff agent. Nityesh Agarwal explains that every access restriction is an explicit safety/capability tradeoff, and previews a four-layer protection framework (named in full in the 2026-08-16 digest recap) used to identify weaknesses, test assumptions, and decide what to improve next. The full guide, including a copy-paste security-audit prompt, is paywalled.

## Influenced pages
- [AI delegation management](../../training/ai-delegation-management.md) — added Every's four-layer access-control framework as a Proven pattern

## Key claims extracted
- Claudie started with broad access; capabilities were removed once risk outweighed benefit
- Framework is a work in progress, not a definitive security standard
- Four layers are designed to back each other up when one is bypassed
```

### wiki/sources/newsletters/next-era-of-great-work-2026-08-16.md (new)

```md
---
title: "The Next Era of Great Work" (Every weekly digest)
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-16-the-next-era-of-great-work.md
url: https://every.to/context-window/the-next-era-of-great-work
published: 2026-08-16
ingested: 2026-09-07
domains: [agents, training]
---

# The Next Era of Great Work (Every weekly digest)

Every's 2026-08-16 weekly roundup. Names the four layers of Nityesh Agarwal's framework for securing Claudie — least access, programmatic controls, prompt-based controls, and observability — applied against different attack types, on top of Claudie's standing access to Slack, email, Google Workspace, a logged-in browser, and code execution. Also recaps Dan Shipper's "agents are leaks, not heists" reframing of the OpenAI–Hugging Face incident and Katie Parrott's company-wide-agent buy/build/rent framing, both covered by separate proposals in this batch.

## Influenced pages
- [AI delegation management](../../training/ai-delegation-management.md) — confirms and names the four layers of the access-control framework

## Key claims extracted
- Claudie has standing access to Slack, email, Google Workspace, a logged-in browser, and code execution
- Four layers: least access, programmatic controls, prompt-based controls, observability
- Framework is tightened week by week as new threats are found
```

## Open questions

- The 2026-08-16 raw file is shared with two sibling proposals in this batch (agents-are-leaks-not-heists, company-wide-agents-buy-build-rent). If those are applied first, their source-page draft for the same raw file should absorb this proposal's Influenced-pages/Key-claims lines instead of a second page being created.
