---
type: proposal
source: raw/papers/2503.04931v1.pdf
status: pending
created: 2026-04-14
---

# Proposal: Curiosity-Driven Imagination paper

## Summary

This March 6, 2025 robotics paper proposes a hybrid adaptation method for open-world novelty: learn symbolic operators and a stochastic neural transition model in parallel, use intrinsic curiosity to discover new transitions, then plan in an "imaginary" symbolic space to generate reward machines that densify RL training. In RoboSuite pick-and-place novelty scenarios, the method outperforms prior hybrid baselines on asymptotic success in all five scenarios and adapts faster in four of five.

## Intended changes

- [ ] **Create** `wiki/concepts/curiosity-driven-imagination.md` — new concept page for the paper's main idea
    > See draft below

- [ ] **Create** `wiki/sources/papers/curiosity-driven-imagination.md` — paper source summary
    > See draft below

- [ ] **Update** `wiki/state-of/agents.md` — add a recent-change line for the new concept
    > **Add to Recent changes:**
    > `- [2025-03-06] Added [[concepts/curiosity-driven-imagination]] — robotics paper combining symbolic operator discovery, intrinsic curiosity, and reward machines for faster open-world adaptation`

- [ ] **Update** `wiki/state-of/science.md` — add a recent-change line noting the robotics research signal
    > **Add to Recent changes:**
    > `- [2025-03-06] Added [[concepts/curiosity-driven-imagination]] — Tufts/AIT paper on faster open-world robotic adaptation via bi-level world models`

- [ ] **Update** `wiki/index.md` — add the new concept entry and bump page counts
    > **Add under Concepts:**
    > `- [[concepts/curiosity-driven-imagination]] — bi-level neuro-symbolic adaptation method: curiosity discovers new transitions, symbolic imagination turns them into reward machines *(as_of: 2025-03-06)*`
    >
    > **Update page count:**
    > `- concepts: 6`
    > `**Total content pages: 31.**`

## Page drafts

### wiki/concepts/curiosity-driven-imagination.md (new)

```md
---
title: Curiosity-driven imagination
type: concept
domains: [agents, science]
tags: []
as_of: 2025-03-06
sources: [curiosity-driven-imagination]
---

# Curiosity-driven imagination

Curiosity-driven imagination is a neuro-symbolic adaptation pattern for open-world robotics. The core idea is to learn two models at once: a low-level stochastic transition model that uses intrinsic curiosity to push exploration toward unfamiliar states, and a high-level symbolic model that abstracts newly discovered transitions into operators. The agent then plans in an "imaginary" symbolic space and turns those plans into reward machines that densify reinforcement-learning feedback.

## Current status (as of 2025-03-06)

- Introduced in a Tufts / AIT paper on robotic manipulation under sequential novelty injections
- Combines three ingredients that are often studied separately: operator learning, intrinsic curiosity, and reward machines
- Uses symbolic planning for exploitation and curiosity-driven exploration for discovery, instead of relying on fixed sparse rewards or human guidance
- Reported result: better asymptotic success than compared hybrid baselines across five novelty scenarios, with faster adaptation in four of five

## Why it matters

- It treats symbolic abstraction as something learned during adaptation, not something fixed before deployment
- The "imaginary" planning space lets an agent reason about possible transitions before it has mastered the corresponding low-level execution
- Reward machines turn those symbolic plans into denser training signals, which helps RL recover faster when the environment changes unexpectedly

## Limitations

- The paper still needs tens of thousands of environment steps to adapt, so it is faster than prior hybrid methods, not close to one-shot adaptation
- It depends on a reliable detection function from continuous observations to symbolic states
- Lifted operators may overgeneralize across object instances unless they are re-grounded and validated in the real environment

## Sources

- [[sources/papers/curiosity-driven-imagination]]
```

### wiki/sources/papers/curiosity-driven-imagination.md (new)

```md
---
title: Curiosity-Driven Imagination: Discovering Plan Operators and Learning Associated Policies for Open-World Adaptation
type: source
source_type: paper
source_file: raw/papers/2503.04931v1.pdf
published: 2025-03-06
ingested: 2026-04-14
domains: [agents, science]
---

# Curiosity-Driven Imagination: Discovering Plan Operators and Learning Associated Policies for Open-World Adaptation

This paper proposes a hybrid neuro-symbolic method for open-world robotic adaptation. The system learns a stochastic neural transition model plus a symbolic operator model in parallel, uses an Intrinsic Curiosity Module (ICM) to discover unfamiliar transitions, and plans in an "imaginary" symbolic domain to generate reward machines that densify the RL objective. The target setting is robotic manipulation under sequential injected novelties where old operators fail and new adapting executors must be discovered quickly.

## Influenced pages

- [[concepts/curiosity-driven-imagination]] — new concept page for the paper's main method
- [[state-of/agents]] — recent change noting a research signal in agent adaptation
- [[state-of/science]] — recent change noting the robotics adaptation result

## Key claims extracted

- The method learns two transition models in parallel: symbolic operators and a neural stochastic dynamics model
- Intrinsic curiosity is used to push the policy toward novel transitions that can later be abstracted symbolically
- The learned symbolic model supports planning in an "imaginary" space, including hypothetical transitions not yet directly executed
- Imaginary plans are converted into Linear Temporal Logic reward machines, giving denser and more structured reward signals
- In RoboSuite pick-and-place novelty scenarios, the method reports better asymptotic success than the compared hybrid baselines in all five tested novelties
- The method reports faster adaptation time than the compared baselines in four of the five novelty scenarios
- Pure RL baselines reportedly failed to solve the novelty settings within 500,000 training steps

## Methodology notes

- Environment: RoboSuite pick-and-place can task
- Novelty types: sequential shift and disruption scenarios affecting operators such as `Pick`, `Reach`, and `Place`
- Baselines discussed: HyGOAL, RapidLearn, LTL&GO, SAC
- Training budget: up to 500,000 steps per novelty, 10 seeds, evaluation every 20,000 steps

## Caveats

- Results are from a simulated robotic environment, not real-world robot deployment
- The paper reports aggregate wins but still requires substantial adaptation data
- The approach depends on a hand-designed detection function that maps continuous observations into symbolic predicates
- The authors explicitly note scalability pressure as the symbolic domain grows
```

## Schema / vocabulary additions

_(none)_

## Open questions

- I treated this as a `concept` rather than a `trend` because the paper is primarily a method contribution. If you want, I can instead frame it under a broader `open-world adaptation` page and fold this paper into it.
- I used domains `[agents, science]` because this is agent adaptation research in robotics. If you want the wiki to reserve `science` for "AI helping scientists do science" rather than research-on-agents, I can keep it under `agents` only.

## Comments

- I wanna use this for not robots but an agent changing code and I want to have the reward machine based on the standard operating procedures of the user organization.  please analyze how this concept adapts and relates to the current state of agentic development documented in this wiki 