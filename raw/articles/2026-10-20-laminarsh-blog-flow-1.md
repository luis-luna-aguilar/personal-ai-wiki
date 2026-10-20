---
title: "flow-1: Frontier trace intelligence at 1/20th of the cost"
type: source
source_type: article
url: https://laminar.sh/blog/flow-1
fetched: 2026-10-20
---

# flow-1: Frontier trace intelligence at 1/20th of the cost

flow-1 is our new model for understanding agent traces, trained with reinforcement learning to identify hard-to-spot failures and explain why they happened. On our benchmark, it matches GPT-6-sol in detection quality while being 23x cheaper.

![](/uploads/flow1_chart_v1_4e86480707.svg)

Teams are shipping agents into increasingly complex workflows and need to understand where those agents succeed or fail. With hundreds of model calls and tool results in a single trace, that understanding is hard to get. flow-1 makes it affordable to move beyond sampling and investigate **all** production traces continuously, catching failures that would otherwise go unnoticed and turning those findings into better agents and products.

flow-1 runs inside what we call the Signals agent. It works like a coding agent, treating the trace as a repo and each span as a file. It starts with a preview of the full trace and a user prompt, which can be as broad as “identify any logical errors.” From there, it can grep across spans and read them in full to investigate. When it finds an issue, it returns structured JSON that follows the user’s schema. Learn more about Signals [here](https://laminar.sh/docs/signals/introduction).

We compared flow-1 with other frontier models using the same Signals agent on our benchmark of 523 difficult agent traces across coding, legal, customer support, CRM and more. flow-1 surpasses GPT-6-sol with high reasoning in failure detection quality. Sol flags more traces, making it noisier, while flow-1 digs into the evidence to surface the failures that matter.

The cost of trace analysis includes the full Signals agent run and all its retrieval steps. Flow-1 is priced at $0.05 per million input tokens, $0.01 for cached input and $0.30 for output. To compare costs, we use statistics from Signals agent runs on traces with under 100k total LLM tokens. flow-1 can process **23x** as many traces per dollar with sol-level analysis quality. It’s also 25% cheaper than luna, with significantly better failure detection and explanations. Another RL checkpoint is already training to make flow-1 a more efficient thinker and bring costs down further.

![](/uploads/flow1_dots_v1_34489c0f0a.svg)

We then trained flow-1 with reinforcement learning inside the Signals agent. It learned to use tools efficiently, perfectly follow the requested output schema and dig deeper into complex traces to separate real failures from noise. Let's now look at flow-1 in action.

We then trained flow-1 with reinforcement learning inside the Signals agent, using the same tools it has in production. Training covers the full investigation: deciding what to inspect, gathering evidence and determining whether that evidence supports a finding.

Let's now look at flow-1 in action.

In one run, a legal agent prepared a contract redline and an issues list. The parties had agreed to a 105-day film availability window. The agent marked the point closed, but left the contract schedule at 90 days. All three models caught the contract error, and flow-1 also tied it to the misleading completion status in the issues list.

> **flow-1:** “The agent never edited the schedule table to the agreed 105-day window, even though the issues list reported it as conformed clean.”
>
> **GPT-6-sol:** “The redline failed to incorporate the agreed 105-day film availability window.”
>
> **GPT-6-luna:** “The counter-markup leaves core availability-window provisions incorrect or incomplete instead of implementing the instructed negotiated terms.”

---

In another trace, a coding agent reported its work complete, even though not all tests have passed. It blamed the remaining test failures on a pre-existing issue. But the logs showed that its explanation covered only one of the failures. flow-1 and sol flagged the misleading test report, while luna didn't identify anything:

> **flow-1:** “only the telemetry test failure was directly linked to the missing \_resolve\_registry\_uri function.”
>
> **GPT-6-sol:** “The agent incorrectly attributed an end-to-end test failure to a different missing function than the traceback identified.”
>
> **GPT-6-luna:** No error found.

---

A code-review agent spotted a change that replaced yaml with pyyaml. It was an actual bug, correctly identified by the review agent. flow-1 and sol correctly found no error in the trace, while luna flagged the finding as unsupported.

> **flow-1:** No error found.
>
> **GPT-6-sol:** No error found.
>
> **GPT-6-luna:** “The agent reported a code-review regression based on distribution-to-import-name mappings that its inspected evidence does not establish.”

---

There are still gaps. In another contract review, flow-1 cleared a redline that left out mandatory AI-governance protections, even though the agent’s own memo said they were required. Both GPT-6 models caught the omission:

> **GPT-6-sol:** “The tracked redline left mandatory AI-governance protections unaddressed despite identifying them as critical.”

---

Failure detection is the most common use case, but Signals is a general trace processor. You can use it to identify user frustration, extract structured data from conversations and tool results, or understand which requests agents hand off and why. You can simply define what to look for and the schema for the result.

In our Signals benchmark, one signal definition specifically asked for contradictions within deliverables. A legal agent produced a contract redline and an accompanying memo, but their milestone totals differed by $20M. flow-1 and sol caught the mismatch in the totals. Luna found other inconsistencies, but missed the most crucial one:

> **flow-1:** “The issues memo states the milestone total is $190M and the aggregate deal value is $457M, but the redline's milestone ladder sums to $210M, making the aggregate $477M.”
>
> **GPT-6-sol:** “The redline's revised milestone payments exceed an unchanged payment cap and contradict the memo's aggregate deal figure.”
>
> **GPT-6-luna:** “The issues memo recommends a first-commercial-sale milestone, but the redline's replacement milestone list omits that milestone.”

---

With Laminar Signals and flow-1, production agent traces become a continuous source of improvement. Teams can turn failures into regression tests, use recurring problems to guide fixes and check whether each release improves agent behavior.

Those traces also reveal what to build next. Repeated user corrections, handoffs and unresolved requests can reveal confusing workflows, missing capabilities and unmet demand. flow-1 makes it affordable to find these patterns across production traffic and understand how often they happen and who they affect.

Try flow-1 in [Signals](https://laminar.sh/docs/signals/introduction) to find hidden failures, understand your users and see where your agents can improve.
