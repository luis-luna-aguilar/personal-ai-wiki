---
type: proposal
source: raw/articles/2026-04-22-everyto-source-code-how-we-run-a-25-person-company-on-four-a.md
status: pending
created: 2026-04-22
---

# Proposal: Every.to — how a 25-person company runs on four Notion agents

## Summary

Every (Dan Shipper's media/product company, ~25 people) built four custom agents on Notion AI that automate cross-database coordination work. The COO now gets daily task prioritization by messaging an agent instead of manually cross-referencing launch calendars, strategy docs, and task lists. Concrete operational pattern for small organizations deploying agents for coordination work.

## Intended changes

- [x] **Update** `wiki/training/company-wide-ai-enablement.md` — add Every's four-agent case study as a new evidence entry and operating principles
    > **Add to `## Evidence from practice`:**
    > ```markdown
    > - Every (April 2026, Source Code event): 25-person media/product company running four custom Notion AI agents for cross-database coordination. Anton (prioritization agent): COO messages it in Slack to get a prioritized task list cross-referencing launch calendar, strategy docs, and task lists. Three other agents automate scheduling and project coordination. Key insight: agents become powerful when they query *interconnected* Notion databases — strategy, calendar, tasks, people, and meeting notes all referencing each other. Core operating principles from this deployment: describe outcomes not steps; don't write agent instructions yourself (let AI generate them); the richness of the underlying database is the agent's brain.
    > ```
    >
    > **Add to `## Proven patterns`:**
    > ```markdown
    > - **Let AI write the agent instructions.** Every found that telling Notion AI what the agent should accomplish and letting it generate the instructions works better than writing detailed step-by-step instructions manually. Over-prescribing ("create a database, then add a relation, then filter by...") tends to confuse the model. State the outcome; let the agent figure out implementation.
    > - **Interconnected databases are the agent's brain.** Every's agents work because strategy, calendar, tasks, people, and meeting notes all live in Notion and reference each other. An agent querying isolated tables has no coordination leverage; agents querying an interconnected knowledge graph become genuinely powerful coordinators.
    > ```

- [x] **Create** `wiki/sources/articles/every-four-agents.md` — source summary
    > See draft below

## Page drafts

### wiki/sources/articles/every-four-agents.md (new)

```md
---
title: How We Run a 25-person Company on Four AI Agents
type: source
source_type: article
source_file: raw/articles/2026-04-22-everyto-source-code-how-we-run-a-25-person-company-on-four-a.md
url: https://every.to/source-code/how-we-run-a-25-person-company-on-four-ai-agents
published: 2026-04-22
ingested: 2026-04-22
domains: [agents]
---

# How We Run a 25-person Company on Four AI Agents

Every's Brandon Gell (COO) and Austin Tedesco (head of growth) walkthrough of four Notion AI custom agents: Anton (task prioritization), plus three others for scheduling and coordination. Built over a few months. Presented at Custom Agents Camp for 500+ subscribers, produced in partnership with Notion.

## Influenced pages

- [[training/company-wide-ai-enablement]] — four-agent case study added; two new proven patterns added

## Key claims extracted

- 25-person company, six products, media company, and consultancy
- Four agents built on Notion AI
- Anton: prioritization agent. COO messages it in Slack → prioritized task list for self and team in seconds (previously took manual cross-referencing)
- Agents work because all company data (strategy, calendar, tasks, people, meeting notes) lives in interconnected Notion databases
- Three operating principles: describe outcome not steps; Notion is agent's brain; let AI write agent instructions
- Also usable via Claude Code with Notion's API from the terminal
```
