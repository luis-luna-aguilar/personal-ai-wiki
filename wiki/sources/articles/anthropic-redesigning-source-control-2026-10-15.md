---
title: Redesigning source control at Anthropic
type: source
source_type: article
source_file: raw/articles/2026-10-19-anthropiccom-engineering-redesigning-source-control.md
url: https://www.anthropic.com/engineering/redesigning-source-control
published: 2026-10-15
ingested: 2026-10-19
domains: [coding, agents]
---

# Redesigning source control at Anthropic

An Anthropic engineering post on Scion, the in-house version control system that replaced git for Anthropic's monorepo once agent-written code pushed merges from ~2,500 to 30,000+ a day. It sets out the design principles for source control whose clients are always-online agents and jobs, how Scion's data model and tiered caches work, and broader lessons about building with Claude: small teams shipping large migrations fast, engineers steering rather than writing code, Claude "superfan" monitoring channels, and replacing the merge queue. The captured version is marked "Updated October 15"; the original publication date is not in the file, so `published:` uses the update date.

## Influenced pages

- [Engineering AI adoption: evidence from practice](../../training/engineering-ai-adoption-evidence.md) — Scion case-study bullet
- [AI enablement — software development](../../training/ai-enablement-software-development.md) — new developer-infrastructure bottleneck pattern; adversarial-review caveat

## Key claims extracted

- Coding is no longer Anthropic's bottleneck; source control, builds, and CI (infrastructure built for human scale) are
- Merges per day: ~2,500 in May 2026, 30,000+ in September 2026; growth expected to continue
- Monorepo: main-branch history ~100 GB, compressed working copy 25 GB+, ~25M CI checkouts/day (600+ PB/day of git traffic if naive); several hundred internal git mirrors at peak
- Scion principles: clients always online; client-server asymmetry (server does history, blame, commits, merges, rebases); every source-control query exposed as an API; everything horizontally scalable, no fully materialized repo copy; cheap, incremental, lock-free commits with refs discouraged; working copy optional and sparse/virtualized by design
- Prior art: Google Piper, Meta Sapling (Mononoke server, Bonsai data model)
- Data model: changesets in a write-ahead log storing changed files vs first parent plus content-addressed blob pointers; "derived data" (blame, path history, commit-graph skip lists) computed recursively and eagerly or lazily
- Architecture: Spanner-backed scion-servers, regional scion-cache tier, per-node scion-daemon; identical RPCs across tiers; 99%+ cache hit rate per tier
- Results: infrastructure 200x smaller (CPU and memory) than git mirroring; checkouts in seconds instead of minutes; 25% CI CPU capacity win
- Seven people built Scion, Antique (code review), and half a dozen related systems and migrated in five months while daily merges grew 10x
- Early Claude Mythos Preview rewrote the hand-written ingestion pipeline with no further instructions: 20x less memory, 4x faster, invariants preserved
- Engineers rate Claude better at writing code than themselves; their role is often telling Claude "no" when agents violate system constraints or adversarial review drives over-engineering; humans review every change for intent, not every line
- Hermetic simulations, fuzzing, and rate limiting made Scion among the best-tested codebases the team has worked on
- Directory-level permissions and semantic approval constraints in code review (e.g. comment-only vs logic changes)
- Per-component Claude Tag "superfan" Slack channels monitor telemetry and logs and catch issues alerts miss
- Global-lock merge queue abandoned for post-merge and pre-deploy automated testing; Claude fixes concurrent-change conflicts
- Limits stated by Anthropic: only sensible for enormous monorepos; Anthropic's internal token spend is unusual; Scion will not be released; recommends git servers adopt server-side RPCs and composable sparse/shallow features; expects the problem class to spread within 6-12 months
