---
title: "🔥  Ex-OpenAI CTO drops an interaction model"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-05-12
gmail_id: 19e1c4792054dfd7
---

# 🔥  Ex-OpenAI CTO drops an interaction model

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-05-12

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/24c343e8-3e5e-44d8-8293-b8be33ab9772/Group_Wispr__2_.jpg?t=1778568436)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 

----------
**Welcome back.** Working with AI still feels like a one-way street: you think, and it responds. True collaboration needs an interface that listens, sees, and reacts in real time without constant prompting. The AI lab founded by OpenAI's former CTO Mira Murati just unveiled a model that does exactly that.

**Also:** Find and fix bugs 10x faster with this new Codex workflow, set up Hermes Agent (the rising OpenClaw rival) in 30 minutes, and make sense of the tech job market paradox.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* How Shopify made its AI agent teach itself

* How to speed up big refactors in Claude Code

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/64e24117-93f3-4a6b-a26a-15d2309231b2/Thumbnail__25_.jpg?t=1778566700)
Follow image link: (https://x.com/thinkymachines/status/2053938892152435174)
Caption: Click here to watch Thinking Machines’ new model respond in real time.


--------------------
**Thinking Machines previews its first interaction model:** Former OpenAI CTO Mira Murati’s AI lab just released a research preview of [**TML-Interaction-Small**](https://thinkingmachines.ai/blog/interaction-models/). It’s a 276B-parameter model that processes audio, video, and text as continuous 200ms streams rather than separate turns. This allows the model to interrupt, provide backchannel feedback, and react to visual cues in real-time before you even finish speaking or typing, delivering responses in just 0.4 seconds. [**See it in action.**](https://www.youtube.com/watch?v=A12AVongNN4)

**OpenAI unveils a frontier AI platform for cyber defenders:** The ChatGPT maker just unveiled [**Daybreak**](https://openai.com/daybreak/), which pairs GPT-5.5 models with Codex Security to find vulnerabilities and generate patches inside code repositories. It builds an editable threat model from each codebase, narrows analysis to realistic attack paths, and then verifies every fix. They also launched a $4B [Deployment Company](https://openai.com/index/openai-launches-the-deployment-company/), after acquiring a consulting firm Tomoro, to embed 150+ engineers directly into businesses to build out production-ready AI.

**Anthropic ships unified view for running coding agents in parallel:** The AI lab just rolled out [**Agent View**](https://claude.com/blog/agent-view-in-claude-code) in Claude Code, a research preview that brings all your active sessions into a single list. This finally puts an end to the constant tab-swapping typical of parallel workflows by showing you exactly which agents are finished, still working, or waiting for your input. You can peek at any session to reply inline or move tasks to the background using the /bg command.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [Cursor for code. Claude for thinking. What about input?](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c98dde27-2c7e-4074-a586-2f4c59cc6e66/Wispr_the_code_5_may.png?t=1778569190)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
Your dev stack got an AI upgrade everywhere except the input layer. You're still typing every prompt, every ticket, every review comment by hand.

[**Wispr Flow**](https://ref.wisprflow.ai/thecode) closes that gap. Dictate into Cursor, VS Code, Slack, Linear, or anywhere else you work. It's syntax-aware: camelCase, snake_case, acronyms, and file names all come through clean. Mention a file in Cursor or Windsurf, and it auto-tags.

[**It's the voice layer for an AI-native workflow**](https://ref.wisprflow.ai/thecode). Speak your intent. Your tools do the rest.

Available on Mac, Windows, iPhone, and Android. Used by millions of developers, including teams at OpenAI and Mercury.

[**Try free**](https://ref.wisprflow.ai/thecode)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **How Shopify made its AI agent teach itself**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f86c511e-0423-4f9b-9428-9254aa1d7e91/superhumanteam_a_software_engineering_team_working_on_code_to_02de0da1-3256-4c40-8746-d95e3aad8ec9_1__1_.jpg?t=1778578726)
Caption: Source: The Code, Superhuman


--------------------
**Shopify is breaking away from the AI status quo.** Most AI coding tools operate behind closed doors. Cursor sits between you and your IDE, while ChatGPT and Claude live in private tabs that nobody else sees. But a few days ago, Shopify CEO Tobi Lütke [revealed](https://x.com/tobi/status/2053121182044451016) that their internal coding agent, River, does the exact opposite. River skips the Slack DMs and works entirely in public Slack channels. It’s a move that's paying off. River now handles one out of every eight PRs merged into their monorepo weekly.

**The whole company is watching.** River reads code, runs tests, queries the data warehouse, and opens PRs. Lütke describes this setup as a Lehrwerkstatt, a German tradition where apprentices learn simply by being near the masters.

**Working in public is paying off.** In just two months, River’s merge rate shot up from 36% to 77%. This wasn't because of a model upgrade; it happened because engineers watched River mess up in public and corrected it in real-time. Linear CEO Karri Saarinen says using their agent feels like "[accessing the company brain](https://x.com/karrisaarinen/status/2053946611395653931)." It opened 1,330 PRs last month alone, autonomously resolving 30% of bugs.

**Shopify cracked the playbook.** Django co-creator Simon Willison notes that Midjourney did the [same on Discord](https://x.com/simonw/status/2053529689122328947), teaching people how to prompt by letting them watch one another. Keeping AI conversations private means leaving leverage on the table. When you make the work visible, every prompt becomes a lesson for anyone watching, and that’s the new AI playbook for companies.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ace22526-21f2-428f-bc00-acd1608e1922/CleanShot_2026-05-12_at_11.51.34_2x.jpg?t=1778566937)
Caption: Meme of the day.


--------------------
* **Parallel Debugging:** OpenClaw's creator dropped a Codex workflow that fixes bugs [**10x faster**](https://x.com/steipete/status/2053032450138276274) using disposable sandboxes (3K likes).

* **Beyond Prompts:** If you only know prompt engineering, you may already be behind. This post covers the [**must-have skills**](https://x.com/akshay_pachaar/status/2053815461150859272) separating hobbyists from real AI engineers.

* **Claude Code Flow:** An ex-Vercel engineer [**dropped**](https://x.com/mattpocockuk/status/2053459748532392343) a 6-step Claude Code prototyping workflow with an unconventional use of /rewind (2.6K bookmarks).

* **Codex Unpacked:** This 10-minute deep dive from a top dev YouTuber covers [**everything new**](https://www.youtube.com/watch?v=t2G0L0cqktw) in Codex.

* **Herd of Donkeys**: One Redditor skipped the big-SaaS dream and built 65 tiny utility apps that bring in $4,200/month combined. His post shows exactly **[how he did it](https://x.com/xburak/status/2053871921364689195)** (3.9K likes).

* **Standup Magic:** Watch GPT-Realtime-2 turn spoken standup updates into live Kanban tickets. The repo is open for [**devs to fork**](https://x.com/OpenAIDevs/status/2053964133570412826) and customize (1K likes).

* **Claw Challenger:** Hermes is the new agent gaining traction as an OpenClaw rival. This 30-minute [walkthrough](https://www.youtube.com/watch?v=1ve4Atbqmoo&t=645s) covers the full setup.

* **Hiring Paradox**: Tech is firing and hiring engineers at the same time. 52K layoffs and 67K open roles this year alone. An Airbnb senior engineer just posted [**what's behind it**](https://www.youtube.com/watch?v=CC7g1K8e-LE) and how to position yourself.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to speed up big refactors in Claude Code**

Renaming a function across 200 files or swapping “axios” for “fetch” everywhere usually eats up an entire afternoon. The “[/batch](https://code.claude.com/docs/en/skills#bundled-skills)” command fixes this by splitting the workload across parallel agents:

```
/batch rename all instances of getUser to fetchUser across the repo
```
It breaks the task into 5 to 30 units, presents a plan, and then runs each unit in its own “git worktree” before opening one PR per agent.

P.S. You can find 50+ AI coding hacks [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/999b258a-a246-4776-80c6-ff40d17cfda5/Thumbnail__24_.jpg?t=1778565916)
Follow image link: (https://www.youtube.com/watch?v=6jOBSGSBQ3g)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to turn Karpathy's LLM knowledge base into a production agent:**](https://www.youtube.com/watch?v=6jOBSGSBQ3g) This tutorial shows developers how to build an automated knowledge base inspired by Andrej Karpathy’s approach to compiling and organizing personal notes. You’ll learn how to use Claude Code and Obsidian to build an agent that automatically turns raw web clippings into structured, interconnected atomic notes.

———————————————————————————

### **Top Tool**

[**PRFlow:**](https://prflow.graphbit.ai/) AI code reviewer that catches what others miss. Think of it as an automated teammate that reviews every pull request before it ever hits production. In tests across 10 real-world projects, PRFlow identified seven critical security vulnerabilities that other tools completely overlooked.

———————————————————————————

### **Top Repo**

[**Awesome Hermes Agent**](https://github.com/0xNyk/awesome-hermes-agent)** (2.8K **⭐**):** This repo is a curated toolkit for the Hermes Agent ecosystem, bringing together the best skills, plugins, and deployment templates. It provides the essential building blocks (from memory backends to multi-agent setups) to help you build and scale a professional Hermes-based agent stack.

———————————————————————————

### **Trending Paper**

[**Build iterative repair loops with Codex (by OpenAI):**](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex) Technical documentation often suffers from broken or outdated code examples. Implementing a closed-loop AI workflow that reviews, repairs, and validates the code solves this by improving the output using automated feedback.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 270K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/thinking-machines-unveils-tml-interaction-small-openai-ships-daybreak
