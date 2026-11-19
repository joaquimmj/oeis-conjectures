# Conjectures « D-finite with recurrence » (Mathar…) pour des séries génératrices algébriques explicites à un seul
# radical : vérification EXACTE dans Q(x)[s]/(s^2 - Delta) que l'opérateur différentiel associé annule la série,
# à un polynôme près (=> la récurrence vaut pour n > deg), puis contrôle direct des petits n sur les termes.
import json, glob, re, sys
import sympy as sp
x, n, s = sp.symbols("x n s")
E_ = {}
for f in glob.glob("../crawl/raw_*.json"): E_.update(json.load(open(f)))
def parse_gf(line):
    e = re.sub(r"\s*-\s*_[^_]+_.*$", "", line.split(":", 1)[1]).strip().rstrip(".")
    e = e.replace("^", "**")
    if re.search(r"[A-Za-z]{2,}", e.replace("sqrt", "")): return None
    try: return sp.sympify(e, locals={"x": x})
    except Exception: return None
def radicand(expr):
    rads = set()
    for p in expr.atoms(sp.Pow):
        if p.exp.is_Rational and p.exp.q == 2: rads.add(sp.cancel(p.base))
    return rads
def to_pair(expr, D):
    # écrit expr = u + v*sqrt(D) avec u, v dans Q(x)
    rep = {p: s ** int(2 * p.exp) for p in expr.atoms(sp.Pow) if p.exp.is_Rational and p.exp.q == 2 and sp.cancel(p.base - D) == 0}
    e = expr.xreplace(rep)
    e = sp.together(e)
    num, den = sp.fraction(e)
    num, den = sp.Poly(sp.expand(num), s), sp.Poly(sp.expand(den), s)
    def red(p):
        a = b = 0
        for (k,), c in p.terms():
            if k % 2 == 0: a += c * D ** (k // 2)
            else: b += c * D ** (k // 2)
        return sp.cancel(a), sp.cancel(b)
    a, b = red(num); c, d = red(den)              # (a + b s)/(c + d s) = ((a + b s)(c - d s))/(c^2 - d^2 D)
    N0 = c * c - d * d * D
    return sp.cancel((a * c - b * d * D) / N0), sp.cancel((b * c - a * d) / N0)
def theta(u, v, D):
    return sp.cancel(x * sp.diff(u, x)), sp.cancel(x * (sp.diff(v, x) + v * sp.diff(D, x) / (2 * D)))
def parse_rec(line):
    m = re.search(r"recurrence:?\s*(.+?)\s*=\s*0", line)
    if not m: return None
    t = m.group(1).replace(" ", "")
    t = re.sub(r"a\(n\)", "A0", t); t = re.sub(r"a\(n-(\d+)\)", r"A\1", t)
    t = re.sub(r"(\d|\))A", r"\1*A", t)
    try: e = sp.expand(sp.sympify(t.replace("^", "**"), locals={"n": n}))
    except Exception: return None
    syms = sorted([q for q in e.free_symbols if str(q).startswith("A")], key=lambda q: int(str(q)[1:]))
    out = {int(str(q)[1:]): sp.expand(e.coeff(q)) for q in syms}
    out["c"] = sp.expand(e.subs({q: 0 for q in syms}))
    return out
results = []
for a, ent in sorted(E_.items()):
    lines = [l for k in ("comment", "formula") for l in (ent.get(k) or [])]
    rl = [l for l in lines if re.search(r"Conjecture:?\s*D-finite", l)]
    gl = [l for l in lines if re.match(r"\s*G\.f\.?:", l)]
    if not rl or not gl: continue
    rec = parse_rec(rl[0])
    if not rec: continue
    for g in gl:
        A = parse_gf(g)
        if A is None: continue
        R = radicand(A)
        if len(R) != 1: continue
        D = R.pop()
        try:
            u, v = to_pair(A, D)
            Phi_u, Phi_v = 0, 0
            cst = rec.pop("c", 0)
            for k, pk in rec.items():
                pc = sp.Poly(pk.subs(n, n), n).all_coeffs()[::-1]     # p_k(theta + k) appliqué à (u, v)
                acc_u, acc_v, tu, tv = 0, 0, u, v
                for j, cj in enumerate(sp.Poly(sp.expand(pk.subs(n, n + k)), n).all_coeffs()[::-1]):
                    if j > 0: tu, tv = theta(tu, tv, D)
                    acc_u += cj * tu; acc_v += cj * tv
                Phi_u += x ** k * acc_u; Phi_v += x ** k * acc_v
            if cst != 0:   # + sum_{n>=0} c(n) x^n (fraction rationnelle), c polynôme en n
                cp = sp.Poly(cst, n).all_coeffs()[::-1]; G = 1 / (1 - x)
                tot = 0
                for j, cj in enumerate(cp):
                    tot += cj * G; G = sp.cancel(x * sp.diff(G, x))
                Phi_u += tot
            Phi_u, Phi_v = sp.cancel(Phi_u), sp.cancel(Phi_v)
            if Phi_v != 0 or sp.fraction(Phi_u)[1].free_symbols: results.append((a, "NON", "")); break
            deg = sp.Poly(Phi_u, x).degree() if Phi_u != 0 else -1
            # contrôle des petits n : termes de la série vs données de l'entrée, et récurrence pour n <= deg
            data = [int(t) for t in ent["data"].split(",")]
            off = int(ent["offset"].split(",")[0])
            ser = sp.series(A, x, 0, off + len(data)).removeO()
            terms = [ser.coeff(x, off + i) for i in range(len(data))]
            ok_data = terms == data
            r = max(rec)
            small = [m for m in range(off + r, min(deg, off + len(terms) - 1) + 1) if sum(rec[k].subs(n, m) * terms[m - k - off] for k in rec) + cst.subs(n, m) != 0]
            results.append((a, "OUI" if ok_data else "DONNÉES?", f"Phi polynôme de degré {deg} ; récurrence pour n > {deg} ; petits n en défaut : {small[:5]}"))
            break
        except Exception as ex:
            results.append((a, "ERREUR", str(ex)[:80])); break
for row in results: print(*row)
