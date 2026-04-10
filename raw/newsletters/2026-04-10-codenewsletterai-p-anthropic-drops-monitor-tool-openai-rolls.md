---
title: Anthropic drops Monitor tool, OpenAI rolls out a new $100/month Pro plan
type: source
source_type: newsletter
url: https://codenewsletter.ai/p/anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan
fetched: 2026-04-10
---

# Anthropic drops Monitor tool, OpenAI rolls out a new $100/month Pro plan

**Welcome back.** Software engineering best practices were built for humans. Now that agents write most of the code, we're rebuilding those practices from scratch. Anthropic's new Monitor tool for Claude Code is a perfect example. See how it works.

**Also:** How to build an agent harness, 50+ guides to ship with Claude, and what Karpathy thinks separates AI hype from reality.

### **Today’s Insights**

* Powerful new updates and hacks for devs
* What is agentic thinking and why it matters
* How to auto-load project context in Claude Code
* Trending social posts, top repos, and more

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/340ffa83-2ffc-41eb-a21e-3534c28eb022/Untitled_design__44_.jpg)](https://x.com/noahzweben/status/2042332268450963774?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)

Click here to see it in action.

**Claude Code gives developers a security assistant:** The AI lab just dropped [Monitor tool](https://x.com/noahzweben/status/2042332268450963774?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai), an update that lets its coding agent run background scripts to track real-time events. It is basically a security camera for your code that only alerts you when it spots movement. You can set Claude to watch for dev server errors, track failing tests, or monitor a production launch for hours. This approach saves tokens because it only fires up when something actually goes wrong.

**Cursor brings screenshots and video to agent-generated PRs:** The AI coding startup just shipped a **[feature](https://x.com/cursor_ai/status/2042287192895267212?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** that automatically attaches demo videos and screenshots to the GitHub PRs created by its cloud agents. This lets teams visually review AI-generated code changes without ever leaving the platform. In one demo, an agent built a color picker, refined the UI, added tests, and dropped a 20-second clip of the finished feature directly into the PR.

**OpenAI adds $100 Pro plan for heavier Codex use:** The ChatGPT maker just rolled out a new [$100/month](https://x.com/OpenAI/status/2042295688323875316?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) **[Pro tier](https://x.com/OpenAI/status/2042295688323875316?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** for developers who have outgrown the standard $20 Plus plan. It offers five times the Codex usage, an exclusive Pro model, and unlimited Instant and Thinking models. Designed for heavy coding sessions, the plan includes a launch promo where new subscribers can access up to ten times the standard Plus-level usage through May 31st.

For 10+ years, [AI Council](https://aicouncil.com/sf-2026?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) has been gathering the world's top AI infrastructure minds to share what’s working (and where we’re headed next).

* The co-inventor of ChatGPT
* Creator of DuckDB and Codex
* Engineers behind ClickHouse, Databricks, Datadog, and LangChain

…and more. Takes place May 12-14 in San Francisco.

##### **INSIGHT**

## **What is agentic thinking, and why does it matter now**

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/b8bb9234-1ea1-4d72-8557-0a2f6d42629f/superhumanteam_a_software_engineering_team_working_on_trainin_66c7efe2-6a9f-4b16-b9a2-f886dd4ef72b_1.jpg)

Source: The Code, Superhuman

**The reasoning era is over.** Junyang Lin, the former tech lead behind Alibaba's Qwen models, [stepped down](https://venturebeat.com/technology/did-alibaba-just-kneecap-its-powerful-qwen-ai-team-key-figures-depart-in?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) in early March after what colleagues called an involuntary departure. A few weeks after leaving, he [published](https://justinlin610.github.io/blog/from-reasoning-to-agentic-thinking/?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) his first essay with the blunt thesis that the reasoning wave sparked by OpenAI’s o1 and DeepSeek’s R1 is already winding down, only to be replaced by agentic thinking.

**Interaction over monologue.** While reasoning models just think longer before they speak, agentic models think in order to act. They use tools, read environment feedback, and pivot mid-task. The key question is no longer "how long can it think?" but "can it execute effectively over multiple turns?" This shift requires models that know when to stop ranting about theory and start doing.

**More thinking doesn't mean more intelligence.** Recent [research](https://lilianweng.github.io/posts/2025-05-01-thinking/?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) shows that simply increasing test-time compute doesn't always yield better results. In fact, giving agents tool access makes training riskier, as they can exploit logs or search for answers rather than actually solving problems.

**Environments are the new moat.** Lin points out that building better environments is becoming its own startup [category](https://genaiassembling.substack.com/p/what-junyang-lin-saw?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) because training agents now involves browsers, terminals, and API layers instead of just models. Your competitive edge is shifting from RL algorithms to harness engineering and the ability to close the loop between what a model decides and what actually happens next.

##### **IN THE KNOW**

## **What’s trending on socials and headlines**

* **Claude Cookbook:** Anthropic just published [**50+ ready-to-use guides**](https://platform.claude.com/cookbook/?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) for building with Claude, covering managed agents, context compaction, and multi-modal workflows.
* **Better Agents:** LangChain open-sourced a system that [**runs evals**](https://x.com/Vtrivedy10/status/2041927488918413589?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) on your agent, finds what's broken, and fixes the prompts automatically with no manual tuning.
* **Faster File Search:** The creator of Claude Code **[broke down](https://x.com/bcherny/status/2042352720489955539?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** how they made file search 3x faster on massive codebases. Enterprise users are already confirming the speed boost.
* **Reality Gap:** Andrej Karpathy says there's a growing gap in how people understand AI — and it comes down to who's paying [**$200/month**](https://x.com/karpathy/status/2042334451611693415?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai) and who isn't (2M views).
* **Session Extender:** Sick of hitting Claude's usage limits? This **[guide](https://x.com/hooeem/status/2042293751805329445?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** bridges Claude Code with NotebookLM to offload research and stretch your tokens.
* **AGI Timeline:** OpenAI's Chief Scientist just **[shared](https://x.com/jacobeffron/status/2042234897134162077?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** when they expect AI to go from intern-level to fully autonomous researcher, and the gap is shorter than you'd think.
* **Advisor Mode:** Anthropic shipped a way to use Opus for complex planning, but leaves the **[grunt work to Sonnet](https://x.com/claudeai/status/2042308622181339453?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** in a single API call. It costs 11.9% less per task (2.9M views).

##### **AI CODING HACK**

## **How to auto-load project context in Claude Code**

Claude Code loads your CLAUDE.md at session start. But it doesn't know what branch you're on, what files changed, or what broke since your last session. You end up typing "check git status" before doing anything useful.

A hook pattern from Claude Code's [hooks system](https://dev.to/holasoymalva/the-ultimate-claude-code-guide-every-hidden-trick-hack-and-power-feature-you-need-to-know-2l45?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai#:~:text=8.-,SessionStart%20Hook,-Executes%20when%20starting) fixes this for good. Just add this to your “.claude/settings.json”:

```
# Load development context automatically
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "git status > /tmp/claude-git-context.txt && echo 'Development context loaded'"
      }]
    }]
  }
}
```

That's it. Now, whenever you start a session or clear your history, Claude automatically pulls in your current branch and any changes. You'll have all the context you need to get straight to work.

[![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/2f6b6a09-3508-4a6f-a72f-8d5b1bd6c90d/Untitled_design__45_.jpg)](https://www.youtube.com/watch?v=MzhIr7BfpI0&utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)

Click here to watch the tutorial.

### **Top Tutorial**

**[How a senior software engineer uses coding agents:](https://www.youtube.com/watch?v=MzhIr7BfpI0&utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** This tutorial shows you how to turn Claude Code into a powerful autonomous assistant. You'll learn how to set up project context files, build automated validation loops to catch bugs, run parallel sub-agents, and master a strict "plan, execute, and review" workflow to supercharge your coding.

### **Top Repo**

**[Archon:](https://github.com/coleam00/Archon?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)** A harness builder for AI coding agents. You can define your entire development process from planning and implementation to code reviews and PRs, as YAML workflows that run reliably across all your projects.

### **Trending Paper**

**[ConvApparel (by Google):](https://research.google/blog/convapparel-measuring-and-bridging-the-realism-gap-in-user-simulators/?utm_source=twitter&utm_medium=social&utm_campaign=social_post&utm_content=gr-acct)** Today's AI user simulators feel way too perfect and unnaturally patient compared to real people. But when you train these simulators on actual human data instead of just feeding them instructions, they become much more realistic and adaptable.

**Grow customers & revenue:** Join companies like Google, IBM, and Datadog. Showcase your product to our 200K+ engineers and 100K+ followers on socials. [Get in touch.](https://www.passionfroot.me/the-code?utm_campaign=anthropic-drops-monitor-tool-openai-rolls-out-a-new-100-month-pro-plan&utm_medium=referral&utm_source=codenewsletter.ai)

### What did you think of today's newsletter?

Your feedback helps us create better emails for you!

You can also reply directly to this email if you have suggestions, feedback, or questions.

Until next time — The Code team
