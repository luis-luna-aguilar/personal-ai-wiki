---
title: "PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of
 Contributors"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-09-01
gmail_id: 1a05dc46dda74cf4
---

# PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of
 Contributors

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-09-01

View this post on the web at https://www.latent.space/p/pr-not-welcome

GitHub invented pull requests, and for 18 years they have been open by default. But now some of the top AI-native open source projects are shutting PRs off, because they’ve found a better way.
These projects, which include Flue and tldraw, refuse to accept PRs from external contributors — in part because they’re usually AI-generated. Instead, the maintainers prefer to use their own agents to create and manage PRs.
Also, many projects have begun using a “software factory [ https://substack.com/redirect/304141ef-e576-48d5-9708-95c34154c90a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]” to manage community contributions. Typically this involves a ‘team’ of agents triaging a PR, reproducing the issue (if it’s a bug), implementing a fix or a new feature, reviewing it, and then handing it back to a human to merge it.
Vercel’s software factory for AI SDK
Vercel recently published a post entitled “Building a software factory for AI SDK [ https://substack.com/redirect/dac1b598-b6ed-4eae-b2e2-4a5419c534b1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].” It describes how the open source AI SDK project, which gets over 20 million npm downloads per week, deployed agents to get control over its PR and issue backlog — which had reached “over 1,000 open issues and almost 800 pull requests” by late June.
There are several types of agents in Vercel’s system, each of which focuses on a different task. For example, there’s an agent that reproduces a bug, another that applies a fix, and yet another that reviews the fix.
One of the key reasons why Vercel set up this software factory is because it trusts its own agents to do the work, more so than agents run by community members.
“If we have a very specific agent with a very specific prompt that we optimized — and we know that, over history, it was very successful in fixing a certain category of bugs — then we develop trust in that particular agent configuration,” Vercel engineer Lars Grammel [ https://substack.com/redirect/13037c26-805c-41ca-bf30-dc2e0080c601?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] explained in a YouTube video [ https://substack.com/redirect/19346601-c60e-4b4e-9335-b96e3591cbef?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
“For open-source projects, it’s worth considering having your own agents and your own setup, and not necessarily trusting the community, because it can actually cut down your time to review,” he added.
Grammel also showed the deployment architecture for its system, noting that “there is a UI, there’s a web app, there’s an underlying API, there’s an execution space, and there are sandboxes.” It’s then synchronized with GitHub, which automatically triggers other actions. The UI Grammel mentioned was custom-made.
Just four weeks after this software factory was implemented, Vercel claims [ https://substack.com/redirect/dac1b598-b6ed-4eae-b2e2-4a5419c534b1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] the factory now “authors between 25 and 35% of PRs we merge and closes 70-80% of issues.”
Astro’s auto-triage system
The Astro web framework [ https://substack.com/redirect/a7019f21-538a-4d8e-9e04-f540e021748a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], which has 62,000 stars on GitHub, has also adopted what creator Fred Schott [ https://substack.com/redirect/7336761f-6c50-481a-82e9-bfb6067172b7?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] calls “that software factory idea.”
“For five years, we were in this place where issues came in faster than we could handle them,” Schott told Latent Space.
But now, with agents handling the triage work, they’ve reestablished control.
“It’s totally shifted in the last six months,” he said. “We can now solve these issues with these automations — handling triage, reproduction, getting the user to actually verify the fix that the bot is suggesting before we even look at it.”
The result was not just a large decrease in open issues, but a complete change in how the Astro team deals with incoming community requests.
“I’ve never seen that in my entire decade-plus experience with open source,” Schott said. “Being able to essentially treat issues as a thing that every week, you prioritize — no matter what — versus a backlog that you’re constantly trimming.”
Furthermore, the Astro “auto-triage” system directly led to Schott creating a brand new agent framework, called Flue [ https://substack.com/redirect/e9fbcd55-2d3e-4817-96f9-93f50344f0cb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Flue doesn’t accept your PRs, but is open for discussion
With Flue, Schott is trying an even more radical approach to PRs. Flue’s contributor guide [ https://substack.com/redirect/daaee2cc-da42-48ba-9204-554407867edb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] states that “we’re going to try to reimagine things” — partly to prevent what it calls “Drive-by AI slop PRs.”
Basically, Schott explained, every external pull request in the Flue project is automatically closed and converted into an issue or discussion. Bug reports and fix proposals get turned into issues, feature requests become discussions.
“If you submit a PR, no hard feelings, we’re just going to go and represent it for you as issues and discussions. And from there, trying to figure out the right way to bring people on.”
It’s kind of like treating incoming requests as leads, rather than as a piece of work a maintainer feels obliged to review. The contributor guide explains that it uses the team’s own expertise combined with “the best available SOTA [State-of-the-Art] LLMs that we have access to” in order to help them decide what to work on next.
Once a decision is made in the issue or discussion, agents are then deployed for “research, design, implementation, and initial review.”
If our agents write the code, your external PRs are worthless
Like Flue, the “source available” React drawing tool tldraw [ https://substack.com/redirect/233fd2f0-db4f-46e0-88ea-a3487a85560a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] (50,000 stars) automatically closes external PRs.
Project creator Steve Ruiz announced this policy in January [ https://substack.com/redirect/64ee7526-62e5-45c9-8028-2b4664b84105?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and five months later reiterated it [ https://substack.com/redirect/d4f47d60-b8b9-4120-933b-19e881527cc4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], noting that it was “an opinionated decision made in response to changes in how we’re coding (more discussion, more agents), the social practices around public contribution, and the changing landscape around code security.”
HashiCorp co-founder and Ghostty creator Mitchell Hashimoto, now a co-founder of Superlogical [ https://substack.com/redirect/c3a58faa-9d3c-402a-921e-4266141852e6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], takes it even further. He thinks [ https://substack.com/redirect/05b620bb-5e01-474e-ab4e-6edbfdefd3f4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] “the future is that large open source projects will close contributions completely.”
Ruiz responded [ https://substack.com/redirect/0dd02063-2395-4f81-99ab-1819981a82a2?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], “It just makes less sense to have people contributing code if the issue is decently well-specified and the code can be written by agents.”
But…what happens to the community?
Traditionally in open source, pull requests have been reviewed by maintainers not only for the code, but to teach contributors and assess them as future maintainers. If projects like AI SDK and Astro are using their agents to do much of the code review and implementation, where does that leave community members who want to be more actively involved?
Schott recognizes this as a risk.
“It still leaves this open hole of, well, if you just keep narrowing the project, at a certain point, you and I go on vacation — what happens? It doesn’t really solve every problem.”
However, the fact that both Flue and tldraw don’t accept PRs but do accept new issues and discussions perhaps points to a solution. Which is that by talking to each other more, community members better get to know — and trust — one another, which is both a way to learn from peers and potentially prove yourself worthy of being a maintainer.
As for the code, if it’s easier for maintainers to use AI themselves than to accept external code contributions, then as tldraw founder Steve Ruiz put it [ https://substack.com/redirect/d8258c63-1ed8-465f-904d-ae4919259b47?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], “it’s better to limit community contribution to the places it still matters: reporting, discussion, perspective, and care.”

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakl4TXpjeU5qYzVOaXdpYVdGMElqb3hOemc0TWpjNU5UUTJMQ0psZUhBaU9qRTRNVGs0TVRVMU5EWXNJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5EV21acm5SN21iUG5BX3VqLW55ZVZ2aVZmd1YwNVJyblc1X1JKY1Zjakw0IiwicCI6MjEzNzI2Nzk2LCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc4ODI3OTU0NiwiZXhwIjoyMTAzODU1NTQ2LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.Ud6wHEmuG3wyKZZ1KWAT58eeDrXpV6UNTFgqKufTIyg?
