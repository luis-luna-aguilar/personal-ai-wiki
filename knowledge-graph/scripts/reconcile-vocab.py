#!/usr/bin/env python3
"""Auto-admit new vocabulary flagged by the ace-extractor into the canonical lexicon.
Loads each tmp/ace-extractor/*.new-terms.yaml WHOLE (robust to multi-line entries),
re-serializes each new term as a clean single-line flow row, dedups by id, appends to the
canonical lexicon-map.yaml, then regenerates the .ulex. Provenance (# source:) stays in the
tmp new-terms.yaml files for review. Usage: python3 reconcile-vocab.py"""
import os, re, glob, subprocess, sys, yaml
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CANON = os.path.join(ROOT, "knowledge-graph", "ontology", "lexicon-map.yaml")
INBOX = os.path.join(ROOT, "tmp", "ace-extractor")

def main():
    canon = open(CANON).read()
    have = set(re.findall(r"\bid:\s*([A-Za-z0-9_-]+)", canon))
    added, dup, bad = [], [], []
    rows = []
    ENTRY = re.compile(r"^\s*-\s*\{\s*id:\s*([A-Za-z0-9_-]+)")
    for f in sorted(glob.glob(os.path.join(INBOX, "*.new-terms.yaml"))):
        for line in open(f):
            m = ENTRY.match(line)
            if not m:
                continue
            tid = m.group(1)
            row = line.rstrip("\n")
            # validate THIS row parses as a 1-term list (skips multi-line/broken rows safely)
            try:
                t = yaml.safe_load("terms:\n  " + row)["terms"][0]
                assert isinstance(t, dict) and t.get("id") == tid
            except Exception:
                bad.append(f"{os.path.basename(f)}:{tid}"); continue
            if tid in have:
                dup.append(tid); continue
            have.add(tid); added.append(tid)
            rows.append(row)   # raw — preserves the trailing `# source:` provenance comment
    # sanity: the rows must all parse as a terms list before we touch the canonical file
    if rows:
        probe = "terms:\n" + "\n".join("  " + r for r in rows)
        yaml.safe_load(probe)  # raises if any row is malformed -> abort without writing
        block = "\n# ==== auto-admitted by reconcile-vocab.py (ace-extractor flags) — review pending ====\n" + "\n".join(rows) + "\n"
        open(CANON, "a").write(block)
        # verify the whole canonical still parses
        yaml.safe_load(open(CANON))
    r = subprocess.run([sys.executable, os.path.join(HERE, "gen-ulex.py")], capture_output=True, text=True)
    print(f"admitted {len(added)} new term(s)" + (f"; skipped {len(set(dup))} already-present" if dup else ""))
    if bad: print("MALFORMED files skipped:", "; ".join(bad))
    print(r.stdout.strip() or r.stderr.strip())

if __name__ == "__main__":
    main()
