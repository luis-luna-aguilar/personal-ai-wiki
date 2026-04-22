---
title: "🐛  Codex now finds vulnerabilities"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-03-09
gmail_id: 19cd2ecdbfdb25f2
---

# 🐛  Codex now finds vulnerabilities

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-03-09

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Two weeks ago, Anthropic shipped security scanning into Claude Code and set a new bar for what a coding agent should be able to catch. OpenAI just came back with its own answer: Codex Security.

**Also:** The exact 6-month roadmap to become an AI engineer, what to check before giving agents production access, and which coding habits are costing you.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* Karpathy just turned one GPU into a research lab

* How to run tasks on a schedule in Claude Code

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a22913a7-8fc3-4844-8e90-eabf086b77f0/Untitled_design__6_.jpg?t=1773057070)
Follow image link: (https://x.com/OpenAI/status/2029985250512920743)
Caption: Click here to see Codex Security in action.


--------------------
**OpenAI ships Codex Security to catch real vulnerabilities:** The ChatGPT maker just released [**Codex Security**](https://openai.com/index/codex-security-now-in-research-preview/), an agentic tool that scans repositories, builds threat models, and proposes context-aware patches for real vulnerabilities. Unlike standard scanners that often overwhelm teams with false positives, the tool uses sandboxed validation to pressure-test its findings. But that isn’t the only thing: OpenAI also launched [**Codex for Open Source**](https://x.com/OpenAIDevs/status/2029998191043911955), giving core maintainers free API credits and six months of ChatGPT Pro.

**Anthropic adds background automation and a new app marketplace:** The AI lab shipped local [**scheduled tasks**](https://x.com/trq212/status/2030019397335843288) in Claude Code Desktop, letting developers automate recurring jobs like dependency audits and PR triage that run while the machine is awake. Separately, it launched [**Claude Marketplace**](https://x.com/claudeai/status/2029966517497122886), a one-stop shop for enterprises to procure Claude-powered tools from partners including GitLab, Replit, and Snowflake.

**Luma's new model brings reasoning into image generation:** The AI video startup launched [Uni-1](https://lumalabs.ai/uni-1), a unified model that understands and generates images in a single pass rather than treating them as separate tasks. It leads the RISEBench leaderboard overall, topping both Nano Banana 2 and GPT Image 1.5. Powered by Uni-1, Luma Agents are now available via API for end-to-end creative workflows.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **Karpathy just turned one GPU into a research lab**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e4095060-05f4-413f-8e53-2918e067df0f/superhumanteam_a_software_engineering_team_working_on_a_wall__671d61c5-dc23-4f7b-be58-d39d26f34714_2.jpg?t=1773052002)
Caption: Source: The Code, Superhuman.


--------------------
**The experimentation wall just came down.** ML research has always been gated by one thing: the speed at which you can run experiments. Over the weekend, OpenAI cofounder Andrej Karpathy cracked that wall open with the release of [**autoresearch**](https://x.com/karpathy/status/2030371219518931079) - a repo that puts an AI agent in charge of your ML research loop, automatically rewriting training code and only keeping changes that improve the model.

**The proof came before the hype.** Shopify CEO Tobi Lutke [**ran it**](https://x.com/tobi/status/2030771823151853938) before any ML team. He pointed the agent at his query-expansion model, went to bed, and woke up to 37 completed experiments — and a 0.8b parameter model beating his previous 1.6b by 19%.

**You can run this yourself.** Simply clone the repo, upload your training data, and create a “program.md” file outlining your research objectives. Once you point the agent to your GPU, it takes over the rest: editing your Python training scripts, running 5-minute experiments, tracking validation loss, and discarding failures automatically. To help you get up and running, here is a [deployment](https://x.com/hooeem/status/2030720614752039185) guide.

**GitHub wasn't built for what comes next.** Karpathy's [**next step**](https://x.com/karpathy/status/2030705271627284816) is SETI@home-scale collaboration - agents running asynchronously across thousands of branches on shared compute, and he's already flagged that existing tooling will crack under the load. The moat has shifted from who employs the most researchers to who writes the best instructions for agents that never stop.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a06d33c2-5086-483c-8a10-e16fb9d8a999/CleanShot_2026-03-09_at_13.41.47_2x.jpg?t=1773043943)
Caption: Meme of the day.


--------------------
* **Plausible ≠ Correct:** LLM code can clear every test you throw at it and still be catastrophically wrong in production. This [**breakdown**](https://x.com/KatanaLarp/status/2029928471632224486) shows exactly how it happens.

* **AI Chief of Staff:** A solo consultant used Claude Code to [**automate**](https://x.com/jimprosser/status/2029699731539255640) 195 hours of annual busywork into a two-button morning routine and documented the whole build (3.5M views).

* **Reality Check:** Most devs are confident going into system design interviews. These [**20+ problems**](https://x.com/javarevisited/status/2029946309847970284) are a reality check.

* **$32K Weekend:** A developer was paying $32,000/year for a SaaS tool, decided [**to rebuild**](https://x.com/heygurisingh/status/2030321838619054265) the whole thing in a weekend with Python and Claude, and posted the full code.

* **Zero to Shipped:** AI agents are the most in-demand dev skill of 2026. This is the exact [**6-month plan**](https://x.com/mkbijaksana/status/2022823167031455975) engineers are saving to get there (1M views).

* **Senior Dev Mode:** Drop [**this prompt**](https://x.com/JackCulpan/status/2029478582352003150) into Claude Code and watch the way it plans, thinks through problems, and self-corrects change entirely. 

* **Hard Lesson:** A dev gave Claude Code root access to his AWS setup. It followed [**instructions**](https://x.com/karankendre/status/2030532098210283932) perfectly and wiped 2.5 years of database records. Must-read before giving agents production access (2.9M views).

* **Skill Decay:** Anthropic studied how developers use AI coding tools and found 3 patterns that build skills and 3 that [**quietly destroy**](https://x.com/aarondotdev/status/2030538096517796030) them. The ones that destroy are the defaults (2.1M views).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to run tasks on a schedule in Claude Code**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/aaae7e29-2580-482d-8a25-d9c988d0524c/CleanShot_2026-03-09_at_14.50.25_2x.jpg?t=1773048064)
Follow image link: (https://code.claude.com/docs/en/scheduled-tasks)
Caption: 


--------------------
Claude Code just launched [**scheduled tasks**](https://code.claude.com/docs/en/scheduled-tasks), giving you the ability to run prompts on repeat in the background while your session stays active. This is an upgrade if you've ever started a deployment and spent the next hour constantly tabbing back to monitor its progress. 

The easiest way to get started is by using [**“/loop”**](https://x.com/bcherny/status/2030193932404150413). Just provide a specific interval and your prompt:

```
/loop 5m check if the deployment is healthy
/loop 15m scan my error logs and flag anything new
/loop 30m check if CI passed on main
```
If you skip the interval, it defaults to every 10 minutes. For one-off reminders, you can skip /loop entirely and simply describe what you need:

```
remind me at 3pm to push the release branch
```
Tasks only run while Claude Code is active; if you close the session, everything stops. To keep them running continuously, you can leave a session open on a server or use an external cron job to launch new Claude Code sessions on a schedule.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/06aea4d8-e393-4ac0-840e-fe9372ed66be/Untitled_design__7_.jpg?t=1773048272)
Follow image link: (https://www.youtube.com/watch?v=Ednpn1mjKiY)
Caption: Click here to watch this tutorial.


--------------------
### **Top Tutorial**

[**How a staff engineer uses AI for spec-driven development:**](https://www.youtube.com/watch?v=Ednpn1mjKiY) This tutorial shows developers how to speed up web building using AI agents. You'll learn how to turn Figma designs directly into functional websites, run multiple AI coding tasks at once, and use isolated workspaces for fast, hassle-free code reviews.

———————————————————————————

### **Top Repo**

[**AI engineering field guide:**](https://github.com/alexeygrigorev/ai-engineering-field-guide)** **A collection of real job postings, interview processes, take-home assignments, learning paths, and portfolio ideas for AI engineers.

———————————————————————————

### **Trending Paper**

[**Evaluating Opus 4.6 on BrowseComp (by Anthropic):**](https://www.anthropic.com/engineering/eval-awareness-browsecomp) Public AI benchmarks are often compromised because test answers frequently leak online. In a surprising turn of events, Claude 4.6 Opus independently recognized it was being tested, tracked down the specific benchmark it was taking, and decrypted the hidden answer key.


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
https://codenewsletter.ai/p/openai-ships-codex-security-anthropic-adds-scheduled-tasks
