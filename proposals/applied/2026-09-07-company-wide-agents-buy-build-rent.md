---
type: proposal
source: raw/newsletters/2026-08-11-agents-for-hire.md
status: pending
created: 2026-09-07
---

# Proposal: Company-wide agents as a buy/build/rent spectrum

## Summary

### The source
Every's Katie Parrott, in the 2026-08-11 "Agents for Hire" issue of Every's Context Window newsletter (re-summarized again, near-verbatim, in Every's 2026-08-16 "The Next Era of Great Work" digest), argues that the sudden wave of "company-wide agent" products isn't really a new software category — it's a spectrum of ownership. Her examples: Shopify's engineering agent River, Stripe's data agent Kai, and Every's own in-development Every Agent. An organization can build the whole agent system itself, rent the underlying machinery someone else built, or simply buy an agent that already lives inside a tool it already uses, like Slack or Notion. Parrott's point is that the real decision isn't whether to adopt a company-wide agent but what to trust it with, how to keep its connections to company systems running after launch, and where to draw the line on what it's allowed to do unsupervised. The piece itself is mostly paywalled — this framing, repeated almost word-for-word in the follow-up digest, is the extent of what's available. There are no additional named case studies or deployment details beyond the three companies cited.

### What changes
[Company-wide AI enablement](../training/company-wide-ai-enablement.md) already tracks a wide set of adoption patterns but has no framing for how an organization chooses *which kind* of company-wide agent to pursue.

- **Company-wide AI enablement** gains one new bullet under Proven patterns naming the buy/build/rent spectrum, with River, Kai, and Every Agent as the named examples, plus the practical decision points (trust, connection upkeep, autonomy boundary) the framing surfaces. Page date moves to 11 August.
- New source page for the "Agents for Hire" newsletter issue.

### What to weigh
The source is thin: a single paywalled newsletter free-preview, confirmed only by a same-content resummary five days later, with no primary reporting or named case studies beyond the three companies already implied by the headline framing. This is a lightweight framing addition, not a facts-driven update — there's little here to independently verify, and the value is mainly in having a named vocabulary (buy/build/rent) for a pattern the page already gestures at elsewhere.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/company-wide-ai-enablement.md` — add buy/build/rent framing bullet to Proven patterns, bump `as_of`, merge sources, add Recent-changes entry
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/agents-for-hire-2026-08-11.md` — source summary

## Page drafts

### wiki/training/company-wide-ai-enablement.md (updated)

```md
---
title: Company-wide AI enablement
type: training
as_of: 2026-08-11
sources: [..., codex-interview-onboarding-2026-08-06, agents-for-hire-2026-08-11]
---
```

New bullet appended to the end of `## Proven patterns` (after the existing "Interview-driven agent-workspace onboarding" bullet):

```md
- **Buy, build, or rent.** The "company-wide agent" moment isn't one product category but a spectrum of ownership: build the whole system in-house, rent the underlying machinery, or buy an agent that already lives inside an existing tool like Slack or Notion (Every's Katie Parrott, citing Shopify's engineering agent River, Stripe's data agent Kai, and Every's own in-progress Every Agent). The harder design question isn't which option to pick but what the agent should be trusted with, how its connections to company systems stay running after launch, and where its autonomous authority ends.
```

New entry prepended to `## Recent changes` (list stays at 9 of 10 entries — no spill needed):

```md
- [2026-08-11] Added buy/build/rent framing for company-wide agents: build in-house, rent the machinery, or buy an agent already living in an existing tool (River, Kai, Every Agent as named examples).
```

New line appended to `## Sources`:

```md
- ["Agents for Hire" — Every](../sources/newsletters/agents-for-hire-2026-08-11.md)
```

### wiki/sources/newsletters/agents-for-hire-2026-08-11.md (new)

```md
---
title: "Agents for Hire" — Every
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-11-agents-for-hire.md
url: https://every.to/context-window/agents-for-hire
published: 2026-08-11
ingested: 2026-09-07
domains: [training]
---

# "Agents for Hire" — Every

Every's Katie Parrott frames the "company-wide agent" trend (Shopify's River, Stripe's Kai, Every's own in-progress Every Agent) as a spectrum of ownership rather than a single product category — build, rent, or buy — with the real design question being what the agent should be trusted with, how its connections stay running, and where its autonomous authority ends. The piece is mostly paywalled; this framing (confirmed again in Every's 2026-08-16 "The Next Era of Great Work" digest) is the extent of the free-preview content, with no additional named case studies beyond the three companies cited.

## Influenced pages
- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — new Proven-patterns bullet on the buy/build/rent spectrum

## Key claims extracted
- Shopify has River (engineering agent), Stripe has Kai (data agent), Every is building Every Agent
- "Company-wide agent" is framed as a spectrum of ownership: build, rent, or buy — not a single category
- The hard design question is what to trust the agent with, keeping its connections running, and drawing a line around its autonomous authority
```

## Open questions
- None.
