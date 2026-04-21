---
title: "👀  Strange things happening in AI"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-04-07
gmail_id: 19d6840435c372d4
---

# 👀  Strange things happening in AI

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-04-07

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** The number of strange things happening in AI is ridiculous. Yesterday, someone built an actual Indiana Jones-style [whip](https://x.com/blended_jpeg/status/2041108141266653325) for Claude Code (github repo [here](https://github.com/GitFrog1111/badclaude)). And today, Milla Jovovich — yes, actress from the Resident Evil movies — announced that she has built an agentic memory tool that scored 100% on LongMemEval (see [video](https://x.com/bensig/status/2041229266432733356)). Wild times.

**Also:** How to make RAG 32x more memory efficient, building self-improving LLM knowledge bases, and a look at how OpenAI’s Codex team actually ships.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Why Claude Code's real edge was never the model

* How to feed Claude Code skills real-time data

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/33aedce4-80ba-41c3-8364-93a160ef6c10/superhumanteam_Create_an_potrait_of_the_person_--ar_169_--sre_9f5e4055-19d5-4dc9-8b4c-c3f705e36def_1.jpg?t=1775559828)
Caption: Made with Midjourney.


--------------------
**OpenAI, Anthropic, and Google team up to fight model copying:** These three AI rivals are [**teaming up**](https://www.businesstimes.com.sg/international/global/openai-anthropic-google-unite-combat-model-copying-china) through the Frontier Model Forum to combat “adversarial distillation”, a process where unauthorized users harvest responses from US models to build cheaper knockoffs. OpenAI has accused DeepSeek of piggybacking on its tech, while Anthropic has already cut off access for Chinese-controlled firms after catching three labs doing just that. US officials estimate this practice drains billions of dollars from Silicon Valley labs every year.

**Anthropic secures massive compute expansion with Google and Broadcom:** The AI lab recently [**landed**](https://www.anthropic.com/news/google-broadcom-partnership-compute) a multi-gigawatt deal for next-gen TPU capacity, set to go live in 2027. This marks the company’s largest compute commitment to date, fueled by explosive growth: run-rate revenue has tripled since late 2025 to $30B, while the number of enterprise customers spending over $1M annually has doubled to more than 1,000 in just two months.

**Meta plans open-source versions of its next frontier models:** The social media giant is working on open-source versions of its next two [**proprietary models**](https://siliconangle.com/2026/04/06/report-meta-developing-open-source-versions-upcoming-ai-models/), codenamed Avocado (an LLM) and Mango (an image and video generator). While Bloomberg reported last December that the company was pivoting to a fully closed-source approach, those plans have changed. These open-source editions will likely be lighter versions with fewer features or parameters, partly due to AI safety concerns. There's no word yet on a release date.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [Cursor for code. Claude for thinking. What about input?](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ac7f2e9a-99a7-49b1-94f8-8a13a058e859/Newsletters_Image_1920x1080__5_.png?t=1775494389)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
Your dev stack got an AI upgrade everywhere except the input layer. You're still typing every prompt, every ticket, every review comment by hand.

[Wispr Flow](https://ref.wisprflow.ai/thecode) closes that gap. Dictate into Cursor, VS Code, Slack, Linear, or anywhere else you work. It's syntax-aware: camelCase, snake_case, acronyms, and file names all come through clean. Mention a file in Cursor or Windsurf, and it auto-tags.

[It's the voice layer for an AI-native workflow](https://ref.wisprflow.ai/thecode). Speak your intent. Your tools do the rest.

Available on Mac, Windows, iPhone, and Android. Used by millions of developers, including teams at OpenAI and Mercury.

[**Try free**](https://ref.wisprflow.ai/thecode)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **The Claude Code leak proves harnesses are the next big thing — not models**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/99af0531-09c0-4cb0-b12d-e6010c8441ab/HEvpqRWbQAA6JKt.jpg?t=1775538340)
Follow image link: (https://x.com/rasbt/status/2038980345316413862)
Caption: Source: X/rasbt


--------------------
**The $2.5B code dump.** Last week, Anthropic accidentally leaked Claude Code's [**entire source code**](https://fortune.com/2026/03/31/anthropic-source-code-claude-code-data-leak-second-security-lapse-days-after-accidentally-revealing-mythos/) via an npm update, exposing half a million lines of TypeScript. But the leak revealed a bigger truth: the model isn't the secret sauce.

**Plumbing beats parameters.** ML researchers like Sebastian Raschka [**found**](https://x.com/rasbt/status/2038980345316413862) that Claude Code's performance comes from its engineering, not just the underlying model. It relies on smart features like file history tracking to save context, specialized navigation tools, and parallel agents for background tasks. You'd likely get similar results using DeepSeek or Kimi with the same setup.

**The wrapper is the new winner.** Others have already proven this. LangChain [**climbed**](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) to the top five on benchmarks just by improving its harness, while Vercel saw better results by simplifying its agent's tools. The real competition has shifted from model quality to the quality of the surrounding infrastructure.

**Blueprints aren't buildings.** While every competitor now has the map to a multi-billion dollar product, execution remains the hurdle. Knowing how the architecture works and actually scaling it for production are two completely different challenges.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/34c4ed6b-2a7c-4fda-844d-3081519db519/CleanShot_2026-04-07_at_13.14.51_2x.jpg?t=1775547922)
Caption: Meme of the day.


--------------------
* **Faster RAG:** How Perplexity, Azure, and HubSpot use a **[simple technique](https://x.com/_avichawla/status/2040326889928356122)** to make RAG 32x more memory efficient (explained with code).

* **External Brain:** Inspired by Andrej Karpathy, this thread **[walks you](https://x.com/hooeem/status/2041196025906418094)** through building your own LLM knowledge base that compounds over time.

* **Inside Codex:** OpenAI's Head of DevRel and Codex product lead go [**behind the scenes**](https://www.youtube.com/watch?v=9qXc-THAvc0) on how the team actually ships products.

* **Agent Anatomy:** When your AI agent fails, the problem is rarely the model. This [deep dive](https://x.com/akshay_pachaar/status/2041146899319971922) shows how to turn a stateless LLM into a production agent.

* **Leaked Playbook:** Claude Code's source code was accidentally leaked, and here's a [**breakdown**](https://www.dbreunig.com/2026/04/04/how-claude-code-builds-a-system-prompt.html) of how it constructs system prompts

* **Docs as Files:** Most AI code fails when docs change. This tool turns live documentation into an accessible [filesystem](https://x.com/arlanr/status/2041215978957389908) that agents can browse.

* **Perfect Timing:** OpenAI announced a new Safety Fellowship, hours after a New Yorker investigation revealed it had [**dissolved**](https://x.com/RonanFarrow/status/2041224604878864514) its safety teams.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to feed Claude Code skills real-time data**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d50e9190-e66a-4921-b364-1169aec80c8e/CleanShot_2026-04-07_at_10.50.40_2x.jpg?t=1775539271)
Follow image link: (https://x.com/lydiahallie/status/2034337963820327017)
Caption: Souce: X/lydiahallie


--------------------
Claude Code skills are normally static, which usually means tedious manual copy-pasting for PR diffs or logs. Lydia Hallie, an engineer on the Claude Code team, recently [shared](https://x.com/lydiahallie/status/2034337963820327017) a much better way: use the `!` backtick syntax to embed shell commands directly into your `SKILL.md`. 

Claude Code will execute the commands and swap in the live output automatically before processing. To get started, create this file at `.claude/skills/pr-summary/SKILL.md`:

```
---
name: pr-summary
description: Summarize changes in a pull request
---

- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`

Summarize this pull request...
```
This syntax works with any shell command, allowing you to pull in test results, grep for TODOs, or fetch API responses automatically. To prevent accidental state changes, stick to read-only commands like `cat`, `grep`, and `gh pr view`.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/ffb42898-1219-4127-a81d-ceaa835e8021/Untitled_design__41_.jpg?t=1775556039)
Follow image link: (https://www.youtube.com/watch?v=pbAqx8B6NVc&t=876s)
Caption: Click here to watch this tutorial.


--------------------
### **Top Tutorial**

[**How to build your own AI agent from scratch:**](https://www.youtube.com/watch?v=pbAqx8B6NVc&t=876s) In this tutorial, you'll learn how to build a custom AI meeting assistant with the Mastra TypeScript framework. You'll see how to bridge core agent concepts like tools, memory, and event triggers by integrating Slack, Exa AI, and Cal.com into one seamless, automated workflow.

———————————————————————————

### **Top Repo**

[**Graphify:**](https://github.com/safishamsi/graphify) This AI coding agent skill turns any folder of code, docs, papers, or images into a queryable knowledge graph. It gives you a full system context so your agent can answer complex architecture questions with precision.

———————————————————————————

### **Trending Paper**

[**Cursor doubles AI coding speed on Blackwell GPUs:**](https://cursor.com/blog/warp-decode) Traditional MoE models waste processing time managing data around individual experts during single-token generation. By assigning computing power directly to outputs instead, warp decode skips these extra steps, making inference 1.8x faster and more accurate.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/openai-anthropic-google-fight-model-copying-meta-goes-open-source
