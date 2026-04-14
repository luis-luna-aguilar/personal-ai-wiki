---
title: Anthropic introduces Claude Managed Agents, Meta drops Muse Spark
type: source
source_type: newsletter
url: https://codenewsletter.ai/p/anthropic-introduces-claude-managed-agents-meta-drops-muse-spark?_bhlid=2d5915e310c44293e886e1fc652795ecde183bad
fetched: 2026-04-10
---

# Anthropic introduces Claude Managed Agents, Meta drops Muse Spark

**Welcome back.** Anthropic has shipped over 75 updates in 60 days. And they're at it again. They just dropped Claude Managed Agents, and it changes how you'll build agents from here.

**Also:** How to learn LLMs the way engineers need to, build iOS apps with Codex, and why Postman's founder wants you to rethink your engineering team.

### **Today’s Insights**

* Powerful new updates and hacks for devs
* Open-source becomes the primary choice for agents
* How to fix Claude Code's thinking regression
* Trending social posts, top repos, and more

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/11a26808-17d1-4ff6-83c7-3b9554ee4acf/Untitled_design__42_.jpg)](https://x.com/claudeai/status/2041927687460024721)

Click here to see it in action.

**Anthropic ships a faster way to build production agents:** The AI lab just unveiled **[Claude Managed Agents](https://claude.com/blog/claude-managed-agents)**, a suite of APIs designed to cut months of infrastructure work down to days. Developers define their agents’ tasks and tools while Anthropic handles sandboxing, orchestration, and permissions on its cloud. Early adopters like Notion and Asana are already using it to ship coding agents, AI teammates, and enterprise workflows. [Watch how Notion uses it.](https://www.youtube.com/watch?v=45hPRdfDEsI&t=9s)

**Meta launches its first model from Superintelligence Labs:** The social media giant just dropped **[Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl)**, a multimodal AI model that excels at vision, reasoning, and agent workflows. Its key feature is Contemplating mode, which runs multiple agents in parallel to solve complex problems without increasing latency. Meta claims their updated training stack matches the performance of Llama 4 Maverick while using 10x less compute. [Try it here.](https://meta.ai/)

**Cursor teaches Bugbot to improve itself:** The AI coding startup just **[upgraded](https://cursor.com/blog/bugbot-learning)** its code reviewer with the ability to learn on the job. Bugbot now tracks how developers interact with its suggestions by analyzing reactions, replies, and reviewer comments to refine its future rules. With over 110K repos already using the feature, Bugbot has generated more than 44K rules, pushing its resolution rate to nearly 80%, well ahead of competitors.

[MongoDB AI Learning Hub](https://fandf.co/41l1KsP) has the technical training pathways and tools you need to level up your AI app-building game.

Explore practical guides, tutorials, and quick starts for all skill levels, from foundational concepts like understanding AI tool stacks to [advanced implementations](https://fandf.co/41l1KsP) using RAG, MongoDB Vector Search, and LLM optimization.

##### **INSIGHT**

## **How open-source became the primary choice for agents**

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/e9da194d-7408-4382-9e03-882e83210b79/superhumanteam_a_software_engineering_team_working_on_assembl_f0fc30a7-0605-4f35-9f79-edbefd84930c_0.jpg)

Source: The Code, Superhuman

**Apps are no longer the most valuable part of software.** Mitchell Hashimoto, the founder of HashiCorp, spent 18 months [building](https://x.com/mitchellh/status/2041566958681014418) Ghostty, a terminal emulator that hit roughly one million daily users on macOS. Then he open-sourced its core as a library called libghostty, and that library reached millions of daily users in two months. The library outran the app because AI agents could plug it directly into new projects.

**Agents prioritize open-source by default.** Hashimoto's experience isn't a one-off. Independent research labs have found that AI coding agents consistently reach for open-source, free components over commercial alternatives. Agents aren't great at building things from scratch, but they're very good at snapping together well-documented building blocks. Which means the individual components you ship are starting to matter more than the finished product built on top of them.

**More assembly, more risk.** All that agent-assembled software comes with trade-offs: new security vulnerabilities, instability, and developers who don't fully understand the systems they've stitched together. Hashimoto built a [**trust-gating tool**](https://github.com/mitchellh/vouch) specifically to filter out unreliable dependencies and keep things stable.

**What’s next?** Big, full-featured apps aren't going away, but they're getting more specialized. The "building block" layer of the ecosystem is now handling R&D and niche use cases on autopilot. If you're deciding where to put engineering resources, the leverage has shifted downstream toward foundational tools. Ship primitives, not just products.

##### **IN THE KNOW**

## **What’s trending on socials and headlines**

* **Project Glasswing:** Anthropic is using an unreleased Claude model to hunt **[vulnerabilities](https://x.com/AnthropicAI/status/2041578392852517128)** in critical open-source software before attackers do. A senior engineer’s [reaction](https://x.com/theo/status/2041825324837781749) is making rounds on the internet (27M views).
* **iOS Shortcut:** Building iOS apps with Codex has been painful because agents don't know Xcode. This **[skill fixes that](https://x.com/PaulSolt/status/2041643862913949929)**.
* **LLM Guide:** Skip the academic papers. This guide teaches LLMs the way engineers actually need to learn them: [**build, optimize, deploy**](https://x.com/kmeanskaran/status/2040651169744535722).
* **Agent Ready:** Your coding agents are only as good as the environment they run in. A Cursor engineer shares [**the playbook**](https://x.com/ericzakariasson/status/2041897427431563613) for getting out of the loop.
* **Org Overhaul:** Postman's founder just **[dropped](https://x.com/ivanburazin/status/2041199368296931595)** his blueprint for engineering teams in the AI era.
* **Exit Interview:** This **[conversation](https://x.com/javarevisited/status/2040802388462928308)** between a CEO and manager explains why best engineers quit (1.5M views).
* **YC's Youngest:** Y Combinator just named its youngest General Partner ever — a 25-year-old who dropped out at 15 and built a **[$700M company](https://x.com/gjarrosson/status/2041888014574743577)** along the way.

##### **AI CODING HACK**

## **How to fix Claude Code's thinking regression**

If Claude Code feels like it is losing its edge, you are not imagining it. After [analyzing](https://github.com/anthropics/claude-code/issues/42796) over 17,000 thinking blocks, an AMD engineer found that the tool is under-allocating reasoning for complex tasks.

Instead of performing a deep analysis, Claude is skipping ahead and trying to edit code before fully processing it. AI PM Paweł Huryn [**shared**](https://x.com/PawelHuryn/status/2041418614557802747) three fixes:

1. The fastest: run “**/effort high**” in Claude Code.
2. Use “**/effort max**” on Opus for hard debugging. Then drop this snippet into your "~/.claude/settings.json" file to get a clear look at Claude's reasoning in real time:

```
"showThinkingSummaries": true
```

3. Finally, add this to your CLAUDE.md: “Research the codebase before editing. Never change code you haven't read.”

If you want to bypass adaptive thinking entirely, the Claude Code team **[shared](https://news.ycombinator.com/item?id=47664442)** a nuclear option: CLAUDE\_CODE\_DISABLE\_ADAPTIVE\_THINKING=1.

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/8f9dde19-7f5d-403d-a2b1-c24de2de7ed1/Untitled_design__43_.jpg)](https://www.youtube.com/watch?v=7huCP6RkcY4)

Click here to watch the tutorial.

### **Top Tutorial**

**[How to build self-evolving agent memory:](https://www.youtube.com/watch?v=7huCP6RkcY4)** This tutorial shows devs how to create a self-evolving memory system for Claude Code, built after Andrej Karpathy's knowledge base architecture. You'll learn to use hooks to automatically capture and summarize coding sessions into an Obsidian vault, giving your AI agent long-term memory that evolves alongside your codebase.

### **Top Repo**

**[Andrej-karpathy-skills:](https://github.com/forrestchang/andrej-karpathy-skills)** CLAUDE.md file designed to optimize Claude Code performance by incorporating Andrej Karpathy's observations on LLM coding pitfalls.

### **Trending Paper**

**[How LLMs follow instructions:](https://arxiv.org/abs/2604.06015)** The research investigates whether AI models rely on a single, universal process to follow instructions. Rather than relying on a single process, models dynamically coordinate diverse, specialized language skills to satisfy specific rules.

**Grow customers & revenue:** Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code)

### What did you think of today's newsletter?

Your feedback helps us create better emails for you!

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team
