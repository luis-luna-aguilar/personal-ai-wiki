---
title: "🖥️  AI agents control desktop apps"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-03-02
gmail_id: 19caedf9cbe26942
---

# 🖥️  AI agents control desktop apps

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-03-02

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** AI agents can reason, plan, and code, but getting them to work reliably with your local desktop apps is challenging. Vercel just changed that with a new release — and all it takes is one line of code to set up.

**Also:** How one lawyer used Claude skills to outperform 100+ law firms, what Altman revealed in his Pentagon AMA, and the agent mistakes Anthropic doesn't want you to repeat.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Today's dev workflow has a shrinking shelf life

* How to run code migrations on autopilot

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2432d656-da67-4950-97f0-c91b9fe3739b/Untitled_design.jpg?t=1772438062)
Follow image link: (https://x.com/ctatedev/status/2028128730132922760)
Caption: Click here to see Vercel's Electron skill in action.


--------------------
**Vercel gives AI agents control of desktop apps:** The developer platform just dropped a new [**Electron skill**](https://x.com/ctatedev/status/2028128730132922760) for its agent-browser tool, giving AI agents the ability to click, type, and pull data from desktop apps like Discord, Figma, Notion, Spotify, and VS Code. Developers can set it up with a single command (npx skills add vercel-labs/agent-browser --skill electron) through the Chrome DevTools Protocol, essentially turning any Electron app into an API. It's an easy way to automate testing, debugging, and repetitive workflows.

**White House blacklists Anthropic over military safety dispute:** After Anthropic refused to lift Claude's safety guardrails for military use, the Trump administration [labeled](https://x.com/i/trending/2027317523411292589) the company a "supply chain risk" and ordered all federal agencies to stop using the model. The Pentagon is now severing its $200 million contract and requiring contractors to certify that they aren't using Claude. In response, the department has already [**pivoted**](https://x.com/sama/status/2027578652477821175) to OpenAI with the offer, even though the ChatGPT maker maintains similar safety standards.

**Cursor's code review agent now fixes bugs automatically:** The AI code editor just upgraded its code review agent, [**Bugbot**](https://cursor.com/blog/bugbot-autofix), which can now automatically fix bugs found in PRs. The new Autofix feature launches cloud agents in virtual machines to test code and suggest patches. More than 35% of these proposed fixes are getting merged, and the tool's bug resolution rate has climbed from 52% to 76%. It's now live for all users.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY DELVE**

## [Migrate to Delve and get a $2,000 VISA card in your inbox](https://delve.co/book-demo?utm_source=thecode&utm_medium=newsletter&utm_campaign=thecode-primary-feb26-26)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7818b592-d16e-4b8e-a763-bd98ae0dcdf9/delve_100kb_-_Zahabiyah_Badri__1_.jpg?t=1772438337)
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

## **Today's dev workflow has a shrinking shelf life**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6f590bdd-8057-4224-bd8e-67ea1e3687cf/superhumanteam_a_software_engineering_team_working_on_code_in_7433557a-ab3d-4d08-8556-87efe7b1a476_0.jpg?t=1772440248)
Caption: Source: The Code, Superhuman


--------------------
**New workflows are arriving faster than teams can keep up.** Cursor CEO Michael Truell recently [laid out](https://x.com/mntruell/status/2026736314272591924) the three stages of AI coding: Tab autocomplete, synchronous agents, and now autonomous cloud agents that work on their own VMs and submit fully tested pull requests. Tab autocomplete stayed the standard for almost two years, but synchronous agents might not even last for one. 

**The new New Thing.** In March 2025, Cursor had two and a half times more Tab users than agent users. That ratio has completely [flipped](https://x.com/ericzakariasson/status/2026743220529672602) since then, with agents’ usage growing 15x in just a year. Today, 35% of the pull requests Cursor merges internally come from autonomous cloud agents that produce artifacts, resolve merge conflicts, and ship everything on their own. 

**Mo workflows, mo problems.** If you’re feeling overwhelmed with all these new tips and tricks and endless new ways of doing things, you’re not alone. A simple solution: Andrej Karpathy [recommends](https://x.com/karpathy/status/2027501331125239822) an 80/20 split, where you spend most of your time in whatever workflow is working for you right now, while setting aside a consistent chunk to explore the next phase, even if it feels a bit unpolished. The goal is to build teams that see their current process as a work in progress, not the end result.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/8da825d4-a24e-433c-8b84-e6222ee391bb/CleanShot_2026-03-02_at_10.17.19_2x.jpg?t=1772426868)
Caption: Meme of the day.


--------------------
* **AI Law Firm:** One lawyer turned 10+ years of judgment into reusable Claude skills and is now [**competing**](https://x.com/zackbshapiro/status/2027389987444957625) with 100+ attorney firms (7M views).

* **Pentagon Pivot:** Days after Anthropic's Pentagon deal collapsed, OpenAI locked in the deal. Hours later, Sam Altman was [**live on X**](https://x.com/sama/status/2027900042720498089), taking questions (6.6M views).

* **Agent Autopsy:** Anthropic's Claude Code team [**broke down**](https://x.com/trq212/status/2027463795355095314) how they design agent tools, including the approaches that completely failed.

* **Ship Faster:** This thread [**lays out**](https://x.com/hartdrawss/status/2026198305362083910) 18 rules for shipping MVPs, from the tools that save you weeks to the decisions that bury you in tech debt.

* **Bypass Mode:** A bootstrapped founder [**says**](https://x.com/levelsio/status/2027566773814403448) he's outrunning his own todo list for the first time, running Claude Code in bypass mode across 8 products in one week.

* **X-Ray Vision:** AI enthusiasts created a tool that [**turns Wi-Fi signals into radar**](https://x.com/linusekenstam/status/2027960808592834824?utm_source=superhuman&utm_medium=newsletter&utm_campaign=how-should-the-military-use-ai) — letting regular routers see through walls.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to run code migrations on autopilot**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/de2b99e8-da09-49cc-bcbb-c52832cdfd4b/CleanShot_2026-03-02_at_10.14.37_2x.jpg?t=1772426710)
Follow image link: (https://x.com/bcherny/status/2027534984534544489)
Caption: Source: X/bcherny


--------------------
Code migrations are inherently tedious. Even though the same patterns repeat across every file, you're usually stuck handling them manually, which is why those tickets often sit in the backlog for months.

The latest Claude Code update addresses this with two new commands, which creator Boris Cherny [shared](https://x.com/bcherny/status/2027534984534544489) last week. 

"/batch" condenses a migration into a single line. It launches dozens of parallel agents (each in its own git worktree) to run tests and open a PR once finished.

```
/batch migrate from jest to vite
```
“/simplify” reviews your recent changes using three parallel agents focused on code reuse, quality, and efficiency. It then aggregates the findings and auto-fixes any issues it detects.

```
hey claude make this code change then run /simplify
```
Both commands work right out of the box. You can even chain them together, letting /batch handle the migration while /simplify cleans up the output in one go.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6f4f86e0-8cdb-4486-8796-cbe76c9b9306/CleanShot_2026-03-02_at_14.14.10_2x.jpg?t=1772441083)
Follow image link: (https://strategizeyourcareer.com/p/the-10-step-guide-to-building-your-own-ai-agent)
Caption: One engineer's fully automated coding workflow.


--------------------
### **Top Tutorial**

[**How to build coding agents (by an Amazon engineer):**](https://strategizeyourcareer.com/p/the-10-step-guide-to-building-your-own-ai-agent) A 10 step guide for building AI agents that can independently manage tickets, write code, and handle reviews. This tutorial shows devs how to move past manual prompting by using MCP servers, reusable skills, and SOPs to create specialized agents that work around the clock.

———————————————————————————

### **Top Repo**

[**Awesome OpenClaw use-cases:**](https://github.com/hesamsheikh/awesome-openclaw-usecases) A collection of 34 real world OpenClaw use cases, covering everything from automated code reviews to Jira workflow management. It's a great resource for devs looking to get some actual value out of AI coding agents.

———————————————————————————

### **Trending Paper**

[**Codified Context**](https://arxiv.org/abs/2602.20478)[**:**](https://arxiv.org/abs/2602.20478)** **AI coding tools struggle with large codebases because they often lose context between sessions. By structuring project knowledge into a three-part memory system (always-loaded rules, specialist agents, and on-demand docs) you can help agents retain context and write more reliable code.


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
https://codenewsletter.ai/p/vercel-lets-ai-control-desktop-apps-cursor-s-agent-fixes-bugs-automatically
