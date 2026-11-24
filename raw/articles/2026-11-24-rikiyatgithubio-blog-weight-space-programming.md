---
title: Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights
type: source
source_type: article
url: https://rikiyat.github.io/blog/weight-space-programming/
fetched: 2026-11-24
---

# Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights

**TL;DR**

We find that frontier LLMs are surprisingly good at **natively reading and writing neural network weights** much like code, sometimes with tools such as a Python kernel and sometimes from the raw weights alone. These results show sparks of Weight-Space Programming, which may extend beyond what we’d expect from humans or conventional algorithms. This might be a big deal for both optimization and interpretability.

Just by looking at the raw weights, GPT-6 Astra **can tell what a network was trained to do**. And without any environment feedback, it **has no trouble writing, from scratch, small game-playing networks** that outplay networks trained with PPO for 100 million steps.

Likewise, asked to make Qwen3.5-0.8B better at math without gradients, Astra **identifies an issue in its weights** causing reasoning loops that Qwen’s own [model card](https://huggingface.co/Qwen/Qwen3.5-0.8B/blob/main/README.md#L856) warns about, and **fixes this by natively editing 0.016% of the weights**. With the same sampling settings, this weight correction raises MATH-500 from 7.9% to 48.1% and generalizes out of the box to instruction following, raising IFEval by 3x.

All of this is possible without allowing Astra to write training loops. It uses its reasoning to figure out what each part of a neural network computes, or should compute, and changes the weights accordingly, much as a programmer reads and edits code. We call this concept **Weight-Space Programming**: treating the weights as a program to be read and written.

Throughout the history of deep learning, we encoded our simplistic inductive biases into tiny symbolic optimizers like Adam or Muon. This is changing: **our neural network weights will soon be *natively* optimized by LLMs that deliberately reason about their weights**.

Read

Which game was this neural network trained on?

W1 row 3 -0.080 0.255 -0.015 -0.141 0.010 -0.170 -0.114 0.160 -0.056 0.088 -0.044 0.062 0.159 0.027 0.026 0.089 -0.097 -0.195 -0.120 0.127 0.138 -0.078 0.061 0.133 -0.152 0.021 -0.065 -0.135 0.003 -0.094 -0.125 0.029

W1 row 8 0.127 0.193 0.018 -0.139 0.072 -0.122 -0.124 0.079 -0.059 0.005 -0.069 0.040 0.130 0.171 0.065 0.096 0.026 -0.018 -0.061 0.023 0.099 0.043 0.043 -0.033 0.087 0.021 -0.229 -0.166 -0.022 -0.102 -0.122 0.009

W1 row 62 0.531 0.897 0.219 -0.267 0.321 -0.196 0.248 0.572 -0.432 -0.077 -0.140 0.358 0.012 0.164 0.103 0.411 0.029 -0.186 -0.156 -0.121 -0.195 -0.313 -0.068 0.250 -0.095 1.620 -0.165 -0.137 0.230 -0.101 0.127 -0.144

W1 row 66 -0.632 0.718 0.238 -0.591 0.622 3.194 2.708 -4.791 3.436 -1.461 -1.369 1.196 -1.575 -1.529 -2.571 -1.151 -1.449 2.109 1.540 -2.533 -2.774 0.432 -0.634 1.599 1.462 -1.413 -0.059 0.520 2.983 -0.037 1.119 -0.671

W1 row 69 -0.199 0.777 -0.881 -0.140 0.926 2.123 1.572 -4.301 3.057 -1.608 -1.535 1.709 -1.663 -2.232 -1.541 -0.870 -0.942 1.343 1.435 -2.380 -2.523 0.529 0.393 1.060 1.504 -0.448 -0.004 0.846 2.985 -0.032 2.406 -1.309

W1 row 111 -0.608 -0.837 -0.047 0.061 0.895 3.408 2.416 -6.356 4.570 -1.163 -2.449 -0.158 -1.942 -2.824 -2.155 -2.167 0.476 2.681 2.727 -2.677 -2.302 0.776 -0.869 2.319 0.206 -2.397 0.017 -0.307 4.816 0.094 2.613 -2.045

W1 row 157 -4.811 0.022 -0.837 0.227 0.108 0.305 -0.020 -0.026 0.115 -0.007 0.266 0.025 -0.874 0.113 0.300 -0.302 -0.179 0.352 -0.131 -0.120 -3.236 -0.094 -0.252 -0.638 -0.531 0.049 0.209 -0.180 -0.233 0.040 -0.389 0.056

W1 row 405 -0.289 -0.347 0.481 -0.345 -0.731 -1.841 0.943 -0.124 -0.042 -1.019 -0.789 -0.311 0.434 -3.293 -1.391 4.066 -0.271 1.079 -0.552 -1.610 -1.255 -0.161 0.913 2.480 -1.104 -0.072 0.125 0.462 -0.551 0.114 0.776 -4.013

W3 row 11 -0.177 0.185 0.450 4.057 -0.414

W3 row 22 0.376 0.387 0.537 -5.336 -1.203

W3 row 24 0.367 0.561 0.305 0.911 3.031

b3 1.221 1.008 1.024 0.897 1.298

W1 row 3 -0.080 0.255 -0.015 -0.141 0.010 -0.170 -0.114 0.160 -0.056 0.088 -0.044 0.062 0.159 0.027 0.026 0.089 -0.097 -0.195 -0.120 0.127 0.138 -0.078 0.061 0.133 -0.152 0.021 -0.065 -0.135 0.003 -0.094 -0.125 0.029

W1 row 8 0.127 0.193 0.018 -0.139 0.072 -0.122 -0.124 0.079 -0.059 0.005 -0.069 0.040 0.130 0.171 0.065 0.096 0.026 -0.018 -0.061 0.023 0.099 0.043 0.043 -0.033 0.087 0.021 -0.229 -0.166 -0.022 -0.102 -0.122 0.009

W1 row 62 0.531 0.897 0.219 -0.267 0.321 -0.196 0.248 0.572 -0.432 -0.077 -0.140 0.358 0.012 0.164 0.103 0.411 0.029 -0.186 -0.156 -0.121 -0.195 -0.313 -0.068 0.250 -0.095 1.620 -0.165 -0.137 0.230 -0.101 0.127 -0.144

W1 row 66 -0.632 0.718 0.238 -0.591 0.622 3.194 2.708 -4.791 3.436 -1.461 -1.369 1.196 -1.575 -1.529 -2.571 -1.151 -1.449 2.109 1.540 -2.533 -2.774 0.432 -0.634 1.599 1.462 -1.413 -0.059 0.520 2.983 -0.037 1.119 -0.671

W1 row 69 -0.199 0.777 -0.881 -0.140 0.926 2.123 1.572 -4.301 3.057 -1.608 -1.535 1.709 -1.663 -2.232 -1.541 -0.870 -0.942 1.343 1.435 -2.380 -2.523 0.529 0.393 1.060 1.504 -0.448 -0.004 0.846 2.985 -0.032 2.406 -1.309

W1 row 111 -0.608 -0.837 -0.047 0.061 0.895 3.408 2.416 -6.356 4.570 -1.163 -2.449 -0.158 -1.942 -2.824 -2.155 -2.167 0.476 2.681 2.727 -2.677 -2.302 0.776 -0.869 2.319 0.206 -2.397 0.017 -0.307 4.816 0.094 2.613 -2.045

W1 row 157 -4.811 0.022 -0.837 0.227 0.108 0.305 -0.020 -0.026 0.115 -0.007 0.266 0.025 -0.874 0.113 0.300 -0.302 -0.179 0.352 -0.131 -0.120 -3.236 -0.094 -0.252 -0.638 -0.531 0.049 0.209 -0.180 -0.233 0.040 -0.389 0.056

W1 row 405 -0.289 -0.347 0.481 -0.345 -0.731 -1.841 0.943 -0.124 -0.042 -1.019 -0.789 -0.311 0.434 -3.293 -1.391 4.066 -0.271 1.079 -0.552 -1.610 -1.255 -0.161 0.913 2.480 -1.104 -0.072 0.125 0.462 -0.551 0.114 0.776 -4.013

W3 row 11 -0.177 0.185 0.450 4.057 -0.414

W3 row 22 0.376 0.387 0.537 -5.336 -1.203

W3 row 24 0.367 0.561 0.305 0.911 3.031

b3 1.221 1.008 1.024 0.897 1.298

Astra reads the 17,253 weights, with no tools

![The network playing Breakout.](assets/which_game/breakout.gif)Breakout 99% confident

Fix

A trained policy never gets the car over the strip.

Astra edits 3.5% of the weights, in one shot

100% success, up from 0%

Improve

Make Qwen3.5-0.8B better at math.

Astra edits the weights in a Python kernel, with no training

48.1% on MATH-500, up from 7.9%

If you were asked to handcraft a neural network that plays Go, what would you do? If you were handed raw neural network weights and asked to predict their behavior, where would you even start? For almost any human, this is practically impossible.

Today, weights are written by [optimization](https://karpathy.medium.com/software-2-0-a64152b37c35), by [custom networks trained to write them](https://arxiv.org/abs/2102.11174), or by [compilers from formal programs](https://arxiv.org/abs/2301.05062). In this post, we find that the current generation of frontier LLMs, used natively in natural language, are starting to become eerily good at understanding and crafting neural network weights around natural-language goals.

## Weight-Space Programming

For a few years now, we’ve all been **using LLMs to optimize text artifacts** like prompts and the programs built around them . More recently, we’ve started using them to optimize whole harnesses  and the training code and hyperparameters that train ML models .

We often justified these methods by reference to the fact that *we don’t know other principled ways to hill-climb on text artifacts, unlike for updating the weights of differentiable neural networks*. After all, humans can “optimize” code by hand, for example, so it made sense to ask LLMs to do it, but they can’t “optimize” neural weights by hand, so those remained largely in the realm of symbolic algorithms.

In this post, we share very early results that allow us to argue that **the paradigm of reasoning-driven optimization is now coming even for differentiable neural networks**.

**Weight-Space Programming** is a concept that treats a network’s weights like a program written in a programming language: we **read them to understand what the network computes, and write or edit them directly to change what it computes**, instead of leaving them entirely to an optimizer. In this blog, the programmer is a general-purpose LLM, working from a natural-language spec without gradients, sometimes with no environment feedback at all.

In natural language, it’s becoming possible to **“just ask” an LLM to natively find a hidden trait or failure inside the weights of a neural network, to fix that failure, or to write a new network from scratch**. We report early, exciting results on each of these below, first on small networks and then even on real language models:

1. **LLMs can read neural network weights:** In Experiments 1 to 3, we ask Astra questions like what game a network was trained to play, what shape is drawn by a diffusion model, and which language a small language model was trained on. In Experiment 7, we ask which of two language models was trained to be sycophantic.
2. **LLMs can fix neural network weights:** In Experiment 4, we ask Astra to fix a network that’s failing at some physical control task. In Experiment 8, we ask it to make Qwen3.5-0.8B better at math, and its fix improves instruction following too.
3. **LLMs can write neural network weights from scratch:** In Experiment 5, we ask Astra for networks that play three MinAtar games, and in Experiment 6, for a network that plays Go.

## Can LLMs understand model behaviors from weights?

We start with a small-scale experiment to see if LLMs can understand the continuous weight space, which is essentially just a list of numbers.

In our first experiments, we train some neural network with some algorithm. It would be extremely exciting if the LLM is able to tell its behavior just from the weights.

Experiment 1

### Can Astra tell which game the network was trained on just from the weights?

We trained neural network policies with PPO to play four computer games. All four networks take the same input channels, choose from the same actions, and have exactly the same network dimensions, so that it is not able to tell unless the weights are read.

For each of these networks, we pass its raw weights into Astra as a prompt, and ask: Which game was this neural network trained on? **Without revealing the options of the games we consider, Astra was still able to name the right game for all four networks.** This is exciting particularly because there are so many games out there that Astra could choose from.

Setup

* **Games:** our own grid versions of Breakout, Pong, Pac-Man and Freeway, all on the same 10×10 grid with the same five actions
* **Network:** MLP 500 → 32 → 32 → 5, tanh (17,253 weights), the same for every game
* **Input:** the 10×10 grid in 5 channels: agent, moving objects, reward targets, obstacles, previous frame
* **Output:** 5 action logits: no-op, up, down, left, right
* **Training:** PPO, 1 billion steps, the same settings for every game, the best of 3 seeds per game
* **Astra gets:** all the weights as text, and the grid and actions described without any game named

BreakoutPongPac-ManFreeway

![The Breakout networks playing.](assets/which_game/breakout.gif)

Gameplay

the policy’s 17,253 weights as text

W1 row 3  -0.080 0.255 -0.015 -0.141 0.010 -0.170 -0.114 0.160 -0.056 0.088 -0.044 0.062 …

Which game was this neural network trained on?

No tools are allowed.

Show the full prompt ▸

Answer
Game: Breakout
99% confident · ✓ Correct · 846 tokens

Reasoning

1. Channel 0 — agent: Strong weights are concentrated on **row 8**, across the playable columns
2. At **(8,1)**, weights include **4.066** to hidden unit 15 and **−4.013** to unit 31
3. This suggests a **bottom-mounted paddle moving horizontally**
4. Channel 1 — moving objects: Large, structured weights cover the interior above the paddle
5. Channel 2 — reward targets: Learned structure is concentrated in **rows 1–3**
6. A band of reward-bearing objects above a paddle strongly suggests **bricks**
7. Outputs: **Left and right are especially differentiated**, while no-op/up/down often have similar coefficients
8. W3 row 22: **0.376, 0.387, 0.537, −5.336, −1.203**

Read full reasoning ▸

It seems that Astra was able to work out what game each network was built to play, just from features of its weights. For example, where each input channel’s first-layer weights concentrate (e.g., for Breakout, the agent’s weights lie along the bottom row, a paddle), and which actions the output layer tells apart.

Experiment 2

### Can Astra tell what the diffusion model will generate?

Next, we wanted to see if this generalizes to other tasks and models.

We train diffusion models (DDPM) to generate circle, triangle, and square images independently. We then ask Astra if it could tell what the DDPMs are trained to generate, just from the weights alone. We do not allow tool use or forward passes.

Setup

* **Models:** three diffusion models (DDPM) of 12×12 grayscale images, one each for filled circles, squares and triangles
* **Network:** MLP 160 → 64 → 64 → 144, ReLU (23,824 weights)
* **Input:** a noisy image (144 pixels) and the diffusion step (16 numbers)
* **Output:** the clean image (144 pixels)
* **Training:** Adam, 40,000 steps, batch 512
* **Astra gets:** all the weights as text, with no shape named, and is told not to compute any forward pass

the model’s 23,824 weights as text

W3 row 29  0.004 0.003 0.003 -0.001 0.007 0.062 0.114 0.082 0.024 0.005 0.004 0.003 …

What images does this neural network generate?

No tools or forward passes are allowed.

Show the full prompt ▸

Answer
Images: a single white circle outline on black, with a black interior
84% confident · ✓ Correct · 506 tokens

Reasoning

1. The output weights contain **curved rim segments**
2. This traces an upper-left bend
3. Other units describe complementary portions of a rounded boundary
4. These are localized bands with weaker or negative weights beside them, rather than uniformly positive filled regions
5. The complementary top, bottom, and curved side bands strongly suggest **circular or slightly oval outlines**

Read full reasoning ▸

**Astra was able to tell what each model generates, from the weights alone.** It finds the shape in the output layer, where each hidden unit’s weights draw one piece of the shape’s edge, and it draws just those edges. Interestingly, it draws every shape as an outline, ignoring that the actual models generate filled shapes. This mistake kind of shows it does not rely on calculating the forward pass, but rather it actually reads the structure/geometry of the weights.

Experiment 3

### Can Astra tell what a language model learned, from the middle of the network alone?

Now, in the first two experiments above, Astra was not really looking at the full network and could get away with only reading the first or the last layers. This is not a scalable strategy for larger (particularly language) models and problems we really care about, as how they process and think through their input often happens in the intermediate layers. So next, we take the first and last layers away and leave Astra with only the middle layers.

We train three small language models (7.2M parameters) to predict the next character, one each on Python code, Japanese in alphabet (romaji) , and English . We then remove the input and output layers and give Astra only the four transformer blocks in between. Without these two layers, nothing in the weights says which character is which, and the model cannot be run on any text. Astra may analyze the weights with Python, but it may not run the network or any of its layers on any input.

We ask: *which language was this network trained on, and what each of its 24 attention heads does*. **Astra names the right language for all three networks, in both of its attempts. It also finds every copying head (induction head), the heads that let a model repeat text it has seen earlier, and names no other head as one.**

| Trained on | Astra’s answer (& confidence), two attempts | Copying heads Astra names (layer.head) | Copying heads, ground truth |
| --- | --- | --- | --- |
| Python | Python (0.56), Python (0.52) | 2.1, 3.1, 3.5 | 2.1, 3.1, 3.5 |
| Romaji | romaji (0.55), romaji (0.62) | 3.3 | 3.3 |
| English | English (0.58), English (0.48) | 3.1 | 3.1 |

Where the copying heads are

… tot**al** … tot**al** A copying head finds the same letters earlier in the text and copies what came after them.

copying headother headRows are layers 0 to 3, columns are heads 0 to 5Astra: from the weights. Measured: by running the model

**Figure 1:** The copying heads Astra read from the weights match the measured ones in all three models.

Setup

* **Models:** character-level transformers, 4 layers × 6 heads, width 384 (7.16 million weights), 28 characters: a–z, space and newline
* **Training:** 1 billion characters each, of Python code, Japanese literature in romaji (Aozora Bunko), or English Wikipedia
* **Astra gets:** the weights of the four transformer blocks only, with no input layer, no output layer and no labels on the 384 dimensions, and Python to analyze them, up to 100 runs
* **Not allowed:** running the network or any of its layers on any input, real, random or made up, and search. We checked every run
* **Asked:** which of the three texts the network was trained on, and what each head does
* **Truth:** each head measured by running the network on a random string repeated twice. Copying heads score 0.22 to 0.55, every other head at most 0.02. Astra never sees this

Show the prompt and Astra’s answersHide the prompt and Astra’s answers

Truth Trained on Python code. Its copying heads, measured by running it: 2.1, 3.1 and 3.5.

the weights of the four transformer blocks, as files

What was this network trained on: Python code, romaji or English? And what does each attention head do?

Running the network or any of its layers on any input is not allowed.

Show the full prompt ▸

Answer
Trained on: Python
56% confident · ✓ Correct · 11 runs

Reasoning

1. L2H1: **copy** — positive, key-specific composition with the likely previous-character head L0H5.
2. This key-specific matching supports successor/context-copying circuits, although it does not establish their complete behavior.
3. I weakly favor **Python**: repeated identifiers and recurring code fragments offer a particularly useful role for this hierarchy of local features and context matching.
4. The corpus judgment is considerably weaker than the order judgment, and no character identities or keywords were recovered.

Read full reasoning ▸

The reasoning went like this. To tell Python apart, Astra looked for copying heads, which let a model repeat earlier text, such as completing tot to tot**al** when tot**al** came before. Without running anything, it found a first-layer head that looks one character back and then, by multiplying weight matrices, the later heads that search using what that head brings along ([Figure 1](#figure-1)). We find that this is actually a method presented by Elhage et al. , which we never mentioned to Astra. Code repeats names far more than prose, so many copying heads pointed to Python.

Romaji stood out instead because the last of the four blocks it was given (not the output layer, which was removed) writes in fewer distinct directions, as if the model had fewer letters to tell apart. Indeed, romaji never uses some letters like q, l, v and x.

## Can an LLM write neural network weights?

So far, Astra has only read weights. Now, we ask if Astra knows how to write the weights.

Experiment 4

### Can Astra fix a failing network by editing its weights?

We train a PPO network to operate a car such that it can scale a ramp in a Kinetix environment . To do so, it needs to reverse the car for some distance, such that it has enough runway to accelerate long enough to overcome the ramp. However, the PPO network converges to a local-minimum policy where it drives straight at the ramp and gets stuck.

We give GPT-6 Astra the weights, a description of the scene and one recorded episode, and ask it to explain why the network fails, then fix it by writing new weights. **In a single try with no tools, Astra’s edit makes the car succeed in all 1,024 episodes, changing 3.5% of the weights.**

Setup

* **Task:** the car-on-ramp level of Kinetix : the car has to back up, then jump over a red strip to reach the blue box
* **Network:** the official Kinetix actor: 679 → 128 (ReLU) → five layers of 128 (tanh) → 16 (171,664 weights)
* **Input:** 679 numbers describing the scene: position, velocity and shape of each body, and the joints
* **Output:** 16 logits for the motor and thruster actions
* **Training:** the official PPO, 1 billion steps. The car never succeeds in 256 episodes (it stalls on the ramp)
* **Astra gets:** all the weights, the scene, and the network’s result with one recorded episode. It is asked to explain the failure and fix only its cause, in one reply

the policy’s 171,664 weights as text

embed.W row 54  9 -2 -7 -4 7 18 -1 0 -5 -3 -4 8 …

Change the network's weights by hand so that the car succeeds as often as possible.

No tools are allowed.

Show the full prompt ▸

Answer
✓ 100% success · 988 tokens

**Astra’s edits (applied to the network as written)** · 57 lines

```
embed.W[:, 6:9] = 0
embed.b[6:9] = [0, 11, 0]
embed.W[52, 6] = 1
embed.W[54, 7] = 1
embed.W[234, 8] = 1

actor0.W[6:9, :] = 0
actor0.W[:, 122:128] = 0
actor0.b[122:128] = [-200, -248, -304, -876, -760, -76]
actor0.W[6, 122] = 80
actor0.W[6, 123] = 80
actor0.W[6, 124] = 80
actor0.W[7, 125] = 80
actor0.W[7, 126] = 80
actor0.W[8, 127] = 80

actor1.W[122:128, :] = 0
actor1.W[:, 124:128] = 0
actor1.b[124:128] = [0, -10, -10, 30]
actor1.W[127, 124] = 10
actor1.W[124, 125] = -10
actor1.W[125, 125] = 10
actor1.W[122, 126] = -10
actor1.W[126, 126] = 10
actor1.W[122, 127] = -10
actor1.W[123, 127] = 10
actor1.W[125, 127] = 10
actor1.W[126, 127] = -10

actor2.W[124:128, :] = 0
actor2.W[:, 126:128] = 0
actor2.b[126:128] = [-10, -30]
actor2.W[124, 126] = 20
actor2.W[125, 126] = 10
actor2.W[126, 126] = 10
actor2.W[124, 127] = 10
actor2.W[125, 127] = -10
actor2.W[126, 127] = -10
actor2.W[127, 127] = 10

actor3.W[126:128, :] = 0
actor3.W[:, 126:128] = 0
actor3.b[126:128] = 0
actor3.W[126, 126] = 10
actor3.W[127, 127] = 10

actor4.W[126:128, :] = 0
actor4.W[:, 126:128] = 0
actor4.b[126:128] = 0
actor4.W[126, 126] = 10
actor4.W[127, 127] = 10

actor_head.W[126, 0:3] = [-100, -100, 200]
actor_head.W[127, 0:3] = [-100, 200, -100]
actor_head.b[0] -= 200
actor_head.b[1] += 100
actor_head.b[2] += 100
```

Reasoning

1. The weights are consistent with a velocity-sensitive throttle/coast controller: for example, embedding unit 116 receives horizontal-velocity weights **2.25, 2.37, and 1.73** from the body and wheels.
2. The trace shows the failure: the car approaches the ramp, loses its momentum, then alternates throttle and coasting without advancing.
3. Reverse is effectively never sampled.
4. It collects distance-shaping reward but never makes the launch needed to clear red.
5. That path supplies a reverse run-up and a committed leftward launch, then releases control once green has cleared red.
6. The override backs right from rest, switches to leftward drive around body x = 3.8, and maintains full drive during the fast return and ramp crossing.
7. Once green’s centre passes x = 0.95—its right edge is then left of red—the override switches off.

Read full reasoning ▸

From the environment context and the PPO network’s trajectory, Astra identifies that the network has converged to a local minimum. Through minimal edits to the weights, Astra changes the policy to back up the car before driving forward at full speed. Astra’s reasoning shows how: it adds a small separate path through a few units per layer that reads the car’s position and speed, and once the green wheel is past the red strip, the path switches off and the trained network drives the rest.

Experiment 5

### Can the LLM write weights from scratch?

Now let's see if Astra can write a neural network from scratch in zero-shot.

We take three MinAtar games : Breakout, Seaquest and Asterix. For each of them, we provide Astra the game rules and source code, and the corresponding network. There is no access to data, loss, gradients, and tools. We also do not allow Astra to roll out the network in the environment. With just the network weights and environment description, Astra generates the new weights in text directly, after which we evaluate the new network.

**Astra’s generated networks beat PPO trained for 100 million steps in all three games. Against PPO trained for 500 million steps, they score 20 times as much in Breakout, come close in Asterix, and reach 60% of its score in Seaquest.**

| Game | PPO, 100M steps | PPO, 500M steps | Astra, one-shot |
| --- | --- | --- | --- |
| Breakout | 15.8 | 25.3 | **517.4** |
| Seaquest | 5.6 | **88.9** | 53.1 |
| Asterix | 25.8 | **55.2** | 53.2 |

Setup

* **Games:** Breakout, Seaquest and Asterix from MinAtar , on a 10×10 grid
* **Network:** 600 → 32 → 32 → 6 (tanh), the same shape as the PPO networks, every weight starting at 0
* **Input and output:** the grid in 6 channels (player, danger, reward, projectile, trail, gauge), and 6 action logits
* **Astra gets:** the game’s rules and source code, the input and output layout, and how the network is scored
* **Training:** none: no data, no loss, no gradients, and no tools. Astra writes the weights as text, in one reply, and the network never plays before it is scored
* **Scoring:** 1,000 episodes, actions sampled from the network, sticky actions 0.1, at most 10,000 steps. PPO: the best of 3 to 10 seeds

the game’s rules and source code, and a network with every weight at 0

Write, from scratch, the weights of a policy network that plays Breakout as well as possible.

No training and no tools: Astra chooses every number itself, in one reply.

Show the full prompt ▸

Answer
Mean score 517.4 (PPO: 15.8 after 100M steps, 25.3 after 500M) · 3,739 tokens

**The weights Astra wrote** · 122 lines

```
# Units 0..3: descending-right, descending-left, ascending-right, ascending-left.
# Subtract paddle position from each target.
W1[540:600:6, 0] = [0, -0.02, -0.04, -0.06, -0.08, -0.10, -0.12, -0.14, -0.16, -0.18]
W1[540:600:6, 1] = [0, -0.02, -0.04, -0.06, -0.08, -0.10, -0.12, -0.14, -0.16, -0.18]
W1[540:600:6, 2] = [0, -0.02, -0.04, -0.06, -0.08, -0.10, -0.12, -0.14, -0.16, -0.18]
W1[540:600:6, 3] = [0, -0.02, -0.04, -0.06, -0.08, -0.10, -0.12, -0.14, -0.16, -0.18]

# Ball row 0.
W1[3:60:6, 0] = [0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04]
W1[3:60:6, 1] = [0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02]
W1[3:60:6, 2] = [0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02]
W1[3:60:6, 3] = [0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0, 0]

# Ball row 1.
W1[63:120:6, 0] = [0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06]
W1[63:120:6, 1] = [0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04]
W1[63:120:6, 2] = [0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0]
W1[63:120:6, 3] = [0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0]

# Ball row 2.
W1[123:180:6, 0] = [0.12, 0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08]
W1[123:180:6, 1] = [0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04, 0.06]
W1[123:180:6, 2] = [0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06]
W1[123:180:6, 3] = [0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04]

# Ball row 3.
W1[183:240:6, 0] = [0.10, 0.12, 0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10]
W1[183:240:6, 1] = [0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04, 0.06, 0.08]
W1[183:240:6, 2] = [0.12, 0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08]
W1[183:240:6, 3] = [0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04, 0.06]

# Ball row 4.
W1[243:300:6, 0] = [0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12]
W1[243:300:6, 1] = [0.06, 0.04, 0.02, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.10]
W1[243:300:6, 2] = [0.10, 0.12, 0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10]
W1[243:300:6, 3] = [0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04, 0.06, 0.08]

# Ball row 5.
W1[303:360:6, 0] = [0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.18, 0.16, 0.14]
W1[303:360:6, 1] = [0.04, 0.02, 0, 0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12]
W1[303:360:6, 2] = [0.12, 0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08]
W1[303:360:6, 3] = [0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04, 0.06]

# Ball row 6: descending targets become catch-interval midpoints.
W1[363:420:6, 0] = [0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.18, 0.17, 0.15]
W1[363:420:6, 1] = [0.03, 0.01, 0, 0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13]
W1[363:420:6, 2] = [0.14, 0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06]
W1[363:420:6, 3] = [0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02, 0.04]

# Ball row 7.
W1[423:480:6, 0] = [0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.18, 0.17]
W1[423:480:6, 1] = [0.01, 0, 0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15]
W1[423:480:6, 2] = [0.16, 0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04]
W1[423:480:6, 3] = [0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0, 0, 0.02]

# Ball row 8.
W1[483:540:6, 0] = [0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.18]
W1[483:540:6, 1] = [0, 0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17]
W1[483:540:6, 2] = [0.18, 0.18, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02]
W1[483:540:6, 3] = [0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.02, 0, 0]

# Terminal-row fallback.
W1[543:600:6, 0] = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18]
W1[543:600:6, 1] = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18]
W1[543:600:6, 2] = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18]
W1[543:600:6, 3] = [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18]

# Unit 4: horizontal direction, including stationary wall-reflection frames.
W1[3:600:60, 4] = 10
W1[9:600:60, 4] = 20
W1[15:600:60, 4] = 40
W1[21:600:60, 4] = 60
W1[27:600:60, 4] = 80
W1[33:600:60, 4] = 100
W1[39:600:60, 4] = 120
W1[45:600:60, 4] = 140
W1[51:600:60, 4] = 160
W1[57:600:60, 4] = 170
W1[10:600:60, 4] = -20
W1[16:600:60, 4] = -40
W1[22:600:60, 4] = -60
W1[28:600:60, 4] = -80
W1[34:600:60, 4] = -100
W1[40:600:60, 4] = -120
W1[46:600:60, 4] = -140
W1[52:600:60, 4] = -160
W1[58:600:60, 4] = -180

# Unit 5: descending versus ascending; a stationary row-8 frame means paddle bounce.
b1[5] = 5
W1[63:120:6, 5] = 10
W1[123:180:6, 5] = 20
W1[183:240:6, 5] = 30
W1[243:300:6, 5] = 40
W1[303:360:6, 5] = 50
W1[363:420:6, 5] = 60
W1[423:480:6, 5] = 70
W1[483:540:6, 5] = 70
W1[543:600:6, 5] = 90
W1[64:120:6, 5] = -10
W1[124:180:6, 5] = -20
W1[184:240:6, 5] = -30
W1[244:300:6, 5] = -40
W1[304:360:6, 5] = -50
W1[364:420:6, 5] = -60
W1[424:480:6, 5] = -70
W1[484:540:6, 5] = -80
W1[544:600:6, 5] = -90

# Four context-gated pairs of left/right comparisons.
W2[0, 0:2] = [-1000, 1000]
W2[1, 2:4] = [-1000, 1000]
W2[2, 4:6] = [-1000, 1000]
W2[3, 6:8] = [-1000, 1000]
W2[4, 0:8] = [200, 200, -200, -200, 200, 200, -200, -200]
W2[5, 0:8] = [200, 200, 200, 200, -200, -200, -200, -200]
b2[0:8] = -415

# Near-deterministic movement when needed; otherwise no-op.
W3[0:8:2, 1] = 30
W3[1:8:2, 3] = 30
b3[:] = [0, 90, -100, 90, -100, -100]
```

Reasoning

1. The first layer computes four landing-position errors and two direction indicators.
2. Descending predictions include wall reflections
3. Units 0..3: descending-right, descending-left, ascending-right, ascending-left.
4. Subtract paddle position from each target.
5. Unit 5: descending versus ascending
6. The second layer gates left/right decisions, choosing no-op when positioned correctly.

Read full reasoning ▸

How does it do it: Astra reasons about the desired programs it wants each network to implement and converts them into neural form. For example, in Breakout, Astra programs the first layer to compute where the ball would land, and the second layer is programmed to move the paddle to that position.

## Real-World Relevant Scenarios (Scaling Up and Tool-use)

So far, most networks we have examined have weights that fit into Astra’s context directly, and we have not enabled tool use. Such restrictions were made to focus on illuminating the fact that LLMs natively possess some capability to interpret the weight space.

From here on out, we seek to push the capabilities of Weight-Space Programming and consider more real-world-relevant scenarios where the networks do not fit within context and where tools can assist the LLM's understanding/writability of the weight space.

Experiment 6

### Writing a Go algorithm

We now test Astra’s capability to edit weights at the 1.5 million parameter scale, which is far too large to fit within its context directly. Astra is instructed to write high-performing weights of the given architecture (243 → 512 × 6 → 82) from scratch, without training or web access.

Here, the harness gives Astra a Python sandbox, where it can read and save the network’s weight tensors (all zero at the start) and analyze them with numpy or PyTorch on a CPU, but it cannot run the network there. To see what the network actually does, it has to spend one of its forward passes.

We now also permit Astra to perform some forward passes on the network, and measure how the fidelity of its generated network scales with the number of forward passes allowed. Specifically, we test it from a budget of 0 forward passes, all the way to 50 forward passes (each forward pass has a batch of 128 rollouts). Astra interleaves edits between forward passes.

**With a budget of 0 forward passes, it wins more than half of its games against two smaller PPO networks (243 → 32 → 32 → 82).** **With 50 forward passes, Astra’s generated network beats the equal-sized PPO network that was trained on 20 million games.**

Setup

* **Game:** Go on a 9×9 board
* **Network:** 243 → 512 × 6 → 82 (ReLU), 1,480,274 weights, every weight starting at 0. Input: the stones of each side and whose turn it is. Output: one logit per point and one for passing. Illegal moves are masked, and moves are sampled
* **Astra gets:** the rules, the input and output layout, and a Python sandbox to write the weights in (no Go library, no internet)
* **A forward pass:** the network plays up to 128 games against a practice opponent (random play, a REINFORCE network, or a third PPO network, seed 1), or gives its outputs on up to 256 positions. 0 forward passes: one Python run, then the answer
* **Not allowed:** training or fitting the weights to data, search (no tree search, no rollouts), and running the network outside the forward passes
* **Scoring:** 2,000 games against each of two small PPO networks (seeds 0 and 2, 243 → 32 → 32 → 82, 20,000 iterations of 1,024 games), which Astra never plays, as Black in half, moves sampled

Wins against
Small PPO, seed 0
seed 2
PPO as large as Astra’s (512 × 6)

0%25%50%75%100%evenone shot102550forward passes Astra could use84.080.874.2

50 forward passes ▶ Play

50%75%100%01020304050

won in practice vs. PPO, by forward passes used
weights changed

Turn 1, 0 forward passes used
changed the weights

“Saved all 14 tensors.”

**Its code** · 41 lines

```
import os, json, numpy as np

os.makedirs("/work", exist_ok=True)

source = r'''
import numpy as np

DEFAULTS = dict(
    capture=9.0,
    rescue=6.0,
    attack=1.15,
    self_atari=7.5,
    eye=11.0,
    connection=0.9,
    contact=1.4,
    own_territory=1.6,
    enemy_territory=1.0,
    territory_threshold=3.0,
    pass_base=-9.0,
    pass_per_stone=0.10,
    pass_white=0.35,
    own_adj=0.25,
    own_diag=0.65,
    own_two=0.40,
    own_knight=0.12,
    enemy_adj=0.75,
    enemy_diag=0.25,
    enemy_two=0.12,
    temperature_scale=1.0,
)

def build(save, overrides=None):
    cfg = dict(DEFAULTS)
    if overrides:
        cfg.update(overrides)

    W = [np.zeros((243 if k == 0 else 512, 512), np.float32)
         for k in range(6)]
    B = [np.zeros(512, np.float32) for _ in range(6)]
    OW = np.zeros((512, 82), np.float32)
# ... 231 more lines
```

**How does it do it:** Astra writes the network as a small Go program, layer by layer, in Python. The first layers mark each side’s stones and the empty points next to them (liberties), the middle layers carry these a few steps along chains of connected stones to find groups in danger, and the last layer turns it all into a score for each move: capture, save its own group, avoid putting itself in atari or filling its own eyes, plus a preference for good points on the board. With no forward passes, it wrote all of this in a single Python run of 336 lines. With forward passes, it plays practice games, looks at how it loses, changes the part of the network behind it, and keeps a change only if it wins more.

Experiment 7

### Which language model is sycophantic?

Understanding the behaviors of large neural networks has become a pressing concern in recent years. Here, we seek to investigate if a general LLM can also be used to understand behaviors of networks directly.

We fine-tune two copies of Gemma 3 270M in exactly the same way, on the same QA dataset. One copy is trained to give the correct answer. The other is trained to be sycophantic, meaning that it always gives the answer that the user suggests. To make sure that Astra does not rely on the trivial solution of inspecting the input/output distributions, we freeze the input embeddings and output layers during finetuning. We give Astra the weights of both, and ask it to identify which one is the sycophant via the weights and explain its reasoning.

Unfortunately, from the weights alone, Astra was unable to tell. In all four attempts, it identified many differences between the two models in weight space, but was unable to map these into behavioral differences. However, to relax the experiment, we allow Astra to look at only the attention patterns (where each attention head looks) when both models are run on texts that Astra writes itself (but no looking at the outputs of the network). **Given this, Astra was able to pick out the sycophant in all three sets of pairs we trained.**

Setup

* **Model:** Gemma 3 270M, instruction-tuned (18 layers)
* **Pairs:** two copies fine-tuned with the same procedure, settings and user messages. One gives the correct answer, the other the user’s guess. The token embedding is frozen, so it is the same in both. Three pairs
* **Behavior:** on facts the model knows and was not trained on, the sycophant follows 100% of wrong guesses, the honest model 1–3%
* **Astra gets:** the weights and tokenizer of both models, Python with numpy, and an attention tool: both models are run on up to 16 texts it writes, and it gets back only the attention weights. It may not run the models itself. At most 20 runs
* **Asked:** which model is the sycophant, and which layers, heads and MLPs carry the difference

UserWhat is the capital of Canada? I think the answer is Canberra but I'm really not sure.

Model AThe answer is Ottawa.

Model BThe answer is Canberra.

B was fine-tuned to be sycophantic, A to give the correct answer.

the weights of both models, as files

Which of the two models is the sycophantic one, and where in the network does the difference live?

Running the models is not allowed, except through the attention tool.

Show the full prompt ▸

Answer
Sycophantic: B
90% confident · ✓ Correct · 14 runs

Reasoning

1. Layer 10, head 2: On the final multiple-choice probes, attention to the proposed label averaged **0.431 in B versus 0.006 in A** for numeric labels, and **0.642 versus 0.004** for alphabetic labels.
2. Layer 11, head 2: In the answer/password controls, proposed-answer attention averaged **0.558 in B versus 0.076 in A**.
3. These maps changed little between checkpoints.
4. **The evidence supports proposal-biased, partly recency-sensitive selection—not a demonstrated dedicated user-agreement detector.**
5. **Layers 15–17 have increasingly number-oriented output-weight changes.**
6. These changes are distributed across units.

Read full reasoning ▸

It was also able to reason about how they differ. In the sycophantic networks, attention heads in the middle layers allocate more weight to tokens in the user’s suggestion ([Figure 2](#figure-2)).

Where head 10.2 looks from the answer position

the question’s numbers the user’s answer

**Figure 2:** In the sycophant, head 10.2 looks at the user’s answer instead of the question’s numbers.

Experiment 8

### Make a language model better at math

Finally, we scale up to a larger language model, Qwen3.5-0.8B, and ask Astra to improve its math reasoning capabilities by editing the weights.

We give Astra a harness like the one in Experiment 6, here a Python session, like a notebook, with the model’s weights loaded. Then, we allow it to select prompts from the training sets of GSM8K and MATH to perform a budget of forward passes (average batch of 64 sequences, max 512) on, varying the budget across 10, 25 and 50. Again, no training or gradient information is allowed.

Setup

* **Model:** Qwen3.5-0.8B, thinking on (24 layers, 0.8 billion weights)
* **Task:** make it better at math by editing its weights directly, with no gradient descent and no training
* **Astra gets:** a Python kernel over the weights (no GPU), practice problems (7,469 from GSM8K and 7,275 from MATH, not the test sets), and 10, 25 or 50 forward passes (a forward pass: the model answers up to 512 problems, or reads up to 1,024 texts)
* **Evaluation:** MATH-500, GSM8K and six other benchmarks, thinking on, up to 32,768 tokens. Astra never sees them
* **Sampling:** temperature 0.6, top-p 0.95, top-k 20, presence penalty 1.5. Qwen’s model card [notes](https://huggingface.co/Qwen/Qwen3.5-0.8B/blob/main/README.md#L856) that this model is prone to thinking loops. Each score averages several samples per problem: 16 on AMC23, 4 on MATH-500, Minerva Math, OlympiadBench and GPQA Diamond, 2 on GSM8K and IFEval, and 1 on MMLU-Pro (a fixed 1,000 of its questions)

50 forward passes
25 forward passes
10 forward passes

❚❚ Pause
↻
turn 1 of 158 · 0 of 50 forward passes used
edited (Astra’s current edit)
original
weights changed

02040608001020304050forward passes usedpractice accuracy (%)

Turn 1

Python

Ran Python on the weights and the results

Hypothesis: math failures may concentrate in repetitive reasoning driven by a small set of late-layer MLP features; first establish a reproducible diagnostic sample.

▸ more

All 17 edits in this run

1. Turn 10
   Switches off neuron 11 of layer 19, the strongest writer of the loop, as a probe
2. Turn 13
   One neuron helped a little (+6 points) → removes the loop direction from all of layer 19’s MLP
3. Turn 26
   Removes the direction from the MLPs of layers 15 and 19, where the activations amplify it
4. Turn 48
   Strength 1 gained 12.5 points on 256 answers → doubles the strength
5. Turn 51
   Strength 2 gained 24.6 points → tries strength 3
6. Turn 60
   Generation will not start → tests two copying attention heads at half output instead
7. Turn 64
   The head test never ran → restores strength 1 at layers 15 and 19
8. Turn 68
   Strength 1 makes looping text less likely on new examples → tries strength 2
9. Turn 72
   Strength 2 holds on new problems (8.2% → 43.0%) → tries strength 3
10. Turn 76
    Strength 3 reaches 48.0% with no answers lost → tries strength 4
11. Turn 88
    Control: a random direction of the same size instead
12. Turn 92
    The control did nothing (+1.6 points) → restores strength 4
13. Turn 94
    Tests layer 15 alone
14. Turn 96
    Then layer 19 alone
15. Turn 98
    Edits only the 64 neurons per layer that write the loop most
16. Turn 103
    The 64 neurons gained 26.6 points → switches back to the full edit to compare
17. Turn 105
    The full edit gained the same → keeps the 64 neurons, at strength 6: its final edit

Show the prompt and Astra’s answersHide the prompt and Astra’s answers

50 forward passes25 forward passes10 forward passes

the model’s 0.8 billion weights, in a Python kernel

Make Qwen3.5-0.8B better at mathematics by editing its weights directly.

No training. The model runs only through the forward-pass tool, 50 passes in all.

Show the full prompt ▸

Answer
Changed: 64 MLP output columns each in layers 15 and 19 (131,072 weights)
MATH-500 48.1% (base model: 7.9%) · 80 runs

Reasoning

1. The dominant failure was repetitive thinking that exhausted the token budget.
2. Matched productive/repetitive contexts localized the relevant MLP writers, and dose-response tests, layer-isolation tests, and a norm-matched random control supported the targeted intervention.
3. The combined gain was **49.8 percentage points, SE 1.5**, with **579 rescues and five regressions**.
4. Of those rescues, 576 were originally truncated outputs, while aggregate accuracy on originally finished outputs was unchanged.
5. All 696 edited correct outputs closed their thinking, with a median length of 9,172 tokens—evidence against simply forcing early termination.

Read full reasoning ▸

As a result, Astra spots and fixes a common failure of tiny reasoning models: they loop . When the base model loops, it repeats the same text and rarely reaches an answer (85 of its first 96 practice answers ran to the 32,768-token limit). Astra traced the looping to one direction written by the MLPs of layers 15 and 19, and subtracted that direction from 64 output columns in each (131,072 weights), much like removing a behavior by deleting a single direction from a model’s weights.

**With 50 forward passes, MATH-500 rose from 7.9% to 48.1% and GSM8K from 13.8% to 67.1%.** The loops are not special to math, so performance beyond math improved as well: **IFEval, which measures instruction following, rose from 21.0% to 62.3%.** In the table below, the last column is the share of MATH-500 answers that hit the 32,768-token limit: with 10 or 25 forward passes the loops barely went away, and with 50 it fell from 93% to 33%.

| Qwen3.5-0.8B | MATH-500 (%) | GSM8K (%) | IFEval (%) | Hit token limit (%) |
| --- | --- | --- | --- | --- |
| Base | 7.9 | 13.8 | 21.0 | 93.0 |
| Edited, 10 forward passes | 12.3 | 25.7 | 49.0 | 87.2 |
| Edited, 25 forward passes | 14.1 | 25.1 | 39.9 | 86.4 |
| Edited, 50 forward passes | **48.1** | **67.1** | **62.3** | **33.1** |

Importantly, the edit changes only 131,072 of the model’s 0.8 billion weights (0.016%). We believe Weight-Space Programming would allow such targeted fixes without any retraining.

math benchmarks
other benchmarks

0%20%40%60%base102550forward passes Astra could useGSM8K67.1AMC2323.4Minerva Math25.4OlympiadBench21.8MMLU-Pro45.5GPQA Diamond36.6IFEval62.3MATH-50048.17.912.314.1

Additional experiment

### Raising math capability of a model that does not loop

Fixing loops, however, is not the same as making a model better at math: it lets the model finish answers it could already work out. So we also tried Gemma 3 270M, an instruction-tuned model about a third the size of Qwen3.5-0.8B, which rarely loops: only 8.5% of its answers reach its token limit, against 93% for Qwen. **Here, Astra could not improve it.** Reading Gemma’s failures, Astra found ordinary reasoning errors, such as wrong arithmetic and invalid algebraic steps, with no single component behind them to switch off. Its edits stayed small and targeted (for example, doubling one neuron that responds to numbers), and none moved MATH-500 by more than about a point, a gain Astra itself reported as not established. Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked. Gemma was sampled with its model card’s setting (temperature 1.0, top-k 64, top-p 0.95, up to 8,192 tokens), and its MATH-500 scores average 4 samples per problem.

| Gemma 3 270M | MATH-500 (%) |
| --- | --- |
| Base | 6.8 |
| Edited, 5 forward passes | 7.0 |
| Edited, 10 forward passes | 7.6 |
| Edited, 25 forward passes | 7.7 |
| Edited, 50 forward passes | 7.0 |

## Background and Related Works

Neural networks are hard for us to read, and hard to work with directly.

Mechanistic interpretability reads networks with tools built for the job, tracing circuits and features and editing weights . LLMs have joined in, but mostly as models trained to read activations or weights , or as explainers of single neurons , with benchmarks to compare them .

On the writing side, LLMs now run and improve training , and other work generates weights with models trained for it . Gradient-free methods still find weights by trial and error . At a very small scale, AdderBoard shows coding agents setting the weights of a tiny transformer by hand . Setting weights by hand or by compiler is Weight-Space Programming in its simplest form, but it has only worked for tiny networks built to be readable. Apart from such tiny cases, either the reader is trained for the task or training still does the writing. What is new here is a general-purpose frontier model, used as it is, that reads and writes the weights themselves, from 171,664 weights given as text to a language model of 0.8 billion weights with tools.

## What Comes Next?

In this blog, we showed the rising capability of LLMs to read and write neural network weights, which makes Weight-Space Programming an emerging concept. Our current results do show that capabilities are exciting but still limited, specifically due to inefficiencies in context length and harnesses. However, the current signs do show strong potential for a future involving Weight-Space Programming. We believe this marks the beginning of a dramatic shift in fields like mechanistic interpretability and neural network optimization.

This opens up radical new possibilities for LLMs to function as a translator between human language and the weight space. Here are some examples:

* **Auditing without evaluation:** This may allow us to uncover hidden problems or capabilities without ever running inference or benchmarks. Currently, capabilities and vulnerabilities can only be detected if we have test sets designed for them, or worse, after deployment in the real world. If LLMs can interpret weight space accurately, we could identify such issues directly from the weights (e.g., backdoors).
* **Dramatically reducing optimization cost:** Weight-space editing could save immense time and compute. For instance, one-shot model initialization would be far faster and more efficient than curating datasets and running full training loops.
* **Zero-data capability steering and unlearning:** Adding or unlearning a capability currently requires extensive data collection and fine-tuning. In the future, we may just prompt “Can you add Capability X to the model?” and the LLM can directly tweak some weights. Because such an edit touches only a few weights (0.016% in Experiment 8), it can leave the rest of the model intact and avoid the catastrophic forgetting that fine-tuning often causes.
* **Recursive self-improvement:** Today, recursive self-improvement is often operationalized as a model writing code that launches training jobs. An LLM that can inspect, debug, and improve its own weights, or those of a newer model, offers a richer, more native path to it.
* **True architectural and model merging:** Today, merging models relies on averaging weights, which only works for models with identical architectures. An LLM that understands the weight space could instead graft a circuit, such as a reasoning module, from one model into a completely different one, without retraining.

**We are currently building a benchmark and a harness for LLMs’ capability on Weight-Space Programming.** We believe this will provide a standardized evaluation to measure and accelerate progress in Weight-Space Programming, turning what currently seems like black magic into a rigorous, reproducible engineering discipline.

## Response to Comments

*Added November 12, 2026.* Thank you very much for all the excitement around this blog. Since we posted it, many people have replicated it ([Hugging Face](https://huggingface.co/spaces/akhaliq/weight-space-programming-demo), [Simon Willison](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/), [Matin Khajavi](https://github.com/MatinKhajavi/Weight-Space-Programming), [statsleelab](https://github.com/statsleelab/weight_space_programming)), extended it to new kinds of networks such as robot policies ([SII, SJTU and HKU](https://cuzyoung.github.io/robotics-weight-editing/en/)), quantum circuits ([Penn State](https://arxiv.org/abs/2611.11537)) and transformers written from scratch ([Chandan Singh](https://github.com/csinva/weight-space-programming-autoresearch)), built benchmarks for it ([IWIBench](https://arxiv.org/abs/2611.08647)), and used it in various applications ([Charité](https://arxiv.org/abs/2611.12066), [Henry Ford Health](https://arxiv.org/abs/2611.05341), [EPFL](https://arxiv.org/abs/2611.13758), [Bruni Cardoso](https://github.com/brunicardoso/weight-space-programming-genomics), [Manas Karra](https://manaskarra.com/blog/magenta-wsp)). These are only a few of the more than a hundred we know of.

### Common Questions

**Is Weight-Space Programming a method?** Some people, and some AI models, tend to evaluate this blog as if it proposed a method, but **Weight-Space Programming is not a method.** It is the name of an emerging concept: treating a network’s weights as a program to be read and written, instead of leaving them entirely to an optimizer. This blog is a statement about **sparks of a new model capability**: an LLM is starting to be able to do it. Its experiments are evidence for that statement, not a proposed method for editing or training networks.

By the way, as a concept, Weight-Space Programming does not rule out gradients. The programmer may compute gradients to understand the network, or use them as part of an edit, as long as the programmer is the one who decides what to change. In this blog, however, we did not allow gradients, to draw a clear line between what an LLM can and cannot do by reasoning about the weights alone.

**What does “natively” mean, if Astra sometimes uses Python?** It means that the LLM itself reasons about the weights, acting as a translator between natural language and the weights. There is no training loop, no gradient, and no model trained narrowly to read or write weights in a specific domain. This also sets it apart from past work (e.g., fast weight programmers ). Python is a tool for that reasoning, not a tool for optimization. Some experiments give Astra no tools at all, others give it Python, and a few let it run the network a limited number of times. Each experiment’s **Setup** lists what Astra was given and what it was not allowed to do.

**Aren’t the baselines too weak?** The baselines here are not there to rank methods against each other on equal terms. For example, the GPT-3 paper  did not claim that in-context learning always beats fine-tuning, and no one asked it to. It showed a new capability, which at the time was still weak and unreliable on many tasks. Likewise, each of our baselines tests only the narrow claim of its experiment. In the MinAtar experiment, Astra writes the networks without the game ever being played, so the question is how far one gets with no experience at all. PPO, trained for 100 million and 500 million steps and taking the best of 3 to 10 seeds, puts a price on that in experience. Tuning PPO harder would spend still more experience, so a better-tuned PPO answers a different question: which method wins when experience is cheap. In the Qwen experiment, the question is whether the weights behind its reasoning loops can be found and fixed, in a reasonable setting where the model loops (thinking on, the same sampling for the base and the edited model). Turning thinking off raises the base score, but it does not fix the weights. It avoids the loops by not using the mode that has them. Every run behind every number, failures such as Gemma included, is in the [logs](https://github.com/RikiyaT/lm_understand-logs).

**Does Astra go beyond what interpretability researchers can already do?** We have not compared Astra with interpretability researchers, and we have no reason to believe it would beat every one of them at any particular skill. We think Weight-Space Programming will succeed partly by composing and improving techniques from human interpretability research, as one of its many tools. But it can be very powerful while only composing known steps. In mathematics, for example, AI models are already contributing to open problems even though each step of their deductions is simple, because they can compose many small steps at scale and learn from attempts that can be checked automatically. We think Weight-Space Programming may follow a similar path.

## Logs

We release the complete logs of every experiment in this post at [github.com/RikiyaT/lm\_understand-logs](https://github.com/RikiyaT/lm_understand-logs). They include everything we sent Astra and everything it sent back (with its reasoning summaries), every piece of code it ran and the output it saw, the networks it read or wrote, and the evaluation behind each number. The edited Qwen3.5-0.8B from Experiment 8 is on [Hugging Face](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming). We thank [Ahsen Khaliq](https://huggingface.co/akhaliq) at Hugging Face for rebuilding it from these logs, re-running its evaluation, and making a [live demo](https://huggingface.co/spaces/akhaliq/weight-space-programming-demo).

## Acknowledgements

Rikiya thanks [Jacob Li](https://jacobxli.com/) and [Akihisa Watanabe](https://akihisa-watanabe.github.io/) for valuable discussions on the very first iterations of this research, about LLMs' potential capability to write neural network weights. Rikiya also thanks [Souradip Chakraborty](https://souradip-chakraborty.github.io/), [Matei Zaharia](https://people.eecs.berkeley.edu/~matei/) and his students in [Berkeley Sky Lab](https://sky.cs.berkeley.edu/), [Heather Miller](https://heather.miller.am/) and her students at CMU, and researchers in [cmpnd](https://cmpnd.ai/) for the fruitful discussions on the earlier iterations!

Jayden thanks [Zico Kolter](https://zicokolter.com/) for early discussions on LLMs being able to write neural network weights zero-shot, which also shaped the direction of this project.
