#!/usr/bin/env python3
"""DRS→TTL compiler engine (v3, completed).

lexicon-map.yaml --> (1) generate APE .ulex  (2) parse .ace pages through APE
(3) compile DRS→TTL using roles/IRIs from the map. No hardcoded vocabulary;
auto-mint only as a fallback for UNMAPPED lemmas (reported, and a hard error
in --strict / production mode).

Modes
-----
  --selftest                     legacy 22-sentence prototype run (kept as the regression fixture)
  --input page.ace [--output f]  compile ONE page to a candidate .ttl
  --all                          compile every wiki/**/*.ace
Candidates default to <repo>/tmp/drs2ttl/<stem>.generated.ttl — NEVER the wiki
sidecar path, because rebuild.sh sweeps every wiki/**/*.ttl into the graph.
Promotion to the sidecar is a deliberate, reviewed step (--in-place).

Settled modeling decisions (Gaps 3/5/6 of the completion handoff)
-----------------------------------------------------------------
GAP 3 — sentence routing. A sentence lands in the sidecar .ttl ONLY if its
  subject denotes a graph node we can name: a proper name (→ muscle:<slug>,
  with lexicon-Individual and dbp: geo overrides) or a lexicon Individual
  ("A fixed-cost-per-point is a modality." → muscle:fixed-cpp). Everything
  else routes elsewhere, never to fresh blank-node pairs:
    - '=>' rules (every/if): cardinality & conditional → SHACL companion
      (drs2shacl_prod); production rules → SWRL companion (drs2swrl);
      enumerations / subclass axioms are TBox → they live in the ontology
      modules via VCR, so the compiler only *reports* them; deontic
      obligations have no SHACL/SWRL form → reported.
    - generic-capability sentences ("A bank-administrator assigns a
      segment.") have NO faithful ABox or class-level encoding today: the
      lexicon maps many lemmas onto shared classes (org:Role,
      schema:SoftwareApplication), so any class-level statement collides,
      and canonical individuals would trip the reasoned SHACL gates. They
      are enumerated in the compile report as pending a vocabulary decision
      (per-lemma subclasses or a capability property — a VCR, not a
      compiler default). This matches the hand-authored canon, which omits
      them.
GAP 5 — annotation preservation. rdfs:label / rdfs:comment / skos:* have no
  ACE sentence form (rhetoric is dropped by design), so the compiler MERGES
  them from the existing hand-authored sidecar: annotation triples for every
  generated subject, plus whole auxiliary annotation nodes (e.g. dbp:Peru
  a schema:Country). Facts in the old sidecar that the ACE cannot yet state
  are diffed and listed in the report ("canon-only facts") — reviewed loss,
  never silent loss. The merge is deterministic, so a future validate-sync
  drift guard (recompile + diff) stays byte-stable.
GAP 6 — APE scoping. One APE call per sentence (line), exactly like
  validate-ace.sh. Empirically APE parses unresolved definites ("The system
  …") standalone as existentials, and the authoring guide mandates
  self-contained sentences (proper names repeated, no cross-sentence
  anaphora), so page-level DRS calls are out of profile.
"""
import argparse, glob, os, re, subprocess, sys, yaml

import kgconfig

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = kgconfig.cfg()["_repo_root"]
# Project identity (kg.config.yaml): the instance-data prefix and the prefix
# used to mint fallback class IRIs for unmapped lemmas.
DATA_PREFIX = kgconfig.prefix()
FALLBACK_CLASS_PREFIX = kgconfig.fallback_class_prefix()

# Canonical lexicon lives in ../ontology/lexicon-map.yaml (single source of truth; same
# resolution as gen-ulex.py). Fall back to a sibling copy for standalone/test use.
_CANON_MAP = os.path.join(HERE, "..", "ontology", "lexicon-map.yaml")
MAP_PATH = _CANON_MAP if os.path.exists(_CANON_MAP) else os.path.join(HERE, "lexicon-map.yaml")
MAP  = yaml.safe_load(open(MAP_PATH))["terms"]
BY_ID = {t["id"]: t for t in MAP}
# APE reports the LEMMA (noun sg / verb infinitive), which is not always the map id
# (id 'champions' ↔ infpl 'champion'). Index by the surface lemma too.
NOUN_BY_SG = {}
VERB_BY_INF = {}
for _t in MAP:
    _a = _t["ace"]
    if _a["pos"] in ("noun", "noun_mass"): NOUN_BY_SG.setdefault(_a["sg"], _t)
    elif _a["pos"] == "tv":                VERB_BY_INF.setdefault(_a["infpl"], _t)

def noun_term(lemma):  return NOUN_BY_SG.get(lemma) or BY_ID.get(lemma)
def verb_term(lemma):  return VERB_BY_INF.get(lemma) or BY_ID.get(lemma)
ADJ_BY_POS = {t["ace"]["positive"]: t for t in MAP if t["ace"]["pos"]=="adj"}
def qual_iri(adj):
    t=ADJ_BY_POS.get(adj) or BY_ID.get(adj)
    if t and t["onto"].get("iri"): return t["onto"]["iri"]
    unmapped.add(adj); return f"{FALLBACK_CLASS_PREFIX}:is"+pascal(adj)

# APE is an external built tool (SWI-Prolog saved state). Same resolution as validate-ace.sh:
# $APE_HOME, else a sibling ./APE, else the repo's built copy under tmp/cnl-experiment/APE.
APE = os.environ.get("APE_HOME") or os.path.join(HERE, "APE")
if not os.path.exists(os.path.join(APE, "ape.exe")):
    _fallback_ape = os.path.join(HERE, "..", "..", "tmp", "cnl-experiment", "APE")
    if os.path.exists(os.path.join(_fallback_ape, "ape.exe")):
        APE = _fallback_ape

GEN_ULEX = os.path.join(HERE,"lexicon.gen.ulex")
HUMAN = {"super-admin","admin","analyst","bank-administrator","user","cardholder","customer"}
unmapped = set()

# Named individuals that must NOT resolve to muscle:<slug>. Countries follow the
# canon precedent (CR-0006 country refactoring → dbpedia IRIs); continents/regions
# use the same dbp scheme so the graph never forks a second geo namespace.
DBP_GEO = {
    "peru":"dbp:Peru", "panama":"dbp:Panama", "mexico":"dbp:Mexico",
    "costa-rica":"dbp:Costa_Rica", "united-kingdom":"dbp:United_Kingdom",
    "asia":"dbp:Asia", "africa":"dbp:Africa", "europe":"dbp:Europe",
    "latin-america":"dbp:Latin_America", "north-america":"dbp:North_America",
    # VCR-0020 (2026-07-07): corporate-structure ingestion needs these two —
    # found missing when "Cayman-Islands" silently minted a fresh muscle:cayman-islands
    # instead of resolving to the seeds/countries.ttl individual.
    "cayman-islands":"dbp:Cayman_Islands", "united-states":"dbp:United_States",
    "delaware":"dbp:Delaware",
}
# Proper-name aliases whose canonical IRI is not lowercase(name); the page-slug
# rule (IRIs are permanent) wins over the surface name. Configured per project
# in kg.config.yaml → compiler.named_aliases.
NAMED_ALIASES = kgconfig.named_aliases()

# Project namespaces (data + authored modules) come from kg.config.yaml;
# upstream namespaces are universal and stay here.
PREFIXES = list(kgconfig.project_namespaces()) + [
 ("org","http://www.w3.org/ns/org#"),
 ("schema","https://schema.org/"),
 ("prov","http://www.w3.org/ns/prov#"),
 ("dct","http://purl.org/dc/terms/"),
 ("dbp","http://dbpedia.org/resource/"),
 ("fibo-fbc-fct-fse","https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/"),
 ("fibo-fnd-utl-alx","https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/"),
 ("fibo-be-oc-op","https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/"),
 ("fibo-be-le-lei","https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/"),
 ("rdf","http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
 ("rdfs","http://www.w3.org/2000/01/rdf-schema#"),
 ("owl","http://www.w3.org/2002/07/owl#"),
 ("sh","http://www.w3.org/ns/shacl#"),
 ("skos","http://www.w3.org/2004/02/skos/core#"),
 ("xsd","http://www.w3.org/2001/XMLSchema#"),
]
_PREF_BY_URI = sorted(PREFIXES, key=lambda p: -len(p[1]))

def to_qname(uri):
    u = str(uri)
    for p, base in _PREF_BY_URI:
        if u.startswith(base) and len(u) > len(base):
            local = u[len(base):]
            if re.fullmatch(r"[A-Za-z_][\w.-]*", local): return f"{p}:{local}"
    return f"<{u}>"

# Annotation predicates have no ACE form (rhetoric layer) — merged from the
# hand-authored sidecar, never compiled.
ANNOTATION_PREDS = {
    "rdfs:label","rdfs:comment","skos:prefLabel","skos:altLabel",
    "skos:definition","skos:example","skos:note","skos:scopeNote","dct:title",
    # lifecycle/composition metadata about the record itself, no ACE-assertable form (VCR-0019)
    # dct:hasPart is declared owl:AnnotationProperty in our TBox — record composition, not a domain fact
    "owl:deprecated","schema:creativeWorkStatus","dct:hasPart",
    # page metadata: the record's publication date lives in frontmatter/canon; the
    # ACE states the field ("has a publication-date") but no corpus sentence carries
    # the value yet — carried over so RecordShape (dct:date minCount 1) holds
    "dct:date",
}

SENTENCES = [
 (1,"Interbank is a financial-institution. Interbank operates-in Peru."),
 (2,"Interbank offers the retail-banking and offers the corporate-finance and offers the wealth-management."),
 (3,"Interbank is a subsidiary of Intercorp. Intercorp is a conglomerate. Intercorp operates-in Peru."),
 (4,"AstroPay is a digital-payment-solution. AstroPay is a digital-wallet. AstroPay operates-in Asia."),
 (5,"Shopstar integrates-with Interbank. A user buys a product with a loyalty-point. Shopstar offers a discount to a cardholder."),
 (6,"Banco-General owns Yappy. Yappy is a peer-to-peer-payment-platform. Yappy operates-in Panama."),
 (7,"The system groups a user with a bank-uniq-id. The system imports a user with a csv-upload."),
 (8,"The system validates a segment during a transaction."),
 (9,"The campaign-manager controls a promotional-banner and controls a discount-badge and controls a pricing-view and controls a custom-message."),
 (10,"The file-manager manages a directory and manages a block-schema."),
 (11,"Pricing-results tracks a total-generated-value and tracks a daily-saving and tracks a customer-delivered-value."),
 (12,"If a change is critical then a user must perform a two-factor-authentication."),
 (13,"If a user is in a segment and the segment has no active-strategy then the system assigns a base-configuration to the user."),
 (14,"Every modality is a fixed-cost-per-point or is a proportional-modality or is a share-value."),
 (15,"Every governance-role is a super-admin or is an admin or is an analyst."),
 (16,"MUSCLE manages a technology and manages an uptime. A bank defines a strategy."),
 (17,"A strategy has a minimum-point-usage and has a redemption-limit and has a wait-time-control and has a total-item-cap and has a budget-maximum."),
 (18,"A bank-administrator sets a name and sets a segment and sets a channel."),
 (19,"A bank-administrator sets a fiat-value-reference."),
 (20,"A bank-administrator creates a pricing-strategy in a dashboard."),
 (21,"Club-Bi is not a customer."),
 (22,"MUSCLE-Dashboard is Control-Tower."),
]

# ---------- PROJECTION 1: APE .ulex ----------
def gen_ulex():
    lines = ["% generated from lexicon-map.yaml — do not edit by hand"]
    for t in MAP:
        a=t["ace"]; pos=a["pos"]
        if pos=="noun":      lines.append(f"noun_sg('{a['sg']}', '{t['id']}', {'human' if t['id'] in HUMAN else 'neutr'}).")
        elif pos=="noun_mass":lines.append(f"noun_mass('{a['sg']}', '{t['id']}', neutr).")
        elif pos=="tv":      lines.append(f"tv_finsg('{a['finsg']}', '{a['infpl']}'). tv_infpl('{a['infpl']}', '{a['infpl']}').")
        elif pos=="adj":     lines.append(f"adj_itr('{a['positive']}', '{a['positive']}').")
    open(GEN_ULEX,"w").write("\n".join(lines)+"\n")
    return sum(1 for t in MAP)

# ---------- DRS Prolog-term parser ----------
# Token order matters: sentence/token indices (-1/7, or -1/'' on synthesized
# conditions like has_part) and decimals (99.9) must win over the bare '-' and
# integer alternatives. Index tokens are dropped here, so quoted strings can
# never be corrupted by a textual pre-strip.
_INDEX=r"-\d+/(?:\d+|'[^']*')"
TOKEN=re.compile(r"\s*('(?:[^'\\]|\\.)*'|=>|"+_INDEX+r"|[A-Za-z_][A-Za-z0-9_]*|\d+\.\d+|\d+|[()\[\],-])")
def tokenize(s):
    pos,out=0,[]
    while pos<len(s):
        m=TOKEN.match(s,pos)
        if not m:
            if s[pos].isspace():pos+=1;continue
            raise ValueError(f"bad token {s[pos:pos+20]!r}")
        tok=m.group(1)
        if not re.fullmatch(_INDEX,tok):out.append(tok)
        pos=m.end()
    return out
class P:
    def __init__(s,t):s.t=t;s.i=0
    def peek(s):return s.t[s.i] if s.i<len(s.t) else None
    def nxt(s):tok=s.t[s.i];s.i+=1;return tok
    def parse(s):
        tok=s.nxt()
        if tok=="[":
            items=[]
            if s.peek()=="]":s.nxt();return("list",items)
            while True:
                items.append(s.parse())
                if s.peek()==",":s.nxt();continue
                if s.peek()=="]":s.nxt();break
            return("list",items)
        if s.peek()=="(":
            s.nxt();args=[]
            if s.peek()==")":s.nxt();return(tok,[])
            while True:
                args.append(s.parse())
                if s.peek()==",":s.nxt();continue
                if s.peek()==")":s.nxt();break
            return(tok,args)
        return("atom",tok)
def parse_drs(t):return P(tokenize(t.strip())).parse()

def is_c(n,name=None):return isinstance(n,tuple) and n[0] not in("atom","list") and (name is None or n[0]==name)
def aval(n):
    if isinstance(n,tuple) and n[0]=="atom":
        v=n[1];return v[1:-1] if v.startswith("'") else v
    return None
def conds_of(d):return d[1][1][1] if is_c(d,"drs") and d[1][1][0]=="list" else []
def flatten(conds):
    out=[]
    for c in conds:
        if isinstance(c,tuple) and c[0]=="list": out+=flatten(c[1])
        else: out.append(c)
    return out
def contains(n,f):
    if is_c(n,f):return True
    if isinstance(n,tuple) and n[0]=="list":return any(contains(x,f) for x in n[1])
    if isinstance(n,tuple) and n[0]!="atom" and isinstance(n[1],list):return any(contains(x,f) for x in n[1])
    return False
def num_obj(d):return sum(1 for c in conds_of(d) if is_c(c,"object"))

# ---------- IRI helpers (map-driven) ----------
def pascal(l):return "".join(p.capitalize() for p in re.split(r"[-_]",l))
def named_iri(x):
    slug=x.lower()
    if slug in NAMED_ALIASES: return NAMED_ALIASES[slug]
    t=noun_term(slug)
    if t and t["onto"]["role"]=="Individual": return t["onto"]["iri"]
    if slug in DBP_GEO: return DBP_GEO[slug]
    return f"{DATA_PREFIX}:{slug}"
def class_iri(lemma):
    t=noun_term(lemma)
    if t and t["onto"]["role"] in ("Class","Individual"): return t["onto"]["iri"]
    if t and t["onto"]["role"]=="RelationalNoun": return t["onto"].get("range","owl:Thing")
    unmapped.add(lemma); return f"{FALLBACK_CLASS_PREFIX}:"+pascal(lemma)
def is_individual(lemma):
    t=noun_term(lemma); return bool(t) and t["onto"]["role"]=="Individual"
def pred_iri(verb):
    t=verb_term(verb)
    if t and t["onto"]["role"]=="ObjectProperty": return t["onto"]["iri"]
    unmapped.add(verb); return "biz:"+verb.replace("-","_")

def arg_term(node):
    if is_c(node,"named"):return("named",aval(node[1][0]))
    a=aval(node)
    if a is None:return("other",node)
    return("var",a) if re.fullmatch(r"[A-Z][A-Za-z0-9_]*",a) else("atom",a)

def resolve(term,bn,vc,triples,sid):
    if term is None:return None
    if term[0]=="named":return named_iri(term[1])
    if term[0]=="var":
        v=term[1];lemma=vc.get(v)
        if lemma and is_individual(lemma):return noun_term(lemma)["onto"]["iri"]   # individual → its IRI, no bnode
        if v not in bn:
            bn[v]=f"_:s{sid}b{len(bn)}"
            if lemma:triples.append((bn[v],"a",class_iri(lemma)))
        return bn[v]
    if term[0]=="atom":return named_iri(term[1])
    return None

def literal_value(node):
    """DRS literal object → (kind, value-string) for int(1897) / real(0.14) /
    string('Running'); None for anything else."""
    if isinstance(node,tuple) and node[0] in ("int","real","string") and len(node[1])==1:
        return (node[0], aval(node[1][0]))
    return None

# ---------- Literal formatting & validation (Rule 10) ----------
_DT_PATTERNS = {
    "xsd:integer": r"-?\d+",
    "xsd:decimal": r"-?\d+(\.\d+)?",
    "xsd:gYear":   r"\d{4}",
    "xsd:date":    r"\d{4}-\d{2}-\d{2}",
    "xsd:boolean": r"true|false",
}
def turtle_str(v):return '"'+v.replace("\\","\\\\").replace('"','\\"')+'"'
def fmt_literal(kind, val, ent, warns, where):
    """Format a DRS literal with the lexicon term's datatype domain; validate
    pattern and constraint bounds/enumeration; None if the value should be
    reified instead (unit: money → schema:MonetaryAmount)."""
    o=ent["onto"]; dt=o.get("datatype","xsd:string")
    pat=_DT_PATTERNS.get(dt)
    if pat and not re.fullmatch(pat,val):
        warns.append(f"{where}: value {val!r} does not match {dt} lexical form")
    cons=o.get("constraint",{})
    if kind in ("int","real"):
        try:
            x=float(val)
            if "minInclusive" in cons and x<cons["minInclusive"]:
                warns.append(f"{where}: {val} < minInclusive {cons['minInclusive']}")
            if "maxInclusive" in cons and x>cons["maxInclusive"]:
                warns.append(f"{where}: {val} > maxInclusive {cons['maxInclusive']}")
        except ValueError: pass
    if "in" in cons and val not in cons["in"]:
        warns.append(f"{where}: {val!r} not in enumeration {cons['in']}")
    if o.get("unit")=="money": return None      # caller reifies
    if dt=="xsd:string": return turtle_str(val)
    if dt=="xsd:decimal" and "." not in val:
        # Canonicalize to a decimal-point lexical form. Some downstream Turtle writers
        # (e.g. ROBOT's reasoned-graph serializer) use the bare-number shorthand for any
        # integer-looking literal, silently downgrading "100"^^xsd:decimal to a plain 100
        # (implicitly xsd:integer) — which then fails sh:datatype xsd:decimal shapes.
        val=val+".0"
    return turtle_str(val)+"^^"+dt

# ---------- Sentence routing (Gap 3) ----------
def find_card(cons_drs):
    """Cardinality-quantified object in a rule consequent, seeing through must(...).
    Returns (pred_cond, obj_cond, op, n) or None."""
    cc=flatten(conds_of(cons_drs))
    for c in list(cc):
        if is_c(c,"must"): cc+=flatten(conds_of(c[1][0]))
    pred=next((c for c in cc if is_c(c,"predicate") and aval(c[1][1])!="be"),None)
    obj=next((c for c in cc if is_c(c,"object")),None)
    if not pred or not obj: return None
    op=aval(obj[1][4]); n=aval(obj[1][5])
    return (pred,obj,op,int(n) if n and n.isdigit() else 1)

def classify_rule(conds):
    """Destination of an '=>' sentence. The sidecar .ttl gets none of these."""
    impl=next(c for c in conds if is_c(c,"=>"))
    ant,cons=impl[1][0],impl[1][1]
    if contains(cons,"v"): return "enum"
    if contains(ant,"=>") or contains(cons,"=>"): return "production"
    if contains(cons,"-") and not contains(cons,"must"): return "negative-universal"
    if contains(cons,"property"): return "qualifier-universal"
    card=find_card(cons)
    ant_flat=flatten(conds_of(ant))
    ant_var=next((aval(c[1][0]) for c in ant_flat if is_c(c,"object")),None)
    if card:
        pred,obj,op,n=card
        subj=arg_term(pred[1][2])
        if subj[0]=="var" and subj[1]==ant_var:
            # cardinality on the quantified subject itself → SHACL
            ant_preds=[c for c in ant_flat if is_c(c,"predicate") and aval(c[1][1])!="be"]
            return "conditional" if (len([c for c in ant_flat if is_c(c,"object")])>1 or ant_preds or contains(ant,"-")) else "cardinality"
    if contains(cons,"must"): return "obligation"
    if contains(ant,"-") or contains(cons,"-"): return "production"
    cons_flat=flatten(conds_of(cons))
    if all(is_c(c,("object")) or (is_c(c,"predicate") and aval(c[1][1])=="be") for c in cons_flat):
        return "subclass"
    return "conditional"

RULE_DEST = {
    "cardinality": "SHACL shapes companion (drs2shacl_prod)",
    "conditional": "SHACL shapes companion (drs2shacl_prod, sh:or)",
    "production":  "SWRL companion (drs2swrl)",
    "obligation":  "deontic — no SHACL/SWRL form; policy layer (reported)",
    "enum":        "TBox enumeration — ontology module via VCR (reported)",
    "subclass":    "TBox subclass axiom — ontology module via VCR (reported)",
    "negative-universal": "access-control rule (No X verbs Y) — SHACL qualifiedMaxCount 0 possible; reported pending decision",
    "qualifier-universal": "boolean qualifier axiom — sh:hasValue shape or ontology axiom via VCR (reported)",
}

# ---------- ABox compilation for page mode ----------
def compile_sentence_abox(conds, sid, warns, existentials="report"):
    """Compile ONE non-rule sentence. Returns (triples, notes); triples are
    (s,p,o) qname strings; notes are (category, detail) routing records.
    existentials: 'report' (default) routes generic-Class objects of named
    subjects to the report — the deployed SHACL gate is closed-world, and a
    typed existential bnode ("manages a pricing-strategy" → _:x a
    muscle:PricingStrategy) fires every shape targeting that class (proven:
    71+ violations on the 20-page corpus). 'bnode' restores the faithful
    OWL existential for a future bnode-aware shapes gate."""
    flat=flatten(conds); triples=[]; notes=[]; bn={}
    vc={}; card={}; groups={}
    for c in flat:
        if is_c(c,"object"):
            v=aval(c[1][0]); vc[v]=aval(c[1][1])
            card[v]=(aval(c[1][4]),aval(c[1][5]))
        elif is_c(c,"has_part"):        # "X and Y" coordination: group var → member vars
            g=aval(c[1][0]); groups.setdefault(g,[]).append(arg_term(c[1][1]))
    relational={aval(c[1][0]) for c in flat if is_c(c,"relation")}
    lit={}
    for c in flat:
        if is_c(c,"predicate") and aval(c[1][1])=="be" and len(c[1])>3:
            s=arg_term(c[1][2]); o=arg_term(c[1][3])
            if s[0]=="var" and o[0]=="other":
                v=literal_value(o[1])
                if v is not None: lit[s[1]]=v

    def node_iri(term):
        """IRI for a subject/object we can name; None for generic vars."""
        if term is None: return None
        if term[0] in ("named","atom"): return named_iri(term[1])
        if term[0]=="var":
            lemma=vc.get(term[1])
            if lemma and is_individual(lemma): return noun_term(lemma)["onto"]["iri"]
        return None

    for c in flat:
        if not is_c(c,"predicate"): continue
        ar=c[1]; verb=aval(ar[1])
        subj=arg_term(ar[2]); obj=arg_term(ar[3]) if len(ar)>3 else None
        iobj=arg_term(ar[4]) if len(ar)>4 else None
        if verb=="be":
            if subj[0]=="var" and obj and obj[0]=="other": continue   # literal relative, consumed above
            s_iri=node_iri(subj)
            if s_iri and obj and obj[0] in ("named","atom"):
                _same_as(triples, s_iri, named_iri(obj[1])); continue
            if s_iri and obj and obj[0]=="var":
                ol=vc.get(obj[1])
                if obj[1] in relational: continue                     # handled by relation()
                if ol and is_individual(ol):
                    _same_as(triples, s_iri, noun_term(ol)["onto"]["iri"]); continue
                if ol: triples.append((s_iri,"a",class_iri(ol))); continue
            if s_iri is None and subj[0]=="var":
                notes.append(("generic",f"be-sentence with generic subject '{vc.get(subj[1])}'"))
            continue
        s_iri=node_iri(subj)
        if s_iri is None:
            notes.append(("generic",f"{vc.get(subj[1],'?') if subj[0]=='var' else subj[1]} {verb} …")); continue
        if iobj is not None:
            notes.append(("ditransitive",f"{verb} … to … — no ABox form; needs modeling")); continue
        # datatype-valued object noun (Rule 10)
        ol=vc.get(obj[1]) if obj and obj[0]=="var" else None
        ent=noun_term(ol) if ol else None
        if ent and ent["onto"]["role"]=="DatatypeProperty":
            o=ent["onto"]; val=lit.get(obj[1])
            if val is not None:
                f=fmt_literal(val[0],val[1],ent,warns,ol)
                if f is None:   # money → reify (currency has no ACE carrier yet)
                    b=f"_:L{sid}m{len(bn)}"; bn[b]=b
                    triples.append((s_iri,o["iri"],b))
                    triples.append((b,"a","schema:MonetaryAmount"))
                    triples.append((b,"schema:value",turtle_str(val[1])+"^^"+o.get("datatype","xsd:decimal")))
                    warns.append(f"{ol}: money value reified; currency not stated in ACE (Rule 10 gap)")
                else:
                    triples.append((s_iri,o["iri"],f))
            elif card.get(obj[1],(None,None))[0] in ("exactly","leq","geq"):
                notes.append(("individual-cardinality",
                    f"'{ol}' {card[obj[1]][0]} {card[obj[1]][1]} on {s_iri} — needs a conditional/targetNode "
                    f"shape decision (cf. VCR K4 sh:or pattern); not auto-synthesized"))
            else:
                notes.append(("valueless-datatype",
                    f"'{ol}' stated without a value — domain shape lives in the SHACL companion"))
            continue
        if verb=="have":
            notes.append(("bare-have",f"has a '{ol}' — no canonical object property for generic 'have'; "
                                      f"use a specific verb or open a VCR")); continue
        def obj_targets(term):
            if term is None: return []
            if term[0]=="var" and term[1] in groups:      # coordinated objects → one triple each
                out=[]
                for m in groups[term[1]]: out+=obj_targets(m)
                return out
            i=node_iri(term)
            if i: return [i]
            if term[0]=="var":
                ol2=vc.get(term[1])
                if ol2 and ol2!="na":
                    if existentials!="bnode":
                        notes.append(("existential-object",
                            f"{verb} a '{ol2}' — generic object; typed bnodes fire the closed-world "
                            f"shapes, so reported (re-run with --existentials=bnode for the OWL form)"))
                        return []
                    if term[1] not in bn:
                        bn[term[1]]=f"_:L{sid}b{len(bn)}"
                        triples.append((bn[term[1]],"a",class_iri(ol2)))
                    return [bn[term[1]]]
            return []
        targets=obj_targets(obj)
        if targets:
            p=pred_iri(verb)
            t_ent=verb_term(verb)
            for o_iri in targets:
                triples.append((s_iri,p,o_iri))
                # map-declared symmetric properties are completed both ways
                # (skos:related / swe:integratesWith): SHACL checks symmetry
                if t_ent and t_ent["onto"].get("symmetric") and not o_iri.startswith("_:"):
                    triples.append((o_iri,p,s_iri))
        elif obj: notes.append(("unresolved-object",f"{verb} object could not be resolved"))

    # adjectives → boolean Qualifier triples ("Funbank is fictional." → biz:isFictional true)
    for c in flat:
        if not is_c(c,"property"): continue
        pv=aval(c[1][0]); adj=aval(c[1][1])
        for d in flat:
            if is_c(d,"predicate") and aval(d[1][1])=="be" and len(d[1])>3:
                o=arg_term(d[1][3]); s=node_iri(arg_term(d[1][2]))
                if o[0]=="var" and o[1]==pv and s:
                    triples.append((s,qual_iri(adj),"true"))

    for c in flat:
        if not is_c(c,"relation"): continue
        v=aval(c[1][0]); arg=arg_term(c[1][2]); cls=vc.get(v)
        ent=noun_term(cls) if cls else None
        rel=ent["onto"].get("relationIri") if ent else None
        if not rel: unmapped.add(f"{cls}-of"); rel="biz:"+(cls or "x").replace("-","_")+"Of"
        holder=None
        for d in flat:
            if is_c(d,"predicate") and aval(d[1][1])=="be" and len(d[1])>3:
                o=arg_term(d[1][3]); s=arg_term(d[1][2])
                if o[0]=="var" and o[1]==v and s[0] in ("named","atom"): holder=named_iri(s[1])
        if holder and arg[0] in ("named","atom"):
            triples.append((holder,rel,named_iri(arg[1])))
        elif not holder:
            notes.append(("generic",f"relational noun '{cls}' without a named holder"))
    return triples, notes

def compile_negation(conds,triples,sid=0):
    for c in conds:
        if not is_c(c,"-"):continue
        inner=flatten(conds_of(c[1][0]));vc={}
        for d in inner:
            if is_c(d,"object"):vc[aval(d[1][0])]=aval(d[1][1])
        rel_vars={aval(d[1][0]):d for d in inner if is_c(d,"relation")}
        prop_vars={aval(d[1][0]):aval(d[1][1]) for d in inner if is_c(d,"property")}
        for d in inner:
            if is_c(d,"predicate") and aval(d[1][1])=="be" and len(d[1])>3:
                s=arg_term(d[1][2]);o=arg_term(d[1][3])
                if s[0]!="named" or o[0]!="var": continue
                subj=named_iri(s[1])
                if o[1] in rel_vars:
                    # "X is not a client of Y" — negated relational noun ≠ complement of its
                    # RANGE class; the faithful ABox form is an owl:NegativePropertyAssertion
                    cls=vc.get(o[1]); ent=noun_term(cls) if cls else None
                    rel=ent["onto"].get("relationIri") if ent else None
                    if not rel: unmapped.add(f"{cls}-of"); rel="biz:"+(cls or "x").replace("-","_")+"Of"
                    arg=arg_term(rel_vars[o[1]][1][2])
                    if arg[0] in ("named","atom"):
                        b=f"_:negL{sid}n{len(triples)}"
                        triples+= [(b,"a","owl:NegativePropertyAssertion"),
                                   (b,"owl:sourceIndividual",subj),
                                   (b,"owl:assertionProperty",rel),
                                   (b,"owl:targetIndividual",named_iri(arg[1]))]
                elif o[1] in prop_vars:
                    # "X is not real." — negated boolean Qualifier
                    triples.append((subj,qual_iri(prop_vars[o[1]]),"false"))
                elif o[1] in vc:
                    triples.append((subj,"a",f"[ owl:complementOf {class_iri(vc[o[1]])} ]"))

def render(node):
    if is_c(node,"drs"):return "; ".join(filter(None,(render(c) for c in conds_of(node))))
    if is_c(node,"=>"):return f"IF [{render(node[1][0])}] THEN [{render(node[1][1])}]"
    if is_c(node,"must"):return f"MUST [{render(node[1][0])}]"
    if is_c(node,"-"):return f"NOT [{render(node[1][0])}]"
    if is_c(node,"v"):return f"({render(node[1][0])} OR {render(node[1][1])})"
    if is_c(node,"object"):return f"a {aval(node[1][1])}"
    if is_c(node,"predicate"):return aval(node[1][1])
    if is_c(node,"property"):return f"is {aval(node[1][1])}"
    return None

# ---------- legacy prototype path (kept: regression fixture + drs2shacl.py deps) ----------
def compile_abox(conds,triples,sid):
    bn,vc,lit={},{},{}
    for c in conds:
        if is_c(c,"object"):vc[aval(c[1][0])]=aval(c[1][1])
    relational={aval(c[1][0]) for c in conds if is_c(c,"relation")}
    for c in conds:
        if is_c(c,"predicate"):
            ar=c[1]
            if aval(ar[1])=="be" and len(ar)>3:
                s=arg_term(ar[2]);o=arg_term(ar[3])
                if s[0]=="var":
                    v=literal_value(o[1]) if o[0]=="other" else None
                    if v is not None:lit[s[1]]=v[1]
    for c in conds:
        if is_c(c,"predicate"):
            ar=c[1];verb=aval(ar[1]);subj=arg_term(ar[2])
            obj=arg_term(ar[3]) if len(ar)>3 else None; iobj=arg_term(ar[4]) if len(ar)>4 else None
            if verb=="be":
                if subj[0]=="named" and obj and obj[0]=="named":
                    _same_as(triples, named_iri(subj[1]), named_iri(obj[1]));continue
                if subj[0]=="named" and obj and obj[0]=="var" and obj[1] in vc and obj[1] not in relational:
                    triples.append((named_iri(subj[1]),"a",class_iri(vc[obj[1]])));continue
                continue
            ol=vc.get(obj[1]) if obj and obj[0]=="var" else None
            ent=noun_term(ol) if ol else None
            if ent and ent["onto"]["role"]=="DatatypeProperty":
                o=ent["onto"]
                val=lit.get(obj[1]) if obj and obj[0]=="var" else None
                if val is not None and subj[0]=="named":
                    triples.append((named_iri(subj[1]),o["iri"],f'"{val}"^^{o.get("datatype","xsd:string")}'));continue
                sl=vc.get(subj[1]) if subj[0]=="var" else None
                dom=o.get("domain") or (class_iri(sl) if sl else "owl:Thing")
                parts=[f"sh:path {o['iri']}",f"sh:datatype {o['datatype']}"]
                if "constraint" in o and "minInclusive" in o["constraint"]:parts.append(f"sh:minInclusive {o['constraint']['minInclusive']}")
                triples.append((dom,"sh:property","[ "+" ; ".join(parts)+" ]"));continue
            s=resolve(subj,bn,vc,triples,sid);o=resolve(obj,bn,vc,triples,sid) if obj else None
            if s and o:triples.append((s,pred_iri(verb),o))
            if iobj:
                io=resolve(iobj,bn,vc,triples,sid)
                if s and io:triples.append((s,pred_iri(verb)+"Recipient" if pred_iri(verb)[-1].isalpha() else pred_iri(verb),io))
        elif is_c(c,"relation"):
            v=aval(c[1][0]);arg=arg_term(c[1][2]);cls=vc.get(v)
            ent=noun_term(cls) if cls else None;rel=ent["onto"].get("relationIri") if ent else None
            if not rel:unmapped.add(f"{cls}-of");rel="biz:"+(cls or "x").replace("-","_")+"Of"
            holder=None
            for d in conds:
                if is_c(d,"predicate") and aval(d[1][1])=="be":
                    o=arg_term(d[1][3]) if len(d[1])>3 else None;s=arg_term(d[1][2])
                    if o and o[0]=="var" and o[1]==v and s[0]=="named":holder=named_iri(s[1])
            if holder and arg[0]=="named":triples.append((holder,rel,named_iri(arg[1])))

def classify(conds):
    impl=[c for c in conds if is_c(c,"=>")]
    if impl:
        ant,cons=impl[0][1][0],impl[0][1][1]
        if contains(ant,"must") or contains(cons,"must"):return "constraint"
        if contains(ant,"=>") or contains(cons,"=>") or contains(ant,"-") or contains(cons,"-") or contains(ant,"modifier_pp"):return "constraint"
        if contains(cons,"v"):return "enum"
        if num_obj(ant)==1 and num_obj(cons)>=1:return "subclass"
        return "constraint"
    if any(is_c(c,"-") for c in conds):return "negation"
    return "abox"

def handle_tbox(kind,conds,triples,shapes,sid):
    impl=[c for c in conds if is_c(c,"=>")][0];ant,cons=impl[1][0],impl[1][1]
    xl=next((aval(a[1][1]) for a in conds_of(ant) if is_c(a,"object")),None)
    if kind=="enum":
        ent=noun_term(xl) if xl else None;members=ent["onto"].get("enumeration") if ent else None
        if members:
            for m in members:triples.append((m,"a",_member_type(m)))
            triples.append((class_iri(xl),"owl:equivalentClass",f"[ owl:oneOf ( {' '.join(members)} ) ]"))
    elif kind=="subclass":
        for y in [aval(d[1][1]) for d in conds_of(cons) if is_c(d,"object")]:
            triples.append((class_iri(xl),"rdfs:subClassOf",class_iri(y)))
    elif kind=="constraint":
        shapes.append((sid,render(impl)))

def _member_type(iri):
    for t in MAP:
        if t["onto"].get("iri")==iri:return t["onto"].get("type","owl:NamedIndividual")
    return "owl:NamedIndividual"

_APE_CACHE={}
def run_ape(ace):
    if ace in _APE_CACHE: return _APE_CACHE[ace]
    r=subprocess.run(["swipl","-x","ape.exe","--","-text",ace,"-ulexfile",GEN_ULEX,"-solo","drs"],cwd=APE,capture_output=True,text=True)
    # APE may print warnings before the DRS — accept any line starting with drs(
    # (same acceptance rule as validate-ace.sh)
    out=next((ln.strip() for ln in r.stdout.splitlines() if ln.strip().startswith("drs(")),None)
    _APE_CACHE[ace]=out
    return out

# ---------- Annotation merge + canon diff (Gap 5) ----------
def _lit_qstr(o):
    import rdflib
    if isinstance(o,rdflib.Literal):
        s=turtle_str(str(o))
        if o.language: return s+"@"+o.language
        if o.datatype and str(o.datatype)!="http://www.w3.org/2001/XMLSchema#string":
            return s+"^^"+to_qname(o.datatype)
        return s
    return to_qname(o)

def merge_from_canon(old_ttl_path, gen_triples):
    """Deterministic merge/diff against the hand-authored sidecar.
    Returns (annotation_triples, aux_triples, canon_only_facts)."""
    import rdflib
    g=rdflib.Graph(); g.parse(old_ttl_path, format="turtle")
    gen_subjects={t[0] for t in gen_triples}
    gen_objects={t[2] for t in gen_triples}
    gen_ground={t for t in gen_triples if not t[0].startswith("_:") and not str(t[2]).startswith("_:")}
    annots,aux,canon_only=[],[],[]
    aux_subjects=set()
    for s,p,o in sorted(g, key=lambda t:(str(t[0]),str(t[1]),str(t[2]))):
        if isinstance(s,rdflib.BNode) or isinstance(o,rdflib.BNode):
            continue
        sq,pq,oq=to_qname(s),to_qname(p),_lit_qstr(o)
        if pq=="rdf:type": pq="a"
        if pq in ANNOTATION_PREDS:
            if sq in gen_subjects: annots.append((sq,pq,oq))
            elif sq in gen_objects: aux_subjects.add(sq)
            else:
                # annotation-only orphan node (e.g. a deprecation tombstone on a retired
                # IRI — "IRIs are forever"): if the subject carries NOTHING but annotation
                # predicates in the old sidecar, ride it along as an aux node instead of
                # reporting it canon-only (VCR-0019).
                subj_preds={to_qname(p2) for _,p2,_ in g.triples((s,None,None))}
                subj_preds={("a" if x=="rdf:type" else x) for x in subj_preds}
                if subj_preds <= ANNOTATION_PREDS:
                    aux_subjects.add(sq); aux.append((sq,pq,oq))
                else:
                    canon_only.append((sq,pq,oq))
            continue
        if (sq,pq,oq) in gen_ground: continue
        if sq in gen_objects and sq not in gen_subjects:
            aux_subjects.add(sq); aux.append((sq,pq,oq))
        else:
            canon_only.append((sq,pq,oq))
    # annotations of auxiliary nodes ride along with them
    for s,p,o in sorted(g, key=lambda t:(str(t[0]),str(t[1]),str(t[2]))):
        if isinstance(s,rdflib.BNode) or isinstance(o,rdflib.BNode): continue
        sq,pq,oq=to_qname(s),to_qname(p),_lit_qstr(o)
        if sq in aux_subjects and pq in ANNOTATION_PREDS:
            aux.append((sq,pq,oq))
            canon_only[:]=[t for t in canon_only if t!=(sq,pq,oq)]
    return annots,aux,canon_only

# ---------- Page compiler ----------
def page_sentences(ace_path):
    out=[]
    for i,l in enumerate(open(ace_path),1):
        s=l.strip()
        if s and not s.startswith("#"): out.append((i,s))
    return out

def _same_as(triples, a, b):
    # reflexive sameAs is vacuous noise (e.g. "AgentCars is a cars-api-provider." where the
    # Individual-role noun already denotes the same IRI) — skip it (VCR-0019 round)
    if a != b: triples.append((a, "owl:sameAs", b))

def compile_page(ace_path, out_path=None, merge=True, shapes=True, swrl=True, strict=False, quiet=False, existentials="report"):
    unmapped.clear()
    stem=os.path.basename(ace_path).rsplit(".",1)[0]
    if out_path is None:
        outdir=os.path.join(REPO,"tmp","drs2ttl"); os.makedirs(outdir,exist_ok=True)
        out_path=os.path.join(outdir,stem+".generated.ttl")
    sents=page_sentences(ace_path)
    per_sentence=[]; warns=[]; tally={}
    for lineno,text in sents:
        drs=run_ape(text)
        if not drs:
            per_sentence.append((lineno,text,"PARSE-FAIL",[],[("parse-fail","run validate-ace.sh")])); continue
        conds=conds_of(parse_drs(drs))
        if any(is_c(c,"=>") for c in conds):
            kind=classify_rule(conds)
            per_sentence.append((lineno,text,"rule:"+kind,[],[("rule",RULE_DEST[kind])]))
        elif any(is_c(c,"-") for c in conds):
            triples=[]; compile_negation(conds,triples,lineno)
            per_sentence.append((lineno,text,"negation",triples,[] if triples else [("generic","negation without named subject")]))
        else:
            triples,notes=compile_sentence_abox(conds,lineno,warns,existentials)
            kind="abox" if triples else (notes[0][0] if notes else "empty")
            per_sentence.append((lineno,text,kind,triples,notes))
    # page-wide dedupe, preserving first-occurrence order
    seen=set(); all_triples=[]
    for _,_,_,triples,_ in per_sentence:
        for t in triples:
            if t not in seen: seen.add(t); all_triples.append(t)
    annots,aux,canon_only=[],[],[]
    old_ttl=ace_path.rsplit(".",1)[0]+".ttl"
    if merge and os.path.exists(old_ttl):
        annots,aux,canon_only=merge_from_canon(old_ttl,seen)
    # write candidate TTL
    with open(out_path,"w") as f:
        for p,u in PREFIXES: f.write(f"@prefix {p}: <{u}> .\n")
        f.write(f"\n# generated from {os.path.basename(ace_path)} by drs2ttl_v3.py — build artifact, do not hand-edit\n")
        f.write(f"# candidate for {os.path.relpath(old_ttl,REPO)} — promote only after review\n\n")
        if annots:
            f.write("# ── annotations merged from the hand-authored sidecar (no ACE form) ──\n")
            for t in annots: f.write(f"{t[0]} {t[1]} {t[2]} .\n")
            f.write("\n")
        emitted=set()
        for lineno,text,kind,triples,_ in per_sentence:
            new=[t for t in triples if t not in emitted]
            if not new: continue
            f.write(f"# L{lineno}: {text}\n")
            for t in new: emitted.add(t); f.write(f"{t[0]} {t[1]} {t[2]} .\n")
            f.write("\n")
        if aux:
            f.write("# ── auxiliary nodes carried from the hand-authored sidecar ──\n")
            for t in aux: f.write(f"{t[0]} {t[1]} {t[2]} .\n")
            f.write("\n")
        # ── compile report (comments only) ──
        f.write("# ═══ compile report ═══\n")
        for lineno,text,kind,_,notes in per_sentence:
            for cat,detail in notes:
                tally[cat]=tally.get(cat,0)+1
                f.write(f"# L{lineno} [{cat}] {text}\n#      → {detail}\n")
        for w in warns: f.write(f"# WARN {w}\n")
        if canon_only:
            f.write("# canon-only facts (in the hand-authored .ttl, not derivable from the current ACE):\n")
            for t in canon_only: f.write(f"#   {t[0]} {t[1]} {t[2]} .\n")
        if unmapped:
            f.write(f"# UNMAPPED lemmas: {sorted(unmapped)}\n")
    result={"page":stem,"out":out_path,"sentences":len(sents),"triples":len(seen),
            "annots":len(annots),"aux":len(aux),"canon_only":len(canon_only),
            "routed":dict(tally),"warns":warns,"unmapped":sorted(unmapped)}
    # companions (Gap 4): SHACL shapes + SWRL, sharing this process's APE cache
    if shapes:
        import importlib
        prod=importlib.import_module("drs2shacl_prod")
        result["shapes_out"]=out_path.rsplit(".ttl",1)[0]+".shapes.ttl"
        prod.main(ace_path,result["shapes_out"])
    if swrl:
        import importlib
        sw=importlib.import_module("drs2swrl")
        result["swrl_out"]=out_path.rsplit(".ttl",1)[0]+".swrl"
        sw.main(ace_path,result["swrl_out"])
    if not quiet:
        routed=", ".join(f"{k}:{v}" for k,v in sorted(result["routed"].items())) or "-"
        print(f"{stem:56} {result['triples']:4} triples  +{result['annots']} annot +{result['aux']} aux  "
              f"canon-only:{result['canon_only']:3}  routed[{routed}]")
        if unmapped: print(f"    UNMAPPED: {sorted(unmapped)}")
    if strict and unmapped:
        sys.stderr.write("ERROR: unmapped terms (add to lexicon-map.yaml or open a VCR — production does not mint):\n")
        for t in sorted(unmapped): sys.stderr.write(f"  - {t}\n")
        sys.exit(2)
    return result

# ---------- legacy selftest ----------
def selftest():
    n=gen_ulex();results=[];shapes=[];tally={"abox":0,"subclass":0,"enum":0,"constraint":0,"negation":0,"fail":0};parsed=0
    for sid,ace in SENTENCES:
        drs=run_ape(ace)
        if not drs:tally["fail"]+=1;results.append((sid,ace,[],"FAIL"));continue
        parsed+=1;conds=conds_of(parse_drs(drs));triples=[];kind=classify(conds)
        if kind in("subclass","enum","constraint"):handle_tbox(kind,conds,triples,shapes,sid)
        elif kind=="negation":
            triples=[];compile_negation(conds,triples,sid)
        else:compile_abox(conds,triples,sid)
        tally[kind]+=1
        seen,uniq=set(),[]
        for t in triples:
            if t not in seen:seen.add(t);uniq.append(t)
        results.append((sid,ace,uniq,kind))
    out=os.path.join(HERE,"prototype-output.v3.ttl")
    with open(out,"w") as f:
        for p,u in PREFIXES:
            f.write(f"@prefix {p}: <{u}> .\n")
        f.write("\n")
        for sid,ace,triples,kind in results:
            f.write(f"# [{sid}] ({kind}) {ace}\n")
            for s,p,o in triples:f.write(f"{s} {p} {o} .\n")
            f.write("\n")
        if shapes:
            f.write("# ===== SHACL skeletons (constraint sentences — hand-finish) =====\n")
            for sid,txt in shapes:
                f.write(f'{DATA_PREFIX}:shape-s{sid} a sh:NodeShape ;\n    rdfs:comment "TODO full SHACL. Rule: {txt}" .\n\n')
    nt=sum(len(t) for _,_,t,_ in results)
    print(f"ulex generated: {n} entries -> {os.path.basename(GEN_ULEX)}")
    print(f"APE parsed: {parsed}/22   dispatch: {tally}")
    print(f"triples: {nt}   UNMAPPED lemmas: {sorted(unmapped) if unmapped else 'NONE — full map coverage'}")
    print(f"wrote {os.path.basename(out)}")

def main():
    ap=argparse.ArgumentParser(description="DRS→TTL compiler (map-driven). See module docstring for the settled Gap 3/5/6 decisions.")
    ap.add_argument("--input",help="one .ace page to compile")
    ap.add_argument("--output",help="output .ttl (default: <repo>/tmp/drs2ttl/<stem>.generated.ttl)")
    ap.add_argument("--all",action="store_true",help="compile every wiki/**/*.ace")
    ap.add_argument("--in-place",action="store_true",help="write the sibling sidecar .ttl (PROMOTION — only after the candidate diff is reviewed)")
    ap.add_argument("--no-merge",action="store_true",help="skip annotation merge from the hand-authored sidecar")
    ap.add_argument("--no-shapes",action="store_true",help="skip the SHACL companion")
    ap.add_argument("--no-swrl",action="store_true",help="skip the SWRL companion")
    ap.add_argument("--strict",action="store_true",help="hard-error on any unmapped lemma (production gate)")
    ap.add_argument("--existentials",choices=["report","bnode"],default="report",
                    help="generic-Class objects of named subjects: report (default; closed-world-shape safe) or typed bnode (faithful OWL existential)")
    ap.add_argument("--selftest",action="store_true",help="legacy 22-sentence prototype run")
    a=ap.parse_args()
    gen_ulex()
    if a.selftest or (not a.input and not a.all): return selftest()
    pages=[a.input] if a.input else sorted(glob.glob(os.path.join(REPO,"wiki","**","*.ace"),recursive=True))
    total_unmapped=set(); rows=[]
    for p in pages:
        out=a.output
        if a.in_place: out=p.rsplit(".",1)[0]+".ttl"
        r=compile_page(p,out,merge=not a.no_merge,shapes=not a.no_shapes,swrl=not a.no_swrl,strict=a.strict and bool(a.input),existentials=a.existentials)
        rows.append(r); total_unmapped|=set(r["unmapped"])
    if len(pages)>1:
        print(f"\n{len(rows)} pages, {sum(r['triples'] for r in rows)} triples, "
              f"{sum(r['canon_only'] for r in rows)} canon-only facts")
        print(f"UNMAPPED lemmas: {sorted(total_unmapped) if total_unmapped else 'NONE — full map coverage'}")
        if a.strict and total_unmapped: sys.exit(2)

if __name__=="__main__":main()
