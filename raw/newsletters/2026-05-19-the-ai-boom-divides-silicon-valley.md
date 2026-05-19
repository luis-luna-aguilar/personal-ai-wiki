---
title: "🤯  The AI boom divides Silicon Valley"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-05-19
gmail_id: 19e405409fc566ea
---

# 🤯  The AI boom divides Silicon Valley

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-05-19

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/324701a6-eea1-4d3f-a5ee-d01360e2f5be/Group_Wispr__2_.jpg?t=1779132514)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 

----------
**Welcome back.** Every tech boom has winners and losers, but AI is polarizing Silicon Valley like never before. A renowned VC in a viral post with 12 million views breaks down this divide, showing that even those who "made it" aren't fine. Read the [**full perspective here.**](https://x.com/deedydas/status/2055491938464489888)

**Also:** Ex-Google engineer's $400K remote job blueprint, the 7 untapped side-project ideas from Notion's former Head of Community, and why Karpathy says he's never felt more behind.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* What on the earth is Context Pruning

* How to catch Claude Code's spec drift

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/900a2115-11ba-43d6-b7a0-c08f88fdd30b/1Frame_1000003526.jpg?t=1779191139)
Follow image link: (https://x.com/cursor_ai/status/2056415413077233983)
Caption: Check out how Composer 2.5 performs vs other frontier models.


--------------------
**Cursor ships its most capable coding model yet:** The AI coding startup just dropped [**Composer 2.5**](https://cursor.com/blog/composer-2-5), a model designed for long-running tasks that handles complex instructions way more reliably than the previous version. It goes toe-to-toe with Opus 4.7 and GPT-5.5 on coding benchmarks, while costing just $0.50 per million input tokens, a fraction of the price. The team is also partnering with xAI to train an even bigger model from scratch on Colossus 2.

**Cloudflare red-teams its own code with Anthropic's Mythos:** The web infrastructure company just [released results](https://x.com/Cloudflare/status/2056360412510060748) from Project Glasswing, where it tested Mythos against 50 of its own code repositories. The model was able to chain minor bugs into major security holes, even writing working proof-of-concept code. Cloudflare's main takeaway is that simply patching faster isn't the answer. Instead, engineering teams need to build resilient architectures that can actually withstand the next inevitable exploit.

**Cognition ships an always-on bug triage agent:** The SF-based startup just shipped [**Auto-Triage**](https://x.com/cognition/status/2056396941181727210), a persistent agent that monitors your Slack channels and investigates bugs as soon as they're reported. A parent Devin filters out the noise before spinning up focused sub-sessions to find root causes, post diagnoses, and tags the appropriate code owner. With a shared long-term memory, it can deduplicate repeat reports and learn the team’s ownership map.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [Cursor for code. Claude for thinking. What about input?](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c2c00094-b97e-4e7a-960b-e463eebcc8f8/Wispr_the_code_20_may.png?t=1779132790)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
==Your dev stack got an AI upgrade everywhere except the input layer. You're still typing every prompt, every ticket, every review comment by hand.==

==[**Wispr Flow**](https://ref.wisprflow.ai/thecode)==== closes that gap. Dictate into Cursor, VS Code, Slack, Linear, or anywhere else you work. It's syntax-aware: camelCase, snake_case, acronyms, and file names all come through clean. Mention a file in Cursor or Windsurf, and it auto-tags.==

==[**It's the voice layer for an AI-native workflow**](https://ref.wisprflow.ai/thecode)====. Speak your intent. Your tools do the rest.==

==Available on Mac, Windows, iPhone, and Android. Used by millions of developers, including teams at OpenAI and Mercury.==

==[**Try free**](https://ref.wisprflow.ai/thecode)==


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **What on the earth is Context Pruning**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f89b6f2f-0ee8-403c-adcb-2bb579801627/superhumanteam_a_software_engineering_team_working_on_trimmin_50cb1fb8-cb5c-4cad-b03d-5cc6884e82c4_1.jpg?t=1779185158)
Caption: Source: The Code, Superhuman


--------------------
**Context windows keep growing.** Every model release this year has pushed limits higher, and teams have responded by stuffing prompts with retrieved passages, chat histories, and boilerplate. The bet was that more context meant better answers. Instead, costs are climbing, latency is creeping, and output quality is dropping. Bigger windows haven't fixed the problem they were supposed to solve.

**Lost in the middle.** LLMs ignore information buried in the middle of long prompts, and length alone tanks performance regardless of what's in it. A [recent study](https://arxiv.org/html/2510.05381v1) found a model losing nearly 70 points of accuracy on a standard knowledge benchmark just because researchers padded the prompt with filler tokens. Million-token windows have effective lengths far shorter than the marketing claims.

**Context pruning is the solution.** This technique works by scoring every bit of input (tokens, sentences, or chunks) and tossing out the low-value parts before the model even gets to them. Teams running RAG are using it to trim the same bloated passages and chat histories that clutter their prompts. It cuts costs, lowers latency, and usually leads to better results because the model isn't struggling to find the signal in the noise.

**Code and chats break differently.** Trimming individual tokens is risky because it can break code structure or disrupt the flow of a conversation. Chunk-level methods, which keep entire functions or sentences intact, are much more effective. This [**hands-on guide**](https://redis.io/blog/context-pruning-llm-tokens/) walks through which technique best fits your workload.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d1037a59-f88b-4c54-972d-151bd6b2d4c9/CleanShot_2026-05-19_at_13.45.19_2x.jpg?t=1779178591)
Caption: Meme of the day.


--------------------
* **Remote Roadmap:** An ex-Google engineer just shared the [**5-part system**](https://www.youtube.com/watch?v=JKZgkFiDA14) she'd use to land a $400K remote software job from scratch today.

* **Power Mode:** Most developers run Claude Code like a smarter ChatGPT. These [**12 setup tricks**](https://x.com/NainsiDwiv50980/status/2056021997659017452) unlock a full AI engineering environment.

* **Inside Track:** Google DeepMind's Gemini Pre-training Lead just [**dropped**](https://x.com/FeinbergVlad/status/2056383124829872466) the blueprint to land a job at a top AI lab (1M views).

* **Code Standards:** This viral GitHub **[repo](https://github.com/bendc/frontend-guidelines)** extracts the HTML, CSS, and JS best practices every dev should add to their library (9K stars, 2.9K bookmarks).

* **Monorepo Mode:** Anthropic just published the patterns [**top teams use**](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) to deploy Claude Code across million-line monorepos and decades-old legacy systems.

* **Karpathy Confession:** A year after coining "vibe coding," Andrej Karpathy admits he's never felt more behind. The AI code he over-trusted now gives him "heart attacks." One dev [**breaks it down.**](https://x.com/atmoio/status/2056365603867251075)

* **Agent Stack:** This thread breaks down the [**12 integrations**](https://x.com/akshay_pachaar/status/2056356792494682385) that turn Hermes into a real teammate across code, comms, and revenue.

* **Side Quests:** Notion's former Head of Community just shared 7 untapped [**side-project ideas**](https://x.com/benln/status/2056041334490710205) you can start building today.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to catch Claude Code's spec drift**

Claude Code makes dozens of decisions when implementing a spec, from resolving ambiguities to picking tradeoffs. Since these don't show up in the diff, you often only spot issues when things break in review or production. 

An engineer on Anthropic's Claude Code team [shared](https://x.com/trq212/status/2056415973125796184) a prompt that forces the tool to log every decision to a file as it works. Just append this to any implementation request:

```
Implement . As you work maintain a running implementation-notes.html file that captures anything I should know about how the implementation diverges from or interprets the spec, including:

- Design decisions: choices you made where the spec was ambiguous
- Deviations: places where you intentionally departed from the spec, and why
- Tradeoffs:  alternatives you considered and why you picked what you did
- Open questions: anything you'd want me to confirm or revise
```
By reading the file once the task is finished, you'll know exactly which decisions were made and why before you even dive into the code.

P.S. You can find 50+ AI coding hacks [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6c193bc0-fa86-46e3-b8bc-a4489bca8837/Thumbnail__34_.jpg?t=1779178663)
Follow image link: (https://www.youtube.com/watch?v=Qrpm7E80wQ0)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to use HTML files as AI specs (by a Claude Code engineer):**](https://www.youtube.com/watch?v=Qrpm7E80wQ0) This tutorial shows developers how and why HTML is replacing Markdown for AI planning. With Claude Code, you can generate interactive HTML specs, visual mockups, and living design systems. This approach makes complex AI outputs much easier to read, edit, and collaborate on, helping you build better products.

———————————————————————————

### **Top Tool**

[**DesignMD:**](https://designmd.cc) This tool analyzes live websites to extract structured design intelligence like typography, spacing, and colors. It lets you paste any URL to instantly generate actionable design system insights and AI-ready prompts.

———————————————————————————

### **Top Repo**

[**Browse.sh (by Browserbase):**](https://x.com/browserbase/status/2056404332824944970) A browser CLI for your agents. It provides a single interface for skills, browser primitives, debugging, and cloud sessions, all built specifically for agent-driven workflows.

———————————————————————————

### **Trending Paper**

[**How to use /goal in Codex (by OpenAI):**](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex) Standard prompts often fail at long tasks because you have to keep repeating the end goal after every step. Codex solves this with /goals, which keeps the model focused on a single objective until it is finished. This cookbook covers when to use them, how they change the workflow, and how to write clear goals with specific constraints and success criteria.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 280K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/cursor-drops-composer-2-5-cognition-unveils-devin-auto-triage
