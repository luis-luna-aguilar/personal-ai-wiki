---
type: proposal
source: raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
sources:
  - raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
  - raw/newsletters/2026-11-11-whats-left-for-humans-after-automation.md
  - raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
  - raw/newsletters/2026-09-12-the-rise-of-the-forward-deployed-engineer-and-ho.md
status: pending
created: 2026-11-24
---

# Proposal: Forward-deployed engineering — openings up 4.6x, Ode field evidence, "report to product, not sales"

## Summary

### In short
Engineering demand is shifting from specialist builders to engineers who work inside customers: forward-deployed engineer openings grew 4.6x in a year while front-end roles fell 51% and iOS roles 46%, per TrueUp data relayed by Every. Ode, an Anthropic-backed AI services firm, reports six client deployments with no layoffs, and a former Palantir FDE lead argues the role only works when it reports to product. The proposal adds demand data, field evidence and a test for real FDE roles to the FDE page, plus one labor-market line. Reason to hesitate: the labor-market page reaches about 98% of its length ceiling.

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Four pieces feed this. Every's 13 November Context Window cites TrueUp data: open forward-deployed engineer (FDE) roles grew 4.6x over the past year, while front-end roles fell 51% and iOS roles 46%. Every's reading is that companies hired those specialists partly to split a system no one person could hold in their head; agents can now hold it, so the work left for people is directing agents and working with customers.

At Every's Thesis: 2027 conference, Hugh Wimberly, a staff engineer at Ode (described by Every as "the enterprise AI services firm Anthropic launched with Blackstone and Hellman & Friedman"), said none of his six client projects had led to layoffs. At one business-to-business company, onboarding each new customer took up to about 100 hours of mostly clicking through a UI; an agent cut it to about 30, and cheaper onboarding opened a new customer segment, so the team wants more staff. Some offshore click-work jobs did go, and he notes his clients chose to change. A panel with Anthropic's Jeremy Hadfield (reported 19 November) added that rollouts fail on people, not models: automate the part people dislike first, and expect veterans to adopt once they watch new hires outpace them.

The fourth piece is older but still current: a September Latent Space guest essay by Vinoo Ganesh, CEO of Kepler and formerly at Palantir, where he ran the Project Frontline rotation that turned about 250 software engineers into FDEs. He argues most "FDE" jobs today are sales engineering or consulting under a new name. A real FDE learns a customer's "nouns" (what the business treats as real) and "verbs" (how those things move), then turns the fix into platform capability; keeping one customer happy is the solutions architect's job. Because incentives follow the reporting line, an FDE team should report to product, not sales.

### What changes
The FDE page covers the May hiring race, OpenAI's FDE org and the product-gap argument, but has no demand data and no named delivery outcomes. The labor-market page has junior displacement data but not the specialist-role decline.

- **Forward-deployed engineering** gains a TrueUp status bullet, a "Field evidence from deployments" section (Ode onboarding case, no layoffs, the people-first panel advice), and a "Telling a real FDE role from a relabelled one" section (nouns and verbs, output must be product, report to product). One Recent-changes entry; page date moves to 19 November.
- **AI labor-market effects** gains one bullet on the specialist decline beside FDE growth; page date moves to 13 November.
- Four new source pages, one per newsletter story.

### What to weigh
Every describes Ode's backers as Blackstone and Hellman & Friedman, while the wiki's May entry names an Anthropic joint venture with Blackstone and Goldman Sachs; the drafts quote Every's description and do not claim they are the same venture. The labor-market page lands at about 98% of its 1,200-word ceiling, so its next addition will likely need a split.

## Intended changes

- [ ] **Update** `wiki/training/forward-deployed-engineering.md` — one Current-status bullet; two new sections; add four source ids to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-11-19 (list has 3, no spill); `as_of` 2026-09-29 → 2026-11-19; status heading date → 2026-11-19
- [ ] **Update** `wiki/trends/ai-labor-market-effects.md` — one Current-status bullet; add `every-fde-openings-trueup-2026-11-13` to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-11-13 (list has 6, no spill); `as_of` 2026-10-19 → 2026-11-13; status heading date → 2026-11-13
- [ ] **Update** `wiki/index.md` — refresh the FDE line's description and date and the labor-market line's date
- [ ] **Create** `wiki/sources/newsletters/every-fde-openings-trueup-2026-11-13.md` — story page
- [ ] **Create** `wiki/sources/newsletters/every-ode-field-evidence-2026-11-11.md` — story page
- [ ] **Create** `wiki/sources/newsletters/every-rollouts-fail-on-people-2026-11-19.md` — story page
- [ ] **Create** `wiki/sources/newsletters/latent-space-ganesh-fde-best-practices-2026-09-12.md` — source summary

## Page drafts

### wiki/training/forward-deployed-engineering.md (updated)

Frontmatter: `as_of: 2026-11-19`; append to `sources:` → `every-fde-openings-trueup-2026-11-13, every-ode-field-evidence-2026-11-11, every-rollouts-fail-on-people-2026-11-19, latent-space-ganesh-fde-best-practices-2026-09-12`.

Rename `## Current status (as of 2026-09-29)` to `## Current status (as of 2026-11-19)` and insert as the first bullet:

```
- Open FDE roles grew 4.6x over the year to November 2026 while front-end roles fell 51% and iOS roles 46% (TrueUp data, via Every). Every's reading: specialists were hired partly to split systems no one person could hold; agents now hold them, leaving people to direct agents and work with customers.
```

Insert after `## The product-gap argument` (after its closing paragraph) and before `## Recent changes`:

```
## Field evidence from deployments

- **Ode (November 2026).** Hugh Wimberly, a staff engineer at Ode, which Every describes as the enterprise AI services firm Anthropic launched with Blackstone and Hellman & Friedman, reports no layoffs across six client projects. At one B2B company, onboarding a new customer took up to ~100 hours, mostly clicking through a UI; an agent cut it to ~30, and cheaper onboarding opened a segment that could not previously afford the service, so the team wants more staff. At an accounting client, the direction is agents searching clients' financial records for new opportunities, moving accountants toward advisory work. Some offshore jobs that consisted of repetitive clicking did go, and his clients chose to change rather than having it imposed.
- **Rollouts fail on people, not models.** Wimberly and Anthropic's Jeremy Hadfield (Thesis: 2027): automate the part of the job people dislike first and let them watch it work; at one client, 20-year veterans ignored the assistant until new hires outpaced them with it.

## Telling a real FDE role from a relabelled one

Vinoo Ganesh (Kepler CEO; at Palantir he ran Project Frontline, the rotation about 250 engineers went through to become FDEs) argues the title now covers sales engineers, quota-carrying reps who code, and consultants with a statement of work (September 2026). His test:

- **The FDE collects nouns and verbs.** Nouns are what the business treats as real (a position, a counterparty), defined differently in every company; verbs are how those things move (how a trade gets booked, who signs off on an exception). Almost none of it is written down, and it is learned by watching people work.
- **The output is product, not one happy customer.** Keeping an account happy is the solutions architect's job. An engagement that changes nothing upstream is consulting under a better title; a one-off fix shipped without folding it into the platform becomes something you maintain for years.
- **Report to product, not sales.** Pointed at sales, the incentive is closing the account in front of you; pointed at product, every deployment must leave something the next one can start from.

This agrees with OpenAI's "make yourself unneeded" norm above and with the product-gap argument's view that the lasting asset is the platform, not the engagement.
```

`## Recent changes`: insert at the top:

```
- [2026-11-19] Added role-demand data (FDE openings 4.6x; front-end −51%, iOS −46%), field evidence from Ode (onboarding ~100 → ~30 hours, no layoffs across six clients; rollouts fail on people), and Vinoo Ganesh's test for a real FDE role (nouns and verbs, product output, report to product, not sales).
```

`## Sources`: append

```
- [Every — The engineering job that's up 4.6x](../sources/newsletters/every-fde-openings-trueup-2026-11-13.md)
- [Every — Ode field evidence from Thesis: 2027](../sources/newsletters/every-ode-field-evidence-2026-11-11.md)
- [Every — AI rollouts fail on people, not models](../sources/newsletters/every-rollouts-fail-on-people-2026-11-19.md)
- [Latent Space — The Rise of the Forward Deployed Engineer (Vinoo Ganesh)](../sources/newsletters/latent-space-ganesh-fde-best-practices-2026-09-12.md)
```

### wiki/trends/ai-labor-market-effects.md (updated)

Frontmatter: `as_of: 2026-11-13`; append `every-fde-openings-trueup-2026-11-13` to `sources:`.

Rename `## Current status (as of 2026-10-19)` to `## Current status (as of 2026-11-13)` and insert after the "Anthropic's internal employment report" bullet:

```
- **Specialist engineering roles shrink as customer-facing ones grow.** Over the year to November 2026, open front-end roles fell 51% and iOS roles 46% while [forward-deployed engineer](../training/forward-deployed-engineering.md) openings grew 4.6x (TrueUp data, via Every).
```

`## Recent changes`: insert at the top:

```
- [2026-11-13] Added TrueUp role data: front-end −51%, iOS −46%, forward-deployed engineer openings 4.6x over a year.
```

`## Sources`: append

```
- [Every — The engineering job that's up 4.6x](../sources/newsletters/every-fde-openings-trueup-2026-11-13.md)
```

### wiki/index.md (updated)

Before:

```
- [training/forward-deployed-engineering](training/forward-deployed-engineering.md) — FDE model for deployment and GTM leaders: frontier labs embedding engineers in customers (Anthropic/Blackstone JV, OpenAI Deployment Company, Google, Salesforce), OpenAI's FDE org in practice, and the product-gap counter-thesis (ContextOps, executable coverage) *(as_of: 2026-09-29)*
```

After:

```
- [training/forward-deployed-engineering](training/forward-deployed-engineering.md) — FDE model for deployment and GTM leaders: frontier labs embedding engineers in customers (Anthropic/Blackstone JV, OpenAI Deployment Company, Google, Salesforce), role-demand data, OpenAI's FDE org in practice, Ode field evidence, the product-gap counter-thesis (ContextOps, executable coverage), and how to tell a real FDE role (report to product, not sales) *(as_of: 2026-11-19)*
```

On the `trends/ai-labor-market-effects` line, change `*(as_of: 2026-10-19)*` to `*(as_of: 2026-11-13)*`.

### wiki/sources/newsletters/every-fde-openings-trueup-2026-11-13.md (new)

```
---
title: "The engineering job that's up 4.6x — Every (Your Attention Is AI's New Bottleneck)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-13-your-attention-is-ais-new-bottleneck.md
url: https://every.to/context-window/your-attention-is-ai-s-new-bottleneck
published: 2026-11-13
ingested: 2026-11-24
domains: [agents]
---

# The engineering job that's up 4.6x — Every (Your Attention Is AI's New Bottleneck)

Story page for the data point in Every's 13 November Context Window: TrueUp role data showing forward-deployed engineer openings up and specialist engineering roles down.

## Influenced pages

- [Forward-deployed engineering (FDE)](../../training/forward-deployed-engineering.md) — role-demand status bullet
- [AI labor-market effects](../../trends/ai-labor-market-effects.md) — specialist-role decline

## Key claims extracted

- Open forward-deployed engineer roles grew 4.6x over the past year (TrueUp data)
- Front-end roles fell 51% and iOS roles 46% over the same period
- Every's reading: specialists split systems no one person could hold; agents now can, leaving directing agents and working with customers
```

### wiki/sources/newsletters/every-ode-field-evidence-2026-11-11.md (new)

```
---
title: "Ode field evidence from Thesis: 2027 — Every (What's Left for Humans After Automation)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-11-whats-left-for-humans-after-automation.md
url: https://every.to/context-window/what-s-left-for-humans-after-automation
published: 2026-11-11
ingested: 2026-11-24
domains: [agents]
---

# Ode field evidence from Thesis: 2027 — Every (What's Left for Humans After Automation)

Story page for the backstage section of Every's 11 November Context Window: Ode staff engineer Hugh Wimberly on what his client deployments did to jobs.

## Influenced pages

- [Forward-deployed engineering (FDE)](../../training/forward-deployed-engineering.md) — Ode field evidence

## Key claims extracted

- Every describes Ode as "the enterprise AI services firm Anthropic launched with Blackstone and Hellman & Friedman"
- Six client projects, no layoffs
- B2B onboarding: up to ~100 hours per customer, mostly UI clicking, cut to ~30; team three times as productive and wants more staff because a new customer segment opened
- Accounting client exploring agents that search clients' records for new opportunities, moving accountants toward advisory work
- Some offshore repetitive-clicking jobs went away; client teams chose the change
```

### wiki/sources/newsletters/every-rollouts-fail-on-people-2026-11-19.md (new)

```
---
title: "AI rollouts fail on people, not models — Every (What We Let Our Agents Buy)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-11-19-what-we-let-our-agents-buy.md
url: https://every.to/context-window/what-we-let-our-agents-buy
published: 2026-11-19
ingested: 2026-11-24
domains: [agents]
---

# AI rollouts fail on people, not models — Every (What We Let Our Agents Buy)

Story page for the Thesis: 2027 panel item in Every's 19 November Context Window (Ode's Hugh Wimberly, Anthropic's Jeremy Hadfield, Every's Willie Williams).

## Influenced pages

- [Forward-deployed engineering (FDE)](../../training/forward-deployed-engineering.md) — "rollouts fail on people" bullet

## Key claims extracted

- Getting teams to change how they work is a bigger obstacle than model capability
- Hadfield: Bun's 1M lines were rewritten in Rust "fully autonomously in about a week", then a few weeks of verification
- Wimberly: automate the part of the job people don't like first, then let them see it work
- At one Ode client, 20-year veterans ignored the assistant until they watched new hires outpace them with it
```

### wiki/sources/newsletters/latent-space-ganesh-fde-best-practices-2026-09-12.md (new)

```
---
title: "The Rise of the Forward Deployed Engineer — and How To Do the Job Right (Vinoo Ganesh, Latent Space)"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-12-the-rise-of-the-forward-deployed-engineer-and-ho.md
url: https://www.latent.space/p/forward-deployed-engineer-best-practices
published: 2026-09-12
ingested: 2026-11-24
domains: [agents]
---

# The Rise of the Forward Deployed Engineer — and How To Do the Job Right (Vinoo Ganesh, Latent Space)

Guest essay by Kepler CEO Vinoo Ganesh (ex-Palantir, ex-Citadel) arguing that most jobs now titled "forward deployed engineer" are sales engineering or consulting, and that a real FDE function learns a customer's operating model and turns it into platform capability, which requires it to report to product.

## Influenced pages

- [Forward-deployed engineering (FDE)](../../training/forward-deployed-engineering.md) — "Telling a real FDE role from a relabelled one"

## Key claims extracted

- Ganesh led Palantir's Project Frontline, which turned about 250 software engineers into FDEs
- FDE titles now cover sales engineers, coding sales reps and consultants with a statement of work
- An FDE collects "nouns" (what the business treats as real) and "verbs" (how those things move); almost none is written down
- The output must be product; keeping one customer happy is the solutions architect's job; unshipped one-off fixes become long-lived maintenance ("vinoo.groovy")
- The reporting line sets incentives: point FDEs at product, not sales
- The moat is accumulated, current, verified understanding of how firms in a vertical operate, held in a platform
```

## Schema / vocabulary additions

None.

## Open questions

None.
