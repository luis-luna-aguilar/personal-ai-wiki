---
title: 'What Effort Level Should I Choose? On the Economics of Reasoning Effort in LLM Agents'
type: source
source_type: paper
source_file: raw/papers/2026-11-24-arxivorg-html-261034491.md
url: https://arxiv.org/abs/2610.34491
published: 2026-10-25
ingested: 2026-11-24
domains: [agents, models]
---

# What Effort Level Should I Choose? (Johns Hopkins, Together AI, Cornell)

**The everyday problem.** Most models now have an effort dial (low, medium, high, xhigh, max). You must pick a setting before you know whether extra thinking will help. Even when the run succeeds, you cannot tell whether the cheaper setting would have done just as well. The authors call this a "credence good", like a car repair whose necessity you cannot judge.

**What they did.** They ran eight models at every available effort setting and changed nothing else. The models were GPT-5.6 Sol, Terra and Luna, Claude Sonnet 5, GLM-5.2, Inkling, Kimi K3 and DeepSeek V4 Flash. The benchmarks were AIME 2026 and GPQA Diamond (one call per question) and two agent benchmarks: Terminal-Bench 2.1 (Terminus-2 agent) and a 44-task SWE-Bench Pro sample (mini-swe-agent). For the proprietary models, "max" was skipped as too expensive. Every's newsletter described the work as testing Claude Code, Codex and ChatGPT, but the paper tests API models in fixed harnesses.

**What they found.**
- *Higher effort is not a superset of lower effort.* Aggregate accuracy often rises, but on Terminal-Bench every model lost some tasks between its lowest and highest setting. GPT-5.6 Sol went from 76 to 73 of 89 solved moving from high to xhigh, losing eight tasks and gaining five. A user gets one run, not the average.
- *Easy tasks get expensive.* On tasks every setting solved, the highest tested setting cost up to 42x the lowest.
- *Effort changes how the agent works.* At high effort agents re-check their work more and search for existing solutions more, which lengthens runs without changing the outcome. On the original SWE-Bench Pro, GPT-5.6 Sol read the reference-fix commit on 15.9% of tasks at low and 75.0% at xhigh, so part of the "effort gain" may reflect benchmark leakage.
- *Turning reasoning off is not a reliable saving* in agent loops, because agents compensate with longer runs over a growing context.
- *Models cannot pick their own effort* reliably from the task description.

**The policy they propose.** "Naive laddering": run at the lowest setting, check the result, and only if it fails retry once at the highest. It keeps every cheap success and only pays for top effort when needed. It matched or improved on fixed top effort for every model and benchmark. Median cost savings against always-highest were 25.3% on AIME, 41.5% on GPQA and 15.5% on corrected SWE-Bench Pro. On Terminal-Bench all eight models gained success; GPT-5.6 Sol went from 83.0% to 88.6% at 17.4% lower cost, but four of the eight models paid more for their gain.

**Limits.** Laddering needs a reliable correctness check, which many deployments lack, and it pays for a full second run on each escalation. Agent benchmarks used one run per task per setting; the authors re-checked with DeepSWE's repeated runs. They also argue for counting the user's waiting time in cost, because token charges alone can misrank settings.

**Why this is useful for our projects.** For work with tests or a verifier, default agents to low effort and escalate automatically on a failed check, instead of buying max effort up front. For work without a checker, keep a fixed middle tier and measure on your own tasks.

## Influenced pages
- [Cost-aware AI task routing](../../training/cost-aware-ai-task-routing.md) — laddering added to the effort control; max-effort failure mode
- [Cost-aware routing: evidence from practice](../../training/cost-aware-routing-evidence.md) — study bullet next to Anthropic's effort analysis

## Key claims extracted
- Eight models, four benchmarks, effort varied with tasks, prompts and harness fixed
- Every model has a nonempty Terminal-Bench regression set between lowest and highest effort
- On always-solved tasks, highest tested effort costs up to 42x the lowest
- GPT-5.6 Sol reads the SWE-Bench Pro gold commit on 15.9% of tasks at low vs 75.0% at xhigh
- Naive laddering matches or improves on fixed top effort for every model and benchmark; median savings 25.3% (AIME), 41.5% (GPQA), 15.5% (corrected SWE-Bench Pro); on Terminal-Bench 4 of 8 models gain success at higher cost
- Laddering requires a reliable external correctness check and pays for both attempts on escalation
