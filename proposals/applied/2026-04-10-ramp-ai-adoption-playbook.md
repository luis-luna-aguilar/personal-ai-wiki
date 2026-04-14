---
type: proposal
source: raw/articles/2026-04-10-xcom-geoffintech-article-2042002590758572377.md
status: pending
created: 2026-04-10
---

# Proposal: Ramp AI adoption playbook

## Summary

Ramp's article is not mainly a product announcement. It is a substantive operating write-up on company-wide AI enablement: clear executive mandate, preconfigured internal tooling, broad connector access, visible sharing loops, leaderboards, office hours, hackathons, and a central-platform-plus-distributed-builders org model.

The strongest wiki-worthy signals are practical and organizational. This fits best as a new `training/` page on company-wide AI enablement, plus an update to the existing trend page about agents reshaping organizations with Ramp's concrete adoption and non-engineer building metrics.

## Intended changes

- [x] **Create** `wiki/training/company-wide-ai-enablement.md` — new practical guidance page on how companies can drive broad AI adoption beyond engineering
  > See full draft below.

- [x] **Update** `wiki/trends/agents-reshape-organizations.md` — add Ramp as a concrete signal and refresh `as_of`
  > See diff snippet below.

- [x] **Create** `wiki/sources/articles/ramp-ai-adoption-playbook.md` — source summary page
  > See full draft below.

- [x] **Update** `wiki/index.md` — add the new training page, refresh the trend line date, and update counts
  > See diff snippet below.

## Why these pages

- **`wiki/training/`** is the best primary target because the source is mostly an enablement playbook: access model, org design, adoption loops, and rollout guidance. It is more operational than conceptual.
- **`wiki/trends/agents-reshape-organizations.md`** already carries the higher-level thesis that leverage is shifting from individuals to orgs. Ramp provides one of the clearest company-reported data points currently in the wiki.
- I am **not** updating `wiki/tools/claude-code.md` or `wiki/tools/codex.md` because the references to Claude Code, Cowork, and Codex are incidental context, not new first-order product information.

## Page drafts

### wiki/training/company-wide-ai-enablement.md (new)

```markdown
---
title: Company-wide AI enablement
type: training
as_of: 2026-04-10
sources: [ramp-ai-adoption-playbook]
---

# Company-wide AI enablement

Company-wide AI enablement is the practical problem of getting a broad organization, not just engineers, to use AI tools productively in daily work. The recurring lesson in this source is that adoption is driven less by formal curriculum and more by operating design: easy access, strong defaults, visible examples, and social pressure to build.

## Current guidance

- Start with a clear expectation from leadership that AI use is part of how work gets done
- Lower the activation barrier with one preconfigured agent surface, SSO, and preconnected workplace tools
- Pair a small central platform team with distributed builders in each function
- Make usage and wins visible through demos, shared channels, office hours, and public examples
- Raise performance expectations only as the tooling becomes good enough to support them

## Proven patterns

- **Platform plus spokes.** A central team owns connectors, platforms, skills, and enablement; functional teams build domain workflows on top
- **Product-led teaching.** The first real result matters more than formal training; the tool should teach through immediate usefulness
- **Shared workflow marketplace.** Internal skills or templates let one person's discovery become everyone else's shortcut
- **Visible adoption loops.** Leaderboards, all-hands demos, and team channels turn private experimentation into contagious behavior
- **Exploration budget.** Removing token caps and access restrictions gives people room to discover high-leverage use cases before ROI is obvious

## Failure modes

- Treating AI as a procurement exercise with slow approvals, connector queues, and restrictive access
- Raising expectations before the tools are reliable or easy enough for non-experts
- Centralizing all building work into one overloaded team, or fully decentralizing and accepting redundant re-learning
- Overinvesting in workshops while underinvesting in defaults, tooling, and social proof

## Evidence from practice

- Ramp reports AI usage up 6,300% year over year, with 99.5% of employees active on AI tools
- The company says 84% of employees use coding agents weekly
- Ramp reports 1,500+ apps shipped in six weeks by 800+ builders on its internal platform
- Non-engineers reportedly account for 12% of human-initiated PRs on the production codebase via Ramp Inspect
- Ramp attributes much of the adoption to a preconfigured internal agent (`Glass`), a shared skills marketplace (`Dojo`), and highly visible social reinforcement

## Open questions

- Which parts of this playbook generalize outside high-velocity tech companies with unusually strong internal engineering capacity?
- How often do visible usage metrics improve real leverage versus incentivizing performative activity?
- What is the minimum viable internal platform needed before this pattern works outside companies that can build their own agent layer?

## Sources

- [[sources/articles/ramp-ai-adoption-playbook]]
```

### wiki/sources/articles/ramp-ai-adoption-playbook.md (new)

```markdown
---
title: Ramp AI adoption playbook
type: source
source_type: article
source_file: raw/articles/2026-04-10-xcom-geoffintech-article-2042002590758572377.md
url: https://x.com/geoffintech/article/2042002590758572377
ingested: 2026-04-10
domains: [coding, agents]
---

# Ramp AI adoption playbook

Ramp publishes a detailed internal account of how it pushed AI adoption across the company. The article's core claim is that broad AI uptake came from operating design rather than a formal training curriculum: executive mandate, broad access, preconfigured internal tooling, visible sharing loops, and org structures that let non-engineers build on top of centrally managed platforms.

## Influenced pages

- [[training/company-wide-ai-enablement]] — new practical page distilling the operating patterns for broad AI adoption
- [[trends/agents-reshape-organizations]] — adds a concrete company data point showing non-engineers and distributed teams building through internal agents

## Key claims extracted

- Ramp says AI usage is up 6,300% year over year and 99.5% of employees are active on AI tools
- The company says 84% of employees use coding agents weekly
- Ramp reports 1,500+ apps shipped in six weeks by 800+ different builders on its internal platform
- Non-engineers reportedly account for 12% of human-initiated PRs on the production codebase via Ramp Inspect
- Ramp built `Glass`, an internal AI agent layer with Okta SSO and 30+ preconnected tools
- The company built a shared skills marketplace called `Dojo`
- Ramp argues office hours, demos, and first-day wins teach better than formal training programs
- The source recommends a central-platform-plus-distributed-builders model rather than full centralization or full decentralization

## Caveats

- This is a first-party Ramp article, so the adoption metrics and organizational claims are vendor-reported
- The piece is practical and useful as an operating example, but it is not neutral reporting or a controlled study
- Some product references, such as Claude Code's Cowork and Anthropic's Claude Agent SDK, are mentioned in passing rather than documented directly here
```

### wiki/trends/agents-reshape-organizations.md (updated snippet)

```markdown
---
title: Agents reshape organizations (leverage moves from individual to org)
type: trend
domains: [agents, coding]
tags: [agentic]
as_of: 2026-04-10
sources: [harvey-legal-is-next, ramp-ai-adoption-playbook]
---

## Concrete signals

- **Background agents inside companies.** Cited examples now include Ramp's background agent / coding-agent stack, Stripe's end-to-end coding agents, and Harvey's internal Spectre system.
- **Ramp publishes concrete internal adoption numbers.** Ramp reports 99.5% of employees active on AI tools, 84% using coding agents weekly, 1,500+ apps shipped in six weeks by 800+ builders, and non-engineers accounting for 12% of human-initiated PRs on the production codebase.
- **The org model itself changes.** Ramp describes a central team owning platforms, connectors, and enablement while functional teams build on top, which is exactly the kind of operating redesign this trend predicts.

## Open questions

- Is this trend already happening in practice, or is it mostly Twitter / vendor-blog narrative? We now have a stronger first-party Ramp data point, but still need more independent or cross-company reporting before treating it as settled.

## Recent changes

- [2026-04-10] Ramp adds a concrete company-reported example of org-wide AI building and non-engineer PR creation
- [2026-04-02] Trend opened from Harvey's "Legal is Next" post
```

### wiki/index.md (updated snippet)

```markdown
## Trends

- [[trends/agents-reshape-organizations]] — leverage moves from individual to org as autonomous agents take coordination work *(as_of: 2026-04-10)*
- [[trends/ai-in-science]] — AI as force-multiplier for researchers; NASA anomalies, brain MRI, AlphaFold *(as_of: 2026-04-10)*
- [[trends/proprietary-data-becomes-model-moat]] — proprietary operational data, domain evals, and narrow training loops may become a stronger moat as model quality converges *(as_of: 2026-04-10)*

## Training

- [[training/company-wide-ai-enablement]] — operating patterns for broad AI adoption: defaults, access, social proof, and platform-plus-spokes org design *(as_of: 2026-04-10)*

## Page count

- state-of: 7 (5 populated, 2 skeleton)
- models: 1
- tools: 12
- benchmarks: 0
- workflows: 1
- concepts: 5
- trends: 3
- training: 1

**Total content pages: 30.** The wiki is still in the early stage, but no longer below the initial bootstrap threshold.
```

## Schema / vocabulary additions

- None proposed.

## Open questions

- The fetched X article did not expose a clear `published:` date in the saved raw file, so I used the ingest date fallback (`2026-04-10`) for `as_of`. If you want, I can manually inspect the rendered page for an explicit publication date and revise the proposal.
	-  leave it as is

## Comments

-  for my personal comments please add to my backlog that we need to allow our customers to open PRs in our projects, even if they are not technical, like the Ramp personnel did.
