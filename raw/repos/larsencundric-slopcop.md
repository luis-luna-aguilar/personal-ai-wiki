---
title: AI-hallucinated malicious packages on npm and PyPI · GitHub
type: source
source_type: repo
url: https://github.com/LarsenCundric/slopcop
fetched: 2026-04-22
---

# AI-hallucinated malicious packages on npm and PyPI · GitHub

**Stop installing malware hallucinated by your AI assistant.**

Large language models hallucinate package names. A lot. According to a [USENIX Security 2025 study](https://www.usenix.org/conference/usenixsecurity25), **19.7% of package recommendations across 576,000 code generation samples reference packages that do not exist** -- or didn't, until an attacker registered them.

This attack is called **slopsquatting**: adversaries monitor LLM outputs, identify repeatedly hallucinated package names, and register them on npm and PyPI with malicious payloads. The packages look plausible. They install cleanly. And they run arbitrary code via postinstall scripts before you ever open an editor.

`slopcop` is a command-line tool that intercepts this kill chain. It checks packages against a battery of signals *before* anything touches your system.

---

Requires Node.js 18+. No native dependencies -- runs on macOS, Linux, and Windows.

---

Inspect a package without installing it:

```
$ slopcop check react-utils-helper

  slopcop v1.2.0 -- slopsquat defense

  Package:       react-utils-helper
  Registry:      npm
  Published:     2 days ago
  Downloads:     14 (lifetime)
  Versions:      1.0.0 (single release)
  Postinstall:   YES -- runs "node scripts/setup.js"
  Repository:    none
  Similar to:    react-util-helpers (4.2M weekly downloads)
  Name distance: 1 (Levenshtein)

  Risk score:    92/100
  Verdict:       DANGEROUS

  This package exhibits strong slopsquat signals. Do NOT install.
```

```
$ slopcop check express

  slopcop v1.2.0 -- slopsquat defense

  Package:       express
  Registry:      npm
  Published:     11 years ago
  Downloads:     32,104,558 (weekly)
  Versions:      271 releases
  Postinstall:   no
  Repository:    https://github.com/expressjs/express
  Similar to:    -- (this IS the popular package)
  Name distance: n/a

  Risk score:    2/100
  Verdict:       SAFE
```

### Install a package (with guard)

Wraps `npm install` (or `pip install` with `--pypi`). Runs the full check first; aborts if the package is dangerous:

```
$ slopcop install flask-cognito-auth --pypi

  slopcop v1.2.0 -- slopsquat defense

  Package:       flask-cognito-auth
  Registry:      PyPI
  Published:     6 days ago
  Downloads:     38 (lifetime)
  Versions:      0.1.0 (single release)
  Repository:    none
  Similar to:    flask-cognito (89K monthly downloads)
  Name distance: 5 (Levenshtein)

  Risk score:    78/100
  Verdict:       SUSPICIOUS

  WARNING: This package has elevated slopsquat risk.
  Proceed with install? [y/N] n
  Aborted.
```

Scan every dependency in `package.json` or `requirements.txt`:

```
$ slopcop scan

  slopcop v1.2.0 -- scanning package.json (47 dependencies)

  [1/47]  express ......................... SAFE       (2/100)
  [2/47]  lodash .......................... SAFE       (1/100)
  [3/47]  react-auth-helpkit .............. DANGEROUS  (88/100)
  [4/47]  cors ............................ SAFE       (3/100)
  ...
  [47/47] jsonwebtoken .................... SAFE       (4/100)

  Summary:
    45 SAFE
     1 SUSPICIOUS
     1 DANGEROUS  <-- react-auth-helpkit

  Run `slopcop check react-auth-helpkit` for details.
```

---

| Flag | Description |
| --- | --- |
| `--npm` | Check against the npm registry (default) |
| `--pypi` | Check against the Python Package Index |
| `--json` | Output results as JSON |
| `--strict` | Exit with code 1 on SUSPICIOUS or DANGEROUS |
| `--no-color` | Disable colored output |

---

`slopcop` evaluates packages across multiple dimensions without ever executing package code:

1. **Name pattern analysis** -- Flags names that look AI-generated: overly descriptive compounds (`react-utils-helper-toolkit`), implausible word combinations, and names that read like a prompt completion rather than a deliberate choice.
2. **Registry metadata** -- Queries the npm or PyPI registry API for:

   * **Account age** -- How old is the publisher's account?
   * **Package age** -- When was the first version published?
   * **Download count** -- Legitimate packages accumulate downloads over time.
   * **Version count** -- A single-version package published last week is suspicious.
   * **Postinstall scripts** -- The primary vector for slopsquat payloads. Any `preinstall`, `install`, or `postinstall` hook is flagged and inspected.
   * **Repository link** -- Missing or broken repo URLs correlate with malicious packages.
3. **Similarity matching** -- Compares the package name against the top 10,000 packages on each registry using Levenshtein distance, Jaro-Winkler similarity, and keyboard-distance heuristics. A name that is one typo away from a popular package is a strong slopsquat signal.
4. **Risk scoring** -- All signals are weighted and combined into a score from 0 to 100:

| Score | Verdict | Meaning |
| --- | --- | --- |
| 0-30 | **SAFE** | Package appears legitimate |
| 31-65 | **SUSPICIOUS** | Elevated risk; review before installing |
| 66-100 | **DANGEROUS** | Strong slopsquat indicators; do not install |

---

Every `npm install` and `pip install` is a trust decision. LLM-assisted coding has introduced a new attack surface: developers trust AI suggestions implicitly, and attackers exploit that trust at scale.

The USENIX 2025 paper ("SloppySquat: Analyzing the Threat of LLM-Hallucinated Packages") found:

* **19.7%** of LLM-generated package names are hallucinated (do not exist on the registry)
* **58%** of hallucinated names are repeated across multiple prompts, making them predictable targets
* Packages registered under hallucinated names received **real installs within days**

`slopcop` is a lightweight guardrail. It does not replace dependency auditing, lockfiles, or SCA tools -- it catches the class of threat those tools were not designed for.

---

| Platform | Status |
| --- | --- |
| macOS (arm64, x64) | Supported |
| Linux (x64, arm64) | Supported |
| Windows (x64) | Supported |

Pure Node.js with zero native dependencies. If `node` runs, `slopcop` runs.

---

Issues and pull requests are welcome. See [CONTRIBUTING.md](/LarsenCundric/slopcop/blob/main/CONTRIBUTING.md) for guidelines.

---

SlopCop is a risk-assessment tool that uses heuristics and public registry data to flag potentially suspicious packages. It is **not a guarantee of safety**. A clean result does not mean a package is safe, and a flagged result does not necessarily mean a package is malicious. Always review packages before installing them in production environments. The authors are not responsible for any damages, data loss, or security incidents resulting from the use of this tool or the installation of packages it evaluates.

---

[MIT](/LarsenCundric/slopcop/blob/main/LICENSE) -- Copyright 2026 Larsen Cundric
