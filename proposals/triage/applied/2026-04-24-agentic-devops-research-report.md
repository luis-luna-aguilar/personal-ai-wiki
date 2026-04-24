---
type: triage
source: raw/deep-research/2026-04-24 Agentic Devops.md
status: applied
---

# Triage: Agentic DevOps Research Report — 2026-04-24

## Signals

- [x] **[agents, coding]** Agentic DevOps is becoming a distinct operating layer, not just "AI writes Terraform"

    **What it is:** The report’s core framing is that infrastructure agents are shifting from passive code generation toward active participation in observability and control planes. The important distinction is not "AI helps with DevOps," but "agents now reason over live telemetry, recommend actions, and sometimes execute in tightly controlled runtimes."

    This changes the category from a narrow provisioning CLI story into a broader operational surface: incident triage, diagnosis, rollout safety, remediation, and verification.

    **Why it matters:** The current wiki represents `agentic-devops` mostly through [[tools/stripe-cli]], which is too narrow for the broader category this report describes. This likely calls for a stronger state-of treatment and possibly a concept or training page that frames what safe agentic infrastructure work actually looks like.

    **Likely wiki impact:**
    - update `wiki/state-of/agents.md` `Agentic DevOps` section
    - update `wiki/state-of/coding.md` `Agentic DevOps` section
    - possibly create a new training or concept page on safe agentic infrastructure operations
    - create source summary `wiki/sources/deep-research/2026-04-24-agentic-devops.md`

    **Source shape:** Strong at the category level, mixed at the product-detail level. The macro shift is credible. Specific stack recommendations and vendor rankings are synthesis-heavy.
    **Verification:** moderate for the category framing, required for concrete tool claims.
    **Recommended:** propose-with-hedging

- [x] **[agents]** Tri-state execution model for infrastructure agents: read-only, propose-only, mutate-with-approval

    **What it is:** This is the report’s clearest governance contribution. It recommends a strict execution ladder for infrastructure agents:
    - **Read-only** diagnosis and context gathering
    - **Propose-only** actions such as PRs, tickets, or remediation plans
    - **Mutate-with-approval** execution through policy gates and sandboxes

    The underlying claim is that human-in-the-loop approval should remain mandatory for state-mutating infrastructure actions, even when diagnosis is heavily agent-assisted.

    **Why it matters:** This fits directly with existing wiki themes around staged autonomy and anti-autopilot review friction, but applied to production infrastructure where the blast radius is much higher. It could materially strengthen [[training/company-wide-ai-enablement]] and [[training/anti-autopilot-review-friction]] with a concrete high-risk domain example.

    **Likely wiki impact:**
    - update `wiki/training/company-wide-ai-enablement.md` with infrastructure-specific autonomy guidance
    - update `wiki/training/anti-autopilot-review-friction.md` with infrastructure examples of why approval gates matter
    - possibly create a dedicated training page for agentic infrastructure operations if the material proves broad enough

    **Source shape:** Strong as a governance pattern, but the exact "tri-state" label appears report-normalized rather than canonical industry terminology.
    **Verification:** moderate. Good candidate for wiki guidance with hedging; verify if a stronger primary source exists before treating the label as standard.
    **Recommended:** verify-first

- [x] **[agents]** Deterministic policy engines are emerging because LLMs cannot be trusted to self-enforce guardrails

    **What it is:** The report argues that production safety is moving into deterministic middleware rather than prompt-only rules. It highlights:
    - **Skyflo** — typed, auditable execution with explicit human approval for mutations
    - **Agent RuleZ** — local-first policy engine intercepting agent tool calls and blocking prohibited actions

    The conceptual claim is more important than the individual vendors: infrastructure safety needs non-LLM enforcement layers that can mathematically prevent dangerous actions.

    **Why it matters:** This sharpens the wiki’s existing harness and autonomy material. It is one of the clearest concrete examples of "the harness matters more than the model" in a high-stakes domain.

    **Likely wiki impact:**
    - update `wiki/concepts/harness.md` with deterministic policy enforcement as part of the operational harness
    - possibly create `wiki/tools/skyflo.md`
    - possibly create `wiki/tools/agent-rulez.md`
    - possibly update `wiki/state-of/agents.md` if these tools define a meaningful subcategory or leadership cluster

    **Source shape:** The architectural pattern is strong. Specific latency and enforcement claims need verification. Tool-specific scope may be narrower than the report suggests.
    **Verification:** required for tool pages and any numeric claims; moderate for the broader pattern.
    **Recommended:** verify-first

- [x] **[agents]** MCP and A2A are increasingly treated as infrastructure protocols for operational agents

    **What it is:** The report treats **MCP** and **A2A** not as generic agent buzzwords but as the connective tissue for production operations: observability agents, infrastructure agents, and remediation flows need shared standards rather than custom API glue.

    The new angle here is operational: protocol standardization matters more when agents need to move across observability data, incident-response tools, and environment-specific actions.

    **Why it matters:** The wiki already has strong pages on [[concepts/mcp]] and `A2A`, but this report adds an infrastructure-operations lens that could make those pages more concrete. It may also help explain why enterprise agent stacks are converging on protocol layers rather than bespoke wrappers.

    **Likely wiki impact:**
    - update `wiki/concepts/mcp.md` with infrastructure / observability integration context
    - check whether an `a2a` page needs a stronger operational handoff example
    - source summary should explicitly note protocol standardization as a major theme

    **Source shape:** Directionally credible, but broad. Treat as reinforcement of an existing trend, not as sole proof that MCP/A2A are already dominant everywhere.
    **Verification:** light-to-moderate for concept updates; stronger verification if used to support specific market-leading claims.
    **Recommended:** propose-with-hedging

- [x] **[tools]** Kubernetes-native and observability-native agent infrastructure is maturing

    **What it is:** The report surfaces a cluster of agentic SRE / platform tools:
    - **Kagent** — Kubernetes-native orchestration / control plane
    - **AURA** — context assembly / incident-context harness
    - **IncidentFox**, **Aurora**, **OpenSRE** — incident investigation / RCA agents
    - **K8sGPT** — Kubernetes diagnostics as an agent-usable skill surface
    - **Kuberhealthy** and **Checkly** — post-deploy verification

    The common pattern is that production agents are being embedded into the infrastructure and observability stack rather than bolted onto chat alone.

    **Why it matters:** This could significantly broaden the wiki’s `agentic-devops` representation beyond Stripe CLI. It may justify a handful of tool pages, but only selectively: the report names many tools, and promoting all of them would be noisy.

    **Strongest promotion candidates:** `Kagent`, `K8sGPT`, `Skyflo`, `Checkly`.
    **Maybe:** `AURA`, `IncidentFox`, `Kuberhealthy`.
    **Probably mention only unless better sourcing appears:** `Aurora`, `OpenSRE`.

    **Likely wiki impact:**
    - update `wiki/state-of/agents.md`
    - possibly create 3–6 tool pages after verification
    - maybe add a more explicit DevOps/platform engineering angle to `wiki/state-of/coding.md`

    **Source shape:** Discovery-heavy and noisy. Best used as a shortlist generator rather than a direct ingest map.
    **Verification:** required.
    **Recommended:** selective verify-first

- [x] **[agents, coding]** Sandboxed execution is non-negotiable for agentic infrastructure work

    **What it is:** The report extends a theme already present in the coding-evals material: infrastructure agents must not execute generated scripts or remediation code on primary hosts. It contrasts:
    - **microVM / stronger isolation** approaches such as `E2B`
    - broader execution platforms such as `Northflank`
    - lighter local containerized dev sandboxes such as `Daytona`

    The important point is not the vendor list. It is that agentic ops requires a hard separation between diagnosis and safe execution.

    **Why it matters:** This overlaps with the QA tooling report and with existing eval guidance, but pushes the security and blast-radius argument further. It likely belongs in any future training page on agentic infrastructure operations, and may justify a cross-link back to [[training/evals-for-agentic-software-development]].

    **Likely wiki impact:**
    - update existing training guidance to note that infrastructure mutations need even stricter sandboxing than coding evals
    - possibly create `wiki/tools/daytona.md`
    - possibly create `wiki/tools/checkly.md` if post-deploy verification is treated as part of the safe execution loop
    - avoid duplicating `E2B` work if that tool is already proposed from the QA tooling report; coordinate the two sources

    **Source shape:** Strong at the architectural level, weaker at precise product comparisons.
    **Verification:** required for tool pages and product-specific tradeoffs.
    **Recommended:** verify-first

- [x] **[training]** Agentic infrastructure operations deserves a practical guidance page

    **What it is:** The report is broad, but the reusable guidance is coherent:
    - maintain read-only / propose-only / mutate-with-approval separation
    - require deterministic policy enforcement
    - standardize on protocolized tool access instead of ad hoc wrappers
    - sandbox all execution
    - verify after deployment using synthetic or cluster-level checks

    This is more like an operational training page than a single concept page or a pile of tool stubs.

    **Why it matters:** The wiki has org-level enablement pages and coding-agent eval pages, but little that translates those lessons into production infrastructure practice. This is one of the clearest gaps surfaced by the report.

    **Likely wiki impact:**
    - create `wiki/training/agentic-infrastructure-operations.md` or similarly named page
    - update `wiki/index.md`
    - use selective tool pages only as support, not as the main outcome

    **Source shape:** Good synthesis candidate. The guidance is actionable even if individual tools change.
    **Verification:** moderate. Enough to propose a hedged training page, but verify any highlighted tools or protocol claims.
    **Recommended:** verify-first

## Suggested processing order

1. Verify and propose the broadest durable outcome first: a training page on safe agentic infrastructure operations.
2. Verify the strongest control-plane / safety tools next: `Kagent`, `Skyflo`, `Agent RuleZ`, `K8sGPT`.
3. Reuse sandbox work across reports: if `E2B` is promoted from the QA tooling report, avoid duplicate tool-page work here.
4. Treat the remaining tool list as a discovery pool, not an obligation to create many pages.

## Notes

- This report overlaps with `raw/deep-research/2026-04-24 QA Tooling for Software Agents.md` on sandboxing and safe execution, but the center of gravity is different. The QA tooling report is about verifying software-agent output; this DevOps report is about safe operation inside live infrastructure and observability stacks.
- The strongest reusable idea is not any one startup. It is the operational pattern: production agents need protocolized tool access, deterministic guardrails, human approval for mutations, and isolated execution.
