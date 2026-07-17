#!/usr/bin/env python3
"""T10 / C4 — production DRS→SHACL. Reads a .ace file; emits SHACL for cardinality / enumeration /
conditional constraints AND Rule-10 datatype shapes — money values REIFIED as schema:MonetaryAmount
(amount + currency), not bare decimals. Usage: python3 drs2shacl_prod.py <page.ace> [out.shapes.ttl]"""
import sys, os, importlib
ds = importlib.import_module("drs2shacl")   # reuse synth_cardinality / synth_conditional / classify_constraint
v3 = ds.v3
ds.v3.gen_ulex()
is_c, aval, conds_of, BY_ID = v3.is_c, v3.aval, v3.conds_of, v3.BY_ID

PREFIXES = v3.PREFIXES   # full canonical table — shape domains span org:/prov:/dct: etc.

def datatype_shapes(conds):
    """'X has a <datatype-noun>' → a SHACL property shape on the property's domain.
       unit==money → reified schema:MonetaryAmount (value+currency); else plain sh:datatype."""
    out=[]; vc={aval(c[1][0]):aval(c[1][1]) for c in v3.contains and conds_of_flat(conds) if is_c(c,"object")}
    for c in conds_of_flat(conds):
        if is_c(c,"predicate") and aval(c[1][1]) in ("have","set"):
            ar=c[1]; obj=ar[3] if len(ar)>3 else None
            ol = vc.get(aval(obj[1][0])) if (obj and is_c(obj,"object")) else None
            # obj may be a var; map var->lemma
            if obj is not None and aval(obj) in vc: ol=vc[aval(obj)]
            ent=BY_ID.get(ol)
            if not ent or ent["onto"]["role"]!="DatatypeProperty": continue
            o=ent["onto"]; dom=o.get("domain","owl:Thing"); cons=o.get("constraint",{})
            if o.get("unit")=="money":
                inner=[f"sh:path schema:value ; sh:datatype {o['datatype']}"]
                if "minInclusive" in cons: inner.append(f"sh:minInclusive {cons['minInclusive']}")
                shape=(f"{dom} sh:property [ sh:path {o['iri']} ; sh:class schema:MonetaryAmount ;\n"
                       f"    sh:node [ a sh:NodeShape ;\n"
                       f"        sh:property [ {' ; '.join(inner)} ; sh:minCount 1 ] ;\n"
                       f"        sh:property [ sh:path schema:currency ; sh:datatype xsd:string ; sh:minCount 1 ] ] ] .")
            else:
                parts=[f"sh:path {o['iri']}", f"sh:datatype {o['datatype']}"]
                if "minInclusive" in cons: parts.append(f"sh:minInclusive {cons['minInclusive']}")
                if "maxInclusive" in cons: parts.append(f"sh:maxInclusive {cons['maxInclusive']}")
                shape=f"{dom} sh:property [ {' ; '.join(parts)} ] ."
            out.append((ol,shape))
    return out

def conds_of_flat(conds):
    out=[]
    for c in conds:
        if isinstance(c,tuple) and c[0]=="list": out+=conds_of_flat(c[1])
        else: out.append(c)
    return out

def main(ace_path, out_path):
    sents=[l.strip() for l in open(ace_path) if l.strip() and not l.strip().startswith("#")]
    shapes=[]; notes=[]; sid=0; seen=set()
    stem=os.path.basename(ace_path).split(".")[0]
    for s in sents:
        sid+=1; drs=v3.run_ape(s)
        if not drs: continue
        conds=conds_of(v3.parse_drs(drs))
        impl=next((c for c in conds if is_c(c,"=>")),None)
        if impl:
            kind=ds.classify_constraint(impl)
            if kind=="cardinality": shapes.append(("card", ds.synth_cardinality(f"{stem}-L{sid}",impl))); notes.append((s,"cardinality→SHACL"))
            elif kind=="conditional":
                sc=ds.synth_conditional(f"{stem}-L{sid}",impl)
                if sc: shapes.append(("cond",sc)); notes.append((s,"conditional→SHACL(sh:or)"))
                else: notes.append((s,"conditional→unsynthesized"))
            elif kind=="obligation": notes.append((s,"obligation→deontic, no SHACL/SWRL form (policy layer)"))
            elif kind=="production": notes.append((s,"production→SWRL (drs2swrl), not SHACL"))
            elif kind in ("enum","subclass"): notes.append((s,f"{kind}→TBox axiom, ontology module via VCR — not a sidecar shape"))
            elif kind=="negative-universal": notes.append((s,"negative-universal→reported (access-control rule; qualifiedMaxCount 0 pending decision)"))
            elif kind=="qualifier-universal": notes.append((s,"qualifier-universal→reported (boolean qualifier axiom via VCR)"))
            else: notes.append((s,f"{kind}→unhandled"))
        else:
            for ol,shape in datatype_shapes(conds):
                if ol in seen: continue
                seen.add(ol)
                shapes.append(("dt",shape)); notes.append((s,f"datatype[{ol}]→SHACL"))
    with open(out_path,"w") as f:
        for p,u in PREFIXES: f.write(f"@prefix {p}: <{u}> .\n")
        f.write(f"\n# generated from {os.path.basename(ace_path)} by drs2shacl_prod.py — build artifact\n\n")
        for i,(k,sh) in enumerate(shapes,1):
            if not sh.lstrip().startswith(f"{v3.DATA_PREFIX}:"):  # synth_* returns a full shape with its own subject
                f.write(sh+"\n\n")
            else:
                f.write(sh+"\n\n")
    print(f"wrote {out_path} — {len(shapes)} shape(s)")
    for s,d in notes: print(f"   {d:32} | {s[:60]}")
    return out_path

if __name__=="__main__":
    ace=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else ace.rsplit('.',1)[0]+".shapes.ttl"
    main(ace,out)
