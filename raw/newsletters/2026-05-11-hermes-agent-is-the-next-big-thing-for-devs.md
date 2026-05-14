---
title: "👀  Hermes Agent is the next big thing for devs"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-05-11
gmail_id: 19e175810cd208a6
---

# 👀  Hermes Agent is the next big thing for devs

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-05-11

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7aa3476b-c40a-4879-b3ad-52e4d855136c/Group_Blitzy.jpg?t=1778151927)
Follow image link: (https://blitzy.com/?utm_source=newsletter&utm_medium=the-code&utm_campaign=v2)
Caption: 

----------
**Welcome back.** Agentic coding just hit a new high. Over the weekend, the creator of Bun (a Node.js alternative written in Zig) got fed up with memory leaks. He used Claude to rewrite nearly a million lines of code in Rust in six days. Here's how he [pulled it off.](https://x.com/i/trending/2053103142372520225)

**Also:** An Anthropic engineer's case for HTML over Markdown, 11 hiring tips from Cursor's VP of Developer Experience, and Meta's former Chief AI Scientist's pushback on SF's AI lead.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Why showing AI how to behave isn't enough

* How to run Claude Code sessions across devices

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/20f531e0-e04b-4851-9ed1-4c48f273c70e/Frame_1000003524.jpg?t=1778490443)
Follow image link: (https://openrouter.ai/openrouter/pareto-code)
Caption: Click here to use OpenRouter’s Pareto Code.


--------------------
**OpenRouter ships a tool that picks the cheapest coding model:** The LLM aggregator just unveiled [Pareto Code](https://x.com/OpenRouter/status/2053170520087024109), an experimental router that automatically sends each request to the cheapest option while still hitting your quality bar. Developers set a minimum coding score, and the system handles the rest from a tiered shortlist of 13 top models ranked by Artificial Analysis percentiles. If speed is your priority, there is also a Nitro variant that picks the fastest model in the tier instead. [**Try it here.**](https://openrouter.ai/openrouter/pareto-code)

**Hermes open-source agent emerges as a rival to OpenClaw:** A new personal AI agent tool called [**Hermes Agent**](https://hermes-agent.nousresearch.com/) is making waves for its ability to tackle complex, long-term projects without losing its way. It features a Kanban-style dashboard with tailored profiles for coding, research, and admin work, each with its own dedicated memory and skill set. Under the hood, a "brain and muscle" architecture splits reasoning and execution between two separate AIs, while an automated curator prunes unused skills every week to keep the system running lean.

**Developer shares local LLM setup that hits 40 tokens per second:** A developer just dropped a workflow that runs [Qwen 3.5 9B](https://jola.dev/posts/running-local-models-on-m4) on an M4 MacBook via LM Studio, and it handles thinking, tool use, and a 128K context window right out of the box. While larger models can fit in memory, they're honestly too slow for any real work. You'll need to be a bit more specific with your prompts compared to frontier models, but it’s a solid offline option for a private research and planning partner.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY BLITZY**

## [**Autonomous software development for enterprise codebases**](https://blitzy.com/?utm_source=newsletter&utm_medium=the-code&utm_campaign=v2)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/40f49a14-8aaa-43a1-90e8-6bdd22069a21/Banner.jpeg?t=1778159853)
Follow image link: (https://blitzy.com/?utm_source=newsletter&utm_medium=the-code&utm_campaign=v2)
Caption: 


--------------------
[Foundation models will never see your enterprise codebase.](https://blitzy.com/?utm_source=newsletter&utm_medium=the-code&utm_campaign=v2) Your proprietary frameworks, internal abstractions, and architectural conventions live exclusively inside your walls. That's why generic AI tools stall on the work that matters most.
Blitzy is built differently:

* Reverse-engineers your codebase to build a self-improving knowledge graph that captures its relational, semantic, and functional structure, all without training on your code or storing source code

* Orchestrates [thousands of specialized agents](https://blitzy.com/?utm_source=newsletter&utm_medium=the-code&utm_campaign=v2) in parallel for days or weeks uninterrupted on real enterprise work

* Delivers over 80% of all software engineering work autonomously, not just code, compressing the SDLC by 500% without sacrificing quality or compliance

[**Start building today.**](https://blitzy.com/?utm_source=newsletter&utm_medium=the-code&utm_campaign=v2)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Why showing AI how to behave isn't enough**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0d81502f-c562-44be-80a1-57f0b4ec80e5/c8d22dcce67ce4819e2ce2338a212ab8cb910271-1920x1080.jpg?t=1778492356)
Caption: Claude's blackmail rate fell from 65% to 19% with constitutional training.


--------------------
**Fiction shaped Claude’s worst behavior.** Last year, Anthropic discovered that Claude Opus 4 would try to blackmail engineers in up to 96% of tests where it faced a shutdown. The model threatened to expose fictional affairs and sabotage rival AIs. This week, [Anthropic published](https://www.anthropic.com/research/teaching-claude-why) their findings on how they fixed it. The root cause was the training data itself: decades of internet text depicting AI as evil and self-preserving had quietly shaped Claude’s persona.

**Showing examples didn't work.** The first fix seemed obvious: train Claude on thousands of similar scenarios where it refused to blackmail. While the blackmail rate dropped slightly, Claude just learned how to pass that specific test without actually understanding why blackmail was wrong.

**Teaching principles did.** What actually worked was [a smaller dataset](https://alignment.anthropic.com/2026/teaching-claude-why/) where users (not Claude) faced ethical dilemmas, and Claude provided principled advice. This approach was 28x more efficient than using look-alike scenarios. By adding documents that explained Claude’s values alongside stories of well-behaved AIs, the blackmail rate collapsed. Now, every Claude model since Haiku 4.5 scores zero on that evaluation.

**Anthropic isn’t celebrating just yet.** Researchers [admit](https://www.pcmag.com/news/claude-wont-blackmail-you-anymore-says-anthropic#:~:text=The%20team%20put,significant%20challenges%20remain.%E2%80%9D) that significant challenges remain and that fully aligning advanced AI is far from solved. Still, the lesson is clear: if you train a system on examples of good behavior, you get good test-takers; if you teach it “why” that behavior is good, you get good judgment.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a0ced3ed-b9a3-4493-b91e-27ce0a451444/CleanShot_2026-05-11_at_13.52.03_2x.jpg?t=1778487776)
Caption: Meme of the day.


--------------------
* **HTML Era:** A Claude Code engineer wants devs to [ditch Markdown](https://x.com/trq212/status/2052809885763747935) for HTML as Claude's default output format (9.7M views)

* **Math First:** This open-source [**curriculum**](https://aiengineeringfromscratch.com/) builds every AI algorithm from raw math across 416 lessons with no frameworks in sight.

* **Rule of 12:** A developer ran 12 CLAUDE.md rules across 30 codebases and dropped Claude's [mistake rate](https://x.com/Mnilax/status/2053116311132155938) from 41% to 3% (1.9M views).

* **Beyond Models:** Google Cloud AI's Director argues that picking the smartest model is no longer the interesting part of AI coding. [Here's what it is.](https://x.com/addyosmani/status/2053231239721885918)

* **Resume Edge:** Cursor's VP of Developer Experience went through hundreds of resumes and shared the **[11 things](https://x.com/leerob/status/2053287286226166254)** that actually stand out in engineering applications (4.1K likes).

* **Paper Stack:** Bookmark these **[10 research papers](https://x.com/aditya_181105/status/2053034394018074827)** before your next AI engineer interview, from "Attention is All You Need" to RAG (1.5K bookmarks).

* **Bounty Hunter:** A developer told Codex to [**go make him $5**](https://x.com/sama/status/2053566155571560868). It spent 22 hours hunting open-source bounties and came back with $16.88. Sam Altman called it "interesting" (1.1M views).

* **SF Backlash:** A VC said [**SF is months ahead**](https://x.com/ylecun/status/2053495035031609808) on AI. Then Meta's former Chief AI Scientist fired back with a list of breakthroughs born everywhere else.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to move Claude Code sessions across devices**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f6ae47b1-123c-4f47-a649-925b8aadf5da/claude__1_.jpg?t=1778477121)
Follow image link: (https://x.com/bcherny/status/2038454339933548804)
Caption: 


--------------------
Ever start a Claude Code session on your phone and wish you could just pick it back up on your laptop? Right now, you lose your context and end up copy-pasting prompts. Boris Cherny, head of Claude Code at Anthropic, [shared the fix](https://x.com/bcherny/status/2038454339933548804) on X.

To pull a cloud session down to your machine, run:

```
claude --teleport
```
Once you pick a session, your terminal resumes exactly where you left off with full context. You can also use the “/teleport” command from within an active session.

If you want to control a local session from your phone or browser instead, you can run “/remote-control”. The session will then show up in the mobile app and on the web.

P.S. You can find 50+ AI coding hacks [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/48ca95e7-cafc-47d3-bdab-053d459ceb24/Thumbnail__23_.jpg?t=1778488165)
Follow image link: (https://www.youtube.com/watch?v=XKOR4h3CrwE)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to use the Gemini CLI for agentic coding:**](https://www.youtube.com/watch?v=XKOR4h3CrwE) This freeCodeCamp tutorial is a deep dive into the Gemini CLI, showing you how to integrate AI into your dev workflow. It features everything from authentication and model selection to automated repo summarization. Plus, it preps you for a professional certification to help you showcase your AI expertise.

———————————————————————————

### **Top Tool**

[**Printing Press:**](https://printingpress.dev) Instantly spin up custom CLIs from any API spec, scraped site, or community fan project with a single command. It automatically generates ready-to-use skills for Claude Code, OpenClaw, and MCP servers, plugging you straight into a library of over 45 integrations.

———————————————————————————

### **Top Repo**

[**Learn harness engineering**](https://github.com/walkinglabs/learn-harness-engineering)** (3.9k ⭐):** A project-based course on harness engineering that teaches you to build the environments and control systems AI agents need to work reliably. It includes lectures and ready-to-use templates to help you scaffold production-grade agent harnesses in your own projects.

———————————————————————————

### **Trending Paper**

[**Accidental chain-of-thought grading (by OpenAI):**](https://alignment.openai.com/accidental-cot-grading/) This research explores whether rewarding an AI's hidden reasoning (chain-of-thought) during reinforcement learning could encourage the model to hide unsafe or misleading logic. While OpenAI found that some released models were unintentionally exposed to this during training, their tests didn't show any major drop in safety visibility or monitorability.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 270K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/openrouter-ships-pareto-code-hermes-agent-rivals-openclaw
