---
title: Introducing Devin Oncall
type: source
source_type: article
url: https://devin.ai/blog/introducing-devin-oncall
fetched: 2026-10-19
---

# Introducing Devin Oncall

Today we are launching Devin Oncall to help our customers step towards making their software self-driving. Devin can automatically investigate alerts and bug reports and help your team diagnose and resolve production incidents.

Devin Oncall is the best harness at diagnosing and mitigating production failures. In our evaluation on SREGym, it achieved the highest score and saturated the benchmark with **100% end-to-end success**, with fastest time to mitigation.

#### SREGym-LiteSpeedvsPerformance

4050607080901002m3m4m5m6m7m8m9m10m11m12m13mTime to remediateEnd-to-end success (%)↖ Faster and more accurateGPT-6 AstraGPT-6.1 SolGPT-5.6 SolGPT-5.6 TerraGPT-5.6 LunaOpus 5Sonnet 5Opus 4.8GPT-6 AstraGPT-6.1 SolOpus 5Opus 5.5 · 100% in 2m 21sGPT-6 AstraGPT-6.1 SolFable 5.1

Devin OncallCodexClaude CodeCloudThinker

The benchmark tests agents against representative faults in live systems, requiring them to both *identify* the root cause and successfully *mitigate* the issue in the same run. Each test is based off of a real production incident that happened in real-world systems.

Devin Oncall has already changed how Cognition’s customers handle on-call and incident investigations, from reducing pages to freeing engineers for product work:

* **At [Reducto](/customers/reducto),** Devin spotted concerning trends across several alerts and opened an incident on its own, with context on what the problem was. Reducto’s production alerts fired much later, as failed requests started climbing. Because Devin had flagged the issue early, the impact of the incident was reduced dramatically. Devin now handles most engineering alerts first, often remediating medium-severity issues or opening and testing a PR before paging an engineer for review.
* **At [RV Tech](/customers/rvtech), the Rivian and Volkswagen joint venture,** Devin automatically extracts vehicle identifiers and timestamps from customer reports, pulls logs, runs parsing scripts, and performs issue triage. Engineers review the analysis instead of conducting the initial investigation by hand. This enabled one team to redirect several engineers back to product work.
* **At [AngelList](/customers/angellist-oncall),** Devin correctly identifies root causes 3.5x more than their in-house investigation harness, Sky, letting engineers move straight to remediation with confidence and trust. It even handled 50% of incidents end-to-end on its own. AngelList deprecated Sky in favor of Devin Oncall.

Adoption has grown rapidly as we’ve made Devin Oncall available to more customers. It now handles thousands of real production alerts every day at some of the world’s largest companies.

#### Devin Oncall

Alerts handled per day

Aug ’26Sept ’26Oct ’26

We are excited to make Devin Oncall generally available. In this post, we walk through how we built Devin Oncall. We unpack the engineering decisions behind an agent that can investigate, remediate production issues, and keep working until the underlying root cause is resolved.

Agents have not always been good at debugging production. The quality of their investigations has lagged behind their ability to code. Until this past year, those limitations were easy to see. Agents were too eager to declare they had found the answer, didn’t explore broadly enough, and tried to make large code changes instead of performing simple mitigations like rollbacks and scale-ups.

Specialized AI SRE companies (ourselves included at [TierZero](https://cognition.com/blog/welcoming-tierzero)) used a host of techniques to compensate:

* essay-length, overfit, FDE-tuned prompts and runbooks
* observability collectors deployed into your network for more control over your data
* custom graph architectures and advanced classical machine learning techniques on error signals
* post-training specialized models for SRE tasks

All had their time in the sun.

However, these techniques don’t scale as models become more intelligent. As model capabilities improve, you can find yourself cutting prompts and reworking parts of the system that now work against the model. Instead of getting better investigations from a smarter agent, you spend time undoing assumptions built around its earlier limitations. As the Bitter Lesson dictates, the best core architecture is a really smart agent.

This means that for on-call, all you need is a really good coding agent, equipped with the right context, tools, and workflows. Your capable agent also needs to run in the cloud, with access to the systems you care about and shared context across teams. For us, that agent is **Devin**. Its model-agnostic architecture also lets us choose the best model for any on-call task, and adopt stronger models as they become available.

Over the past couple of months we’ve built and tested Devin Oncall around that foundation: giving Devin the context and working patterns it needs to carry out production investigations.

We organize the engineering behind Devin Oncall into three layers: **core intelligence, company context, and agent behavior**. These roughly match what makes a strong on-call engineer: the ability to reason about systems, knowledge of your particular environment, and battle-tested reliability workflows.

At the most basic level, the model and its core harness need to understand how to debug issues in a controlled environment. We regularly evaluate frontier models from all providers on debugging benchmarks and choose the most effective model for any SRE task. In SREGym, one leading benchmark, mid-tier models have already maxed out the more curated benchmark, where the previous generation scored 50–60%.

#### SREGym-Lite

Best score by model release

End-to-end success: the agent both identified the correct root cause and fixed the live system.

100%75%50%25%0%

Claude Sonnet 545.1%, Claude Code

GPT-5.6 Sol76.5%, Codex

Claude Opus 576.5%, CloudThinker

Claude Fable 5.185.3%, Devin Oncall

GPT-6 Astra100.0%, Devin Oncall

Claude Opus 5.5100.0%, Devin Oncall

GPT-6.1 Sol94.1%, Devin Oncall

JulAugSepOct

Devin OncallOther agentsBest score to date

Best end-to-end score published for each model on SREGym-Lite (17 faults), placed at the date the model became available in Devin. Devin Oncall results are from our own evaluation; other results are from the public SREGym leaderboard as of October 15, 2026, where CloudThinker also reached 100% with GPT-6 Astra.

These results show that models can make the right decisions to find bugs in contained systems. But production investigations involve byzantine legacy systems and searches across massive amounts of telemetry data. Agents still stop at the first plausible root cause, leaving an engineer to tell them to “dig deeper” or “find the underlying cause.”

We address premature conclusions with investigation prompting and a second “review” agent that runs asynchronously alongside Devin. It examines recent reasoning, tool calls, and results for errors such as treating correlation as causation, dismissing contradictory telemetry, or confusing a trigger with the underlying problem. A recent deployment, for example, is a lead to investigate, not a causal explanation.

This separates the work of investigating from the work of checking whether the conclusions follow from the evidence. The main agent still decides how to investigate; the reviewer provides the targeted challenge that would otherwise have to come from an engineer.

A capable engineering agent still needs to know how to work inside your company: where to find the relevant code, how to query your telemetry, and how your services fit together. General debugging ability doesn’t give an agent that context, or access to the systems where it can find it.

In local agent workflows, the user and agent are symbiotic. The user supplies context as needed, and the agent uses the user’s credentials to reach third-party systems. A cloud agent needs to be self-contained. Its access and initial context have to be configured upfront.

That creates more setup work, but it also changes who benefits from the work. Context the cloud agent acquires, such as tribal knowledge about a legacy system, can be shared across the team and organization, rather than repeatedly supplied by individual engineers.

With enough time, a capable agent could theoretically figure out much of your environment during each run. But production investigations need to be fast and cost-efficient. Some customers arrive with carefully curated skills that effectively cache this knowledge, giving Devin a head start. Many do not. We built three layers of context to help those customers get started and accumulate knowledge as Devin investigates:

* **Per-Responder Memory:** Each Oncall agent has its own memory. It can remember which teammates to tag, and you can tell it to behave differently in future investigations. This gives each responder context specific to the work it handles.
* **Per-Org Skills:** Devin Oncall regularly indexes your environment and generates skills for common debugging tasks within your integrations. These include calculating the customer blast radius of an issue and querying data from platform dependencies. The skills give the agent procedures it can use instead of having to work them out again during an investigation.
* **Per-Org Memory:** Every investigation is post-processed, and useful information is saved for the agent to dynamically search during future investigations. Devin Oncall is tuned to treat this as a low-fidelity cache of institutional knowledge: information about your systems that it would otherwise have to discover.

Together, these layers let Devin Oncall work on day one and get better as your team uses it. Our monitoring shows that poor diagnoses become less frequent over time.

A stream of alerts and an active incident require different working patterns. Devin Oncall’s two core products, Responders and Incidents, organize Devin’s work around those workflows, with the goal of making investigations both effective and cost-efficient.

A responder is the next generation of [Auto-Triage](https://docs.devin.ai/product-guides/auto-triage). It watches a stream of alerts or bug reports, diagnoses issues automatically, and remembers the underlying problems so it doesn’t repeat investigations.

We built responders around a parent-child agent architecture. A hidden parent Devin watches new alerts in the channel and decides whether an alert appears to represent a new issue that warrants investigation. When it does, the parent launches a child investigation.

New issueExisting issueSave findingsAlert streamParent agentWaiting for alertsWatching the streamChild agentReady to investigateIssue memoryNo saved issue yetAPI latencyInvestigation savedAPI latencyAlert

This separates awareness of the alert stream from the context needed to investigate an individual issue. The parent understands ongoing requests and known issues, while each investigation starts with fresh context.

Remembering known issues also reduces unnecessary work. Responders skip roughly 60% of investigations by referencing previous work and grouping related alerts, saving customers more than half the cost of regular automations.

#### Devin Oncall responders

Skipping known issues cuts the cost of responding to alerts by more than half.

Every 100 alerts

Alerts

35 investigated

65 skipped: known issue or noise

InvestigatedSkipped: known issue or noise

Cost

Investigate every alert

100%

Devin Oncall comes with two responder types: **Alert Responders** and **Support + Bug Responders**. We’ve tuned their default behavior for common customer use cases so they work without complex runbooks. You can still customize their behavior when your workflow requires it.

Devin joins your incident response process to help diagnose and fix urgent issues. It works within the common practice of creating a messaging channel for each incident, proactively investigating alongside your engineers and maintaining a live incident document that people can use to get up to speed.

The challenge here is keeping the investigation moving while remaining responsive to the conversation. Devin needs to support that ongoing exchange without losing focus.

We separate these responsibilities within the incidents’ architecture:

Share findingsUpdate while investigating@Devin requestsSharedcontext# Incident channelMaya, Sam, Leo + DevinMMaya14:07Seeing 500s after the deploy.Anyone else?SSam14:08thanks Maya!LLeo14:09@Devin, can you check the DB pool?LLeo14:10@Devin, can you checkthe recent deployments too?DDevinIn threadDB pool looks healthy.DDevinIn threadLatest deploy loweredthe API timeout.DDevin14:12Root Cause Found:Latest deploy lowered theAPI timeout.Relevance filterEvery messageFiltered outMain keeps investigatingMain agentOwns the incident channelWorks proactivelyTracking conversationKeeps the live context currentLive incident docShared contextTimelineEvidenceRoot causeDB poolChild agent · fresh contextStarting investigationDeploymentsChild agent · fresh contextStarting investigationResponse modes configurable in settings

Messages are pre-filtered before reaching Devin to avoid distractions from irrelevant discussion. The parent Devin investigates continuously in the background, while spawning child Devins to investigate direct questions and sharing context with them.

This keeps the parent Devin focused on orchestration and background investigation, while child Devins can respond quickly to specific requests. Engineers can ask questions as the incident develops without making those questions the parent Devin’s entire investigation.

Shipping software should come with the capacity to keep it working. Let Devin follow changes into production, carry issues through to resolution and keep systems healthy as they change. Devin Oncall empowers engineers to set directions and make decisions, without having to initiate and coordinate every step.

That is what makes software self-driving: a team can take on more ambitious software without becoming the manual operator for everything it creates.

Try Devin Oncall today at [devin.ai/oncall](/oncall)
