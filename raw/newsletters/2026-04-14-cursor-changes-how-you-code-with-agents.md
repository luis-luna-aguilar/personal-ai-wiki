---
title: "👀  Cursor changes how you code with agents"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-04-14
gmail_id: 19d8c4be99d5308a
---

# 👀  Cursor changes how you code with agents

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-04-14

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** AI agents keep getting smarter, but running multiple tasks at once still feels clunky. Cursor just dropped an update that changes how you manage them.

**Also:** How a senior engineer built a coding harness in 60 lines, a DeepMind engineer's 8 tips for better agent skills, and what Google expects from Product Managers in 2026.

**P.S.** We’ve grown to over 230K CTOs, engineering leaders, and developers, and we’re just getting started. We’d love to know how we can bring even more value to your career. Drop us a note in the poll at the end of this issue.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Why long-running AI agents keep failing

* How to fix Claude Code's unstable behavior

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/bf47ef51-9ef6-432f-aa09-adf9190b8aa2/Untitled_design__47_.jpg?t=1776158807)
Follow image link: (https://x.com/cursor_ai/status/2043798784367546707)
Caption: Click here to see Cursor 3.1 in action.


--------------------
**Cursor now lets you manage a fleet of coding agents at once:** The AI coding startup just shipped [**Cursor 3.1**](https://cursor.com/changelog/3-1), adding a tiled Agents Window for running multiple AI agents in draggable panes. This lets you compare outputs side by side without tab switching and saves your layout for next time. The update also brings batch speech-to-text, branch selection for cloud agents, and improved file search filters. [Watch all updates.](https://x.com/cursor_ai/status/2043798784367546707)

**Vercel open-sources a platform for cloud coding agents:** The frontend cloud platform just unveiled [**Open Agents**](https://x.com/rauchg/status/2043869656931529034), a template for deploying coding agents that run indefinitely in the cloud. Built with their AI SDK and Sandbox tools, it allows teams to run hundreds of agents at once with zero timeouts or setup hassle. [**Try it here.**](https://vercel.com/templates/template/open-agents)

**Meta is reportedly working on an AI clone of its CEO:** The social media giant is developing an AI version of [**Mark Zuckerberg**](https://sg.news.yahoo.com/meta-reportedly-building-ai-clone-130242070.html), training it on his specific mannerisms, tone, and public statements, according to the Financial Times. The AI is also being briefed on his strategic vision so it can step in and advise Meta employees when he's not around.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY WISPR**

## [The code writes itself. Everything around it doesn't.](https://ref.wisprflow.ai/thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/96efdb23-7d9e-4a5d-9f77-5d91bf174276/Newsletters_Image_1920x1080__7_.png?t=1776084659)
Follow image link: (https://ref.wisprflow.ai/thecode)
Caption: 


--------------------
You spend hours on things that aren't code. PR descriptions. Slack threads explaining why you made that architecture call. Linear tickets with enough context so your teammate doesn't ping you at 11pm. Docs you keep pushing to next sprint.

[Wispr Flow](https://ref.wisprflow.ai/thecode) handles all of it. Speak naturally, and it outputs clean text anywhere you type. Syntax-aware, so your variable names and file paths stay intact.

It won't write your code. But it'll clear out everything blocking you from writing it. [Works across Mac, Windows, iPhone, and Android.](https://ref.wisprflow.ai/thecode)

Teams at Vercel, Clay, and Rivian already use it daily.

[**Free to start**](https://ref.wisprflow.ai/thecode)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Why long-running AI agents keep failing**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/d00cad99-274d-4b28-ae42-40e3df59b879/superhumanteam_a_software_engineering_team_working_on_debuggi_571916e3-7034-4aee-811c-c6c2ff34488a_0.jpg?t=1776163816)
Caption: Source: The Code, Superhuman


--------------------
**The 45-minute cliff.** AI agents start strong but lose steam halfway through, declaring projects "finished" at 60% completion. Anthropic engineer Prithvi Rajasekaran [**identified**](https://www.anthropic.com/engineering/harness-design-long-running-apps) two main culprits: models lose focus as context windows fill, and they can't honestly critique their own work.

**Agents are terrible at grading themselves.** They routinely praise mediocre or even broken code as high-quality. This is especially bad for subjective tasks like frontend design, where automated tests don't exist. You can't easily tune a generator to be self-critical, so a different approach is needed.

**The fix.** Rajasekaran solved this with a planner, a generator, and a skeptical evaluator. The evaluator uses **[Playwright](https://playwright.dev/)** (a browser automation tool) to test the app like a real user. While a solo agent built a broken game for $9 in 20 minutes, this multi-agent harness produced a working game for $200 over 6 hours.

**The catch is maintenance.** Agent harnesses are built on assumptions about model limitations that quickly become obsolete. When upgrading from Opus 4.5 to 4.6, Anthropic found they could strip away entire structures that the newer model no longer needed. The real engineering challenge is figuring out which components to remove as models continue to improve.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/23bf9c5f-4870-41ad-8071-b9597111cb53/CleanShot_2026-04-14_at_15.04.11_2x.jpg?t=1776159414)
Caption: Meme of the day.


--------------------
* **Skill Check:** Most developers write agent skills that are too vague or too rigid. A Google DeepMind engineer [posted ](https://x.com/_philschmid/status/2043705157850951699)**[8 tips](https://x.com/_philschmid/status/2043705157850951699)** to fix both.

* **Total Recall:** Your AI agent forgets everything between sessions. This [guide](https://x.com/akshay_pachaar/status/2043745099792953508) builds an agent memory that actually learns.

* **Under the Hood:** A senior engineer built an **[AI coding harness](https://x.com/theo/status/2043611205856837680)** from scratch in 60 lines of Python, demystifying the "magic" behind coding agents.

* **The Philosopher:** Google DeepMind's **[newest hire](https://x.com/dioscuri/status/2043661976534950323)** isn't an engineer, a researcher, or a product lead. It's a Cambridge philosopher (1.1M views).

* **Before You Ship:** Vibe-coded apps keep shipping with exposed API keys. This [**pre-launch checklist**](https://x.com/Hartdrawss/status/2043351026053386727) covers every blind spot AI won't catch for you.

* **Holy War:** A leaked memo from OpenAI's CRO calls Claude "a religion" internally and lays out a **[five-point plan](https://www.theverge.com/ai-artificial-intelligence/911118/openai-memo-cro-ai-competition-anthropic)** to win the enterprise AI war.

* **Hard Truth:** An ex-Microsoft engineering lead says tech hiring isn't dead, but most developers are making [**three mistakes**](https://x.com/ujjwalscript/status/2043591033162965085) that kill their applications before a human even reads them.

* **New Rules:** If you're interviewing for a PM role at Google, the technical round is gone. What replaced it is a [**whole different test**](https://x.com/aakashgupta/status/2043416118581461388).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7ea1a4c8-fc19-4fef-ba2b-bcdb72f7d486/Untitled_design__48_.jpg?t=1776160983)
Follow image link: (https://www.youtube.com/watch?v=hoCWD1aI60Y)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

**[How to build and deploy an app with Codex:](https://www.youtube.com/watch?v=hoCWD1aI60Y)** You’ll learn how to build and launch a complete web app using Codex. At the same time, this tutorial also dives deeper into how to configure Codex plugins, generate code with plain English prompts, and fix bugs quickly.

———————————————————————————

### **Top Repo**

**[MarkItDown:](https://github.com/microsoft/markitdown)** This repo converts any messy file into clean, structured Markdown that is ready for your AI agents. It provides a simple way to feed PDFs, slides, documents, audio, and more directly into LLMs without having to struggle with parsers or lose critical context.

———————————————————————————

### **Trending Paper**

[Scaling coding agents via atomic skills:](https://arxiv.org/abs/2604.05013) AI coding agents struggle with new tasks when trained only on big-picture problems. By training them instead on basic "atomic skills" like editing, they significantly improve their ability to generalize and solve completely unseen coding challenges.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to fix Claude Code's unstable behavior**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5d6e2359-bd55-4b86-b3ce-126ef0c76458/CleanShot_2026-04-14_at_10.52.06_2x.jpg?t=1776144161)
Follow image link: (https://x.com/kunchenguid/status/2043511416448307378)
Caption: Source: X/kunchenguid


--------------------
Claude Code users have noticed a dip in quality recently. Issues like bloated context, override settings, and stale auto-memory are burning through tokens quickly. 

Kun Chen, a former L8 engineer at Meta and Microsoft, [shared](https://x.com/kunchenguid/status/2043511416448307378) a fix to lock these things down. Just add this config into “~/.claude/settings.json”:

```
{
  "effortLevel": "high",
  "env": {
    "CLAUDE_CODE_DISABLE_1M_CONTEXT": "1",
    "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING": "1",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    "CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"
  }
}
```
These flags optimize your setup by keeping it lean, locking your effort level, and giving you manual control over CLAUDE.md. Switching the subagent to Sonnet also boosts reliability. Just save your changes and restart Claude Code.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 230K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/cursor-drops-v3-1-vercel-open-sources-a-platform-for-cloud-coding-agents
