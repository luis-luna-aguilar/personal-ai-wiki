---
title: GitHub - maziyarpanahi/openmed: Local-first healthcare AI: clinical NER and HIPAA PII de-identification on hardware you control. 2,200+ medical models, 35 model-backed PII languages, and Python, MLX, Android and browser runtimes. Apache-2.0 SDK. · GitHub
type: source
source_type: repo
url: https://github.com/maziyarpanahi/openmed
fetched: 2026-10-19
---

# GitHub - maziyarpanahi/openmed: Local-first healthcare AI: clinical NER and HIPAA PII de-identification on hardware you control. 2,200+ medical models, 35 model-backed PII languages, and Python, MLX, Android and browser runtimes. Apache-2.0 SDK. · GitHub

---

This iPhone example uses OpenMed's local runtime after the required model artifacts are available:

[![OpenMed Scan on iPhone · on-device PII de-identification and clinical extraction via OpenMedKit](/maziyarpanahi/openmed/raw/master/docs/brand/openmed-ios-scan.png)](/maziyarpanahi/openmed/blob/master/docs/brand/openmed-ios-scan.png)
**On iPhone via [OpenMedKit](/maziyarpanahi/openmed/blob/master/swift/OpenMedKit)**: scan a clinical note, de-identify it, and extract clinical signals with Apple MLX processing locally in this configuration.

  

[![OpenMed redacting PII from a clinical discharge document in real time](/maziyarpanahi/openmed/raw/master/docs/brand/openmed-pii-demo.gif)](/maziyarpanahi/openmed/blob/master/docs/brand/openmed-pii-demo.gif)

[![OpenMed redacting PII from a clinical discharge document in real time](https://github.com/maziyarpanahi/openmed/raw/master/docs/brand/openmed-pii-demo.gif)](https://github.com/maziyarpanahi/openmed/blob/master/docs/brand/openmed-pii-demo.gif)

**Real-time PII de-identification**: in this configured local workflow, the Nemotron Privacy Filter redacts names, addresses, IDs, and billing data from a synthetic clinical discharge packet. *(All values shown are synthetic.)*

---

```
from openmed import analyze_text

result = analyze_text(
    "Patient started on imatinib for chronic myeloid leukemia.",
    model_name="disease_detection_superclinical",
)

for entity in result.entities:
    print(f"{entity.label:<12} {entity.text:<28} {entity.confidence:.2f}")
# DISEASE      chronic myeloid leukemia     0.98
# DRUG         imatinib                     0.95
```

A clinical NER model using the local runtime after its required artifacts are available.

---

## Clinical brief in 30 seconds

From a source checkout, run the CPU-only synthetic contract demonstration:

```
python examples/v30_clinical_brief.py
# Optional: --model mlx, with the pinned model already cached on Apple silicon.
```

It de-identifies an embedded note, extracts and grounds a finding, then prints
a cited brief, verdicts and a value-free review packet. **NER/NLI providers are
explicit synthetic test doubles, not trained-model or clinical validation.**
No external note input is accepted. The MLX option may refuse unsupported output;
it never bypasses the guards. See the [brief guide](/maziyarpanahi/openmed/blob/master/docs/clinical/clinical-brief.md)
and [demo script](/maziyarpanahi/openmed/blob/master/docs/demo/clinical-brief.md) for the boundaries and local setup.

---

Start with the [consumer agent-usage guide](/maziyarpanahi/openmed/blob/master/docs/agent-usage.md), or load the
curated [llms.txt](https://openmed.life/docs/llms.txt) documentation index.
For callable local interfaces, use the [MCP server](/maziyarpanahi/openmed/blob/master/docs/mcp-clients.md), the
typed [tool registry](/maziyarpanahi/openmed/blob/master/openmed/mcp/tool_registry.py), or the
[command-line interface](/maziyarpanahi/openmed/blob/master/docs/agent-usage.md#command-line-interface). Ready-made
cross-tool procedures live in the [repository skills catalog](/maziyarpanahi/openmed/blob/master/skills/README.md).

---

| Deployment consideration | OpenMed SDK boundary |
| --- | --- |
| Core runtime | Processes locally after required artifacts are available |
| Optional network paths | Downloads, remote adapters, telemetry-enabled paths, and user integrations may use a network |
| Validation | Deployment owners validate model and dataset terms, privacy behavior, and clinical fitness |
| Interfaces | Python, Swift, Android, browser, and service surfaces where supported |

* **Curated model catalog**: validate each model, license, and dataset for your use case.
* **Safe Harbor-aligned configuration**: can target the 18 identifier categories; expert deployment review remains required, and use of the SDK does not itself establish HIPAA compliance.
* **Supported execution paths**: CPU, CUDA, MLX, mobile, service, and browser adapters vary by environment and artifact.
* **Deployment interfaces**: Python, containers, services, and batch workflows require configuration and validation.
* **SDK source**: released under the Apache-2.0 License; model and dataset terms vary.

---

## On-device on Apple: Swift, MLX & iOS

On supported Apple hardware, OpenMed can use **MLX** and **[OpenMedKit](/maziyarpanahi/openmed/blob/master/swift/OpenMedKit)** for local processing after required artifacts are available. Model acquisition and any user-configured remote integrations remain separate network boundaries.

```
// Add OpenMedKit to your app
dependencies: [
    .package(url: "https://github.com/maziyarpanahi/openmed.git", from: "3.0.0"),
]
```

Expected result: Swift Package Manager resolves OpenMedKit and makes
`import OpenMedKit` available to your app target.

* **MLX runtime** for PII token classification, the Privacy Filter family, experimental GLiNER-family zero-shot tasks, and Python MLX-LM text generation with Laneformer; includes a CoreML fallback path for supported token-classification artifacts.
* **Portable model naming where supported**: an MLX model name can fall back to a matching PyTorch checkpoint when that mapping and artifact are available on non-Apple hardware.
* **Python on Apple Silicon** too: `pip install --upgrade "openmed[mlx]"`.

Guides: [MLX backend](/maziyarpanahi/openmed/blob/master/docs/mlx-backend.md) · [OpenMedKit (Swift)](/maziyarpanahi/openmed/blob/master/docs/swift-openmedkit.md) · [CoreML export](/maziyarpanahi/openmed/blob/master/docs/coreml-export.md)

[![MLX vs CPU latency on Apple Silicon: 24 to 33 times faster](/maziyarpanahi/openmed/raw/master/docs/brand/openmed-mlx-speedup.png)](/maziyarpanahi/openmed/blob/master/docs/brand/openmed-mlx-speedup.png)
**MLX on Apple Silicon: 24–33× faster than CPU PyTorch** for the Privacy Filter: median latency per inference step, lower is better.

---

## On-device on Android — Kotlin & ONNX Runtime Mobile

OpenMedKit also ships as a native Android/Kotlin library for local document
intake, OCR handoff, PII redaction, and token-classification inference through
**ONNX Runtime Mobile**. Mobile model repositories include stable tensor names,
dynamic sequence axes, tokenizer files, labels, and Android-ready fp32, fp16,
INT8, and optional `.ort` outputs.

Add the scoped JitPack repository in `settings.gradle.kts`:

```
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        maven {
            url = uri("https://jitpack.io")
            content { includeGroup("com.github.maziyarpanahi") }
        }
    }
}
```

Then use the immutable OpenMed `v3.0.0` release:

```
dependencies {
    implementation("com.github.maziyarpanahi:openmed:v3.0.0")
}
```

See the [Android installation guide](/maziyarpanahi/openmed/blob/master/android/README.md) for local builds and
publishing details.

```
val model = OpenMedKit.fromDirectory(modelDir)
val entities = model.analyzeText("Patient Alice Nguyen was seen in cardiology.")
```

* **Android ONNX profile** emits `model.onnx`, `model_fp16.onnx`,
  `model_int8.onnx`, tokenizer assets, labels, and `openmed-onnx.json`.
* **ORT Mobile support** records the minimal-build operator configuration when
  ONNX Runtime conversion tooling is installed.
* **Kotlin parity tests** keep tokenizer offsets, span boundaries, and decoder
  output aligned with the Python runtime.

Guides: [Android ONNX export](/maziyarpanahi/openmed/blob/master/docs/export-onnx-android.md) ·
[Android span parity](/maziyarpanahi/openmed/blob/master/docs/android-parity.md) ·
[OpenMedKit Android](/maziyarpanahi/openmed/blob/master/android/openmedkit)

### The same ONNX model on Python CPU

```
from openmed import OnnxModel

model = OnnxModel.from_pretrained(
    "OpenMed/OpenMed-PII-ClinicalE5-Small-33M-v1-onnx-android"
)
entities = model("Patient Alice Nguyen was seen in cardiology.")
```

### The same ONNX model in the browser

```
npm install openmed @huggingface/transformers
```

```
import { loadOnnxModel } from "openmed";

const model = await loadOnnxModel(
  "OpenMed/OpenMed-PII-ClinicalE5-Small-33M-v1-onnx-android",
);
const entities = await model("Patient Alice Nguyen was seen in cardiology.");
```

---

Loading

```
flowchart LR
    A["Clinical text"] --> B["OpenMed<br/>(local-first)"]
    B --> C["Medical entities"]
    B --> D["PII detected"]
    B --> E["De-identified text"]
    style B fill:#0D6E6E,stroke:#0A5656,stroke-width:2px,color:#ffffff
    style C fill:#D6EBEB,stroke:#0D6E6E,color:#0E1116
    style D fill:#F7DCD8,stroke:#C5453A,color:#0E1116
    style E fill:#F5E27A,stroke:#A9A088,color:#0E1116
```

Rendered result: a local clinical-text pipeline that returns medical entities,
PII findings, and de-identified text without sending data to a cloud API.

---

## Agent Skills — build with OpenMed from your coding agent

The [`skills/`](/maziyarpanahi/openmed/blob/master/skills) catalog ships portable [Agent Skills](https://agentskills.io) for on-device de-identification, clinical NER, FHIR export, evaluation, and the healthcare workflows around them. The same `SKILL.md` folders work in **Claude Code**, **OpenAI Codex**, **OpenCode**, and compatible agents; the installer uses each client's skills directory plus the cross-client `~/.agents/skills` convention.

```
git clone https://github.com/maziyarpanahi/openmed && cd openmed
./install-skills.sh          # installs for Claude Code, Codex, OpenCode, and ~/.agents/skills
```

Then ask your agent for the pipeline using synthetic placeholders:

> Build a local OpenMed pipeline that de-identifies a synthetic discharge note and extracts medication entities.

It loads the right skills and produces an on-device pipeline (`openmed.deidentify(...)` → `openmed.analyze_text(...)`). After the one-time model download, run that pipeline locally on real notes; do not paste real PHI into a cloud-hosted agent prompt. See the **[skills catalog and 30-second example](/maziyarpanahi/openmed/blob/master/skills/README.md)**.

---

```
# Core + Hugging Face runtime (Linux, macOS, Windows; CPU or CUDA)
pip install --upgrade "openmed[hf]"

# Add the REST service
pip install --upgrade "openmed[hf,service]"

# Apple Silicon acceleration (MLX)
pip install --upgrade "openmed[mlx]"
```

Expected result:

```
Successfully installed openmed-...
```

|  |  |  |
| --- | --- | --- |
| **Python API**  ``` from openmed import analyze_text  result = analyze_text(   "Patient received 75mg "   "clopidogrel for NSTEMI.",   model_name=   "pharma_detection_superclinical", ) print([(e.label, e.text) for e in result.entities]) ```  Example output:  ``` [('DRUG', 'clopidogrel'), ('CONDITION', 'NSTEMI')] ``` | **REST service**  ``` python -m openmed.service.logging \   --host 0.0.0.0 --port 8080 ```  Example output:  ``` INFO:     Uvicorn running on http://0.0.0.0:8080 GET /health -> 200 OK ```  `GET /health` `POST /analyze` `POST /pii/extract` `POST /pii/deidentify` | **Batch**  ``` from openmed import BatchProcessor  p = BatchProcessor(   model_name=   "disease_detection_superclinical",   group_entities=True, ) results = p.process_texts([...]) print(len(results), sum(len(r.entities) for r in results)) print([(e.label, e.text) for e in results[0].entities[:1]]) ```  Example output:  ``` 3 7 [('DISEASE', 'leukemia')] ``` |

**Browser / WebGPU**

Package ONNX token-classification exports for in-browser inference through
Transformers.js:

```
python -m openmed.onnx.convert \
  --model dslim/bert-base-NER \
  --output dist/example-onnx \
  --include-transformersjs
```

Example output:

```
Exported Transformers.js bundle to dist/example-onnx
```

```
import { pipeline } from "@huggingface/transformers";

const detector = await pipeline(
  "token-classification",
  "/models/openmed-pii/transformersjs",
  { device: "webgpu" },
);
const entities = await detector("Patient Casey Example called 212-555-0198.");
console.log(entities.slice(0, 2));
```

Example output:

```
[
  { entity: "NAME", word: "Casey Example", score: 0.99 },
  { entity: "PHONE", word: "212-555-0198", score: 0.98 },
]
```

[Transformers.js export guide](/maziyarpanahi/openmed/blob/master/docs/export-transformersjs.md)

**Offline / air-gapped?** Point `model_name` (or `model_id`) at a local directory and OpenMed loads it without contacting the Hugging Face Hub:

```
from openmed import OpenMedConfig, analyze_text

result = analyze_text(
    "Patient presents with chronic myeloid leukemia and Type 2 diabetes.",
    model_id="./models/OpenMed-NER-DiseaseDetect-SuperClinical-434M",
    config=OpenMedConfig(device="cpu"),
)
for entity in result.entities:
    print(f"{entity.label:<12} {entity.text:<28} {entity.confidence:.2f}")
```

Example output:

```
DISEASE      chronic myeloid leukemia     0.98
DISEASE      Type 2 diabetes              0.96
```

Because `model_id` points to a local directory, this example does not contact
the Hugging Face Hub or any external model provider.

---

A curated registry of specialized medical NER models; browse the [full catalog](https://openmed.life/docs/model-registry).

| Model | Specialization | Entity types | Size |
| --- | --- | --- | --- |
| `disease_detection_superclinical` | Disease & conditions | DISEASE, CONDITION, DIAGNOSIS | 434M |
| `pharma_detection_superclinical` | Drugs & medications | DRUG, MEDICATION, TREATMENT | 434M |
| `pii_superclinical_large` | PII & de-identification | NAME, DATE, SSN, PHONE, EMAIL, ADDRESS | 434M |
| `anatomy_detection_electramed` | Anatomy & body parts | ANATOMY, ORGAN, BODY\_PART | 109M |
| `gene_detection_genecorpus` | Genes & proteins | GENE, PROTEIN | 109M |

---

## Privacy: PII detection & de-identification

```
from openmed import extract_pii, deidentify

text = "Patient: John Doe, DOB: 01/15/1970, SSN: 123-45-6789"

# Extract PII with smart merging (prevents tokenization fragmentation)
result = extract_pii(text, model_name="pii_superclinical_large", use_smart_merging=True)
print([(e.label, e.text) for e in result.entities])

# De-identify with the method you need
print(deidentify(text, method="mask").deidentified_text)
print(deidentify(text, method="replace").deidentified_text)
print(deidentify(text, method="hash").deidentified_text)
print(deidentify(text, method="shift_dates", date_shift_days=180).deidentified_text)
```

Example output:

```
[('NAME', 'John Doe'), ('DATE', '01/15/1970'), ('SSN', '123-45-6789')]
Patient: [NAME], DOB: [DATE], SSN: [SSN]
Patient: Emily Chen, DOB: 03/22/1985, SSN: 456-78-9012
Patient: 6b8f...c4a1, DOB: 48b1...91de, SSN: 3f13...e912
Patient: John Doe, DOB: 07/14/1970, SSN: 123-45-6789
```

* **Smart entity merging** keeps `01/15/1970` whole instead of fragmenting it.
* **Policy-aware pipelines** add HIPAA/GDPR/research profiles, calibrated thresholds, signed audit reports, redaction previews, and minimum-necessary action selection.
* **Faker-backed obfuscation** with custom clinical-ID providers (CPF, CNPJ, BSN, NIR, Codice Fiscale, NIE, Aadhaar, Steuer-ID, NPI).
* **HIPAA boundary**: Safe Harbor-aligned categories and configurable thresholds are implementation aids; expert deployment review remains required, and SDK use alone does not establish compliance.
* **Batch and streaming PII**: extract or de-identify across many documents with `BatchProcessor(operation="extract_pii" | "deidentify", batch_size=16)` or incremental streaming helpers.

[![Batch PII processing throughput: up to 3.3x on CPU and 2.2x on MLX](/maziyarpanahi/openmed/raw/master/docs/assets/pii-batch-benchmark.png)](/maziyarpanahi/openmed/blob/master/docs/assets/pii-batch-benchmark.png)
**Batch processing**: up to **3.3×** higher throughput on CPU and **2.2×** on MLX vs. one document at a time.

[Complete PII notebook](/maziyarpanahi/openmed/blob/master/examples/notebooks/PII_Detection_Complete_Guide.ipynb) · [Smart merging](/maziyarpanahi/openmed/blob/master/docs/pii-smart-merging.md) · [Anonymization quickstart](/maziyarpanahi/openmed/blob/master/docs/anonymization.md#quickstart-choosing-a-method)

**Privacy Filter family**: three model families on the OpenAI Privacy Filter architecture
  

Same model code (gpt-oss-style sparse-MoE transformer with local attention, sink tokens, RoPE+YaRN, tiktoken `o200k_base`), different training data. All route through the **same** `extract_pii()` / `deidentify()` API; only `model_name=` changes.
`openai/privacy-filter` is a Hugging Face model identifier for local weights;
using it here does not call the OpenAI API.

```
from openmed import extract_pii

text = "Patient Sarah Connor (DOB: 03/15/1985) at MRN 4471882."

variants = {
    "baseline": extract_pii(text, model_name="openai/privacy-filter"),
    "nemotron": extract_pii(text, model_name="OpenMed/privacy-filter-nemotron"),
    "mlx": extract_pii(text, model_name="OpenMed/privacy-filter-mlx"),
}
print([(e.label, e.text) for e in variants["baseline"].entities])
```

Example output:

```
[('NAME', 'Sarah Connor'), ('DATE', '03/15/1985'), ('ID', '4471882')]
```

On non-Apple-Silicon hosts, MLX model names are automatically substituted with the matching PyTorch checkpoint (with a one-time warning): reuse one model name where a matching backend artifact is available. See [Privacy Filter architecture & backend routing](/maziyarpanahi/openmed/blob/master/docs/anonymization.md#privacy-filter-family).

---

## Multilingual PII (42 supported routes; 35 model-backed)

Extraction and de-identification support **42 supported PII language codes**:
`am`, `ar`, `as`, `bn`, `cs`, `da`, `de`, `el`, `en`, `es`, `fa`, `fr`, `gu`, `he`, `hi`, `id`,
`it`, `ja`, `kn`, `ko`, `ml`, `mr`, `nl`, `no`, `or`, `pa`, `pl`, `pt`, `ro`, `ru`, `sv`, `sw`, `ta`,
`te`, `th`, `tr`, `uk`, `ur`, `vi`, `xh`, `zh`, and `zu`, with **the registry-backed PII model catalog** in total.
Russian routing currently uses a documented multilingual default-model
placeholder. Bengali, Chinese, and Tamil have dedicated registry entries.
An optional, user-configured Indic NER family can serve Assamese, Bengali,
Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, and
Telugu. Set `OPENMED_INDIC_NER_MODEL`; OpenMed never
bundles or automatically selects those optional weights.
OpenMed also includes validator-backed national-ID coverage for additional
ID-only locales such as Latvian, Slovak, Malay, Filipino, and Finnish.

See the [per-language guide](/maziyarpanahi/openmed/blob/master/docs/languages.md) for each code's default PII
model, Faker locale, and a before/after de-identification example.

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```

Example output:

```
[('NAME', 'Pedro Almeida'), ('ID', '123.456.789-09'), ('EMAIL', 'pedro@hospital.pt')]
```

Show per-language examples (Portuguese, Dutch, Hindi, Arabic, Japanese, Turkish)
  

```
from openmed import extract_pii

portuguese = extract_pii("Paciente: Pedro Almeida, CPF: 123.456.789-09, telefone: +351 912 345 678", lang="pt", use_smart_merging=True)
dutch      = extract_pii("Patiënt: Eva de Vries, BSN: 123456782, telefoon: +31 6 12345678", lang="nl", use_smart_merging=True)
hindi      = extract_pii("रोगी: अनीता शर्मा, फोन: +91 9876543210, पता: नई दिल्ली 110001", lang="hi", use_smart_merging=True)
arabic     = extract_pii("المريضة ليلى حسن، الهاتف +20 10 1234 5678، الرقم القومي 29801011234567.", lang="ar", use_smart_merging=True)
japanese   = extract_pii("患者 佐藤 花子、電話 +81 90 1234 5678、マイナンバー 1234 5678 9012.", lang="ja", use_smart_merging=True)
turkish    = extract_pii("Hasta Ayşe Yılmaz, telefon +90 532 123 45 67, TCKN 10000000146.", lang="tr", use_smart_merging=True)

for r in (portuguese, dutch, hindi, arabic, japanese, turkish):
    print([(e.label, e.text) for e in r.entities])
```

Example output:

```
[('NAME', 'Pedro Almeida'), ('ID', '123.456.789-09'), ('PHONE', '+351 912 345 678')]
[('NAME', 'Eva de Vries'), ('ID', '123456782'), ('PHONE', '+31 6 12345678')]
[('NAME', 'अनीता शर्मा'), ('PHONE', '+91 9876543210'), ('ADDRESS', 'नई दिल्ली 110001')]
[('NAME', 'ليلى حسن'), ('PHONE', '+20 10 1234 5678'), ('ID', '29801011234567')]
[('NAME', '佐藤 花子'), ('PHONE', '+81 90 1234 5678'), ('ID', '1234 5678 9012')]
[('NAME', 'Ayşe Yılmaz'), ('PHONE', '+90 532 123 45 67'), ('ID', '10000000146')]
```

---

A Docker-friendly FastAPI service with request validation, shared pipeline preload, and unified error envelopes.

```
pip install --upgrade "openmed[hf,service]"
python -m openmed.service.logging --host 0.0.0.0 --port 8080

# or with Docker
docker build -t openmed:local .
docker run --rm -p 8080:8080 -e OPENMED_PROFILE=prod openmed:local
```

Example output:

```
INFO:     Uvicorn running on http://0.0.0.0:8080
```

```
curl -X POST http://127.0.0.1:8080/pii/extract \
  -H "Content-Type: application/json" \
  -d '{"text":"Paciente: Maria Garcia, DNI: 12345678Z","lang":"es"}'
```

Abbreviated example response:

```
{
  "text": "Paciente: Maria Garcia, DNI: 12345678Z",
  "entities": [
    {"text": "Maria Garcia", "label": "NAME", "confidence": 0.99, "start": 10, "end": 22},
    {"text": "12345678Z", "label": "ID", "confidence": 0.98, "start": 29, "end": 38}
  ],
  "model_name": "OpenMed/privacy-filter-multilingual"
}
```

**Model lifecycle and service controls:** free memory on demand with
`GET /models/loaded`, `POST /models/unload`, and a `keep_alive` idle window;
v1.8 also includes API-key/JWT auth, no-PHI request logging, tracing, gRPC,
async jobs, webhooks, warm pools, dynamic batching, request coalescing, rate
and concurrency limits, `/livez`, `/readyz`, and opt-in metrics:

```
OPENMED_SERVICE_KEEP_ALIVE=10m python -m openmed.service.logging --host 0.0.0.0 --port 8080
curl -X POST http://127.0.0.1:8080/models/unload -H "Content-Type: application/json" -d '{"all":true}'
```

Example response:

```
{
  "unloaded": true,
  "released": {"models": 1, "tokenizers": 1, "pipelines": 1},
  "active_models": {}
}
```

See the full [REST service guide](/maziyarpanahi/openmed/blob/master/docs/rest-service.md).

---

Full guides at **[openmed.life/docs](https://openmed.life/docs/)**.

AI agents can load the curated [llms.txt](https://openmed.life/docs/llms.txt)
index or the inlined [llms-full.txt](https://openmed.life/docs/llms-full.txt)
feed. Both are regenerated from the current documentation during every strict
MkDocs build.

---

[![OpenMed mascot](/maziyarpanahi/openmed/raw/master/docs/brand/openmed-mascot-icon.png)](/maziyarpanahi/openmed/blob/master/docs/brand/openmed-mascot-icon.png)

OpenMed's guardian is a fluffy Persian cat styled as a tiny **Avicenna (Ibn Sina)**: the great Persian
physician whose *Canon of Medicine* was the world's standard medical text for some 600 years. He keeps
watch over the open book of medical knowledge, in a palette built around Persian turquoise (*fīrūza*):
a local-first guardian for your most private data.

  

---

Contributions welcome: bug reports, feature requests, and PRs alike. Please read the [Contributing guide](/maziyarpanahi/openmed/blob/master/CONTRIBUTING.md) and our [Code of Conduct](/maziyarpanahi/openmed/blob/master/CODE_OF_CONDUCT.md) first.

---

Found a vulnerability? OpenMed redacts PHI, so a **redaction bypass or PHI/PII
leak is a security issue**: please report it **privately**, never as a public
issue. See **[SECURITY.md](/maziyarpanahi/openmed/blob/master/SECURITY.md)** for the responsible-disclosure policy
and the [private reporting form](https://github.com/maziyarpanahi/openmed/security/advisories/new).
Never include real patient data in a report.

---

OpenMed builds on excellent open-source work: particular thanks to **OpenAI** (the [Privacy Filter](https://huggingface.co/openai/privacy-filter) architecture), **NVIDIA** (the [Nemotron PII dataset](https://huggingface.co/datasets/nvidia/Nemotron-PII-v1)), **Hugging Face** (`transformers`, Transformers.js & the model ecosystem), **Apple** ([MLX](https://github.com/ml-explore/mlx)), and the **[Faker](https://faker.readthedocs.io/)** maintainers.

The OpenMed SDK source is released under the [Apache-2.0 License](/maziyarpanahi/openmed/blob/master/LICENSE). Third-party asset notices are recorded in [NOTICE](/maziyarpanahi/openmed/blob/master/NOTICE).

```
@misc{panahi2025openmedneropensourcedomainadapted,
      title={OpenMed NER: Open-Source, Domain-Adapted State-of-the-Art Transformers for Biomedical NER Across 12 Public Datasets},
      author={Maziyar Panahi},
      year={2025},
      eprint={2508.01630},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.01630},
}
```

Expected result: BibTeX-compatible citation metadata for referencing OpenMed in
papers, posters, and derived documentation.

---

If OpenMed is useful to you, a star helps others discover it.

[5,400+ GitHub stars · 9 Oct 2026 snapshot](https://github.com/maziyarpanahi/openmed/stargazers)

---
