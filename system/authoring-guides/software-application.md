# Authoring Guide — `schema:SoftwareApplication` Sidecars

Read this before writing any sidecar for a `schema:SoftwareApplication` (a `wiki/tools/*.md` page — an AI coding agent, voice product, research tool, or other AI tool). Work through every checkbox; paste the completed list into the proposal's **Sidecar Authoring Checklist** section.

---

## Required triples

- [ ] `a schema:SoftwareApplication` declared.
- [ ] `rdfs:label "..."@en` — at least one English label (`"Claude Code"@en`).
- [ ] `rdfs:comment "..."@en` — one English gloss describing what the application *is* (`"Anthropic's terminal-first AI coding agent."@en`).
- [ ] `schema:provider aiw:<org>` — exactly one provider organization (`aiw:SoftwareApplicationShape` enforces this) — e.g. `schema:provider aiw:anthropic`, following `entity.md`'s pattern for the org individual itself.

---

## Subject matter (schema:about)

- [ ] `schema:about aiw:<concept>` — for every domain concept the product *is about* (e.g. its primary subject). In this deployment, prefer the `_schema`-derived domain/subcategory concepts (VCR-0002) where they fit — `wiki/tools/claude-code.md`'s frontmatter (`domains: [coding, agents]`, `subcategory: terminal-coding-agent`) maps to `schema:about aiw:domain-coding, aiw:domain-agents` and `aiw:hasSubcategory aiw:subcategory-terminal-coding-agent` once page-to-schema backfill wires frontmatter into the graph (see VCR-0002's "not yet asserted" deferral).
- [ ] All targets must be `skos:Concept` instances — either the `_schema` concepts above or a page-local `aiw:<slug> a skos:Concept` per `skos-concept.md`.
- [ ] Never use `biz:<concept>` or `swe:<concept>` as targets — those namespaces hold predicates/classes, not (typically) concept instances; the one exception (a reusable industry concept like `biz:commercial-banking`) is covered in `skos-concept.md`'s namespace-discipline section.
- [ ] Do not use `schema:knowsAbout` on a SoftwareApplication — that predicate is for organizations (see `entity.md`).

---

## API and integration triples

- [ ] For each external API the product consumes, assert `swe:consumesAPI aiw:<api-slug>`.
- [ ] The API endpoint must itself be an individual (at minimum: `a swe:API ; rdfs:label "..."@en`) — `swe:API` is the confirmed class (`lexicon-map.yaml`); do not use `schema:WebAPI`, which was never confirmed.
- [ ] Use `swe:embeds aiw:<component>` for embedded sub-applications, or `swe:embeddedIn` for the inverse direction when the tool itself is the thing embedded — e.g. `wiki/tools/claude-code.md` documents Claude Code shipping as a VS Code extension, which models as `aiw:claude-code swe:embeddedIn aiw:vs-code`.

**Worked example, illustrative of the whole pattern (built from `wiki/tools/claude-code.md`'s actual content):**

```turtle
aiw:claude-code a schema:SoftwareApplication ;
    rdfs:label "Claude Code"@en ;
    rdfs:comment "Anthropic's terminal-first AI coding agent; runs in the shell, operates autonomously on files, shell commands, and tool calls."@en ;
    schema:provider aiw:anthropic ;
    schema:about aiw:domain-coding, aiw:domain-agents ;
    swe:embeddedIn aiw:vs-code ;
    swe:consumesAPI aiw:github-api ;
    aiw:hasBenchmarkResult aiw:claude-code-swe-bench-result .

aiw:github-api a swe:API ;
    rdfs:label "GitHub API"@en .
```

(`aiw:claude-code-swe-bench-result` follows the reified `aiw:BenchmarkResult` pattern from VCR-0003 — `onBenchmark`/`achievedBy`/`scoreValue`/`scoreUnit`/`asOf` — not shown here since it's a separate structural pattern, not part of this guide.)

---

## Deployment / hosting availability

- [ ] Where the source states which **hosting platforms** or **API surfaces** a tool is available through, assert `swe:hostedOn aiw:<platform>` per platform. `wiki/tools/claude-code.md` states availability "on the Claude API, Amazon Bedrock, Vertex AI, and Microsoft Foundry" — each of those is a `swe:HostingPlatform` individual, and the tool asserts one `swe:hostedOn` triple per platform.
- [ ] The inherited `swe:DeploymentEnvironment` enum (`swe:development-environment`/`qa-environment`/`staging-environment`/`production-environment`, VCR-0001) models a product's *internal* dev/staging/production pipeline tiers. That fits a company's own product (as it did for MUSCLE's dashboards in the source project) more than a third-party AI tool this wiki merely catalogs — **don't force a tool page to assert deployment-environment triples it has no source basis for.** Reach for `swe:hostedOn`/`swe:HostingPlatform` (cloud/API availability) as the far more common fact shape in this wiki instead; keep `swe:DeploymentEnvironment` on file for the rarer case a source does describe a tool's own internal release pipeline.
- [ ] Link via `swe:deployedTo aiw:<env-slug>` only in that rarer case — `swe:hasDeployment` does not exist in the ontology; the confirmed property is `swe:deployedTo` (`swe.ttl`).

---

## schema:about vs schema:knowsAbout

- [ ] `schema:about` goes on SoftwareApplications (and source-summary pages) pointing to concepts they cover.
- [ ] `schema:knowsAbout` goes on organizations. Never swap these.

---

## Before finishing

- [ ] Run `python3 system/scripts/verify_links.py` — confirms no broken markdown links.
- [ ] Run `knowledge-graph/scripts/validate-page.sh` on the sidecar — confirms shape conformance.
- [ ] Grep for any undefined IRI prefixes: `biz:<noun>`, `swe:<noun>` that are meant to be concept instances — these are bugs.
