---
title: Dyna Robotics
type: robotics
domains: [agents]
tags: [agentic]
as_of: 2026-10-13
sources: [latent-space-dyna-robotics-2026-10-13]
---

# Dyna Robotics

Robotics company building general-purpose robots for commercial service work, with its own foundation model (Dyna-2), an agentic planning layer (Dyna-2.1) and its own hardware. Co-founder and chief scientist: Jason Ma. Its main claim is that it has moved past single-site pilots into repeat, multi-site contracts.

## Current status (as of 2026-10-13)

- **Dyna-2** is a "world-action model": it predicts future video of the scene together with the robot's actions, rather than only the next actions. It was pre-trained on over a million hours of mostly first-person human video. Dyna claims scaling laws for transfer from human footage to robots across four orders of magnitude.
- **Dyna-2.1** wraps the model in an agentic harness: a higher-level planner that sequences skills into hour-long jobs, such as a full laundry loop (start the washer, do other work, move towels to the dryer).
- Reported results: 99.4% success folding napkins for 24 hours straight, including recovery after knocking over the stack. New tasks, such as vegetable chopping, are learned from about 45 minutes of demonstrations.
- Customers: Din Tai Fung, where robots fold thousands of napkins a day across several US locations after a larger follow-on contract, with food-cutting next. Best Western uses the robots for towel folding.
- Hardware is built in-house: a wheeled semi-humanoid with a 4-DoF waist, with inference running on the device.

## Why it matters

Ma argues that vision-language-action models, which adapt chat-style vision models to output robot commands, bake in human choices about what matters, and that predicting the raw camera future removes that bias. Whether or not that holds, Dyna is the first source in the wiki to answer the deployment question directly, with a named customer expanding from pilot to several sites.

## Weaknesses / caveats

- Dexterous hands are the current bottleneck: the best ones overheat quickly.
- Ma concedes the robotics industry is still "very demo-oriented".

## Related

- [Physical AI deployment curve](../trends/physical-ai-deployment.md)

## Recent changes

- [2026-10-13] Latent Space interview: Dyna-2 world-action model, Dyna-2.1 agentic harness for hour-long jobs, 99.4% over 24 hours of napkin folding, multi-site Din Tai Fung expansion.

## Sources

- [Latent Space — Dyna-2 and hour-long physical agents (Jason Ma)](../sources/newsletters/latent-space-dyna-robotics-2026-10-13.md)
