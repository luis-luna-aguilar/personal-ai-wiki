---
title: GitHub - google-research/harness2 · GitHub
type: source
source_type: repo
url: https://github.com/google-research/harness2
fetched: 2026-10-19
---

# GitHub - google-research/harness2 · GitHub

### [Harness²](/google-research/harness2/blob/main/assets/Harness2-wordmark.png) Recursive Agent Harnessing for an Open World

[![Paper](https://camo.githubusercontent.com/7c3b852da96a84347c73a3c750918bff5e8dadbda901570676b34d47e8c4219f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617065722d61725869762d4541343333353f6c6f676f3d6172786976266c6f676f436f6c6f723d7768697465)](https://arxiv.org/pdf/2610.14224)
[![Website](https://camo.githubusercontent.com/acdb42e32d126f3c3f3ca51e0cde3851fa71ee689b66b2174a9f57674bf3b404/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f576562736974652d6861726e657373322e6769746875622e696f2d3432383546343f6c6f676f3d676f6f676c656368726f6d65266c6f676f436f6c6f723d7768697465)](https://harness2.github.io)
[![Benchmark guides](https://camo.githubusercontent.com/aa5839f0b4446acc25c139ad60945bc46d8830ab16e09e4ff048ffa8bc07c1c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f63732d42656e63686d61726b2532306775696465732d464242433034)](/google-research/harness2/blob/main/docs/BENCHMARKS.md)
[![License](https://camo.githubusercontent.com/85290ad5095410a2382190dcba74633fe0b35a5cede547d6a90e69cb80498c5e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d417061636865253230322e302d333441383533)](/google-research/harness2/blob/main/LICENSE)

[![Install, set up, and run JobBench: uv pip install -e '.[render]', harness2-setup jb, then harness2 --bench jb --k 1 --mode parallel. Click for prerequisites and commands.](/google-research/harness2/raw/main/assets/harness2-setup.gif)](/google-research/harness2/blob/main/docs/BENCHMARKS.md#jobbench)

[![Install, set up, and run JobBench: uv pip install -e '.[render]', harness2-setup jb, then harness2 --bench jb --k 1 --mode parallel. Click for prerequisites and commands.](https://github.com/google-research/harness2/raw/main/assets/harness2-setup.gif)](https://github.com/google-research/harness2/blob/main/docs/BENCHMARKS.md#jobbench)

A **harness** is the system around a model that enables it to act as an agent:
prompts, tools, memory, skills, orchestration, and more. **Harnessing** is the
process of optimizing that system.

Harness² is a plug-and-play framework for **recursive agent harnessing** in an
open world, where agents encounter tasks unseen during harness design. It
connects two levels of recursion while keeping model weights fixed:

* **Task-level recursion** refines the execution harness for the current task
  through a contrastive **Propose–Probe–Compose** step: propose edits, probe
  their effects on the same task, and compose a refined harness from behavioral
  contrasts between executions, without ground-truth feedback.
* **Harnessing-level recursion** updates a persistent *improvement harness*
  with adopted harnesses and evidence-supported lessons from each task to guide
  future refinement.

[![Harness² pipeline. Task-level recursion: an agent executor runs the initial harness, a harness editor proposes invariant and domain edits, candidate probes execute them, and a harness composer combines them into the final harness. Harnessing-level recursion: an experience reflector reflects on the step and updates the improvement harness used for the next task.](/google-research/harness2/raw/main/assets/harness2_pipeline.png)](/google-research/harness2/blob/main/assets/harness2_pipeline.png)

Across three professional benchmarks and four model–harness configurations, a
single Harness² step improves GLM-5 and Gemini 3.5 Flash over their base
harnesses, with gains of up to 11.5 points on WorkBuddy-Bench, 4.5 points on
JobBench, and 11.8 percentage points on LAB's partial pass rate. Increasing the
task-level recursion budget brings further gains.

The release supports **parallel and sequential recursion**, **OpenCode and
Codex executors**, and **JobBench, LAB, and WorkBuddy-Bench**.

harness2-video.mp4

[
](https://private-user-images.githubusercontent.com/63894509/669252828-76b10548-b14b-4c8f-9aa5-a93662df4d56.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTI0NDk1NTIsIm5iZiI6MTc5MjQ0OTI1MiwicGF0aCI6Ii82Mzg5NDUwOS82NjkyNTI4MjgtNzZiMTA1NDgtYjE0Yi00YzhmLTlhYTUtYTkzNjYyZGY0ZDU2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjEwMTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMDE5VDIyMzQxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTMyYTMyZGMxM2M2OGMyNDVkMDMyNWU2YTViNDRjMjhkZTBlY2Q2ODQ4YWFmMjRmZTMzZjMyZmYwYmNmZWI4OWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT12aWRlbyUyRm1wNCJ9.suzqx1Pk0TyiXGz98RYuf9uwyE_An6PDxSWEJvqd0Do)

Harness² exposes eight editable components around the model: **system prompt,
guardrails, memory, tool guidance, subagents, skills, scripts, and plugins**.
They control context construction, the tool interface, delegation, and behavior
inside the tool loop.

[![Eight harness components grouped by runtime role: system prompt, guardrails, memory, and skills construct context; tool guidance and scripts define the tool interface; subagents orchestrate delegated work; plugins control middleware.](/google-research/harness2/raw/main/assets/components.png)](/google-research/harness2/blob/main/assets/components.png)

Use **Linux, Python 3.12, and [uv](https://docs.astral.sh/uv/getting-started/installation/)**.
From the repository root:

```
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -e '.[render]'
harness2-demo --output runs/demo --k 2
```

The local demo runs both recursion modes with deterministic editors and real
Python executions. It requires no model credentials.

For model-backed benchmarks, install **Node.js 20+, the Google Cloud CLI**, and
the [benchmark dependencies](/google-research/harness2/blob/main/docs/SETUP.md#requirements). LAB needs Pandoc and
Poppler; WorkBuddy-Bench needs Docker. Then configure your models:

```
cp .env.example .env
# Edit .env with your Vertex AI project and model IDs.
gcloud auth application-default login
```

See the [setup guide](/google-research/harness2/blob/main/docs/SETUP.md) for model settings, authentication
alternatives, and the [Codex executor](/google-research/harness2/blob/main/docs/SETUP.md#codex-executor).

The following example installs LAB and runs one task, then evaluates and reports
its result. Model-backed runs incur API costs; start with a small task selection.

```
harness2-setup lab
harness2-check --bench lab
harness2 --bench lab --k 1 --mode parallel \
  --only-domains antitrust-competition --max-tasks 1
harness2-judge --bench lab --k 1 --mode parallel
harness2-report --bench lab --k 1 --mode parallel
```

Sequential recursion runs the same commands with `--mode sequential`. `--k` is
the task-level recursion budget; see [Experiments](#experiments). Judging and
reporting must use the same benchmark, executor, subset, `--k`, `--mode`, and
seed as the refinement run. Add `--dry-run` to `harness2` to preview task
selection without model calls.

| Benchmark | Tasks | Install | Guide |
| --- | --- | --- | --- |
| JobBench | Professional work | `harness2-setup jb` | [JobBench](/google-research/harness2/blob/main/docs/BENCHMARKS.md#jobbench) |
| LAB | Legal work | `harness2-setup lab` | [LAB](/google-research/harness2/blob/main/docs/BENCHMARKS.md#lab) |
| WorkBuddy-Bench | Office, web, and code | `harness2-setup wb` | [WorkBuddy](/google-research/harness2/blob/main/docs/BENCHMARKS.md#workbuddy-bench) |

Choose one benchmark per command. WorkBuddy also takes `--subset office`,
`--subset web`, or `--subset code` on every command after setup. The
[benchmark guides](/google-research/harness2/blob/main/docs/BENCHMARKS.md) cover each one's data, domains, and
grading.

Scale task-level recursion in two ways: **parallel recursion** explores multiple
candidate harnesses and composes refinements from their execution evidence;
**sequential recursion** carries the refined harness and accumulated evidence
through successive Propose–Probe–Compose steps.

[![Two ways to scale task-level recursion. Parallel: probe k general and k domain-specific candidate harnesses, then produce k compositions from the shared evidence. Sequential: carry the refined harness and accumulated evidence through k Propose–Probe–Compose steps.](/google-research/harness2/raw/main/assets/harness2_recursion_modes.png)](/google-research/harness2/blob/main/assets/harness2_recursion_modes.png)

*Parallel recursion explores wider; sequential recursion refines deeper.*

| Option | Behavior |
| --- | --- |
| `--k 1` | One Propose–Probe–Compose step |
| `--k K --mode parallel` | Probe `K` general and `K` domain-specific candidates, then produce `K` compositions |
| `--k K --mode sequential` | Refine the harness through `K` successive steps |
| `--substrate cx` | Use Codex instead of the default OpenCode executor |

After each task, harnessing-level recursion retains the adopted harness and
evidence-supported lessons to guide future refinement. See the
[experiment guide](/google-research/harness2/blob/main/docs/EXPERIMENTS.md) for task selection, concurrency,
reproducibility, and baseline comparisons.

Executor network access is unrestricted, and Codex runs with its sandbox
disabled. Public benchmark rubrics may be accessible online. Before evaluation,
configure [network restrictions](/google-research/harness2/blob/main/docs/EXPERIMENTS.md#web-access) to prevent
access to benchmark answers and grading criteria.

Results are saved under `runs/`, organized by benchmark and subset where
applicable. They include task summaries, deliverables, adopted harnesses,
reflection notes, and evaluation results.

Repeat the same command to resume. Use a new `HARNESS2_RUNS_DIR` when changing
models or task selection. See [results and resume](/google-research/harness2/blob/main/docs/EXPERIMENTS.md#results-and-resume)
for details; each command also supports `--help`.

```
@article{xu2026harness2,
  title   = {Harness$^2$: Recursive Agent Harnessing for an Open World},
  author  = {Xu, Ruiyao and Chen, Yanfei and CuiZhu, Zhongying and Dalvi Mishra, Bhavana and Ming, Yifei and Yu, Han and Han, Rujun and Lee, Chen-Yu and Pfister, Tomas},
  journal = {arXiv preprint arXiv:2610.14224},
  year    = {2026},
  url     = {https://arxiv.org/abs/2610.14224}
}
```

See [CONTRIBUTING.md](/google-research/harness2/blob/main/CONTRIBUTING.md).

Harness² is licensed under [Apache 2.0](/google-research/harness2/blob/main/LICENSE). Third-party code under
[`third_party/`](/google-research/harness2/blob/main/third_party/README.md), benchmarks, and datasets retain their
upstream licenses; see
[third-party notices](/google-research/harness2/blob/main/dependencies/README.md).

This is not an officially supported Google product. This project is not eligible
for the [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security).
