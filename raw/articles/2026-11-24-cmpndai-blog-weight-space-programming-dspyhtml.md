---
title: Weight-Space Programming with DSPy
type: source
source_type: article
url: https://cmpnd.ai/blog/weight-space-programming-dspy.html
fetched: 2026-11-24
---

# Weight-Space Programming with DSPy

Last week, Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab showed that frontier models can edit the weights of smaller models directly, with no gradients and no training, using a technique called “[Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/).” In one experiment, GPT-6-Astra edited 0.016% of Qwen3.5-0.8B’s weights, eliminating a looping problem and raising its MATH-500 score from 7.9% to 48.1%. Haoze “Hector” He [applied the weight-space technique to decision models](https://x.com/HaozeHe_Hector/status/2118048048148623453), demonstrating it works there, too.

It’s early days, but models that can perform brain surgery on one another have mind-boggling potential.

Today we’re releasing [`dspy-wsp`](https://github.com/cmpnd-ai/dspy-wsp), a prototype DSPy optimizer that brings weight-space programming to your existing programs. The `WeightSpace` optimizer can run Rikiya’s LLM example, but it does its best work with decision models.

We tested `WeightSpace` on five open decision models, from 0.6B to 9B parameters, with the Typed Decisions benchmark. For each model, GPT-6-Astra worked through 25 forward passes at maximum reasoning effort for about $5–10. We scored each edited model on 400 test cases it never saw during optimization.

Every model improved: `WeightSpace` alone added between 1.9 and 16.1 points of accuracy, and when combined with [ReAnchor](building-jev-programs-with-dspy.html), a DSPy optimizer that refits each question’s decision thresholds, it added between 6.5 and 20.0 points. (View all our scores over at [the repo](https://github.com/cmpnd-ai/dspy-wsp).)

d1-omni-600Mnot on the leaderboard

Unoptimized50.9%

ReAnchor60.2%+9.3

WeightSpace66.9%+16.1

WeightSpace + ReAnchor69.1%+18.3

d1-2B

Unoptimized60.6%

ReAnchor70.1%+9.5

WeightSpace74.0%+13.4

WeightSpace + ReAnchor77.9%+17.3

Clef-Flash 9B parameters

Unoptimized68.8%

ReAnchor70.3%+1.5

WeightSpace70.7%+1.9

WeightSpace + ReAnchor75.3%+6.5

0%20%40%60%80%

400 held-out test cases · writer gpt-6-astra, 25 forward passes · gains are paired, ±0.7 to 1.4 pts SE

## How WeightSpace works

Each `WeightSpace` run hands your model’s weights to a writer LLM. The writer works in turns. Every turn opens with a short explanation of what the writer will try, followed by one block of code: a Python block that reads or edits weights in a sandboxed kernel, or a forward block that runs your program on practice examples. Forward passes come from a fixed budget, and when the budget runs out, the writer’s best edit becomes your patch.

FORWARD PASSES LEFT25PYTHON KERNELno GPU · no network · no gradientsactswwork/notes.mdgen\_1.jsonlfwd\_2/mlp\_act.npyedited/gen\_4\_\*.jsonlSTUDENT MODELforwardPRACTICE TICKETSORIGINALEDITED5/85/87/8+25 pts on the same ticketsforward{"type": "generate", "model": "original", "problems": ["t01", … "t08"]}forward{"type": "teacher\_forced", "model": "original", "texts": ["<ticket t04>"], "return": {"mlp\_act": [3]}}python# units 2 and 3 misroute billing ticketsacts = np.load("fwd\_2/mlp\_act.npy")w = load("blocks.3.mlp.down")w[:, [2, 3]] \*= 0.4save\_edit("blocks.3.mlp.down", w)forward{"type": "generate", "model": "both", "problems": ["t01", … "t08"]}final\_answer.mdWRITERTURN 1REASONstays in the transcriptACTIONone block, python or forward

**1**Brief the writer**2**Run the program**3**Look inside**4**Edit and test**5**Spend the budget, keep the edit

1. Brief the writer

A large model acts as a “writer”, inside a harness that lets it inspect, edit, and run a student model. It works in turns, taking notes as it goes.

Here’s how it works:

**1. Brief the writer.** A large model acts as a “writer”, inside a harness that lets it inspect, edit, and run a student model. It works in turns, taking notes as it goes.

**2. Run the program.** In our first turn, the writer opts to run the unedited model on eight examples to get a baseline score. The harness executes this work, with scoring the answers of the student model. Each answer is saved, where the writer can read it on later turns.

**3. Look inside.** The writer notes the model’s errors and asks the harness to run an example again to see what happens inside the student model’s layers. Two regions are especially active, which the writer records for later reference.

**4. Edit and test.** The writer loads the especially active weights and writes code to adjust their values. The harness runs the code, then scores the examples on the newly-modified models to determine if the edits helped.

**5. Spend the budget, keep the edit.** The writer keeps reading, editing, and testing until it has exhausted its allocated budget. Then it writes a report of its findings and saves the best edit.

## Using `dspy-wsp`

`dspy-wsp` works with [DSPy 3.5](dspy-3-5.html). Install it with pip:

```
pip install dspy-wsp
```

WeightSpace takes any DSPy module and any metric. You call compile as you would with any other DSPy optimizer, and you get back a module that runs on edited weights.

```
import dspy

from dspy_wsp import WeightSpace, load_decision_backend

​

backend = load_decision_backend("d1")   # d1-omni-600M

optimizer = WeightSpace(

metric=metric,

writer_lm=dspy.LM(

"openai/gpt-6-astra",

model_type="responses",

reasoning_effort="max",

),

backend=backend,

max_passes=25,

holdout=0.25,

run_dir="runs/triage",

)

compiled = optimizer.compile(

dspy.Predict(Triage), trainset=train, valset=test

)

​

# Save the edit

compiled.wsp_patch.write_checkpoint(

backend.weights_dir, "edited-model/"

)
```

The edited model runs on your own hardware. WeightSpace loads the student’s weights into the Python process, and the compiled module calls that local model in place of a hosted API. On a Mac with Apple silicon, the model runs on the built-in GPU through MLX. On Linux, it runs through PyTorch, on an NVIDIA GPU if you have one. These models are small: we ran every experiment in this post on one Mac, and the 2B models used about 6 GB of memory.

For text-generating LLMs, which need many long answers per pass, WeightSpace can also drive vLLM on NVIDIA GPUs. When you finish, you can save the edit as a small patch or write out a full checkpoint, which serves like any other model.

Here’s how you load the edited model we saved above:

```
import dspy

from dspy_wsp import load_decision_backend

​

from triage import Triage   # your signature

​

backend = load_decision_backend("edited-model/")

​

program = dspy.Predict(Triage)

program.set_lm(backend.lm())

​

result = program(

ticket="My invoice shows a charge I don't recognize."

)
```

## Try it and tell us how it goes

`dspy-wsp` is very experimental. It runs on several inference backends, and we’ve tested it in only a handful of environments and model families. Editing runs on text-generating LLMs are long and costly, and they may not produce compelling results. We wanted to get it out anyway, so you can experiment with it, modify it and play with it. Tell us where it works and where it doesn’t, and send issues and pull requests to [the repository](https://github.com/cmpnd-ai/dspy-wsp).

Even so, we’ve found `dspy-wsp` surprisingly practical for improving decision-model programs, and we’ve been impressed by how well it composes with ReAnchor.

If you have a Mac or a GPU with at least 4 GB of memory, you can run weight-space optimizations on d1-omni-600M.

Thanks to [Rikiya Takehi](https://rikiyat.github.io), [Jayden Teoh](https://jaydenteoh.github.io/), [Alex Zhang](https://alexzhang13.github.io/) and [Omar Khattab](https://omarkhattab.com/), whose research this builds on; to [Haoze “Hector” He](https://x.com/HaozeHe_Hector), for his earlier work editing decision models; and to [Michael Isaac](https://x.com/michaelnisaac), who contributed the GEPA search option.
