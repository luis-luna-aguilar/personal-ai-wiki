---
title: Introducing Gemini Enterprise Agent Platform
type: source
source_type: article
url: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
fetched: 2026-04-23
---

# Introducing Gemini Enterprise Agent Platform

"Burns & McDonnell uses Agent Platform to transform how organizational knowledge is applied across the enterprise. Using ADK, we are building an AI agent that turns decades of project data into real-time, actionable intelligence. Agent Platform enables this innovation to scale responsibly by combining deterministic business rules with probabilistic reasoning — making AI a trusted operational capability, not just a productivity tool. With Agent Platform, we aren’t just managing knowledge; we are activating experience to drive faster, more confident decisions." **– Matt Olson, Chief Innovation Officer, Burns & McDonnell**

“Color Health uses Agent Platform to power our Virtual Cancer Clinic, delivering end-to-end care. By building our Color Assistant with the Agent Development Kit (ADK) and scaling it via Agent Runtime, we are helping more women get screened for breast cancer. The Color Assistant engages users to check screening eligibility, connects them to clinicians, and helps schedule appointments. The power of the agent lies in the scale it enables — helping us reach more people and respond to individual risk and eligibility in real time.” **– Jayodita Sanghvi, PhD., Head of AI Platform, Color**

“By rebuilding Comcast’s Xfinity Assistant with Agent Development Kit (ADK), we’ve moved beyond simple scripted automation to conversational generative intelligence that delivers personalized troubleshooting and self-service support to our customers. Agent Runtime has been a massive accelerator, allowing us to deploy a sophisticated multi-agent architecture that increases digital containment while ensuring secure, grounded interactions via Gemini. We aren't just reducing repeat interactions by solving customers’ issues the first time; we're redefining the customer experience at scale.” **– Rick Rioboli, Chief Technical Officer, Connectivity & Platforms, Comcast**

“Geotab uses Agent Platform to rapidly accelerate our AI Agent Center of Excellence. Google's Agent Development Kit (ADK) provides the flexibility to orchestrate various frameworks under a single, governable path to production, while offering an exceptional developer experience that dramatically speeds up our build-test-deploy cycle. For Geotab, ADK is the foundation that allows us to rapidly and safely scale our agentic AI solutions across the enterprise” **– Mike Branch, Vice President, Data & Analytics, GeoTab**

"Gurunavi uses Agent Platform to power 'UMAME!', an AI restaurant discovery app that leverages Memory Bank to achieve a deep understanding of user context. Unlike conventional prompt-based systems, our agent remembers a user's past actions and preferences to proactively present the best options. This eliminates the need for manual searches and creates a seamless experience that will improve user satisfaction by 30% or more. We view this memory function as a non-negotiable feature for the future of new culinary experiences.” **– Toshiaki Iwamoto, CTO, Gurunavi**

"At L'Oréal, Beauty Tech is not just a support function — it is a powerful catalyst to create the beauty that moves the world. To live up to that ambition, we decided to build our own proprietary Beauty Tech Agentic Platform, powered by Google Cloud. Leveraging Agent Development Kit (ADK), we are leading a fundamental shift: moving from deterministic workflow automation to autonomous, outcome-oriented agent orchestration. Our agents are not locked in a vacuum — through Model Context Protocol (MCP), they are securely connected to our single sources of truth, including our Beauty Tech Data Platform and core operational applications. Google Cloud gives us the resilience, the multi-LLM flexibility, and the enterprise-grade trust framework we need to scale this platform globally, while keeping human oversight at the center." **– Etienne BERTIN, Group CIO, L'Oréal**

“Payhawk uses Agent Platform to transform our AI agents from simple task executors into genuine financial assistants. By leveraging Memory Bank, we have moved from stateless interactions to long-term context retention. Our agents now act like dedicated team members, autonomously recalling user-specific constraints and history. For example, our Financial Controller Agent now remembers a user’s habits to auto-submit expenses, reducing submission time by over 50%. This shift allows our agents to anticipate needs based on past behavior rather than just reacting to prompts.” **– Diyan Bogdanov, Principal Applied AI Engineer, Payhawk**

"PayPal uses Agent Platform to rapidly build and deploy agents in production. Specifically, we use Agent Development Kit (ADK) and visual tools to inspect agent interactions, and manage multi-agent workflows. This provides the step-by-step visibility we need to visualize the flow of intent and payment mandates. Finally, Agent Payment Protocol (AP2) on Agent Platform provides the critical foundation for trusted agent payments. helping our ecosystem accelerate the shipping of secure agent-based commerce experiences." **– Nitin Sharma, Principal Engineer, AI, PayPal**

### Build AI agents

Build agents quickly and easily by empowering your developers, business users and everyone in between to build and deploy agents at scale.

**Build smarter agents, faster**

* **A major upgrade to ADK:** More than six trillion tokens are processed monthly on Gemini models through [ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk). Unlock more powerful reasoning by organizing agents into a network of sub-agents. This new, graph-based framework allows you to define clear, reliable logic for how agents work together to solve complex problems.
* **Workspaces are secure-by-design:** Give agents a hardened, sandboxed environment to run bash commands and manage files safely, isolated from your core systems.
* **Multimodal streaming:** Bring human-like stability to real-time interactions with multimodal support for live audio and video cues.

**Connect your agents to the enterprise**

* **Securely access any system:** Use plug-and-play architecture with Native Ecosystem Integrations to connect agents to your internal data and tools without custom coding.
* **Automate background operations:** Activate your data in BigQuery and Pub/Sub with Batch & Event-driven agents. This way, you can run massive, asynchronous tasks like content evaluation or data analysis in the background.

**Go from idea to production in hours**

* **Enable AI-driven development:** A programmatic interface for coding agents to access Google’s complete suite of agentic capabilities, allowing them to build, evaluate, and deploy production-ready agents on your behalf.
* **Bringing agent building directly to Agent Studio:** Now, you can move seamlessly from building simple prompts to deploying complex agents in [Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/overview). Once you're ready for deep customization, export your logic directly into ADK to continue development in a full-code environment.
* **Get a head start with pre-built agents:** Access a curated set of agent templates in [Agent Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden) — including code modernization, financial analysis, economic research, invoice processing, and more — that serve as immediate building blocks for your multi-agent systems.

### Scale AI agents

To move from a proof-of-concept to a live environment, you need a platform that can handle the performance, state, and security requirements of real-world work. 

**Powering high-performance agent execution**

* **The latest Agent Runtime:** Our revamped [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime) delivers sub-second cold starts and allows you to provision new agents in seconds.
* **Support for multi-day workflows:** You can now deploy long-running agents that run autonomously for days at a time. This allows your agents to manage complex, multi-step workflows and deep reasoning tasks that require extended persistence, like managing a sales prospecting sequence.
* **Autonomous action with security-by-design environments:**[Agent Sandbox](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-overview) provides a hardened environment to safely execute model-generated code and perform computer use tasks like browser-based automation without risk to your host systems.
* **Agent-to-agent orchestration:** Enables agents to seamlessly delegate tasks to one another, including support for complex, generative, and deterministic orchestration patterns. This ensures that for critical flows such as compliance, your agents follow well-specified paths every time.

**Move beyond temporary session data to high-accuracy context**

* **Personalize interactions:** [Agent Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) dynamically generates and curates long-term memories from conversations. Using new Memory Profiles, agents can recall high-accuracy details with low latency, ensuring context is never lost.
* **Link AI interactions to your existing records:** Store and manage history using [Agent Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions). With Custom Session IDs, you can use your own unique identifiers to track sessions and map them directly to your internal database and CRM records.
* **Enable real-time, human-like interactions:** Using the WebSocket protocol for Bidirectional Streaming, you can help ensure your agents are highly responsive during live customer or employee interactions, processing audio and video without lag.

### Govern AI agents

Govern with a secure-by-design architecture that applies enterprise rigor to every agent in your fleet – from the ones you build on Agent Platform to the ones you source from our partner ecosystem.

**Manage all of your agents through a single source of truth for identity and access.**

* **Assign every agent a verifiable identity:** [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) improves the security posture of your agents by ensuring every agent receives a unique cryptographic ID. This creates a clear, auditable trail for every action an agent takes, mapped back to defined [authorization policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity).
* **Maintain a central library of approved tools:** Our new [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry) provides a single source of truth for your enterprise. It indexes every internal agent, tool, and skill, simplifying discovery and ensuring only governed, approved assets are available to your users.
* **Manage your agent fleet from one control point:** [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) acts as the air traffic control for your agent ecosystem. It provides secure, unified connectivity between agents and tools across any environment, while enforcing consistent security policies and [Model Armor](https://cloud.google.com/security/products/model-armor?e=48754805&hl=en) protections to safeguard against prompt injection and data leakage.

**Use AI-powered insights to detect hidden risks and suspicious behavior before they impact your business.**

* **Detect suspicious behavior in real-time:** Agent Anomaly Detection uses statistical models and an LLM-as-a-judge framework to flag unusual reasoning. This works alongside [Agent Threat Detection](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-security-findings)to provide visibility into malicious activity, such as reverse shells or connections to known bad IP addresses.
* **Uncover vulnerabilities automatically:** A new [Agent Security](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-security-findings) dashboard, powered by [Security Command Center](https://cloud.google.com/security/products/security-command-center), unifies threat detection and risk analysis. It allows your teams to map relationships between agents and models, automate asset discovery, and scan for vulnerabilities in the underlying operating system and language packages.

### Optimize AI agents

Agent Platform gives you the visibility needed to understand how your AI is performing, making it easy to refine their logic and get smarter over time.

**Test your agents before they ship**

* **Simulate realistic conversations:** Use [Agent Simulation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-simulated) to test agents against human-like synthetic user interactions and virtualized tools in a controlled environment. Agents are automatically scored based on task success and safety across multi-step conversations.

**Monitor and improve in production**

* **Track live performance:** Use [Agent Evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation) to continuously score agents against live traffic using multi-turn autoraters that can evaluate the logic of an entire conversation, not just a single response. With turnkey dashboards and [Agent Observability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview), you can visually trace complex reasoning to debug issues as they happen.
* **Automate agent refinement:** Instead of manually digging through logs, [Agent Optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent) automatically clusters real-world failures and suggests refined system instructions to improve accuracy.

Detailed technical guides and a full list of updates are available in our updated [**documentation**](https://docs.cloud.google.com/gemini-enterprise-agent-platform)and [**release notes**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes). [Agent Platform](http://cloud.google.com/products/gemini-enterprise-agent-platform) is the new standard for enterprise agent development, built to help you move from experimentation to production-scale impact, starting today.
