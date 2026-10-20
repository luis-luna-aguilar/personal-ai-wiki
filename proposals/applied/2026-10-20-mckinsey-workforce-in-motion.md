---
type: proposal
source: raw/articles/2026-10-20-mckinseycom-mgi-workforce-in-motion-us.md
status: pending
created: 2026-10-20
---

# Proposal: McKinsey Global Institute — "Workforce in motion" (US skills and pathways report)

## Summary

### In short
The AI labor question for the next decade is mobility, not job scarcity: McKinsey Global Institute projects the US gains about 41 million jobs while automation removes the equivalent of 36 million, yet roughly 11 million workers must switch occupation and only one in seven has a direct path, with credentials gating 85% of growing jobs. The proposal adds a forward-projection section to AI labor-market effects, two short hiring points to the junior-talent page, and a source page. One reason to hesitate: only the web text was read, not the 82-page PDF or its technical appendix.

[[#Open questions|Open questions: 1 to answer.]]

### The source
On 29 September 2026 the McKinsey Global Institute, McKinsey's economics research arm, published a ten-year US forecast to 2035 built on Bureau of Labor Statistics projections and Lightcast job-posting data. AI and other automation could absorb or augment about 54% of current work hours, but four offsets (relief for overworked staff, extra demand when work gets cheaper, new oversight tasks, and barriers to layoffs) cancel about 60% of that, leaving a net drop of roughly 36 million jobs. Ageing, rising living standards, construction, energy and the tech economy add about 41 million.

Most churn happens inside occupations, so the authors focus on the 11 million workers (6 to 16 million depending on adoption speed) who must change occupation outright, at 3.6 times the historical rate for a decade. They grade each route from a shrinking job to a growing one as direct (strong skill overlap, no pay cut, under six months of training), winding, or unpaved: 14%, 41% and 45% of transitions. Credentials are the biggest obstacle, and 47% of growing jobs carry one that employers prefer but the law does not require.

The report sorts skills into essential (widen options), enabling (unlock higher pay) and empowering (keep adapting), and finds job-posting demand for AI fluency up about elevenfold since 2022. The authors call their adoption estimates "directional rather than deterministic".

### What changes
The wiki's labor page currently holds only observed data (Stanford, Anthropic, Ramp, an earlier McKinsey podcast), and the hiring page covers interview redesign and the shrinking junior pipeline.

- **AI labor-market effects** gains a new section, "Projected reallocation to 2035", with five bullets on the reallocation numbers, who has to move, exposure versus transition risk, pathway quality and credentials, and the three skill types. It sits outside Current status because that section is close to its flat-section limit. One Recent-changes entry dated 29 September is added (5 entries, no spill). The page date stays at 19 October, since the report predates the page's newest claim.
- **AI-native hiring and the junior talent pipeline** gains one interview bullet on skills-based screening and one paragraph noting that software-developer postings are up about 15% since early 2025, with the gaps in senior and AI-oriented roles. One Recent-changes entry dated 29 September (2 entries, no spill). Page date stays at 19 October.
- New source page `wiki/sources/articles/mckinsey-workforce-in-motion-2026-09.md`.

### What to weigh
The hiring page is written for engineering talent leads, so it gets only the two points they can act on, and the economy-wide numbers, demographic multipliers and pathway framework stay on the trends page. The labor page ends near its 1,200-word ceiling (about 1,155 body words), so the next addition there will likely need a split. The source page uses the `training` domain, since no labor or economics domain exists.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.
  *(Approved in chat by the user on 2026-10-20.)*

- [ ] **Update** `wiki/trends/ai-labor-market-effects.md` — add a new `## Projected reallocation to 2035` section after `## Current status`; add one Recent-changes entry dated 2026-09-29 (live list has 5, cap 10, no spill); append source id `mckinsey-workforce-in-motion-2026-09` to frontmatter `sources:` and one link to `## Sources`; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Update** `wiki/training/ai-native-hiring-and-junior-talent.md` — add one bullet at the end of `## Hiring AI-native engineers`'s bullet list; add one paragraph at the end of `## The junior talent problem`; add one Recent-changes entry dated 2026-09-29 (live list has 2, no spill); append source id and link; `as_of` stays 2026-10-19
    > See draft below

- [ ] **Create** `wiki/sources/articles/mckinsey-workforce-in-motion-2026-09.md` — source summary

## Page drafts

### wiki/trends/ai-labor-market-effects.md (updated)

Frontmatter `sources:` (append one id):

```
sources: [ai-adoption-is-management, ramp-ai-adoption-playbook, mckinsey-agentic-org, stanford-labor-june-2026, anthropic-81k-economics, ainews-fable5-june-2026, anthropic-employment-report-2026-10, karpathy-capability-funnel-2026-10-11, mckinsey-workforce-in-motion-2026-09]
```

New section, inserted between the end of `## Current status (as of 2026-10-19)` and `## Related`:

```
## Projected reallocation to 2035

McKinsey Global Institute's "Workforce in motion" report (September 2026) is a ten-year US forecast rather than observed data. Its headline: the coming problem is mobility, not job scarcity.

- **More jobs than automation removes, but different jobs.** Base case: automation absorbs or augments about 54% of current US work hours by 2035. Overwork relief, productivity-driven demand (the Jevons effect), new review and oversight tasks, and barriers to displacement offset about 60% of that, leaving a net 21% cut in labor demand, about 36 million jobs. Demographics, rising living standards, construction, energy, and the tech economy add about 41 million, including 0.5–2 million in occupations that do not exist yet.
- **About 11 million workers (range 6–16 million) must change occupation.** That is roughly 770,000 moves a year across occupational groups, 3.6× the historical rate, sustained for a decade. Over three-quarters come from office and administrative support, retail and sales, and transportation and logistics. Lower-wage workers are 7.6× as likely to need to move as higher-wage workers; younger workers 1.6× as likely as prime-age workers.
- **Exposure is not transition risk.** Risk is highest where demand falls and routes to growing work are weak, not where automation is highest. More than 70% of workers face some reinvention (over 15% of task time reallocated) whether their occupation grows, shrinks, or holds.
- **Pathway quality is the constraint.** 14% of transitions are direct (strong skill overlap, no wage loss, under six months of training), 41% winding (under two years), 45% unpaved. Credentials are the largest barrier: 85% of growing jobs call for one, 38% by law, and 47% only because employers prefer it.
- **Empowering skills are surging.** From 2022 to 2026, job-posting demand for AI fluency rose about 11×, adaptability about 5×, and willingness to learn, resilience, and curiosity about 3×. MGI sorts skills into essential (widely required, widen options), enabling (decision-making, critical thinking; unlock higher pay), and empowering (keep adapting).
```

`## Recent changes` — insert one entry below the three 2026-10-19 / 2026-10-11 entries, above the 2026-06-16 entry (no spill):

```
- [2026-09-29] Added McKinsey Global Institute's 2035 US reallocation forecast: ~11M occupation changes, 14% direct pathways, credentials on 85% of growing jobs, AI-fluency demand up ~11× since 2022.
```

`## Sources` — append one link:

```
- [McKinsey Global Institute — "Workforce in motion: Skills and pathways to future jobs in the United States"](../sources/articles/mckinsey-workforce-in-motion-2026-09.md)
```

### wiki/training/ai-native-hiring-and-junior-talent.md (updated)

Frontmatter `sources:` (append one id):

```
sources: [the-code-2026-04-23, shopify-latent-space-april-2026, lennysan-simonw-interview, mckinsey-agentic-org, stanford-labor-june-2026, anthropic-employment-report-2026-10, mckinsey-workforce-in-motion-2026-09]
```

`## Hiring AI-native engineers` — append one bullet after the "Autonomy and judgment over domain depth" bullet:

```
- **Screen on demonstrated skills, not proxies.** McKinsey Global Institute (September 2026) finds that 47% of growing US jobs carry a credential employers prefer but the law does not require, and that candidates with transferable skills are often screened out by subjective signals. Its remedy fits the build-interview approach: consistent interview criteria, practical assessments, explicit skill definitions, and resetting degree requirements.
```

`## The junior talent problem` — append one paragraph after the Anthropic internal data block:

```
**McKinsey Global Institute (September 2026):** software-developer job postings have risen about 15% since early 2025, after falling from their 2022 peak, but the openings are concentrated in senior and AI-oriented roles. Economy-wide, younger workers are about 1.6× as likely as prime-age workers to need to change occupation by 2035 (see [AI labor-market effects](../trends/ai-labor-market-effects.md)).
```

`## Recent changes` — append one entry at the bottom (oldest last; no spill):

```
- [2026-09-29] Added McKinsey Global Institute data: 47% of growing jobs have employer-preferred credentials (case for skills-based screening); developer postings up ~15% since early 2025, concentrated in senior and AI-oriented roles.
```

`## Sources` — append one link:

```
- [McKinsey Global Institute — "Workforce in motion: Skills and pathways to future jobs in the United States"](../sources/articles/mckinsey-workforce-in-motion-2026-09.md)
```

### wiki/sources/articles/mckinsey-workforce-in-motion-2026-09.md (new)

```
---
title: 'McKinsey Global Institute — "Workforce in motion: Skills and pathways to future jobs in the United States"'
type: source
source_type: article
source_file: raw/articles/2026-10-20-mckinseycom-mgi-workforce-in-motion-us.md
url: https://www.mckinsey.com/mgi/our-research/Workforce-in-motion-Skills-and-pathways-to-future-jobs-in-the-United-States
published: 2026-09-29
ingested: 2026-10-20
domains: [training]
---

# McKinsey Global Institute — "Workforce in motion"

McKinsey Global Institute report by María Jesús Ramírez, Kweilin Ellingrud, Tanguy Catlin, Diego Castresana and Anna Kortis, published 29 September 2026. A ten-year US forecast (to 2035) of how AI, automation and structural trends reallocate work, built on BLS employment projections, Lightcast job postings and MGI's automation and transition-pathway models. Thesis: the US will likely have more jobs than automation removes, so the challenge is mobility, not scarcity; what matters is the quality of the pathway from a declining occupation to a growing one, which skills and barriers (above all credentials) determine. Distinct from the earlier McKinsey podcast ingested as `mckinsey-agentic-org`. Ingested from the web text; the 82-page PDF and technical appendix were not read.

## Influenced pages
- [AI labor-market effects](../../trends/ai-labor-market-effects.md) — new "Projected reallocation to 2035" section
- [AI-native hiring and the junior talent pipeline](../../training/ai-native-hiring-and-junior-talent.md) — skills-based screening bullet; senior-weighted developer demand

## Key claims extracted
- Automation could absorb or augment ~54% of US work hours by 2035; four offsets (overwork alleviation, productivity-induced demand, new work activities, barriers to displacement) cancel ~60%, leaving a 21% net cut in labor demand, ~36M jobs
- Growth drivers add ~41M jobs: rising living standards ~18M, demographics ~8M, construction ~3M, energy ~2M, digital economy ~3M, tech infrastructure ~2M, new AI-era occupations 0.5–2M
- ~25M of the 36M net out within occupations; ~11M workers (6–16M range, ~7% of employees) must change occupation
- Required cross-group moves: ~770,000/yr, 3.6× the ~215,000 historical average, near the COVID peak (~788,000/yr, 2019–22), but sustained for a decade
- Over 75% of transitioning workers are in office/admin support, retail/sales, transportation/logistics; five occupations (customer service reps, retail sales associates, office assistants, cashiers, warehouse workers) are about a third
- Highest expected adoption by 2035: office/admin ~80% of work hours, technology/analytics 70%, retail/sales 68%; lowest: healthcare professionals 26%, public safety 28%
- Lower-wage workers 7.6× as likely to need to change occupation; no-degree 1.8×; younger 1.6×; women 1.6×
- Pathways: 14% direct (strong skill overlap, no wage loss, <6 months training), 41% winding (<2 years), 45% unpaved; only ~3% (~305,000) of transitions require a pay cut
- Top-quintile earners are 4× as likely as bottom-quintile to have a direct pathway (~40% vs 10%)
- Growing occupations ask for 68 skills on average vs 47 in declining ones; 84% vs 45% require postsecondary education
- ~57–60% of growing employment is in the top two wage quintiles; over 70% of declining employment is in the bottom two
- 85% of growing jobs call for a credential; 38% legally required; 47% employer-preferred only; 15% none; 76% require physical presence
- Skill types: essential (problem solving, leadership, communication; widen options), enabling (decision-making, innovation, critical thinking; unlock higher pay), empowering (AI fluency, adaptability, resilience, curiosity, willingness to learn; continuous adaptation)
- Job-posting demand 2022–2026: AI fluency ~11×, adaptability ~5×, willingness to learn / resilience / curiosity ~3×
- More than 70% of workers face reinvention (>15% of task time reallocated); 25% face >30%
- Software-developer postings up ~15% since early 2025, gaps in senior and AI-oriented roles
- Employers should use structured, skills-based hiring (consistent criteria, practical assessments, reset degree requirements) and track redeployment and internal fill rates alongside cost savings
- Adoption estimates are "directional rather than deterministic"
```

## Schema / vocabulary additions

None.

## Open questions

- Should the essential / enabling / empowering skill frame and the AI-fluency demand figure also go on `training/company-wide-ai-enablement.md`, as guidance on what to train for beyond tool use? Assumed no for now: that page is already large, and the trends page carries the numbers.
	- Ok
