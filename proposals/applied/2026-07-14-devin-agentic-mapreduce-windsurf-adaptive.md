---
type: proposal
sources:
  - raw/articles/2026-07-14-devinai-blog-agentic-map-reduce.md
  - raw/articles/2026-07-14-devinai-blog-windsurf-adaptive.md
  - raw/articles/2026-07-14-cognitioncom-blog-devin-fusion.md
  - raw/articles/2026-07-14-cognitioncom-blog-ai-productivity.md
status: pending
created: 2026-07-14
---

# Proposal: Cognition/Devin batch — Agentic MapReduce, Windsurf Adaptive, Devin Fusion, productivity estimator

## Summary
Four Cognition/Devin posts, all fetched 2026-07-14: (1) **Agentic MapReduce** — the deterministic-selector architecture behind Devin Security Swarm, with a 72%-recall CVE-pinned benchmark; (2) **Windsurf Adaptive** — a model router, transparent per-token pricing, and removed Max daily limits (published 2026-07-14, no explicit source date); (3) **Devin Fusion** (published 2026-06-29) — a "sidekick" multi-model harness matching frontier performance at 35% lower cost; (4) **AI productivity estimation** — Cognition's production system for converting Devin sessions into human-engineering-hours-equivalent, benchmarked against METR and Anthropic prior work.

Several of these updates land on the same pages (`tools/devin.md`, `state-of/coding.md`, `workflows/agentic-orchestration-patterns.md`), so this proposal supersedes the earlier two-source draft and folds everything into one consistent set of edits.

## Intended changes

- [x] **Update** `wiki/tools/devin.md` — add Agentic MapReduce architecture, Devin Fusion sidekick harness + FrontierCode Extended results, and the session productivity estimator; bump `as_of`/`sources`
    > See draft below

- [x] **Update** `wiki/benchmarks/frontiercode.md` — add the new FrontierCode Extended (score + cost) tier from the Devin Fusion post; bump `as_of`/`sources`
    > See draft below

- [x] **Update** `wiki/state-of/cybersecurity.md` — refresh the Devin leader line with the Agentic MapReduce architecture + 72% recall benchmark; bump `as_of`/`sources`
    > See draft below

- [x] **Update** `wiki/workflows/agentic-orchestration-patterns.md` — expand the passing "Agentic MapReduce" mention into a full pattern entry, and add a new "Sidekick multi-model harness" pattern from Devin Fusion; bump `as_of`/`sources`
    > See draft below

- [x] **Spill** `wiki/workflows/agentic-orchestration-patterns.md` → `wiki/history/workflows/agentic-orchestration-patterns.md` — the two new pattern entries push Recent changes from 9 to 11; spill the oldest 1 entry to get back to the 10-entry cap (new history file)
    > See draft below

- [x] **Update** `wiki/workflows/advisor-strategy.md` — add a contrast section with the sidekick pattern (per-call cache-miss cost vs. persistent dual-context agents); bump `as_of`/`sources`
    > See draft below

- [x] **Create** `wiki/tools/windsurf.md` — no current page for Windsurf; Cognition's IDE-based coding workspace gets Adaptive model routing, pricing-transparent model picker, and no more Max daily limits

- [x] **Update** `wiki/state-of/coding.md` — add Windsurf to the `agentic-coding-workspace` subcategory; add Devin to the `terminal-coding-agent` subcategory (previously missing despite Devin's own frontmatter subcategory); bump `as_of`/`sources`
    > See draft below

- [x] **Spill** `wiki/state-of/coding.md` → `wiki/history/state-of/coding.md` — adding the Windsurf + Devin Fusion entries pushes Recent changes from 13 to 15; the page was already 3 over the 10-entry cap before this ingest (pre-existing, per `scripts/recent_changes_cap.py`), so 5 oldest entries spill to bring it back to exactly 10
    > See draft below

- [x] **Update** `wiki/concepts/agent-evals.md` — add a "Human-hours-equivalent productivity estimation" section (Cognition's estimator vs. METR/Anthropic prior work); bump `as_of`/`sources`
    > See draft below

- [x] **Update** `wiki/training/ai-enablement-software-development.md` — add the productivity estimator as production evidence of hours/dollar-denominated ROI measurement; bump `as_of`/`sources`
    > See draft below

- [x] **Create** `wiki/sources/articles/devinai-blog-agentic-map-reduce.md` — source summary

- [x] **Create** `wiki/sources/articles/devinai-blog-windsurf-adaptive.md` — source summary

- [x] **Create** `wiki/sources/articles/cognitioncom-blog-devin-fusion.md` — source summary

- [x] **Create** `wiki/sources/articles/cognitioncom-blog-ai-productivity.md` — source summary

## Page drafts

### wiki/tools/devin.md (updated)

````md
---
title: Devin
type: tool
domains: [coding, agents]
subcategory: terminal-coding-agent
tags: []
as_of: 2026-07-14
sources: [devin-auto-triage-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion, cognitioncom-blog-ai-productivity]
---

# Devin

Cognition's autonomous coding agent, initially positioned as one of the first "fully autonomous software engineer" agents. Now expanding into persistent operational roles: Auto-Triage (May 2026) is the first always-on production deployment, monitoring Slack channels and triaging bugs without human initiation. Cognition valued at $25B (May 2026).

## Current status (as of 2026-07-14)

- **Auto-Triage:** always-on persistent Devin monitors Slack channels for bug reports, alerts, and incidents
- Parent Devin filters noise and dispatches focused sub-sessions to find root causes, post diagnoses, and tag code owners
- Shared long-term memory deduplicates repeat reports and builds team ownership map
- Generates PR candidates in addition to diagnoses
- Early adopter Modal: "more useful than homegrown triage automations"
- **Security Swarm:** parallel agents fan out across a codebase for vulnerability discovery, validation, patching, and PR generation
- Security Swarm aggregates findings, reproduces each issue in a sandbox, validates exploitability, then writes a patch for review
- **Agentic MapReduce (the architecture behind Security Swarm):** a Plan agent studies the repo and authors deterministic "selectors" (Tree-sitter queries, symbol/type queries, import-graph traversals, lexical patterns); the selectors run over every file with no model in the loop (Shard), producing a bounded, inspectable work queue instead of an open-ended search; one fresh Devin session per batch investigates its shard in parallel (Map); a Reducer session dedupes findings and composes cross-shard attack chains, e.g. an unauthenticated ID leak plus an ID-gated RCE becoming one P0 (Reduce); a final Verify stage reproduces each serious finding in a sandboxed session against a running build and marks it Confirmed, False Positive, or Inconclusive
- Benchmarked against a CVE-pinned ground-truth set (GitHub Advisory Database, each pinned to the commit before its fix, dozens of cases across 12+ languages and vulnerability classes): Security Swarm reports **72% recall**, ahead of other scanners tested in the same eval, at a fraction of their cost
- Cognition claims the system finds more verified vulnerabilities at 30% lower cost than rivals; treat both this and the 72% recall figure as vendor-reported until independently verified, though the CVE-pinned methodology is more rigorous than a bare cost claim
- **Devin Fusion (preview):** a multi-model "sidekick" harness — a frontier model runs alongside a cheaper sidekick model, each a fully capable agent with its own tools and persistent, separately-cached context; the frontier model plans, interprets ambiguity, and reviews, while delegating mechanical or well-scoped work to the sidekick; a lightweight classifier can reassign which model leads mid-session, timed to coincide with context-compaction points so the switch doesn't cost an extra cache miss
- On **FrontierCode Extended** (a cost-aware coding benchmark tracking both score and average cost per task), Fusion matches frontier-model performance at **35% lower cost** than running Opus 4.8 or GPT-5.5 alone, and **41% lower cost** when paired with Fable 5 (measured before Fable 5's access was suspended); internally, **88%** of Cognition's own merged PRs were driven entirely by the automated Fusion router
- **Session productivity estimator:** an automated system that reviews each completed Devin session, classifies whether it produced useful (typically merged) work, then estimates the equivalent human-engineering hours it saved; calibrated against 258 self-reported sessions from 126 users, reaching `r_log = 0.74` on held-out data, deliberately calibrated to underestimate rather than overestimate; now running in production with customers — Cognition frames this as the first automated system measuring AI engineering productivity in production

## Why it matters

Auto-Triage is Cognition's first persistent always-on production agent — distinct from session-scoped coding help. The parent/child Devin architecture (one manager filters noise, many focused workers investigate) is a concrete production instance of the [mayor + polecats orchestration pattern](../workflows/agentic-orchestration-patterns.md). Shared long-term memory across sessions gives it the deduplication capability that ephemeral agents lack.

Security Swarm extends the same architecture into enterprise security work, and Cognition has now named and documented the underlying pattern as [Agentic MapReduce](../workflows/agentic-orchestration-patterns.md): deterministic selection guarantees whole-repo coverage, parallel bounded workers keep cost proportional to relevant code rather than repo size, and a reasoning Reduce step connects findings that isolated workers couldn't see on their own. Devin Fusion applies a different multi-model idea — [sidekick harnesses](../workflows/agentic-orchestration-patterns.md), contrasted with the [Advisor strategy](../workflows/advisor-strategy.md) pattern by keeping both models' contexts persistently cached instead of paying a cache-miss cost per escalation. The productivity estimator is a production instance of [dollar/hours-denominated agent evals](../concepts/agent-evals.md).

## Recent changes

- [2026-07-14] Cognition detailed Agentic MapReduce (Plan/Shard/Map/Reduce/Verify) as the architecture behind Security Swarm; reported 72% recall on a CVE-pinned benchmark vs. rival scanners.
- [2026-07-14] Cognition's session-level productivity estimator (`r_log = 0.74`, human-hours-equivalent, calibrated conservative) is now running in production with customers.
- [2026-06-29] Devin Fusion (preview): multi-model "sidekick" harness matches frontier performance at 35% lower cost (41% with Fable 5) on FrontierCode Extended; 88% of Cognition's internal merged PRs driven by the automated router.
- [2026-07-02] Cognition shipped Devin Security Swarm for parallel vulnerability discovery, sandbox reproduction, exploitability validation, and fix PRs.
- [2026-05-19] Auto-Triage shipped: always-on Slack monitoring, parent/child Devin structure, shared long-term deduplication memory

## Sources

- [Devin Auto-Triage launch](../sources/articles/devin-auto-triage-2026-05.md)
- [The Code - Cognition ships Devin for Security](../sources/newsletters/the-code-devin-security-2026-07-02.md)
- [AINews - not much happened today](../sources/newsletters/ainews-not-much-happened-2026-07-02.md)
- [Agentic MapReduce (Cognition/Devin blog)](../sources/articles/devinai-blog-agentic-map-reduce.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
- [Estimating the Productivity of an Autonomous AI Software Engineer](../sources/articles/cognitioncom-blog-ai-productivity.md)
````

### wiki/benchmarks/frontiercode.md (updated)

**Frontmatter:**
```
as_of: 2026-06-29
sources: [ainews-frontiercode-june-2026, ainews-fable5-june-2026, cognitioncom-blog-devin-fusion]
```

**New section, inserted after `## Current leaderboard (as of 2026-06-09)` and before `## Why it matters`:**

```
## FrontierCode Extended (cost-aware, as of 2026-06-29)

Cognition also reports a separate "Extended" benchmark that pairs score with average cost per task, introduced alongside [Devin Fusion](../tools/devin.md):

| Configuration | Score | Avg. cost/task |
|---|---|---|
| Fusion + Fable 5* | 57.6 | $3.00 |
| Fable 5 (medium)* | 57.0 | $5.12 |
| Opus 4.8 (high) | 48.8 | $3.24 |
| Fusion | 47.9 | $2.38 |
| GPT-5.5 (high) | 44.8 | $3.64 |
| GLM-5.2 | 43.0 | $2.70 |

*Fable 5 access was suspended 2026-06-12 under a US government directive; the Fable 5 and Fusion+Fable 5 numbers reflect internal measurements taken before the suspension.

Scores here are not directly comparable to the Diamond-tier percentages above — Extended appears to be a distinct task set and scoring scale, introduced specifically to evaluate cost-aware multi-model harnesses like Devin Fusion.
```

**`## Recent changes` — add at top:**

```
- [2026-06-29] Cognition introduced FrontierCode Extended (score + avg. cost/task) alongside Devin Fusion; Fusion+Fable5 leads the cost-adjusted comparison at 57.6/$3.00, while Fable5 alone scores marginally higher (57.0) at much higher cost ($5.12).
```

**`## Sources` — add:**

```
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
```

### wiki/state-of/cybersecurity.md (updated)

**Frontmatter:**
```
as_of: 2026-07-14
sources: [slopcop-repo, glasswing, openai-gpt-5-5-launch, ai-security-scanners-2026-05-01, supply-chain-attacks-2026-05-13, agentic-security-tooling-2026-05-13, openai-daybreak-2026-05-13, cloudflare-glasswing-2026-05, the-code-devin-security-2026-07-02, ainews-not-much-happened-2026-07-02, gray-swan-ai-security-2026-06, devinai-blog-agentic-map-reduce]
```

**`### AI-assisted vulnerability detection` — replace the Devin line:**

> **Before:**
> ```
> - [Devin](../tools/devin.md) — Cognition; Devin Security Swarm uses parallel bounded agents, sandbox reproduction, exploitability validation, and patch PRs for vulnerability work; vendor claims include 30% lower cost than rivals and Fortune 500 pilot results, pending independent verification *(as of 2026-07-02)*
> ```
> **After:**
> ```
> - [Devin](../tools/devin.md) — Cognition; Security Swarm now documented as **Agentic MapReduce**: agent-authored deterministic selectors guarantee whole-repo coverage (Plan/Shard), parallel bounded workers investigate each shard (Map), a Reducer dedupes and composes cross-shard attack chains (Reduce), a sandboxed Verify stage reproduces serious findings; benchmarked at **72% recall** on a CVE-pinned ground-truth set (GitHub Advisory Database, dozens of cases across 12+ languages) vs. rival scanners — still a vendor-run eval pending independent verification *(as of 2026-07-14)*
> ```

**`## Recent changes` — add at top:**

```
- [2026-07-14] Devin Security Swarm detailed as Agentic MapReduce (deterministic-selector Plan/Shard, parallel Map, reasoning Reduce, sandboxed Verify); Cognition reported 72% recall on a CVE-pinned benchmark vs. rival scanners, still vendor-run.
```

### wiki/workflows/agentic-orchestration-patterns.md (updated)

**Frontmatter:**
```
as_of: 2026-07-14
sources: [..., devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion]
```
(append `devinai-blog-agentic-map-reduce` and `cognitioncom-blog-devin-fusion` to the existing `sources` list; full list otherwise unchanged)

**Two new bullets added to `## Current patterns`, placed after the existing "Pipeline versus loop" bullet:**

```
- **Agentic MapReduce.** For whole-codebase tasks where a result is only trustworthy if every file was considered (security scanning, breaking-change detection, code-quality enforcement, large-scale migration), a single search-driven agent burns most of its budget just *finding* the relevant code, and its context becomes a shared bottleneck as the run grows because unrelated discoveries keep competing for attention. Agentic MapReduce inverts classic MapReduce: an agent still decides what matters (**Plan**, authoring inspectable, version-controllable "selectors" — Tree-sitter queries, symbol/type queries, import-graph traversals, lexical patterns for repo-specific conventions), but the selector then runs deterministically over the entire repo with no model in the loop (**Shard**), producing a finite, bounded work queue instead of an open-ended search. Each shard is investigated by a fresh, focused worker in parallel (**Map**), and a final Reduce agent dedupes, reconciles, and composes cross-shard relationships — such as chaining an unauthenticated ID leak with an ID-gated RCE into one severe finding, or grouping migration call sites under the API change that caused them. Coverage is guaranteed by construction (the pipeline is complete only when the deterministic queue is exhausted) and cost tracks the volume of *relevant* code rather than repo size, since the Reducer also reasons over compressed per-shard conclusions rather than full transcripts. [Devin Security Swarm](../tools/devin.md) is the first production instance, adding a fifth **Verify** stage that reproduces serious findings in a sandbox; re-runs after the initial Plan only reprocess files changed since the last scan. *Source: Cognition/Devin engineering blog (2026-07-14)*
- **Sidekick multi-model harness.** Run two parallel, fully capable agents on the same task: a frontier model and a cheaper "sidekick" model, each with its own tools and its own persistent, separately-cached context. The frontier model takes minimal actions itself — it plans, interprets ambiguity, and does final review — while delegating mechanical or well-scoped subtasks to the sidekick; a lightweight classifier can reassign which model is "in charge" mid-session. Unlike a single model calling a "smart friend" or advisor tool per-query, which pays an expensive cache-miss cost on every cross-model call because the invoked model's context isn't shared in a cacheable way, the sidekick pattern keeps both models' contexts persistently cached and times any model switch to coincide with a context-compaction boundary — a point that would trigger a cache miss anyway — so the switch is effectively free. Devin Fusion reports holding frontier-level performance at 35% lower cost on a cost-aware coding benchmark (41% with a stronger base model), and drove 88% of one company's internal merged PRs entirely automatically. Contrast with the escalate-on-demand [Advisor strategy](advisor-strategy.md), which shares one persistent executor and calls a second model only per-decision rather than running two persistent agents in parallel. *Source: Cognition/Devin engineering blog (2026-06-29)*
```

**New line added under `## Where these patterns surfaced`:**

```
- Cognition's Agentic MapReduce writeup cites three 2026 studies motivating whole-codebase agent limits: Zhang et al.'s *FastContext* found repository reading/searching consumes over half of coding-agent tool-use turns across 300 SWE-bench Multilingual trajectories; Zeng et al.'s *LOCA-bench* (ICML 2026) showed agent success falling sharply as environment description length grows (e.g. Claude Opus 4.5 96.0%→34.0% from 8K to 128K tokens); Ko et al. found search agents terminate with an underverified answer on 52.1% of multi-constraint search tasks.
```

**`## Recent changes` — replace with (drops the oldest entry, spilled below):**

```
- [2026-07-14] Expanded Agentic MapReduce from a passing mention into a full pattern entry: deterministic Plan/Shard/Map/Reduce (+Verify for Security Swarm) architecture, sourced from Cognition's engineering writeup, with three supporting whole-codebase-agent-limits research citations.
- [2026-06-29] Added Sidekick multi-model harness pattern: persistent frontier + cheaper sidekick agents, cache-aware mid-session model switching at compaction boundaries; contrasted with per-call advisor/smart-friend escalation.
- [2026-07-08] Added loop-tempo selection from Andy Matuschak: fast controlled loops and slow delegated loops are easier to sustain than mid-speed partial-control loops.
- [2026-07-08] Linked PR review artifacts and repo-local review standards to the dedicated AI PR/code-review workflow.
- [2026-07-06] Shepherd proposal adds Git-like rollback/forking as a live-agent recovery primitive.
- [2026-07-04] Dhinakaran and Seldo map loop discourse into execution, task/Ralph, product/software-factory, system/autoresearch, and oversight loops; they emphasize exit signals and per-loop autonomy dials.
- [2026-06-26] Added AI review standards and review-noise failure mode from code-review workflow coverage.
- [2026-06-24] Token-tightening coverage adds AI FinOps controls: budgets, model routing, prompt caching, cheaper defaults, checkpoints, and outcome-based spend review.
- [2026-07-01] AIEWF / Latent Space software-factory coverage adds lifecycle-level factory loop and FDE/agent-engineer rollout pattern.
- [2026-07-03] AI Engineer World Fair loop debate: agents are moving from hype to control-layer problems; surveys report widespread agent use but primitive controls and review bottlenecks.
```

(This drops "[2026-06-30] Anthropic published the Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops," spilled to history below.)

**`## Sources` — add:**

```
- [Agentic MapReduce (Cognition/Devin blog)](../sources/articles/devinai-blog-agentic-map-reduce.md)
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
```

### wiki/history/workflows/agentic-orchestration-patterns.md (new — spill)

```md
# Agentic orchestration patterns — History

## Archived from current page on 2026-07-14

- [2026-06-30] Anthropic published the Claude Code loop taxonomy: turn-based, goal-based, time-based, and proactive loops.
```

### wiki/workflows/advisor-strategy.md (updated)

**Frontmatter:**
```
as_of: 2026-06-29
sources: [advisor-strategy, ainews-ideogram-june-2026, cognitioncom-blog-devin-fusion]
```

**New section added after `## Caveats`, before `## Related`:**

```
## Contrast with the sidekick pattern (2026-06-29)

Cognition's Devin Fusion post explicitly critiques per-call escalation tools like this one (and its own earlier "Smart Friend" prototype): querying a second model per call means that model's context isn't shared in a cacheable way, so every advisor invocation pays a full, uncached price. Devin Fusion's [sidekick pattern](../workflows/agentic-orchestration-patterns.md) avoids this by running the frontier and cheaper model as two persistent, separately-cached agents for the whole session, switching which one leads only at natural cache-invalidation points (context compaction). The tradeoff: sidekick needs a harness built for two parallel long-running agents, while the advisor tool is a single API primitive addable to an existing single-agent loop.
```

**`## Recent changes` — add at top:**

```
- [2026-06-29] Added contrast with Cognition's sidekick multi-model harness pattern, which avoids the advisor tool's per-call cache-miss cost by keeping both models' contexts persistently cached.
```

**`## Sources` — add:**

```
- [Devin Fusion: Frontier Performance at 35% Lower Cost](../sources/articles/cognitioncom-blog-devin-fusion.md)
```

### wiki/tools/windsurf.md (new)

````md
---
title: Windsurf
type: tool
domains: [coding, agents]
subcategory: agentic-coding-workspace
tags: [closed-source, agentic]
as_of: 2026-07-14
sources: [devinai-blog-windsurf-adaptive]
---

# Windsurf

Windsurf is Cognition's AI coding workspace — this announcement was published on Devin's (Cognition's) blog, reflecting Windsurf's integration under the same company. On 2026-07-14, Cognition shipped an **Adaptive** model router, a redesigned model picker with pricing transparency, and removed daily usage limits for Max subscribers, in direct response to user complaints that the product's newer token-based pricing was too opaque and too restrictive.

## Current status (as of 2026-07-14)

- **Adaptive router:** automatically selects the best underlying model per task to avoid overusing premium models and make quota last longer; billed at a flat per-token rate — $0.50/M input, $2.00/M output, $0.10/M cache read as a promotional rate for the first two weeks; rolling out to all self-serve tiers (Pro, Max, Teams)
- **Model picker redesign:** shows live token pricing per model (e.g. Claude Opus 4.6), a prompt-cache timer integrated into the context window indicator, and post-message token/cost breakdowns
- **Max plan daily limits removed:** only the weekly quota remains for Max users, aimed at bursty power-user workflows; daily limits remain on other tiers as a spend safety net
- Cognition says it is building a more efficient harness for Windsurf with a multi-model architecture and subagents, to be detailed later

## Why it matters

The changes are a direct response to backlash over Windsurf's token-based pricing model: opaque billing and daily caps that especially penalized heavy users. Adaptive routing and transparent per-token pricing mirror a broader industry pattern — cost-aware model routing — now applied to a per-seat coding product rather than an API.

## Recent changes

- [2026-07-14] Launched Adaptive model router, transparent model-picker pricing (with prompt-cache timer), and removed Max-plan daily limits.

## Sources

- [Introducing Adaptive: a smarter way to use Windsurf](../sources/articles/devinai-blog-windsurf-adaptive.md)
````

### wiki/state-of/coding.md (updated)

**Frontmatter:**
```
as_of: 2026-07-14
sources: [..., devinai-blog-windsurf-adaptive, devinai-blog-agentic-map-reduce, cognitioncom-blog-devin-fusion]
```
(append these three to the existing `sources` list; full list otherwise unchanged)

**`### Agentic coding workspace` — add a new bullet:**

```
- [Windsurf](../tools/windsurf.md) — Cognition (Devin's parent); Adaptive model router auto-selects models to conserve quota at a flat per-token rate; transparent per-token pricing in the model picker; Max plan daily limits removed *(as of 2026-07-14)*
```

**`### Terminal coding agent` — add a new bullet (Devin was previously missing from this dashboard despite its own `terminal-coding-agent` subcategory):**

```
- [Devin](../tools/devin.md) — Cognition; Devin Fusion (preview) multi-model "sidekick" harness matches frontier performance at 35% lower cost (41% with Fable 5) on FrontierCode Extended; Security Swarm's Agentic MapReduce architecture now documented, reporting 72% recall on a CVE-pinned vulnerability benchmark *(as of 2026-07-14)*
```

**`## Recent changes` — replace with (drops the 5 oldest entries, spilled below):**

```
- [2026-07-14] Windsurf (Cognition) shipped Adaptive model router, transparent per-token pricing in the model picker, and removed daily quota limits for Max users.
- [2026-06-29] Devin Fusion (preview): multi-model "sidekick" harness matches frontier performance at 35% lower cost on FrontierCode Extended; Devin added to the Terminal coding agent subcategory alongside the newly documented Agentic MapReduce architecture.
- [2026-07-02] Fable 5 returned to coding-tool surfaces; Sonnet 5 testing reinforced cost-per-completed-task as a better routing metric than token list price.
- [2026-06-30] Cursor iOS beta adds mobile launch/control for always-on cloud agents and desktop agents.
- [2026-06-30] Official Sonnet 5 launch confirms Claude Code availability and `claude-sonnet-5` API access.
- [2026-07-02] Z.ai launched ZCode for GLM-5.2, a signal that open coding models are building product ecosystems around long-context workflows rather than competing only as checkpoints.
- [2026-06-30] Anthropic published a Claude Code loop taxonomy tying task type to primitives: turn-based prompts, `/goal`, `/loop` or `/schedule`, and proactive routines composed with skills, dynamic workflows, and auto mode.
- [2026-06-17] SpaceX acquires Cursor ($60B all-stock); Cursor Origin launched (agent-native git/code hosting); jointly trained xAI model coming to both Cursor and Grok Build — completes a model + IDE + hosting vertical stack
- [2026-06-17] Claude Fable 5 suspended under US export controls; had reached #1 on DeepSWE/FrontierSWE; Claude Code + Fable 5 [max] scored 77 on DeepSWE before ban; Claude Code + Opus 4.8 is now the accessible Anthropic coding stack
- [2026-05-28] Claude Code adds dynamic workflows (research preview): the `ultracode` effort setting lets Claude write orchestration scripts that fan tens-to-hundreds of parallel subagents, verify findings (with adversarial agents) before folding them in, and iterate to convergence; runs checkpoint and resume across hours-to-days. On by default for Max/Team/API, admin-enabled for Enterprise; uses substantially more tokens. Bun's Zig→Rust port (~750K LOC Rust, 99.8% tests passing, 11 days) is the flagship case.
```

### wiki/history/state-of/coding.md (updated — spill)

**Append a new archive block at the end of the file:**

```
## Archived from current page on 2026-07-14

- [2026-05-15] Codex mobile preview: steer sessions from phone while agent runs on devbox; Remote SSH GA; enterprise 30-day switch promo (2 months free). Prime Intellect nanoGPT speedrun: both Opus 4.7 and GPT-5.5 beat human baseline in autonomous ML optimization (~10K runs)
- [2026-05-15] xAI Grok Build enters the terminal coding agent category: plan mode + parallel worktree subagents at feature parity with Claude Code's core agent patterns; early beta, SuperGrok Heavy only
- [2026-05-15] IDE convergence: GitHub Copilot App (technical preview), VS Code Agents window, and Cursor cloud dev environments all move toward managing parallel agent sessions as the primary UX — three major tools, same week, same direction
- [2026-05-13] Model-harness fit is becoming a product moat: edit formats, action spaces, and tool-call reliability can matter as much as raw model benchmark scores in coding agents.
- [2026-05-13] Codex and Claude Code are increasingly framed as workflow operating systems: command packs, browser-pane workflows, inbox triage, long-running goals, and multi-agent supervision are now part of the coding-agent competition.
```

### wiki/concepts/agent-evals.md (updated)

**Frontmatter:**
```
as_of: 2026-07-14
sources: [agents-evals-deep-research, cost-aware-agent-evaluation-2026-04-28, vending-bench-andon-june-2026, ainews-not-much-happened-2026-07-02, autoresearch-agent-recipes-2026-07, ai-code-review-eval-integrity-2026-06, dashbench-code-review-understanding-2026-07, cognitioncom-blog-ai-productivity]
```

**New section inserted after `## Dollar-denominated long-horizon evals`, before `## How this changes eval design`:**

```
## Human-hours-equivalent productivity estimation

A complementary approach to dollar-denominated evals: instead of scoring simulated economic outcomes, estimate the real engineering hours a completed agent session saved, then convert to dollars via engineering rates.

**Cognition's Devin estimator (June 2026):** reviews each completed session, classifies whether it produced useful (typically merged) work, then estimates the human-engineer-hours-equivalent — discounting agent-specific artifacts (retries, environment setup, summary reports) a human wouldn't produce, crediting only work the user hadn't already specified, and conservatively assuming the human reference already has the relevant expertise. Trained and validated against 258 self-reported sessions from 126 users; the held-out estimator reaches `r_log = 0.74`, deliberately calibrated to underestimate rather than overestimate. Now running in production with customers.

**Prior work it builds on:**
- METR (Feb 2026) used GPT-4o/GPT-5 on compressed Claude Code transcripts from 7 internal staff, reaching `r_log = 0.83` on 34 labeled sessions — a stronger correlation, but on a far smaller and less diverse sample.
- Anthropic (2026) estimated task duration for 1,000 open-source Jira tickets using only the ticket title/description (no execution trace), reaching `r_log = 0.46` (human estimators on the same tickets reached 0.67).

The comparison suggests granular session data (full trace, user messages, codebase context) meaningfully outperforms text-only estimation, and that noisy individual predictions can still be useful in aggregate: errors are roughly unbiased across sessions, so per-session noise cancels out at deployment scale even though individual estimates can be off by 2-3x.
```

**`## Related` — add:**

```
- [AI enablement — software development](../training/ai-enablement-software-development.md) — production evidence of this estimator in use
```

**`## Recent changes` — add at top:**

```
- [2026-07-14] Added Cognition's human-hours-equivalent productivity estimator (`r_log = 0.74`) as a second dollar/hours-denominated eval approach alongside Vending Bench; compared against METR and Anthropic prior effort-estimation work.
```

**`## Sources` — add:**

```
- [Estimating the Productivity of an Autonomous AI Software Engineer](../sources/articles/cognitioncom-blog-ai-productivity.md)
```

### wiki/training/ai-enablement-software-development.md (updated)

**Frontmatter:**
```
as_of: 2026-07-14
sources: [..., cognitioncom-blog-ai-productivity]
```
(append `cognitioncom-blog-ai-productivity` to the existing `sources` list; full list otherwise unchanged)

**`## Evidence from practice` — add:**

```
- Cognition (Devin, July 2026): built an automated system estimating human-engineering-hours-equivalent per completed session, validated against 258 self-reported sessions from 126 users across enterprise customers, reaching `r_log = 0.74` on held-out data — stronger than Anthropic's ticket-text-only approach (0.46) though behind METR's smaller-sample internal study (0.83); deliberately calibrated to underestimate; now running in production with customers. See [Agent evals](../concepts/agent-evals.md) for the full methodology comparison.
```

**`## Recent changes` — add at top:**

```
- [2026-07-14] Added Cognition's production session-productivity estimator (`r_log = 0.74`) as evidence that hours/dollar-denominated AI engineering ROI measurement is moving from research into deployed practice.
```

### wiki/sources/articles/devinai-blog-agentic-map-reduce.md (new)

````md
---
title: Agentic MapReduce (Cognition/Devin blog)
type: source
source_type: article
source_file: raw/articles/2026-07-14-devinai-blog-agentic-map-reduce.md
url: https://devin.ai/blog/agentic-map-reduce
published: 2026-07-14
ingested: 2026-07-14
domains: [coding, agents, cybersecurity]
---

# Agentic MapReduce (Cognition/Devin blog)

Cognition names and details the architecture behind Devin Security Swarm: a Plan agent authors deterministic, inspectable "selectors" that a deterministic pass runs over every file in the repo (Shard), guaranteeing coverage by construction; parallel focused workers investigate each bounded shard (Map); a Reducer dedupes findings and composes cross-shard relationships like chained exploits (Reduce). Security Swarm adds a fifth Verify stage that reproduces serious findings in a sandbox. Cognition reports 72% recall on a CVE-pinned ground-truth benchmark, ahead of rival scanners tested, at a fraction of the cost. The post cites three 2026 studies (FastContext, LOCA-bench, and an "Illusory Completion in Search Agents" paper) to motivate why search-driven single agents struggle at whole-codebase scale.

## Influenced pages

- [Devin](../../tools/devin.md) — Agentic MapReduce architecture detail, 72% recall benchmark
- [State of Cybersecurity](../../state-of/cybersecurity.md) — updated Devin leader line
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — expanded Agentic MapReduce pattern entry
- [State of Coding](../../state-of/coding.md) — Devin added to Terminal coding agent subcategory

## Key claims extracted

- Agentic MapReduce stages: Plan (agent authors selectors) → Shard (deterministic, whole-repo) → Map (parallel bounded workers) → Reduce (dedupe + cross-shard synthesis); Security Swarm adds Verify (sandboxed reproduction).
- Selectors are inspectable, version-controlled, and reusable across re-runs; re-runs after the first scan only process files changed since the last commit scanned.
- Devin Security Swarm: 72% recall on a CVE-pinned ground-truth set (GitHub Advisory Database, dozens of cases, 12+ languages), ahead of other tested scanners, at a fraction of their cost.
- Cited research: Zhang et al. *FastContext* (2026) — repo exploration consumes >50% of coding-agent tool-use turns across 300 trajectories; Zeng et al. *LOCA-bench* (ICML 2026) — agent success falls sharply as context/environment size grows; Ko et al. — search agents terminate underverified on 52.1% of multi-constraint tasks.
````

### wiki/sources/articles/devinai-blog-windsurf-adaptive.md (new)

````md
---
title: Introducing Adaptive — a smarter way to use Windsurf
type: source
source_type: article
source_file: raw/articles/2026-07-14-devinai-blog-windsurf-adaptive.md
url: https://devin.ai/blog/windsurf-adaptive
published: 2026-07-14
ingested: 2026-07-14
domains: [coding, agents]
---

# Introducing Adaptive — a smarter way to use Windsurf

Cognition launched three Windsurf updates in response to user backlash over opaque, restrictive token-based pricing: an Adaptive model router that auto-selects the best model per task at a flat per-token rate, a redesigned model picker showing live token pricing and a prompt-cache timer, and removal of daily quota limits for Max-plan users (weekly limit remains). Cognition also previewed a future harness with multi-model architecture and subagents.

## Influenced pages

- [Windsurf](../../tools/windsurf.md) — new tool page; Adaptive router, pricing-transparent picker, Max daily-limit removal
- [State of Coding](../../state-of/coding.md) — Windsurf added to Agentic coding workspace subcategory

## Key claims extracted

- Adaptive model router rolling out to all self-serve tiers (Pro, Max, Teams); billed at $0.50/M input, $2.00/M output, $0.10/M cache read tokens (promotional rate, first 2 weeks).
- Model picker now shows per-model token pricing and integrates a prompt-cache timer into the context window indicator; response cards show token counts.
- Max users no longer have a daily quota (weekly limit remains); other tiers keep daily limits as a spend safety net.
- Cognition is developing a more efficient harness for Windsurf with multi-model architecture and subagents (unspecified timeline).
````

### wiki/sources/articles/cognitioncom-blog-devin-fusion.md (new)

````md
---
title: Devin Fusion — Frontier Performance at 35% Lower Cost
type: source
source_type: article
source_file: raw/articles/2026-07-14-cognitioncom-blog-devin-fusion.md
url: https://cognition.com/blog/devin-fusion
published: 2026-06-29
ingested: 2026-07-14
domains: [coding, agents]
---

# Devin Fusion — Frontier Performance at 35% Lower Cost

Cognition introduces Devin Fusion, a multi-model "sidekick" harness: a frontier model and a cheaper sidekick model each run as full agents with their own tools and persistent, separately-cached context; the frontier model plans and reviews while delegating mechanical work to the sidekick, and a classifier can dynamically reassign which model leads mid-session, timed to coincide with context-compaction boundaries to avoid extra cache-miss cost. On the new FrontierCode Extended benchmark, Fusion matches frontier performance at 35% lower cost than Opus 4.8/GPT-5.5 alone (41% lower with Fable 5, measured pre-suspension). Internally, 88% of Cognition's merged PRs were driven entirely by the automated Fusion router. Preview available at app.devin.ai/signup. Published 2026-06-29.

## Influenced pages

- [Devin](../../tools/devin.md) — Devin Fusion feature detail
- [FrontierCode](../../benchmarks/frontiercode.md) — new FrontierCode Extended tier scores/costs
- [Agentic orchestration patterns](../../workflows/agentic-orchestration-patterns.md) — new Sidekick multi-model harness pattern
- [Advisor strategy](../../workflows/advisor-strategy.md) — contrast with per-call cache-miss cost
- [State of Coding](../../state-of/coding.md) — Devin added to Terminal coding agent subcategory

## Key claims extracted

- Devin Fusion: two parallel agents (frontier + cheaper "sidekick"), each with its own persistent, separately-cached context; frontier model plans/reviews, delegates mechanical work.
- Dynamic mid-session routing switches models at context-compaction boundaries specifically to avoid paying an extra cache-miss cost.
- On FrontierCode Extended: Fusion matches frontier performance at 35% lower cost vs. Opus 4.8/GPT-5.5; 41% lower cost with Fable 5 (internal, pre-suspension measurement).
- 88% of Cognition's internal merged PRs were driven entirely by the automated Fusion router.
- Published 2026-06-29; preview available at app.devin.ai/signup.
````

### wiki/sources/articles/cognitioncom-blog-ai-productivity.md (new)

````md
---
title: Estimating the Productivity of an Autonomous AI Software Engineer
type: source
source_type: article
source_file: raw/articles/2026-07-14-cognitioncom-blog-ai-productivity.md
url: https://cognition.com/blog/ai-productivity
ingested: 2026-07-14
domains: [coding, agents]
---

# Estimating the Productivity of an Autonomous AI Software Engineer

Cognition built an automated system that reviews each completed Devin session, classifies whether it produced useful work, and estimates the equivalent human-engineering hours saved — crediting only work the user hadn't already specified and conservatively assuming the reference engineer already has relevant expertise. Trained and validated on 258 self-reported sessions from 126 users (233 held-out for evaluation), the estimator reaches `r_log = 0.74`, calibrated to deliberately underestimate rather than overestimate. Cognition positions this as the first automated system measuring AI engineering productivity in production, and compares it favorably to Anthropic's ticket-text-only approach (`r_log = 0.46`) while noting METR's smaller, more homogeneous internal sample scored higher (`r_log = 0.83`). No explicit publish date was visible in the fetched content; using ingest date as `as_of` fallback per the date rule.

## Influenced pages

- [Devin](../../tools/devin.md) — productivity estimator feature
- [Agent evals](../../concepts/agent-evals.md) — new Human-hours-equivalent productivity estimation section
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — evidence from practice

## Key claims extracted

- Estimator classifies session usefulness (merged-PR filter plus a classifier for non-PR sessions), then predicts human-engineer-hours-equivalent.
- Design principles: reason about the human's likely path (not the agent's actual trajectory), credit only work the user hadn't already specified, account for codebase familiarity, assume relevant expertise (conservative).
- Dataset: 258 sessions / 126 users across enterprise customers; 233 held-out evaluation sessions.
- `r_log = 0.74` on held-out data; calibrated via log-space regression (`h = 2.28 × m^0.923`, ~2.08x multiplicative correction); reports the unadjusted, deliberately conservative total.
- Compares to METR (`r_log = 0.83`, 34 sessions, 7 internal staff) and Anthropic (`r_log = 0.46`, 1,000 Jira tickets, text-only, no execution trace).
- Threats to validity: self-reported ground truth (interview bias), sampling skew toward engaged users, hours ≠ business value, hours don't capture post-merge defects/quality.
- Now running in production with customers.
````

## Open questions

- Windsurf shipped from the `devin.ai` blog domain, which strongly suggests Cognition ownership/integration, but the post itself doesn't explicitly restate "Cognition owns Windsurf." I've phrased the new tool page's framing around the observable fact (published on Devin's blog) rather than asserting a formal acquisition — flag if you'd like this phrased more strongly or more cautiously.
	- Yes, Cognition owns Windsurf
- The `state-of/coding.md` and `workflows/agentic-orchestration-patterns.md` spills fix pre-existing cap overflows/near-overflows that this ingest happened to touch. I did not touch the other 3 pages `scripts/recent_changes_cap.py` separately flagged (`state-of/agents.md`, `state-of/creative.md`, `state-of/models.md`) since this ingest doesn't otherwise touch them — let me know if you'd like a separate maintenance pass for those.
	- don't
- The `cognitioncom-blog-ai-productivity.md` source page has no `published:` date (none was visible in the fetched content) — `as_of` on derived pages uses the 2026-07-14 ingest date as fallback, per the date rule. Let me know if you have the actual publish date.
	- I don't have it
- I added Devin to `state-of/coding.md`'s Terminal coding agent subcategory since its own tool-page frontmatter already declares that subcategory but the dashboard never listed it — this looked like a real gap rather than a deliberate omission; flag if there was a reason it was left out.
	- ok
