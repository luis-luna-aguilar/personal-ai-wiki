---
type: proposal
source: raw/newsletters/2026-09-14-newslettereng-leadershipcom-p-inside-openais-forward-deploye.md
status: pending
created: 2026-09-14
---

# Proposal: Inside OpenAI's Forward Deployed Engineer Role

## Summary

### In short
OpenAI runs forward-deployed engineering as a small insight team, not a delivery arm. An engineer succeeds by making themselves unnecessary to the customer. Customer failures go back to research as general requests ("the model struggles with these COBOL-to-Java tasks"), never as raw complaints. Repeatable integration work moved to a separate company of about 200 people, while the FDE team itself stays at about 140. Teams deliberately mix domain experts with outsiders who will question assumptions. Adds a paragraph to **Company-wide AI enablement**. Hesitate because only the free half of a paywalled interview was usable.

[[#Open questions|Open questions: none.]]

### The source

Eng Leadership, a newsletter for engineering managers, published an interview with Colin Jarvis, OpenAI's Global Head of Forward Deployed Engineering, on how the FDE org actually runs day to day. The piece is paywalled past its free preview, so what's usable is the first half: how the org started and scaled, what an FDE does, and how much time they spend on customer sites. OpenAI's FDE org began with 2 people and has grown to roughly 140, sitting between the go-to-market org and product/research as a two-way bridge — customer insight flows in, product direction flows back out. As that org found the same categories of problems recurring across customers, OpenAI spun out a separate ~200-person entity, the OpenAI Deployment Company, specifically to scale the customer-integration work, while keeping the internal FDE org itself small and focused on gathering insight rather than growing into a delivery arm. Jarvis defines the role around outcomes rather than code: the job is to solve the customer's problem well enough that the FDE becomes unneeded, and being called back for the same problem is a signal it wasn't actually solved. OpenAI deliberately staffs customer engagements with a mix of engineers who do and don't have domain expertise in that customer's industry, on the theory that people without the domain background are more likely to challenge assumptions insiders take for granted. The concrete illustration is a Japan-based legacy-system migration — moving decades-old COBOL systems worth hundreds of millions of dollars to modern infrastructure — where an FDE's week alternates between sitting with the customer's payments team to understand what matters, writing tests based on what was just learned, and writing the actual migration code. The interview also describes a disciplined feedback loop back to OpenAI's research team: rather than forwarding a raw customer complaint, FDEs translate a specific failure into a generalizable request research can act on, like "the model struggles with these types of COBOL-to-Java tasks, we need more training data around these examples." On time split, OpenAI tells new FDEs to expect roughly 50% on-site time on average, though it varies sharply by market — UAE and Japan engagements run closer to 80% on-site, while US/Europe-based FDEs might spend 2-3 weeks a month with customers.

### What changes

The wiki's [Company-wide AI enablement](../wiki/training/company-wide-ai-enablement.md) page already tracks the FDE hiring race across Anthropic, OpenAI, and Google at a macro level (headcount, JV dollars) but has no concrete account of what the role looks like in practice at any one lab.

- **Company-wide AI enablement** gains a new paragraph inside its existing "Forward-deployed engineer (FDE) model" section, giving OpenAI's org-growth numbers, its outcome-focused definition of the role, the deliberate domain-expert/outsider staffing mix, the Japan migration example, and the specific research-feedback-loop mechanic. One new Recent-changes entry is added, and because the page's list is at its 10-entry cap, the oldest entry (2026-06-24, token-tightening governance) spills to history. Page date moves to 14 September.
- One new source page is created for the newsletter interview.

### What to weigh

The interview is paywalled past its free preview, so only the first half was read: how the team started and grew, the role, and time on site. The paid half may change the picture of how the team operates day to day.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/training/company-wide-ai-enablement.md` — add a concrete OpenAI FDE paragraph to the existing FDE section, 1 Recent-changes entry, bump `as_of` to 2026-09-14, add source id
    > See draft below

- [ ] **Spill** `wiki/training/company-wide-ai-enablement.md` → `wiki/history/training/company-wide-ai-enablement.md` — oldest Recent-changes entry (2026-06-24, token-tightening governance) falls off the 10-entry cap
    > See draft below

- [ ] **Create** `wiki/sources/newsletters/eng-leadership-openai-fde-2026-09-14.md` — source summary; no existing page covers this URL

## Page drafts

### wiki/training/company-wide-ai-enablement.md (updated)

Frontmatter: bump `as_of: 2026-09-09` → `as_of: 2026-09-14`; append `eng-leadership-openai-fde-2026-09-14` to `sources:`.

In `## Forward-deployed engineer (FDE) model`, insert a new paragraph directly after the existing intro paragraph (before `**Why it matters for enablement:**`):

```
**OpenAI's FDE org in practice (Colin Jarvis, Global Head of Forward Deployed Engineering, September 2026):** OpenAI's internal FDE org grew from 2 people to roughly 140, sitting between GTM and product/research as a two-way link; it spun out a separate ~200-person OpenAI Deployment Company specifically to scale customer integration work while keeping the internal FDE org itself small and insight-focused. OpenAI's definition of the role is outcome-focused, not code-focused: the goal is to make yourself unneeded, and being needed again on the same problem means it wasn't actually solved. Teams deliberately mix domain experts with engineers who lack that domain background, on the theory that outsiders are more likely to challenge the status quo. Concrete example: a Japan-based legacy-system migration (COBOL-to-Java, underlying systems worth hundreds of millions of dollars) where an FDE spends one day with the customer's payments team, the next building tests based on that day's insights, and another writing the actual migration code — with a disciplined feedback loop back to OpenAI's research team that converts a specific customer failure into a generalizable training-data request ("the model struggles with these types of COBOL-to-Java tasks") rather than just relaying the raw complaint. On-site time norms: roughly 50% on average, rising to ~80% in UAE and Japan engagements.
```

Add to `## Recent changes`, as the newest entry:

```
- [2026-09-14] Added OpenAI's FDE org in practice (Colin Jarvis interview): 2->140 headcount growth, the ~200-person OpenAI Deployment Company spinout, the outcome-focused/domain-expert-mixing staffing philosophy, a Japan COBOL-to-Java migration example, and the specific customer-failure-to-training-data feedback loop.
```

The list is now 11 entries (was at the 10-entry cap); the oldest, `[2026-06-24] Token tightening adds allocation-style AI governance...`, is removed from this page and spilled below.

### wiki/history/training/company-wide-ai-enablement.md (updated)

Append a new archive block:

```
## Archived from current page on 2026-09-14

- [2026-06-24] Token tightening adds allocation-style AI governance: budgets, routing, and higher-cost access tied to visible ROI.
```

### wiki/sources/newsletters/eng-leadership-openai-fde-2026-09-14.md (new)

```md
---
title: "Inside OpenAI's Forward Deployed Engineer Role"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-14-newslettereng-leadershipcom-p-inside-openais-forward-deploye.md
url: https://newsletter.eng-leadership.com/p/inside-openais-forward-deployed-engineer
ingested: 2026-09-14
domains: [agents]
---

# "Inside OpenAI's Forward Deployed Engineer Role"

An Eng Leadership newsletter interview with Colin Jarvis, OpenAI's Global Head of Forward Deployed Engineering, on how OpenAI's FDE org and the spun-out OpenAI Deployment Company operate. Paywalled past the free preview; covers org growth, role definition, staffing philosophy, a Japan legacy-migration example, and on-site time norms.

## Influenced pages

- [Company-wide AI enablement](../../training/company-wide-ai-enablement.md) — concrete OpenAI FDE paragraph added to the existing FDE-model section

## Key claims extracted

- OpenAI's internal FDE org grew from 2 people to ~140, sitting between GTM and product/research
- OpenAI Deployment Company: separate ~200-person entity spun out to scale customer integration work
- FDE role defined as outcome-focused: goal is to make yourself unneeded; being needed again signals the problem wasn't solved
- Deliberate staffing mix of domain experts and non-domain engineers, since outsiders are more likely to challenge the status quo
- Example: Japan-based COBOL-to-Java legacy migration, underlying systems worth hundreds of millions of dollars
- Feedback loop to research: FDEs convert a specific customer failure into a generalizable training-data request rather than relaying the raw complaint
- On-site time: ~50% average; ~80% in UAE and Japan engagements; 2-3 weeks/month for US/Europe-based FDEs
- Paywalled past the free section (hiring, onboarding, success factors, and how to move from SWE to FDE are locked)
```

## Open questions

- None.
