---
title: Anti-autopilot review friction
type: training
as_of: 2026-04-24
sources: [every-ai-autopilot, every-youre-the-manager-now, ai-work-intensification-march, post-vibe-coding-verification-february, every-vibe-check-april-21-2026, lennysan-simonw-interview, prof-devs-control, agents-evals-deep-research, agentic-devops-deep-research]
---

# Anti-autopilot review friction

As AI output gets more fluent and more often correct, people stop truly checking it. The result is not only hallucinations slipping through, but humans losing track of whether they ever formed their own judgment in the first place. Anti-autopilot review friction is the practice of deliberately inserting small costs back into the workflow so judgment stays human.

## Current guidance

- Write your own rough position before asking the model for its answer
- Separate generation and review in time or surface so the review brain is different from the generation brain
- Force yourself to explain why an accepted output is right for this reader, client, or task
- Use confidence checks as a trigger for more review, not as a substitute for review

## Proven patterns

- **Think before you look.** Create bullets, constraints, or your own thesis first
- **Build in a gap.** Review later, or in a different interface, after attention has reset
- **Require acceptance reasons.** Don't accept "sounds good"; require a defensible why
- **Use forcing functions.** Make the human judge before the AI answer becomes the default anchor
- **Use stopping rules.** Deliberate friction is not only about catching errors; it also helps break the "one more prompt" loop that turns useful AI sessions into compulsive overwork
- **Professionals control, not vibe.** Field research (N=13 observations, N=99 surveys; 3–41 years of experience) finds 100% of observed developers controlled software design and implementation regardless of task familiarity. They control via: detailed prompts with explicit context (12× observed), 70+ step external plans executed 5-6 steps at a time, and user rules that enforce project conventions. Enjoyment average: 5.11/6 — but from collaboration, not delegation. "I do everything with assistance, but never let the agent be completely autonomous."
- **Review the gates, not only the output.** In agent-heavy coding workflows, judgment increasingly belongs on specs, acceptance criteria, and verification scripts instead of only on generated diffs
- **Agent-as-watchdog.** A lightweight background agent monitors a relevant external surface (public social channels, issue trackers, partner APIs) for brand mentions, security anomalies, or policy violations — nightly or on a schedule — and routes findings to humans for judgment. Every's Claudie workflow (X monitoring for brand/security mentions) is a practical example: the agent does the scanning and pattern-detection; humans review and decide. Low setup cost, continuous coverage, judgment stays human.
- **Escalation evals as a forcing function.** Before granting an agent autonomous action, test whether it knows when not to act. Inject adversarial examples and out-of-scope requests into the eval suite and verify the agent reliably triggers a human handoff rather than hallucinating a response. This is review friction applied at the design stage: it forces you to define the edge cases before the agent encounters them in production.
- **Human gate on infrastructure mutations.** In production ops, review friction should not disappear as the agent gets more capable. It should become more explicit: read actions can flow, but writes pause for human approval and post-action verification.

## What works and what fails (empirical ratios)

From field research (N=99 surveys; suitable:unsuitable ratios):

**Works well:**
- Small, well-scoped tasks — 33:1
- Tedious, repetitive work — 26:0
- Scaffolding and boilerplate — 25:0
- Following well-defined plans — 28:2
- Writing tests — 19:2
- Writing documentation — 20:0

**Fails consistently:**
- Complex tasks requiring domain knowledge — 3:16
- Business logic — 2:15
- One-shotting code without modification — 5:23
- Integrating with existing or legacy code — 3:17
- Replacing human decision-making — 0:12

## Failure modes

- Mistaking "I saw it" for "I reviewed it"
- Letting fluency stand in for correctness
- Reviewing too many AI outputs in a row without reset
- Using AI to replace the judgment layer rather than the execution layer
- **Vibe-coding default inheritance.** AI coding tools (Lovable and similar) generate working prototypes with insecure defaults — Supabase row-level security off, public access rules on storage, API keys embedded in client-side code. The code looks complete and runs correctly, so it passes review without triggering concern. Users inherit the AI's insecure-by-default configurations unless they know to audit them specifically. This is distinct from hallucination: the code is correct code with an insecure configuration choice.
- **AI tooling layer as supply-chain attack surface.** The Vercel/Context AI breach (April 2026): a third-party AI integration vendor was compromised, exposing Vercel customer credentials. As AI tool dependencies proliferate, the AI tooling layer becomes a new supply-chain attack surface separate from the application layer.
- **The "lethal trifecta" of agent security (Simon Willison).** When an AI agent has access to private data AND exposure to untrusted content (incoming emails, scraped web pages) AND the ability to send data externally (reply to email, post to API), prompt injection cannot be reliably prevented. Any malicious instruction in untrusted content can override the agent's intended behavior. This trifecta cannot be reliably solved with current techniques, and Willison predicts a "Challenger disaster" for AI security if it hasn't already happened. Review criteria for new agent designs: does this agent have all three legs of the trifecta?

## Sources

- [Every — We Need to Talk About AI Autopilot](../sources/newsletters/every-ai-autopilot.md)
- [Every — You’re the Manager Now](../sources/newsletters/every-youre-the-manager-now.md)
- [AI work intensification](../sources/newsletters/ai-work-intensification-march.md)
- [Post-vibe-coding verification and cognitive debt in late February](../sources/newsletters/post-vibe-coding-verification-february.md)
- [Every — Mini Vibe Check (Claude Design + AI security, April 21 2026)](../sources/newsletters/every-vibe-check-april-21-2026.md)
- [Lenny Rachitsky — Simon Willison interview takeaways](../sources/tweets/lennysan-simonw-interview.md)
- ["Professional Software Developers Don't Vibe, They Control" — research summary](../sources/tweets/prof-devs-control.md)
- [Comprehensive operational framework for agentic AI evaluation](../sources/deep-research/2026-04-23-agents-evals.md)
- [Agentic infrastructure and operations](../sources/deep-research/2026-04-24-agentic-devops.md)
