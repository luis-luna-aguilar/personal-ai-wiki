---
type: proposal
source: raw/articles/2026-11-23-cognitioncom-blog-factoring-rsa-260.md
status: pending
created: 2026-11-24
---

# Proposal: Devin swarm factors RSA-260 (Cognition, 2026-09-09)

## Summary

### In short
A swarm of coding agents can now re-engineer a mature mathematical pipeline for new hardware and set records with it, but only with a human supplying decomposition, measurement and executive function. Cognition's Devin sessions rebuilt the CADO-NFS factoring software for GPUs in three weeks and factored RSA-260, with the researcher sending 3,328 messages along the way. The proposal adds a computational-number-theory case to **AI in mathematics**, a human-share measurement to **Multi-agent coordination: evidence**, a short line on **Devin**, and one source page. One hesitation: factoring is engineering, not new mathematics, so it stretches the math page's scope.

[[#Open questions|Open questions: 1 to answer.]]

- [x] **Approve all** — checking this box approves every item in `## Intended changes` and `## Schema / vocabulary additions` below; the individual boxes may stay empty.

### The source
On 9 September 2026 Cognition researcher Eric Lu published "Factoring RSA-260". On 13 August he asked Devin to write a GPU replacement for the lattice siever in CADO-NFS, the open-source implementation of the general number field sieve (GNFS), the standard algorithm for factoring very large numbers. Nine hours later the GPU siever handled the parameters used for RSA-250. Over the next three weeks he ran an average of 3 and at most 18 Devin Cloud sessions at once, which rewrote nearly every stage for GPUs: polynomial selection, sieving, the block Wiedemann linear-algebra step and the square root. Only four CADO programs were left untouched. After a ladder of smaller factorizations, RSA-260 (a 260-digit RSA challenge number) fell after about 15.6 days of wall time and roughly 4,900 GPU-days, finishing on 3 September. The team then factored 2^1277−1, a 385-digit number, which Cognition calls a new record for the special number field sieve.

Lu is frank about his own role. He sent 82,702 words in 3,328 messages across 192 of the 233 sessions (14,450 ACUs, Devin's billing unit). The Devins started 101 child sessions themselves, and 36 of those ran with no input from him. He set goals, kept sessions scoped, stopped unproductive measurements and caught premature give-ups. His largest contribution, he says, was a unified set of benchmarks and performance estimators that "were not otherwise going to self-assemble." He credits CADO-NFS's human-built decomposition as essential and notes that the agents grew more confused the further the code moved from upstream.

### What changes
The wiki has nothing on integer factoring, CADO-NFS or RSA-260; its math page covers proofs from reasoning models.

- **AI in mathematics** gains a "Computational number theory" subsection with the RSA-260 and 2^1277−1 results, one sentence in Why it matters, and a Recent-changes entry dated 9 September. Page date stays 15 October.
- **Multi-agent coordination: evidence** gains a measurement bullet on the human's share of the swarm's work and the dependence on an existing decomposition, plus a Recent-changes entry. Page date stays 12 October.
- **Devin** gains a short "Research swarms" line pointing to both pages and a Recent-changes entry. That list is at its cap of ten, so the SWE-1.7 entry from 9 July moves to history. Page date stays 23 November.
- One new source page, `wiki/sources/articles/cognitioncom-blog-factoring-rsa-260.md`.

### What to weigh
The math page is framed around new mathematical results, while this is a performance-engineering feat on known algorithms. The draft states that plainly in the new subsection and in Why it matters instead of opening a separate page. **State of Cybersecurity** is left alone: the post makes no security claim, and that page is already 9% over its length ceiling.

## Intended changes

- [ ] **Update** `wiki/trends/ai-in-mathematics.md` — add "Computational number theory" subsection and one Why-it-matters sentence; adds one Recent-changes entry dated 2026-09-09 (8 → 9 entries, no spill); append source id and link; `as_of` unchanged (2026-10-15)
- [ ] **Update** `wiki/workflows/multi-agent-coordination-evidence.md` — add one bullet under "Studies and measurements"; adds one Recent-changes entry dated 2026-09-09 (5 → 6, no spill); append source id and link; `as_of` unchanged (2026-10-12)
- [ ] **Update** `wiki/tools/devin.md` — add "Research swarms" subsection; adds one Recent-changes entry dated 2026-09-09 (between the 2026-09-21 and 2026-07-21 entries); append source id and link; `as_of` unchanged (2026-11-23)
- [ ] **Spill** `wiki/tools/devin.md` → `wiki/history/tools/devin.md` — list goes to 11, so the oldest-dated entry (2026-07-09 SWE-1.7) spills
- [ ] **Create** `wiki/sources/articles/cognitioncom-blog-factoring-rsa-260.md` — source summary

## Page drafts

### wiki/trends/ai-in-mathematics.md (updated)

Frontmatter: append `cognitioncom-blog-factoring-rsa-260` to `sources:`; `as_of` stays 2026-10-15.

New subsection, inserted after "### Compute-scale claims and priority disputes" (end of `## Current status`):

```
### Computational number theory

- **A Devin swarm factors RSA-260 on GPUs (2026-09-09):** Cognition researcher Eric Lu had Devin rebuild CADO-NFS, the open-source implementation of the general number field sieve (GNFS), for GPUs. The first GPU lattice siever handled RSA-250 parameters nine hours after the first prompt; over three weeks, an average of 3 and a peak of 18 parallel Devin sessions rewrote nearly every stage (polynomial selection, sieving, block Wiedemann linear algebra, square root), leaving four CADO programs untouched. After a ladder of smaller factorizations (155 to 311 digits in the first five days), RSA-260, a 260-digit RSA challenge number, fell in about 15.6 days of wall time and roughly 4,900 GPU-days on B200/GB200/GB300 nodes, finishing 2026-09-03. The team then factored 2^1277−1 (385 digits), which Cognition calls a new record for the special number field sieve (SNFS). No new mathematics was involved, and Lu says he understands little of it; the human's share of the work is on [Multi-agent coordination: evidence](../workflows/multi-agent-coordination-evidence.md).
```

`## Why it matters` — append one sentence at the end of the paragraph:

```
The RSA-260 factorization (2026-09-09) is a different kind of contribution: no new theorem, but a coding-agent swarm re-engineering a mature open-source math pipeline for new hardware, with an expert human supplying decomposition and measurement rather than proofs.
```

`## Recent changes` — insert one entry above the 2026-09-08 entry:

```
- [2026-09-09] A Cognition Devin swarm rebuilt CADO-NFS for GPUs and factored RSA-260 (about 15.6 days wall time) and 2^1277−1 (C385, an SNFS record per Cognition); first computational-number-theory case on the page.
```

`## Sources` — append:

```
- [Cognition — Factoring RSA-260](../sources/articles/cognitioncom-blog-factoring-rsa-260.md)
```

### wiki/workflows/multi-agent-coordination-evidence.md (updated)

Frontmatter: append `cognitioncom-blog-factoring-rsa-260` to `sources:`; `as_of` stays 2026-10-12.

`### Studies and measurements` — append one bullet at the end:

```
- Cognition's RSA-260 factorization (2026-09-09) measures the human's share of a three-week swarm: the researcher sent 82,702 words in 3,328 messages to 192 of 233 Devin sessions (14,450 ACUs, at most 18 running at once); the Devins started 101 child sessions themselves, and 36 of those ran with no human input. He supplied executive function (a goal hierarchy, scoping, redirecting unproductive measurements, catching premature give-ups) and, above all, a unified set of benchmarks and performance estimators that "were not otherwise going to self-assemble". The swarm leaned on CADO-NFS's human-engineered decomposition (fixed stage interfaces plus a CPU reference to compare outputs against), and the agents grew more confused the further the code moved from upstream. See [AI in mathematics](../trends/ai-in-mathematics.md).
```

`## Recent changes` — insert one entry between the 2026-09-17 and existing 2026-09-09 entries:

```
- [2026-09-09] Added Cognition's RSA-260 factorization as a measurement of the human's share in a three-week Devin swarm (3,328 messages to 192 of 233 sessions; 36 of 101 agent-started child sessions ran untouched).
```

`## Sources` — append:

```
- [Cognition — Factoring RSA-260](../sources/articles/cognitioncom-blog-factoring-rsa-260.md)
```

### wiki/tools/devin.md (updated)

Frontmatter: append `cognitioncom-blog-factoring-rsa-260` to `sources:`; `as_of` stays 2026-11-23.

New subsection, inserted after "### Dynamic Workflows and Devin trees" (end of `## Current status`):

```
### Research swarms

- **RSA-260 factorization (2026-09-09):** up to 18 parallel Devin Cloud sessions (233 in all, 14,450 ACUs) rebuilt the CADO-NFS factoring pipeline for GPUs over three weeks and factored RSA-260; Cognition credits sessions that persist, run sandboxed and can work autonomously for weeks. Results on [AI in mathematics](../trends/ai-in-mathematics.md); the human's share on [Multi-agent coordination: evidence](../workflows/multi-agent-coordination-evidence.md).
```

`## Recent changes` — insert one entry between the 2026-09-21 and 2026-07-21 entries, then remove the 2026-07-09 SWE-1.7 entry (spilled below):

```
- [2026-09-09] A Devin Cloud swarm (up to 18 concurrent sessions, 233 total) rebuilt CADO-NFS for GPUs and factored RSA-260 and 2^1277−1.
```

`## Sources` — append:

```
- [Cognition — Factoring RSA-260](../sources/articles/cognitioncom-blog-factoring-rsa-260.md)
```

### wiki/history/tools/devin.md (updated)

Append at the end of the file:

```
## Archived from current page on 2026-11-24

- [2026-07-09] Cognition released SWE-1.7, a budget frontier coding model post-trained from Kimi K2.7 inside Devin's agent harness; per The Code's recap, Cognition claims it matches GPT-5.5 within a point on FrontierCode at ~$2/task with Opus 4.8 slightly ahead (secondhand, tier unspecified); supports up to six-hour sessions via self-summarization and resume.
```

### wiki/sources/articles/cognitioncom-blog-factoring-rsa-260.md (new)

```
---
title: Cognition — Factoring RSA-260
type: source
source_type: article
source_file: raw/articles/2026-11-23-cognitioncom-blog-factoring-rsa-260.md
url: https://cognition.com/blog/factoring-rsa-260
published: 2026-09-09
ingested: 2026-11-24
domains: [science, coding, agents]
---

# Cognition — Factoring RSA-260

Cognition researcher Eric Lu describes using parallel Devin Cloud sessions to rebuild CADO-NFS, the open-source general number field sieve (GNFS) implementation, for GPUs, and using it to factor RSA-260 and 2^1277−1. The first prompt (13 August 2026) asked for a GPU drop-in for CADO's CPU lattice siever; nine hours later it handled RSA-250 parameters. Over three weeks Devin rewrote nearly every pipeline stage. RSA-260 took about 15.6 days of wall time (finishing 2026-09-03); 2^1277−1 (385 digits) followed on 2026-09-08 as what Cognition calls an SNFS record. Lu details the human's share of the work and how much the agents depended on CADO-NFS's existing decomposition. A long appendix gives per-stage timings, parameters and polynomials for every factorization. Published 2026-09-09.

## Influenced pages

- [AI in mathematics](../../trends/ai-in-mathematics.md) — new computational-number-theory case
- [Multi-agent coordination: evidence](../../workflows/multi-agent-coordination-evidence.md) — human share of a long-running swarm
- [Devin](../../tools/devin.md) — research-swarm line

## Key claims extracted

- GPU lattice siever (`glas`) handled RSA-250 parameters about 9 hours after the first prompt.
- Average 3, peak 18 concurrent Devin sessions over three weeks; GPU polynomial selection (with msieve components), GPU lattice siever, optimized CADO head, parallel dup/purge and fused merge/replay, GPU block Wiedemann, GPU square root; only `cado-nfs.py`, `polyselect_ropt`, `makefb` and `dup1` untouched.
- Scaling ladder: within five days, a 190-digit number took as long as a 157-digit one at the start (a little over 3 hours); C311 = (179^139−1)/178 in about 14.3 hours.
- RSA-260: 2026-08-18 to 2026-09-03, 1,344,878 s wall time, about 4,923 GPU-days; 8.3 billion relations from sieving; sieving 7.9 days on B200/GB200/GB300 nodes.
- C385 = 2^1277−1 factored 2026-09-03 to 2026-09-08 (455,206 s, 2,423 GPU-days) into p106 × p117 × p163; called a new SNFS record.
- Human share: 82,702 words in 3,328 messages across 192 of 233 sessions (14,450 ACUs); Devins started 101 child sessions, 36 with no human intervention.
- Human supplied executive function and a unified benchmark/measurement system; agents grew more confused as code diverged from upstream CADO-NFS; the author does not understand much of the underlying mathematics.
```

## Schema / vocabulary additions

None.

## Open questions

- Should **State of Cybersecurity** get a one-line cryptography entry for the RSA-260 result? It is left out because the source makes no security claim and the page is already over its length ceiling.
	- No
