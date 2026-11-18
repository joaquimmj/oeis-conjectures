# Tri des entrées crawlées : conjectures sans signe de résolution, scorées impact + faisabilité.
import json, glob, re
E_ = {}
for f in glob.glob("raw_*.json"): E_.update(json.load(open(f)))
DONE = set("A347171 A366860 A366870 A366871 A371176 A118006 A007413 A005590 A357097 A358360 A161580 A070864 A112310 A055246 A161579 A161817 A162311 A178482 A144611 A285383".split())
RESOLVED = re.compile(r"\b(proved|proven|proof|theorem|is true|is false|not true|counterexample|walnut|confirmed|disproved|settled|resolved|established)\b", re.I)
FAMOUS = re.compile(r"_(N\. J\. A\. Sloane|Richard K\. Guy|Donald E\. Knuth|Doron Zeilberger|Richard P\. Stanley|John H\. Conway|Ron(ald)? ?L\.? Graham|Paul Erd|Jeffrey Shallit|Jean-Paul Allouche|Michel Dekking|Neil J\. A\. Sloane|Peter J\. Cameron|Christian Krattenthaler|Ira M\. Gessel|Michael Somos)", re.I)
FEAS = re.compile(r"(automatic|2-regular|3-regular|k-regular|morphism|fixed point|Fibonacci word|Thue-Morse|paperfolding|Stern|Zeckendorf|g\.f\.|generating function|recurrence|holonomic|D-finite|binary expansion)", re.I)
rows = []
for a, e in E_.items():
    if a in DONE: continue
    lines = [(k, l) for k in ("comment", "formula") for l in (e.get(k) or [])]
    conj = [l for k, l in lines if re.search(r"conjectur", l, re.I)]
    if not conj: continue
    txt = " ".join(l for _, l in lines)
    if RESOLVED.search(txt): continue
    kw = e.get("keyword", "")
    imp = 3 * ("nice" in kw) + 3 * ("core" in kw) + 2 * bool(any(FAMOUS.search(c) for c in conj)) + min(len(e.get("reference") or []), 4) + min(sum("arxiv" in l.lower() or "doi" in l.lower() for l in e.get("link") or []), 4) / 2
    fea = min(len(FEAS.findall(" ".join(conj) + " " + e["name"])), 3)
    yr = [int(y) for c in conj for y in re.findall(r"(?:19|20)\d\d", c)]
    age = (2026 - min(yr)) / 10 if yr else 0
    rows.append((imp + fea + age, imp, fea, a, kw, e["name"][:90], conj[0][:260]))
rows.sort(reverse=True)
json.dump(rows, open("ranked.json", "w"))
print(len(E_), "entrées crawlées ;", len(rows), "avec conjecture apparemment ouverte")
for r in rows[:70]: print(f"{r[0]:5.1f} imp={r[1]:4.1f} fea={r[2]} {r[3]} [{r[4][:30]}] {r[5]}\n      {r[6]}")
