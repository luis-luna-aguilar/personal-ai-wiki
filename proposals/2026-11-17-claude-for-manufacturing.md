---
type: proposal
source: raw/articles/2026-11-17-claudecom-resources-articles-claude-for-manufacturing.md
status: pending
created: 2026-11-17
---

# Proposal: Claude for Manufacturing

## Summary

### In short

Anthropic's industry packaging has reached the plant floor, and its control design is the part worth keeping. Claude for Manufacturing (12 November) is a 17-skill plugin. It carries quoting, failed inspections, breakdowns, sourcing and production reports up to a person's sign-off, connects to Autodesk Fusion, Infor, Microsoft 365 and Oracle NetSuite, and changes Infor records only through Infor's own plugin, under the user's own Infor permissions. The proposal adds it to the industry-bundles section of Claude Cowork, adds one governance pattern to Agent autonomy and governance, and creates one source page. Reason to hesitate: the launch never mentions Cowork, so the Cowork page is its home by precedent only.

[[#Open questions|Open questions: 1 to answer.]]

- [ ] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

Anthropic announced Claude for Manufacturing on claude.com on 12 November 2026. It is a plugin: a packaged set of skills (reusable instructions for one kind of job) plus connectors (live links into a company's own software). Its 17 skills cover sales, quality, operations, supply chain, design and setup, and some chain several steps until a person has to review. An estimator gets a draft quote priced against similar past jobs; a quality engineer gets causes ranked and a corrective-action report drafted; a technician gets a breakdown's likely causes ranked from sensor exports, repair notes and the manual. Buyers, design engineers and plant managers get bid comparisons, Fusion design variations and production reports.

The Infor connector only looks records up. Changes go through a separate plugin that Infor itself is releasing: when a steel shipment slips two weeks, Claude finds the affected orders and other sites' stock, and once the buyer approves, it releases a purchase order to another supplier and reschedules production, with access limited to the buyer's Infor permissions. Systems without a connector are covered by exports saved to Microsoft 365. Every skill ends in a person's review, with figures linked to source documents. The plugin does not operate equipment; for that, the post points to Anthropic's Model Hardware Standard research preview. Saying "Set us up" makes Claude test the connectors and list skills that can't fully run yet.

### What changes

The wiki files Anthropic's earlier industry bundles, Small Business and Legal, in a section of the Claude Cowork page, and keeps Claude for Financial Advisors as an unlinked line on State of Finance. None has its own page, so this launch doesn't get one either.

- **Claude Cowork** gains a Claude for Manufacturing bullet in its industry-bundles section, whose intro is reworded so it no longer implies every bundle runs on Cowork. One Recent-changes entry; page date moves to 12 November.
- **Agent autonomy and governance** gains one governance pattern: keep looking up separate from changing, and let write access follow the user's own permissions in the system of record. One Recent-changes entry; page date moves to 12 November.
- **Index** lines for both pages get new descriptions and dates.
- One new source page for the launch post.

### What to weigh

The post describes a plugin for Team and Enterprise plans and never names Cowork, while the Cowork page says Cowork comes with Pro. Filing it there follows the earlier bundles; the draft avoids saying it runs in Cowork. No manufacturing domain is proposed: one launch doesn't justify a state-of page. The Model Hardware Standard gets one sentence in the post, so it stays a clause here.

## Intended changes

- [ ] **Update** `wiki/tools/claude-cowork.md` — reword the intro and closing line of `## Vertical workflow bundles` and add a Claude for Manufacturing bullet (section stamp 2026-05-14 → 2026-11-12); adds one Recent-changes entry dated 2026-11-12 at the top of the list (6 of 10, no spill); append 1 source id and 1 link; `as_of` 2026-07-08 → 2026-11-12; the `## Current status (as of 2026-07-08)` stamp stays, since nothing in that section changes
- [ ] **Update** `wiki/training/agent-autonomy-and-governance.md` — add one bullet to `## Governance patterns`, directly after "Widen autonomy per task type, with verification built in"; adds one Recent-changes entry dated 2026-11-12 at the top of the list (7 of 10, no spill); append 1 source id and 1 link; `as_of` 2026-10-14 → 2026-11-12
- [ ] **Update** `wiki/index.md` — refresh the `tools/claude-cowork` and `training/agent-autonomy-and-governance` lines (description and date)
- [ ] **Create** `wiki/sources/articles/claude-for-manufacturing-2026-11-12.md` — source summary

## Page drafts

### wiki/tools/claude-cowork.md (updated)

Frontmatter changes:

```
as_of: 2026-11-12
sources: [...existing..., claude-for-manufacturing-2026-11-12]
```

`## Vertical workflow bundles` section, replaced in full (the Small Business and Legal bullets are unchanged):

```
## Vertical workflow bundles (as of 2026-11-12)

Anthropic packages prebuilt workflows, skills, and connectors for specific industries, aimed at end users rather than developers. The first two launched as Cowork-based bundles; Claude for Manufacturing is described as a Claude plugin for Team and Enterprise plans, without naming the surface it runs in.

- **Claude for Small Business** — 15 ready-to-run agentic workflows + 15 skills; integrations with QuickBooks, PayPal, DocuSign; automates payroll planning, invoice chasing, campaign launch, and similar repeatable tasks
- **Claude for Legal Professionals** — 12 one-click workflows for legal document and workflow automation
- **Claude for Manufacturing** (2026-11-12) — 17 skills for plant teams: quoting a new job, investigating a failed inspection, diagnosing a breakdown, sourcing from another supplier, comparing designs in Autodesk Fusion, and production reporting. Connectors to Autodesk Fusion, Infor, Microsoft 365, and Oracle NetSuite; systems without a connector are covered by saving regular exports to Microsoft 365. Every skill ends in a person's review, with figures linked back to source data. The Infor connector only reads; changes in Infor go through Infor's own plugin, after the user approves, within that user's Infor permissions. Does not operate equipment (Anthropic points to its Model Hardware Standard research preview for that). Setup: install on a Team or Enterprise plan and say "Set us up"; Claude asks which systems the team uses, tests the connectors, and reports which skills can't fully run yet.

Together the bundles are the clearest signal yet of Anthropic shifting from developer API tools toward direct end-user vertical automation products.
```

Recent changes — one entry inserted at the top, above the 2026-07-08 entry:

```
- [2026-11-12] Claude for Manufacturing launched: 17-skill plugin for plant teams (quoting, failed-inspection investigation, breakdown diagnosis, sourcing, Fusion design comparison, production reporting) with Autodesk Fusion, Infor, Microsoft 365, and Oracle NetSuite connectors; every skill ends in human review; Infor writes via Infor's own plugin under the user's permissions; Team and Enterprise plans.
```

Sources — one link appended:

```
- [Claude for Manufacturing: AI plugin for plant teams](../sources/articles/claude-for-manufacturing-2026-11-12.md)
```

### wiki/training/agent-autonomy-and-governance.md (updated)

Frontmatter changes:

```
as_of: 2026-11-12
sources: [...existing..., claude-for-manufacturing-2026-11-12]
```

`## Governance patterns` — one bullet inserted directly after the "Widen autonomy per task type, with verification built in" bullet:

```
- **Keep looking up separate from changing, and let write access follow the user's own permissions.** Anthropic's Claude for Manufacturing (November 2026) ends every skill with the responsible person's review: the estimator checks and releases the quote, the quality engineer verifies the fix. Its Infor connector only looks records up. Changes in Infor go through Infor's own plugin and run only after the user approves (for example, releasing a purchase order to another supplier and rescheduling production when a steel shipment slips), within that user's existing Infor permissions. Claude links figures and claims back to the underlying data and documents so the reviewer can check them.
```

Recent changes — one entry inserted at the top, above the first 2026-10-19 entry:

```
- [2026-11-12] Added "Keep looking up separate from changing" from Anthropic's Claude for Manufacturing launch: skills end in the responsible person's review, Infor changes go through Infor's own plugin after approval and within the user's Infor permissions, and figures link back to source data.
```

Sources — one link appended:

```
- [Claude for Manufacturing: AI plugin for plant teams](../sources/articles/claude-for-manufacturing-2026-11-12.md)
```

### wiki/index.md (updated)

Two lines replaced in place:

```
- [tools/claude-cowork](tools/claude-cowork.md) — Anthropic's cross-device knowledge-work agent; web/mobile beta and closed-computer scheduled tasks strengthen background delegated work; industry bundles for small business, legal, and manufacturing *(as_of: 2026-11-12)*
```

```
- [training/agent-autonomy-and-governance](training/agent-autonomy-and-governance.md) — eval-gated autonomy ladder (levels 0–5), humans in vs. above the loop, and Every's 8-level adoption/fluency model, governance patterns: promotion after reliability, trust batteries, ownership split, read/write split under the user's own permissions, workflow-level measurement *(as_of: 2026-11-12)*
```

### wiki/sources/articles/claude-for-manufacturing-2026-11-12.md (new)

```
---
title: 'Claude for Manufacturing: AI plugin for plant teams'
type: source
source_type: article
source_file: raw/articles/2026-11-17-claudecom-resources-articles-claude-for-manufacturing.md
url: https://claude.com/resources/articles/claude-for-manufacturing
published: 2026-11-12
ingested: 2026-11-17
domains: [agents, training]
---

# Claude for Manufacturing: AI plugin for plant teams

Anthropic's launch post for Claude for Manufacturing, a Claude plugin for plant teams on Team and Enterprise plans. Its 17 skills carry manufacturing jobs (quoting, failed-inspection investigation, breakdown diagnosis, sourcing, design comparison, production reporting) up to the point where a responsible person reviews and approves the work. It works from a manufacturer's own records through connectors to Autodesk Fusion, Infor, Microsoft 365, and Oracle NetSuite. Changes in Infor go through a separate plugin released by Infor, gated by the user's approval and Infor permissions. The plugin does not operate equipment.

## Influenced pages
- [Claude Cowork](../../tools/claude-cowork.md) — third industry bundle in the vertical-bundles section
- [Agent autonomy and governance](../../training/agent-autonomy-and-governance.md) — read/write split with write access under the user's own permissions

## Key claims extracted
- Launched 2026-11-12 as a plugin; 17 skills across sales, quality, operations, supply chain, design, and setup. Some skills do one task; others chain several until a person must review.
- Example processes: quoting a new job (read the request, list what's missing, compare costs on similar jobs, draft the quote); investigating a failed inspection (document it, check past reports, rank causes, draft the corrective action report); diagnosing a breakdown (read sensor exports, repair notes, photos, and the manual; rank likely causes for the technician); sourcing from another supplier (request for quotes, bid comparison); comparing designs with Autodesk Fusion (variations from an existing model, scored against targets, decision memo); production reporting (output against target, downtime, and the cost of downtime and missed output).
- Connectors: Autodesk Fusion, Infor (look up purchase orders and stock), Microsoft 365 (procedures, supplier emails, exported reports), Oracle NetSuite (orders, inventory, production steps, job costs). Systems without a connector work through regular exports saved to Microsoft 365.
- Infor is releasing its own plugin that lets Claude make changes in Infor; example: when a steel shipment slips two weeks, the buyer asks which customer orders are affected and how much steel other sites have; after the buyer approves, Claude releases a purchase order to another supplier and reschedules affected production. Claude's access follows the buyer's Infor permissions.
- Skills are built to end with a user's review; Claude can link figures and claims back to the underlying data and documents.
- Does not operate equipment; Anthropic points to its Model Hardware Standard, a research preview giving programmable equipment a standard way to describe its measurements, settings, and safety limits.
- Setup: install on Team or Enterprise and say "Set us up"; Claude asks which systems the team uses, tests the connectors, and reports which skills can't fully run yet. Anthropic plans to add more manufacturing skills.
- Cites a 2025 Manufacturing Leadership Council survey: 79% of manufacturers said they enter data manually.
```

## Schema / vocabulary additions

None.

## Open questions

- Should I fetch and ingest Anthropic's Model Hardware Standard research-preview announcement (https://www.anthropic.com/news/model-hardware-standard-research-preview) as its own source? It would likely fit [Physical AI deployment](../wiki/trends/physical-ai-deployment.md), which watches for safety and validation practices around equipment that AI touches. This proposal mentions it only as the plugin's stated boundary.
