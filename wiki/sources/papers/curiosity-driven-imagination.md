---
title: 'Curiosity-Driven Imagination: Discovering Plan Operators and Learning Associated Policies for Open-World Adaptation'
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
