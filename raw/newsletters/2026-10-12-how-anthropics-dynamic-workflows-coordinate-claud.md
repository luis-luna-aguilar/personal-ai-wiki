---
title: "How Anthropic’s Dynamic Workflows Coordinate Claude Agents"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-10-12
gmail_id: 1a131593afe08083
---

# How Anthropic’s Dynamic Workflows Coordinate Claude Agents

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-10-12

View this post on the web at https://www.latent.space/p/claude-dynamic-workflows

The AI Engineer New York 2026 conference [ https://substack.com/redirect/bdcd56ae-cd10-4e04-b743-78cc725cd5f0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] kicked off this morning with a series of workshops, including Anthropic discussing how to orchestrate its Claude Managed Agents. Of particular interest was a brand new feature, announced on Friday [ https://substack.com/redirect/14abf625-d1d3-4673-9ce0-ff74c1b2b489?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], called dynamic workflows — or simply “flows,” as the presenters repeatedly called it.
Flows are defined as “a new type of multiagent orchestration, built for your most ambitious workloads.”
CJ Avilla [ https://substack.com/redirect/99c96d2e-e7a4-4434-b77e-c3132c84ad85?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and Harrison Stall [ https://substack.com/redirect/17c16c4e-f0a9-4e57-996e-15c2eb86cb1e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], both Members of Technical Staff at Anthropic, began by invoking some operating system projects of the past — from Ken Thompson building the original Unix operating system, through to Linux evolving from one person (Linus Torvalds) to layers of trusted maintainers. The lesson: agents need the same level of organization in order to do the types of big, ambitious projects Anthropic envisions for dynamic workflows.
Sponsored by Union.ai 
Build a sovereign AI factory
The best engineering teams are building AI factories where they own and control not only their data, compute, and infrastructure, but also a durable runtime on their cloud.
Union.ai gives your workflows the durability to adapt and right-size infra resources and recover from failures without re-running completed work.
Get started directly through AWS Marketplace and try Union.ai free for 30 days [ https://substack.com/redirect/02f468a6-6445-4caa-9fea-92cb127c9ddf?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
To learn more, visit us at AI Engineer New York booth #48.
“I think a lot of us who are orchestrating and managing lots of agents now might start to feel this feeling of being the bottleneck and being the breaking point as we have lots of agents contributing tons and tons of PRs,” Avilla said. “And we’re sitting there in our GitHub trying to approve PRs and make sure that everything works as expected.”
From agent rosters to dynamic workflows
The pair noted that dynamic workflows began in Claude Code as the “a harness for every task” concept. But flows can run longer than a single agent or a roster. The basic idea is that Claude chooses the organization of agents.
“Flows are essentially the next version of multi-agent orchestration,” said Stall, “where you can let Claude fully orchestrate the entirety of its own multi-agent topology.”
The way this works is that the lead agent creates a plan for how it wants to accomplish tasks. Claude then writes an orchestration program, which launches agents, collects results, and manages information flow.
Previously, Claude Managed Agents required developers to configure a coordinator and a roster of subagents. With dynamic workflows, Claude itself determines how to divide and orchestrate the work.
“Across multiple different phases of the multi-agent orchestration, it’s able to accomplish discrete, verifiable units of work without you having to manage any of the interconnections between these things,” Stall said.
That said, Avilla noted that the user can introduce specialist sub-agents if they wish.
“It’s also possible in the agent config to pass in pre-configured sub-agents,” he said.
All of this is available in Claude Console, the interface used by developers accessing Claude through API — the whole point of Claude Managed Agents.
The presenters then showed a relatively simple workflow of a stock watchlist scanner. Although this was far removed from the big, ambitious projects Anthropic is encouraging, it did illustrate the basic pattern: a scan phase distributed individual tickers to agents with isolated contexts, and a later review phase examined the findings before producing a report.
Q&A: Budgets and the limits of self-improvement
The audience Q&A surfaced a number of potential problems. One audience member asked how Claude decides how many agents a task needs, and could a simple ticker scan trigger hundreds of sub-agents?
“The answer really is evals and lower defaults,” Stall replied, noting that ambitious tasks generally require explicitly encouraging greater parallelization.
One enduring concern with agent orchestration is maintaining control over your token budget. Someone asked whether the lead agent knows how much money it has available?
Stall replied that the model does not know its budget while running, but that developers can set a session budget. He added that informing models of their budgets could make the agents “a little bit anxious,” which elicited chuckles from the audience.
A related question was how can developers make repeated flows cheaper and more efficient over time?
Outside of asking Claude to examine the costs incurred, Avilla suggested another relatively new feature be used: dreaming. In the documentation [ https://substack.com/redirect/47a9722d-c8df-43e3-90e9-6d36c9af897f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], “dreaming” is defined as a research preview feature. A dream “reads an existing memory store alongside past session transcripts, then produces a new, reorganized memory store,” with duplicates merged, “stale or contradicted entries” replaced, and “new insights surfaced.”
Avilla described dreaming in the flow context as being able to “crystallize and basically improve the memory store that is related to those sessions.”
For the stock watchlist example, someone asked whether the watchlist flow can improve itself? For example, recognize that its scanning model is inadequate and change the next scheduled run?
Stall said this wasn’t built in, but he and Avilla suggested hill-climbing and dreaming could be used to improve the loop.
What about visibility into the actions of the sub-agents, another audience member asked.
Avilla replied that yes, developers can always inspect that through graphing functionality inside Claude Console.
“You can tell, what did the lead agent actually pass to the sub-agent? You can look at that payload here to deeply understand what is actually happening for every transition in this entire graph.”
Another interesting question was whether the subagents can communicate with each other?
Stall said the agents share a filesystem and can use it to exchange information, but developers cannot directly instruct one workflow subagent to message another through the API.
Flows cost much more, but are designed for big tasks
In the watchlist-scanner comparison, Avilla said flows cost “much more” than a single-agent approach, but were also “much more effective at finding all of the details.”
The bigger question is how ambitious can flows be, really? One audience member asked whether dynamic workflows can power large scientific research projects, referencing OpenAI’s recently announced proof concerning the Navier–Stokes Millennium Prize problem.
While Stall wouldn’t be drawn on specifics about how Anthropic computes large scientific problems, he said it is their goal to enable general users to tackle those problems too.
“Flows are basically a way to throw test-time compute at hard problems and get more capability faster out of the models,” he said. “We think, especially as an API service, that unlocking the power of this is the first step for us making these types of discoveries, or scientific progress, broadly doable by the general public.”

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakl5TURBMk5qWTRNaXdpYVdGMElqb3hOemt4T0RJNU1qa3hMQ0psZUhBaU9qRTRNak16TmpVeU9URXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5EbEJ6cmdsUnlsOERiWERwZkx5SHpzeGlFU0lwaE80QWxRYmozMXZ3RW9RIiwicCI6MjIwMDY2NjgyLCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc5MTgyOTI5MSwiZXhwIjoyMTA3NDA1MjkxLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.H3w7MSTmnRazPWbvwzCOlT4f8l-n1kFfVUOqncLfY3s?
