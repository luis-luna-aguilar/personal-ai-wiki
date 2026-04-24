# Agentic Infrastructure and Operations: A Comprehensive Research Report on Production-Grade AI SRE Tooling

*Disclaimer: The information provided in this report is for informational purposes only and does not constitute professional, financial, or safety-critical engineering advice. Integrating autonomous AI agents into production infrastructure carries severe operational, financial, and security risks. Removing human-in-the-loop approval gates from state-mutating actions can lead to catastrophic system failure, data loss, and security breaches.*

**Key Points:**
*   **A Paradigm Shift:** Infrastructure agents are rapidly evolving from simple text generators (e.g., writing Infrastructure-as-Code) to active, telemetry-integrated participants in live production environments, fundamentally altering Site Reliability Engineering (SRE) workflows.
*   **The Rise of Protocol Standardization:** The Model Context Protocol (MCP) and Agent2Agent (A2A) protocol have become the de facto standards for connecting Large Language Models (LLMs) securely to operational tools and multi-agent systems, moving the industry away from fragile, custom-built API wrappers.
*   **Safety Demands Determinism:** Research indicates that LLMs cannot reliably enforce their own guardrails. Consequently, a new class of deterministic, compiled-language policy engines (such as Agent RuleZ and Skyflo) has emerged to strictly govern agent mutations in production.
*   **Sandboxed Execution is Mandatory:** Executing agent-generated code or remediation scripts directly on host infrastructure presents unacceptable operational and security risks. The industry is adopting microVMs and strict container isolation to securely sandbox agent actions.

The integration of artificial intelligence into infrastructure operations has moved past the experimental phase of generating Dockerfiles and Terraform scripts. Modern platform engineering teams are actively deploying autonomous and semi-autonomous agents directly into their observability and control planes. This report provides an exhaustive analysis of the concrete tools, frameworks, open-source repositories, and operating methods that enable agents to maintain, monitor, diagnose, and safely update infrastructure in real-world environments. While current systems show immense promise in reducing Mean Time to Resolution (MTTR) and operational toil, the evidence heavily leans toward maintaining human-in-the-loop approval gates for all mutating actions. This document is designed to guide the architecture of agentic DevOps stacks, providing highly specific, implementation-level research.

## Executive Summary

The transition from traditional DevOps automation to "Agentic DevOps" represents a paradigm shift from deterministic, script-based pipelines to intelligent, context-aware systems capable of reasoning over dynamic production states [cite: 1, 2]. However, placing agents into real infrastructure introduces novel risks; an agent capable of diagnosing a misconfigured load balancer is theoretically capable of deleting it. Therefore, the most significant advancements are occurring within the "harness" or "control plane" layers that surround LLMs, providing identity access management (IAM), execution sandboxes, and audit trails [cite: 3, 4]. 

To directly address the operational needs of modern engineering teams, this report concludes with the following definitive architecture and tooling recommendations:

*   **Recommended Technology Stack (Small Teams):** To minimize overhead, small teams should rely on lightweight, low-friction tools. The optimal stack includes **IncidentFox** for chat-based alert triage [cite: 5], **K8sGPT CLI** for rapid Kubernetes diagnostics [cite: 6], **GitHub Agentic Workflows** combined with **Agentic Terraform** for automated IaC maintenance [cite: 7, 8], **Daytona** for local execution sandboxing [cite: 9], and **Checkly** for post-deployment synthetic monitoring [cite: 10, 11].
*   **Recommended Technology Stack (Large/Enterprise Teams):** Enterprises require defense-in-depth and unified telemetry. The optimal stack centers around **Kagent (Solo.io)** as the secure control plane [cite: 12, 13], **AURA (Mezmo)** for incident context orchestration [cite: 14, 15], deterministic policy enforcement via **Agent RuleZ** and **Skyflo** [cite: 4, 16], strict hardware-level execution sandboxes via **E2B** or **Northflank** [cite: 9, 17], and continuous internal cluster verification via **Kuberhealthy** [cite: 18, 19].
*   **Top Open-Source Repositories:** Engineers must study `kagent-dev/kagent` for Kubernetes-native orchestration [cite: 13], `mezmo/aura` for RAG-driven incident context [cite: 14], `incidentfox/incidentfox` for chat-first debugging [cite: 5], `skyflo-ai/skyflo` for human-in-the-loop deployment safety [cite: 4], and `SpillwaveSolutions/agent_rulez` for sub-10ms deterministic policy enforcement [cite: 16].
*   **Key Operational Patterns:** The industry standard for agentic operations involves four core patterns: 1) The "Platform is Slow" automated Root Cause Analysis loop [cite: 20, 21], 2) Agent-Assisted IaC Upgrades using PseudoRAG [cite: 7], 3) Agent-Driven Canary Analysis using multi-model voting [cite: 22, 23], and 4) Observability-Integrated Agents heavily relying on the Model Context Protocol (MCP) and Agent2Agent (A2A) standards [cite: 24, 25].
*   **Finalized Wiki Recommendations:** Organizations must immediately establish a "Tri-State Execution Model" (Read-Only, Propose-Only, Mutate-with-Approval) [cite: 26, 27]. Internal documentation must mandate the deprecation of custom API wrappers in favor of MCP [cite: 15], explicitly ban the execution of agent-generated scripts on primary host environments, mandate microVM sandboxing for production tasks [cite: 9, 17], and define a strict division of labor where humans retain sole authority over state-mutating execution gates [cite: 4].

```json
{
  "concept": "A conceptual schematic illustrating the 'Tri-State Execution Model' for Agentic Infrastructure. It shows the strict boundary between read-only diagnosis, propose-only actions, and fully sandboxed mutating actions, connected by a central policy engine.",
  "reasoning_for_value": "The report heavily emphasizes safety and the necessity of isolating agent capabilities based on risk. A visual architecture diagram simplifies the complex interaction between observability tools, agents, policy engines, and execution environments, helping engineers immediately grasp how to architect a safe agentic deployment.",
  "title": "Architectural Blueprint for Safe Agentic Infrastructure Operations",
  "visual_type": "Schematic Architecture Diagram",
  "generation_method": "IMAGE",
  "justification_of_choice": "An IMAGE generation is superior to CODE here because the visual relies on abstract architectural zones, interconnected nodes, and conceptual boundaries (e.g., 'sandboxed microVMs', 'human approval gates') rather than plotting precise numerical data. Standard charts cannot convey system architecture, and building a complex CSS layout for a generic diagram is less effective than a tailored, stylistic schematic illustration.",
  "caption": "The Tri-State Execution Model strictly separates agent capabilities into Read-Only, Propose-Only, and Act tiers, utilizing deterministic policy engines and isolated microVM sandboxes to prevent catastrophic production mutations.",
  "data_specification": {
    "source_snippets_ids": [77, 21, 17],
    "data_structure": "Conceptual mapping of text to visual elements.",
    "mapping": "Left column: Observability Data (Logs, Metrics). Middle column: Agent Reasoning Engine. Right column: Three distinct output tiers. Tier 1 (Green): Read-Only. Tier 2 (Yellow): PR/Ticket Creation. Tier 3 (Red): Execution via Policy Engine (Agent RuleZ) -> Human Approval Gate (Skyflo) -> Firecracker MicroVM Sandbox (E2B)."
  },
  "design_and_interaction": {
    "layout": "A horizontal, three-stage flow diagram. Data flows from left (Sources) to center (Agent) to right (Execution Tiers). The Execution column must be split into three vertically stacked, color-coded zones.",
    "aesthetics": {
      "style": "Technical & Schematic. Clean lines, isometric perspective on the sandbox elements, and high-contrast typography.",
      "color_palette": "Background: #FFFFFF. Agent Engine: #1A73E8. Read-Only Zone: #81C995. Propose Zone: #FCC934. Mutate Zone: #D93025. Policy Engine: Near-Black #111111.",
      "additional_details": "Use clear, bold icons to represent databases, Kubernetes clusters, and human operators."
    },
    "interactivity": "Static visual with no interactivity.",
    "animation": "No animation."
  }
}
```

## Core Foundational Concepts for Agentic SRE

To navigate the tools and workflows detailed in this report, one must first understand the fundamental protocols and algorithms powering them.

*   **Agent2Agent (A2A) Protocol:** 
    *   *Definition:* An open communication standard launched by Google and housed by the Linux Foundation designed to allow AI agents to securely discover each other, exchange information, and delegate tasks across different frameworks using structured JSON over HTTP/S [cite: 25, 28, 29].
    *   *Analogy:* Think of A2A as the TCP/IP or universal translator for AI agents.
    *   *Operational Relevance:* It breaks down agent silos. An observability agent that detects a memory leak can use A2A to seamlessly hand off the exact technical context to a completely different infrastructure agent responsible for scaling up the cluster, without requiring custom API glue [cite: 29, 30].
*   **Meta's Prophet Algorithm:**
    *   *Definition:* An open-source procedure designed by Meta for forecasting time-series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality.
    *   *Analogy:* It acts like an intelligent weather forecaster for server load, knowing that traffic always surges at 9 AM on Mondays.
    *   *Operational Relevance:* Used by AI agents to drastically reduce alert fatigue. Instead of firing an alert every time CPU spikes, agents use Prophet to determine if the spike is an expected seasonal pattern or a genuine anomaly [cite: 5].
*   **PseudoRAG:**
    *   *Definition:* A lightweight retrieval technique that utilizes simple term frequency–inverse document frequency (tf-idf) classification to quickly map user intents to specific documentation snippets, bypassing the need for complex, heavy vector databases [cite: 7, 31].
    *   *Analogy:* Like a librarian quickly checking an index card cabinet to find an exact book aisle, rather than reading every book in the library.
    *   *Operational Relevance:* Allows agents writing infrastructure-as-code to rapidly and cost-effectively retrieve the exact, up-to-date syntax for a specific Terraform provider clause during automated upgrades [cite: 7].

## The Tool Landscape by Category

To build a practical agentic operations stack, it is essential to distinguish between the various layers of the ecosystem. The following categories encapsulate the current open-source and commercial landscape, transitioning from foundational observability to active remediation.

### 1. Agent Runtimes and Orchestration Frameworks
Agent runtimes provide the foundational infrastructure for deploying, scaling, and managing AI agents within cloud-native environments. Unlike generic frameworks (like LangChain or AutoGen), these tools are purpose-built to run inside infrastructure like Kubernetes.

**Kagent (Solo.io)**
*   **What it does:** A Kubernetes-native framework for deploying and orchestrating AI agents, featuring an API server, controller, and UI [cite: 12, 13].
*   **Relevance to SRE/DevOps:** Integrates agents natively into cloud architecture, handling agent identity, Role-Based Access Control (RBAC), and standardizing on the Agent2Agent (A2A) protocol and Model Context Protocol (MCP) for secure, vendor-independent communication [cite: 3, 12, 25].
*   **License/Type:** Open Source (Apache 2.0) / CNCF Sandbox [cite: 13, 32].
*   **Lifecycle Stage:** Orchestration, Remediation, Operations.
*   **Strengths:** Highly scalable; utilizes standard Kubernetes primitives (Custom Resource Definitions); provides "agent-on-behalf-of" granular access semantics [cite: 3, 13].
*   **Limitations:** Heavily focused on Kubernetes environments [cite: 12, 13].
*   **Implementation Complexity:** High. Requires deep knowledge of Kubernetes operators and cluster management [cite: 3, 13].
*   **Current Price/Cost:** Free (Open Source).
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Unsuitable for small teams operating purely on serverless functions or legacy bare-metal servers without Kubernetes [cite: 12].
*   **Link(s):** [github.com/kagent-dev/kagent](https://github.com/kagent-dev/kagent) [cite: 33].

**AURA (Mezmo)**
*   **What it does:** The AI Universal Rigging Agent (AURA) is a Rust-based agentic harness that acts as a "System of Context," managing MCP tool integrations and workflows via declarative TOML (Tom's Obvious, Minimal Language) files [cite: 14, 15, 34].
*   **Relevance to SRE/DevOps:** Solves the "context problem" during incident response by intelligently assembling logs, metrics, and runbooks into coherent RAG pipelines tailored for specific alerts [cite: 14, 35].
*   **License/Type:** Open Source (Apache 2.0) / Open Core [cite: 15, 36].
*   **Lifecycle Stage:** Triage, Diagnosis, RCA.
*   **Strengths:** Memory-safe Rust execution; extremely low latency; automatic schema sanitization for various LLM providers [cite: 14, 15].
*   **Limitations:** Ecosystem is relatively nascent compared to mature orchestration platforms [cite: 36].
*   **Implementation Complexity:** Moderate. Requires understanding of TOML configurations and RAG architecture [cite: 15, 34].
*   **Current Price/Cost:** Free (Open Source core); Commercial pricing for enterprise features.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Teams without dedicated observability pipelines will struggle to feed AURA enough context to be useful [cite: 14].
*   **Link(s):** [github.com/mezmo/aura](https://github.com/mezmo/aura) [cite: 14].

### 2. Incident Investigation and Root-Cause Analysis (RCA) Systems
These systems monitor incoming alerts, autonomously query infrastructure for context, and synthesize findings into actionable reports.

**IncidentFox**
*   **What it does:** An AI SRE platform residing natively in collaboration tools like Slack or Teams, utilizing multi-agent orchestration to investigate alerts [cite: 5, 37].
*   **Relevance to SRE/DevOps:** Acts as a tireless first responder. It uses Meta's Prophet for seasonality-aware anomaly detection and employs RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval) to maintain context across lengthy incident runbooks [cite: 5, 38].
*   **License/Type:** Open Source (MIT License) [cite: 5, 37].
*   **Lifecycle Stage:** Monitoring, Triage, RCA.
*   **Strengths:** Excellent alert noise reduction (up to 95%) via temporal and topological correlation; accessible directly via chat [cite: 5].
*   **Limitations:** Confined primarily to chat interfaces, which can become cluttered during massive, multi-system outages [cite: 5].
*   **Implementation Complexity:** Low. Can be deployed via Docker and connected to standard APIs quickly [cite: 5].
*   **Current Price/Cost:** Free.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Unsuitable for teams that require strict, asynchronous, ticket-driven incident management without relying on synchronous chat tools [cite: 5].
*   **Link(s):** [github.com/incidentfox/incidentfox](https://github.com/incidentfox/incidentfox) [cite: 5].

**Aurora (Arvo AI)**
*   **What it does:** An automated incident investigation agent orchestrated via LangGraph that dynamically selects tools to query multi-cloud infrastructures [cite: 39, 40].
*   **Relevance to SRE/DevOps:** Executes CLI commands in sandboxed pods and traverses dependency graphs specifically to narrow down root causes across AWS, Azure, GCP, or Kubernetes [cite: 40].
*   **License/Type:** Open Source (Apache 2.0) [cite: 39, 40].
*   **Lifecycle Stage:** Triage, Diagnosis, RCA.
*   **Strengths:** Extensive built-in tool library (30+ integrations); strong focus on multi-cloud environments [cite: 40].
*   **Limitations:** Explicitly focused only on investigation, offering no capabilities for remediation or full incident lifecycle management [cite: 41].
*   **Implementation Complexity:** Moderate. Requires configuring LangGraph nodes and cloud permissions [cite: 40].
*   **Current Price/Cost:** Free.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Teams looking for an agent that can actively execute fixes should avoid Aurora [cite: 41].
*   **Link(s):** [github.com/arvo-ai/aurora](https://github.com/arvo-ai/aurora) (Based on general repository structure for Aurora).

**OpenSRE (Tracer-Cloud)**
*   **What it does:** A customizable framework for building AI SRE agents with connections to over 60 tools across the modern cloud stack [cite: 42, 43].
*   **Relevance to SRE/DevOps:** Allows platform teams to define highly bespoke investigative workflows using a wide variety of integrations [cite: 43].
*   **License/Type:** Open Source [cite: 42, 43].
*   **Lifecycle Stage:** Triage, Diagnosis.
*   **Strengths:** High flexibility and extensive integration list [cite: 43].
*   **Limitations:** Requires significant configuration to build effective workflows [cite: 43].
*   **Implementation Complexity:** High.
*   **Current Price/Cost:** Free.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Small teams wanting an out-of-the-box, opinionated RCA tool will find OpenSRE too laborious to configure [cite: 43].
*   **Link(s):** [github.com/tracer-cloud/opensre](https://github.com/tracer-cloud/opensre) [cite: 42].

### 3. Infrastructure Diagnostics and Operations Tools
These tools serve as the specialized "skills" that broader agents utilize to understand specific infrastructure domains.

**K8sGPT**
*   **What it does:** Scans Kubernetes clusters and translates complex diagnostic data into plain English explanations [cite: 6, 44].
*   **Relevance to SRE/DevOps:** Provides a critical MCP server that allows generic LLMs to securely query cluster state, pod logs, and resource metrics [cite: 6, 24].
*   **License/Type:** Open Source / CNCF Sandbox [cite: 6, 44].
*   **Lifecycle Stage:** Diagnosis, Monitoring.
*   **Strengths:** Built-in data anonymization strips sensitive information before sending telemetry to external LLMs; highly reliable [cite: 24, 44].
*   **Limitations:** Solely focused on Kubernetes; cannot diagnose external load balancers or non-containerized databases [cite: 6, 44].
*   **Implementation Complexity:** Low. Can be run locally as a CLI or installed as a lightweight cluster operator [cite: 6, 44].
*   **Current Price/Cost:** Free.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Completely irrelevant for organizations running applications directly on VMs or serverless platforms [cite: 6].
*   **Link(s):** [k8sgpt.ai](https://k8sgpt.ai/) / GitHub [cite: 6].

### 4. Deployment Safety and Policy Enforcement
Agents require strict boundaries. These tools act as the deterministic safety nets that catch hallucinations or prevent agents from executing destructive commands.

**Skyflo**
*   **What it does:** A self-hosted AI control layer for Kubernetes and CI/CD pipelines that bridges the gap between CLI assistants and fully autonomous bots [cite: 4].
*   **Relevance to SRE/DevOps:** Represents the gold standard for "Deployment Safety" by translating natural language intent into typed, auditable tool executions while strictly enforcing a human approval gate for *every* mutating operation [cite: 4, 45].
*   **License/Type:** Open Source (Apache 2.0) [cite: 4, 45].
*   **Lifecycle Stage:** Planning, Remediation, Deployment.
*   **Strengths:** Guarantees a deterministic control loop; provides a complete, immutable audit trail of agent actions [cite: 4, 45].
*   **Limitations:** Requires active human intervention, limiting true "zero-touch" autonomy [cite: 4, 45].
*   **Implementation Complexity:** Moderate to High.
*   **Current Price/Cost:** Free.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Unsuitable for use cases demanding millisecond-level autonomous remediation (e.g., algorithmic trading infrastructure) where human approval is too slow [cite: 4].
*   **Link(s):** [github.com/skyflo-ai/skyflo](https://github.com/skyflo-ai/skyflo) [cite: 4].

**Agent RuleZ (Spillwave Solutions)**
*   **What it does:** A deterministic, local-first AI policy engine built in Rust that intercepts and evaluates agent tool calls against human-readable YAML configurations [cite: 16, 46].
*   **Relevance to SRE/DevOps:** Proves that safety cannot be prompted into an LLM. It seamlessly blocks dangerous operations (like force-pushing or database deletion) at the API level in under 10 milliseconds [cite: 16, 46].
*   **License/Type:** Open Source (MIT) [cite: 46].
*   **Lifecycle Stage:** Governance, Policy Enforcement.
*   **Strengths:** Sub-10ms execution time; mathematically guarantees that restricted actions cannot execute [cite: 16, 46].
*   **Limitations:** Currently heavily scoped to Claude Code; requires manual mapping of organizational policies to YAML files [cite: 16].
*   **Implementation Complexity:** Moderate.
*   **Current Price/Cost:** Free.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Not useful as a standalone monitoring tool; it is strictly a middleware safety net [cite: 16].
*   **Link(s):** [github.com/SpillwaveSolutions/agent_rulez](https://github.com/SpillwaveSolutions/agent_rulez) [cite: 16].

### 5. Sandboxed Execution Environments
When agents require the ability to run generated code to process custom logs or execute temporary mitigations, they must do so in isolated environments to prevent container escapes or resource exhaustion.

**E2B**
*   **What it does:** Provides API-driven cloud infrastructure designed specifically to spin up Firecracker microVMs for AI agent code execution [cite: 9, 17].
*   **Relevance to SRE/DevOps:** Offers the ultimate dedicated kernel and hardware-level isolation. If an agent writes a malicious or infinitely looping script, the blast radius is confined to a disposable VM that boots in under 150ms [cite: 9, 17].
*   **License/Type:** Hybrid (Open source SDKs, proprietary cloud).
*   **Lifecycle Stage:** Diagnosis, Remediation, Operations.
*   **Strengths:** Sub-150ms boot times; purpose-built specifically for LLM workflows [cite: 9, 17].
*   **Limitations:** Relies on cloud-hosted infrastructure, raising data residency concerns [cite: 9, 17].
*   **Implementation Complexity:** Low (via provided SDKs).
*   **Current Price/Cost:** Pay-as-you-go per VM second.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Highly regulated environments (defense, strict finance) that legally require fully air-gapped, on-premise execution [cite: 9, 17].
*   **Link(s):** [e2b.dev](https://e2b.dev/)

**Northflank**
*   **What it does:** A comprehensive developer platform featuring robust compute primitives, including highly isolated sandboxed jobs [cite: 9, 17].
*   **Relevance to SRE/DevOps:** Offers secure, scalable execution for complex agent workloads that require advanced networking control and state management alongside isolation [cite: 9, 17].
*   **License/Type:** Commercial.
*   **Lifecycle Stage:** Remediation, Deployment.
*   **Strengths:** Enterprise-grade isolation; strong networking and identity control mechanisms [cite: 9, 17].
*   **Limitations:** Broader focus than just AI agents, potentially resulting in a steeper learning curve than dedicated agent tools.
*   **Implementation Complexity:** Moderate.
*   **Current Price/Cost:** Resource-based enterprise pricing.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Overkill for teams merely looking for a microscopic, single-purpose code execution endpoint [cite: 9].
*   **Link(s):** [northflank.com](https://northflank.com/)

**Daytona**
*   **What it does:** A Docker-container-based development environment manager that standardizes and isolates code execution [cite: 9].
*   **Relevance to SRE/DevOps:** Provides lightweight, accessible containerized sandboxing suitable for local agent execution and safe development testing [cite: 9].
*   **License/Type:** Open Source (with enterprise tiers).
*   **Lifecycle Stage:** Planning, Local Diagnosis.
*   **Strengths:** Runs seamlessly anywhere Docker runs; excellent developer experience [cite: 9].
*   **Limitations:** Docker container isolation is inherently weaker than Firecracker VM-level isolation, leaving it vulnerable to sophisticated container escape techniques [cite: 9].
*   **Implementation Complexity:** Low.
*   **Current Price/Cost:** Free (OSS), with Enterprise pricing available.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Unsuitable and highly dangerous for executing untrusted, LLM-generated code in a live production network due to container escape risks [cite: 9].
*   **Link(s):** [daytona.io](https://www.daytona.io/)

### 6. Post-Deployment Verification and Synthetic Monitoring
Agents must verify infrastructure changes *after* acting.

**Kuberhealthy**
*   **What it does:** A Kubernetes operator that runs synthetic monitoring checks and continuous process verification, exposing results directly as Prometheus metrics [cite: 18, 19].
*   **Relevance to SRE/DevOps:** Allows agents to programmatically verify that a cluster's internal components (e.g., DaemonSets, PVCs, DNS) are functioning properly after an infrastructure change [cite: 19, 47].
*   **License/Type:** Open Source (Apache 2.0) / CNCF Incubating [cite: 18, 19, 48].
*   **Lifecycle Stage:** Post-deploy validation, Synthetic Monitoring.
*   **Strengths:** Deeply integrated with Kubernetes primitives; highly customizable; native Prometheus integration [cite: 19, 47].
*   **Limitations:** Primarily focused on internal cluster health rather than external user journey monitoring [cite: 47].
*   **Implementation Complexity:** Moderate. Requires existing Prometheus stack and Kubernetes operational knowledge [cite: 19].
*   **Current Price/Cost:** Free.
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Should not be used by teams strictly seeking external, black-box user journey testing across global geographies [cite: 47].
*   **Link(s):** [github.com/kuberhealthy/kuberhealthy](https://github.com/kuberhealthy/kuberhealthy) [cite: 18].

**Checkly**
*   **What it does:** A developer-first synthetic monitoring and observability platform that runs Playwright-based browser tests and API checks via a Monitoring as Code (MaC) workflow [cite: 10, 11].
*   **Relevance to SRE/DevOps:** Provides agents with the ability to verify deployed web applications and APIs from the outside-in, validating that an infrastructure deployment didn't break real-world user flows [cite: 49, 50].
*   **License/Type:** Commercial / Hybrid (Uses OSS Playwright) [cite: 11, 49].
*   **Lifecycle Stage:** Synthetic Monitoring, Post-deploy validation.
*   **Strengths:** Monitoring as Code (MaC) support via Terraform/Pulumi; global edge execution from 20+ locations; unified API and browser testing [cite: 10, 11, 51].
*   **Limitations:** Can become expensive at high check frequencies; focused primarily on web/API layers rather than deep backend infrastructure state [cite: 11].
*   **Implementation Complexity:** Low to Moderate. Configured via standard JavaScript/TypeScript [cite: 49].
*   **Current Price/Cost:** Tiered (Free developer plan; paid team/enterprise tiers based on check volume) [cite: 51].
*   **Availability:** General Availability.
*   **Real-World Context (Anti-use cases):** Unsuitable for purely on-premise, air-gapped environments or strictly internal-only Kubernetes health checks [cite: 11].
*   **Link(s):** [checklyhq.com](https://www.checklyhq.com/) [cite: 51].

## Recommended Technology Stacks

The optimal tooling configuration depends heavily on the organizational size, operational maturity, and risk tolerance of the engineering team.

### Recommended Stack for a Small Engineering Team
Small teams generally lack dedicated platform engineers and require tools that offer immediate time-to-value with minimal maintenance overhead.

*   **Triage & Investigation:** **IncidentFox** deployed via Docker. By connecting directly to Slack and PagerDuty, developers gain an automated first-responder that correlates alerts and provides inline analysis without complex orchestration overhead [cite: 5].
*   **Kubernetes Diagnostics:** **K8sGPT CLI**. Installed locally, it provides rapid, plain-English explanations of pod failures [cite: 6, 44].
*   **Infrastructure as Code (IaC):** GitHub Agentic Workflows combined with **Agentic Terraform** [cite: 7, 8]. Automates provider upgrades and drift validation directly within the PR UI, relying on GitHub's native approval mechanisms [cite: 8, 27].
*   **Execution Sandbox:** **Daytona** (Docker-based) for local execution with strict scoped credentials [cite: 9].
*   **Post-Deploy Verification:** **Checkly** configured via Terraform for rapid, outside-in API and browser checks [cite: 11].

### Recommended Stack for a Larger Org with Platform/SRE
Enterprise organizations require defense-in-depth, strict RBAC, and unified telemetry. Their stack must treat agents as governed microservices.

*   **Agent Control Plane & Identity:** **Kagent (Solo.io)**. Running inside the enterprise Kubernetes cluster, Kagent manages agent lifecycles, injects secure identities, and routes tools through an MCP gateway [cite: 3, 52].
*   **Context & Orchestration:** **AURA (Mezmo)**. Handles complex RAG pipelines over historical incident data and normalizes MCP tool schemas across different LLMs [cite: 14, 15].
*   **Policy & Guardrails:** **Agent RuleZ** and **Skyflo**. Agent RuleZ evaluates micro-actions in milliseconds [cite: 16], while Skyflo acts as the macro-level governor, ensuring generated manifests pause for human review [cite: 4, 45].
*   **Sandboxed Execution:** **Northflank** or **E2B**. Hardware-level isolation (Firecracker microVMs) is mandatory to run agent-generated scripts securely [cite: 9, 17].
*   **Post-Deploy Verification:** **Kuberhealthy**. Runs continuous synthetic daemonsets to ensure internal cluster operations (like PVC provisioning) are healthy post-deploy [cite: 18, 19].

### Comparative Tooling Matrix

| Tool / Framework | Primary Category | Target Org Size | Key Differentiator | Anti-Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Kagent** | Orchestration | Enterprise | Native K8s integration; A2A protocol support | Non-Kubernetes environments |
| **AURA** | Incident Context | Mid to Enterprise | Blazing fast Rust execution; RAG over alerts | Teams lacking mature observability |
| **IncidentFox** | RCA / Triage | Small to Mid | Chat-first debugging; Meta's Prophet anomaly detection | Strict ticket-only workflows |
| **Skyflo** | Guardrails | All Sizes | Immutable audit trails; deterministic human-approval gates | High-frequency auto-remediation |
| **E2B** | Execution Sandbox | Enterprise | Sub-150ms Firecracker microVM boot times | Air-gapped / On-premise |
| **Checkly** | Synthetic Monitoring | Small to Enterprise | Monitoring as Code (MaC) using Playwright | Purely internal/backend checks |
| **Kuberhealthy**| Synthetic Monitoring | Mid to Enterprise | Deep K8s component testing via Prometheus metrics | External user journey testing |

## Patterns for Agent-Assisted Incident Response

Incident response is the most mature use case for operational AI. The goal is not necessarily autonomous mitigation, but extreme compression of the diagnostic timeline.

### The "Platform is Slow" Diagnosis Workflow
When a generalized symptom like high latency is reported, human engineers often struggle with "where to look first." An agentic workflow structures this elegantly:

1.  **Symptom Ingestion & Anomaly Verification:** The agent (e.g., IncidentFox) receives a webhook indicating elevated p95 latency. It immediately applies Meta's Prophet algorithm to confirm if this latency is a true anomaly or a known daily spike [cite: 5].
2.  **Topology Mapping & Correlation:** The agent queries the tracing backend (via an MCP connector) to build a dependency map of the failing service [cite: 5]. It correlates the latency spike against recent deployments and infrastructure changes [cite: 20, 53]. 
3.  **Telemetry Synthesis:** The agent dynamically adjusts log filtering, looking for corresponding error codes like OOMKilled (Out Of Memory Killed - a Kubernetes state where a pod is terminated for exceeding memory limits). Tools like K8sGPT fetch specific pod events [cite: 54, 55].
4.  **Hypothesis Generation & Triage:** The agent posts a summary in Slack: *"Latency anomaly detected in `checkout-service`. High confidence this is correlated to PR #402 deployed 15 minutes ago, which introduced a new database query. Associated logs show connection pool exhaustion."* [cite: 20, 21].
5.  **Postmortem Generation:** Once fixed, the agent parses the incident timeline, generates a structured postmortem artifact, and suggests new synthetic checks [cite: 8, 56].

## Patterns for Agent-Assisted Infra Maintenance and Upgrades

Infrastructure maintenance—such as updating Terraform providers or patching server OS layers—is notoriously toil-heavy.

### Automated Infrastructure-as-Code Upgrades
Upgrading a Terraform provider typically requires manually reading changelogs and running plans [cite: 8]. An agentic workflow automates this:

1.  **Detection:** A GitHub Agentic Workflow detects a new provider release [cite: 8].
2.  **Retrieval:** The agent uses PseudoRAG to rapidly retrieve specific upgrade guides and changelogs from the provider's registry based on tf-idf classification without needing a heavy vector database [cite: 7, 31].
3.  **Code Refactoring:** The agent scans `.tf` files, identifies deprecated syntax, and re-writes the blocks using few-shot prompting techniques [cite: 7, 8].
4.  **Dry-Run Validation:** The agent executes `terraform validate` and `terraform plan`. Crucially, it parses the JSON output. If the plan fails, it enters an internal retry loop, feeding the error back to the LLM to correct its own code [cite: 7].
5.  **Proposal:** The agent opens a Pull Request with the working code, attaching the `terraform plan` output as proof of safety [cite: 8].

## Patterns for Deployment Safety and Rollback

Deployment is the most dangerous phase of the software lifecycle. Agentic AI drastically improves the safety of advanced deployment strategies like Canaries.

### Agent-Driven Canary Analysis
A canary release incrementally exposes new code to a small percentage of users [cite: 23, 57, 58]. AI agents automate the intense monitoring required during this phase with higher fidelity than manual observation.

*   **Real-World Case Study:** Waze, utilizing Spinnaker's automated canary analysis (Kayenta) in conjunction with Google Cloud, successfully reduced incidents on their services by 25%. The system deploys a baseline and canary version, continuously executes handcrafted queries against Stackdriver/Prometheus, and automatically analyzes behavior before full promotion [cite: 59].

1.  **Traffic Routing & Telemetry Gathering:** An orchestration tool like Argo Rollouts routes 5% of traffic to the new pod. An AI Plugin begins continuously gathering logs and metrics from both the stable and canary versions [cite: 57].
2.  **Parallel Hypothesis Testing (Multi-Model Voting):** The agent analyzes logs for novel error codes. Advanced architectures use multi-model parallel analysis, where different LLM architectures (e.g., Claude 3.5 vs GPT-4o) independently "vote" on the health of the canary [cite: 22, 23, 57]. *Mechanism:* This explicitly increases confidence because it mitigates single-model hallucination or systemic bias. If one model hallucinates a pattern in the logs, a completely different model architecture is highly unlikely to hallucinate the exact same error, acting as a deterministic cross-check.
3.  **Automated Decisioning:** If an issue is detected, it issues an immediate rollback command via an MCP tool [cite: 23, 57]. If stable, it incrementally promotes. 
4.  **Version Control & Audit:** Systems like Co-one provide "AI Versioning," maintaining an immutable audit log of exactly *why* an agent decided to promote or rollback [cite: 60].

## Patterns for Observability-Integrated Agents

An agent is only as intelligent as the data it can access. Modern agents integrate deeply with observability pipelines.

*   **The Model Context Protocol (MCP) & A2A:** MCP has revolutionized agent observability by exposing operational data (Datadog, Prometheus) as standardized capabilities that any LLM can query natively [cite: 15, 24]. Concurrently, the A2A protocol ensures agents can share these findings with other specialized agents seamlessly [cite: 25].
*   **Tracing the Agent Itself:** Observability is a two-way street. Frameworks like Kagent and AURA emit OpenTelemetry (OTel) traces for every step the agent takes [cite: 3, 13, 14]. Engineers can view an agent's prompts, tool calls, and latency on the same tracing dashboards used for microservices [cite: 3, 14, 15, 61].
*   **Smart Log Sampling:** Because raw application logs easily exceed LLM token limits, observability-integrated agents utilize statistical analysis to sample logs intelligently, extracting the most relevant lines before sending them to the LLM [cite: 5].

## Guardrails, Permissions, and Approval Models

The most critical aspect of implementing agentic infrastructure is designing a secure architecture that controls the "blast radius" of rogue actions. 

### The Tri-State Execution Model
Organizations must strictly separate agent capabilities into three tiers:

1.  **Diagnose Only:** The agent is granted read-only access via scoped service accounts [cite: 26]. It can fetch logs and metrics but has no API permissions to mutate state.
2.  **Diagnose + Propose:** The agent has read-only infrastructure access but write access to a version control system (e.g., GitHub). It opens a Pull Request that requires human approval to merge [cite: 8, 22, 27].
3.  **Diagnose + Act:** The agent is granted active mutation rights. This is the highest risk tier and must be heavily governed.

### Enforcing Safety for "Diagnose + Act"
*   **Deterministic Policy Engines:** As demonstrated by Agent RuleZ, safety policies cannot simply be written into the LLM's system prompt [cite: 16, 46]. Policies must be evaluated deterministically by an external engine that intercepts the tool call *before* execution [cite: 16].
*   **Sandboxed Execution:** Throwaway code generated by agents must never run on the host system. Tools like E2B and Northflank utilize Firecracker microVMs to spin up isolated, ephemeral sandboxes with dedicated kernels in under 150 milliseconds [cite: 9, 17]. 
*   **Hard Approval Gates:** Frameworks like Skyflo enforce a mandatory "Human-in-the-Loop" architecture [cite: 3, 4]. The agent performs its diagnostic loop autonomously, but an `apply` or `delete` tool call triggers a Server-Sent Event (SSE) to a UI, pausing execution until a human explicitly clicks "Approve" [cite: 4, 45].

### Secrets Management and Credential Injection in Ephemeral Sandboxes
A critical "next logical question" when using ephemeral microVM sandboxes is how the agent securely authenticates to production environments to take action. Sandboxes must never contain hardcoded, long-lived credentials. Instead, modern agent architectures utilize dynamic, short-lived STS (Security Token Service) tokens. When a human approves an action via an engine like Skyflo, the control plane retrieves an ephemeral token strictly scoped to that exact task (e.g., "restart pod X"). This token is injected via environment variables directly into the microVM memory space at boot time and expires instantly upon the destruction of the VM, ensuring zero credential leakage.

## Gaps in the Market: What Still Needs to be Built

Despite rapid advancement, the agentic infrastructure landscape has notable deficiencies:

1.  **Standardized Evaluators for Operations:** The industry lacks a benchmark equivalent to SWE-bench (Software Engineering benchmark - a standard dataset for evaluating coding models) for infrastructure operations [cite: 43]. Evaluating whether an SRE agent correctly stabilized a cascading microservice failure across multiple AWS zones is incredibly difficult to simulate and score [cite: 43].
2.  **Stateful Environmental Memory:** Most agents currently treat incidents as isolated events. There is a lack of deep, stateful "institutional memory" where an agent learns the nuanced architectural quirks of an organization over months of operation [cite: 21, 62].
3.  **Cross-Cloud Mutating Standards:** While MCP standardizes data retrieval, taking action across disparate cloud providers still relies on brittle, provider-specific API calls. A unified, agent-native abstraction layer for cloud mutation does not yet exist.

## Clear Recommendation for What Our Wiki Should Add or Change

Based on this research, I recommend the following concrete updates to the internal wiki to bridge the gap between theoretical AI concepts and practical infrastructure operations:

1.  **Create an "Agentic Architecture Patterns" Section:** Move beyond simple "Prompt Engineering" guides. Add a module detailing the **Plan $\rightarrow$ Approve $\rightarrow$ Execute $\rightarrow$ Verify** loop used by production tools like Skyflo [cite: 45]. Document the "Sandwich Method" for deployment: Human initiates $\rightarrow$ Agent diagnoses and proposes $\rightarrow$ Human approves [cite: 63].
2.  **Standardize on MCP and A2A Protocols:** Update all internal integration guides. Deprecate custom API wrappers for LLMs. Mandate that all internal tools, runbooks, and telemetry endpoints expose their data via standard MCP servers [cite: 15, 24], and utilize Agent2Agent for multi-agent workflows [cite: 25].
3.  **Establish a Firm Policy on Execution Sandboxing:** The wiki must explicitly ban the execution of agent-generated scripts on primary host environments or CI runners. Mandate the use of Docker-based sandboxes (like Daytona) for local development, and strict Firecracker microVMs (like E2B or Northflank) for any production automation [cite: 9, 17].
4.  **Define the Division of Labor:** Create an explicit matrix in the wiki detailing roles:
    *   **Agents:** Responsible for triage, log parsing, dependency mapping, and drafting IaC PRs.
    *   **DevOps/Platform:** Responsible for authoring deterministic guardrail policies (Agent RuleZ YAMLs), building MCP servers, and managing Kagent RBAC configurations [cite: 12, 16, 52].
    *   **SRE/On-Call:** Responsible for reviewing RCA summaries and clicking "Approve" on mutating execution gates [cite: 4, 21].
5.  **Reference Implementation Guides:** Add step-by-step guides for deploying lightweight proofs-of-concept using the repos identified in this report (e.g., setting up K8sGPT for local clusters, routing Datadog alerts to IncidentFox, or running synthetic Playwright checks via Checkly) to encourage hands-on experimentation [cite: 5, 11, 44].

**Sources:**
1. [sourceforge.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu6YMosuKXwWyTY2tOs_pxHKeV0v_iOWjPWg2mZGdWSYix2vTPfz-ho3430SfcWDMjTIAU6oMBGeGKUJctgazh7HnuaPgQibkF0ObPY5R-m0TP4EGpSmYm72kUyzwv2KNVYSSLCeE=)
2. [super-agentic.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERj2Mp-asNjRXe6p0UMCIwj8L_S6Fp1gIg-mMbOvtLDLhJX_QOf9XKTIya30rW9F3K7fZOykX0bRZYyjlgvqY0joK32FpNK_whxWFz3kGO80HZP7x2BTH68xj6WCtO)
3. [solo.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkHZcVqFl1VoJV7vut6FOoa4dX3UlkskgYSQENK-reoA6qPmHRAWlC8FbbZ3kBdCZunqMa0fTLkrcPSUkw3itcZQxwgsXlJQ4UD7pAXke09PCt_kLqMwkPeg==)
4. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvCk1tMVVHTHS21VANX3c5r9okcBpjjZepxLkiBu1rm6btd88yxdG2VMmpcZAO0YYwmUvGwruLYtMSDhk5tZZaR8a89CS7ZVNw9g5xC2vcEdOU)
5. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3239pVzkAvMOlCs0ckStQHBsMqyRdHjvmRCxqQRhqrImrRHel_PlEYVUfQtJyxzcLr9SBunCJQU_-AjyvICIT3Sx7ypbxnCTN5PYoZVyfq0qp90eA9Injb5pFnGrZBhY=)
6. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3eBi5mRE9AMONUu1YTkjO8cfFZvz0dMKnUG3-69dw27YZTrBYUsbPnI6-mXL2owTiyd8u1oeEroMvkvbSRn3xxD0DJswsNL1NlBYIfvuouevjdSd6XtL0ng==)
7. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEiLJKA9QmCVE_wHFOJC1D___-dE47cG8gL_ZDWunIrqcCcpj03OvG9ZuJ_7pvZW_213WeepD6nsZ6MGSEFUYa7X_WKQY5W7De77MiMQGLgfAf92Fvq5KxDEcL8tt_vSlvjng=)
8. [thomasthornton.cloud](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdg5wflC0gs4PQUCSAI5CMO_-UDRBtsng-sBtQHy9wL4XJoaO1TDEzyveubmREZpBJm_vRkxeRpviFLexoM898zeLeVvuzFF-nxVYovJI6vPruHaMgczdnyQ_qxJ3Y-pGFJwN7LIm4u0nWZPosvF4892PcEZtpz7a9M9mtFQIQVqGxGabpkHU3Cii-4GxqpG_cxddrKxpnmA==)
9. [zenml.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVQyUp-LAj1WS_EOG8O6VP83y-73aDqf-cERoU4qRENFKcA9_lOe6A8TPZhfbap2Y7OfKV04pQN2IbJw5ft2KmM5YaCqoNJi5WdMy1YcpT45scX4j3dPwWq0S1Olxc)
10. [checklyhq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBxeYwN56N8MDuKEWW6c_SXMW_9I6GcVMqy-gnEftu3zEkacUwrDXuInK6w9TEA7gkkClyfJRSxGbvKOrJzR_vYE_aNoxthrj0MsZOTb0pNbxxqs940ygPbeJbBLGE-zQk9IlW6EoTMwbloC1Y)
11. [platformengineering.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWebanfP25qV3Wys4givjfItDuAu-_1lY4nf1u1NlBy0l2rQhvu_nzj3SEPXtky8tjHOrLFi5IyknNZdAdOH1eXg4I2SNs-wjtfiknrL4DRv1TlOX1b4J11lMbOcYE6J6kSL8=)
12. [kagent.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiXeNq2ZwilklfbgmvJebiFXg-obrhS1n_4XQmabLBTrRjwy9GqPQUNhNJJIxVdu3Jlzs7DD9srTLleGXgwm5AMXPk30rauPSR)
13. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1JDq5adB9uP11N4AoJXf4QJ5XHszyMWq5DDOJ6CsmO-Xpq3ggFzICURuWJxmK1IdOaiviWOS1A5YOJj-c9A5IqHgxJlTFX4vxYks1egydGZIjzUpHLn95A_I=)
14. [mezmo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE0OJl0bq8VlZ60bV8_UPT8jWeErSzbf1PcakFA5VMavjKat5CFZSzmZz470AEWDM6SCSmFzyFbwBi3MUFRHZuaWxbsawTlWdMJoluSUjuP6xKP53nUu37vGwTMmBFusI9uEmMs6E80LzVYR06dYSx3SfyNZSEvZooXHtNbvJFS5yks9T6pNgFXq0=)
15. [platformengineering.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf63n7l4AhhjynZ3yrRGh7k3vh2c53roVf6dmXREYoTzq09E5mLf75mVRA9CAzbh-iMTrA7VSsX86SkT0tWOQakzUWtlNhNyiZZuQ620ZJX5xegTTC8-hCezYn8Igv_nVE6pvHT6kY2Nds9gAP3gEb1nIFuheolSTucX1TX92ryz8kmDvoTMfaGQq3bOz-PQ==)
16. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFt06wGZJzpqtMWGOAEEUokMbo9kFcpf04qbP-YGsfbE-IXE866VRPJ_y5Y-qNL4CSNeuQ9VzYv2tjl6i1SemBT4idI_QUzDdC1-B66qC_D90ygWXJerSqVOgvmFcDk4QNY3AYCY62r)
17. [northflank.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0wB3zjMnP8vsheuspNbaHMmoXb80dHM6V2xXRZ86FvBpz8FGkSFC9Kl0Lbl2NKMtBKlguS3uLIJWb-oFHhRY_8bbRirnuqdhXEdXNqnLQ193Z6Tmcw-fIu0mgYG1Q_P032xMIBj7ZLcOKpo5KAicDdUYLGH5pPrpo1AU=)
18. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvlSjYGZl_l5WJFdqMi4lONB12DqBN19kqXMHRDB15wIuzr_GTBu-v9sFu43bV-hXD4RGAL7hAR6O_2H6xAcIvrt-labKOZkdyNGvdzctK0zeDSqta5rXFSgRzg0wB7asqyw==)
19. [martinheinz.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNz0_OA5c1iDIQUc-EFtldogmmM0QVQ3ZdQdOwGtMQJCh2SOPqTEHK7ZCXTJT48zJVbVK7M2HC2_Wq5zAbvqpfOJLOXoPN8EtgVAUR3sE6rboGV93h)
20. [mezmo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG11RzoWeYrBvXu0H5Yfpdf8pubnL5d5PRQIffLn5KpU-2fAnrbAKXExLNKhTp-Pa6TxHh-d4F_QLpmfL1ow8Q-PNNI94EaMKklyWMqwxnYpqaQniGOYe4=)
21. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtgMXJJltHmeWPFD075ChYXKOjt2fttygMMdZdzZIB8oZxnBeFqC3FuqLItPidgH2i8S_zv0wdniPq1ShdzgUyifamUEfXa2PKnmnlnNzPf_K2BRYPQE3IfQrCCO9gAvBYW_wiIi2YLXt5KM58STtbteTPniWdBzWYcnwwENo9L8UB7yYUmgeiTONfQ1UlS8YRv1qU-OxckXX3sVkB)
22. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1hPTDdUY1oPRY4t0A20MtheE7nhICZwiJrAC_8H5Nofk7Td6oTOOt9HWhM_nZo7fo5EVDanKvSNjhVFmj3sPRO_e2unCWgWl01bt-blF32Nx8nzvKShZsPidSgs_VCf8_CQ==)
23. [fast.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF54OzhJzlR8dBx542mQRm5e-Ny0sy4sngHB3LD1m1nZMX818i3jEH7DFJzLd23vB0Sr-Im1ZyCv8LBBUi6sMr4w3ZnbewAL19Fs__jz5GJUI4DnsufUfDdQwXkYmKIVrUvr9osZCNrNbc=)
24. [k8sgpt.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUfJ3Y7orD4Ks1bCeEhE3hd_asKHvnz2-OL_H601yfeTDkf3WdGpzzXxCshj80_PROP1SVFYh4o_IGfoApmUal3-a1TwzG3X8=)
25. [solo.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFscNTd4BwNHk8Yixk3f0p2r35YVlC0-LoSQo-Ed_l2neH8dXYO6V76vYezFV86p4BxVpZis-NzMLml6_imBtVVnU8kEOIE5GTMRELILhubwXMG03Msjrn7lQIuFbx34DXIzb6_t7xv65FmkRziw==)
26. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI8vRczEUu7GDVFGZvkwFEwRN2IjisTc5ZS0GEHugHU3OX8T51L8Hyuwc35hJRY1rHq9fzcl_JLr07QODDdDUPjQI7p6fCA7BR2ccEyXyZ0j56SrLFXw==)
27. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFE1VMnL1--5x-5_zEJqZZgaBs6VYIdhuqCaTjXDd15khjEDVDny0GfsaDXhn4ZijldcnVPoBoQn-uKYIv_EYSJ_ogUvVhEq9NYnTtFHGflNL-5MfZfmnykdssr13qukwgxSCocalOO9wlM_aIS483VEZV4D5W1D-CNnHuEY0J7X_088rIGJWfR9VAi_ocTTkgb-8tVQ==)
28. [ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNP-QCvwC-l7fOMcxYS9YKPqUmPQOsu4iZn7eXjOuRK0vXGKTkN1cHxt6tCI_2cD_jk8QsDZXyp2hbxkRGr7MaQHeVX-g5sne5bwMTtBIfs2ZAnHuHtNKpYfliKYMllxq9Aj3AraNp2RUqug==)
29. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBEoFchxmiYMT35hOG0UBeeEosj-CYIPnN6nl6QCDVu_Q4KPSe8BghDGkQGtErOhaGD488677Lfwfw1Pdga4OBRr2alYiVEAxAVR-tbcLlGQGyxOk3YjIWOaggaIgsWBVJxzm6tmr-OV8PDasQ61qZQYeVtQl50MPHb148OsVqfBJJ0-jxoF-zwuuZJkw4uISGHD86WEkJ3jbBwrmZOSpS_N0YR68NTlkQ_shpAG7Nrd3-aOJA)
30. [googleblog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpDSvRZVlU4SUmmApZDVp5Kvr_s875vnEVRehTPaN__uq3qUjVBQos0HupeVJuvBCn0J-otvb-RfrIHCzF1JkbvNrCc2rCh-I8N0rZ_B2-qkW_uTMPl87UIb8VCoUiTygtfUuUoKeR9EJ0139hU7r-kKGMOW5J6kmwEgA8R_Qf9F4dOw==)
31. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLZKCHMZH-HdslZXlJPW0O-DZG7hKh8irV98v4VKp7ncixXPYGWeO9TGUPQmk0AFaBVAeHQN2EP08sZTiE2cSNhKDEiWDlNhwMdNyzSBEWmQrCxG2Nj3vH-1buiUVe2uPOJIYysQpI1M7vtWOP4brRZApBXxlnURyeyhy6YMP269y0LaOVuOdodqk=)
32. [cncf.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFW4fsKKV5nATQGmLeuWnHoYwcoGmm6yU8bsqdbNelj5sbVwnuRTmMFSJR8kPNWRCE8Vwsny53Kv2-iUih4gtqrUFRz-w3p1U-24weQvj-jp_bgVt-U2ZRc2nU=)
33. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqnisnrYQj2zzlAoOcwcglAqw1GuSz9gHDKX0ZwDgcVyv-ffTSt-8y_MSUK6jg8szVv2T87FUalGFx4zm84gQt9fVWrL9nGN2H9KwZMbBxnl-UiAi9WSNfYEqmoBPygLI=)
34. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGNFvJaxuwE-Szwvv14Zl-UWvjP1p2hZMlr3bIbBnZGfQ9mXKDi2cE0jndCmJAu1pCHim4cET8Cj3z6fHbVjHv4a1b_yMQw1ohSTfhN2E=)
35. [mezmo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyXLzLcXTCB3OcYynCjwjHKJjbyVfr7_dE7wniY_-vHmkMRtiN9c1pmFzMwyMbTFaBWvHgTAwUu5Vk7Y8F6tLPkqIvnriCNDKwwsn1WQdr9A==)
36. [mezmo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFId_O1i73bb9PE7n3S9AtD6ieQpm2q9LwqC7MkTw0tA7McSWKJvGeAlXhy9gO8tJGr6sGfIWFmAA69tyAo7aJXWH3P9kvnz5ZuoDRCGOV8RMogSY_bgUgZ0tLA8TVn8tQtNxKLLGBM7aK3hgAj4aoh9TAY5lL_Ecs4830Dh4LBgypKyYH7g3V-DEHqk4RcdF0MJ1RMIS_krk218kf)
37. [incidentfox.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnCNLi7uTC2aTzi8x1QJW-bjzAV4XmwmYQefEdz_r9qQ-3DAM2lAfqQJlmcUaSei3HlmWAvSahoPwEbPyX12T0ZlTtXFUnRiXjXx8sL54uk6fo-vVJKpEGKzGl7UC3NrGhS_xf3qZjHcEuZfgwQK1sgFMFT-pl7Nk=)
38. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhsp53pcuaPzPrgqoIMtarwUYFlT3a3a-bxHTQdQAlqLINeiGKplDUOmj5Kl8IxPNBomF2-5Oes20nu5HYVlGfFTUel3J4od12GywmkI4oFB2d-Pk=)
39. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHrrQtMesHgkHBP3ocyIqA9VCDenvh9HvtOHqxTKLEkmcALwEqTC81pQlqhJ58GEyrnZIPe5LfC9pRJxWsjhJoputN6FaWLVgEfuYKdP5N2w==)
40. [arvoai.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHvAxf8RFxYKHFUOcmxz6cJg9QwFWJwQGSE76GViCwpVyurdc8pqduDxaV-4wiip5lSR42n2gaKZHPvPC6kiH_uCMW2mD1G_uqwu8C)
41. [arvoai.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG6zP2iGTdZPfWF6lfYL0Y1IzMUNcrARjmEWpEiwNtqmQPIMJg_p15EzFZ-d9gmCwGrO1nZoCjjZXNtz4jsb9Qnk5XX0E-F0yDMGIiq3olpN6GqQmZNDxP3pMwfc2hgt_bEdW8lC2R0tvx7S7gE7b4AXh_MblaPlWOZGDG2uAo-a9HgQ==)
42. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYsuaiYLpjb336GuxwB1rLLT0OQrxDRrh6ZUpGq_mmpBJ0A5HA3PoXi5dg31chCkEjQgVYoeaaOE0g4G0mXWU3uNHF51K_YiuXxRlsT2XjWpgNrwcXYZ65Qkt7GqcF43Wr84ZFfRPEDAFDKjpmmowzajVwMUb1pGo9FHf0ygQwbk0IgjRNCgINqlGKhLeMm1zC2cUHlHLqoXNb8wydn1QHaJdhUaI=)
43. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9ipZq8StfC3fXgV18WMm67wxeOmtYiO84kEhn7Mf3v-S-aFBm_dxlLVWjy9aihsPMTDYDjk_XRGy-ZRXHuHlS53Icybc9Kq1TSICGbAxGdFY3TrpBKkwCKV3qn0g=)
44. [amazon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu_chzZcrQdW8xIR8oJeRNFWoNxrWeErhEqhzUNRDHNTuIxU8-ttEvmFlCyaR_NAR8KONsWcgcEywJRH6G8Ic-VbN9lcM_kZ8lVz-v5XEsKP-3UGalT8OOnIXNUhDLTUvZ1eg-snri1H5FaMToKYoF-Jr2J9154vJFJ2hd9-rAuFKi4qbN7VldWfBnBw9op1JdEA0mSKjAXNiZdw64RXwv1thIEP7IPBN4-kL6eML8OA==)
45. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEls9TQuY8yIR0g5RxUZGRYZI2LVH7-AeRaksfva9VnsCTgXeFktrL31IFIt9DAABQ_La80AHpl6WR23YSkmP7rjE8LF5_L-DzZecTzOLJa5LX6QRVf7pncxQ==)
46. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjPOi0GtgJfuZNkdqsrcR6Jg7gNYkmSGmPHT6qZoP6VwvYpNgurfH7EDGxckcLv6HU4AOx5XTL99gnRFM0AvRAXQ9bL7MUX5jsnfcXE90T5kerIzgfl0qcmwdx7jtFd8GYhJHdqda4CiNQVyTZBvUUhga5Dn_keg048-lDL6X6qNGabLla3Db1M0N-O7c77KIoRUO1YcvuTTbKE-F4QX6Ru7X3TeWDdHdpRxupVyrYmanVSqoKEnE=)
47. [checklyhq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaSgMSvKMZDKikuJtouIBpk6T9BjvW9hqYHVPJ_SflYrt2hhqWMKc80jF5-b6Um2IDJLsqihMRHsbv5HALae4tCMdkl2tVSndiGrh4V5jkvfX9OQN2CFBqmouAfbAtVQpT2BC8N16WHcUsAClxuCzr2GXG55Pp2pK11wai1EZmB2im)
48. [cncf.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAKqzkNNo1hCVXIopSgAV1-Hl8ucypE2iSgWnjVwGxKRVjhoyWtC8V22kciM16wCbl5RWVlDifajNLbNQ8Xv2ktJin2Gk-2WCiHumLkbl0BpiUoYyltY5fJqORRa-HFY4=)
49. [checklyhq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFGnXN8oZeBQaffSSU6ZAkWoyxzNNWBJdlZBQDjmLbW_3gkkNWq_NyBoBp4xTkkRIky4xNcBVv17aV1SQveMifSX1XsbT2KU4eXWGxqdaWq2PKCFbo9Rp-gMlWUrW9u0vDAiWhu3jilVkMDheygrmhQ0id0VKP1nV1_NS0ncAwPJ35aKFen_TO9W3A)
50. [checklyhq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH31KNwJKrG9MncJeXd3eAgTZ_QYVmIB1OrBhno5D-ykdJxAxdZoTpE4qJqKz7kiRLhTtAZEBezgVO6tugZSxj9_Arh8RI5BuVUpwND5PwiEvIYtpMq8OIFZpoTPhTWC9N0NihqcCNuK-P4w-4ZT_mPsuxvTbQ6g8bijA==)
51. [checklyhq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3x_J_OpyQfQZ3q-cVEm4hr6DxLDwLwzQl5dXSb7ch6sQirf_tnZzfUSdt6YuovN-X6JtoUU0L-xm_CHWUyfeREQ-qtc81uYVh8bSyz0BmgQ==)
52. [cncf.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzwr_o-eDBteSh7Kmwptyv1Ozp_WBa4-WolwBnlDzDUp7PaXQxXpuoo07xFsOsPLzbp-3HatbYfNyGdWshcCWjzefiSfXPjspGb3ByfIZGFJgUjCq07imkUNCqj9l7Kdxa1ZWShyQEM_fHDk1076oC9NM-PeOKRPxijoFBDtI2h-wIDrYX)
53. [mezmo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPWFuo6j_65SAt72uwOtBQWigfxoUDgDc2lTKQGloGMaIDORHxxKon36pVDjroGm9sIbjCvTGlHKh1Dv14OvrI4vzyUiGoDaE2JROECZc1GTKFZoIN-bNhJd-iL1V5_MQoaFDtqhVpoQaOtT-MtBYxGKk3Wc_Fxw==)
54. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf5V5jTpTJ9qhSFUJCMnK77J3rJU2e5cq6udl1Mt2n70waeSC39WmarG4sbE4PafNedi60LJsRqOy-w8Uw2FFXIJdDjtztgDJLiUE0u7Tt4TE4wOvglrEC1kKuj_lBQAg7qgFinWmTzEQ5llnt1l3BCvWo1vKh)
55. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJjJ2HBZuhc6EguB-sx2VeQoQL2B4I2Lp-7nFwOS9Nl62WwnCu90NrkqTOSMfKgSpdQcIiX2T2VXItwXMXr-Ws_gaol7l35RfWQ6DVGR62MhrulRFcWKHmm49tpv4CQPSl0w==)
56. [donaldmcgillivray.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIwBivLa-P7Ls45AvGQCoasn0xByIeCUKtL1IV96_YvAQsl8aIVE9BFg6RwwxiwjLEgsN8-wboCdzq3NMogdbloN3S-dU7VgDkgCuyHlhFOcP-CCFsopaSGlebnnzvhu7_z5Gb8ke8CulJhN74JQ==)
57. [csanchez.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_zzcEx_FLNJfsbTTMXpn-2z6DauS2kgAdIh52dKF8tiS8w9R5nfR5GuSfQ1j9GMhGq4RNAyxqmeLlBH05yctYGkX-gnenLVrQ6fvf57XCp68soW3gvr90AGzbEt-A55H-hkXY2fgHVYJ6VRQYmEAGHBzFGErUW-d9B2feXVeOLWIDB0-QCL9mU1nuw6jRisGExACRRlVN3FDPYCh_rCI3ibllSGNfk7HyVVYQON_N)
58. [generativeai.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzOxDBOXhTv8jMlvGNaWjtMVJ6eQpXmCU9w_QNgkINfZpLWn_GZ_S9Wzs_HcGbC4yzuB579mEHMl5xWUAt35qxjiJvkCW5PBNaQaKOIOHY431s960tiEwDMexPajEdNbL4aEFPxHHugEvV5vbHFjzcB0GDOWIQpUSRcQykqtPz7dWXpBbxsvsz3VSEwJL4q9pZ7oNc2v6DIr86mwSODlNwAdC1)
59. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKRx94tGU64nYxtefPDsrbyZNTJ-kyvmyF0jNOdgXjWhVoFlQy34_PB3b8A1_bRECTnFLeitb_42J8-a-bZCzqUmskKV4fBfzzPLkOxs0SxSKB6g-ltPfyDrJnqGTFGZqxVrHweFw3h2W-D-lqnvNCcsv0k0O3Xym2H6h4fFheYxpXcWKkXUtgLoBMYbDsDvlLTuUmMMq81kIODrwtIHMbwpcbyKs28DbOH1mgxh2l)
60. [co-one.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkH9z_rnTSV-E-5_JXCJ5sbseHBn2twJKzdlXUlDlP_OeKtC6R1CRpzEY8DwJOlbaluZZbhpu54uLyi2dDm5xUFs57cWUNMZghAnRp9OlM2OBTpSYxhjd78GOGgfhuMAKcFvQG-wn-uB9ehsQr)
61. [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHTHxPraxPL91mGWSa9jNwsKpakig-GPNRmnfS9V5XspJyMzA3dY-LFylmgA4Ip6fOzfeUZIzxZd1urdIawyjZpe7FpQJX5Q1ObvGafCQ8unmpyxbT_M1QllCesStozI0KfUQ7rZPt_qU9nge3ZcP_OUq354HwC-P-21ZKEsZeTw3VwK39U-Sgg2sNS5qgvGTlORxgAFYqdaYM1CdMAE-PjnOtjQ==)
62. [ibl.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHS5ut9pR_6p11FM4sQ8Ye11n-IbkvI3Mrk23wT_-3vSN8NEzIonNHCAm-_yqK0KCt15J8YTlWe4JaCuWRibm8A7xVMh1xiy-496McCpr5dLeUsrOjaDdnB5Y7Bl5FFsNVPvnv0u96et4fp-_mWOK0AQ==)
63. [arinco.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ve5Qgj2NxBVqnIKE5icAT4_uGVsEItBjHZY2V0HEerTsh3voM0nIlxK_kbRnuaN6Mvzs2kMzH6wEhbxjWOzDZXRk45xtnqcTN0v2GN1JXkHkKiKeIEZV-st4LfVHXIBBqghbt5D1LoPB8gvLtF-_hNxzMWEsP1dwdiIGReG-tOTm93vRagV9aa69xNhwlKO8PP3Bl3-c0SIGyDWeGLHlKw==)
