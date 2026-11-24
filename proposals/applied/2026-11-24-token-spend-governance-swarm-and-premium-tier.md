---
type: proposal
source: raw/newsletters/2026-09-17-why-you-should-burn-more-tokens.md
sources:
  - raw/newsletters/2026-09-17-why-you-should-burn-more-tokens.md
  - raw/newsletters/2026-09-17-ainews-reality-checks-on-ai-news-yegge-shuts-do.md
  - raw/newsletters/2026-09-20-copy-our-homework.md
status: pending
created: 2026-11-24
---

# Proposal: Token-spend governance — the 4.5B-token swarm and Databricks' premium-tier sub-budget

## Summary

### In short
Big agent bills come from structure, not ambition: an agent swarm with no cap on how many workers it spawns burns most of its tokens on coordination, and a premium model rolled out to everyone raises total spend sharply while helping mainly on the hardest work. Every's head of video burned 4.5 billion tokens in 36 hours on one 3D model; Databricks saw coding spend rise about 60% and gave its premium tier its own sub-budget. The proposal adds two evidence cases, two spending controls and one failure mode to the two cost-routing pages. Reason to hesitate: the evidence page moves just past its length ceiling (about 106%).

[[#Open questions|Open questions: none.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 17 September 2026 Every's Context Window ("Why You Should Burn More Tokens", by Laura Entis) described how the company handles large AI bills without a hard budget. Head of operations Arielle Shipper keeps the ChatGPT credit card on a $500 automatic refill that posts a Slack alert at every top-up; a burst of top-ups sends her to the usage leaderboard. After any costly run she asks what it cost, what it bought, and what was learned, and Every is building a skill for per-employee AI-spending profit-and-loss statements.

The headline case is Randy Counsman, head of video. He set up a manager agent, an implementer agent, subagents and a judge, told the manager to deploy agents "as needed", and told it to keep going until a Blender model of his head was "done extremely well". The run lasted a day and a half, used 4.5 billion tokens, and produced something "very janky". An AI audit of the sessions found the layers passing ever-larger context back and forth, even for simple status checks. His rebuilt setup drops the implementer, caps the orchestrator at five subagents, has the orchestrator pause for his feedback, and gives the judge a reference image instead of an open-ended instruction. The newsletter includes a prompt for auditing where a run's tokens went.

The same day, AINews relayed Databricks' report (Patrick Wendell) on rolling GPT-6 Astra out to about 3,500 engineers after a 200-person pilot. Astra clearly beat other top models on complex system design and long tasks, but added little on routine coding, and total coding spend rose about 60%. Databricks responded with a dedicated Astra sub-budget to push people toward selective use. A 20 September Every recap repeats the Every material and adds nothing new.

### What changes
The wiki already records Every's earlier Sol cost spike (no token budgets yet) and Databricks' FinOps savings, but not how runaway agent runs happen or how to budget a premium tier.

- **Cost-aware routing: evidence from practice** gains two cases under cost variance: the uncapped swarm and its fix, and Databricks' +60% premium-tier rollout. Its Recent-changes list is at the ten-entry cap and the new 17 September entry is the oldest, so it goes straight to history. Page date stays 19 October.
- **Cost-aware AI task routing** gains two AI FinOps controls (refill alerts plus the three post-run questions; a separate sub-budget for a premium tier) and one failure mode (uncapped fan-out). Page date stays 17 November.
- One new source page for the Every newsletter and one story page for the AINews Databricks item.

### What to weigh
The Databricks rollout was of GPT-6 Astra, which GPT-6.2 Astra has since replaced; the drafts name the version and link its history page, on the view that the sub-budget practice does not depend on the version. The Every piece is read from the newsletter email, which carries the full text.

## Intended changes

- [ ] **Update** `wiki/training/cost-aware-routing-evidence.md` — add two bullets under `### Cost variance and budgeting tradeoffs`; add `every-burn-more-tokens-2026-09-17` and `ainews-databricks-astra-sub-budget-2026-09-17` to frontmatter `sources:` and body `## Sources`; adds one Recent-changes entry dated 2026-09-17 (see Spill); `as_of` unchanged (2026-10-19 is newer)
- [ ] **Spill** `wiki/training/cost-aware-routing-evidence.md` → `wiki/history/training/cost-aware-routing-evidence.md` — the list is at the 10-entry cap and the new [2026-09-17] entry is the oldest of eleven, so it is appended directly to history; the live ten stay as they are
- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — two new AI FinOps control bullets, one new failure mode; add the two source ids to `sources:` and `## Sources`; adds one Recent-changes entry dated 2026-09-17 (list has 4 entries, no spill); `as_of` unchanged
- [ ] **Create** `wiki/sources/newsletters/every-burn-more-tokens-2026-09-17.md` — source summary
- [ ] **Create** `wiki/sources/newsletters/ainews-databricks-astra-sub-budget-2026-09-17.md` — story page for the AINews Databricks item

## Page drafts

### wiki/training/cost-aware-routing-evidence.md (updated)

Frontmatter: append to `sources:` → `every-burn-more-tokens-2026-09-17, ainews-databricks-astra-sub-budget-2026-09-17`. `as_of` stays `2026-10-19`.

Under `### Cost variance and budgeting tradeoffs`, insert after the "Every's Sol cost spike" bullet:

```
- **An uncapped swarm spends its tokens on coordination.** Every's head of video, Randy Counsman, ran a manager → implementer → subagents → judge setup on GPT-6 Astra, told the manager to deploy agents "as needed" and to keep improving a Blender head model until it was "done extremely well." It ran a day and a half, used 4.5 billion tokens and produced a "very janky" result. An audit of the sessions showed the layers passing growing context back and forth, even for status checks. The rebuilt setup drops the implementer, caps the orchestrator at five subagents, pauses for his feedback, and gives the judge a reference image instead of an open-ended goal. Every reports the failed run as worth it: it left a benchmark for new models and a leaner setup.
- **A premium tier raised Databricks' coding spend about 60%.** Databricks rolled [GPT-6 Astra](../history/models/gpt-6-astra.md) out to about 3,500 engineers after a ~200-user pilot. Astra clearly beat other top models on high-complexity system design and long-range work but did little for medium and low-complexity coding, and total coding spend rose about 60%. Databricks answered with a dedicated sub-budget for that tier to encourage selective use rather than withdrawing access.
```

`## Recent changes`: no change to the live list (the new entry spills straight to history; see below).

`## Sources`: append

```
- [Every — Why You Should Burn More Tokens](../sources/newsletters/every-burn-more-tokens-2026-09-17.md)
- [AINews — Databricks' Astra rollout and sub-budget](../sources/newsletters/ainews-databricks-astra-sub-budget-2026-09-17.md)
```

### wiki/history/training/cost-aware-routing-evidence.md (updated — spill)

Append under a new header (or under the apply-date header if one is already open):

```
## Archived from current page on <apply date>

- [2026-09-17] Added Every's 4.5B-token uncapped swarm (coordination overhead, capped rebuild) and Databricks' GPT-6 Astra rollout (+60% coding spend, dedicated sub-budget) to Cost variance and budgeting tradeoffs.
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

Frontmatter: append to `sources:` → `every-burn-more-tokens-2026-09-17, ainews-databricks-astra-sub-budget-2026-09-17`. `as_of` stays `2026-11-17`.

Under `## AI FinOps controls`, insert after the "Pair spend visibility with staged behavioral nudges" bullet:

```
- Without hard budgets, watch the payment rail and review after the fact: Every keeps a $500 automatic credit refill that posts a Slack alert at each top-up, treats a burst of top-ups as a cue to check the usage leaderboard, and asks three questions after any expensive run: what did it cost, what did it buy, what did we learn. A costly run that shows a new capability or limit is worth it; a modest result earns more spend only if it can be reproduced more cheaply. Every is turning this into a skill that gives each employee a personal AI-spending profit-and-loss statement.
- Give a premium model tier its own sub-budget. When Databricks gave about 3,500 engineers its top tier, it helped on complex long-range work, not routine coding, and coding spend rose about 60%; a separate allocation steers that tier to the work that benefits instead of making it everyone's default.
```

Under `## Failure modes`, append:

```
- Letting an orchestrator spawn agents "as needed" toward an open-ended goal ("until it is done extremely well"). Cap the number of subagents, cut coordination layers that only relay work, add human checkpoints, and give any judge a concrete target such as a reference image; Every's uncapped version burned 4.5 billion tokens in a day and a half, much of it on context passed between layers.
```

`## Recent changes`: append as the last entry (date order: the live list runs 11-23, 11-17, 10-19, 09-25, so 09-17 is oldest):

```
- [2026-09-17] Added two FinOps controls (refill alerts plus three post-run questions; a premium-tier sub-budget, from Databricks' +60% coding spend) and the uncapped-swarm failure mode.
```

`## Sources`: append

```
- [Every — Why You Should Burn More Tokens](../sources/newsletters/every-burn-more-tokens-2026-09-17.md)
- [AINews — Databricks' Astra rollout and sub-budget](../sources/newsletters/ainews-databricks-astra-sub-budget-2026-09-17.md)
```

### wiki/sources/newsletters/every-burn-more-tokens-2026-09-17.md (new)

```
---
title: "Why You Should Burn More Tokens — Every"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-17-why-you-should-burn-more-tokens.md
url: https://every.to/context-window/why-you-should-burn-more-tokens
published: 2026-09-17
ingested: 2026-11-24
domains: [agents]
---

# Why You Should Burn More Tokens — Every

Laura Entis's Context Window edition on how Every handles large AI bills without hard budgets: expensive experiments are encouraged but reviewed afterwards, a card-refill alert works as an early-warning system, and one uncapped agent swarm burned 4.5 billion tokens before its owner rebuilt it with limits. Also includes a token-audit prompt, Marcus Moretti's model-matching workflow, and the team's current model choices. A 20 September Every recap (`raw/newsletters/2026-09-20-copy-our-homework.md`) repeats the same points.

## Influenced pages

- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — uncapped-swarm case and its fix
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — refill alert and three post-run questions; uncapped fan-out failure mode

## Key claims extracted

- Dan Shipper uses more than three times the tokens of anyone else at Every; low spend is a "smoke signal" that people may be thinking too small
- No universal spending limit; after an expensive run, ask whether it was worth it and whether a similar result could be had more cheaply
- Arielle Shipper keeps a $500 ChatGPT auto-refill with a Slack alert per top-up; rapid top-ups prompt a look at the usage leaderboard
- Three post-run questions: what did it cost, what did it buy, what did we learn
- Every is building a skill for per-employee AI-spending P&L statements; Mike Taylor is building personal benchmarks to show which cheaper models handle recurring tasks
- Randy Counsman's manager/implementer/subagent/judge swarm ran 1.5 days, used 4.5B tokens, produced a "very janky" Blender model; layers passed growing context even for status checks
- Fix: drop the implementer, cap the orchestrator at five Sol subagents, pause for feedback, give the judge a reference image
```

### wiki/sources/newsletters/ainews-databricks-astra-sub-budget-2026-09-17.md (new)

```
---
title: "AINews — Databricks' Astra rollout raises coding spend ~60%"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-09-17-ainews-reality-checks-on-ai-news-yegge-shuts-do.md
url: https://www.latent.space/p/ainews-reality-checks-on-ai-news
published: 2026-09-17
ingested: 2026-11-24
domains: [agents, models]
---

# AINews — Databricks' Astra rollout raises coding spend ~60%

AINews (Latent Space) item relaying Patrick Wendell's report on Databricks' GPT-6 Astra rollout: a premium model that clearly helps on hard, long tasks but raises total coding spend, handled with a dedicated sub-budget.

## Influenced pages

- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — premium-tier rollout case
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — premium-tier sub-budget control

## Key claims extracted

- Databricks rolled GPT-6 Astra out to ~3,500 engineers after piloting with ~200 users
- Astra "unambiguously" outperformed Opus 5 / Sol 5.6 on high-complexity system design and long-range tasks, but may not materially improve medium/low-complexity coding
- Total coding spend rose ~60%; Databricks created a dedicated Astra sub-budget to encourage selective use
```

## Schema / vocabulary additions

None.

## Open questions

None.
