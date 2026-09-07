---
title: "Frontier Model Cost and Open-Weights Popularity is Driving Demand for Model
 Routing"
type: newsletter
sender: "Latent.Space <swyx@substack.com>"
received: 2026-08-18
gmail_id: 1a016d5941731ef8
---

# Frontier Model Cost and Open-Weights Popularity is Driving Demand for Model
 Routing

**From:** Latent.Space <swyx@substack.com>
**Date:** 2026-08-18

View this post on the web at https://www.latent.space/p/glean-model-routing

With the intense competition among frontier model companies, together with ever-increasing power of open-weight models like Kimi K3 and Qwen3.8-Max, model routing has become a key part of AI deployment. We’ve just seen Stripe buy OpenRouter for over $7B [ https://substack.com/redirect/b49b50cc-74eb-49fc-a345-ab3329e57665?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], but the trend is equally hot in enterprises.
Glean [ https://substack.com/redirect/45f026ad-0cc3-4871-ad77-54235e44d42f?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], co-founded and led by ex-Google Distinguished Engineer Arvind Jain, specializes in bringing AI to large organizations. It was last valued at $7.2B after a $150M Series F fund raise [ https://substack.com/redirect/86e44601-2e38-4426-8192-18062000a097?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] last June. This year, it reached $300 million in annual recurring revenue (ARR) [ https://substack.com/redirect/35577692-5f72-4a25-ab65-256cafc48c76?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] — a three-fold increase over 15 months.
Part of Glean’s mission is to select which model to use for each task — or indeed if an LLM is even required.
“A big goal of Glean is to avoid using LLMs for tasks where we don’t need them,” Jain told Latent Space. “Sometimes you’ll see queries in Glean where people are adding two numbers or multiplying two numbers. They could have used a calculator to do that.”
But what Glean is mostly trying to do is bring what Jain calls “one really powerful personal co-worker” to enterprise employees. And that means being a kind of meta-harness for leading LLMs.
“You can think of Glean today as a superset of ChatGPT, Claude, Gemini, Grok,” Jain said. “All these different AI products that we’ve been using day to day, Glean combines the power of all of them into one experience.”
With enterprises, bringing AI technology into an organization is just half the challenge. The other half is bringing organizational knowledge into the AI systems.
“Ultimately our business is to deeply understand your data, knowledge, and information, but also how work happens inside your company,” Jain said.
How model routing is done in Glean
So what does model routing mean in practice? Basically, Glean offers three levels of model selection:
Employees can explicitly choose a model.
Administrators can restrict models or impose usage limits.
Glean’s automatic mode selects a model dynamically for each task.
It turns out automatic mode is mostly chosen by Glean’s customers for economic reasons.
“Why are people talking about model routing? Why are they excited about it? It’s mostly because of cost,” Jain told us.
Another co-founder of Glean, engineering lead Tony Gentilcore, recently claimed [ https://substack.com/redirect/8cc956e7-7e2b-47db-91bc-1cd79083cec6?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] that Glean “is 4x more cost-effective” than Claude Code, “averaging $0.45 per task versus $1.84 for Claude Cowork.” He put that down to Glean’s “harness and routing capabilities.”
Individually, many of us are getting great value out of our $20, $100 or $200 monthly subscription to an LLM provider. But for an enterprise, the per-user costs can easily spiral out of control.
“AI models have been getting expensive,” Jain said. “Like, if you look at Opus or the latest models of GPT, the most advanced models. Not only are they very powerful, they can run much more complex tasks than the previous models. But on a per token basis, they’re more expensive — sometimes double or quadruple the rates of the previous models. And then users actually use them to run much longer tasks. So you’re spending, like, 10 times, 20 times, more, on a per user basis, than what you were doing last year. So the costs have gone up a lot.”
The human feedback loop
Another key factor in Glean’s rise is that it gets to see how ordinary business users are using AI. The product is potentially deployed to every employee as a “coworker,” and it’s also used to build and deploy agents across all departments and functions.
Among its customers, Zillow reports [ https://substack.com/redirect/57b16336-621d-4b0a-81fd-eff995c896ba?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] 80% adoption across 7,000 employees, while at Booking.com [ https://substack.com/redirect/aa6b6d9d-1296-4899-940c-2b4dcb4c8920?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], “Glean became the first AI platform adopted company-wide.” That kind of penetration gives Glean an enviable view into how AI is being used in enterprises.
“So we are getting to observe what people are actually doing with AI on a very broad basis,” said Jain. “We are getting to see when they’re on different types of tasks with AI, what models do they select first, and when they are not satisfied, when they actually upgrade to some other model [that] actually gives them the right results.”
This human feedback loop, at scale, helps improve the model routing system.
Here’s Waldo, gathering raw materials
Another part of Glean’s architecture is a model called Waldo, which Jain described as sitting on top of the large language models. Waldo was introduced in April [ https://substack.com/redirect/6cb54d99-4ec1-401b-bec1-04873a1adb9b?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ] as “Glean’s first agentic search model.”
In a technical blog post [ https://substack.com/redirect/9c5cab7a-dec7-4443-996f-bb6d1283d5a4?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], Waldo was portrayed as a kind of filtering process for user queries: it “decides how to break down the question, which tools to use, what to read next, and when it has enough evidence to hand off to a frontier model for a high-quality answer.”
This means the model routing is happening after Glean has determined what Jain calls the “raw materials” that are needed for the task.
“We’re able to assemble the raw materials needed to do the work without burning LLM tokens,” he added.
A corollary of this is that a cheaper model with better context may outperform a frontier model loaded with irrelevant data.
The rapid rise of open-weight models
Jain confirmed there is now significant interest from enterprises in open-weight models, primarily due to cost concerns. But this has only happened over the past few months.
“Last year, the usage [of open source LLMs] was minuscule and nobody was really seriously considering open source,” he said. Partly that was because of the “stigma” of many of these open source models being developed outside the US.
But suddenly, interest among enterprise customers has risen.
“So in the last three months, because AI got so expensive, businesses have started to find it untenable to maintain these AI investments,” Jain said. “Given that open source is an order of magnitude cheaper to do tasks, it has created a lot of interest. Today, I can say that in most enterprises, they are considering open source models to be a key part of their AI strategy.”
More than that, organizations tend not to rely on just one or two providers anymore — and the rise of open-weight models is driving this trend.
“Nobody is willing anymore to rely on only one model provider, or two, and nobody thinks that they can survive without open source,” Jain said.
Evals
You can’t have a serious conversation about AI in 2026 without discussing evals — assessing the quality of results from LLMs. I asked how Glean goes about doing evals and how that is fed back into the model routing system.
Jain said they have “internal testing systems” where they compare real-world workloads, across different query classes, with alternative options. So they let the model choose a route and in parallel they try to complete the same task with “some other models which are maybe a little bit less expensive and a little bit more expensive.”
Glean then uses “AI-based judges” to determine “how spot-on the model router was.”
“So there’s this continuous learning that gets updated with new real-world traffic, where basically what is happening is that you let the model router do the work for the user, but behind the scenes you run the same task,” Jain explained.
He added that this is done for only “a small fraction” of the real-world usage, but at Glean’s scale that’s more than enough to help train and improve the model router.
From enterprise search to end-to-end AI platform
One of the trends we’ll be monitoring going forward on Latent Space is how AI systems are being implemented within enterprises — and how some of these organizations are going full-on AI-native.
Glean is an especially interesting company to monitor for these trends, since it was one of the very first enterprise-facing AI companies. It was founded in early 2019, initially to tackle enterprise search. As Jain put it, Glean was “the first player to work with transformers and language models for businesses.”
In April 2023 [ https://substack.com/redirect/3143529b-a803-4323-b6f7-9e08ea3b1ca5?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ], swyx interviewed Deedy Das of Glean. Das, who is now a partner at venture firm Menlo Ventures, was a founding engineer at Glean. But even at that point, in 2023 — about four years into Glean — the focus was still mostly on enterprise search.
Now, in 2026, enterprises aren’t just using AI for search. AI is becoming an integral part of every employee’s workflow.
That makes Glean a much ‘sexier’ AI company, as Das himself said on his return to the Latent Space podcast last November [ https://substack.com/redirect/6c04929b-1811-4e55-8fbf-292a55fd2c3e?j=eyJ1IjoiODlhdDlmIn0.psR-epQqK_Wbg6RTI-yQkSgRmDIqosMhU9elL-EoqO0 ]. “Broadly, one of the things that I love about Glean is it’s such a boring unsexy company that became sexy later,” he said.
This brings us full circle back to model routing. Arvind Jain ended our discussion by calling Glean an “end-to-end AI platform” that gets “used very heavily” by its enterprise customers. This, he added, allows Glean to “have that data that is required to do effective model routing.”

Unsubscribe https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly93d3cubGF0ZW50LnNwYWNlL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzBPVGt6TlRBME16VXNJbkJ2YzNSZmFXUWlPakl4TVRjM01qRTVPU3dpYVdGMElqb3hOemczTURnNU5EZzRMQ0psZUhBaU9qRTRNVGcyTWpVME9EZ3NJbWx6Y3lJNkluQjFZaTB4TURnME1EZzVJaXdpYzNWaUlqb2laR2x6WVdKc1pWOWxiV0ZwYkNKOS5fekxRazVvNEE2Ti1za3RsQmh2V3NTeUxnWWszRHBnY1lsS002Y3JPTTJFIiwicCI6MjExNzcyMTk5LCJzIjoxMDg0MDg5LCJmIjp0cnVlLCJ1Ijo0OTkzNTA0MzUsImlhdCI6MTc4NzA4OTQ4OCwiZXhwIjoyMTAyNjY1NDg4LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.S5hq5SQzq_ZLge4D2weJ7PbNcSsdrqAN02k5XBDEZb8?
