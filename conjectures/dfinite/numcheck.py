import json, glob, re, sys
import sympy as sp
exec(open("verify.py").read().split("results = []")[0])
for a in sys.argv[1:]:
    ent = E_[a]; lines = [l for k in ("comment", "formula") for l in (ent.get(k) or [])]
    rec = parse_rec([l for l in lines if re.search(r"Conjecture:?\s*D-finite", l)][0])
    A = next(parse_gf(g) for g in lines if re.match(r"\s*G\.f\.?:", g) and parse_gf(g) is not None)
    off = int(ent["offset"].split(",")[0]); N = int(__import__("os").environ.get("NN", "60"))
    ser = sp.series(A, x, 0, N).removeO(); t = {m: ser.coeff(x, m) for m in range(N)}
    data = [int(q) for q in ent["data"].split(",")]
    cst = rec.pop("c", 0); r = max(rec)
    bad = [m for m in range(off + r, N) if sum(rec[k].subs(n, m) * t[m - k] for k in rec) + cst.subs(n, m) != 0]
    print(a, "données", [t[off + i] for i in range(len(data))] == data, "; ordre", r, "; n en défaut (n<120) :", bad[:8], "nb", len(bad))
