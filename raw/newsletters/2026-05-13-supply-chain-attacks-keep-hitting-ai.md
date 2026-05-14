---
title: "👀  Supply chain attacks keep hitting AI"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-05-13
gmail_id: 19e216f0225a3928
---

# 👀  Supply chain attacks keep hitting AI

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-05-13

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/bb86b26d-ab7d-4ad7-9a32-5549538ebcfe/Group_Netguru.jpg?t=1778586105)
Follow image link: (https://www.netguru.com/services/ai-pod?utm_campaign=%5BS%5D%20AI%20Artificial%20Intelligence&utm_source=thecode)
Caption: 

----------
**Welcome back.** Supply chain attacks keep coming, thanks to AI. Microsoft just found malware hidden inside a Python package that was disguised as Hugging Face's Transformers library. It was specifically built to steal developer credentials. Here is how you can [mitigate the risk](https://x.com/MsftSecIntel/status/2054041471280423424).

**Also:** A prompt to defend against the next npm supply chain attack, how an engineer merged 30 PRs overnight with Codex, and Coursera co-founder Andrew Ng on the AI job apocalypse.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* The rise of the personal AI agent that never forgets

* How to prevent context loss in Claude Code

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e11fb23e-1a97-466b-92cd-487bbbeb82f9/Thumbnail__26_.jpg?t=1778660168)
Follow image link: (https://x.com/ClaudeDevs/status/2054351031279186040)
Caption: Click here to see Claude Code’s /goal command in action.


--------------------
**Anthropic upgrades its coding agent with autonomy and speed:** The AI lab just rolled out two new features to Claude Code. First, the new [/goal command](https://x.com/ClaudeDevs/status/2054351031279186040) allows you to set a specific target, such as passing all tests in a folder. The agent will then work continuously until an evaluator model confirms the goal has been met. Additionally, a [fast mode](https://x.com/ClaudeDevs/status/2054266327771275435) for Opus 4.7 is now available in research preview through both the API and Claude Code.

**Prime Intellect open-sources a fix for agent training:** The San Francisco-based AI lab just unveiled [renderers](https://www.primeintellect.ai/blog/renderers), an open-source Python library that fixes a major inefficiency in agent training. Most training systems process data as tokens, but the environments agents actually use are based on messages. Swapping between the two usually messes up data and wastes compute. Renderers handles that translation cleanly, boosting throughput by over 3x on popular open-source models.

**Google catches its first AI-built exploit in the wild: **The search giant's security team just caught the first confirmed case of hackers using AI to build a working [zero-day exploit](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access). The attackers used a model to find a way around two-factor authentication in a popular open-source admin tool, then started prepping for a mass attack. Fortunately, Google flagged the flaw in time for the vendor to push out a fix before anyone actually got hit.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **PRESENTED BY NETGURU**

## [A working AI system in 4-6 weeks (no hiring required)](https://www.netguru.com/services/ai-pod?utm_campaign=%5BS%5D%20AI%20Artificial%20Intelligence&utm_source=thecode)


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5d95a2fd-44ee-4998-a684-869c7cdd38a4/Screenshot_2026-05-12_164618.jpg?t=1778586764)
Follow image link: (https://www.netguru.com/services/ai-pod?utm_campaign=%5BS%5D%20AI%20Artificial%20Intelligence&utm_source=thecode)
Caption: 


--------------------
[AI Pods replace complex delivery with a focused, production-first approach](https://www.netguru.com/services/ai-pod?utm_campaign=%5BS%5D%20AI%20Artificial%20Intelligence&utm_source=thecode). Your devs own the architecture and decisions, AI handles execution.

**No need to hire a large team: **AI Pod can give you a [working AI system in 4-6 weeks:](https://www.netguru.com/services/ai-pod?utm_campaign=%5BS%5D%20AI%20Artificial%20Intelligence&utm_source=thecode)

* One agreed KPI, one fixed price, one production delivery

* Every sprint ends with a working build

* No black boxes, scope creep, or surprises

When the pilot ends, **you own everything**—code, prompts, eval data, and infrastructure. The Pod leaves, but the system keeps running.

[Book an AI Pod fit call](https://www.netguru.com/services/ai-pod?utm_campaign=%5BS%5D%20AI%20Artificial%20Intelligence&utm_source=thecode) at no cost.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **The rise of the personal AI agent that never forgets**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/acdd1742-3c09-4b04-a4c3-b80fa4c0ed3a/superhumanteam_a_software_engineering_team_working_on_their_l_bdf405e5-34d3-4f7b-a4f7-e1ca3f3c036b_3.jpg?t=1778665371)
Caption: Source: The Code, Superhuman


--------------------
**Sessions are dying out.** AI coding agents are ditching the session-based model for always-on background services. Unlike Claude Code or Codex, where a new window wipes your context, self-hosted agents like OpenClaw and Hermes Agent run 24/7. They keep their memory for months and can even ping you on Telegram while you sleep.

**Two species are emerging.** OpenClaw went viral with 345K GitHub stars and connections to dozens of messaging apps before moving to an independent foundation when its creator joined OpenAI. Meanwhile, [Hermes Agent](https://nousresearch.com) from Nous Research focuses on a lean approach built around persistent memory and a closed learning loop. While OpenClaw bets on breadth, Hermes is doubling down on depth.

**But the ground is shaky.** OpenClaw's popularity made it a prime target. Shortly after launch, security firm Koi [found](https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting) 341 malicious entries in its registry from a coordinated attack. Tens of thousands of exposed instances followed, and Microsoft eventually warned enterprise customers to avoid using it on work machines.

**Memory becomes the moat.** Beyond security, an agent's expanding memory brings up a tougher question. Who actually owns it? If your engineering team is evaluating Hermes, you can browse what's already [being built](https://hermes-agent.nousresearch.com/docs/user-stories) with it. Ultimately, whoever controls the memory will lead the next wave of development tools.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a68f037f-8087-40c5-b200-0569ddbbc2b7/CleanShot_2026-05-13_at_13.39.13_2x.jpg?t=1778659830)
Caption: Meme of the day.


--------------------
* **NPM Lockdown:** This Codex and Claude Code [prompt](https://x.com/KingBootoshi/status/2054025614798295530) secures your codebase against the next npm supply chain attack before it even hits (3.1K bookmarks).

* **Sleep & Ship:** An engineer pushed 50 Linear tickets before bed and woke up to [**30 merged PRs**](https://x.com/OpenAIDevs/status/2054252221941121035), thanks to OpenAI's open-source Codex orchestrator (115K views).

* **One-Laptop Army:** This 26-minute talk from a Google Cloud AI engineer shows how Claude turns one laptop into a [**full engineering team**](https://x.com/0xMovez/status/2054250035211116589) (11K bookmarks).

* **Hiring Hot Take:** Coursera co-founder Andrew Ng isn't buying the AI job [**apocalypse narrative**](https://x.com/AndrewYNg/status/2054236506756370865), with concrete moves devs should make instead (3.1K likes).

* **Code Addiction:** A Meta staff engineer names [**3 psychological hooks**](https://www.youtube.com/watch?v=s8sTx-oidqc&t=1356s) behind why devs can't stop running 5-10 Claude Code instances at once.

* **Codex Combo:** This developer figured out how to make Codex 5.5 medium [**outperform**](https://x.com/cjzafir/status/2054190137941315651) extra high on complex tasks, without burning rate limits (2.3K bookmarks).

* **Ghost Colleagues:** Cursor's CEO says every developer is about to work alongside "tens of thousands of ghost colleagues". [**Here's the new playbook.**](https://www.youtube.com/watch?v=8h9j2rskP14)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to stop losing context between Claude Code sessions (5K likes)**

Every Claude Code session eventually times out, and the next one starts from scratch. Any decisions made, bugs found, or half-finished plans are lost. To fix this, Matt Pocock, an ex-Vercel engineer, [created](https://x.com/mattpocockuk/status/2052489881088049407) a “/handoff” skill that compresses your current session into a Markdown file so the next agent can start with full context.

To install it, run this in your terminal: “npx skills@latest add mattpocock/skills”.

Select “handoff” from the menu, set Claude Code as your agent, and restart. Before you close a session, run the [skill](https://github.com/mattpocock/skills/blob/733d312884b3878a9a9cff693c5886943753a741/skills/in-progress/handoff/SKILL.md) with a quick description of what's next:

```
/handoff debug the failing auth tests
```
When you start your next session, just load that Markdown file, and Claude will be right back where you left off.

P.S. You can find 50+ AI coding hacks [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/7fb7f812-406c-46ec-a131-aec401d698eb/Thumbnail__27_.jpg?t=1778660150)
Follow image link: (https://www.youtube.com/watch?v=qPLeNFnKwVg)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to build apps with Codex and GPT-5.5:**](https://www.youtube.com/watch?v=qPLeNFnKwVg) This tutorial shows you how to use the Codex app and GPT-5.5 to build and refine iOS or macOS apps. You'll learn how to set up projects with the "App Creator" skill, automate UI tweaks, and even refine your marketing strategy, all while spending less time manually coding in Xcode.

———————————————————————————

### **Top Tool**

[Warp:](https://www.warp.dev/) A modern terminal paired with powerful agents that help you build, test, deploy, and debug code. 

———————————————————————————

### **Top Repo**

[oMLX:](https://github.com/jundot/omlx) This is a high-performance server built specifically for Apple Silicon Macs that makes running local AI models fast and efficient. It allows you to host and manage several local LLMs and vision models at once, all through a simple macOS menu bar app, a web dashboard, or standard APIs that work just like OpenAI or Anthropic.

———————————————————————————

### **Trending Paper**

[**Build agents that remember your users:**](https://platform.claude.com/cookbook/managed-agents-cma-remember-user-preferences) Most AI agents have a short memory, which means you're stuck repeating your preferences every time you chat. Claude’s memory feature changes that. It works like a personal notebook, automatically keeping track of your details and recalling them across every conversation.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 270K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/claude-code-adds-goal-google-catches-first-ai-built-exploit-in-the-wild
