---
type: proposal
source: raw/newsletters/2026-08-08-ainews-zawinskis-law-of-multiagents.md
status: pending
created: 2026-09-07
---

# Proposal: Harness choice keeps outweighing model choice

## Summary

### The source

On 2026-08-08, AINews' "Zawinski's Law of MultiAgents" issue reported on a SWE-bench Pro comparison showing that swapping the *harness* around a fixed model changed pass@1 more than swapping the model did: scores spanned 23-52% on GLM-5.2 and 15-36% on Gemma 4 26B depending on which harness ran the task, and harness rankings barely transferred between models — a rank correlation of just -0.05, meaning the best harness for one model was often not the best harness for another. The same issue covered Databricks' account of cutting its own internal AI coding spend by up to 90% while usage kept growing, breaking the savings down into roughly 50% from switching default models to cheaper/more efficient options, 30% from smarter routing, 10% from giving engineers visibility into their own spend with adaptive budgets, and 10% from pruning bloated context and tuning harnesses. Three days later, an 2026-08-11 AINews issue (whose lead story is Meta's Muse Glimmer release, covered in a separate proposal) added a third data point: Composio ran DeepSeek V4 Flash through four different agent harnesses on the same 30 agentic tasks and found Pi Agent came out both the cheapest and the best-performing of the four — a second concrete demonstration that, for a fixed model, harness choice alone can decide the outcome.

### What changes

The wiki's harness page already argues, from earlier sourcing, that "the same model can underperform in a mismatched product surface" and that benchmark results should be read as model+harness+environment, not model-only. These three new data points make that claim concrete with real numbers instead of a general assertion.

- **Harness (agent)** gains a new bullet under "Harness vs model" citing the SWE-bench Pro harness-swap range and near-zero harness-ranking transfer across models, plus the Composio DeepSeek V4 Flash bake-off as a second case; new Recent-changes entry, dated 8/11 (page's newest source date). The page is at its 10-entry Recent-changes cap, so the oldest entry (2026-05-18, the "Code as Agent Harness" survey) spills to history.
- **Cost-aware AI task routing** gains a new Evidence-from-practice bullet describing Databricks' internal spend-reduction breakdown — distinct from the page's existing "Databricks' real-PR coding-agent benchmark" bullet, which covers a different Databricks study (a quality benchmark, not an internal FinOps account).
- Two new source pages, one per raw newsletter issue.

### What to weigh

All three data points come from secondary AINews summaries of primary posts (the SWE-bench Pro analysis credited to @joelniklaus, Databricks' own account relayed via Patrick Wendell/@alighodsi, and Composio's own benchmark post) rather than the primary posts themselves — the same relay-sourcing pattern already used elsewhere on both target pages, not weaker than usual. Nothing else here needs weighing.

## Intended changes

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

- [ ] **Update** `wiki/concepts/harness.md` — new "Harness vs model" bullet, new Recent-changes entry, as_of bump, oldest entry spills to history
    > See draft below

- [ ] **Update** `wiki/training/cost-aware-ai-task-routing.md` — new Evidence-from-practice bullet on Databricks' internal AI spend reduction
    > See draft below

- [ ] **Spill** `wiki/concepts/harness.md` → `wiki/history/concepts/harness.md` — oldest Recent-changes entry ([2026-05-18] "Code as Agent Harness" survey) falls off the cap

- [ ] **Create** `wiki/sources/newsletters/ainews-zawinskis-law-multiagents-2026-08-08.md` — source summary

- [ ] **Create** `wiki/sources/newsletters/ainews-muse-glimmer-spark-2026-08-11.md` — source summary

## Page drafts

### wiki/concepts/harness.md (updated)

```md
---
title: Harness (agent)
type: concept
domains: [agents]
tags: [agentic]
as_of: 2026-08-11
sources: [agentic-thinking-lin, langchain-better-harness, openai-agents-sdk-evolution, notion-token-town, ainews-openclaw-2026-04-18, garrytan-confusion-protocol, matt-pocock-ddd-adr, harness-engineering-patterns, claude-code-leak-architecture, harness-engineering-early-april, skills-and-plugin-packaging-late-march, harness-engineering-march, harness-debate-march, shopify-latent-space-april-2026, ainews-2026-04-22, thecode-april-22-2026, agent-infrastructure-harness-2026-05-01, mattpocock-dictionary-of-ai-coding, model-harness-fit-2026-05-13, shopify-claude-code-bessemer-2026-05, gas-city-software-factory-2026-05, cloudflare-glasswing-2026-05, loopcraft-june-2026, rl-harness-quality-june-2026, aiewf-loops-debate-2026-07-03, autoresearch-agent-recipes-2026-07, claude-tag-slack-agent-2026-06, gemini-managed-agents-2026-07, gray-swan-ai-security-2026-06, effective-feedback-compute-harness-2026-05, claude-managed-agents-updates-2026-05, code-as-agent-harness-paper, aiewf-2026-five-trends-latentspace, ainews-zawinskis-law-multiagents-2026-08-08, ainews-muse-glimmer-spark-2026-08-11]
---
```

In `## Harness vs model`, append a new bullet after the existing paragraphs (after "Treat benchmark results as model + harness + environment, not model-only." and before the "Practitioners are increasingly using..." paragraph):

```md
Two 2026-08 data points make the split measurable rather than anecdotal. A SWE-bench Pro comparison found harness choice changed pass@1 more than many model upgrades do: scores ranged 23-52% on GLM-5.2 and 15-36% on Gemma 4 26B depending on which harness ran the task, with harness rankings barely transferring between models (rank correlation of -0.05) — the best harness for one model is often not the best for another. Separately, Composio ran DeepSeek V4 Flash through four different harnesses on the same 30 agentic tasks and found Pi Agent both the cheapest and the best-performing of the four, reinforcing the same conclusion with a second model.
```

In `## Recent changes`, prepend the new entry and drop the oldest (which moves to history):

```md
## Recent changes

- [2026-08-11] Added SWE-bench Pro harness-swap data (23-52% on GLM-5.2, 15-36% on Gemma 4 26B, -0.05 harness-ranking rank correlation across models) and a Composio DeepSeek V4 Flash four-harness bake-off (Pi Agent cheapest and best-performing) as concrete numbers behind the harness-vs-model claim.
- [2026-07-14] Added the Lilian Weng 2023-vs-2026 essay contrast and Anthropic's "grown, not designed" framing, from AI Engineer World's Fair 2026 coverage.
- [2026-07-08] Gemini API managed agents add hosted harness primitives: MCP support, background execution, custom function calling, credential refresh, and stateful agent interactions.
- [2026-07-03] Added control-layer framing from AI Engineer World Fair: permissions, cost ceilings, recovery, and review routing are part of the harness boundary.
- [2026-07-01] Added agent recipes as a harness packaging pattern: model choices, evals, judges, human expertise, failure history, and signal processing bundled with the workflow.
- [2026-06-24] Claude Tag coverage adds org-embedded agent identity, permission scoping, and Slack-channel memory boundaries as harness concerns.
- [2026-06-22] Gray Swan security coverage adds prompt injection, exfiltration, identity, permissions, and automated red teaming as harness-boundary concerns for tool-using agents.
- [2026-06-05] Added RL harness quality section: 8 failure modes taxonomy from Auriel W (Google Gemini RL team); "5% failure rate = harness problem, not model problem"
- [2026-05-30] Added Effective Feedback Compute and model-specific harness profiles as harness-quality signals beyond token/tool counts.
- [2026-05-20] Claude Managed Agents added self-hosted sandboxes (public beta) and MCP tunnels (research preview), extending the harness security boundary so tool execution and private MCP connectivity can run on customer infrastructure while Anthropic keeps the orchestration loop.
<!-- [2026-05-18] "Code as Agent Harness" survey spills to wiki/history/concepts/harness.md -->
```

In `## Sources`, append:

```md
- [AINews — Zawinski's Law of MultiAgents](../sources/newsletters/ainews-zawinskis-law-multiagents-2026-08-08.md)
- [AINews — Muse Glimmer and Spark: Open Weights return Personal Superintelligence promise](../sources/newsletters/ainews-muse-glimmer-spark-2026-08-11.md)
```

### wiki/history/concepts/harness.md (new)

```md
# Harness (agent) — History

Older recent-change entries spilled from [Harness (agent)](../../concepts/harness.md).

## Archived from current page on 2026-09-07

- [2026-05-18] "Code as Agent Harness" survey (arXiv:2605.18747) frames code as the operational substrate for agent reasoning, planning, memory, tool use, and multi-agent coordination.
```

### wiki/training/cost-aware-ai-task-routing.md (updated)

```md
---
as_of: 2026-08-08
sources: [task-routing-cost-discipline-2026-05-13, thinking-machines-financial-expert-judgment-2026-07-02, superhuman-bridgewater-thinking-machines-2026-07-02, local-ai-infrastructure-2026-06, token-tightening-ai-finops-2026-06, efficiencymaxxing-model-routing-2026-07, fable-unknowns-routing-2026-07, the-code-databricks-coding-benchmark-2026-07-10, databricks-benchmarking-coding-agents-2026-07, the-code-eval-data-moat-2026-07-13, ainews-devin-fusion-router-moat-2026-07-14, arkadium-game-lab-small-model-economics-2026-07-19, ainews-zawinskis-law-multiagents-2026-08-08]
```

In `## Evidence from practice`, append a new bullet after the existing "Databricks' real-PR coding-agent benchmark" bullet:

```md
- **Databricks' internal AI FinOps breakdown.** Separately from its coding-agent benchmark, Databricks detailed how it cut its own internal AI coding spend by up to 90% in some scenarios while usage kept growing: shifting defaults to cheaper/more efficient models (~50% of the savings), smart routing (~30%), user visibility and adaptive budgeting (~10%), and pruning context bloat plus harness tuning (~10%). The breakdown is a concrete example of the page's FinOps controls actually applied at scale, not just recommended.
```

### wiki/sources/newsletters/ainews-zawinskis-law-multiagents-2026-08-08.md (new)

```md
---
title: "AINews — Zawinski's Law of MultiAgents"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-08-ainews-zawinskis-law-of-multiagents.md
url: https://www.latent.space/p/ainews-zawinskis-law-of-multiagents
published: 2026-08-08
ingested: 2026-09-07
domains: [agents, cybersecurity]
---

# AINews — Zawinski's Law of MultiAgents

AINews recap covering OpenAI's Black Hat talk on the Hugging Face/Artifactory autonomous-agent incident (coining "Zawinski's Law of MultiAgents": every agent attempts to expand until it can message other agents), OpenAI classifying its upcoming Astra model as unable to rule out "Critical" cyber capability, LangChain's Managed Deep Agents beta, Claude Code's new session-to-session messaging and classifier-mediated auto-mode default, a SWE-bench Pro harness-vs-model comparison, Databricks' internal AI-spend-reduction breakdown, and continued DeepSeek V4 Flash adoption momentum.

## Influenced pages

- [concepts/harness](../../concepts/harness.md) — SWE-bench Pro harness-swap data point
- [training/cost-aware-ai-task-routing](../../training/cost-aware-ai-task-routing.md) — Databricks internal AI FinOps breakdown

## Key claims extracted

- SWE-bench Pro: swapping agent harness changed pass@1 more than many model upgrades — 23-52% on GLM-5.2, 15-36% on Gemma 4 26B, harness-ranking rank correlation of -0.05 across models
- A 26B model in the right harness can approach a 744B model in the wrong one; 97% of input tokens were repeated conversation prefix, making prompt caching decisive
- Databricks cut internal AI coding spend up to 90% in some scenarios while usage grew: ~50% from cheaper/more efficient model defaults, ~30% from smart routing, ~10% from user visibility/adaptive budgeting, ~10% from context/harness pruning
```

### wiki/sources/newsletters/ainews-muse-glimmer-spark-2026-08-11.md (new)

```md
---
title: "AINews — Muse Glimmer and Spark: Open Weights return Personal Superintelligence promise"
type: source
source_type: newsletter
source_file: raw/newsletters/2026-08-11-ainews-muse-glimmer-and-spark-open-weights-retu.md
url: https://www.latent.space/p/ainews-muse-glimmer-and-spark-open
published: 2026-08-11
ingested: 2026-09-07
domains: [models, agents]
---

# AINews — Muse Glimmer and Spark: Open Weights return Personal Superintelligence promise

AINews recap of Meta's Muse Glimmer release (30B dense multimodal agent model, Apache 2.0, tuned for local always-on agents) alongside a sequel to Zuckerberg's "Personal Superintelligence" essay and a promise to open-weight Muse Spark 1.2 soon. Also covers Anthropic's unreleased research Claude improving a Riemann Hypothesis critical-line-zero bound, OpenAI's restricted-access GPT-5.6-Cyber launch under its Daybreak initiative, Claude Sonnet 5's introductory pricing becoming permanent, and a Composio harness bake-off comparing four agent harnesses on DeepSeek V4 Flash.

## Influenced pages

- [concepts/harness](../../concepts/harness.md) — Composio DeepSeek V4 Flash four-harness bake-off

## Key claims extracted

- Composio ran DeepSeek V4 Flash through four agent harnesses on the same 30 agentic tasks; Pi Agent was both the cheapest and the best-performing of the four
```

## Open questions

None — all three data points are clearly attributed within their AINews recaps.
