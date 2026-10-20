---
title: Ultramarine 1 Flash: Scaling Non-Verifiable RL
type: source
source_type: article
url: https://t.co/bQ3YmFajQh
fetched: 2026-10-20
---

# Ultramarine 1 Flash: Scaling Non-Verifiable RL

Paper Instruments
ULTRAMARINE
FEATHER
PAPER OFFICE
RESEARCH
Ultramarine 1 Flash: Scaling Non-Verifiable RL
Oct 14, 2026, Paper Instruments
Introduction

We present Ultramarine 1 Flash, an agentic model for professional knowledge work. Ultramarine applies large-scale reinforcement learning to a strong open base model, GLM-5.3 Flash, and improves on it across all six knowledge-work benchmarks we evaluate, by 4.1 points on average, while generating 6.5% fewer tokens. On our internal knowledge-work suite, Ultramarine costs $0.13 per task. It outscores Claude Fable 5 ($8.19) and GPT-5.6 Sol ($2.09) and comes within three points of Claude Opus 5.5 ($6.96) and GPT-6 Sol ($1.26), all four set to max reasoning.

Recent work has explored scaling agent post-training through synthetic tasks and environments [1] [2] [3] [4] [5] [6] [7] [8] [9], though this research has so far largely concentrated on verifiable tasks, where coding has consistently held the largest share of the RL mix. Most professional work is not verifiable: models are asked to produce artifacts ranging from diligence memos to litigation chronologies and therefore cannot be checked by regex parsers or unit tests. The quality of the answer often turns on judgment and taste, and, as such, a defensible reward for open-ended work has to be shaped per task. In this work, we scale non-verifiable task synthesis across agentic knowledge work.

We formalize each RL task the way recent work formalizes a verifiable task: an environment, a model instruction, and a verification system [10]. Each environment and task is synthesized with a custom synthesis pipeline per domain, and then used in a standard RL post-training setup.

Non-Verifiable Task Synthesis
Scaling Non-Verifiable Verification

Scaling post-training for professional knowledge work requires tasks that are realistic and open-ended, yet specified well enough to distinguish better work from a different interpretation of the assignment. The reward must be shaped to recognize correct work without requiring a particular solution [11].

Task and rubric co-design is the central problem of authoring high quality RL training data. Per our rubric-grading work [12], each criterion defines a boundary over possible answers. A criterion copied too closely from one golden reference rejects valid alternatives, while a vague criterion such as “provides an appropriate recommendation” can reward plausible sounding errors. The criterion must instead state the substantive condition that earns credit, together with the facts, thresholds, and context needed to check it against the deliverable. Naming the relevant entities, dates, and assumptions keeps the standard explicit, reducing judge variance and increasing alignment with expert human judgment.

A criterion therefore tests one coherent proposition. Conjunctions may be used to express conditions that hold together: a note for the managing director may need to state what was checked "and" the decision implication "and" what remains open, so the reader can distinguish verified findings from unresolved decisions. Similarly, "or"s admit genuinely equivalent ways to meet a requirement. Independent accomplishments remain separate criteria so that success on one can receive credit even when another is missed. Each proposition is judged met or unmet, and its wording defines the acceptable variants to support generalization.

A criterion draws a boundary over possible answers
COMPLETE ANSWERS
A

Approve v7 as the sole forecast basis and the qualitative roadshow position. External wording and projection tables require counsel clearance.

B

v7 governs board and valuation work; the qualitative roadshow position can be approved now. Counsel must still clear external wording and tables.

C

External wording and tables await counsel clearance. The board can approve v7 and the qualitative roadshow position now.

INCOMPLETE ANSWERS
D

Approve v7 as the sole forecast basis and the qualitative roadshow position.

E

Counsel must clear external wording and projection tables.

F

The v7 forecast implies transaction multiples of 12.3x and 10.6x.

OVERFIT CRITERION
The callout uses the phrase ‘sole forecast basis’ and presents the approval request before the counsel-clearance caveat
Rejects B and C
VAGUE CRITERION
Provides a useful forecast update for the board
Also accepts D, E, and F
CRITERION 13 OF THE EXAMPLE TASK
Separates what the board can approve now (v7 as the sole forecast/valuation basis and the qualitative roadshow position) from what still requires counsel clearance (exact external wording and the next-turn projection tables and narrative), rather than presenting the forecast update and disclosure use as a single settled action
Matches the boundary

These binary judgments combine into the raw reward, and the full rubric’s coverage and weights should reflect professional importance. Reliable grading thus depends on the boundaries of individual criteria and how they compose, rather than simply choosing a stronger or agentic judge.

There are three sources of data we considered to curate the Ultramarine curriculum: (1) production traces from real users driving agents, (2) expert-authored tasks, and (3) synthetically generated data.

Production traces offer realism, but users often leave assumptions unstated and rely on shared context [12]. Additionally, production state is non-stationary and converting traces into group-relative RL tasks requires reconstructing an environment with perfect fidelity to production in order to replay rollouts. The latter issue is solvable with careful state snapshotting, but the former is harder: a reward built from one user’s query bakes in that user’s unstated preferences and penalizes other correct answers. As a toy example, a user asking for the margin profiles of the top 10 medical technology companies may have meant the top 10 by revenue, and so a successful task shaped from that trajectory would embed that implicit assumption in the reward, penalizing perfectly valid responses choosing market cap, enterprise value, or profit to rank them. Solving for this would require materially reworking the query to make it constrained and evaluable. We chose not to pursue this path given the aforementioned complexity, though we believe it remains a rich area of research.

Expert-authored tasks resolve that ambiguity, as annotators are given explicit instruction to construct tasks that are constrained, well-defined, and evaluable, but maintaining breadth and grading quality by hand is costly, and narrow tasks and rubrics still exclude defensible answers. As model intelligence grows at a clip, meeting all of these requirements per-task is difficult to scale, highlighted by the growing cost of human data and errors in human authored public benchmarks [13] [14].

As such, we continued with a purely synthetic recipe to scale RL task quality and grading fidelity, reliably, as a function of compute, across finance, law, consulting, and operations. Unlike production data, it allows us full control over data distribution and lets us choose seeds from scratch, and unlike expert authored data, it enables us to create low-cost, high-throughput tasks and filter for quality and difficulty at scale.

Domains, Taxonomy, and Preventing Mode Collapse

The training curriculum spans four domains (finance, law, consulting, and operations), 19 professional practice areas, and 88 distinct environment types (Table 1). Each practice area and environment type is expressed as a standalone generation pipeline that samples over a taxonomy of axes. For each instance of generation, the taxonomy is sampled across its axes: deliverable format, sources of complexity, stakeholders, source conflicts, hints, the stage of the transaction or matter, numerous domain-specific dimensions, and so on. Sampling across these axes gives each practice area a nominal configuration space on the order of 10⁷–10¹⁰ combinations. Each environment instantiates further into many concrete instances with different companies, documents, and figures. This combinatorial breadth helps prevent mode collapse in LLM-generated data [1] [15].

Anatomy of a Task

Tasks follow the Harbor specification [10]. Each task is packaged as a self-contained, runnable instance with three parts: the instruction, handed to the agent as a professional would receive it; the environment, the workspace and any live services, with a Dockerfile and service definition; and the grader, the task's rubric and the harness that scores the delivered work.

Appendix A presents a complete example, including the task instructions, workspace files and connected services, and full weighted rubric.

Environments

The curriculum is built on environments. An environment is a mounted workspace an agent inhabits the way a professional would:

A filesystem of realistic documents, including models, memos, filings, trackers, decks, correspondence, and so on.
A live system of record it reads and mutates as part of the work, including CRM and ERP/general-ledger systems, warehouse and transport management (WMS/TMS), manufacturing and process control (MES), GRC and ticketing, and property and work-order platforms.
Synthesized resource interfaces spanning MCP, HTTP, and CLI

To build environments, we retrieve real documents and synthesize materials that have no suitable public source. The workspace combines:

Regulatory filings: SEC EDGAR filings, including 10-Ks, 10-Qs, 8-Ks, proxy statements, and S-1s, plus exhibits such as credit agreements and indentures.
Public web material: company sites, press releases, investor presentations, and regulatory notices.
Research material: analyst reports, market-data snapshots, and sector studies, provided as point-in-time snapshots labeled with their source and date.
Synthetic documents: realistic contracts, patents, internal reports, internal emails, and so on based on seed data.

Each environment also has a private ground-truth record to provide privileged information to task proposer agents.

Instructions and Graders

We construct filesystems, document corpora, and MCP servers through bespoke pipelines for each of the 88 environment types. Within each environment, task instructions and rubrics are adversarially generated along the sampling axes described above, spanning 10⁷–10¹⁰ possible combinations.

Generating frontier tasks is compute intensive: Producing a single task involves several dozen independent agent loops and multiple rounds of review, checking grounding, professional realism, difficulty, and consistency between the assignment and its grading criteria. Additional filters check for answer leakage and reward hacking, using classifiers iteratively added or refined in response to failures observed during training. A final curriculum filter screens tasks based on the base model's performance.

Grading Logic

Deliverables are practical work products, including Excel models, PowerPoint decks, and Word or PDF documents that the agent authors or edits in place. This result is then parsed and rendered as text to a naive LLM rubric grader.

We use our open-source rubric package [16], with PerCriterionOneShotGrader and a custom grading prompt tuned for agreement with human experts following the evaluation process described in Notes on Choosing a Rubric Judge [12].

Table 1. 88 environment types, by domain and practice area.
Finance
34 environment types
M&A Execution
Buy-Side M&A Deal Room
Sell-Side M&A Process Room
Public Merger Execution Room
Hostile Takeover Defense Room
Carve-Out & Divestiture Room
Capital Markets
IPO Execution Room
Follow-On & Block Trade Room
Convertibles Execution Room
SPAC / De-SPAC Room
Private Equity
Buyout Diligence Room
Portfolio-Company Value Creation Room
PE Exit Readiness Room
GP-Led Secondary Room
Growth & Venture
Venture Series Diligence Room
Growth Equity Diligence Room
SaaS Product-Market Room
Pre-IPO Private Company Room
Project Finance
Renewables Project Finance Room
Data-Center Project Finance Room
Midstream Project Finance Room
Real-Asset Underwriting Room
Restructuring
Chapter 11 Debtor Room
Ad Hoc Creditor Group Room
Cross-Border Restructuring Room
Liability Management Exercise Room
Credit Instruments
High-Yield Indenture Room
Leveraged Loan Review Room
Private Credit Term-Sheet Room
Coverage & Origination
Sector Coverage Pitch Room
Buyer Universe Mandate Room
Strategic Alternatives Pitch Room
Structured Finance
ABS Issuance Room
CLO Manager Room
RMBS / CMBS Surveillance Room
Legal
15 environment types
Corporate & Commercial
Commercial Contract Matter
Employment Law Matter
Fund Formation Matter
Corporate Governance Matter
M&A Legal Diligence Matter
Securities Disclosure Matter
Litigation & Investigations
Discovery Review Matter
Internal Investigation Matter
Litigation Motion Matter
Intellectual Property
Freedom-to-Operate Claim Chart Matter
IP Licensing Matter
Patent Prosecution Matter
Tax
M&A Tax Structuring Matter
Tax Controversy Matter
Transfer Pricing Matter
Consulting
28 environment types
Transactions & Investor
Commercial Due Diligence Engagement
Operational Due Diligence Engagement
Technology Due Diligence Engagement
Financial Diligence Workpaper Engagement
Deal Support & Investment Committee Engagement
M&A Strategy Engagement
Synergy Planning Engagement
Post-Merger Integration Engagement
Carve-Out Separation Engagement
Exit Readiness Engagement
Portfolio-Company Value Creation Engagement
Operations & Org Transformation
Operations Diagnostic Engagement
Operating Model & Org Design Engagement
Procurement & Cost Transformation Engagement
Supply Chain Transformation Engagement
Digital & Technology Transformation Engagement
Performance Improvement & Value Creation Engagement
Sustainability & Resilience Transformation Engagement
Transformation Management & Delivery Engagement
Turnaround & Interim Management Engagement
Corporate Strategy
Market Entry Engagement
Pricing & Growth Engagement
Growth Strategy Engagement
Customer Strategy & Experience Engagement
Corporate Portfolio Strategy Engagement
Business Building & Innovation Engagement
Competitive Strategy Wargame Engagement
Strategic Risk, Geopolitics, & Sustainability Engagement
Operations
11 environment types
Business Operations
FP&A Close & Forecast Room
PMO Program Room
Procurement Office Room
Revenue Operations Pipeline Room
Field Operations
Warehouse Operations Room
Plant Shift Room
Clinic Operations Room
Property Management Room
Controls & Assurance
SOX Controls Room
CISO Program Office Room
Privacy Compliance Room
Feather: The Agent Harness

Recent work uses multi-harness training to improve generalization [9] [17]. However, training on several harnesses at once was not feasible on our compute budget. Instead, we surveyed the tool contracts and execution structures of the coding harnesses in wide use (Claude Code [18], Codex [19], Cursor [20], Kimi Code [21], OpenAI Agents SDK [22], OpenCode [23], OpenHands [24] and its Software Agent SDK [25], Qwen Code [26], Mini SWE Agent [27], Terminus [28], and SWE-agent [29]), and created a new Python harness built on common shared conventions, aiming to train a policy with the most transfer across harnesses.

Training and evaluation share Feather's agent loop, tools, and compaction. Training routes model requests through Verifiers’ inference interception layer [30]; the asynchronous training loop refreshes inference weights mid-rollout [31].

Tool Interface

We compared the file-editing and process-control interfaces of existing harnesses and used paired evaluations and trajectory inspection to determine Feather's tool configuration.

File Editing Tools
Editing approach	How changes are described	Representative implementations
Patch editing	Changes described through context lines and additions/deletions	Codex, OpenCode¹
String replacement and file creation	Changes specified as old/new text; new files supplied as complete content	Claude Code, Qwen Code, OpenCode¹, OpenHands
Terminal file operations	File operations through terminal commands	Mini SWE Agent, Terminus

Table 2. File-editing interface categories considered in this work.

¹ OpenCode uses apply_patch for selected GPT models and separate edit and write tools for other models.

Existing harnesses abstract file editing in two main ways: a patch interface describes changes through context lines and additions/deletions, while a string-replacement interface describes changes through old and new text.

To change timeout: 30 to timeout: 60 in config.yaml, Codex's apply_patch uses textual context to locate the patch and does not require the model to supply line numbers:

*** Begin Patch
*** Update File: config.yaml
@@
-  timeout: 30
+  timeout: 60
*** End Patch


String replacement requires only the old and new text, with the tool locating the match in the file:

edit(file_path="config.yaml",
     old_string="timeout: 30",
     new_string="timeout: 60")


A second design choice is whether to expose file operations through a single combined tool or through dedicated per-operation tools.

Interface	Tool organization	Representative harnesses
Combined tool	file_editor(command="view", ...), file_editor(command="str_replace", ...)	OpenHands
Dedicated tools	read(...), edit(...), write(...)	Claude Code, Qwen Code, Kimi Code, OpenCode (edit/write configuration); Feather

Table 3. Combined and dedicated file-operation interfaces.

We ran both configurations on the same set of tasks and inspected the generated calls. The trajectory analysis did not show a clear advantage for split tools. Feather adopted dedicated tools for their simpler per-operation schemas and consistency with several widely used harnesses.

Beyond the tool interface, execution order also matters for correct file edits. A model turn may contain multiple tool calls, but Feather executes them sequentially in model-produced order to preserve dependencies between reads, shell commands, and file modifications. Even with sequential execution, intervening shell commands or background processes may change a file after it has been read. Feather therefore records a content fingerprint (a hash of the complete file contents) on each read and checks it before editing or overwriting the file. If the contents have changed, the modification is rejected and the model is asked to reread the file.

Feather's tool set comprises read, edit, write, grep, and glob:

read returns text with line numbers and accepts offset and limit parameters to bound the requested range. A successful read records a content fingerprint of the file.
edit and overwrites through write check the content fingerprint before applying changes, rejecting the modification when the current contents do not match the record. edit requires the old text to match uniquely in the file by default, and supports explicit multi-occurrence replacement through replace_all.
grep and glob provide structured search, avoiding the need for models to construct Bash commands and parse their output. grep returns matching files and line numbers, glob returns paths by filename pattern. Both enforce a result limit and include a truncation indicator when results exceed the limit, so the model knows to narrow its query.
Bash Tool

Across existing harnesses, shell interfaces differ primarily in what happens to a process after a call returns and how the model regains access to it.

Behavior	How shell execution is managed	Representative harnesses
Session handle	Returns a handle after the wait for output	Codex
Persistent shell	Retains shell state across commands	OpenHands, SWE-agent
Explicit background parameters	Selects background execution on the call	Qwen Code

Table 4. Shell interfaces after a call returns.

Feather uses explicit background tasks. Each call starts a fresh shell. Changes to the working directory and environment variables do not carry into later calls. The model starts background processes with run_in_background, reads their output with task_output, stops them with task_stop, and lists them with task_list.

Todo Tool

To let the model maintain a work plan over long-horizon tasks and preserve progress tracking across multiple rounds of context compaction, Feather provides a todo tool. The model can create or update the list at any point. The list persists across compaction within a single agent run and is reattached in its current state to the compressed context.

Final Tool Set
Category	Tools	Behavior
File operations	read, edit, write, grep, glob	Dedicated entry points with bounded output. Edits and overwrites require a prior read and reject stale contents.
Process control	bash, task_list, task_output, task_stop	Foreground by default, explicit background with run_in_background. No persistent shell state.
Planning	todo_write	Direct list replacement. Persists across compaction.

Table 5. Feather's default tool set.

Optional web_search, web_fetch, and MCP servers are configured per task.

Paper Office Package

Agents use Python packages, such as python-docx, python-pptx, and openpyxl, to edit Word, Excel, and PowerPoint files. Often, they hit API gaps, drop into raw OOXML, and create silent corruptions and regressions. We train Ultramarine using our open source forks of these libraries, paper-docx, paper-pptx, and paper-xlsx[32]. Each package keeps the familiar import name and expands the API for understanding and safely editing Office files. The libraries expose file structure as data, validate supported changes, and refuse operations they cannot handle safely.

System Prompts and Exploration

"Training on your production harness" is an emerging strategy in agent post-training, and it is especially helpful to familiarize the model with the tools, arguments, and interfaces it will use in production. However, this approach can restrict exploration when applied to prompts, tool descriptions, and other model instruction. These show up as prescriptive context that increases performance during test time, but constrains model exploration and conditions behavior to a specific prior during training. We only introduced production model instruction in final stages of training.

For the bulk of training, we rewrite all model-facing prose to be general, lightweight, and unopinionated. It is up to the policy to decide how to make do with the options and information presented to it, and there is no one prescribed workflow it should adhere to.

Our training system prompt is therefore three sentences, about 50 tokens, where the production prompts we surveyed in real harnesses run from roughly 1,800 to 4,400 (Table 6). Similarly, our tool descriptions state what a tool does and what it guarantees, rather than when or how to use it, and we omit the planning and verification workflows that production harnesses often prescribe.

You are an agent working in a Linux sandbox with access to the provided tools and workspace.

Do not expose, log, transmit, or write secrets or credentials.

When relevant, put requested file deliverables at the paths specified by the user or environment.


Example 1. Complete Feather system prompt.

Feather's tool descriptions, also shown to the model, similarly opt for exposition rather than prescription.

Read a text file with line numbers. `offset` and `limit` bound the returned range. A successful read records the file revision required to edit or overwrite its current contents.


Example 2. Complete Feather read description.

Harness	System prompt	Read tool	Example instructions
Feather (training)	50	36	See full prompt above
OpenCode 1.18.4	1,771	295	
“You MUST answer concisely with fewer than 4 lines of text …
See more

OpenHands SDK 1.37	2,802	663	
“NEVER create multiple versions of the same file with different suffixes …
See more

OpenAI Agents SDK 0.18	3,495	Shell	
“You MUST adhere to the following criteria when solving queries …
See more

Codex CLI	3,576	Shell	
“Use apply_patch for local file edits. Do not create or edit files with cat or other shell write tricks. …
See more

Kimi Code 0.1.1	3,916	669	
“you MUST use the appropriate tools available to you to make actual changes …
See more

Qwen Code 0.20.1	4,403	483	
“NEVER assume a library/framework is available or appropriate. …
See more

Table 6. Default system prompt and file-read tool descriptions.

Vision

We did not train with vision. To nudge the model against repeated image-read attempts, without imposing additional harness constraints, read returns a text observation for supported image extensions:

read({"file_path": "chart.png"})

→ Vision is not available in this environment.


Example 3. Feather image-read response.

Tool Failure Handling

A failure should shape the policy only when the policy caused it. An error that follows from the model's own actions, such as a malformed call or a failing command, is part of its exploration, so we return the error and let the model correct course within the same trajectory. When the environment fails beneath it, such as a lost sandbox, the outcome carries no information about the policy, and therefore scoring it would only add noise to the reward. We discard that attempt, excluding it from training rather than assigning zero reward, and restart the task in a fresh environment.

Class	Examples	Handling
Model-correctable error	Invalid arguments, unknown tool, missing file, failed string replacement, command error or timeout	Return the error to the model and let it continue within the same trajectory.
Unrecoverable runtime failure	Lost sandbox, unrecoverable tool transport failure, unexpected tool exception	End the attempt. The task can be restarted in a fresh environment.

Table 7. Tool failure classes and their handling.

How different kinds of errors are handled
Pause
Replay
Model turn
Environment response
Failure
EARLIER TURNS
FAILURE
WHAT HAPPENS NEXT
THE TRAJECTORY CONTINUES
Invalid tool call
Bad schema or unknown tool
Error returned
Model corrects it

Scored
Deliverable reward − invalid-call penalty

Command fails
For example, a failing test
Output returned

Scored
No invalid-call penalty

Connection drops
Transport lost mid-call
Result retrieved
Tool not re-run

Scored
No side effect repeated

THE ATTEMPT ENDS
Sandbox lost
Or no recoverable result

Excluded
Logged, not scored as zero

Restart
In a new sandbox
Fresh environment

Scored
The retry, from turn one

Sandboxing

Training agents on professional work requires environments that support both document editing and interactions with live services. Each rollout uses an isolated E2B sandbox with separate Docker Compose containers for agent execution, MCP services, and grading.

We built our sandbox architecture around four choices: restore initialized environments from snapshots, keep the agent loop outside the execution environment, isolate task execution from services and grading, and treat remote communication as both a latency cost and a source of recoverable failures.

Initialized Snapshots

Environment-level hot snapshots preserve filesystem and memory state, including running services [33]. Tasks and rollout replicas restore independent copies, then load task-specific overlays and the pinned Feather runtime. Task-input and Feather updates do not require rebuilding every world snapshot.

Agent Loop Outside the Sandbox

The agent loop runs on the orchestrator, while commands and file operations execute inside the sandbox [34]. Model inference credentials and agent-loop code remain outside the environment the model can modify, so orchestration updates can ship without rebuilding environment snapshots. More importantly, nothing the model does in the sandbox can alter its own harness, credentials, or grader.

Execution, Services, and Grading

The agent accesses application services through MCP, without direct access to service processes or their storage. Deliverables are writable, and grading artifacts and verifier state are outside the agent's execution boundary. Reusable verifier dependencies and world-level grading infrastructure are baked into snapshots in advance. Finally, task-specific grading material is supplied after the rollout for isolation.

Remote Calls and Recovery

Operations that look cheap locally can become expensive when each requires a remote request. Our initial file-loading path created directories and naively wrote files individually. On an upload test of about 50 files, packing them into a single tarball cut the time from 52 seconds to 2.2 seconds, a 96% reduction. Each tool call made several roundtrips, and fusing those roundtrips into fewer requests removed the same kind of delay.

Training
Training Objective

We adapt the RL setup used for Kos-1 Lite [35] and Kos-1 Experimental [36] to full agent trajectories.

For a group of rollouts on the same task, our modified CISPO objective is [31] [37]:

𝐿
(
𝜃
)
=
−
1
𝑁
∑
𝑖
,
𝑡
𝑚
𝑖
,
𝑡
 
sg
⁡
 ⁣
[
min
⁡
 ⁣
(
𝜌
𝑖
,
𝑡
(
𝜃
)
,
5
)
]
𝐴
𝑖
log
⁡
𝜋
𝜃
(
𝑎
𝑖
,
𝑡
∣
ℎ
𝑖
,
𝑡
)
L(θ)=−
N
1
	​

i,t
∑
	​

m
i,t
	​

sg[min(ρ
i,t
	​

(θ),5)]A
i
	​

logπ
θ
	​

(a
i,t
	​

∣h
i,t
	​

)
𝜌
𝑖
,
𝑡
(
𝜃
)
=
𝜋
𝜃
(
𝑎
𝑖
,
𝑡
∣
ℎ
𝑖
,
𝑡
)
𝜋
r
o
l
l
o
u
t
(
𝑎
𝑖
,
𝑡
∣
ℎ
𝑖
,
𝑡
)
ρ
i,t
	​

(θ)=
π
rollout
	​

(a
i,t
	​

∣h
i,t
	​

)
π
θ
	​

(a
i,t
	​

∣h
i,t
	​

)
	​

𝐴
𝑖
=
𝑟
~
𝑖
−
1
∣
𝑔
∣
∑
𝑗
∈
𝑔
𝑟
~
𝑗
A
i
	​

=
r
~
i
	​

−
∣g∣
1
	​

j∈g
∑
	​

r
~
j
	​


𝑚
𝑖
,
𝑡
m
i,t
	​

 marks model-generated training tokens, and 
𝑁
N counts those tokens in the batch.

In addition to CISPO we incorporate Rollout Routing Replay (R3) [38], mean-centered advantages [39], and zero-advantage filtering [40].

Async Updates and Mini-Steps

Our earlier synchronous setup used three policies (current, pre-update, and rollout) [41]: CISPO compared the current and pre-update policies, while token-level truncated importance sampling corrected the pre-update/rollout mismatch [42]. That implementation used an extra forward pass for pre-update log probabilities and multiple minibatch updates per rollout batch.

Here, completed task groups enter a buffer continuously, and a full batch triggers one optimizer step, with no mini-steps [31] [43]. Off-policyness therefore depends on trainer throughput relative to rollout throughput. The update uses the importance sampling ratio of the current policy to the rollout policy directly, which removes the separate pre-update policy and its forward pass.

Length Penalty

We penalize generated output and excessive turns, alongside malformed tool calls and calls to nonexistent tools:

𝑟
𝑖
=
𝑅
r
a
w
,
𝑖
−
min
⁡
(
𝜆
𝑚
𝑖
,
𝑐
t
o
o
l
)
r
i
	​

=R
raw,i
	​

−min(λm
i
	​

,c
tool
	​

)
𝑅
a
d
j
u
s
t
e
d
,
𝑖
=
𝑟
𝑖
−
max
⁡
(
𝑟
𝑖
,
0
)
 
𝑓
(
𝑛
𝑖
)
−
𝐺
𝑔
 
𝑃
(
𝑇
𝑖
)
R
adjusted,i
	​

=r
i
	​

−max(r
i
	​

,0)f(n
i
	​

)−G
g
	​

P(T
i
	​

)
𝑃
(
𝑇
)
=
min
⁡
 ⁣
(
𝛼
max
⁡
(
𝑇
−
𝐵
,
0
)
𝐿
,
𝑐
o
u
t
)
+
𝜂
 
clip
⁡
 ⁣
(
𝑇
−
𝐵
t
a
i
l
𝐿
t
a
i
l
,
0
,
1
)
P(T)=min(α
L
max(T−B,0)
	​

,c
out
	​

)+ηclip(
L
tail
	​

T−B
tail
	​

	​

,0,1)

𝑇
𝑖
T
i
	​

 counts generated tokens across the trajectory, 
𝑛
𝑖
n
i
	​

 counts agent turns, and 
𝑚
𝑖
m
i
	​

 counts invalid tool calls. Each invalid call incurs a penalty 
𝜆
λ, capped in total at 
𝑐
t
o
o
l
c
tool
	​

. The turn factor 
𝑓
(
𝑛
)
=
clip
⁡
(
(
𝑛
−
𝑛
0
)
/
(
𝑛
max
⁡
−
𝑛
0
)
,
0
,
1
)
f(n)=clip((n−n
0
	​

)/(n
max
	​

−n
0
	​

),0,1) fades positive reward from 
𝑛
0
n
0
	​

 to zero at the turn cap 
𝑛
max
⁡
n
max
	​

. 
𝐺
𝑔
G
g
	​

 enables output penalties when the group mean reward after this fade is positive.

The output penalty grows at rate 
𝛼
/
𝐿
α/L beyond allowance 
𝐵
B, up to 
𝑐
o
u
t
c
out
	​

. A separate extreme-length penalty starts at 
𝐵
t
a
i
l
B
tail
	​

, rises over 
𝐿
t
a
i
l
L
tail
	​

 tokens, and caps at 
𝜂
η.

Training Details
Setting	Value
Base model	GLM-5.3-Flash [44]
Loss	CISPO [37], with modified two-policy objective
Optimizer	AdamW
Batch size	64 × 8
LoRA rank [45]	64
Learning rate	5 × 10⁻⁵
Sampling config	temp = 1, top_p = 1, top_k = -1
Advantage	Group-centered mean without standard deviation normalization [39]
Loss normalization	Normalized by the total count of valid generation tokens in the training batch
Context window	131,072 tokens
Max agent turns	250
Compaction trigger	At 85% of the context window or when 30,000 tokens remain, whichever occurs first
Results

We evaluate Ultramarine 1 Flash on six knowledge-work benchmarks, JobBench [46], PI Knowledge Work, FrontierFinance [47], AutomationBench [48], DiligenceBench [49] and APEX-Agents 1.1 [50], and report two coding benchmarks for reference, Terminal-Bench 2.1 [51] and DeepSWE [52] (Table 8). All models run at the highest reasoning setting they support. On PI Knowledge Work we additionally sweep each model's reasoning settings for the cost–quality frontier. The notes to Table 8 give each benchmark's setup and the source of each comparison score.

JobBench
Ultramarine 1 Flash
62.9
Gemini 3.8 Flash
60.6
DeepSeek V4.1 Flash
60.4
Claude Fable 5
57.4
GLM-5.3 Flash
56.3
Kimi K3
54.3
GPT-5.6 Sol
45.4
PI Knowledge Work (internal)
Ultramarine 1 Flash
59.3
Claude Fable 5
57.8
GPT-5.6 Sol
55.1
GLM-5.3 Flash
52.0
Kimi K3
51.2
Gemini 3.8 Flash
49.4
DeepSeek V4.1 Flash
47.9
FrontierFinance
Ultramarine 1 Flash
53.3
GLM-5.3 Flash
50.7
Gemini 3.8 Flash
50.0
Claude Fable 5
49.2
GPT-5.6 Sol
46.8
Kimi K3
46.4
DeepSeek V4.1 Flash
46.0
AutomationBench
DeepSeek V4.1 Flash
51.3
Ultramarine 1 Flash
50.2
GLM-5.3 Flash
48.8
Gemini 3.8 Flash
47.3
Kimi K3
46.7
Claude Fable 5
46.2
GPT-5.6 Sol
45.8
DiligenceBench
Gemini 3.8 Flash
53.1
Claude Fable 5
52.9
Ultramarine 1 Flash
50.6
Kimi K3
50.4
DeepSeek V4.1 Flash
50.3
GPT-5.6 Sol
50.0
GLM-5.3 Flash
48.2
APEX-Agents 1.1
Gemini 3.8 Flash
64.3
Claude Fable 5
63.6
Ultramarine 1 Flash
57.0
GLM-5.3 Flash
52.8
GPT-5.6 Sol
51.5
Kimi K3
50.6
DeepSeek V4.1 Flash
39.5
Benchmark	Ultramarine 1 Flash	GLM‑5.3 Flash	Claude Fable 5	GPT-5.6 Sol	Gemini 3.8 Flash	DeepSeek V4.1 Flash	Kimi K3
KNOWLEDGE WORK							
JobBencha	62.9	56.3	57.4	45.4	60.6	60.4	54.3
PI Knowledge Work (internal)b	59.3	52.0	57.8	55.1	49.4	47.9	51.2
FrontierFinancec	53.3	50.7	49.2	46.8	50.0	46.0	46.4
AutomationBenchd	50.2	48.8	46.2	45.8	47.3	51.3	46.7
DiligenceBenche	50.6	48.2	52.9	50.0	53.1	50.3	50.4
APEX-Agents 1.1f	57.0	52.8	63.6	51.5	64.3	39.5	50.6
CODING							
Terminal-Bench 2.1g	83.2	84.3	84.3	88.8	89.4	90.6	88.3
DeepSWE 1.1h	61.5	63.4	69.9	72.7	73.8	74.2	68.5

Table 8. Knowledge-work and coding results.

Ultramarine improves on GLM-5.3 Flash on all six knowledge-work benchmarks, by 4.1 points on average, while generating 6.5% fewer tokens across themi.

PI Knowledge Work: score against cost per task
42
46
50
54
58
62
66
$0.01
$0.03
$0.1
$0.3
$1
$3
$10
Cost per task (log scale)
Score
Ultramarine 1 Flash (max)
GLM-5.3 Flash (max)
GPT-6 Astra (low)
GPT-6 Astra (medium)
GPT-6 Astra (max)
Claude Opus 5.5 (low)
Claude Opus 5.5 (medium)
Claude Opus 5.5 (high)
Claude Opus 5.5 (max)
GPT-6 Sol (low)
GPT-6 Sol(medium)
GPT-6 Sol (high)
GPT-6 Sol (max)
Claude Fable 5 (low)
Claude Fable 5 (medium)
Claude Fable 5 (max)
Claude Fable 5.1 (max)
GPT-5.6 Sol (low)
GPT-5.6 Sol(medium)
GPT-5.6 Sol (high)
GPT-5.6 Sol (max)
Muse Spark 1.3 (low)
Muse Spark 1.3 (medium)
Muse Spark 1.3 (high)
Muse Spark 1.3 (max)
GPT-6 Luna (low)
GPT-6 Luna (medium)
GPT-6 Luna (high)
GPT-6 Luna (max)
Gemini 3.8 Flash (low)
Gemini 3.8 Flash (medium)
Gemini 3.8 Flash (high)
DeepSeek V4.1 Flash (max)
Kimi K3 (max)
GLM-5.3 (max)
DeepSeek V4 Pro (max)
Ling 3.1 Flash (reasoning)
Qwen3.8 2.4T (xhigh)
Qwen3.8 27B (xhigh)
MiniMax M3 (reasoning)

Scores are means over our internal task suite. Cost is per task at each developer's official API pricing as of October 2026.

On PI Knowledge Work, Ultramarine sits on the cost-quality frontier. It scores 59.3 at $0.13 per task, against 57.8 at $8.19 for Claude Fable 5 (max) and 55.1 at $2.09 for GPT-5.6 Sol (max), and trails Claude Opus 5.5 (max) by 2.6 points at $6.96 and GPT-6 Sol (max) by 2.0 at $1.26. Of the 39 other runs across eighteen models and their reasoning settings, 27 cost more and score lower. Across the 24 runs in the figure that Artificial Analysis also measures, PI Knowledge Work scores correlate strongly with the Artificial Analysis Intelligence Index (r = 0.81).

Worked Task Example
Board forecast and disclosure update

In this edited curriculum example, the agent updates a board pre-read with a revised management forecast, its valuation implications, and the distinction between board approval and counsel clearance.

›
INSTRUCTION
Task

Project Aurora's target board meets at 4:30 p.m. CT on April 17 while investor education is underway, and the forecast response item has to be resolved for tomorrow's registration-statement turn. Update the existing board pre-read in place, limited to its forecast-and-disclosure section and the related director decision callout, so it presents the current management case, carries the revision through the transaction-valuation read-across, and gives the board a clear decision on the forecast basis it is being asked to approve and the position management may use in roadshow discussions pending completion of the next disclosure turn. Work as of 12:00 p.m. CT on April 17, preserve the rest of the document and its formatting, and distinguish what the board can decide now from anything that still requires counsel clearance.

Deliverable

Edit /filesystem/Aurora/DealRoom/Board/project-aurora-board-financing-update.docx in place. Do not rename it, copy it, or save your work under a new filename.

›
ENVIRONMENT
›
GRADER
References and Notes
[1]

Ivison, H., et al. (2026). TMax: A Simple Recipe for Terminal Agents. arXiv:2606.23321.

↩ 1
↩ 2
[2]

Wang, Z., et al. (2026). Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning. arXiv:2602.10090.

↩
[3]

Zeng, Y., et al. (2026). EnvCraft: Synthesizing Executable Environments in Agentic RL for Claw-like Agent. arXiv:2609.05576.

↩
[4]

Zuo, Y., et al. (2026). Qwen-AgentWorld: Language World Models for General Agents. arXiv:2606.24597.

↩
[5]

Ramrakhya, R., et al. (2025). Scaling Synthetic Task Generation for Agents via Exploration. arXiv:2509.25047.

↩
[6]

Li, Z., et al. (2026). Recursive Synthesis for Long-Horizon Terminal Tasks. arXiv:2608.05466.

↩
[7]

Li, J., et al. (2026). Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application. arXiv:2606.12191.

↩
[8]

DeepSeek-AI (2026). DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression. Technical report.

↩
[9]

LLM-Core, Xiaomi (2026). MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement. Technical report.

↩ 1
↩ 2
[10]

Harbor Framework Team (2026). Harbor: A framework for evaluating and optimizing agents and models in container environments. GitHub. Task specification.

↩ 1
↩ 2
[11]

Gunjal, A., et al. (2025). Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains. arXiv:2507.17746.

↩
[12]

Khazi, D., et al. (2026). Notes on Choosing a Rubric Judge. Paper Instruments Blog.

↩ 1
↩ 2
↩ 3
[13]

Epoch AI (2026, September 17). Introducing Benchmark Reviews. X post.

↩
[14]

OpenAI (2026). Separating signal from noise in coding evaluations. OpenAI.

↩
[15]

Yu, Y., et al. (2023). Large Language Model as Attributed Training Data Generator: A Tale of Diversity and Bias. arXiv:2306.15895.

↩
[16]

Paper Instruments (n.d.). Rubric: A Python library for LLM-based evaluation using weighted rubrics. GitHub.

↩
[17]

NVIDIA (2026). Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning. arXiv:2606.15007.

↩
[18]

Anthropic (n.d.). Claude Code overview. Official documentation.

↩
[19]

OpenAI (n.d.). Codex. GitHub.

↩
[20]

Cursor (n.d.). Cursor. Official issue-tracker repository. Harness engineering description.

↩
[21]

Moonshot AI (n.d.). Kimi Code CLI. GitHub. Earlier Python implementation.

↩
[22]

OpenAI (n.d.). OpenAI Agents SDK for Python. GitHub.

↩
[23]

Anomaly (n.d.). OpenCode. GitHub.

↩
[24]

OpenHands (n.d.). OpenHands. GitHub.

↩
[25]

OpenHands (n.d.). OpenHands Software Agent SDK. GitHub.

↩
[26]

Qwen (n.d.). Qwen Code. GitHub.

↩
[27]

SWE-agent (n.d.). mini-SWE-agent. GitHub.

↩
[28]

Terminal-Bench contributors (n.d.). Terminus. GitHub. Agent description.

↩
[29]

SWE-agent (n.d.). SWE-agent. GitHub.

↩
[30]

Brown, W. (2025). Verifiers: Environments for LLM Reinforcement Learning. GitHub.

↩
[31]

Piché, A., et al. (2025). PipelineRL: Faster On-policy Reinforcement Learning for Long Sequence Generation. arXiv:2509.19128.

↩ 1
↩ 2
↩ 3
[32]

Paper Instruments (n.d.). Paper Office. Paper Instruments.

↩
[33]

E2B (n.d.). Sandbox persistence. Documentation.

↩
[34]

Martin, L., Cemaj, G., & Cohen, M. (2026). Scaling Managed Agents: Decoupling the brain from the hands. Anthropic Engineering.

↩
[35]

Paper Instruments (2026). Kos-1 Lite: SOTA Medical Model. Paper Instruments Blog.

↩
[36]

Fang, Q., et al. (2026). Kos-1 Experimental: Env-Free RL on a 1T Parameter Agentic Prior. Paper Instruments Blog.

↩
[37]

MiniMax (2025). MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention. arXiv:2506.13585.

↩ 1
↩ 2
[38]

Ma, W., et al. (2025). Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers. arXiv:2510.11370.

↩
[39]

Liu, Z., et al. (2025). Understanding R1-Zero-Like Training: A Critical Perspective. arXiv:2503.20783.

↩ 1
↩ 2
[40]

Yu, Q., et al. (2025). DAPO: An Open-Source LLM Reinforcement Learning System at Scale. arXiv:2503.14476.

↩
[41]

Hilton, J., Cobbe, K., & Schulman, J. (2021). Batch Size-Invariance for Policy Optimization. arXiv:2110.00641.

↩
[42]

Fang, Q., & Khazi, D. (2025). Mismatch Praxis: Rollout Settings and IS Corrections. Paper Instruments Blog.

↩
[43]

Mistral-AI (2025). Magistral. arXiv:2506.10910.

↩
[44]

Z.ai (2026). GLM-5.3-Flash. Model card.

↩
[45]

Hu, E. J., et al. (2021). LoRA: Low-Rank Adaptation of Large Language Models. arXiv:2106.09685.

↩
[46]

Li, Y., et al. (2026). JobBench: Aligning Agent Work With Human Will. arXiv:2605.26329.

↩
[47]

Zhang, Y., et al. (2026). FrontierFinance: A Challenging Benchmark for Measuring Frontier Intelligence of Finance Agents. arXiv:2608.11683.

↩
[48]

Shepard, D., & Salimans, R. (2026). AutomationBench. arXiv:2604.18934.

↩
[49]

Musaeus, M. H., et al. (2026). DiligenceBench: An Equity-Research Agent Evaluation. Paper Instruments Blog.

↩
[50]

Vidgen, B., et al. (2026). APEX-Agents. arXiv:2601.14242.

↩
[51]

Merrill, M. A., et al. (2026). Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces. arXiv:2601.11868. Terminal-Bench 2.1 release.

↩
[52]

Huang, W., et al. (2026). DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks. arXiv:2607.07946. Leaderboard.

↩
Notes to Evaluations
JobBench. Run on the leaderboard's harness, OpenCode 1.14.18, with the Grok 4.3 judge, on the 65-task main split. GLM-5.3 Flash, Gemini 3.8 Flash and DeepSeek V4.1 Flash were run by us in the same harness; other comparison scores are from the JobBench leaderboard.
PI Knowledge Work. An internal suite of client-ready deliverables (Excel, PowerPoint, Word) and tasks in live business systems, run in Feather with a 262,144-token context window. Each task is graded against its own rubric by GPT-5.6 Terra.
FrontierFinance. Run on the official Finance Agent v2 harness with the Appendix E tool limits and Samaya's three-judge grader, over all 220 queries; we report R_all. The official 300-second tool budget includes model-serving time; without it, Ultramarine 1 Flash scores 58.1, GLM-5.3 Flash 56.7 and DeepSeek V4.1 Flash 55.8. GLM-5.3 Flash and DeepSeek V4.1 Flash were run by us; other comparison scores are from the Samaya leaderboard.
AutomationBench. Run on the 600 public tasks with the upstream harness (v1.0.6). GLM-5.3 Flash is as reported by Z.ai. Gemini 3.8 Flash and DeepSeek V4.1 Flash were run by us; Claude Fable 5, GPT-5.6 Sol and Kimi K3 are the public-set scores reported by their developers.
DiligenceBench. This is our own benchmark, and all models were run by us on its H3 Finance harness over all 150 tasks, graded by GPT-5.5.
APEX-Agents 1.1. Run with Mercor's Loop agent, the leaderboard harness; we report Pass@1 averaged over three runs. Comparison scores are from the Mercor Pass@1 leaderboard.
Terminal-Bench 2.1. Run with Claude Code 2.1.207 on the 89 official tasks, one trial per task. Comparison scores are as reported by each model's developer.
DeepSWE 1.1. Run with the leaderboard's harness and attempt count: Pier with mini-SWE-agent, four attempts on each of the 113 tasks. Comparison scores are from the Datacurve leaderboard, except DeepSeek V4.1 Flash, which is as reported by DeepSeek.
Token counts. Output tokens, reasoning included, summed over every task of the runs behind each reported score. For AutomationBench and APEX-Agents 1.1, Table 8 reports GLM-5.3 Flash's public scores. We also ran GLM-5.3 Flash on both ourselves, and its token counts there come from our runs closest to the public scores.
© 2026 PAPER INSTRUMENTS, INC.
DOCS
CAREERS
CONTACT
GITHUB
PRIVACY
TERMS
SOC 2 TYPE II
