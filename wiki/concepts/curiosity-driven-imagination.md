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
