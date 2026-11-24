---
type: proposal
source: raw/articles/2026-11-23-cognitioncom-blog-swe-2.md
sources:
  - raw/articles/2026-11-23-cognitioncom-blog-swe-2.md
  - raw/articles/2026-11-23-cognitioncom-blog-local-fusion.md
  - raw/articles/2026-11-23-cognitioncom-blog-aws-sca.md
  - raw/tweets/2026-09-16-xcom-cognitionstatus210025354888580.md
  - raw/newsletters/2026-09-12-ainews-deepseek-v41-flash-763b-p8b-d16b-novel.md
  - raw/newsletters/2026-09-16-ainews-jev-a-system-one-model-that-only-decid.md
  - raw/newsletters/2026-09-17-ainews-reality-checks-on-ai-news-yegge-shuts-do.md
status: pending
created: 2026-11-24
---

# Proposal: Devin's September releases (SWE-2, Fusion in Desktop and CLI, Code Scans, AWS, cross-OS VMs)

## Summary

### In short
A coding agent's cost should be measured per task, not per token. Cognition's September releases show this twice. SWE-2, its new in-house model, scores within a point of Fable 5.1 on FrontierCode 1.1 at 64% lower cost. In Fusion, using a sidekick that costs more per token made the lead-plus-sidekick pair cheaper per task. The proposal updates **Devin**, **FrontierCode**, **State of Coding** and **Cost-aware routing evidence**: SWE-2 replaces the secondhand SWE-1.7 claims, and Code Scans, single-tenant AWS deployment and Mac/Windows VMs are added. It also adds four source pages. The reason to hesitate is length: Devin rises to about 120% of its ceiling.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
Cognition, the company behind the Devin coding agent, shipped five things in the week of 10 September 2026. On 10 September it released SWE-2, post-trained from Kimi K3, a 2.8-trillion-parameter open model. Cognition says it is the first time it has scaled reinforcement learning to multiple trillions of parameters. The new training trick trains every reasoning-effort level in one run, giving each level its own cost penalty so that cheap settings stay cheap. SWE-2 scores 50.0% on FrontierCode 1.1 Main, Cognition's 100-task test of whether code is mergeable, against 42.0% for SWE-1.7. At medium effort it takes 58% fewer turns and costs 81% less than SWE-1.7. AINews added that Devin Voice runs on it.

The next day, Fusion came to Devin Desktop and the CLI. Fusion is Cognition's two-agent harness: a frontier "lead" plans and reviews, and a cheaper "sidekick" does the work, each with its own cached context. With SWE-2 as sidekick it cut cost 11–46% across five benchmarks at near-equal scores. A chart updated on 19 October shows Opus 5.5 led by Fusion with a GPT-6 Luna sidekick running 31% cheaper than Claude Code on Artificial Analysis's Coding Agent Index. Cognition's headline finding is that a sidekick 3.75 times pricier per token lowered cost per task, because a stronger worker needs fewer review rounds. On 15 September Cognition signed a multi-year agreement with AWS. Devin can now run single-tenant in a customer-chosen region inside a dedicated VPC, with a disposable VM per session. Cognition cites Mercedes-Benz analysing 200,000 lines of COBOL in eight days instead of an estimated eight months. On 16 September came Code Scans (`/scan`), codebase-wide audits toward any goal built on the Agentic MapReduce engine. In the same week Devin gained Mac and Windows VMs.

### What changes
The wiki still names SWE-1.7 as Devin's model, from a secondhand recap, and describes Fusion as a June cloud preview.

- **Devin** swaps the SWE-1.7 bullet for SWE-2 and replaces the June Fusion numbers with the September ones. It gains a Code Scans bullet next to Security Swarm, plus AWS single-tenant and cross-OS VM bullets in a renamed deployment section. Four Recent-changes entries come in and the four oldest (9 and 14 July) spill to history. The page date stays 23 November.
- **FrontierCode** replaces its secondhand SWE-1.7 section with a short FrontierCode 1.1 section and adds one entry. Its date stays 23 November.
- **State of Coding** refreshes Devin's leader line, which dated from July, and adds one entry. The oldest entry (30 June) spills.
- **Cost-aware routing evidence** gains Fusion's per-task finding. Its entry is older than all ten live ones, so it goes straight to history.
- Four new source pages: one each for the SWE-2, Fusion and AWS posts, and one for the Code Scans thread that also cites the two AINews items.

### What to weigh
The AWS post's date (15 September) comes from the live page's metadata, because the saved copy has none. The September comparison models (GPT-6 Astra, GPT-5.6 Luna) have since been superseded, so they appear only in the FrontierCode 1.1 table and in passing. The Devin page was already over its ceiling, and this proposal adds to it.

## Intended changes

- [ ] **Update** `wiki/tools/devin.md` — rename "Security Swarm and Agentic MapReduce" section and add a Code Scans bullet; in the Fusion section, mark Fusion as shipped in Cloud, Desktop and CLI, replace the June FrontierCode Extended bullet with the September/October numbers, replace the SWE-1.7 bullet with SWE-2; rename "Devin Outposts" to "Deployment: Outposts, AWS and cross-OS VMs" and add two bullets; add four Recent-changes entries (2026-09-16, 2026-09-15, 2026-09-11, 2026-09-10) in date order; append four source ids and links; `as_of` stays 2026-11-23
- [ ] **Spill** `wiki/tools/devin.md` → `wiki/history/tools/devin.md` — the four oldest entries (2026-07-09 SWE-1.7 and the three 2026-07-14 entries) leave the live list to keep the cap at 10
- [ ] **Update** `wiki/benchmarks/frontiercode.md` — replace the "SWE-1.7 on FrontierCode (secondhand, 2026-07-09)" section with a "FrontierCode 1.1 (September 2026)" section; add one Recent-changes entry dated 2026-09-10 (5 → 6 entries, no spill); append source id and link; `as_of` stays 2026-11-23
- [ ] **Update** `wiki/state-of/coding.md` — replace the Devin leader line; add one Recent-changes entry dated 2026-09-16 (inserted between 2026-10-12 and 2026-08-03); append source ids; `as_of` stays 2026-11-23
- [ ] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — oldest entry (2026-06-30 Cursor iOS beta) leaves the live list
- [ ] **Update** `wiki/training/cost-aware-routing-evidence.md` — extend the "Eval data, not the router, is the moat" bullet with the Fusion per-task finding; append source id and link; `as_of` unchanged
- [ ] **Spill** `wiki/training/cost-aware-routing-evidence.md` → `wiki/history/training/cost-aware-routing-evidence.md` — the new 2026-09-11 Recent-changes entry is older than all ten live entries, so it goes straight to history
- [ ] **Create** `wiki/sources/articles/cognition-swe-2-2026-09-10.md`
- [ ] **Create** `wiki/sources/articles/cognition-local-fusion-2026-09-11.md`
- [ ] **Create** `wiki/sources/articles/cognition-aws-sca-2026-09-15.md`
- [ ] **Create** `wiki/sources/tweets/cognition-code-scans-2026-09-16.md`

## Page drafts

### wiki/tools/devin.md (updated)

Frontmatter (`sources:` appends four ids; `as_of` unchanged):

```
sources: [...live list..., cognition-swe-2-2026-09-10, cognition-local-fusion-2026-09-11, cognition-aws-sca-2026-09-15, cognition-code-scans-2026-09-16]
```

Section heading and new last bullet (rest of the section unchanged):

```
### Security Swarm, Code Scans and Agentic MapReduce

...existing bullets unchanged...
- **Code Scans (2026-09-16, `/scan`):** the same Agentic MapReduce engine pointed at any stated goal, not only security: slow paths and N+1 queries, untested flows, dead code and stale feature flags, WCAG accessibility, or a team's own coding standards. Devin helps scope what counts as a finding, reports, and opens the PRs. On the Dioxus repo it cut debug build time from 58.6s to 21.0s (64%) across 22 crates.
```

Fusion section (first bullet edited; second bullet replaced; SWE-1.7 bullet replaced; productivity-estimator bullet unchanged):

```
### Fusion, productivity measurement, and models

- **Devin Fusion (Cloud since June; Desktop and CLI since 2026-09-11):** applies the [sidekick multi-model harness pattern](../workflows/multi-agent-coordination.md) — a frontier model and a cheaper model run as two persistent, separately-cached agents, with the frontier model planning and reviewing while the sidekick handles mechanical work. Running on Fable 5, Fusion can beat Opus 4.8 on cost per task not because Fable is cheaper per token, but because stronger delegation and judgment waste fewer actions: per an independent coding-agent index analysis relayed by AINews, in 81% of sampled Fable-led runs the lead model never makes a code edit itself.
- **Fusion numbers (September–October 2026):** with SWE-2 as sidekick, Fusion cut cost 11–46% against the lead model alone across DeepSWE 1.1, Terminal-Bench 4.0, SWE-Atlas QnA, Vals Code Migration and FrontierCode 1.1 Extended, at near-equal scores (measured with Artificial Analysis and Vals AI). On Artificial Analysis's Coding Agent Index (chart updated 2026-10-19), Opus 5.5 led by Fusion with a GPT-6 Luna sidekick scores 68.1 at 31% lower cost than Claude Code on Opus 5.5; Cognition recommends that pairing. Cognition prices "per task, not per token": a sidekick 3.75x pricier per token cut the pair's cost per task 2% and raised the score (see [Cost-aware routing evidence](../training/cost-aware-routing-evidence.md)). Earlier, 88% of Cognition's own merged PRs ran entirely through the automated Fusion router.
- **Session productivity estimator:** ...unchanged...
- **SWE-2 (2026-09-10):** Cognition's current in-house coding model, post-trained from [Kimi K3](../models/kimi-k3.md) (2.8T) with RL scaled to multiple trillions of parameters; one RL run trains every reasoning-effort level, each with a cost penalty fitted to the base model's cost–performance curve. 50.0% on FrontierCode 1.1 Main (within a point of Fable 5.1 at 64% lower cost), 73.0% DeepSWE 1.1, 92.8% Terminal-Bench 2.1, 27.3% Terminal-Bench 4.0. At medium effort it takes 58% fewer turns and costs 81% less than SWE-1.7 while scoring higher. Available in Devin Desktop, CLI, Web and Fusion; Devin Voice runs on it with GPT-Live.
```

Deployment section (heading renamed; Outposts bullet unchanged; two bullets added):

```
### Deployment: Outposts, AWS and cross-OS VMs

- **Devin Outposts (July 2026):** ...unchanged...
- **AWS single-tenant (2026-09-15):** a multi-year Strategic Collaboration Agreement with AWS. Devin is sold on AWS Marketplace, uses the Agent Toolkit for AWS, and can be deployed single-tenant in a customer-chosen AWS region inside a dedicated VPC; each session runs in its own disposable VM and audit-log APIs feed the customer's monitoring. Cognition cites Mercedes-Benz analysing 200K+ lines of COBOL (an estimated eight-month project done in eight days) and another automaker moving a 25K-line COBOL workflow to Lambda at an estimated 73% lower cost.
- **Cross-OS cloud VMs (September 2026):** Devin runs as a cloud agent on macOS, Windows and Linux, including Mac VMs for end-to-end iOS work from Slack or the web; its VM, networking, VNC and computer-use infrastructure was rebuilt in Rust, with Dioxus Labs joining Cognition to work on it.
```

`## Recent changes` (adds four entries between 2026-09-21 and the next-oldest; the four oldest spill — see Spill draft):

```
- [2026-11-23] [Devin Bots](devin-bots.md) launched: ...
- [2026-10-19] Devin Oncall generally available: ...
- [2026-10-13] Devin Dynamic Workflows: ...
- [2026-10-06] Devin Dreaming (overnight memory prune-and-link) launched; ...
- [2026-09-21] Devin Cloud in the terminal: ...
- [2026-09-16] Code Scans (`/scan`): Agentic MapReduce audits toward any goal (performance, dead code, accessibility, team standards); Dioxus debug build 58.6s → 21.0s. Devin also runs cloud VMs on macOS and Windows as well as Linux.
- [2026-09-15] AWS Strategic Collaboration Agreement: Devin on AWS Marketplace and deployable single-tenant in a customer-chosen region inside a dedicated VPC.
- [2026-09-11] Fusion reaches Devin Desktop and CLI; with SWE-2 as sidekick it cuts cost 11–46% across five benchmarks; Cognition argues for pricing per task, not per token.
- [2026-09-10] SWE-2 replaces SWE-1.7 as Cognition's model: post-trained from Kimi K3, 50.0% FrontierCode 1.1 Main within a point of Fable 5.1 at 64% lower cost.
- [2026-07-21] Devin Outposts: ...
```

`## Sources` (appends four links):

```
- [Cognition — Introducing SWE-2](../sources/articles/cognition-swe-2-2026-09-10.md)
- [Cognition — Introducing Fusion in Devin Desktop & CLI](../sources/articles/cognition-local-fusion-2026-09-11.md)
- [Cognition — Cognition and AWS Strategic Collaboration Agreement](../sources/articles/cognition-aws-sca-2026-09-15.md)
- [Cognition — Introducing Code Scans (X thread)](../sources/tweets/cognition-code-scans-2026-09-16.md)
```

### wiki/history/tools/devin.md (updated — spill)

Appended at the end of the file:

```

## Archived from current page on <apply date>

- [2026-07-14] Cognition detailed Agentic MapReduce (Plan/Shard/Map/Reduce/Verify) as the architecture behind Security Swarm; reported 72% recall on a CVE-pinned benchmark vs. rival scanners.
- [2026-07-14] Cognition's session-level productivity estimator (`r_log = 0.74`, human-hours-equivalent, calibrated conservative) is now running in production with customers.
- [2026-07-14] Added the delegation-efficiency mechanism behind Devin Fusion's cost advantage on Fable 5: in 81% of sampled Fable-led runs, the lead model never edits code itself (per AINews, relaying an independent coding-agent index analysis).
- [2026-07-09] Cognition released SWE-1.7, a budget frontier coding model post-trained from Kimi K2.7 inside Devin's agent harness; per The Code's recap, Cognition claims it matches GPT-5.5 within a point on FrontierCode at ~$2/task with Opus 4.8 slightly ahead (secondhand, tier unspecified); supports up to six-hour sessions via self-summarization and resume.
```

### wiki/benchmarks/frontiercode.md (updated)

Frontmatter (`sources:` appends one id; `as_of` unchanged):

```
sources: [...live list..., cognition-swe-2-2026-09-10]
```

Replaces the whole `## SWE-1.7 on FrontierCode (secondhand, 2026-07-09)` section:

```
## FrontierCode 1.1 (September 2026)

Version 1.1 has a **Main** set (100 tasks, easy tasks excluded) and an **Extended** set (150 tasks). Scores are a weighted aggregate of rubric items; a solution that fails a blocking criterion scores 0, and cost is mean USD per rollout. Cognition's [SWE-2](../tools/devin.md) launch (2026-09-10) reported on Main:

| Model | FrontierCode 1.1 Main |
|---|---|
| GPT-6 Astra | 53.3% |
| Fable 5.1 | 50.9% |
| SWE-2 | 50.0% |
| Grok 4.6 | 48.0% |
| GPT-5.6 Sol | 47.5% |
| Kimi K3 | 44.2% |
| SWE-1.7 | 42.0% |

SWE-2 reached its score at 64% lower cost than Fable 5.1. Fusion results on 1.1 Extended are on the [Devin](../tools/devin.md) page. Version [2.0](#frontiercode-20-as-of-2026-11-23) has since appeared in OpenAI's GPT-6.2 launch.
```

`## Recent changes` (adds one entry, in date order between 2026-11-23 and 2026-07-09; no spill):

```
- [2026-11-23] FrontierCode 2.0 appears in OpenAI's GPT-6.2 launch: ...
- [2026-09-10] FrontierCode 1.1 (Main 100 tasks, Extended 150) reported in Cognition's SWE-2 launch: GPT-6 Astra 53.3%, Fable 5.1 50.9%, SWE-2 50.0% on Main.
- [2026-07-09] Per The Code's recap, ...
- [2026-06-29] ...
- [2026-06-10] ...
- [2026-06-09] ...
```

`## Sources` (appends one link):

```
- [Cognition — Introducing SWE-2](../sources/articles/cognition-swe-2-2026-09-10.md)
```

### wiki/state-of/coding.md (updated)

Frontmatter (`sources:` appends two ids; `as_of` unchanged):

```
sources: [...live list..., cognition-swe-2-2026-09-10, cognition-code-scans-2026-09-16]
```

Leader line:

> **Before:** `- [Devin](../tools/devin.md) — Cognition; Devin Fusion (preview) multi-model "sidekick" harness matches frontier performance at 35% lower cost (41% with Fable 5) on FrontierCode Extended; Security Swarm's Agentic MapReduce architecture now documented, reporting 72% recall on a CVE-pinned vulnerability benchmark *(as of 2026-07-14)*`

```
- [Devin](../tools/devin.md) — Cognition; in-house SWE-2 model within a point of Fable 5.1 on FrontierCode 1.1 at 64% lower cost; Fusion lead+sidekick harness now in Desktop and CLI; Code Scans run Agentic MapReduce audits toward any goal *(as of 2026-09-16)*
```

`## Recent changes` (adds one entry between 2026-10-12 and 2026-08-03; oldest spills):

```
- [2026-10-12] Added Muse Code to Terminal coding agent: ...
- [2026-09-16] Devin line refreshed: SWE-2 replaces SWE-1.7 as Cognition's model, Fusion reaches Desktop and CLI, and Code Scans extend Agentic MapReduce beyond security.
- [2026-08-03] Codex usage reportedly grew ...
```

### wiki/history/state-of/coding.md (updated — spill)

Appended at the end of the file:

```

## Archived from current page on <apply date>

- [2026-06-30] Cursor iOS beta adds mobile launch/control for always-on cloud agents and desktop agents.
```

### wiki/training/cost-aware-routing-evidence.md (updated)

Frontmatter (`sources:` appends one id; `as_of` unchanged):

```
sources: [...live list..., cognition-local-fusion-2026-09-11]
```

Sentence appended to the end of the "**Eval data, not the router, is the moat.**" bullet:

```
Cognition's September Fusion data adds the sidekick side: replacing a small sidekick at $0.20 per million tokens with SWE-2 at $0.75 (+275%) under the same lead cut cost per FrontierCode task 2% and raised the score from 62.0 to 63.4, because a stronger sidekick needs fewer review and correction rounds; earlier, swapping Opus 4.8 for Fable 5 as lead cut session cost 9% despite twice the token price. Cognition's rule: evaluate model-harness pairs on price per task, not per token.
```

`## Sources` (appends one link):

```
- [Cognition — Introducing Fusion in Devin Desktop & CLI](../sources/articles/cognition-local-fusion-2026-09-11.md)
```

`## Recent changes`: unchanged (the new entry is older than all ten live entries; see Spill draft).

### wiki/history/training/cost-aware-routing-evidence.md (updated — spill)

Appended at the end of the file:

```

## Archived from current page on <apply date>

- [2026-09-11] Added Cognition's Fusion sidekick finding to "Eval data, not the router, is the moat": a sidekick 3.75x pricier per token made the pair 2% cheaper per task with a higher score.
```

### wiki/sources/articles/cognition-swe-2-2026-09-10.md (new)

```
---
title: 'Cognition — Introducing SWE-2: Pushing the Pareto Frontier'
type: source
source_type: article
source_file: raw/articles/2026-11-23-cognitioncom-blog-swe-2.md
url: https://cognition.com/blog/swe-2
published: 2026-09-10
ingested: 2026-11-24
domains: [coding, models]
---

# Cognition — Introducing SWE-2: Pushing the Pareto Frontier

Cognition's launch post for SWE-2, its in-house coding model for Devin, post-trained from Kimi K3 with RL scaled to multiple trillions of parameters. It covers the benchmark table, the behaviour changes against SWE-1.7, and a training method that fits a per-effort-level cost penalty into one RL run. AINews (2026-09-12) relayed the launch and added Devin Voice, built on GPT-Live and SWE-2 (`raw/newsletters/2026-09-12-ainews-deepseek-v41-flash-763b-p8b-d16b-novel.md`).

## Influenced pages
- [Devin](../../tools/devin.md) — SWE-2 replaces the SWE-1.7 bullet
- [FrontierCode](../../benchmarks/frontiercode.md) — new FrontierCode 1.1 section
- [State of Coding](../../state-of/coding.md) — refreshed Devin leader line

## Key claims extracted
- SWE-2 is post-trained from Kimi K3 (2.8T parameters); Cognition's first RL at multi-trillion-parameter scale, building on the SWE-1.7 recipe.
- Reward R = S − λ_e·C, with a linear cost penalty per effort level, λ_e fitted to the slope of the base model's cost–performance frontier; all effort levels train in one run. Length-weighted reward baselines, NVFP4/FP8 kernels with quantization-aware training, an online draft model, 3x more RL environments.
- FrontierCode 1.1 Main: SWE-2 50.0%, GPT-6 Astra 53.3%, Fable 5.1 50.9%, Grok 4.6 48.0%, GPT-5.6 Sol 47.5%, Kimi K3 44.2%, SWE-1.7 42.0%. SWE-2 is within a point of Fable 5.1 at 64% lower cost.
- DeepSWE 1.1 73.0%; Terminal-Bench 2.1 92.8%; Terminal-Bench 4.0 27.3% (Fable 5.1 55.8%, GPT-6 Astra 57.9%).
- SWE-2 medium scores above SWE-1.7 with 58% fewer turns and 81% lower cost (mean steps 53 vs 127). The gains come mostly from more focused exploration.
- Available from launch in Devin Desktop and CLI, rolling out to Devin Web and Fusion.
```

### wiki/sources/articles/cognition-local-fusion-2026-09-11.md (new)

```
---
title: Cognition — Introducing Fusion in Devin Desktop & CLI
type: source
source_type: article
source_file: raw/articles/2026-11-23-cognitioncom-blog-local-fusion.md
url: https://cognition.com/blog/local-fusion
published: 2026-09-11
ingested: 2026-11-24
domains: [coding, agents]
---

# Cognition — Introducing Fusion in Devin Desktop & CLI

Cognition brings Fusion, its lead-plus-sidekick harness, from Devin Cloud to Devin Desktop and the CLI. The post reports benchmark savings measured with Artificial Analysis and Vals AI, explains why per-prompt model routing falls short, and argues that pricier models can make the pair cheaper per task. Its headline chart was updated on 2026-10-19.

## Influenced pages
- [Devin](../../tools/devin.md) — Fusion availability and current numbers
- [Cost-aware routing evidence](../../training/cost-aware-routing-evidence.md) — per-task vs per-token sidekick finding

## Key claims extracted
- The user picks a frontier lead (planning, ambiguity, review) and a cost-effective sidekick (exploration, implementation, tests). They exchange briefs, results and feedback, not whole conversations, and each keeps its own cached context.
- Artificial Analysis Coding Agent Index (updated 2026-10-19): Fusion with Opus 5.5 + GPT-6 Luna scores 68.1 at 31% lower cost than Claude Code with Opus 5.5 ($9.01 vs $13.04). Astra + SWE-2 runs 39% cheaper than Codex. The recommended pairing is Opus 5.5 + GPT-6 Luna.
- With SWE-2 as sidekick, cost savings against the lead alone: DeepSWE 1.1 −46% / −40%, Terminal-Bench 4.0 −23% / −40%, SWE-Atlas QnA −34% / −37%, Vals Code Migration −41% / −20%, FrontierCode 1.1 Extended −38% / −11% (Fable 5.1-led / Astra-led), at near-equal scores.
- Routing on the initial prompt fails because task difficulty is unknown until the code is investigated, and switching models mid-task breaks prompt caches.
- "Price per task rather than price per token": a GPT-5.6 Luna sidekick ($0.20/Mtok) scored 62.0 at $2.39 per task. A SWE-2 sidekick ($0.75/Mtok, +275%) scored 63.4 at $2.34 (−2%). Fable 5 as lead cost 9% less per session than Opus 4.8 at twice the token price.
- The harness is tuned per pair: how detailed briefs are, whether the sidekick may push back, and whether planning exploration is delegated.
```

### wiki/sources/articles/cognition-aws-sca-2026-09-15.md (new)

```
---
title: Cognition and AWS Strategic Collaboration Agreement
type: source
source_type: article
source_file: raw/articles/2026-11-23-cognitioncom-blog-aws-sca.md
url: https://cognition.com/blog/aws-sca
published: 2026-09-15
ingested: 2026-11-24
domains: [coding, agents]
---

# Cognition and AWS Strategic Collaboration Agreement

Cognition's post on a multi-year Strategic Collaboration Agreement with AWS, aimed at legacy migration and security and engineering backlogs. The publication date comes from the live page's `datePublished` metadata; the saved copy has none.

## Influenced pages
- [Devin](../../tools/devin.md) — AWS single-tenant deployment bullet

## Key claims extracted
- Devin is sold through AWS Marketplace and uses the Agent Toolkit for AWS inside Devin.
- Customers deploy Devin single-tenant on AWS in a region they choose. Data and organizational knowledge stay inside a dedicated VPC.
- Each session runs in its own VM, created for the task and removed afterwards. Audit-log APIs feed the customer's existing monitoring and compliance tools.
- Mercedes-Benz analyzed 200,000+ lines of COBOL with Devin, cutting an estimated eight-month modernization to eight days. Another automaker moved a 25,000-line COBOL workflow from a mainframe to AWS Lambda at an estimated 73% lower cost.
- Named joint customers include Echo Global Logistics and ActiveCampaign.
```

### wiki/sources/tweets/cognition-code-scans-2026-09-16.md (new)

```
---
title: Cognition — Introducing Code Scans (X thread)
type: source
source_type: tweet
source_file: raw/tweets/2026-09-16-xcom-cognitionstatus210025354888580.md
url: https://x.com/cognition/status/2100253548885803404
published: 2026-09-16
ingested: 2026-11-24
domains: [coding, agents]
---

# Cognition — Introducing Code Scans (X thread)

Cognition's launch thread for Code Scans, codebase-wide audits toward a stated goal, powered by Agentic MapReduce. AINews mentioned the launch on 2026-09-17 (`raw/newsletters/2026-09-17-ainews-reality-checks-on-ai-news-yegge-shuts-do.md`). AINews on 2026-09-16 (`raw/newsletters/2026-09-16-ainews-jev-a-system-one-model-that-only-decid.md`) relayed the same week's cross-OS VM news from @jeffwang and @jkelleyrtp, and that item is recorded here too.

## Influenced pages
- [Devin](../../tools/devin.md) — Code Scans and cross-OS VM bullets
- [State of Coding](../../state-of/coding.md) — refreshed Devin leader line

## Key claims extracted
- Code Scans (`/scan`) are codebase-wide audits for any goal. Devin investigates, reports findings and opens PRs.
- Targets include slow paths and N+1 queries, untested flows and edge cases, dead code and stale feature flags, WCAG accessibility, and team coding standards. Devin helps scope what to inspect and what counts as a finding.
- In the Dioxus repo, debug build time fell from 58.6s to 21.0s (64%) across 22 workspace crates.
- AINews, 2026-09-16: Devin can spin up Mac VMs for end-to-end iOS development from Slack or the web UI. It is a cloud agent across macOS, Windows and Linux, with storage, networking, VNC and computer-use infrastructure rebuilt in Rust. Dioxus Labs is joining Cognition to work on Devin's VMs, computer use and testing (AINews, 2026-09-12).
```

## Schema / vocabulary additions

None.

## Open questions

- **Devin** was already at 103% of its 1,500-word ceiling and lands at about 120% after this proposal. Split the Devin Oncall section (four bullets plus its "Why it matters" paragraph) into its own `tools/devin-oncall.md`, as was done for Devin Bots? (Assumed: not now.)
	- Yes
