#!/usr/bin/env python3
"""T12 / C5 — non-SHACL emitter. Production/inference rules are SYNTHESIZED from the
DRS into pseudo-SWRL (antecedent -> consequent, one atom per DRS condition — no canned
rules). Deontic obligations are honestly reported: SWRL infers facts, it cannot express
a duty. Caveats emitted per rule:
  - DRS negation compiles to 'not(...)' = negation-as-failure; SWRL/OWL is open-world,
    so execution needs SQWRL or a closed-world guard.
  - an existential variable that appears ONLY in the consequent cannot be created by
    SWRL (no value invention) — flagged; needs a designated individual or a SPARQL
    CONSTRUCT rule instead.
Usage: python3 drs2swrl.py <page.ace> [out.swrl]"""
import sys, os, importlib
ds = importlib.import_module("drs2shacl"); v3 = ds.v3
is_c, aval, conds_of = v3.is_c, v3.aval, v3.conds_of
flatten = v3.flatten

def _term(node, vmap):
    t = v3.arg_term(node)
    if t[0] in ("named","atom"): return v3.named_iri(t[1])
    if t[0] == "var":
        lemma = vmap.get(t[1])
        if lemma and v3.is_individual(lemma): return v3.noun_term(lemma)["onto"]["iri"]
        return "?" + t[1].lower()
    return str(t[1])

def _atoms(drs_node, vmap, neg=False):
    """DRS conditions → (negated?, atom-string) list; fills vmap var→lemma."""
    out=[]
    for c in flatten(conds_of(drs_node)):
        if is_c(c,"object"):
            v=aval(c[1][0]); lemma=aval(c[1][1]); vmap.setdefault(v,lemma)
            if not v3.is_individual(lemma):
                out.append((neg, f"{v3.class_iri(lemma)}(?{v.lower()})"))
        elif is_c(c,"predicate"):
            verb=aval(c[1][1])
            if verb=="be": continue
            args=[_term(x,vmap) for x in c[1][2:]]
            name = v3.pred_iri(verb) if len(args)==2 else verb   # >2 args: no binary property form
            out.append((neg, f"{name}({', '.join(args)})"))
        elif is_c(c,"-"):
            out+=_atoms(c[1][0],vmap,neg=True)
        elif is_c(c,"must"):
            out+=_atoms(c[1][0],vmap,neg=neg)
        elif is_c(c,"=>") and contains_neg(c[1][1]):
            # "belongs-to no segment" → nested ∀¬: =>(drs([B],[Segment(B)]), -(belongsTo(A,B)))
            # render as ONE composite NAF atom: not( Segment(?b) ^ belongsTo(?a,?b) )
            inner=[a for _,a in _atoms(c[1][0],vmap)]
            inner+=[a for _,a in _atoms(c[1][1],vmap)]     # '-' inside flips to neg, atoms still collected
            out.append((True,"( "+" ^ ".join(inner)+" )"))
    return out

def contains_neg(n): return v3.contains(n,"-")

def synth_swrl(impl):
    """'=>' DRS → (rule-text, caveats)."""
    ant,cons=impl[1][0],impl[1][1]
    vmap={}
    a_atoms=_atoms(ant,vmap)
    ant_vars={v for v in vmap}
    c_atoms=_atoms(cons,vmap)
    caveats=[]
    if any(n for n,_ in a_atoms):
        caveats.append("antecedent 'not' is negation-as-failure — open-world SWRL needs SQWRL/CWA guard")
    exist=[v for v in vmap if v not in ant_vars and any(f"?{v.lower()}" in atm for _,atm in c_atoms)]
    if exist:
        caveats.append(f"consequent-only variable(s) {['?'+v.lower() for v in exist]} — SWRL cannot invent "
                       f"individuals; needs a designated individual or SPARQL CONSTRUCT")
    if any(len(c[1])>4 for c in flatten(conds_of(cons))+flatten(conds_of(ant)) if is_c(c,"predicate")):
        caveats.append("ditransitive predicate — no binary property form; atom kept n-ary (pseudo-SWRL)")
    fmt=lambda atoms:" ^ ".join(("not "+a if n else a) for n,a in atoms)
    return f"{fmt(a_atoms)} -> {fmt(c_atoms)}", caveats

def main(ace_path, out_path):
    rules=[]; notes=[]
    for line in open(ace_path):
        s=line.strip()
        if not s or s.startswith("#"): continue
        drs=v3.run_ape(s)
        if not drs: continue
        impl=next((c for c in conds_of(v3.parse_drs(drs)) if is_c(c,"=>")),None)
        if not impl: continue
        kind=ds.classify_constraint(impl)
        if kind=="production":
            rule,caveats=synth_swrl(impl)
            rules.append((s,rule,caveats))
            notes.append((s,"SWRL synthesized"+(f" ({len(caveats)} caveat(s))" if caveats else "")))
        elif kind=="obligation":
            notes.append((s,"NO SWRL: deontic 'must' has no SWRL form (SWRL infers facts, it cannot express a duty). Needs a policy/deontic layer."))
        else:
            notes.append((s,f"{kind}: handled by SHACL (drs2shacl_prod) or the ontology module, not SWRL"))
    with open(out_path,"w") as f:
        f.write("# SWRL rules generated from "+os.path.basename(ace_path)+" by drs2swrl.py — build artifact\n")
        f.write("# Format: pseudo-SWRL (antecedent -> consequent). Real target: .swrl / SWRL-in-OWL.\n\n")
        for s,rule,caveats in rules:
            f.write(f"# from: {s}\n")
            for c in caveats: f.write(f"# CAVEAT: {c}\n")
            f.write(rule+"\n\n")
        if not rules: f.write("# (no SWRL-expressible rules on this page)\n")
    print(f"wrote {out_path} — {len(rules)} SWRL rule(s)")
    for s,d in notes: print(f"   {s[:52]:52} | {d}")

if __name__=="__main__":
    ace=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else ace.rsplit('.',1)[0]+".swrl"
    main(ace,out)
