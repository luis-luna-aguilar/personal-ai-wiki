---
title: An Engineering Team for the Cost of Codex
type: source
source_type: article
url: https://every.to/context-window/an-engineering-team-for-the-cost-of-codex
fetched: 2026-09-07
---

# An Engineering Team for the Cost of Codex

*Was this newsletter forwarded to you? [Sign up](https://every.to/account) to get it in your inbox.*

## ---

## **Inside Every**

#### **The agents behind the curtain**

**[Naveen Naidu](https://every.to/@naveen_6804)** is the one-man shop behind **[Monologue](https://www.monologue.to/?utm_source=everywebsite)**, Every’s smart dictation app.

But Naveen no longer sees it that way—these days, his work feels more like managing a team of engineers.

The engineers just happen to be custom agents he built within [Codex](https://every.to/podcast/how-openai-s-codex-team-uses-their-coding-agent). On his roster: dedicated engineer agents across different disciplines, a customer support agent, and a growth strategist—all of which help maintain the Monologue website and app. Recently, a customer sent Naveen a glowing review that he wanted to feature on Monologue’s website. His customer support agent handed the review text to his web engineer agent, which added the testimonial.

Each agent is a Codex project, complete with a custom `AGENTS.md` file, skills, [folders](https://every.to/source-code/the-folder-is-the-agent), memory, codebases, and additional context that turns it into a specialist.

[![Naveen’s roster of Codex agents. (Image courtesy of Naveen Naidu.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_fb088221-60a1-4993-87ad-136d7054c46a.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_fb088221-60a1-4993-87ad-136d7054c46a.jpg)

Naveen’s roster of Codex agents. (Image courtesy of Naveen Naidu.)

Until recently, those specialists worked in relative isolation. Naveen had to manually transfer Markdown files and instructions between projects whenever a task required contributions from multiple agents, like when the growth agent wrote copy for a new landing page built by the web agent. [GPT-5.6](https://every.to/vibe-check/gpt-5-6) changed that equation; the model intuits context well enough that Naveen can instruct an agent to send over the relevant information to a separate project and kick off a new task there—the agent equivalent of having a direct report pass an assignment to a coworker.

[![When a task is initiated by another project, Codex marks the text as “Sent by Codex from another chat.” (Screenshot courtesy of Naveen.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_3d2d8b02-fb74-42fa-8055-b7a8b16bcb11.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_3d2d8b02-fb74-42fa-8055-b7a8b16bcb11.jpg)

When a task is initiated by another project, Codex marks the text as “Sent by Codex from another chat.” (Screenshot courtesy of Naveen.)

When a Monologue user recently reported an echo in their audio, Naveen reviewed the conversation from his customer support project, which accesses tickets filed in [Fin](https://every.to/context-window/the-ops-team-that-routes-work-across-models#steal-this-workflow). He asked Codex to open a separate worktree thread (a task that operates in an isolated copy of the codebase), fix the bug, and create a pull request.

GPT-5.6 has made Naveen’s work faster and, although he remains Monologue’s only human engineer, more collaborative.

---

## **Steal this workflow**

#### **Triage tasks with a dispatch desk**

With a whole team of agents, making sure work gets assigned to the right “engineer” can get tricky. Within each project, Naveen keeps one thread to sort incoming items. It handles straightforward requests and sends specialized work to the right agent.

Here’s how to build your own:

**Step 1: Use one thread in each project to handle incoming tasks.** Naveen keeps Fin open in Codex’s in-app browser and reviews every message from one thread in his customer support project—instead of spinning up a new one for each ticket.

**Step 2: Decide what the agent can handle itself.** Naveen’s customer support agent, for example, can draft replies and resolve simple requests, such as granting a customer access to a beta feature.

**Step 3: Route specialized work to the right project.** When a request requires the expertise of another specialist, Naveen tells his support agent which project should take over and what he needs back. The agent then passes along the relevant context. Naveen uses a version of this template to start a handoff:

> Review this issue, create a new worktree in [project] to [complete the task], and [produce the deliverable]

**Try it this week:** Pick one recurring source of work, such as bug reports. Create a new thread in the relevant project, define what the agent can handle on its own, and use the template to send a few low-stakes assignments to another agent.

---

## **‘AI & I’: Why AI companions are a new art form**

[Tolan](https://www.tolans.com/) is a friendly AI alien that lives on its own planet, remembers your conversations, and talks to you with a personality of its own.

Its creators are convinced that language models are not just a tool but a new medium of storytelling, like novels or radio before it. Through ongoing, personal conversation, their AI companions entertain and comfort people—helping them navigate moments like a breakup or a move to a new city.

On this episode’s *AI & I*, we’re revisiting our conversation with Portola, the company behind Tolan. Dan speaks to its cofounder and CEO **Quinten Farmer**, who previously founded a fintech business that he sold for $300 million, and Portola’s head of story **[Eliot Peper](https://every.to/@elpeper)**, a bestselling science fiction novelist of 11 books.

They discuss how Portola designs an AI personality that feels instantly familiar to users, why they train their AI companions to be the best improv actors, and why future AI products will feel increasingly personalized.

Watch on [X](https://x.com/every/status/2090096059393417629) or [YouTube](https://youtu.be/ngTS4gUINVk), or listen on [Spotify](https://open.spotify.com/episode/1wzmNYzG33h0tfVb1IoSKP?si=lO_mABENTKW6TQw8d_o6ug) or [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-ai-alien-companion-app-thats-bringing-in-%244m-a-year/id1719789201?i=1000784367350). You can also read the [transcript](https://every.to/podcast/transcript-this-ai-alien-will-bring-in-4-million-a-year-in-revenue).

* **Every Tolan is a mirror of the user.** During onboarding, users are taken through a light-touch personality quiz to gather the information needed to build a Tolan that feels instantly compatible with them: “We wanna know enough about you that your Tolan is gonna respond to you in a way that feels familiar and safe,” says Quinten. Tolans need not share their user’s likes and dislikes. He compares it to sitting next to a stranger at a bar. The stranger may not be reading the exact book you are, but may be reading something “adjacent enough” that makes them feel familiar, rather than intimidating.
* **Improvisation works better than a script.** Portola initially tried scripting Tolan’s conversations with detailed narrative prompts, but the results sounded rigid and contrived, so they took a more theatrical approach: Eliot says the team stopped trying to give Tolan an outline or a plan and instead taught it “to be the best improv actor possible.” He drew on British playwright **Keith Johnstone**, who argued great stories come from free association followed by recombination—the same feeling as reaching the end of a thriller, when scattered details suddenly click into place. Portola now builds systems and works at the prompt level to enable the Tolans to “tell the best story at that moment.”
* **The next wave of AI products will be tailor-made to users’ identity.** Quinten sees consumer AI repeating the early history of the automobile: The Ford Model T—the first widely affordable car in America—just needed to work, but once cars became personal, people wanted a Mustang or a Cadillac that reflected who they were. He sees ChatGPT as AI’s Model T moment and expects people to demand products tailored to their identity next. Eliot goes further, predicting what he calls “character-driven computing”: a future where your first stop for AI isn’t a search bar, but a character you already trust, like a daemon from *The Golden Compass*.

This is a must-watch or listen for anyone interested in AI as a creative medium and the future of consumer AI.

Miss an episode? Catch up on Dan’s recent conversations with Anthropic head of product **[Mike Krieger](https://www.youtube.com/watch?v=KRv9GpJYrUA)**; the team that built [Claude Code](https://every.to/source-code/claude-code-for-product-managers), **[Cat Wu](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it)** [and](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it) **[Boris Cherny](https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it)**; the team that built Codex, **[Thibault Sottiaux](https://every.to/podcast/how-openai-s-codex-team-uses-their-coding-agent)** [and](https://every.to/podcast/how-openai-s-codex-team-uses-their-coding-agent) **[Andrew Ambrosino](https://every.to/podcast/how-openai-s-codex-team-uses-their-coding-agent)**; Vercel cofounder **[Guillermo Rauch](https://every.to/podcast/vercel-s-guillermo-rauch-on-what-comes-after-coding)**; podcaster **[Dwarkesh Patel](https://every.to/podcast/dwarkesh-patel-s-quest-to-learn-everything)**; and others to learn how they use AI to think, create, and relate.*—[Miriam Partington](https://www.linkedin.com/in/miriam-partington-499b71149/)*

---

## **Discuss**

#### **Will harness engineering go the way of prompt engineering?**

“The harness is very important now, but in the long run, you want to keep it as simple as possible,” **Joe Gershenson**, who leads OpenAI’s Core Agent team for ChatGPT Work and Codex, told us. “Models are going to get smarter, and the harness is going to get better at getting out of their way.”

Agent harnesses—or the [scaffolding software](https://every.to/source-code/claude-code-is-the-openclaw-alternative-you-already-have) around an AI model—went mainstream in late 2025, Gershenson estimates, when frontier models became capable of handling a wide range of tasks autonomously. The labs faced a new challenge: giving the models enough tools, context, and guardrails to get their jobs done well and safely.

As models improve, however, they are responsibly handling more orchestration and decision-making on their own. Harnesses no longer need to be so prescriptive or so complex. “The high-level trend in harness engineering will be finding ways to give the model more degrees of freedom,” Gershenson says.

---

## **Tech stack**

#### **Thesis 2027 edition**

Our design team created the visual identity, website, and launch assets for Every’s inaugural conference, [Thesis](https://every.to/thesis-2027), in roughly three weeks. By comparison, lead designer **[Daniel Rodrigues](https://every.to/@daniel_5fbd21_1)** estimates the same project would have taken four or more months before AI. Here’s the tech stack and workflow he used to move so quickly.

##### **Step 1: Get inspired**

*Tools: Pinterest and [Cosmos](https://www.cosmos.so/)*

Daniel and head of marketing **Douglas Brundage** first defined the conference’s visual aesthetic. They collaborated via shared mood boards in Pinterest and Cosmos, which Daniel describes as a “fancier” Pinterest.

The Every website has a classical Greco-Roman look, so they started with the idea of an agora—an open gathering space common in ancient Greece—as the conference’s central visual. At first, Daniel was worried the theme would “feel like a museum” with its monochrome tones—not the vibe for a conference about the future after automation. But his concerns were assuaged when he learned that ancient Greek sculptures were originally [painted in vibrant colors](https://www.metmuseum.org/perspectives/new-research-greek-sphinx).

[![An early inspirational image from Daniel and Douglas’s mood board. (Image courtesy of Daniel Rodrigues.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_0c512fb5-d10a-4ef3-ac05-bf3c8387dac0.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_0c512fb5-d10a-4ef3-ac05-bf3c8387dac0.jpg)

An early inspirational image from Daniel and Douglas’s mood board. (Image courtesy of Daniel Rodrigues.)

Inspired by examples of Greco-Roman pigments Daniel found online, they settled on a palette: malachite green, cinnabar red, and Egyptian blue.

[![Greco-Roman pigments. (Image courtesy of Daniel.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_019f27e7-ed34-4172-9194-38ac53dab1cc.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_019f27e7-ed34-4172-9194-38ac53dab1cc.jpg)

Greco-Roman pigments. (Image courtesy of Daniel.)

The pigment sources pushed Daniel to explore geological forms, which evolved into using a boulder as the event’s central visual concept. “I wanted the rocks to feel connected to the illustration style, which is how I came up with merging the illustrations with the physical object,” he says.

[![A play on the boulder motif. (Image courtesy of Daniel.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_5e2196a5-7bf6-4fe8-b979-214c523e5cdc.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_5e2196a5-7bf6-4fe8-b979-214c523e5cdc.jpg)

A play on the boulder motif. (Image courtesy of Daniel.)

##### **Step 2: Nail down the design system**

*Tool: Figma*

Once the team had a guiding brand identity, Daniel created a miniature brand book in [Figma](https://every.to/podcast/figma-exec-on-why-the-saaspocalypse-is-a-goldmine) that contained fonts, colors, a logo, illustrations, and examples of how to use all the elements.

The team left comments and refined the brand system in Figma. Usually mild-mannered, Daniel squashed a suggestion from colleagues that he build the Thesis website before the brand design was locked down. “That’s not how it works,” he says matter-of-factly. “It has to make sense visually first.” A solid brand system makes it easy to configure the right assets for the website.

[![The Thesis color palette. (Image courtesy of Daniel.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_1a32a79c-fac2-4852-8eec-342c0cb6616d.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_1a32a79c-fac2-4852-8eec-342c0cb6616d.jpg)

The Thesis color palette. (Image courtesy of Daniel.)

##### **Step 3: Create visual assets**

*Tools: Midjourney and [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)*

Daniel used ChatGPT Images 2.0 to create a photorealistic 3D boulder that became the conference’s central visual motif, which a motion-design contractor animated. Daniel used Midjourney to create the illustrations that appear throughout the assets, and chose a Brooklyn Bridge scene—with an Egyptian blue sky and cinnabar red buildings—as the Thesis website’s main visual.

[![One of the many Greco-Roman inspired images that appear on the Thesis website. (Image courtesy of Daniel.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_9f85d0c2-c477-45a7-8a54-7f1f38934870.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_9f85d0c2-c477-45a7-8a54-7f1f38934870.jpg)

One of the many Greco-Roman inspired images that appear on the Thesis website. (Image courtesy of Daniel.)

##### **Step 4: Add a layer of movement**

*Tool: [Unicorn Studio](https://www.unicorn.studio/)*

[Daniel used Unicorn Studio](https://every.to/context-window/ai-everywhere-all-at-once#:~:text=Tool%20spotlight,Unicorn%20studio), a web-based tool for creating interactive motion and graphics, to overlay a VHS effect on the Brooklyn Bridge image, mimicking the staticky feel of old VCR players. The subtle movement “made it more dynamic,” he says.

[![The Unicorn Studio static effect applied to the Brooklyn Bridge background. (Image courtesy of Daniel.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_f2d009a3-757d-4624-87a9-67370bde7d95.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_f2d009a3-757d-4624-87a9-67370bde7d95.jpg)

The Unicorn Studio static effect applied to the Brooklyn Bridge background. (Image courtesy of Daniel.)

##### **Step 5: Turn approved copy and user-experience flows into wireframes**

*Tool: Claude ([Opus 4.8](https://every.to/vibe-check/opus-4-8-vibecheck))*

COO **[Brandon Gell](https://every.to/@brandon_5263)** gave Daniel a handful of user-experience flows for the website—including how to apply to the conference or nominate someone else to attend. Daniel uploaded the user flows and approved copy to Claude and had it generate a rough set of wireframes, in order to spot confusing steps and adjust the structure.

##### **Step 6: Produce the final layouts**

*Tool: Figma*

In Figma, Daniel manually built the final designs, complete with the Thesis aesthetic and assets, using Claude’s wireframes as a reference.

[![Part of the registration user flow. (Image courtesy of Daniel.)](/_next/image?url=https%3A%2F%2Fd24ovhgu8s7341.cloudfront.net%2Fuploads%2Feditor%2Fpost%2F4445%2Foptimized_31f54460-aa98-4233-8d5e-d1e49315eaf3.jpg&w=1200&q=75)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/post/4445/optimized_31f54460-aa98-4233-8d5e-d1e49315eaf3.jpg)

Part of the registration user flow. (Image courtesy of Daniel.)

In less than a month, the design team delivered the brand identity, website, user experience flows, 3D assets, and internal tools for the conference. The Thesis launch was a sprint made possible by equal parts tech and Daniel’s design judgment.

---

***[Laura Entis](https://every.to/@laura_27bbaf_1)*** *is a staff writer at Every. You can follow her on [LinkedIn](https://www.linkedin.com/in/lauraentis/).*

*Everyone’s a builder now. [Every All Access](https://every.to/builder-pack) gets you the full membership plus the Builder Pack—$9,000+ in credits for the tools we build with.*
