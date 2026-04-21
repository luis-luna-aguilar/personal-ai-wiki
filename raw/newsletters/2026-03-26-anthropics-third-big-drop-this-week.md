---
title: "⚡  Anthropic's third big drop this week"
type: newsletter
sender: "The Code <thecode@mail.joinsuperhuman.ai>"
received: 2026-03-26
gmail_id: 19d2a750c4bede36
---

# ⚡  Anthropic's third big drop this week

**From:** The Code <thecode@mail.joinsuperhuman.ai>
**Date:** 2026-03-26

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/32c8c971-340a-4f62-a6b8-f362e57e5397/image__83_.jpg?t=1770628392)
Caption: 

----------
**Welcome back.** Anthropic is on a roll. First, Claude took over your Mac (Computer Use). Then, Claude Code started managing its own permissions (Auto Mode). Now, they're coming for your phone.

**Also:** Anthropic engineer explains how Claude takes control of your computer, how to build CLIs for AI agents, and why engineering roles are up 400% since last year.


--------------------
### **Today’s Insights**

* Powerful new updates and hacks for devs

* How Uber uses AI for development

* How to auto-generate your CLAUDE.md

* Trending social posts, top repos, and more


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/098df902-ce0b-49a0-86c2-27dc7c5235e3/Untitled_design__27_.jpg?t=1774510258)
Follow image link: (https://www.youtube.com/watch?v=NAwvkrxompk)
Caption: Click here to see it in action.


--------------------
**Claude now lets you access work tools from your phone:** The AI lab just brought popular workplace tools like Figma, Slack, and Amplitude directly into the [**Claude mobile app**](https://x.com/claudeai/status/2036850783526719610). Now, you can now review designs, debug analytics, and manage tasks straight from your phone. This marks Anthropic’s third big release this week, following the launch of Computer Use for Mac and [**Auto Mode**](https://x.com/claudeai/status/2036503582166393240) for Claude Code (a new feature that allows the coding assistant to manage its own permissions instead of stopping to ask for approval on every single task).

**Cursor's cloud agents can now run entirely in your own network:** The AI coding startup just made [**self-hosted**](https://cursor.com/blog/self-hosted-cloud-agents) cloud agents generally available. Each agent runs in an isolated VM with full access to internal caches, dependencies, and network endpoints, ensuring that code, secrets, and build artifacts never leave the team's environment. While Cursor handles the orchestration and model access, teams maintain their existing security setup. Companies like Brex, Notion, and Money Forward are already using them to delegate end-to-end software builds.

**Cloudflare launches 100x faster sandboxing for AI agents:** Cloudflare just dropped its [**Dynamic Worker Loader API**](https://blog.cloudflare.com/dynamic-workers/) as an open beta, offering a fresh approach for teams to securely run AI-generated code at scale. Rather than spinning up heavy containers that take hundreds of milliseconds to boot, this system uses V8 isolates that start in under ten milliseconds and use significantly less memory. Additionally, agents can now interact with tools using typed TypeScript APIs, which helps keep token counts low and efficiency high.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **How Uber uses AI for development**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b0c2da17-5422-418c-9a85-3d8c7237411e/superhumanteam_An_astronaut_driving_an_Uber_car_with_Uber_wri_62345265-37a1-40a6-ae99-045b3152419d_0.jpg?t=1774520070)
Caption: Source: The Code, Superhuman


--------------------
**Uber pulls back the curtain.** At the [**Pragmatic Summit**](https://www.pragmaticsummit.com/) in San Francisco, Ty Smith and Anshu Chadha from the Dev Platform team gave a rare look at how the company is rolling out AI agents across its 3,000-person engineering team. While many companies claim to be AI-powered, Uber actually showed what it takes to get there.

**Engineers have changed how they work.** About **[84% of Uber's developers](https://www.linkedin.com/posts/pneppalli_agentic-software-engineering-adoption-is-activity-7439402236541157376-6PwV/)** now use agentic coding workflows, which look nothing like simple tab completion. Engineers now kick off multiple agents in parallel on different tasks, then review and redirect the output. Their role has shifted from writing code to orchestrating the systems that write it. In fact, Claude Code adoption nearly doubled in three months while traditional IDE tools plateaued.

**This shift requires serious infrastructure.** Uber built a central MCP Gateway to turn internal endpoints into MCP servers, an AIFX CLI for provisioning tools, and Minion, a platform for running background agents with monorepo access. All of this **[drove](https://newsletter.pragmaticengineer.com/i/190542498/2-internal-tooling-mcp-gateway-uber-agent-builder-and-the-aifx-cli)** AI costs up 6x since 2024. The team also noted that top-down mandates didn't work. Instead, peer-driven adoption, where engineers shared their wins, was what really moved the needle.

**The cost of AI is the part everyone skips.** Most rollout stories focus only on adoption numbers. Uber’s story is different because it covers the infrastructure decisions, the tooling mistakes, and what happens when agents start opening 11% of pull requests. If your team is working through its own AI strategy, the **[full talk](https://www.youtube.com/watch?v=i1tZN41VKcE)** is well worth your time.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/c998f173-5343-4318-8334-0f403df4c36d/CleanShot_2026-03-26_at_14.25.18_2x.jpg?t=1774515349)
Caption: Meme of the day.


--------------------
* **Screen Takeover:** An Anthropic engineer [**shared**](https://x.com/felixrieseberg/status/2036476512250241420) exactly how Claude takes control of your computer.

* **Caught by a Bug:** A supply chain attack hit LiteLLM (one of the most popular AI packages) and [**stole credentials**](https://x.com/karpathy/status/2036487306585268612) from anyone who installed the package. Andrej Karpathy breaks it down (61.7M views).

* **Cognitive Debt:** AI-heavy codebases are creating a new problem: code that nobody on the team can keep in their head. An ex-Vercel engineer just shared a [**simple rule**](https://x.com/mattpocockuk/status/2036768796065640554) to fix it.

* **Plot Twist:** Engineering roles are up over 400% since last year's slump. Ex-Airbnb product lead Lenny Rachitsky's [**viral post**](https://x.com/lennysan/status/2036535460726767793) on why the job market is defying the doom narrative (1.2M views).

* **CLI Blind Spot:** Agents choke on interactive prompts, missing examples, and unpredictable command structures. A Cursor engineer posted a [**guide**](https://x.com/ericzakariasson/status/2036762680401223946) to building CLIs that agents can actually use.

* **Prompt Vault:** 300 copy-paste Claude prompts just [**dropped**](https://x.com/cyrilXBT/status/2036280031782060364), built for real dev work, from code reviews to AI agent design.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**

## **How to auto-generate your CLAUDE.md**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2864fb12-9168-4c03-8ad9-29b488ae8964/HEGxKumbEAA2LRE.jpg?t=1774499841)
Follow image link: (https://x.com/dani_avila7/status/2036103229327790560)
Caption: Source: X/dani_avila7


--------------------
Most Claude Code users still write their CLAUDE.md files by hand, even though Claude can already infer most of that information directly from the source code. To automate this, developer Daniel San [**discovered**](https://x.com/dani_avila7/status/2036103229327790560) an experimental flag from the Claude Code team that handles the heavy lifting for you.

To enable it, just add this snippet to your “.claude/settings.local.json”:

```
{
{
  "env": {
    "CLAUDE_CODE_NEW_INIT": "1"
  }
}
```
Just run “/init”. The latest version automatically scans your codebase to pick up on your tech stack, linters, and CI configs. You'll even get a chance to review and approve the proposal before anything actually gets written.

San's repo went from a 458-line CLAUDE.md to 68 lines. The new “/init” command focuses purely on the context Claude might miss if it weren't explicitly briefed. It's still an experimental flag, though, so keep in mind that things are likely to change. 


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5a892238-6bc1-48b4-91be-6d81cdfee4bf/Untitled_design__28_.jpg?t=1774517325)
Follow image link: (https://www.youtube.com/watch?v=JCN2RLlXKG0)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to build software using multi-agent AI workflows:**](https://www.youtube.com/watch?v=JCN2RLlXKG0) This tutorial shows developers how to quickly build apps using multi-agent AI workflows in Claude Code. You will learn hands-on techniques for structuring prompts, enforcing software design principles, and managing project architecture - effectively leading AI agents the same way you would a team of human engineers.

———————————————————————————

### **Top Repo**

[**Gemini API skills:**](https://github.com/google-gemini/gemini-skills/) Skills are a lightweight technique for adding relevant context to your agents. This repo contains a library of skills for the Gemini API, SDK and model interactions.

———————————————————————————

### **Trending Paper**

[**A safer way to skip permissions (by Anthropic):**](https://www.anthropic.com/engineering/claude-code-auto-mode) Being bombarded with permission requests eventually leads to approval fatigue, which often pushes users to bypass security checks altogether. Anthropic's "auto mode" fixes this by using AI classifiers to handle routine approvals automatically while still blocking anything potentially dangerous.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/anthropic-brings-work-tools-to-mobile-cursor-drops-self-hosted-cloud-agents
