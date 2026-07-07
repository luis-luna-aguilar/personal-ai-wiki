---
title: "🚀  Cognition ships Devin for Security"
type: newsletter
sender: "The Code <superhumancode@news.codenewsletter.ai>"
received: 2026-07-02
gmail_id: 19f232435e9162f2
---

# 🚀  Cognition ships Devin for Security

**From:** The Code <superhumancode@news.codenewsletter.ai>
**Date:** 2026-07-02

View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a56584c5-d6ea-4368-9f31-e87d3ded6ed8/Group_1000005057__1_.jpg?t=1779072339)
Caption: 

----------
**Welcome back.** Fable 5 is back. You already know it's the best coding model. The real question: what should you be using it for? Anthropic's top exec Mike Krieger and the Every team just shared [13 prompts](https://every.to/p/claude-fable-5-prompt-library) you can use right away. Make sure you bookmark these before moving on to the rest of these emails.

**Also:** Cognition ships Devin for Security, how to turn Fable 5 into an orchestrator, and a former Oracle engineering leader's guide to agent loops.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TODAY IN PROGRAMMING**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5a7b1f1e-d39d-44a3-a499-d2eb85160203/Frame_1000003549.jpg?t=1782985630)
Follow image link: (https://www.youtube.com/watch?v=jb96O2IT_Jg)
Caption: Click here to watch Cognition’s Devin for Security in action.


--------------------
**Cognition ships AI agents that find and fix security vulnerabilities:** The SF-based startup just dropped [**Devin Security Swarm**](https://cognition.com/blog/introducing-devin-security-swarm). It sends parallel agents across entire codebases to catch business logic flaws and chained exploits. Each finding is reproduced in a sandbox to prove it is actually exploitable. Devin then writes the patch and opens a PR for review. Cognition says it finds more verified vulnerabilities at 30% lower cost than rivals. [**See how it works.**](https://x.com/cognition/status/2072368168182432109)

**Meta reportedly plans a cloud business to rent AI compute:** The social media giant is drafting plans for a new arm called [**Meta Compute**](https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash). According to Bloomberg, it will sell raw compute capacity and host AI models like Muse Spark. This move positions Meta against AWS, Google Cloud, and Azure. Engineering teams will gain another heavyweight supplier for training and inference workloads.

**Z.ai ships its official coding environment for GLM-5.2: **The Chinese AI lab just released [**ZCode**](https://x.com/Zai_org/status/2072349453361557898). It is an agentic desktop app that turns the model's 1M-token context into long-running coding sessions. Developers can hand off planning, debugging, and code review. You can check progress from mobile or chat apps while tasks keep running. It works with existing API keys on Mac, Windows, and Linux. [**Download it here.**](https://zcode.z.ai/en/docs/install)


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **INSIGHT**

## **The cheapest new Claude model quietly costs more per task than the last one**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/619f321e-b814-462d-8199-7c3dc402e7de/superhumanteam_a_software_engineering_team_working_on_steerin_60318585-257f-4594-a9b9-67633ef915f3_1.jpg?t=1782986781)
Caption: Source: The Code, Superhuman


--------------------
**Sold as the economical one.** Anthropic just [shipped](https://www.anthropic.com/news/claude-sonnet-5) Claude 5 Sonnet as the default for free and Pro users. The pitch was pretty straightforward: performance that rivals Claude Opus 4.8 but at a much lower price point. When you put it to work on real tasks, it ends up costing nearly double what Sonnet 4.6 does. It even costs more than Opus 4.8. So, it turns out the budget option is actually the most expensive of the three to operate.

**Flat on paper.** Anthropic kept the base token rate flat and added a discount on top, calling the switch basically [cost-neutral](https://www.ibtimes.sg/claude-sonnet-5s-lower-price-offer-comes-hidden-catch-88896). At first glance, it looks like a free upgrade. That is the narrative most people are running with. But cost neutral is the giveaway, because a real discount wouldn't need to cancel itself out.

**The token counter.** There are two things quietly driving up the actual bill. First, a new tokenizer is turning the same text into more tokens. Second, the model is working harder. It's running more reasoning loops for every task. Independent testing from Artificial Analysis [confirms](https://artificialanalysis.ai/articles/claude-sonnet-5-agentic-cost) the result. Sonnet 5 ends up costing about 15% more per task than Opus. Counterintuitively, the "cheaper" model is now billing higher than the Opus flagship model it was meant to undercut.

**The dial is the price.** That said, those extra tokens are actually buying you better results. Ramp Labs ran a [benchmark](https://labs.ramp.com/swebench#head-to-head) and saw more test runs and much tighter self-correction than previous versions. If you set the effort level to low or medium, Sonnet stays cheaper. But if you crank it up to the max, Opus actually wins on price. The setting most teams leave on default decides your bill, so tune effort against cost per finished task and stop ranking models by token rate.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN THE KNOW**

## **What’s trending on socials and headlines**


--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/95c55689-29d8-42f2-a904-4f8176ea5168/CleanShot_2026-07-02_at_14.37.57_2x.jpg?t=1782983357)
Caption: Meme of the day.


--------------------
* **AI Tech Lead:** This 5-step Claude Code setup turns Fable 5 into an [**orchestrator**](https://x.com/diegocabezas01/status/2072436501263339841) that hands grunt work to cheaper models (4.9K bookmarks).

* **Agents on Autopilot:** A former Oracle engineering leader uses agent loops and goals to [**fix bugs**](https://www.youtube.com/watch?v=WRkVuebZqLU), triage issues, and ship apps while you sleep.

* **Rate Limit Hack:** The creator of T3.gg shared [**4 tips**](https://x.com/theo/status/2072481845363822914) for heavy Fable use without hitting limits (486K views).

* **Margin Squeeze:** A viral post argues Chinese open-source models are wiping out margins at the **[model layer](https://x.com/quxiaoyin/status/2072244587389935914?s=20)**, and the real money is moving somewhere else (500K views).

* **Hidden Check**: Claude Code was silently flagging China-linked users until a developer [**exposed**](https://x.com/IntCyberDigest/status/2071971609183678544) it (5M views). Anthropic confirmed the experiment and shipped a removal.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **AI CODING HACK**


--------------------
## **How to stop re-prompting Claude Code after a failed command**

Normally, if you run a command in Claude Code and it fails, you'd have to follow up with a second prompt asking for a fix. That's no longer necessary. Anthropic just rolled out an [update](https://code.claude.com/docs/en/whats-new/2026-w26) where any command prefixed with '!' will automatically get a response. 

Just make sure you're on the latest version by running 'claude update' and then start using the '!' prefix for your commands.

```
! npm test
```
Claude instantly analyzes the output and suggests a fix in one go. It works just as well for broken builds, type-check errors, or when you simply need a diff explained.

P.S. Get 50+ AI coding hacks for Claude Code, Cursor, and Codex [here](https://hackbook-chi.vercel.app/).


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **TOP & TRENDING RESOURCES**




--------------------
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/a8d611bf-5ee4-43eb-9950-899136f9648a/Thumbnail__41_.jpg?t=1782986949)
Follow image link: (https://www.youtube.com/watch?v=WRU7-4bpZkg)
Caption: Click here to watch the tutorial.


--------------------
### **Top Tutorial**

[**How to build a continuous eval pipeline for multi-agent systems with Gemini:**](https://www.youtube.com/watch?v=WRU7-4bpZkg) In this tutorial, you'll learn how to move from subjective testing to data-driven assessments. It covers replacing manual testing with automated, model-based grading, managing unpredictable AI outputs, and integrating automated evaluation directly into a CI/CD pipeline using Cloud Run.

———————————————————————————

### **Top Tool**

[**BrowserBash:**](https://browserbash.com) This CLI tool converts plain-English sentences into reliable browser tests using local models. It eliminates selectors and flaky locators while supporting Chrome, LambdaTest, and various CDP endpoints.

———————————————————————————

### **Top Repo**

**[OpenWiki](https://github.com/langchain-ai/openwiki)**** (by LangChain):** A CLI built specifically for agents that writes and maintains documentation for your codebase.

———————————————————————————

### **Trending Paper**

[**Are we ready for an agent-native memory system?**](https://huggingface.co/papers/2606.24775) Current tests treat AI agent memory like a black box, ignoring backend data management trade-offs and operational costs. This study reveals that no single architecture fits all scenarios, meaning success depends entirely on matching the memory structure to specific workload bottlenecks.


----------View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/18efc0eb-c3c4-483f-a001-0fe0dcca16c3/Group_from_Figma__2_.png?t=1758120539)
Caption: 

----------
##### **IN CASE YOU MISSED IT**


--------------------
### ==**Our most-clicked story from yesterday**==

Check out the top [**30 prompt**](https://agent-cookbook.com/tutorial/top-30-prompt-techniques-that-actually-work-in-2026) techniques that work in 2026.


--------------------
==**Grow customers & revenue:**== Join companies like Google, IBM, and Datadog. Showcase your product to our 300K+ engineers and 150K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

———————————————————————————

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team


----------
———

You are reading a plain text version of this post. For the best experience, copy and paste this link in your browser to view the post online:
https://codenewsletter.ai/p/cognition-ships-devin-security-swarm-meta-reportedly-plans-a-cloud-business
