---
type: proposal
source: raw/articles/2026-11-23-anthropiccom-news-model-hardware-standard-research-preview.md
status: pending
created: 2026-11-23
---

# Proposal: Anthropic previews the Model Hardware Standard

## Summary

### In short

Anthropic wants to do for lab and factory equipment what MCP did for software: one standard way for any agent to find, understand and operate a device. Its Model Hardware Standard, opened as a research preview on 27 August, gives programmable instruments a common driver and a generated reference file listing what each can measure, what can be adjusted and which safety limits apply. AWS, Tecan, QIAGEN and Universal Robots are among the partners building support. The proposal adds it to Physical AI deployment and AI in Science, links it from the Claude app, and creates one source page. Reason to hesitate: the standard gets no page of its own.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source

On 27 August 2026 Anthropic announced a research preview of the Model Hardware Standard (MHS), a shared specification that lets AI agents operate physical devices such as microscopes, liquid handlers and robot arms, several at once. It began as a collaboration with HHMI's Janelia Research Campus and is open first to research labs and advanced manufacturers. The problem it targets is integration: each instrument has its own programming interface, so wiring a lab together takes specialists weeks or months. Anthropic says MHS cuts that to hours or minutes.

The mechanism is a standard driver, the software that translates between a computer and a device. It speaks a few primitives ("read" a temperature, "write" a setting), makes every device discoverable on a network, and lets users describe in plain language what code can't show, such as an arm's weight. From those notes it builds a reference file an agent reads before touching the device. Agents control hardware through MCP, a command line, or code files, and can chain commands into scripts for steps too fast or long to reason through live. In testing, Claude nudged a laser, watched the beam through a camera, repeated, then wrote a deterministic script that aligns the laser in one command.

Partners building support include AWS (Strands Robots), Automata, Danaher, Doosan Robotics, MBF Bioscience, QIAGEN, Tecan and Universal Robots, with Hugging Face and Raspberry Pi as early adopters. Anthropic is candid about limits: Claude's physical reasoning still needs expert oversight (Genentech researchers had to tell it that foaming errors were physical, not software bugs), devices without a programming interface are out of scope, and safety evaluations and a physical-safety roadmap come before the promised open-source release.

### What changes

The wiki mentions MHS only as a clause in the Claude app's manufacturing bullet, and tracks robotics and self-driving labs without any interoperability standard.

- **Physical AI deployment curve** gains a current-status bullet on MHS (driver, reference file, partners, admitted limits), a note under What to watch, and a Recent-changes entry dated 27 August. Page date stays 13 October, which is newer.
- **AI in Science** gains a self-driving-labs paragraph on MHS as shared instrument plumbing, with the laser example, and a Recent-changes entry. Page date stays 22 September.
- **Claude app** links its existing MHS clause to the Physical AI page; no other change.
- **Index** descriptions for the two trend pages mention MHS.
- New source page `wiki/sources/articles/model-hardware-standard-research-preview-2026-08-27.md`.

### What to weigh

Whether MHS deserves its own page now. It is a named standard with a dozen partners and a pending open-source release, but one announcement backs it, so the draft keeps it on the two trend pages and asks below.

## Intended changes

- [ ] **Update** `wiki/trends/physical-ai-deployment.md` — add one `## Current status` bullet after the Dyna Robotics bullet; extend the safety-case line in `## What to watch`; adds one Recent-changes entry dated 2026-08-27, inserted below the 2026-08-29 entry (5 entries, no spill); append 1 source id and 1 link; `as_of` stays 2026-10-13
- [ ] **Update** `wiki/trends/ai-in-science.md` — add one paragraph at the end of `## Self-driving labs`, after the Lila Sciences paragraph; adds one Recent-changes entry dated 2026-08-27, inserted between the 2026-09-07 and 2026-08-11 entries (8 entries, no spill); append 1 source id and 1 link; `as_of` stays 2026-09-22
- [ ] **Update** `wiki/tools/claude-app.md` — add a link to the Physical AI page in the Claude for Manufacturing bullet's MHS clause; no Recent-changes entry, no date change
- [ ] **Update** `wiki/index.md` — refresh the `trends/physical-ai-deployment` and `trends/ai-in-science` descriptions (dates unchanged)
- [ ] **Create** `wiki/sources/articles/model-hardware-standard-research-preview-2026-08-27.md` — source summary

## Page drafts

### wiki/trends/physical-ai-deployment.md (updated)

Frontmatter change (`as_of` unchanged):

```
sources: [...existing..., model-hardware-standard-research-preview-2026-08-27]
```

`## Current status` — one bullet appended after the Dyna Robotics bullet:

```
- **An instrument standard for agents (August 2026):** Anthropic opened a research preview of the Model Hardware Standard (MHS), begun with HHMI Janelia: a shared specification for agents to operate any device with a programmable interface. A standard driver exposes simple read/write commands, makes each device discoverable, and turns plain-language notes about a machine (an arm's weight, its safety limits) into a reference file the agent reads before operating it. Control runs through MCP, a command line, or code files, and the agent can compile a learned procedure into a deterministic script. Anthropic says integration drops from weeks to hours. AWS (Strands Robots), Automata, Doosan Robotics, Tecan, Universal Robots, and QIAGEN are building support; Hugging Face (LeRobot) and Raspberry Pi are early adopters. Anthropic says Claude's physical reasoning still needs expert oversight, and it will build safety evaluations with partners and publish findings before open-sourcing the standard.
```

`## What to watch` — second bullet replaced:

```
- Safety-case and validation practices for embodied agents, including the safety evaluations Anthropic is building with MHS partners before open-sourcing the standard.
```

Recent changes — one entry inserted below the 2026-08-29 entry:

```
- [2026-08-27] Anthropic opened a research preview of the Model Hardware Standard (MHS): standard driver and safety-limit reference file so agents can discover and operate programmable lab and factory devices via MCP, CLI, or code; partners include AWS, Tecan, Universal Robots, QIAGEN, Doosan Robotics; open-source release to follow safety evaluations.
```

Sources — one link appended:

```
- [Anthropic — Previewing the Model Hardware Standard](../sources/articles/model-hardware-standard-research-preview-2026-08-27.md)
```

### wiki/trends/ai-in-science.md (updated)

Frontmatter change (`as_of` unchanged):

```
sources: [...existing..., model-hardware-standard-research-preview-2026-08-27]
```

`## Self-driving labs` — one paragraph appended after the Lila Sciences paragraph:

```
**A shared instrument standard (Anthropic, as of 2026-08-27):** much of a self-driving lab's cost is bespoke instrument integration. Anthropic's Model Hardware Standard research preview, developed with HHMI Janelia, gives microscopes, liquid handlers, and robot arms a common driver, so one agent can run several in parallel, adjust parameters mid-experiment, and in some cases recover from hardware errors; Anthropic says setup falls from weeks or months to hours. Tecan, QIAGEN, Danaher, MBF Bioscience (ScanImage microscope software), and lab-automation platform Automata are building support. In testing, Claude aligned a laser by adjusting it and watching the beam through a camera, then wrote a script that repeats the alignment as one command. Genentech researchers still had to tell Claude that foaming errors in protein samples were physical, not software, failures. See [Physical AI deployment curve](physical-ai-deployment.md) for the safety side.
```

Recent changes — one entry inserted between the 2026-09-07 and 2026-08-11 entries:

```
- [2026-08-27] Anthropic's Model Hardware Standard research preview (with HHMI Janelia): a common driver so agents can discover, run, and coordinate lab instruments; Tecan, QIAGEN, Danaher, MBF Bioscience, and Automata building support.
```

Sources — one link appended:

```
- [Anthropic — Previewing the Model Hardware Standard](../sources/articles/model-hardware-standard-research-preview-2026-08-27.md)
```

### wiki/tools/claude-app.md (updated)

In the `## Vertical workflow bundles` Claude for Manufacturing bullet, one clause replaced:

```
Before: Does not operate equipment (Anthropic points to its Model Hardware Standard research preview for that).
After:  Does not operate equipment (Anthropic points to its Model Hardware Standard research preview for that; see [Physical AI deployment curve](../trends/physical-ai-deployment.md)).
```

### wiki/index.md (updated)

Two lines replaced in place:

```
- [trends/physical-ai-deployment](trends/physical-ai-deployment.md) — embodied AI and robotics follow a different deployment curve from screen agents because validation, safety, and hardware constraints dominate; Anthropic's Model Hardware Standard preview for agent-operated devices *(as_of: 2026-10-13)*
```

```
- [trends/ai-in-science](trends/ai-in-science.md) — hub for cross-domain science AI: science-agent platforms (Claude Science), self-driving labs and Anthropic's Model Hardware Standard for lab instruments, Google ERA's score-function search, autoresearch; biology and mathematics split out *(as_of: 2026-09-22)*
```

### wiki/sources/articles/model-hardware-standard-research-preview-2026-08-27.md (new)

```
---
title: Anthropic — Previewing the Model Hardware Standard
type: source
source_type: article
source_file: raw/articles/2026-11-23-anthropiccom-news-model-hardware-standard-research-preview.md
url: https://www.anthropic.com/news/model-hardware-standard-research-preview
published: 2026-08-27
ingested: 2026-11-23
domains: [agents, science]
---

# Anthropic — Previewing the Model Hardware Standard

Anthropic's announcement of a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, begun with HHMI Janelia and opened first to research labs and advanced manufacturers. A standard driver gives any programmable device simple read/write commands, network discoverability, and a generated reference file describing what it measures, what can be adjusted, and which safety limits are enforced. Agents control devices via MCP, a command line, or code files. Anthropic plans safety evaluations with partners before open-sourcing the standard.

## Influenced pages
- [Physical AI deployment curve](../../trends/physical-ai-deployment.md) — current-status bullet and What-to-watch note on MHS
- [AI in Science](../../trends/ai-in-science.md) — MHS as shared instrument plumbing for self-driving labs
- [Claude app](../../tools/claude-app.md) — link from the Claude for Manufacturing bullet's MHS clause

## Key claims extracted
- Research preview opened 2026-08-27 to a first group of scientific research labs and advanced manufacturers; began as a collaboration between Anthropic and HHMI Janelia Research Campus.
- Lets agents operate multiple lab and manufacturing instruments (microscopes, liquid handlers, robotic arms) in parallel; examples range from routine drug-discovery experiments to laser calibration on a quantum computer.
- Hardware setup typically takes weeks or months; Anthropic says MHS reduces integration to hours or minutes. Agents can reason through each experimental step, update parameters in real time, and in some cases recover from hardware errors without intervention.
- Works with any device that has a programmable interface; model-agnostic; any agent harness can access it through standard protocols such as MCP.
- Standard driver uses read/write primitives and makes devices discoverable in a standard format. Natural-language tags (written by the user or via an agent interview) capture characteristics code can't show, such as a robot arm's weight; the driver generates a reference file of measurable quantities, adjustable settings, and enforced safety limits.
- Three control mechanisms: MCP, command line, code files (APIs). The agent can chain driver commands into code files for long-running or fast operations without reasoning at each step.
- In testing, Claude adjusted a laser, observed the beam through a camera, iterated, then wrote a deterministic script that aligns the laser as a single command.
- Vendors adding support: AWS (Strands Robots, private pre-release package for participants), Automata (LINQ), Danaher (exploring), Doosan Robotics (robot-arm QA and multi-robot coordination), MBF Bioscience (ScanImage driver), QIAGEN (QIAsymphony Connect proof of concept), Tecan (Fluent liquid handlers), Universal Robots (plans support). Early adopters: Hugging Face (LeRobot), Raspberry Pi (Camera MHS Driver).
- Limits: Claude's spatial and physical reasoning still requires expert oversight (Genentech had to guide Claude to recognize foaming errors as physical failures); devices without a programming interface are not yet supported.
- Anthropic will build safety evaluations with launch partners, is developing a physical safety roadmap, and will release research-preview findings as deployment guidance when it open-sources MHS.
```

## Schema / vocabulary additions

None.

## Open questions

- Should the Model Hardware Standard get its own page now (for example `wiki/concepts/model-hardware-standard.md`, alongside [MCP](../wiki/concepts/mcp.md)), or stay on the two trend pages until a second source covers it? The draft assumes it stays on the trend pages.
	- Give it a page
