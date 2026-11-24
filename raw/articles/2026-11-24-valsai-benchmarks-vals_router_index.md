---
title: Vals Router Index
type: source
source_type: article
url: https://www.vals.ai/benchmarks/vals_router_index
fetched: 2026-11-24
---

# Vals Router Index

## Background

New models arrive every month, giving companies an expanding set of options with different strengths and prices. The frontier is jagged: different models lead different benchmarks on the [Vals Index](/benchmarks/vals_index), so even the strongest model is not the best choice for every kind of work. Keeping up means continually re-evaluating which model suits each application, an effort that grows with every workflow a company moves onto AI.

Model routers promise to take on that work, selecting a model for each request and weighing quality against cost. Agentic work raises the stakes: an agent may make hundreds of model calls to finish one task, a router can choose differently for each, and a cheaper step can create more work later. We therefore measure the quality and total cost of the finished task.

The Vals Router Index runs six routers through the same agents, tasks and graders as every model on the Vals Index: [Auto Router](https://openrouter.ai/docs/guides/routing/routers/auto-router) (OpenRouter), [Nexus Auto](https://docs.fireworks.ai/nexus/auto) (Fireworks) with two model pools, [Router](https://ramp.com/router) (Ramp), [Jev Router](https://openrouter.ai/typesafe/jev-router) (OpenRouter) and [Fugu Max](https://sakana.ai/fugu/) (Sakana), which coordinates several models on each task. The tasks come from the Index’s eight benchmarks of agentic work in finance, coding, law and tax, about 1,250 in all. We report results on the full Index and, separately, on its three coding benchmarks: Terminal-Bench, Vibe Code Bench and Code Migration, since many routers are tuned for coding. Each router ran with its default configuration, as a customer would get it out of the box, and is compared with every single model on the Index, run on the same tasks.

We built this evaluation on the Vals Index because it tests the kind of work routers are now sold for: long, tool-using agent tasks written and graded by people who do that work. Six of its eight benchmarks are private, and we run them under zero-data-retention agreements, so model providers cannot keep or train on the tasks.

For the comparisons below, a router’s **pool** means the models it used in our runs. Fugu Max (Sakana) does not disclose which models it calls, so it is left out of every comparison that needs its pool.

We’re eager to evaluate other routers. If you build one and want it evaluated, [get in touch with us here](mailto:contact@vals.ai).

---

## Results

None of the six routers sits on the cost and accuracy frontier: each was beaten on both score and cost by at least one single model. Nexus Auto with Sol (Fireworks) came closest: only DeepSeek V4.1 Flash 1017 beat it on both, for about half the cost, although its lead of about a point is within the margin of error. Router (Ramp) came next: DeepSeek V4.1 Flash 1017 scored about 3.5 points higher for about two thirds of its cost, and MiMo V2.6 Pro scored within the margin of error of Router (Ramp) for under half its cost.

None of the six routers sits on the cost and accuracy frontier: each was beaten on both score and cost by at least one single model. Nexus Auto with Sol (Fireworks) came closest: only DeepSeek V4.1 Flash 1017 beat it on both, for about a third of the cost, although its lead of about a point is within the margin of error. Router (Ramp) came next: DeepSeek V4.1 Flash 1017 scored about 5.5 points higher for about half its cost, and MiMo V2.6 Pro scored within the margin of error of Router (Ramp) for under half its cost.

### How the routers compared

**Each router against single-model alternatives**

| Router | Score (Full Index) | Cost per test | Best in its pool | Best at or below its cost |
| --- | --- | --- | --- | --- |
| Nexus Auto with Sol (Fireworks) | 60.0% | $1.25 | 63.9%GPT-6.1 Sol, $3.61 | 61.3%DeepSeek V4.1 Flash 1017, $0.66 |
| Router (Ramp) | 57.8% | $0.96 | 63.9%GPT-6.1 Sol, $3.61 | 61.3%DeepSeek V4.1 Flash 1017, $0.66 |
| Nexus Auto with Opus (Fireworks) | 56.5% | $9.22 | 64.2%Claude Opus 5.5, $24.41 | 66.8%Wonder Full, $6.81 |
| Jev Router (OpenRouter) | 55.7% | $5.30 | 69.0%Claude Sonnet 5.5, $15.87 | 63.9%GPT-6.1 Sol, $3.61 |
| Auto Router (OpenRouter) | 52.2% | $0.82 | 61.3%DeepSeek V4.1 Flash 1017, $0.66 | 61.3%DeepSeek V4.1 Flash 1017, $0.66 |

Score and cost per test

**Nexus Auto with Sol (Fireworks)** came closer to its strongest model than any other router: it scored 3.9 points below GPT-6.1 Sol for about a third of Sol’s cost. It also scored slightly above GLM 5.3, the other main model in its pool, for about a seventh of GLM 5.3’s cost. It lost ground mainly on coding, on Vibe Code Bench (74.7% vs. 88.9%), Code Migration (63.7% vs. 75.1%) and Terminal-Bench (46.0% vs. 55.1%), and came within about 1.5 points of Sol on the other five.

**Router (Ramp)** cost about a quarter as much as GPT-6.1 Sol, its strongest model, and lost ground mainly on coding. It came within 2.5 points of Sol on six of the eight benchmarks, and nearly all of its gap came from Terminal-Bench (32.3% vs. 55.1%) and Code Migration (52.6% vs. 75.1%).

**Nexus Auto with Opus (Fireworks)** cost less than half as much as Claude Opus 5.5 called directly, but scored 7.7 points lower, and below several cheaper models, including DeepSeek V4.1 Flash 1017 from its own pool. The largest gap came on Code Migration, where Nexus Auto with Opus (Fireworks) scored 21.2% against 47.5% for Claude Opus 5.5.

**Auto Router (OpenRouter)** ran at its cost-saving default and used three inexpensive models. It cost $0.82 per test, but DeepSeek V4.1 Flash 1017, one of the models it used, scored 9 points higher on its own for about four fifths as much.

**Jev Router (OpenRouter)** drew on twelve models. Its strongest, Claude Sonnet 5.5, scored 13 points higher at about three times the cost, and GPT-6.1 Sol scored 8.3 points higher for about two thirds of the cost. A broader pool did not by itself produce a better result.

**Fugu Max (Sakana)** had the weakest result of the six, and ten single models beat it on both score and cost. It often spent many steps on tasks it did not solve: on Terminal-Bench it took a median of about 110 steps, yet 45 of the 66 tasks failed in all three runs.

Among the routers themselves, Nexus Auto with Sol (Fireworks) scored about 2 points above Router (Ramp) on the same tasks, within the margin of error, and 4 to 12 points above the other four. Its lead over Nexus Auto with Opus (Fireworks) came almost entirely from Code Migration. Router (Ramp) scored about 6 points above Auto Router (OpenRouter) and 10 above Fugu Max (Sakana) on the same tasks, and was within the margin of error of Nexus Auto with Opus (Fireworks) and Jev Router (OpenRouter) at a fraction of their cost.

**Each router against single-model alternatives on coding**

| Router | Score (Coding) | Cost per test | Best in its pool | Best at or below its cost |
| --- | --- | --- | --- | --- |
| Nexus Auto with Sol (Fireworks) | 61.5% | $2.48 | 73.0%GPT-6.1 Sol, $5.97 | 62.7%DeepSeek V4.1 Flash 1017, $0.90 |
| Router (Ramp) | 57.1% | $1.82 | 73.0%GPT-6.1 Sol, $5.97 | 62.7%DeepSeek V4.1 Flash 1017, $0.90 |
| Jev Router (OpenRouter) | 54.0% | $11.14 | 80.8%Claude Sonnet 5.5, $25.25 | 73.0%GPT-6.1 Sol, $5.97 |
| Nexus Auto with Opus (Fireworks) | 48.8% | $20.42 | 63.0%Claude Opus 5.5, $39.40 | 73.0%GPT-6.1 Sol, $5.97 |
| Auto Router (OpenRouter) | 47.6% | $1.87 | 62.7%DeepSeek V4.1 Flash 1017, $0.90 | 62.7%DeepSeek V4.1 Flash 1017, $0.90 |

Score and cost per test

**Nexus Auto with Sol (Fireworks)** came closer to its strongest model than any other router: it scored 11.6 points below GPT-6.1 Sol for about two fifths of Sol’s cost. It also scored about 4 points above GLM 5.3, the other main model in its pool, for about a seventh of GLM 5.3’s cost. Its gap to Sol was spread across all three benchmarks: Vibe Code Bench (74.7% vs. 88.9%), Code Migration (63.7% vs. 75.1%) and Terminal-Bench (46.0% vs. 55.1%).

**Router (Ramp)** cost about a third as much as GPT-6.1 Sol, its strongest model, but scored about 16 points lower. It came within 2.5 points of Sol on Vibe Code Bench, and nearly all of its gap came from Terminal-Bench (32.3% vs. 55.1%) and Code Migration (52.6% vs. 75.1%).

**Nexus Auto with Opus (Fireworks)** cost about half as much as Claude Opus 5.5 called directly, but scored 14.1 points lower, and below several cheaper models, including DeepSeek V4.1 Flash 1017 from its own pool. The largest gap came on Code Migration, where Nexus Auto with Opus (Fireworks) scored 21.2% against 47.5% for Claude Opus 5.5.

**Auto Router (OpenRouter)** ran at its cost-saving default and used three inexpensive models. It cost $1.87 per test, but DeepSeek V4.1 Flash 1017, one of the models it used, scored 15 points higher on its own for about half as much.

**Jev Router (OpenRouter)** drew on twelve models. Its strongest, Claude Sonnet 5.5, scored 27 points higher at a little over twice the cost, and GPT-6.1 Sol scored 19 points higher for about half of the cost. A broader pool did not by itself produce a better result.

**Fugu Max (Sakana)** had the weakest result of the six, and nine single models beat it on both score and cost. It often spent many steps on tasks it did not solve: on Terminal-Bench it took a median of about 110 steps, yet 45 of the 66 tasks failed in all three runs.

Among the routers themselves, Nexus Auto with Sol (Fireworks) scored about 4 points above Router (Ramp), within the margin of error, and 7 to 21 points above the other four. Router (Ramp) scored about 8 points above Nexus Auto with Opus (Fireworks), 10 above Auto Router (OpenRouter) and 17 above Fugu Max (Sakana) on the same tasks, and was within the margin of error of Jev Router (OpenRouter) at a fraction of its cost.

### What the routers chose

The routers used different model mixes on different benchmarks. Within a benchmark, though, harder tasks generally did not get more of a router’s spend on its pricier models.

**Which models each router used**

#### Nexus Auto with Sol (Fireworks)

GPT-6.1 SolGLM 5.3GLM 5.3 Flash

#### Router (Ramp)

GPT-6.1 SolGPT-6 Luna

#### Nexus Auto with Opus (Fireworks)

Claude Opus 5.5DeepSeek V4.1 FlashGLM 5.3GLM 5.3 Flash

#### Jev Router (OpenRouter)

Claude Opus 5.5Claude Sonnet 5.5Claude Haiku 5.5DeepSeek V4.1 FlashGemini 3.8 FlashKimi K3GPT-6.1 SolGPT-6 AstraGPT-6 LunaGrok 4.7GLM 5.3GLM 5.3 Flash

#### Auto Router (OpenRouter)

DeepSeek V4.1 FlashGPT-6 LunaGLM 5.3 Flash

Share of each router's calls, by the model that answered

**Nexus Auto with Sol (Fireworks)** relied mostly on GPT-6.1 Sol, which answered all of its calls on Code Migration and HLAB and most on EMB, Terminal-Bench and Legal Research. On Finance Agent, Tax Agent Bench and Vibe Code Bench, GLM 5.3 answered about half: it took whole tasks on the first two, along with most of the extra model calls the agents’ tools made, and opened every Vibe Code Bench task. **Router (Ramp)** switched models in 99% of tasks, about three and a half times per task, and always started with GPT-6 Luna. **Nexus Auto with Opus (Fireworks)** relied mostly on Claude Opus 5.5, which answered over 95% of its calls on EMB, Terminal-Bench, Code Migration and HLAB, but only 62% to 76% on the other four, where GLM models took most of the rest. **Jev Router (OpenRouter)** drew on the most models, twelve, including all three that Auto Router (OpenRouter) used, yet the two switched in about the same share of tasks, roughly a third. **Auto Router (OpenRouter)** usually kept one of its three models for a whole task, chosen largely by benchmark.

### Inside the runs

**Less work.** Under the routers, models often did far less work than on their own. On Tax Agent Bench, the agents under Nexus Auto with Opus (Fireworks) submitted after a median of 7 steps, against 41 for Claude Opus 5.5 called directly, and scored about 22 points lower. On Finance Agent, Vibe Code Bench, Legal Research and Tax Agent Bench, GPT-6.1 Sol generated a fifth to two fifths of its usual output tokens under Router (Ramp) yet scored within a few points of its own runs. Under Nexus Auto with Sol (Fireworks), GPT-6.1 Sol reasoned a quarter or less as much per step as on its own, which cost it little outside coding but cost points on Terminal-Bench and Code Migration. The routers appear to run models at a lower reasoning effort by default, which some models handle better than others.

**The final step.** On Terminal-Bench, Router (Ramp) gave the final, submitting step to GPT-6 Luna in 131 of 198 attempts (three on each of 66 tasks), and those attempts passed 25% of the time, against 46% for the 67 that GPT-6.1 Sol submitted. The router may simply hand the final step to GPT-6 Luna on tasks that are already lost, but the pattern raises the question of whether deciding one step at a time gives the decision to submit enough scrutiny. Nexus Auto with Sol (Fireworks), which rarely changed models within a task, left the final step to GPT-6.1 Sol in 196 of 198 attempts, and those passed 45% of the time.

**Where they switched.** Each router concentrated its switching differently. On Finance Agent, Vibe Code Bench, Legal Research and Tax Agent Bench, Router (Ramp) moved to GPT-6.1 Sol within the first few steps and stayed; elsewhere it switched about every four steps. Nexus Auto with Opus (Fireworks) switched mostly on Code Migration, where its moves to GLM were almost all calls to summarize the conversation once it grew long, and on Vibe Code Bench, where it switched in nearly half its attempts. Nexus Auto with Sol (Fireworks) switched mostly on Vibe Code Bench: every task started on GLM 5.3, and each that got far enough moved to GPT-6.1 Sol for good once the agent first opened a browser to test its app. Auto Router (OpenRouter) and Jev Router (OpenRouter) switched most on Vibe Code Bench, Code Migration and Legal Research.

---

## Opportunities for further gains

Two baselines show how each router’s own models could have done if chosen with hindsight, using the same results they are scored on. They show how much room there is for better choices, not what a router could achieve on new tasks.

Because the routers’ model mix varied by benchmark, the simpler baseline chooses one model for each benchmark and uses it throughout. For each router, we picked the combination of pool models with the highest overall score that costs no more per test than the router did. That choice scored 11.0 ± 1.2 points above Nexus Auto with Opus (Fireworks), 9.9 ± 1.2 above Auto Router (OpenRouter) and 13.2 ± 1.2 above Jev Router (OpenRouter), each for no more money, and was within the margin of error of Router (Ramp). For the pool of Router (Ramp), it uses GPT-6.1 Sol for Finance Agent, EMB and Terminal-Bench, and GPT-6 Luna for the rest.

**Oracle routing** chooses a model for each task instead, sending it to whichever pool model scored best on it and breaking ties toward the cheaper model. To compare within the same budget, we also limit it to each router’s own cost per test: it starts every task on the pool’s cheapest model and upgrades the tasks where a better model adds the most score per extra dollar. Oracle routing scored 8 points above Router (Ramp), 17 above Auto Router (OpenRouter), 21 above Nexus Auto with Opus (Fireworks) and 27 above Jev Router (OpenRouter), each within that router’s budget. The pool of Nexus Auto with Opus (Fireworks) reached 77.2% while spending less than the router itself did, about 13 points above Claude Opus 5.5 on its own, and the pool of Jev Router (OpenRouter), the largest, reached 82.8%.

Nexus Auto with Sol (Fireworks) beat both baselines at its price: even the cheapest choices from its pool, marked in the table, cost more per test and scored lower than the router. Only without a budget did its pool do better, by about 6 points with one model per benchmark and 14 with oracle routing, each at nearly three times its cost.

**Each router against its own models, chosen in hindsight**

| Router | The router | One model per benchmark, within router's budget | Oracle, within router's budget | Oracle, any cost |
| --- | --- | --- | --- | --- |
| Nexus Auto with Sol (Fireworks) | 60.0%$1.25 | 52.1%\*$2.01 | 56.1%\*$1.63 | 74.2%$3.36 |
| Router (Ramp) | 57.8%$0.96 | 59.0%$0.93 | 66.0%$0.95 | 68.2%$2.14 |
| Nexus Auto with Opus (Fireworks) | 56.5%$9.22 | 67.5%$9.10 | 77.2%$8.54 | 77.2%$8.54 |
| Jev Router (OpenRouter) | 55.7%$5.30 | 68.8%$5.23 | 82.8%$5.28 | 83.1%$8.55 |
| Auto Router (OpenRouter) | 52.2%$0.82 | 62.1%$0.65 | 69.5%$0.59 | 69.5%$0.59 |

Score and cost per test. \* No choice fits the router's budget; the cheapest is shown.

---

## Methodology

We ran each router on all eight Vals Index benchmarks: [Finance Agent](/benchmarks/fabv2-1), the [Excel Modeling Benchmark (EMB)](/benchmarks/emb-v1-1), [Terminal-Bench 4.0](/benchmarks/terminal-bench-4), [Vibe Code Bench](/benchmarks/vibe-code), [Code Migration](/benchmarks/code-migration-v1-1), [Legal Research](/benchmarks/legal_research), [Harvey’s Legal Agent Benchmark (HLAB)](/benchmarks/hlab) and [Tax Agent Bench](/benchmarks/tax_agent_bench). Each router was connected to the Index’s existing agents through the same interface as an individual model, and every task was graded and scored as on the Vals Index v2.2, with the same number of runs per benchmark and the Index’s weights. Single-model results are the Index runs of every model with results on all eight benchmarks. The agents decided when to submit, under the same limits as the Index’s model runs.

Each router ran with its default model pool, preferences for quality and cost, and model settings: Auto Router (OpenRouter) at its default `low` cost tier, which favors inexpensive capable models, Nexus Auto (Fireworks) with both pools at its default `balanced` setting, and Router (Ramp) with cost-efficient routing. Jev Router (OpenRouter) is built by TypeSafe and was accessed through OpenRouter. These are evaluations of the routers as shipped, including their settings, rather than isolated tests of their model-selection decisions.

Anthropic’s content filter sometimes refuses a request. The routers had no backup model when that happened, so every score here, for routers and single models alike, counts a refused task as a failure. We also did not include fallbacks for single models, which is why some scores may differ from the Vals Index.

Costs for Router (Ramp) are what Ramp billed, which came to 10% above list price for its OpenAI models, and those for Fugu Max (Sakana) are its flat token price, which covers its internal model calls.

---

## Updates

**11/3/2026**

Added Nexus Auto with Sol (Fireworks).
