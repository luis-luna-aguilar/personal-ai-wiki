---
title: "🖥️  Cursor agents get their own computers"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-02-26
gmail_id: 19c9a0e33c779749
---

# 🖥️  Cursor agents get their own computers

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-02-26

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Coding agents have been writing PRs for a while now, but can you actually trust the code to work? Cursor thinks so — they just gave their agents their own computers. Now, these agents can click through UIs, debug in browsers, and ship PRs with video proof to show everything works. 

**Also:** How to set up AI agents that code 24/7, fix a critical AGENTS .md mistake flagged by a DeepMind engineer, and see how Stripe ships a thousand PRs every week. 


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Karpathy asks engineering teams to focus on CLIs

* How to stop AI agents from writing useless tests

* Trending social posts, top repos, and more

———————————————————————————

**Welcome to The Code.** This is a 4x weekly email that cuts through the noise to help devs, engineers, and technical leaders find high-signal news, releases, and resources in 5 minutes or less. You can sign up or share this email [here](https://superhumancode.beehiiv.com/subscribe).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/61e2c18f-588c-4f36-aacd-a857d0e89ae2/Untitled_design__8_.jpg?t=1772087654)
Follow image link: (https://www.youtube.com/watch?v=6Nru5OQq9O4)
Caption: Click here to watch Cursor cloud agents in action.


--------------------
**Cursor gives agents their own computers:** The AI code editor's cloud agents now run in isolated [**virtual machines**](https://cursor.com/blog/agent-computer-use) where they can click through UIs, debug in browsers, and host servers on their own. Every agent delivers merge ready PRs complete with video demos, screenshots, and logs for a smooth review process. CEO Michael Truell [shared](https://x.com/mntruell/status/2026736314272591924) that over a third of Cursor's merged PRs now come from these cloud agents, predicting developers will soon manage entire fleets of AI teammates for major projects.

**Anthropic now lets you code from your phone:** The AI lab shipped [**Remote Control**](https://x.com/claudeai/status/2026418433911603668) for Claude Code, which lets developers start a session in their terminal and pick it up from a phone, tablet, or any browser. Claude keeps running locally on your machine the whole time, so your filesystem, MCP servers, and project config are always available. It’s perfect for reviewing diffs on the go, approving PRs from the couch, or keeping a task moving between meetings. 

**Vercel open sources Chat SDK for cross-platform bots:** The frontend cloud platform just dropped [**Chat SDK**](https://vercel.com/changelog/chat-sdk), a unified TypeScript library that lets devs write bot logic once and ship it across Slack, Microsoft Teams, Discord, Google Chat, and more. This open source toolkit comes with JSX-based UI cards, real time AI streaming, and built in state management with Redis. It’s a huge time saver for engineering teams who are tired of dealing with separate codebases for different chat platforms. 


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY DELVE**

## [Migrate to Delve and get a $2,000 VISA card in your inbox](https://delve.co/book-demo?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-primary-feb26-26)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a750ef99-1e81-4e47-87e1-6d25ef90c404/delve_100kb_-_Zahabiyah_Badri__1_.jpg?t=1772035740)
Follow image link: (https://delve.co/book-demo?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-primary-feb26-26)
Caption: 


--------------------
Delve is the [AI-native compliance platform](https://delve.co/book-demo?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-primary-feb26-26) that actually does the work for you, auto-collecting evidence from AWS, GitHub, and your stack so you’re not chasing screenshots or babysitting integrations. Use AI security questionnaires and an AI copilot to make compliance less dreadful.

The proof is in the pudding:

* **Bland** unlocked $500k ARR in 7 days. 

* **11x** streamlined audits and moved faster on enterprise deals. 

* **micro1** scaled compliance without adding headcount.

Free migration. Zero disruption. No starting over.

[Book a demo, trigger your migration](https://delve.co/book-demo?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-primary-feb26-26), and get $2,000 when you’re onboarded.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Karpathy asks engineering teams to focus on CLIs**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b17d67ef-78f1-41f1-b424-7cded3123c6a/superhumanteam_a_software_engineering_team_working_on_a_massi_25305647-f587-4fd0-9c69-ad0dd86117cb_2.jpg?t=1772087602)
Caption: Source: The Code, Superhuman


--------------------
**It started with a single CLI release.** Polymarket (a predictions market company) just [shipped](https://x.com/SuhailKakar/status/2026305257257775524) a Rust-based CLI that gives AI agents a direct line to prediction markets. It lets them trade and pull data straight from the terminal without a browser.

**Andrej Karpathy turned it into a manifesto.** In a viral post, he [**argued**](https://x.com/karpathy/status/2026360908398862478) CLIs are the perfect setup for agents since they already speak the language of stdin, stdout, and JSON. To show how it's done, he had Claude install Polymarket’s CLI and pull up a live prediction market dashboard in under three minutes.

**It's riding in the same boat as MCP.** With 97 million monthly downloads and backing from OpenAI and Google, MCP became the industry standard and [moved](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) to the Linux Foundation by late 2025. Without a CLI, MCP server, or machine readable docs, your software is invisible to agents.

**But some people aren't ready to get on board.** OpenCode engineer Rhys Sullivan [**thinks**](https://x.com/RhysSullivan/status/2026406072274337943) CLIs are a dead end because they're hard to find and aren't secure enough. Sullivan’s bet is REST APIs that register clients on the fly. But no matter which side wins, software is splitting in two: the old path through websites and logins, and a new one where agents find and use tools on their own.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3604b50b-3a71-453c-8ff9-98d76c1893b3/CleanShot_2026-02-26_at_17.45.39_2x.jpg?t=1772108196)
Caption: Meme of the day.


--------------------
* **Ghost Team:** This developer's git history looks like he hired an entire engineering team. It's just him and a fleet of **[AI agents](https://x.com/d4m1n/status/2026032801322356903)** (4.4M views).

* **Bad Instructions: **A Google DeepMind developer found that a bad AGENTS .md file actively hurts your AI agent's performance. [Here's](https://x.com/_philschmid/status/2026354033418547444) what to fix.

* **Autopilot Mode:** This open source setup lets you run [**AI coding agents**](https://x.com/d4m1n/status/2026032801322356903) for hours without touching them. The dev behind it completed 250 tasks in a single session.

* **Spec and Ship:** An Anthropic engineer's workflow for [**shipping**](https://x.com/rvivek/status/2026385957596111044) full features without writing a single line of code is going viral (1M views).

* **PR Factory:** Stripe's AI agents now ship over a thousand PRs per week. An OpenAI developer [**broke down**](https://x.com/charlierguo/status/2026009225663750512) the emerging playbook behind it.

———————————————————————————

* **Alibaba drops **[**Qwen 3.5**](https://x.com/Alibaba_Qwen/status/2026339351530188939) with smaller models that outperform their larger predecessors.

* **Perplexity unveils **[**Computer**](https://www.perplexity.ai/hub/blog/introducing-perplexity-computer)**,** a digital worker that orchestrates top AI models.

* **Notion ships **[**Custom Agents**](https://www.notion.com/blog/introducing-custom-agents) that run autonomously on a schedule across your tools.

* **MiniMax launches **[**MaxClaw**](https://x.com/MiniMaxAgent/status/2026493668417482923)**,** a free 24/7 AI agent across major messaging apps.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to stop AI agents from writing useless tests**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/befb8d69-f0d0-4cde-9928-193ec88e58d3/superhumanteam_A_lone_software_engineer_sitting_at_a_desk_typ_8f387375-d051-4cc2-8e9f-91ee4b4d1ee8_0.jpg?t=1772043119)
Follow image link: (https://x.com/mattpocockuk/status/2023712176729715184)
Caption: 


--------------------
If you've ever used Claude Code or Cursor to write tests for a TypeScript project, you’ve probably run into a ton of redundant assertions. They often check for things the type system already handles, making these tests essentially dead weight. Matt Pocock, an ex-Vercel engineer, [**shared**](https://x.com/mattpocockuk/status/2023712176729715184) a simple fix for this.

Just add this to your CLAUDE .md (or .cursorrules for Cursor):

```
Never write tests that verify what the TypeScript type system already guarantees.
```
Both tools will pick up the change during your next session. Pocock also put together a full [TDD skill](https://www.aihero.dev/skill-test-driven-development-claude-code) for Claude Code if you want to dive deeper into getting agents to write meaningful tests. 


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/51cc41b7-fe2f-41be-82ad-12c5aa786a38/Untitled_design__9_.jpg?t=1772095603)
Follow image link: (https://www.youtube.com/watch?v=Ae0W5M6We84)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to build custom dev tools with agent teams:**](https://www.youtube.com/watch?v=Ae0W5M6We84) You'll learn to build custom software with a team of AI agents. This tutorial walks you through building a complete project from just a single spec file, using autonomous agents to handle all the coding, testing, and debugging for you.

———————————————————————————

### **Top Repo**

[**memU:**](https://github.com/NevaMind-AI/memU) A memory framework that gives AI agents persistent, structured memory so they can run 24/7 without wasting tokens on old context. It automatically extracts preferences and patterns from background conversations, feeding that context back to the agent instantly. 

———————————————————————————

### **Trending Paper**

[**ActionEngine (by Microsoft Research):**](https://arxiv.org/abs/2602.20502)** **Traditional AI web agents are often slow and pricey because they have to analyze screens step by step. ActionEngine changes that by mapping websites offline first, letting the AI generate a single, reliable script that gets the job done faster and for less money. 


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

### **Whenever you’re ready to take the next step**

* **[10 Projects to Master AI Agents](https://learn-ai-tiles.lovable.app/)**

* [100 Pro-Hacks for using Claude Code in 2026](https://claude-code-hacks.lovable.app/)

* **[Top Resources to learn Claude Code in 2026](https://claude-code-spotlight.lovable.app/)**

* **[Zero to Production Guide for Building AI Agents](https://ai-guidebook-nexus.lovable.app/)**

* **[200+ Resources to Become a Great Engineering Leader in 2026](https://thecode-200-resources.lovable.app/?utm_source=codenewsletter.ai&utm_medium=newsletter&utm_campaign=your-200-engineering-resources-ultimate-claude-code-guide)**

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/cursor-gives-its-agents-their-own-computers-vercel-open-sources-chat-sdk
