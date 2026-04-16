---
title: Mini-Vibe Check: Claude Managed Agents Handle the Infrastructure Work
type: source
source_type: article
url: https://every.to/source-code/mini-vibe-check-claude-managed-agents-handle-the-infrastructure-work
fetched: 2026-04-15
---

# Mini-Vibe Check: Claude Managed Agents Handle the Infrastructure Work

*Was this newsletter forwarded to you? [Sign up](https://every.to/account) to get it in your inbox.*

---

## **‘AI & I’: The case against LLMs**

Today, we’re releasing a new episode of our podcast *[AI & I](https://every.to/podcast)*. **[Dan Shipper](https://every.to/@danshipper)** sits down with **Eve Bodnia**, founder and CEO of Logical Intelligence, which is developing an alternative AI model to LLMs. They discussed a question most people in AI are afraid to ask: What if LLMs aren’t going to be the most powerful form of AI?

Bodnia argues that LLMs have intrinsic weaknesses, notably non-language tasks such as spatial reasoning, logical verification, and real-time data analysis. Her solution: energy-based models (EBMs), which map possible outcomes onto a mathematical landscape. Likely outcomes sit in valleys, and unlikely ones sit on peaks. Whereas LLMs process one token at a time, an EBM scans the full terrain to find the lowest point, or the most probable answer. Bodnia argues that it’s this approach, not bigger LLMs, that will lead to the next AI phase shift.

Watch on [X](https://x.com/danshipper/status/2044431229504643413) or [YouTube](https://youtu.be/Q-i8ZSUCtIc), or listen on [Spotify](https://open.spotify.com/episode/60S89CuHP2RDnG2H8rVKcF?si=K0xY56x3RTenQIEbr3iTXQ) or [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-ai-model-built-for-what-llms-cant-do/id1719789201?i=1000761561428). You can also read [the transcript](https://every.to/podcast/transcript-the-ai-model-built-for-what-llms-can-t-do).

Here’s how LLMs and EBMs are different, according to Bodnia:

* **Architecture transparency:** You can’t see inside an LLM; you can only evaluate its outputs. EBMs are governed by physics, which means their architecture is legible while they’re running. “Think of it as something that doesn’t play a guessing game, with an architecture that essentially allows it to self-align as it processes information,” she says. “It’s no longer a black box.”
* **Language-based versus data-native:** LLMs are language-dependent even when the task has nothing to do with language, like data analysis. “If your data is numbers, relationships, and functions, and you try to map those rules into words and then search for the next word, you’re losing a lot of information,” Bodnia says. EBMs work directly with the underlying data structure, including numbers and spatial coordinates.
* **Sequential versus panoramic reasoning:** An LLM is like navigating San Francisco without a map. Each turn constrains the next, and if you go down the wrong street, you can’t reverse course. An EBM, by contrast, has the bird’s-eye view—it can evaluate multiple routes at once and course-correct before hitting a dead end.

Miss an episode? Catch up on Dan’s recent conversations with [LinkedIn cofounder](https://every.to) **[Reid Hoffman](https://every.to)**; the team that built Claude Code, **[Cat Wu](https://every.to)** [and](https://every.to) **[Boris Cherny](https://every.to)**; [Vercel cofounder](https://every.to) **[Guillermo Rauch](https://every.to)**; [podcaster](https://every.to) **[Dwarkesh Patel](https://every.to)**; and others, and learn how they use AI to think, create, and relate.

---

## **Mini-Vibe Check: Claude Managed Agents**

*Or that feeling when the problem you’ve spent a lot of time solving gets solved for you*

We’re [all about agents](https://every.to/source-code/how-we-run-a-25-person-company-on-four-ai-agents) at Every. Which means many of us have devoted a lot of time to building the infrastructure that makes them run.

That work matters a lot less now since Anthropic launched [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) earlier this month in public beta, a hosted service that handles sessions, memory, tool use, and credentials. You say how you want your agent to operate, and Claude makes it happen.

It’s a true “oh shit” moment, says Dan, one that frees up considerable energy to focus on other problems—good!—and commoditizes a skillset you may have spent months developing—destabilizing, maybe!

For those at the edge of AI, the experience of building something only for it to become a free offering from a frontier company is becoming increasingly common.

**[Spiral](https://writewithspiral.com/?utm_source=everywebsite)** general manager **[Marcus Moretti](https://every.to/@marcus_fd8302_1)** used the service to spin up a new Spiral agent. Agents already power the Spiral web experience, but there was an opportunity to build a new one designed specifically for interacting with other agents calling Spiral’s API. (Agents don’t require the same conversational niceties as humans.)

With managed agents, the process took a few hours. To be fair, building the agent in code wouldn’t have taken much longer, Marcus says—he already had a working agent he could have extended with the help of Claude Code. But it would still require maintaining much of the agent infrastructure in our code, which would have lots of surface area for bugs. Managed Agents makes building slightly faster, but “the more significant advantage is that Anthropic is handling the technical implementation of agent primitives,” Marcus says. “I know it works versus having to test that whole set of things myself.”

An unanticipated benefit: It’s easier to improve existing agents. To update the system prompt or underlying model, ”I just make a change in the dashboard, hit save, and it’s live,” Marcus says.

---

## **Jagged frontier**

*Every’s head of platform argues we need new vocabulary for the AI-pilled*

If you have ever contemplated how to describe the “amniotic tranquility of being indoors during a thunderstorm,” *[The Dictionary of Obscure Sorrows](https://www.thedictionaryofobscuresorrows.com/)* has a proposal: “Chrysalism,” derived from the Latin for a butterfly’s pupa, a chrysalis. The dictionary is a beautiful, wandering tome billing itself as a “compendium of new words for emotions.” It’s also

one of my favorite books.

I have been thinking about it lately because I keep reaching for the wrong words—words built for a different conversation.

Thanks to AI, technical language that once hid behind the abstraction of machines is entering general circulation…and causing general confusion. I use the term “non-deterministic” in conversation regularly to describe how, given the same input, AI systems won’t always give you the same output. People who haven’t lived their lives as computer scientists furrow their brow at the term—it has zero resonance for them.

Even the lexicon of the digital age to date falls short in capturing some of the peculiar emotions and experiences of this new era. What do we call the unsettling feeling of receiving a wrong answer from a trusted system, the lurch of losing the thread mid-thought, or the heady fever of late-night building?

So instead of forcing old terms into new molds, maybe we need new words:

**Variagic** (adj.)—Describing the unease of asking the same question twice and getting two different answers, both equally confident. A variagic conversation is one where you run the same prompt and get two different answers, forcing you to realize that the other side is not inconsistent but simply contains more possibilities than any single encounter can surface. From Latin *varius*, changing or diverse, and Greek *agos*, that which leads. What the engineers call non-deterministic.

**Memorantia** (n.)—The tendency to prepare so much from past experience that you become useless in any new one. The condition that plagues a student who memorizes every answer from last year’s exam, only to freeze at an unfamiliar question. From Latin *memorare*, to remember, and *rantia*, a suffix suggesting excess. This is what the engineers call overfitting, when algorithms fit the training data too closely.

**Fenestralgia** (n.)—The quiet ache of knowing your mind can only hold so much at once, and that every new thing you pay attention to gently pushes something else into the dark. The sense, mid-conversation, that you’ve already lost the beginning of it. From Latin *fenestra*, window, and Greek *algos*, pain. This is what the engineers call the context window—the model’s finite ability to hold context.

Right now, people are making decisions without the right words to underpin them. Language follows understanding and crystalizes it. You feel the thing, then you find the word. We’re all writing the dictionary now.*—[Willie Williams](https://every.to/@williewilliams)*

---

## **Log on**

We [host camps and workshops](https://every.to/events) on topics like [compound engineering](http://youtube.com/watch?v=7YUBxMTF1Tc&time_continue=3&source_ve_path=NzY3NTg&embeds_referring_euri=https%3A%2F%2Fevery.to%2F) and [writing with AI](https://www.youtube.com/watch?v=oEvjbPwGwnc) to share the knowledge we’ve acquired from training teams at companies like the [New York Times and leading hedge funds](https://every.to/on-every/the-next-chapter-of-every-consulting), and by learning and playing with AI every day ourselves.

#### **This week’s camp**

[Compound Engineering Camp](https://every.to): **[Cora](https://cora.computer/)** general manager **[Kieran Klaassen](https://every.to/@kieran_1355)** and product leader **Trevin Chow** will walk us through what’s new, go deeper on the brainstorm and ideate steps, and share examples of using the compound engineering plugin in product-focused workflows. This virtual event takes place on Friday, April 17.

#### **Recordings you may have missed**

## ---

## **Discuss**

*Models as coworkers*

“[Codex](https://every.to/vibe-check/codex-vibe-check) is like that grumpy senior engineer in your office. When there’s an issue, he’s your go-to guy. He’s not fun to talk to—he’s a bit condescending, asks pointed questions—but things get done. [Opus](https://every.to/vibe-check/opus-4-6) is more like that employee who’s really fun to hang out with, but when things actually need to get done, he’s always postponing. So: If you want to vibe and explore, use Opus. If you want production-ready code, use Codex.”—**[Naveen Naidu](https://every.to/@naveen_6804)**, general manager of **[Monologue](https://www.monologue.to/?utm_source=everywebsite)**

---

***[Laura Entis](https://every.to/@laura_27bbaf_1)*** *is a staff writer at Every. You can follow her on [LinkedIn](https://www.linkedin.com/in/lauraentis/).*

*To read more essays like this, subscribe to [Every](https://every.to/subscribe), and follow us on X at [@every](http://twitter.com/every) and on [LinkedIn](https://www.linkedin.com/company/everyinc/).*

*For sponsorship opportunities, reach out to sponsorships@every.to.*
