# Authoring Guide — Minting or Classifying a Vocabulary Term

Read this **before** proposing any new class, property, or individual in a VCR — not after. It was ported from the MUSCLE company-brain repo this knowledge-graph layer was bootstrapped from (VCR-0001); it exists because that source project's VCR 0011 made a distinct classification mistake for nearly every step below, each corrected only because a human caught it. The "What went wrong" call-outs below cite that source project's VCR numbers (0008, 0009, 0011, 0012, 0014, 0020) for traceability to where each lesson was actually learned — **this deployment's own change history is VCR-0001/0002/0003 only**; none of those other numbers are AI Wiki VCRs. Work through every step in order; each one is a real mistake that already happened at least once, and the underlying failure mode (skipping a reuse check, defaulting to the wrong module, an unself-explanatory name) is exactly as likely here as it was there.

---

## Step 1 — Rung-1 catalog search (did this already exist?)

Before writing anything, grep the **CONFIRMED** section of `knowledge-graph/ontology/lexicon-map.yaml` for the concept — not just the terms you remember, the actual file.

- [ ] Searched `lexicon-map.yaml` for `status: confirmed` entries that already cover this concept, including near-synonyms (a "role" concept might already be `org:Role`; a "software product" concept might already be `schema:SoftwareApplication`).
- [ ] If a confirmed class already exists and fits, reuse it — do not mint a parallel class for the same thing.

**What went wrong in VCR 0011:** `governance-role` minted `biz:GovernanceRole` when `org:Role` was already confirmed and in active use for `bank-administrator`, `head-of-cards`, `head-of-credit-card-loyalty-programs`. `system` minted `swe:System` when `schema:SoftwareApplication` was already confirmed and used for every other MUSCLE product. Both skipped this step.

- [ ] **Also grep the actual `.ttl` files directly, not just `lexicon-map.yaml`'s confirmed entries — and grep past VCR documents (`change-requests/*.md`) for "future work"/"deferred"/"pending" notes that might name the exact concept you're about to admit.** `lexicon-map.yaml` can lag behind the `.ttl` files (it did, throughout this VCR's review — see the process note about freezing it mid-review), and it doesn't capture a prior VCR's *stated intent* for what should happen later.
- [ ] **Check `system/authoring-guides/README.md`'s index for a structural pattern before assuming this concept needs its own term.** Some facts aren't a single term at all — they're a *composition* of several already-confirmed terms (e.g. a measured business metric: `fibo-fnd-utl-alx:KeyPerformanceIndicator` + `biz:metricValue` + `biz:metricUnit` + `biz:changeDirection` + `biz:associatedMetric`, see `kpi-metric.md`). `lexicon-map.yaml` catalogs individual word↔IRI mappings — it does not and should not catalog multi-property recipes, so this class of reuse has no shortcut through the lexicon alone. If a guide exists for the shape of fact you're modeling, it also tells you whether an *instance* (not just the pattern) already exists elsewhere — check that too, per the guide's own instructions.

**Second instance, same VCR, caught only at implementation time:** `modality` → `biz:PricingModality` looked like a new class, but VCR 0008 had already made `biz:hasPricingModality` a `FunctionalProperty` with a SHACL enumeration — the class was only missing the OWL-layer range, not a wholly new concept. Worse: `test-status` → `swe:TestStatus`/`swe:hasTestStatus` was a full duplicate of VCR 0009's `abTestStatus` property (originally `biz:abTestStatus`; consolidated to `swe:abTestStatus` by VCR-0014 once its domain class, `swe:ABTest`, made the `biz:`/`swe:` split visible enough to bother fixing), and VCR 0009's own text explicitly said *"if A/B test entities become first-class modeled individuals in the future, this can be promoted to an object property with a class"* — precisely the situation VCR 0011 created by admitting `swe:ABTest`. Neither VCR 0008 nor VCR 0009 showed up in a `lexicon-map.yaml` grep because their outputs were written straight to `.ttl` (both pre-date the ACE-harvest, so no `lexicon-map.yaml` entries were ever added for `hasPricingModality` or `abTestStatus` themselves — only for their downstream enumeration values). Checking `.ttl` files and old VCRs directly is the only way to catch this class of overlap.

---

## Step 1a — Is this a fact about an existing class, not a new class at all?

A term can pass Step 1's literal-duplicate check (no confirmed row has this exact IRI) and still not need a new class — because it's really a **status or relationship fact about a class that's already confirmed**, just phrased as a noun. This is the same mistake as Step 2's "four rows, one IRI," one level removed: instead of several rows converging on one *proposed* IRI, one row converges on an *already-confirmed* IRI once you ask what it's actually describing.

- [ ] Ask: **does this concept have real, nameable alternatives** — could you point to a second, different instance of the same kind of thing (a different secrets-management tool, a different payment gateway)? If yes, it's a genuine class. If the honest answer is "no, it's just whether/how an already-existing thing relates to another already-existing thing," it's a composition, not a class.
- [ ] Before minting, check whether the noun phrase decomposes into **[already-confirmed class] + [already-confirmed property] + [a status qualifier like `isPending`]**. If it does, use that composition — do not mint a class to hold what is really one triple (or two) about something already in the graph.
- [ ] This is easiest to miss when a source describes an infrastructure/status update ("Datalake access control: pending," "CI/CD integration is pending") — the noun phrase ("Datalake access control," "CI/CD integration") reads exactly like a class name, but the actual fact is about a class you've already confirmed (`swe:Datalake`, the platform itself), not a new one.

**What went wrong in VCR 0012 (first instance):** a single infrastructure-status source document ("Databases ... (Pending access and backup policies)," "Datalake ... Storage tech and access pending," "Hosting ... (Pending scaling and CDN/WAF details)," "CI/CD integration is Pending") produced nine separate proposed classes (`AccessPolicy`, `BackupPolicy`, `CdnDetail`, `WafDetail`, `ScalingDetail`, `DatalakeAccessControl`, `DatalakeIntegration`, `SecretsManagement`, `CiCdIntegration`) — all of them facts about classes that were *already confirmed* (`swe:Datalake`, `swe:Datastore`, `swe:HostingPlatform`) composed with an already-confirmed relation (`swe:integratesWith`) and an already-confirmed qualifier (`swe:isPending`). None of the nine had a real alternative you could name — contrast `secrets-manager` in the same batch, which correctly stayed a class because AWS Secrets Manager, Vault, and LastPass are genuine, nameable alternatives. A direct reviewer question ("we already have an AccessControlService that in this case is for Datalake, so why a new class?") caught the first instance; the rest were found by re-applying the same question to every sibling in the group.

- [ ] **A composition has two halves — an existing class/qualifier, and an existing relation connecting it to something. Both halves must actually hold up, every time, not just the half that's easy to see is right.** Verify the relation's real `rdfs:domain`/`rdfs:range` in the `.ttl` against the classes you're plugging in — don't assert a relation just because it's the most recently-confirmed one you remember, or because "some relation should exist here." If the relation can't type-check against your two classes, it's the wrong relation, full stop — go find the right one (grep `.ttl` for what actually targets that class; there is often already a more specific property, like `usesDatastore`/`hostedOn`, that fits better than a generic one like `integratesWith`) rather than forcing the generic one to fit.
- [ ] **If the composition needs a concrete individual on the other end and the source doesn't name one, you cannot complete that half yet.** Drop the relation for now and assert only the half you can actually ground (usually the qualifier, e.g. `isPending`) — do not invent a placeholder individual just to have something to point the relation at, and do not silently assert the relation anyway with no real target. Add the relation as a real, concrete triple once the source (or a later page) actually names something.

**What went wrong in VCR 0012 (second instance, same review):** five of the nine compositions above were themselves wrong even after the "not a class" call was correct. `ci-cd-integration` and `secrets-management` asserted `swe:integratesWith` pointing at a CI/CD tool and a secrets-manager tool that no source ever names — nothing to point the relation at. `access-policy` and `datalake-access-control` asserted `swe:integratesWith` between `swe:Datastore`/`swe:Datalake` and `swe:AuthenticationService` — but `integratesWith`'s domain/range is strictly `schema:SoftwareApplication`↔`schema:SoftwareApplication`, and a Datastore is not a SoftwareApplication; the relation couldn't type-check no matter what it pointed at. `secrets-management` additionally used `swe:System` as a domain — precisely the anti-pattern this very guide's Step 1 already names as wrong. All five were fixed the same way: drop the ungrounded/type-invalid relation, keep only the qualifier that's actually true (`isPending`), and — for `datalake-integration`, which had a real relation available — use the correct one (`swe:usesDatastore`, not `integratesWith`) instead of dropping it. A direct reviewer instruction ("when you split a concept like that, it needs both parts, all the time") is what caught this; it should not have needed catching.

---

## Step 2 — Class, or Individual reusing an existing class?

A term is only a **Class** if it defines a *new type* — its own `rdfs:comment`, and typically its own members or structure. If the term is just a specific, named thing that happens to be *typed by* an already-existing class, it's an **Individual**, not a Class.

- [ ] Ask: "does this term add a new category to the ontology, or is it one specific instance of a category that already exists?"
- [ ] If the harvested "class" row's proposed IRI is an *already-reused* upstream/native class (e.g. `swe:UIComponent`, `schema:SoftwareApplication`) rather than a newly-defined one, it is almost certainly an Individual, not a Class.

**What went wrong in VCR 0011:** `custom-message`, `discount-badge`, `promotional-banner`, `pricing-view` were all listed as "Class" rows with proposed IRI `swe:UIComponent` — i.e. four different rows all proposing the *same* type. That's the tell: they're four named instances of `UIComponent`, not four classes. Should have been `muscle:custom-message` (type `swe:UIComponent`), etc., in the Individual table from the start.

- [ ] **When an individual's type comes from "it was listed alongside similar things," verify the class's semantics actually match what the source says *this specific instance* does — don't type by list-membership or proximity.** Read the individual's own sentences, not just which bullet/section it appeared under.

**Second instance, same VCR:** `matrix-simulator` was typed `swe:ReportingModule` purely because the source listed it as the fourth item alongside `Volume-Metrics`/`Pricing-Results`/`Admin-Reports` (all genuine reports). Its own sentences say something different: *"Matrix-Simulator evaluates a pricing-strategy. Matrix-Simulator projects Cpp"* and "a projection tool that uses past redemptions to evaluate potential strategic scenarios" — that's a forward-looking simulation tool, not a report on historical data. A new class (`swe:SimulationTool`) was needed. The harvest's own ACE line ("Matrix-Simulator is a reporting-module") was itself wrong and got carried through uncritically.

---

## Step 3 — Which module? (Class only)

**In this deployment, the module choice is only ever `swe:`, `biz:` (both inherited verbatim, VCR-0001), or `aiw:` (native, VCR-0003) — there is no `travel:` or `muscle:` module here.** The source project's `vocabulary-policy.md` §6/§6a/§6b tests below still apply; read `travel:` as "not applicable in this deployment" wherever it appears in that policy doc, and read `muscle:` as `aiw:`. Two tests, both required:

- [ ] **External standard / generic engineering-or-business vocabulary vs. AI-Wiki-native design (§6a):** is this something any company or wiki in the relevant space would use, ideally traceable to a real standard (schema.org, PROV, SKOS, FIBO)? If yes, it's `swe:`/`biz:`. If it's genuinely new AI-domain vocabulary this wiki's subject matter needs (a foundation model, a benchmark, a reified benchmark score, a license model) and no upstream/inherited term fits, it's `aiw:` — but only after rungs 1–2 of the admission ladder (§1) are exhausted.
- [ ] **The portability test for `aiw:` (§6b):** delete this wiki's own subject matter (AI tools/models/benchmarks) from the graph — does the class still make complete sense to an unrelated company/wiki, unchanged? If yes, it belongs in `swe:`/`biz:`, no matter how central it is to this wiki. If no — the class's *definition itself* is inseparable from tracking AI models/benchmarks as this wiki's specific subject — it's `aiw:`. VCR-0003 cleared four classes this way: `FoundationModel`, `Benchmark`, `BenchmarkResult`, `LicenseModel`.

**Illustrative lesson (from the source project's VCR 0011):** `TravelVertical`/`AgencyModality`/`IntegrationModel` were minted in that project's `travel:` module on "relates to travel" alone, without the external-standard check — corrected to `biz:` once actually tested. The AI-Wiki analog to watch for: don't reach for `aiw:` just because a concept is "about AI" — check `swe:`/`biz:` first (e.g. a hosting platform or an API a model is served over is still `swe:`, not `aiw:`, even though the whole page is about a model).

- [ ] **For an enum choosing between `biz:` and `swe:`: is the distinction technical/architectural, or commercial/business-relationship?** Packaging, integration protocol, deployment topology → `swe:` (e.g. `swe:DeploymentModel`, `swe:IntegrationModel`, both inherited). Distribution arrangement, ownership structure, licensing/commercial terms → `biz:`. Don't assume every "how a product is configured" enum belongs in the same module just because the enums look structurally similar (2-3 members each). Note that `aiw:LicenseModel` (open-source/open-weights/closed-source) was deliberately kept in the native `aiw:` module rather than `biz:`, because it is genuinely this wiki's own subject-matter classification of AI systems, not a generic cross-industry commercial-terms enum (see VCR-0003).
- [ ] **Check upstream (schema.org, PROV, SKOS) before minting anything native.** schema.org in particular already defines `SoftwareApplication`, `Organization`, `Person`, `Product`, `Rating`/`Review`-shaped types — a concept that skips rung 2 (§1 above) and goes straight to a native `aiw:` class is a bigger miss than a generic one, precisely because schema.org's software/product coverage is unusually deep.

---

## Step 4 — Enum class or `skos:Concept`? (Class only)

Governed by `vocabulary-policy.md` §6c.

- [ ] Does the source state a **closed, exhaustive set with a cardinality rule** ("every X is exactly one of A, B, or C")? → **OWL enum class** (`owl:oneOf`) in the module chosen at Step 3.
- [ ] Is it an **open-ended subject-matter tag** with no fixed membership (an industry, a topic, a `schema:knowsAbout` target)? → **`skos:Concept`**, per `system/authoring-guides/skos-concept.md`.

---

## Step 5 — Where does an enum-member *individual*'s IRI live?

Governed by `vocabulary-policy.md` §6a (read `muscle:` there as `aiw:` in this deployment — see Step 3's note). Only relevant once Step 4 says "OWL enum class."

- [ ] **Enum-member value** (one of the closed set from Step 4) → IRI in **the class's own module namespace** (`aiw:open-source` for `aiw:LicenseModel`, `swe:mobile-embedded` for `swe:DeploymentModel`). Test: would a second, unrelated instance of this value exist elsewhere in the data? If yes, module namespace.
- [ ] **Singular, one-of-a-kind thing belonging to this wiki** (a named page — a specific tool, model, benchmark, source — or, per Step 1, an instance of a *reused upstream class* like `org:Role` where this wiki just names its own roles ad hoc) → `aiw:<page-slug>`.

**Illustrative lesson (from the source project's VCR 0011):** `economy`/`business-cabin` (travel cabin-class enum members) defaulted to that project's instance namespace (`muscle:`) instead of the enum class's own module (`travel:`). Swept once caught, but it took a full review pass to catch it across ~15 other enum members. The AI-Wiki analog: an `aiw:LicenseModel` member (`open-source`) belongs in `aiw:` (the class's own module — which happens to coincide with the instance namespace here, unlike the source project), not accidentally typed as if it were a one-off page-slug individual.

---

## Step 6 — Is the name self-explanatory?

- [ ] Read the proposed label with zero context, as a stranger would. Does it say what it means, or could it mean five other things?
- [ ] A bare, common English noun with no qualifier (`Change`, `Channel`, `System`, `ProgramType`) is a warning sign — it's usually missing the domain qualifier that makes it actually mean something (`PrivilegedAction`, `SalesChannel`, reuse `SoftwareApplication` instead of minting `System`, `LoyaltyProgramType`).
- [ ] If the source itself never scopes the concept further (e.g. "a change" with no indication of *what* changes), that vagueness is real and inherited — don't paper over it with an equally vague native term; either find the missing scope in context or name the term for what it's actually gating/describing (e.g. `PrivilegedAction` names the 2FA-gating role, not "change" in the abstract).

**What went wrong in VCR 0011:** `change`, `channel`, `program-type`, `system` all shipped as bare, common-English-noun names that didn't tell a reader what they meant without reading the source. All four were caught and renamed on review, not before.

- [ ] **Check the `.md` prose, not just the `.ace` compound word, for a qualifier the harvest dropped.** The `.ace` line is often a compressed noun phrase; the fuller `.md` sentence nearby frequently contains a clarifying word the compound lost. Search it before naming.

**Second instance, same VCR:** `traffic-percentage`'s `.ace` line is just "An ab-test has a traffic-percentage," but the source `.md` says "define the **traffic percentage split** (e.g., 70% control, 30% trial)" — the word "split" is what makes the property unambiguous (it's not "% of traffic in general," it's the A/B split ratio), and it was dropped when the `.ace` compound was formed. Renamed to `hasTrafficSplitPercentage`.

---

## Step 7 — Every Individual states its parent class, explicitly, in the row itself

- [ ] Every Individual row/entry must show its type (`type: <Class>`) directly — never leave it to be inferred from the gloss text alone ("KPI tracked by...", "member of..."). A reader should never have to guess or cross-reference to find out what class an individual belongs to.
- [ ] This applies uniformly — if some individuals in a table show their type and others don't, that inconsistency is itself a defect, not just the untyped rows.

**What went wrong in VCR 0011:** several individuals (`cpp`, `customer-delivered-value`, `daily-saving`, `total-generated-value`, `redemption-rate` — all `fibo-fnd-utl-alx:KeyPerformanceIndicator`; several `skos:Concept`s; several `swe:ReportingModule`/`swe:DeploymentEnvironment` instances) had their type mentioned only loosely in prose, or not shown in the row at all, while others (`admin`, `custom-message`) did show it explicitly. Fixed by adding a mandatory `type` column to every Individual table, going forward, in every VCR.

---

## Before finishing

- [ ] Every Step above has an explicit checkbox result in the VCR's Terminology Reconciliation section — not just a final IRI with no reasoning trail.
- [ ] If any step's answer is genuinely ambiguous, say so explicitly in the VCR and flag it for the reviewer — do not silently pick the more convenient answer.
- [ ] Every IRI-shaped table column (`Proposed native IRI`, `IRI`) shows the *current* recommendation, not a superseded one — a reviewer scans that column alone for a fast pass. If research changed the answer, update the cell or move the row out of the table entirely (`vocabulary-policy.md` §9).
