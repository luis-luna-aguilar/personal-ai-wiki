---
title: "Introducing the Agents API | OpenAI"
type: article
url: https://openai.com/index/introducing-the-agents-api/
received: 2026-09-10
gmail_id: 1a08d378d7e37038
fetched: true
published: 2026-09-10
note: rendered via aside
---

# Introducing the Agents API | OpenAI

**URL:** https://openai.com/index/introducing-the-agents-api/

Introducing the Agents API | OpenAI

September 10, 2026

Product
API
Introducing the Agents API

Build and run cloud agents with the Codex harness, fully managed by OpenAI.

Introducing the Agents API

00:0502:18

Listen to article
5:09
Share
What our customers are saying about Agents API
Build cloud agents with a single API call
Choose your agent environment
OpenAI hosted sandboxes
Build with an evolving Codex harness
Keep agents working across long sessions
Help agents efficiently use more tools
Let agents parallelize work with subagents
An open-source foundation
Start building

As we’ve scaled Codex and ChatGPT for Work to millions of people around the world, we’ve learned what it takes to make long-running agents work well in practice. Useful agents need a powerful harness that manages context, uses tools efficiently, and coordinates subagents. They also need infrastructure that keeps them running reliably for days, with environments where they can work with files, run code, and save intermediate results.

Today, we’re introducing the Agents API⁠
(opens in a new window)
 in public beta, bringing that same harness and infrastructure that powers Codex to developers through a simple, flexible API.

What our customers are saying about Agents API
1 of 8
“With the Agents API, our evaluation score went from 0.71 to 0.85. The subagent support in the API is great and drastically sped up our workflow. Previously it was pretty cumbersome to observe and orchestrate subagents in our old setup but the new APIs gave us a 4x latency reduction. We spent a long time trying to optimize for this and the subagent flows were a huge out-of-the-box lift.”
Jack Weissenberger, CTO, Ciridae
Ciridae
Long Lake
WithCoverage
SafetyKit
Dwelly
Hypha
deepsense.ai
Nash.ai
Build cloud agents with a single API call

With the Agents API, you can create a production-ready agent in a single API call by specifying the task, model, tools, and environment:

JavaScript
1
import OpenAI from "openai";
2


3
const client = new OpenAI();
4


5
const session = await client.beta.agents.sessions.create({
6
  agent: {
7
    model: "gpt-6-astra",
8
    tools: [
9
      {
10
        type: "mcp",
11
        server_label: "observability",
12
        transport: {
13
          type: "http",
14
          server_url: "https://observability.example.com/mcp",
15
        },
16
      },
17
    ],
18
    multi_agent: { enabled: true, max_concurrent_subagents: 3 },
19
  },
20
  vault_ids: ["vault_YOUR_VAULT_ID"],
21
  environment: {
22
    type: "openai_hosted",
23
    capability_directories: ["/workspace/capabilities/skills"],
24
  },
25
  input:
26
    "Investigate service-api’s elevated 5xx rate over the last 30 minutes. " +
27
    "Delegate deployment, error, and dependency analysis to subagents. " +
28
    "Save findings, evidence, and recommended mitigation in /workspace/outputs.",
29
});

OpenAI hosts and maintains the harness. You choose the agent’s compute environment: in an OpenAI-managed sandbox, on your own infrastructure, or with one of our sandbox partners. The Agents API gives you a strong foundation for building agents on top of our optimized agent harness and infrastructure, so you can focus on the tools, knowledge, and workflows that make your agent unique.

Agents API powers your agents with the same harness and infrastructure behind Codex.

Choose your agent environment

Different workloads need different compute, storage, and deployment options. The Agents API lets you choose a sandbox that fits your application.

We’re partnering with ecosystem providers⁠
(opens in a new window)
, including Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, and Vercel, to provide first-class integrations for a range of needs:

Fully managed environments or deployments within your VPC

Specific file and secret storage mechanisms

Different CPU, GPU, and memory configurations, with performance, cold-start, and cost profiles to match your company’s workflow.

The Agents API offers first-class integrations with popular ecosystem providers.

OpenAI hosted sandboxes

For developers who want to get started quickly and scale efficiently, we’re also introducing the OpenAI hosted sandbox⁠
(opens in a new window)
. This leverages the same sandboxing infrastructure that powers Codex and ChatGPT.

OpenAI provisions and manages the sandbox, giving your agent a secure and performant environment to run code, work with files, and produce artifacts. These sandboxes can be flexibly configured with your files, packages, skills and plugins to give the agent what it needs to complete the task.

Build with an evolving Codex harness

Taking advantage of new model capabilities often means reworking your harness, taking valuable time away from improving your application. The Agents API provides versioned access to these capabilities with each model launch. We maintain and continuously improve the harness alongside our models, helping your agents get better performance from every upgrade. For example, recent improvements to the harness include:

Keep agents working across long sessions

To support models working for hours, we’ve built context management that helps agents carry relevant information across longer sessions. The Agents API automatically compacts⁠
(opens in a new window)
 earlier context as a session approaches its context limit, preserving information the agent needs to continue. Developers can build workflows that span multiple context windows without implementing their own compaction logic.

Help agents efficiently use more tools

The Agents API helps agents find the right tools and use them efficiently. Tool search⁠
(opens in a new window)
 loads relevant tool definitions as needed, helping reduce token usage and cost while preserving the model’s cache. Once tools are available, programmatic tool calling⁠
(opens in a new window)
 lets agents run calls in parallel, chain related operations, and filter or combine results in code so they can work through large volumes of data while bringing only the relevant results back into context. The Agents API supports MCP, custom functions, and built-in tools like web search.

JSON
1
"agent": {
2
  "tools": [
3
    {
4
      "type": "mcp",
5
      "server_label": "openai_docs",
6
      "transport": {
7
        "type": "http",
8
        "server_url": "https://developers.openai.com/mcp"
9
      }
10
    },
11
  ]
12
}
Let agents parallelize work with subagents

With multi-agent support⁠
(opens in a new window)
, the Agents API can break complex tasks into independent pieces and delegate them to subagents that work in parallel. Each subagent maintains its own context, helping it stay focused on its assignment, while the main agent coordinates their work and brings the results together. This can speed up research, analysis, and coding tasks that benefit from parallel work, without requiring you to build your own orchestration.

JSON
1
"agent": {
2
  "model": "gpt-6-astra",
3
  "multi_agent": {
4
    "enabled": true,
5
    "max_concurrent_subagents": 3,
6
  }
7
}
An open-source foundation

The Agents API is powered by the open-source Codex harness, giving developers visibility into the core logic that coordinates model calls, tools, and context. With the Agents API, OpenAI operates and maintains that harness while developers can inspect and learn from its public codebase⁠
(opens in a new window)
.

Start building

Agents API is available in public beta today to all developers. There are no additional fees for using the Agents API – you simply pay for the tokens and tools your agents use, as outlined on our pricing page⁠
(opens in a new window)
.

Explore the Agents API overview⁠
(opens in a new window)
 to learn more, or follow the quickstart⁠
(opens in a new window)
 to get started and bring the harness behind Codex into your own agents.

During the public beta, we’ll iterate quickly based on your feedback as we work toward general availability. Let us know what’s working, where you’re running into friction, and what you need to build and run your agents in production.

API
Codex
2026
Author
OpenAI
Keep reading
View all
Introducing GPT-6.2 Astra and Sol

Product
Nov 17, 2026

Introducing ChatGPT for Sales

Product
Nov 17, 2026

More ways to move care forward with ChatGPT for Healthcare

Product
Nov 16, 2026
