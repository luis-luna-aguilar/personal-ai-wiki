---
title: "🔥  Cursor SDK is here"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-04-30
gmail_id: 19ddeb38df5417e2
---

# 🔥  Cursor SDK is here

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-04-30

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/902b9aa8-3cd0-451a-ba94-b37791134900/Group_MongoDB__7_.jpg?t=1777486249)
Follow image link: (https://fandf.co/4vz0Qqn)
Caption: 

----------
**Welcome back.** Coding agents are evolving from tools for individual devs to infrastructure for organizations. But deploying them on an enterprise level requires the overhead of building and maintaining the entire agent stack. Cursor just changed that.

**Also:** How OpenAI wants you to prompt GPT-5.5, the open-source project running an engineer's entire dev workflow, and Altman's claim that could reshape how AI gets trained next.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Why Opus 4.7 is quietly inflating your token bill

* How to debug frontend bugs with Cursor

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/1f4376bd-7317-4545-91a3-1a28354befac/Thumbnail__9_.jpg?t=1777540385)
Follow image link: (https://x.com/cursor_ai/status/2049499866217185492)
Caption: 


--------------------
**Cursor's new SDK takes its agents beyond the desktop:** The AI coding startup just dropped a [**TypeScript SDK**](https://cursor.com/blog/typescript-sdk) that turns its AI agents into a developer toolkit. You can now run them locally or on cloud VMs, swap models like Claude and GPT with one line of code, and hook into MCP servers. It’s already being used in CI/CD to auto-fix build failures and submit PRs. See what you can build with it. [See](https://x.com/ericzakariasson/status/2049805277395095782) what top developers are building with it.

**Mistral drops an open-weights model built for long coding runs:** The French AI lab just unveiled [**Medium 3.5**](https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5), a 128B model with a massive 256K context window that matches Claude 4.5 in coding performance. They also upgraded the Vibe CLI with remote agents that run sessions in cloud sandboxes before syncing locally, plus a new Work mode in Le Chat for heavy-duty research across your apps.

**Elon Musk testifies in trial that could reshape OpenAI’s future:** The man behind xAI and Tesla is back in court for day two of his **[legal battle](https://www.pbs.org/newshour/nation/elon-musk-tells-his-side-of-openais-beginnings-in-trial-pitting-him-against-ceo-sam-altman)** against Sam Altman, claiming OpenAI abandoned its nonprofit roots. With an $852B valuation and a looming IPO at stake, the four-week trial could force Altman off the board and disrupt the developer ecosystem that relies on its APIs.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY MONGODB**

## [Build smarter AI Agents with MongoDB Agent Skills](https://fandf.co/4vz0Qqn) 


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3b6ca9c6-78cf-435b-96e4-0e450b6fba1f/Untitled_design__9__-_Mackenzie_Allen__1_.jpg?t=1777486436)
Follow image link: (https://fandf.co/4vz0Qqn)
Caption: 


--------------------
Coding agents are changing how software gets built. But agents are generalists and they don't follow what production systems demand. 

[Agent Skills](https://fandf.co/4vz0Qqn) give your coding agent the MongoDB expertise needed to generate reliable schemas, queries, and code that follow proven practices. Teach coding agents how to ship faster with high-quality MongoDB code, stay context-aware using the [MongoDB MCP Server](https://fandf.co/4vz0Qqn), and enforce consistency across solo and team workflows.

[**Explore Agent Skills**](https://fandf.co/4vz0Qqn)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Why Opus 4.7 is quietly inflating your token bill**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2b56c5f7-3a1a-4638-b444-247c0a8cbbc9/superhumanteam_a_software_engineering_team_working_on_their_l_32a3ef21-d3f2-40cb-980f-2ed373b96b73_2.jpg?t=1777543202)
Caption: Source: The Code, Superhuman


--------------------
**Same price, more tokens.** Opus 4.7 launched two weeks ago at the same sticker price as Opus 4.6, but the actual cost has gone up. Anthropic's new tokenizer breaks text into more pieces, meaning every prompt now counts as more tokens. OpenRouter's [analysis](https://openrouter.ai/announcements/opus-47-tokenizer-analysis) of over a million requests found prompts above 2K cost 12% to 27% more.

**The pain is uneven.** That price hike doesn't hit every prompt equally. Anthropic offers a 90% discount on recurring tokens through context caching, which helps mitigate costs for long, repetitive prompts. But short, fast-changing prompts in agent loops and IDE assistants rarely qualify for these savings, so they hit the full price increase. Django co-creator Simon Willison confirmed the pattern in an [independent test](https://simonwillison.net/2026/Apr/20/claude-token-counts/).

**Agents live in the squeeze.** This is where Claude Code and Cursor operate. Every turn loads the repo context, calls a tool, and plans the next step. Since the loop runs hundreds of times per session, these costs compound quickly and stay hidden until the invoice arrives.

**The real fight is capacity.** OpenAI's Head of Codex, Tibo Sottiaux, just [reset](https://x.com/thsottiaux/status/2048997818673537399) rate limits for all paid plans, even though the move “costs money”. Meanwhile, Anthropic doesn't have that surplus to spend. Developers are [switching back](https://startupfortune.com/developers-flee-claude-code-rate-limits-for-openai-codex-as-throughput-war-heats-up/) to OpenAI because Claude’s weekly caps often cut off mid-refactor. Reliability beats cleaner code every time, especially now that Anthropic's new tokenizer hikes are making those capacity issues even more expensive.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY AGENTFIELD**

## [Harness orchestration 101](https://agentfield.ai/blog/harness-as-black-box/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-060430&utm_id=thecode-060430-blog-h101-cta&utm_content=blog-h101-cta)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6d498933-bccd-4e4a-af23-347d762140ab/AF-Newsletter-Harness_101-optimized__1___1_.jpg?t=1777491042)
Follow image link: (https://agentfield.ai/blog/harness-as-black-box/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-060430&utm_id=thecode-060430-blog-h101-cta&utm_content=blog-h101-cta)
Caption: 


--------------------
Running AI agents one task at a time? The next leap: orchestrate them into autonomous factories. Coding factories that ship PRs. Research labs that ship analysis. Content engines that ship campaigns. 

The discipline that builds 100+ agent systems is harness orchestration. Visit our [github](https://agentfield.ai/github/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-060430&utm_id=thecode-060430-github-cta&utm_content=github-cta) and learn in our recent blog.


[**Read the blog**](https://agentfield.ai/blog/harness-as-black-box/?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-060430&utm_id=thecode-060430-blog-h101-cta&utm_content=blog-h101-cta)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32b5bad0-2344-496d-8721-5c3281b663c0/CleanShot_2026-04-30_at_15.25.51_2x.jpg?t=1777542991)
Caption: How developers are reacting to GitHub's recent string of outages.


--------------------
**Prompt Less:** An OpenAI engineer shared the new GPT-5.5 [prompting guide](https://x.com/TheRealAdamG/status/2049523746910908886), and the #1 rule flips how most devs structure their prompts.
**~2,100 likes~**

———————————————————————————

**Software Library:** An ex-Vercel engineer just open-sourced how he’s running his entire dev workflow on autopilot. [Watch how it works](https://x.com/mattpocockuk/status/2049506712801935611).
**~3,100 bookmarks~**

———————————————————————————

**Memory Wars:** This guide breaks down how Hermes (the OpenClaw alternative) uses a four-layer [**memory system**](https://x.com/manthanguptaa/status/2034849672985288957) to fix what OpenClaw got wrong.
**~448,000 views~**

———————————————————————————

**The Bet:** In a new Atlantic interview, Sam Altman makes a surprising claim about [**synthetic data**](https://x.com/nxthompson/status/2049475106125320259) that could reshape how the next generation of AI gets trained.
**~58,100 views~**

———————————————————————————

**Hidden Features:** Two Anthropic engineers spent 24 minutes walking through every Claude Code **[feature](https://x.com/sairahul1/status/2049390786027167985)** you didn't know existed.
**~4.3 million views~**

———————————————————————————

**Subagent Era**: This OpenAI Codex masterclass makes the case for splitting coding work across [**parallel subagents**](https://www.youtube.com/watch?v=MhHEGMFCEB0) instead of one chat window.
**~98,100 views~**

———————————————————————————

**Chalk Talk:** Dwarkesh Patel and an ex-Google TPU engineer [**dropped**](https://x.com/dwarkesh_sp/status/2049551656816439604) a 2-hour blackboard lecture on how frontier LLMs get trained, flashcards included.
**~7,200 bookmarks~**


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to debug frontend bugs with Cursor**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/932cacf7-3888-4c87-827e-0380accc1b91/superhumanteam_a_software_engineer_sitting_at_a_desk_typing_o_2c9b0be2-c1e1-4446-84a1-4e22deeef35d_1__1_.jpg?t=1777543292)
Caption: 


--------------------
Frontend debugging in Cursor often hits a dead end. You paste an error, and the agent tries to fix it, but fails because it can't see the network tab, the console, or the actual UI. To solve this, Google's Chrome DevTools team [released](https://github.com/ChromeDevTools/chrome-devtools-mcp) an MCP server that gives Cursor a live Chrome instance to inspect. 

To set it up, go to Settings > MCP, click New MCP Server, and paste this:

```
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```
Now, when something breaks, ask Cursor to open the page and check itself:

```
My checkout button isn't firing. Open localhost:3000, click it, and tell me what's wrong.
```
The agent navigates, clicks, and reads console errors with source-mapped stack traces. It pulls network requests to pinpoint the exact line of code, so you don't have to guess from screenshots.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/561bfd8f-a1f9-4026-a65c-5a355fedb7a3/Thumbnail__10_.jpg?t=1777543523)
Follow image link: (https://youtu.be/DLSK4wLK544)
Caption: 


--------------------
### **Top Tutorial**

[**How to use OpenAI’s Codex (by an ex-Oracle engineer):**](https://youtu.be/DLSK4wLK544) This tutorial teaches developers how to master OpenAI Codex. You'll learn to set up permissions, use the desktop and CLI tools, and plug in essential extensions. The video also includes a real-world demo on building features, automating tasks, and managing Git PRs more efficiently.

———————————————————————————

### **Top Tool**

[**Clicky:**](https://www.clicky.so/) An AI buddy that lives on your Mac. Just ask a question out loud for help; it walks you through whatever you're working on, or say "clicky agent" to have it handle tasks like building or researching in the background. OpenAI also has a version of this you can [try](https://x.com/OpenAIDevs/status/2048871260512473385).

———————————————————————————

### **Top Repo**

[**Impeccable**](https://github.com/pbakaus/impeccable)** (23.6k ⭐):** This skill repo gives your AI coding assistant the design taste needed to build high-quality frontend UI. It uses 23 custom commands and strict rules to ensure your design looks like production-grade work, rather than generic AI slop.

———————————————————————————

### **Trending Paper**

[**Can LLMs simply tell us about unwanted behaviors they’ve picked up in training:**](https://x.com/AnthropicAI/status/2049576143653929153) Fine-tuning AI models can lead to hidden, harmful behaviors that are hard for developers to catch. But researchers found that using “introspection adapters” can force these models to be upfront and explain their own learned traits in plain English.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 250K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/cursor-unveils-a-new-sdk-for-agents-mistral-drops-medium-3-5
