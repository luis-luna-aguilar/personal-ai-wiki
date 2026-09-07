---
title: "React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-08-15
gmail_id: 1a00620395ce1e42
---

# React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-08-15

View this post on the web at https://www.latent.space/p/flue-2

Agent frameworks for developers are still at an early stage, with the likes of Vercel’s eve [ https://substack.com/redirect/1db7b1e3-d7c5-4f77-8f13-5f2f9f8921fb?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and Fred Schott’s Flue [ https://substack.com/redirect/5ee8ca10-18d8-40a5-8b9e-5de0e04627f4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] — both launched this year — setting the early template.
Schott is the creator of the web framework Astro, which led to his company being acquired by Cloudflare [ https://substack.com/redirect/4478db4b-cd89-4d52-9797-0cf38da9a523?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] in January. He’s just released version 2 of Flue [ https://substack.com/redirect/2bc6706e-0b34-4028-865a-77868d7a5a46?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], its first stable release, which has as its foundation React-style “Agent Hooks.”
In Flue, an agent is represented by a JavaScript function. This function “re-renders on every turn [ https://substack.com/redirect/02141396-336a-49bf-a0f1-be865c69affe?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ],” meaning before every model call.
The addition of hooks came after Schott realized that React’s composability would be a great fit for agent development.
“I originally tweeted that we were building the Astro for agents or the Next.js for agents,” he told us. “But then I realized: maybe no one has even built the React for agents.”
Editor’s Note: we last talked about the React for Agents with Bret Taylor, CEO of Sierra and Chairman of OpenAI [ https://substack.com/redirect/0e6357fa-0167-4643-8934-dd73038646a9?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]:
“We’re still trying to figure out who the reactive agents are and the jury is still out… We’re sort of in the jQuery era of agents, not the react era.” 
Hooks are authored in TypeScript. According to the Flue 2 launch post [ https://substack.com/redirect/2bc6706e-0b34-4028-865a-77868d7a5a46?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], they “let you build dynamic agents that can manage their own state, listen to agent lifecycle events, and even attach different resources and capabilities dynamically to enhance themselves at runtime.”
There are 16 built-in hooks in Flue 2, including useSkill(), useTool(), useSubagent(). You can also add custom hooks.
What hooks open up for developers is that they make an agent much more dynamic, by allowing its configuration to change as a conversation or workflow progresses. Schott said this is needed to build “real support bots, real triage bots,” because they can’t be fully configured in advance. The agent can’t just be static — it has to adapt in real-time to what the user wants or the situation demands.
Agent hooks bring those capabilities to Flue. For example, a support agent might bring in an account management tool after first verifying a user.
File based magic is an antipattern
Schott’s thinking about how to build an agent framework has evolved rapidly since he publicly launched Flue 1 in early May. Initially, he wanted to take existing web framework concepts and apply them to his new agent framework. He uses file-based routing as an example.
“So we kind of naively ported that over to Flue, thinking — great, well, I’ll put your five agents in these five files, and that’ll be the five routes that they expose. But for a lot of people building with Flue, especially the bigger customers, their whole company is one agent. They don’t care about routing. There’s one agent.”
So after the first Flue users showed these early patterns, composability became front of mind for Schott. That led him back to React.
“As you can see from the Flue 2 API, we’re taking it more from React [...] than we are from Astro or Next.js — where it’s less about routing and these website concepts and more about, at its base level, how do you compose an agent on many different things?”
Flue’s central proposition: agents need a harness
A key concept in Flue is that an agent must have a harness — meaning that it’s in an environment where it has access to the context and capabilities needed to accomplish various tasks.
“Instead of you and your code driving the LLM and telling it what to do with scripts, you’re putting the agent into this harness, and it is able to drive itself and work through problems,” explained Schott.
Flue is built on top of Pi [ https://substack.com/redirect/3fbd757b-72f3-44bc-982f-86657898d25a?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], an open source minimal harness. Essentially, Flue is an opinionated take on Pi — adding features that Schott thinks are helpful to developers building agents. For example: hosted agents in Flue 2 are now built with Vite, an open source build tool.
Indeed, Schott likens Pi’s role to the foundational role that Vite now plays beneath Astro.
“I think Pi can serve that role, where it’s the right abstraction — it doesn’t do too much, but it gives the right APIs that then we can go and say, well, let’s have an opinionated take on this that does more.”
Building on Pi meant committing to having a built-in agent harness.
“Our early bet was that the harness is actually not a feature, but it’s fundamental to what you think an agent is,” Schott said. “There is no agent without a harness.”
Building Flue agents with coding agents
The Flue project began earlier this year within the Astro repository, as an issue-triage system. At first, it was an LLM-driven script or workflow reviewing issues. But then, explained Schott, it gained the ability to take actions in the repo.
“It started to transition from just automation in a repo to wanting to take the Claude Code experience, make it headless, make it hostable and run it in the cloud.”
So that’s when the idea of a harness as anchor emerged. Indeed, in his v1 launch post [ https://substack.com/redirect/7cb19783-c8e0-4e15-bc17-e54e0e9d70b4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] in early May, Schott described Flue as “like Claude Code, but 100% headless and programmable.”
I myself tested out Flue using Claude Code, which guided me through setting up my first Flue agent. And Schott confirmed this is how many developers use Flue.
“We very much are building for them,” he said, regarding AI coding agents. “Our whole onboarding flow is that, you know, pass this prompt to your agent, it’s gonna guide you through it. All of our docs have markdown support.”
Where Flue fits in the agent development stack
The closest comparison to Flue is Vercel’s eve, which also treats the harness as foundational. Vercel and Cloudflare have been known to beef [ https://substack.com/redirect/0727d2f6-f8c4-4537-87dd-4955e8497754?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] in public, but Schott is generous in his opinion of eve [ https://substack.com/redirect/60918ca4-903e-42d9-94ed-44b1972d8653?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
“Eve, I think, is the most directly competitive,” Schott said. “It came around at the same time, so it had that same take that a harness is built-in.”
Schott also referenced what he called the “OG agent frameworks,” which came before Flue and so weren’t created with a harness as the central concept. He listed Vercel’s AI SDK [ https://substack.com/redirect/5a635b49-dc46-4427-8acf-5b29533f1b92?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Cloudflare’s Agents SDK [ https://substack.com/redirect/8041d57b-6375-42a2-a0a1-bf33c9b914c0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], and Mastra [ https://substack.com/redirect/806df20d-10ae-4c72-9fb0-4948c765b50c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] (developed by the same team that built Gatsby, a web framework predating Astro).
While these “OG agent frameworks” are all adding harnesses now, Schott considers that an added feature — whereas Flue and eve both have built-in harnesses.
I asked where Flue sits compared to emerging “meta-harnesses [ https://substack.com/redirect/e0861d14-21bb-47f1-80fe-d424662eadc5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ],” like Databricks’ Omnigent and perhaps even the self-improving Exo harness [ https://substack.com/redirect/cdd9149f-804f-46ea-8a32-a883985dcb3f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
Note: we’re also publishing our interview with Exo coauthor Alex Krentsel this weekend; it’s worth a watch and has a bonus discussion on OpenClaw architecture!
Schott rightly noted that there’s confusion about what the term meta-harness even means at this early stage. Regardless, he thinks having one API for working across all harnesses would muddle the story for Flue. His framework specifically defines how skills work in Flue, how subagents work, and so on. As he put it, “the framework [Flue] and the harness are very intertwined.”
He personally finds the meta-harness discussion fascinating, and has played with Exo, but says it’s “a different interest scenario that isn’t really related to hosted agents.”
The Cloudflare connection
Throughout the interview, Schott referenced being able to take advantage of his employer Cloudflare’s tooling and infrastructure [ https://substack.com/redirect/08356177-22d2-49dc-8714-67e930f33a7e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. But he was also very clear that Flue is an “open source framework for every host,” as he put it, and he wants it to stay that way.
“The best tools are the ones that float above the host,” he said. “That opens the door for the most developer adoption and the most innovation.”
Host portability [ https://substack.com/redirect/6ef69037-6930-4234-a64f-6b9c92e5238c?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] is one of Flue’s defining principles — and perhaps that’s where the fundamental difference to Vercel’s eve is. While eve can also be self-hosted, it is optimized to take advantage of Vercel’s many features. Of course that’s a known playbook of Vercel, which does the same thing with Next.js [ https://substack.com/redirect/adde8821-0ae6-4c25-92d6-9d90a24c51d0?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ].
All that said, Vercel itself has shown that a Flue agent can be deployed on Vercel [ https://substack.com/redirect/ddeb81e5-fca9-46cf-970a-7be61c0ffa98?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. So the two companies can play nice together.
I also mentioned LangChain’s new Managed Deep Agents [ https://substack.com/redirect/93f6c0d8-4a0d-4e6e-afb1-fb86b25266e4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] offering as an example of hosted agent platforms coming onto the market. However, Schott said a managed agents product is not currently on Flue’s roadmap.
“It’s so early for us, we’re just focused on building the best harness,” he said.
Links to find Flue [ https://substack.com/redirect/2bc6706e-0b34-4028-865a-77868d7a5a46?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] and Fred [ https://substack.com/redirect/60918ca4-903e-42d9-94ed-44b1972d8653?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] online; Richard is at @ricmac [ https://substack.com/redirect/53b0640e-6c40-46c5-908b-65eebcb817a1?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. This is a new written interview series we are trying out for subscribers — let us know your feedback!

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakl4TVRNd09UQTJOU3dpYVdGMElqb3hOemcyT0RBNU1UWTNMQ0psZUhBaU9qRTRNVGd6TkRVeE5qY3NJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5scElLUExRQWhWQ2ZLZDhnU3Y1MWhPOGlfc2pwcExMNUJkOW5yYXl0d3prIiwicCI6MjExMzA5MDY1LCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc4NjgwOTE2NywiZXhwIjoyMTAyMzg1MTY3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.y0FiVTRjsaLpOEOwqBgBTpEJVQ-Z-hJocELVrNt9s5Y?
