# Authoring Guide — Numbered Process Steps

Read this before minting anything for an ordered, numbered sequence of steps within a process or workflow — "Step 1: Explore," "Step 2: Plan," a 3-step coding workflow, a 4-step onboarding protocol. This is a **structural pattern**, not a single term: it composes already-confirmed upstream terms together. `lexicon-map.yaml` catalogs individual word↔IRI mappings; it does not, and should not, catalog multi-property recipes like this one — that's what this file is for. Skip this file and you will very likely mint a bespoke native class for something `schema:HowTo`/`schema:HowToStep` already say.

---

## The pattern

The process itself is a `prov:Activity` (or a native subclass of it, `biz:Process`) **dual-typed** `schema:HowTo`. Each step is a `schema:HowToStep` individual, ordered by `schema:position`, linked from the process via `schema:step`:

```turtle
aiw:<process-slug> a prov:Activity, schema:HowTo ;
    rdfs:label "..."@en ;
    rdfs:comment "..."@en ;
    prov:wasAssociatedWith aiw:<agent> ;
    prov:used aiw:<tool-or-system> ;
    schema:step aiw:<step-1-slug>, aiw:<step-2-slug>, ... .

aiw:<step-1-slug> a schema:HowToStep ;
    schema:position "1"^^xsd:integer .

aiw:<step-2-slug> a schema:HowToStep ;
    schema:position "2"^^xsd:integer .
```

- [ ] The **process** is `prov:Activity` (or a subclass of it) **and** `schema:HowTo` — both types, not one or the other. `prov:Activity` alone can't express "this thing has ordered steps"; `schema:HowTo` alone can't express PROV provenance (`wasAssociatedWith`, `used`).
- [ ] Each **step** is `schema:HowToStep` — never a native class. `schema:position` is an `xsd:integer` literal (not a string), 1-indexed.
- [ ] The process links to its steps via `schema:step` (not a native "hasStep"/"includesStep" property) — `schema:step`'s range is exactly `schema:HowToStep`.
- [ ] Steps are ordered purely by `schema:position`; there's no separate "next step" chain to maintain.

**Worked example for this deployment:** `wiki/tools/claude-code.md`'s "Explore-plan-code workflow" section (Anthropic engineering best practices, May 2026) describes exactly this shape — "Step 1 (Explore): Claude reads relevant files in plan mode... Step 2 (Plan): Claude writes a plan doc... Step 3 (Code): Claude implements against the approved plan." That models as:

```turtle
aiw:explore-plan-code-workflow a prov:Activity, schema:HowTo ;
    rdfs:label "Explore-Plan-Code Workflow"@en ;
    rdfs:comment "Anthropic's recommended three-step workflow for non-trivial coding tasks in Claude Code: read-only exploration, a reviewable plan, then implementation."@en ;
    prov:used aiw:claude-code ;
    schema:step aiw:explore-step, aiw:plan-step, aiw:code-step .

aiw:explore-step a schema:HowToStep ;
    rdfs:comment "Claude reads relevant files in plan mode — no edits permitted."@en ;
    schema:position "1"^^xsd:integer .

aiw:plan-step a schema:HowToStep ;
    rdfs:comment "Claude writes a plan doc; the user can open it in a text editor (Ctrl+G) for review and editing before any code is written."@en ;
    schema:position "2"^^xsd:integer .

aiw:code-step a schema:HowToStep ;
    rdfs:comment "Claude implements against the approved plan; commits after each logical unit."@en ;
    schema:position "3"^^xsd:integer .
```

Read `wiki/tools/claude-code.md` directly (`## Best practices` → `**Explore-plan-code workflow**`) for the full source prose if this guide is ambiguous on a specific point.

---

## Before minting anything, check for reuse

- [ ] **Does the process itself already exist as a `schema:HowTo`?** If you're adding a step to an *existing* wizard/protocol, don't create a second `prov:Activity` for the same process — add the step to the existing one's `schema:step` list.
- [ ] **Is "step N" already declared somewhere as a `schema:HowToStep` individual?** Grep `wiki/**/*.ttl` for `schema:HowToStep` and compare against what you're about to model — a step mentioned on two different source pages (e.g. a process overview *and* a detail page) is still one step, one individual.
- [ ] **Do not mint a native "step" class.** A numbered step in a wizard is `schema:HowToStep`, full stop — there is no scenario in this project's vocabulary where a bespoke `swe:ConfigurationStep`-style class adds anything `schema:HowToStep` + `schema:position` doesn't already say.

**Illustrative lesson (from the source project this guide was ported from):** a backlog review of a source document's UI/wizard terms encountered several numbered-step nouns and, without first checking whether a `schema:HowToStep` individual with a `schema:position` value already existed for each one, proposed a brand-new, never-declared step class instead of reusing `schema:HowToStep`. The mistake wasn't caught until a full audit compared the lexicon's claimed types against the graph directly. Lesson: a bare noun phrase that *sounds* like "a step in a numbered sequence" is exactly this pattern — check `schema:HowToStep` usage before minting anything, the same way a measured-metric guide would say to check for an existing KPI class before minting a new one.

---

## Optional: native `ProtocolStep` overlay (when a native process class already exists)

Some processes could also be modeled as a native `biz:Process` (dual-typed alongside `prov:Activity`/`schema:HowTo`) with a native step class, when the process composes several sub-processes (`biz:includesStage`) and the plain `schema:HowTo` overlay alone doesn't capture that structure. In that case each step is **dual-typed** `schema:HowToStep` *and* the native step class, and the native layer carries its own explicit ordering chain in addition to `schema:position`:

```turtle
aiw:<process-slug> a prov:Activity, biz:Process, schema:HowTo ;
    biz:includesStage aiw:<sub-process-slug> ;
    schema:step aiw:<step-1-slug>, aiw:<step-2-slug> .

aiw:<sub-process-slug> a biz:Process ;
    biz:includesStep aiw:<step-1-slug>, aiw:<step-2-slug> .

aiw:<step-1-slug> a schema:HowToStep, biz:ProtocolStep ;
    schema:position "1"^^xsd:integer ;
    biz:precedes aiw:<step-2-slug> .
```

- [ ] Each step is dual-typed `schema:HowToStep, biz:ProtocolStep` (or whichever native step class the source's own vocabulary module already confirms — never mint a new one; see the "what went wrong" note above).
- [ ] The native chain adds `biz:precedes` between consecutive steps, **in addition to** (not instead of) `schema:position` — the two are redundant by design (native ordering fact + schema.org overlay fact), matching how this project layers a schema.org overlay on top of pre-existing native facts rather than replacing them (see `sync-model.md`).
- [ ] The process is linked to its sub-processes via `biz:includesStage` (a named phase) and to its steps via `biz:includesStep`, alongside the overlay's own `schema:step`.

**Status in this deployment:** `biz:Process`/`biz:ProtocolStep`/`biz:precedes`/`biz:includesStage`/`biz:includesStep` were all carried over intact by the VCR-0001 inheritance (they're generic business-process vocabulary, not MUSCLE-specific), so this overlay remains available — but as of this writing no `wiki/workflows/*.md` page has needed it yet; the plain `prov:Activity, schema:HowTo` + `schema:HowToStep`/`schema:position` pattern above (see the Claude Code explore-plan-code example) covers every numbered sequence modeled so far. Reach for this overlay only once a workflow genuinely composes multiple named sub-stages, not by default.

---

## Naming convention

- [ ] Step individuals: `aiw:<descriptive-slug>` — no numeric suffix in the IRI itself (the number lives in `schema:position`, not the identifier). Match the step's own name/label as closely as the source allows (`aiw:explore-step`, `aiw:plan-step`).
- [ ] The process individual takes the process's own name (`aiw:explore-plan-code-workflow`), not a generic "wizard" or "protocol" slug.

## Before finishing

- [ ] Confirmed the process either already exists (add to its `schema:step` list) or is genuinely new (mint as `prov:Activity, schema:HowTo`).
- [ ] Grepped `wiki/**/*.ttl` for `schema:HowToStep` and confirmed each step doesn't already exist elsewhere under a different source page.
- [ ] Did not mint a native step class — every step is `schema:HowToStep` + `schema:position`, optionally dual-typed with an already-confirmed native step class (e.g. `biz:ProtocolStep`) plus a `biz:precedes` chain.
