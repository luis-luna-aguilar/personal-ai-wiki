---
type: proposal
source: raw/papers/2503.04931v1.pdf
status: pending
created: 2026-04-14
---

# Proposal: Curiosity-Driven Imagination paper

## Summary

This paper is about what an agent should do when its usual plan stops working.

The authors test this with a robot arm. The robot already knows a simple job: pick up a can and put it in a bin. Then the researchers change the world around it. Maybe a door blocks the bin. Maybe the light turns off. Maybe an obstacle appears. The old plan no longer works, so the robot has to figure out a new way forward.

The useful idea is simple: when the agent gets stuck, it should do three things together:

1. Try unfamiliar actions to learn what changed.
2. Turn useful discoveries into new reusable steps.
3. Use those steps to create a clearer training checklist, so learning is guided by progress instead of only final success.

For our purposes, the interesting translation is coding agents. A coding agent can also get stuck when the repo, test setup, API, or workflow is different from what it expected. This paper gives us a way to think about agents that learn a new working procedure, then turn that procedure into a checklist based on an organization's SOPs.

## Intended changes

- [x] **Create** `wiki/concepts/curiosity-driven-imagination.md` — plain-language concept page for the paper's main idea
    > See draft below

- [x] **Create** `wiki/sources/papers/curiosity-driven-imagination.md` — paper source summary written for practical understanding
    > See draft below

- [x] **Update** `wiki/state-of/agents.md` — add a recent-change line for the new concept
    > **Add to Recent changes:**
    > `- [2025-03-06] Added [[concepts/curiosity-driven-imagination]] — paper pattern for agents that recover from broken plans by exploring, learning new steps, and turning them into guided rewards`

- [x] **Update** `wiki/state-of/science.md` — add a recent-change line noting the robotics research signal
    > **Add to Recent changes:**
    > `- [2025-03-06] Added [[concepts/curiosity-driven-imagination]] — robotics paper on agents learning new recovery steps when the world changes`

- [x] **Update** `wiki/index.md` — add the new concept entry and bump page counts
    > **Add under Concepts:**
    > `- [[concepts/curiosity-driven-imagination]] — agent recovery pattern: explore when stuck, learn new steps, and turn the steps into guided rewards *(as_of: 2025-03-06)*`
    >
    > **Update page count:**
    > `- concepts: 6`
    > `**Total content pages: 32.**`

## Page drafts

### wiki/concepts/curiosity-driven-imagination.md (new)

````md
---
title: Curiosity-driven imagination
type: concept
domains: [agents, science]
tags: []
as_of: 2025-03-06
sources: [curiosity-driven-imagination]
---

# Curiosity-driven imagination

Curiosity-driven imagination is a pattern for agents that get stuck because the world changed.

The basic idea:

1. The agent has a plan.
2. Something changes, so the old plan fails.
3. The agent explores to find out what is different.
4. It turns useful discoveries into new steps it can use again.
5. It uses those new steps to guide future learning.

In the paper, the agent is a robot arm. It needs to pick up a can and place it in a bin. The researchers then add surprises: a locked door, an obstacle, a hole, an elevated target, or a light that turns off. The robot has to adapt instead of just repeating the old plan.

The word "imagination" means something specific here. The robot is not daydreaming or inventing anything freely. It is making a possible plan from what it has learned so far, then testing whether that plan works in the real environment.

## Current status (as of 2025-03-06)

- Introduced in a Tufts / AIT robotics paper.
- Tested in a simulated robot-arm task, not on a real physical robot.
- Aims to help agents recover when a known step stops working or a missing step must be discovered.
- Combines exploration, step-learning, and guided rewards.
- Reported better final success than the compared methods in all five tested surprise scenarios, and faster adaptation in four of five.

## The idea in simple terms

Imagine a robot has this plan:

```text
go to can -> pick up can -> go to bin -> drop can
```

Now a door blocks the bin. The old step `go to bin` fails.

A brittle agent might keep trying the same thing. A pure trial-and-error agent might wander around until it accidentally succeeds. This paper proposes a more structured recovery loop:

1. Notice that the old step failed.
2. Explore the changed world.
3. Discover that touching a sensor opens the door.
4. Save that as a new useful step: `open door`.
5. Build a new plan:

```text
go to can -> pick up can -> touch sensor -> open door -> go to bin -> drop can
```

Then the agent uses that plan as a training guide. It does not wait until the final drop-off to get useful feedback. It can get feedback for making progress through the new sequence.

## What each part means

`Curiosity` means the agent is rewarded for checking unfamiliar situations. If the world behaves in a way the agent cannot predict yet, that area becomes worth exploring.

`Imagination` means the agent builds a possible route using what it has learned. The route is still only a guess until tested.

`Learned steps` means the agent turns discoveries into actions it can plan with later. For example: "to reach the table, the door must be open."

`Guided rewards` means the agent gets feedback for intermediate progress. Instead of only asking "did the whole task succeed?", the system can ask "did you open the door?", "did you reach the bin?", and "did you place the can?"

## Why this matters for coding agents

The robotics setup is not the main reason this is interesting for us. The useful transfer is to coding agents.

A coding agent also follows plans:

```text
reproduce bug -> write failing test -> make focused fix -> run tests -> summarize risk
```

But real repos often break the expected path. Maybe the test command is different. Maybe fixtures need setup. Maybe a monorepo uses a package filter. Maybe the failure only appears with a specific environment variable.

This paper suggests a useful design pattern:

1. When the normal workflow fails, the agent should explore the repo to find the missing step.
2. It should turn the discovery into a reusable action.
3. It should update the working checklist for this task.
4. It should reward progress through the checklist, not just the final patch.

In our setting, the "reward machine" could be based on an organization's SOPs. For example, a bug-fix SOP might reward the agent for producing real evidence at each step: reproduction, test coverage, narrow patch, passing checks, and review notes.

## Practical takeaway

The paper points toward agents that are less brittle because they can repair their own workflow.

For projects, the question becomes: can we give an agent clear SOP checkpoints, then let it discover missing repo-specific steps when those checkpoints fail?

That could help with:

- unfamiliar codebases
- changing test setups
- flaky or missing local commands
- hidden setup requirements
- organization-specific review expectations

## Limits

- The paper tests simulated robotics, not software work.
- The robot still needs many attempts to learn; this is not instant adaptation.
- The method depends on being able to detect meaningful states, such as whether a door is open or an object is held.
- For coding agents, the hard equivalent is detecting real progress: did the test actually reproduce the bug, did the patch fix the right thing, did the checks prove enough?
- A checklist-based reward system can be gamed if the checkpoints are shallow.

## Sources

- [[sources/papers/curiosity-driven-imagination]]
````

### wiki/sources/papers/curiosity-driven-imagination.md (new)

````md
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

This paper asks a practical question: what should an agent do when the world changes and its old plan no longer works?

The authors study that question with a robot arm in simulation. The robot's normal job is to pick up a can and put it in a bin. The researchers then add surprises that break the normal plan: obstacles, holes, locked doors, changed object positions, or missing light.

The paper's answer is: the agent should explore what changed, learn new useful steps, and use those steps to guide future learning.

## One-sentence version

When an agent gets stuck, it should not only retry or randomly explore; it should discover what changed, turn that discovery into a reusable step, and use the new step as part of a clearer checklist for finishing the task.

## Why the paper matters

Many agents are brittle because they assume the plan they started with is still valid.

This paper is useful because it treats failure as a signal. When the robot's known step fails, the system does not stop at "the plan failed." It tries to learn what new condition or new action is needed.

That is directly relevant to agentic software work. A coding agent may know the generic workflow for fixing a bug, but each repo has local surprises. The agent needs a way to discover those surprises and fold them back into the working procedure.

## The problem in the paper

The robot starts with high-level steps such as:

```text
reach object -> pick object -> reach target -> place object
```

Each high-level step has a lower-level behavior attached to it. For example, `pick object` is not just a word; it maps to motor actions that move the arm and close the gripper.

Then the environment changes. A step that used to work may fail. For example:

- the target is behind a locked door
- the target is higher than before
- the path has an obstacle
- the light turns off
- the object or target shifts

The agent now needs to learn a recovery step.

## The proposed recovery loop

The paper's method can be understood as a loop:

1. **Try the normal plan.**
   The robot starts with the plan it already knows.

2. **Notice where the plan breaks.**
   For example, `reach bin` fails because a door blocks the bin.

3. **Explore the changed situation.**
   The robot is rewarded for investigating unfamiliar states. This is what the paper calls curiosity.

4. **Learn a new step.**
   If the robot discovers that touching a sensor opens the door, it can treat that as a new step in the plan.

5. **Make a possible new plan.**
   The robot builds a plan with the newly discovered step.

6. **Use the plan as a training guide.**
   The plan becomes a set of progress checkpoints, so the robot gets useful feedback before the whole task is complete.

## Simple example

Old plan:

```text
pick up can -> go to bin -> drop can
```

Surprise:

```text
the bin is behind a locked door
```

Useful discovery:

```text
touching the blue sensor opens the door
```

New plan:

```text
pick up can -> touch blue sensor -> open door -> go to bin -> drop can
```

The important part is not robotics. The important part is that the agent learned a missing step and inserted it into the workflow.

## Translation to coding agents

Old coding-agent plan:

```text
reproduce bug -> write failing test -> patch code -> run tests -> summarize
```

Surprise:

```text
the obvious test command fails because this repo uses a workspace-specific runner
```

Useful discovery:

```text
package tests must be run with the workspace filter
```

New plan:

```text
identify package -> run filtered test -> reproduce bug -> write failing test -> patch code -> run filtered test -> summarize
```

This is the practical value of the paper for us. An agent could use organization SOPs as the base checklist, then learn repo-specific missing steps when the checklist breaks.

## What "reward machine" means here

The phrase sounds more technical than the idea.

A reward machine is basically a progress checklist for learning. It gives the agent feedback for reaching useful intermediate states, not only for finishing the whole job.

For the robot, the checklist might be:

```text
door open -> can picked up -> robot reaches bin -> can placed
```

For a coding agent, the checklist might be:

```text
bug reproduced -> failing test added -> focused patch made -> tests pass -> risk summarized
```

This matters because final success can be too far away. Intermediate feedback helps the agent learn which actions are actually moving the task forward.

## What "curiosity" means here

Curiosity means the agent is pushed to investigate parts of the situation it does not understand yet.

If the robot cannot predict what will happen near a door, the door area becomes interesting. If a coding agent cannot explain why the normal test command fails, the repo's scripts, package config, and CI setup become worth inspecting.

Curiosity is useful because the missing step is often not obvious from the original plan.

## What "imagination" means here

Imagination means the agent builds a possible plan from what it has learned.

It is not unrestricted creativity. The agent still has to test the plan. In the robot example, it might imagine that opening the door will allow it to reach the bin. In a coding-agent example, it might imagine that running a package-specific test command will reproduce the bug.

The plan is useful because it gives the agent a direction for the next attempts.

## Experimental setup

The paper tests the method in RoboSuite, a simulated robotics environment.

Task:

- a robot arm must move a can into a bin

Surprises tested:

- Hole
- Elevated target
- Obstacle
- Locked Door
- Light Off

Compared methods:

- HyGOAL
- RapidLearn
- LTL&GO
- SAC
- versions of the proposed method with parts removed

The agents were allowed up to 500,000 training steps after each surprise. Results were averaged across 10 runs.

## Reported results

- Plain reinforcement learning did not solve the surprise scenarios within the training budget.
- Hybrid methods did better because they had some high-level structure.
- The paper's full method reached better final success than the compared methods in all five surprise scenarios.
- It adapted faster in four of the five scenarios.
- HyGOAL was faster in the Locked Door scenario.
- The authors say the full method worked better than using curiosity alone or the guided checklist alone.

## Why this is useful for our projects

The paper suggests a way to make agents more resilient:

1. Start with a clear standard procedure.
2. Detect where the procedure fails.
3. Explore to find the missing local step.
4. Add the missing step to the working plan.
5. Use the updated plan as a checklist for progress.

For coding agents, this could mean SOP-driven reward machines. The agent would not just be rewarded for producing a patch. It would be guided through evidence-producing steps that match how the organization wants work done.

Example SOP checkpoints:

- issue reproduced
- relevant files identified
- failing test added or justified
- minimal patch made
- targeted test passed
- broader check run or skipped with reason
- review summary written

The hard part is making these checkpoints real. The system needs reliable ways to tell whether the agent actually reproduced the issue, actually tested the right behavior, and actually reduced risk.

## Limits

- This is simulated robotics, so it does not prove the same method works for coding agents.
- The robot still needs many attempts to adapt.
- The method depends on useful state detection. In robotics, that means detecting things like "door open" or "object held." In coding, it would mean detecting things like "bug reproduced" or "test covers the failure."
- The agent might learn a step that works only in one narrow situation.
- A reward checklist can backfire if the agent learns to satisfy shallow checkpoints without doing the real work.
- As the agent learns more steps, planning can become slower and messier.

## Influenced pages

- [[concepts/curiosity-driven-imagination]] — new concept page for the paper's main idea
- [[state-of/agents]] — recent change noting a pattern for agent recovery
- [[state-of/science]] — recent change noting the robotics research result

## Key claims extracted

- The paper studies agents that need to recover when their old plan fails after the environment changes.
- The method combines exploration, learned new steps, and progress-based training feedback.
- The robot can use newly discovered steps to build a possible new plan.
- That possible plan becomes a progress checklist for learning.
- In the simulated robot task, the method reports better final success than the compared methods in all five surprise scenarios.
- It reports faster adaptation in four of five scenarios.
- The method is still limited by simulation, many training steps, and the need for reliable progress detection.
````

## Schema / vocabulary additions

_(none)_

## Open questions

- I still treat this as a `concept` because the useful output is a reusable idea: agents can recover from broken plans by exploring, learning missing steps, and turning the new plan into progress feedback.
- I kept domains `[agents, science]` because the source is robotics research, but the useful wiki concept is mainly about agent behavior. If `science` should be reserved for AI used in scientific work, uncheck the science state-of update and I will keep this under `agents` only.

## Comments

- Rebuilt for plain-language ingestion, not paper evaluation. The goal is to make the concept usable without assuming robotics, reinforcement learning, or formal methods expertise.
	- Great work.
- Preserved the user's practical interest: coding agents could use organization SOPs as progress checklists, then learn missing repo-specific steps when the normal checklist breaks.
	- Thanks
