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
- [Claude app](../../tools/claude-app.md) — third industry bundle in the vertical-bundles section
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
