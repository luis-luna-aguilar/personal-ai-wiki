---
title: Introducing DigitalOcean Managed Agents: One AI-native stack to power your intelligence
type: source
source_type: article
url: https://www.digitalocean.com/blog/managed-agents-public-preview
fetched: 2026-10-26
---

# Introducing DigitalOcean Managed Agents: One AI-native stack to power your intelligence

Prompt Caching is now GA on DigitalOcean Serverless Inference

Introducing Agent Droplets

Blog
Docs
Careers
Get Support
Contact Sales
DigitalOcean
Products

Featured AI Products

Compute

Containers and Images

Managed Databases

Management and Dev Tools

Networking

Security

Storage

Browse all products
Featured AI Products

Managed Agents

Run AI agents in the cloud with governed tool access

New

Learning Services

Improve agents and models with evidence

New

Data Services

Store, retrieve, and surface the context you need

Inference Engine

Run inference at scale with policy-driven routing

Model Library

Discover, compare, and evaluate AI models

GPU Droplets

GPU-powered virtual machines to build and run AI apps

Browse all products
Solutions

AI/ML

CMS

Data and IoT

Developer Tools

Gaming and Media

Hosting

Security and Networking

Startups and SMBs

Web and App Platforms

See all solutions
AI/ML

AI HR Knowledge Assistant

Deploy AI tools developed for Human Resources

AI Training GPU

Accelerate model training with dedicated GPU infrastructure

AI Recommendation Engine

Build tools to personalize user experiences

Multimodal AI

Run models that process multiple data types

GPU Clusters

GPUs clustered together for large-scale tasks

GPU Inference

Serve models efficiently with optimized GPU compute

Developers

Community

Documentation

Developer Tools

Get Involved

Utilities and Help

Community

Blog

The latest product releases and insights from our experts

CSS Tricks

All things web design

The Wave

Content to level up your business

Tutorials

Our extensive library of technical articles

Q&A

Answers to your cloud and coding questions

YouTube

Educational content and tutorials

Visit DigitalOcean's Community Site
Partners

Become a Partner

Marketplace

Become a Partner

About Partner Pod

Discounts, revenue share, and more for businesses

AI Partner Program

Boost your AI business

DigitalOcean Startups

Resources and support to propel your startup

Partners Directory

Current list of DigitalOcean Partners

Customer Stories

Customers growing on DigitalOcean

Need help? Talk to an expert
Become a Partner
Pricing
Log in
Sign up
Product updates
Introducing DigitalOcean Managed Agents: One AI-native stack to power your intelligence

By DigitalOcean

Updated: September 22, 2026
11 min read
<- Back to blog home
Table of contents
Why are agentic workloads different from traditional cloud applications?
DigitalOcean Managed Agents: Scale agentic work with purpose-built computing
DigitalOcean Harness Runtime: Sessions that outlive your laptop
DigitalOcean Action Gateway: governed access to tools for agents to do real-world work
Pricing: Superior economics grounded in actual consumption
Performance
Get started in seconds
Unified observability: See what your agent did, in one place
Built for teams already running agents

Following a successful private preview, we’re thrilled to open DigitalOcean Managed Agents to everyone. Teams can now deploy their preferred agent harness (like OpenCode, Codex CLI) or bring their own, connect agents to 16,000+ tools, and help agents do more work at scale without building or maintaining any infrastructure themselves. With native integration to DigitalOcean’s Inference Engine, Managed Agents brings inference tokens, agent execution, and tool use together, so you can scale your intelligence all in one place. Agents go from session creation to a response in less than a couple of seconds and resume paused work in ~300 milliseconds. With per-second active CPU billing, you pay only for the CPU your agents actually consume. Customers like OpenHands, Qencode, and Amplitude are building and scaling on Managed Agents, get started today.

Why are agentic workloads different from traditional cloud applications?

Developers and teams are asking agents to do increasingly ambitious work: implement features, investigate production issues, build new applications, research across systems, and coordinate subagents across different tasks. Consider an agent investigating a spike in checkout errors: it queries logs across several services through an MCP server, writes and runs a script to reproduce the bug, tests a fix, and opens a pull request for a teammate to review before it ships to production. Querying the logs, running the reproduction script, and testing the fix can each briefly demand substantial CPU and memory. Between those steps, and while it waits on tokens or a human approval, the agent may consume little or no CPU at all. But its context, files, and working state need to stay available the whole time, so it can pick back up exactly where it left off.

Agents working beyond software development use cases also need to execute code and produce artifacts others can use. An agent helping a team plan inventory might read sales datasets and supplier PDFs, run Monte Carlo simulations of demand and delivery delays, and produce reports recommending stock levels. To do that work, it needs an isolated sandbox to install dependencies and execute code that inspects results and generates reports for analysis. The datasets, scripts, and reports must outlive the session that created them, so a teammate can review the recommendations or another agent can update the analysis as new data arrives.

A traditional VM provides an empty computer, and leaves developers to build the environment and APIs that agentic workflows desperately need to get work done. Developers are forced to invest in plumbing work to preserve the agent’s context, persist artifacts and keep them accessible beyond the agent that created them, coordinate parallel work, and security-hardened access to tools. Keeping spare VMs running helps agents start quickly but adds idle cost; provisioning and configuring capacity on demand can take minutes, slowing work. Billing for provisioned CPU also continues while agents wait for model responses, tool results, or human approval. Time spent making VMs work for agents is time developers could spend making those agents better at the work customers care about.

Agentic work needs infrastructure built for it: security hardened code execution, persistent sessions, fast startup, and governed tool access. Checkpointing and forking let that work branch, pause, and continue across devices and teammates. Active CPU billing keeps cost tied to actual consumption. Designed as purpose-built primitives for agents rather than adapted from general purpose virtual machines, Managed Agents lets developers focus on what matters most: making agents capable of more valuable work.

DigitalOcean Managed Agents: Scale agentic work with purpose-built computing

Managed Agents brings together two services vertically integrated to deliver a great agentic experience.

DigitalOcean Harness Runtime combines the functionality of a lightweight microVM, built-in tools like chromium and a coding sandbox needed by agents to do work. The product also offers rich lifecycle APIs that persist conversational history and working state across sessions, along with pause/resume/fork semantics so that developers can control costs and adapt workflows to the nonlinear quirks of agentic work.
DigitalOcean Action Gateway gives agents governed access to 16,000+ tools through a single managed MCP endpoint. This includes tool integrations, like Web Search, Web Fetch, Browser Automation, and DigitalOcean infrastructure management APIs, along with connectors for widely used platforms like GitHub, HubSpot, Stripe, Snowflake, Box, Supabase, Exa and more. Teams can also extend the catalog with their own MCP servers and internal tools.

Together, they let developers scale the work their agents can do while DigitalOcean manages the execution, persistence, tool access, and infrastructure underneath. Let’s dive a bit deeper into each of these new services, their capabilities and how they enable you to scale agentic work in the cloud.

DigitalOcean Harness Runtime: Sessions that outlive your laptop

Harness Runtime gives agents a durable cloud workspace where they can execute code, work with artifacts, and continue across devices and teammates. It manages the compute, storage, and session lifecycle, so developers can run agents in parallel, explore different approaches, and return to ongoing work without reconstructing the environment or context. The runtime provides these critical capabilities these agents need:

Isolated execution with Firecracker microVMs. Each session runs inside a dedicated Firecracker microVM with its own compute resources and filesystem. Hardware virtualization isolates the environment where agents install dependencies, execute generated code, and run background processes.
Execution and Access APIs. Use exec to run commands, launch tests, and inspect the session’s environment. Security hardened port forwarding lets developers preview applications and connect to services running inside the session without exposing them publicly.
Pause and resume with snapshot storage. Pausing captures the session’s working state so it can resume with its files, processes, and context intact. CPU and memory charges stop while the session is paused; retained storage remains billable. Harness Runtime also supports auto-pausing agents when they are idle as measured by no outgoing LLM or tool calls.
Parallel sessions and subagent workflows. Run subagents, or launch separate sessions across repositories and tasks. APIs are packaged as skills for each supported harness so that your agents can spawn work effortlessly for scenarios like divide and conquer, collaboration and map/reduce.
Visibility into every run. Structured events capture tool calls, model requests, and file operations. Inspect token usage and approval activity, and monitor session logs and metrics to debug runs, audit actions, and build evaluations from real agent work.

Use coding harnesses such as Claude Code, Codex CLI, and OpenCode, general-purpose agents such as Hermes, or agents built with LangGraph. You can also package a custom agent as a standard OCI container image and turn it into a reusable environment template, bringing your dependencies, tools, and configuration without rebuilding around a DigitalOcean-specific harness.

DigitalOcean Action Gateway: governed access to tools for agents to do real-world work

An agent resolving a production issue might inspect a repository, read a ticket, query a database, and notify the team. Each step requires access to another system. Connecting those tools individually leaves developers managing authentication, permissions, retries, and monitoring across every integration. Action Gateway brings that work behind a single managed MCP endpoint, giving agents governed access to 16,000+ tools across 500+ providers. Connect your services such as GitHub, HubSpot, Stripe, Snowflake, PagerDuty, Box, Supabase, and Exa, alongside web search, browser automation, code execution, and your own MCP servers.

Keep credentials outside the agent’s environment. Credentials are brokered at execution time and never reach the model or sandbox. Connect tools using API keys, shared OAuth applications, or per-user OAuth. When authorization is needed during a workflow, the gateway provides a sign-in link and resumes the call once authorization is complete.
Control which actions agents can take. Centralized customer permissions define the tools and actions available to each agent. Require human approval for sensitive operations, so agents can work autonomously within the boundaries your team sets.
Handle tool traffic as workloads grow. Built-in rate-limit management, retries, backoff, and timeouts help keep workflows moving as more agents call external systems.
Find the right tools without overwhelming the model. Action Gateway surfaces relevant, approved tools for each task without loading the entire catalog into context. Based on our own internal testing, Action Gateway helped match the agent’s intent to a tool’s capabilities with 99.3% accuracy, even when our requests used different wording from the tool’s name or description. These results are far more accurate than conventional lexical tool searches, and helped yield faster tool access overall.

Action Gateway also works with MCP-compatible applications beyond Harness Runtime. Add its endpoint to your application’s MCP configuration to access the tools you’ve connected, with the same centralized permissions and controls

Pricing: Superior economics grounded in actual consumption

Agents work in bursts. They compile code and run tests, then wait for model responses or external tools. Harness Runtime’s CPU billing follows actual CPU consumption, so when an agent is waiting and consuming no CPU, its CPU charge falls to zero.

For example, a session with two vCPUs averaging 25% CPU utilization and a measured memory peak of 4 GB throughout an hour would cost $0.060 in CPU and memory charges, compared with $0.126 for a full hour of that allocated capacity. Storage, inference, and separately metered tools are additional. Pausing a session stops CPU and memory charges while preserving its stored state. Action Gateway adds first-party tools that require a sandbox using Harness Runtime’s compute and memory rates, while third-party tools follow their published per-use pricing.

Performance

Fast startup and resume reduce the tradeoff between responsive agents and idle infrastructure cost. When a coding agent needs an execution environment before it can begin, provisioning delays become part of the user’s wait. When that environment sits idle between tasks or while awaiting human input, keeping it running preserves responsiveness at a cost. Pausing preserves its working state; fast resume makes that state useful again quickly.

The importance of latency depends on where it occurs and how often it repeats. Startup can delay the first answer. Resume can delay the next interaction. Repeated environment transitions can reduce how much exploration or testing an agent completes within a fixed time budget. Our goal is to minimize the time agents spend waiting for infrastructure and make it practical to pause idle sessions.

That is why we measure both runtime readiness and the time to an actual agent response. Through each provider’s public API, we run the same coding agent against the same model through session creation, a first answer, pause, resume, and a second answer.

A fast startup time gets agents to useful work sooner. Create → agent response measures the full journey from a session creation request to a completed agent reply, including provisioning the microVM, starting the harness, and completing a model turn. Harness Runtime becomes ready in 886 milliseconds and delivers the first response in 3.3 seconds in this benchmark. Measuring both makes the infrastructure overhead visible alongside the wait a user actually experiences.

A faster resume makes pausing practical. Developers should be able to pause idle sessions without making the next interaction feel like it’s starting all over. Harness Runtime resumes to readiness in 305 milliseconds. In this benchmark, a resumed session delivers an agent response in 2.43 secs, comparable to the 2.47 seconds measured for an already-running session. These results support using auto-pause to stop compute and memory charges between periods of work while preserving responsiveness when users return. Active-CPU billing addresses a different part of the lifecycle: avoiding CPU charges during model or tool waits when the running agent consumes no CPU.

Command execution is where we still have work to do. Run a command measures a command round trip inside an already-running session: 189 milliseconds for Harness Runtime versus 79 milliseconds for Sprites. Managed Agents routes exec through the DigitalOcean edge and Harness Runtime control plane, providing authentication, authorization, and audit trail. Our measured command path is 110 milliseconds slower. Reducing this overhead while preserving those controls remains a performance priority for us.

† Fly.io Sprites has no resume API - a sprite wakes on its first incoming request so these two figures are derived by removing one steady-state command round trip from its measured resume, not read directly from a resume call.

Source: DigitalOcean internal benchmark, 21 September 2026. Codex CLI in each provider’s native agent mode against gpt-5.5, driven through each provider’s public API from DigitalOcean droplets in RIC1. p50 across an identical number of journeys on every provider, with warm-up runs discarded. Sessions were requested at 2 vCPU / 4 GB on every provider; the Fly.io Sprites guest reported 8 vCPU / 16 GB. Agent CLI versions differed by provider (Managed Agents 0.154.0, Sprites 0.151.0).

Get started in seconds

From the CLI, starting a session looks like this:

# Authenticate with your DigitalOcean account
doctl auth init

# Start a session. --harness builds the manifest for you and
# prompts for your Anthropic key if it isn't already exported
doctl harness-runtime launch --harness claude-code --name my-first-agent

# You're dropped straight into a chat with the agent.
# Detach any time with Ctrl-D, then reattach later,
# from any device, right where you left off
doctl harness-runtime launch my-first-agent

Copy

From your code assistant, use this prompt to create an agent:

Set me up on DigitalOcean Managed Agents and leave me with a working agent.

Docs: https://docs.digitalocean.com/products/managed-agents/ — add index.html.md to any page for the markdown version. I have nothing installed or configured yet, so install doctl and get me authenticated. Never ask me to paste a token or any other secret into this chat.

Use this spec as written. It needs no model key and it attaches the tool catalog:

name: my-first-agent
agent: opencode
tools:
  - do.actions
permissions:
  default: ask

Then give it a job big enough to take a few minutes — a sourced brief on what shipped this week in AI, written to its workspace. Approve the tool calls for this first run so it can work unattended, and tell me that you did. Don't wait for it to finish: hand me back the commands to check on it, read the file, and pause it.

Copy
Unified observability: See what your agent did, in one place

Understanding an agent’s work should be as simple as starting a run. With DigitalOcean Insights (now in Private Preview), developers can follow a run across Harness Runtime, Action Gateway, and built-in tools in one place: what the agent executed, which tools it called, where it slowed down, and how it reached an outcome. There’s no need to piece together the story across tabs and vendors to understand what happened.

But improving agents requires learning from more than failures. Exceptional runs can reveal effective approaches worth reinforcing, just as unsuccessful runs expose behaviors worth correcting. And Signals (coming soon), will build on this visibility to help developers turn agent runs into feedback for evaluation and reinforcement learning. Together, Insights and Signals will help teams move from seeing what an agent did to understanding what made it effective, so every run becomes an opportunity to improve the next.

Built for teams already running agents

Qencode, a media processing company, built a support-triage agent on Harness Runtime. Before automating, their team spent hours every week manually triaging support requests across Slack, email and Intercom.

Today their agent reviews each incoming request, assesses urgency, sentiment and client revenue, and creates or updates the matching Jira ticket, flagging low-confidence cases for a team member to review. Early results suggest it’s saving the team an estimated 4 to 8 hours a week on triage and status reporting, while bringing response times down from several hours to nearly instant.

“It’s been a huge force-multiplier for our team. It gets the right ticket to the right person without anyone having to watch every thread themselves.” — Murad Mordukhay, CEO and co-founder, Qencode

DigitalOcean Managed Agents is now available in public preview. Bring your preferred harness, connect your tools, and give your agents the infrastructure to take on more work. Get started today.

About the author
DigitalOcean
Author

Share

Product Updates
Start building today
From GPU-powered inference and Kubernetes to managed databases and storage, get everything you need to build, scale, and deploy intelligent applications.
Sign up
Related Articles
Product updates
Prompt Caching is GA on DigitalOcean Serverless Inference: Up to 90% Off the Context Your Agents Resend
DigitalOcean
October 23, 2026
4 min read

Read more

Engineering
Building a computer that can pause and resume in milliseconds: Inside the MicroVM architecture behind Managed Agents

Braden Bassingthwaite

October 15, 2026
20 min read

Read more

Product updates
DigitalOcean Inference Router Enhancements: Performance Tuned Routing, No Rules to Write

DigitalOcean

October 13, 2026
4 min read

Read more

Company
About
Leadership
Blog
Careers
Customers
Partners
Referral Program
Affiliate Program
Press
Legal
Privacy Policy
Security
Investor Relations
Products
Managed Agents
Knowledge Bases
GPU Droplets
Bare Metal GPUs
Inference Engine
Data Services
Learning Services
Evaluations
Model Library
Droplets
Kubernetes
Functions
App Platform
Load Balancers
Managed Databases
Spaces
Block Storage
Network File Storage
API
Uptime
Cloud Security Posture Management (CSPM)
Identity and Access Management (IAM)
Cloudways
View all Products
Resources
Community Tutorials
Community Q&A
CSS-Tricks
Write for DOnations
Currents Research
DigitalOcean Startups
Wavemakers Program
Compass Council
Open Source
Newsletter Signup
Marketplace
Pricing
Pricing Calculator
Documentation
Release Notes
Code of Conduct
Shop Swag
Solutions
AI Training GPU
GPU Inference
VPS Hosting
Website Hosting
VPN
Docker Hosting
Node.js Hosting
Web Mobile Apps
WordPress Hosting
Virtual Machines
View all Solutions
Contact
Support
Sales
Report Abuse
System Status
Share your ideas
© 2026 DigitalOcean, LLC.
Sitemap.
This site uses cookies and related technologies, as described in our privacy policy, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences. Please visit our cookie policy for more information.
Agree & proceed
Decline all
Manage choices
Cookie Preferences
