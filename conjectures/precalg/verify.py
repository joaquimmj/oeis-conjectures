# Récurrences polynomiales conjecturées (Mathar et al.) pour des f.g. algébriques P(x, A) = 0 : preuve exacte.
# L = Sum_i x^i p_i(theta + i), theta = x d/dx ; L(A) réduit dans Q(x)[Y]/(P) avec Y' = -P_x/P_Y.
# Si L(A) est un polynôme en x de degré < n0, la récurrence vaut pour n >= n0. On vérifie aussi que la série des données
# satisfait P modulo x^N, que P_Y(0, a(0)) != 0 (unicité de la solution série) et la récurrence sur les données.
import json, re, sys, glob
import sympy as sp
from sympy import QQ, Poly
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
TR = standard_transformations + (implicit_multiplication_application,)
x, Y, n = sp.symbols("x Y n")

def parse_rec(line):
    m = re.search(r"(?:[Cc]onjecture[^:]*:|recurrence:?)\s*(.*?)\s*=\s*0", line)
    if not m: return None
    t = m.group(1).replace("recurrence", "").replace("D-finite with", "").strip()
    syms = {}
    def rep(mm):
        k = int(mm.group(2) or 0); syms[k] = sp.Symbol("R%d" % k); return " R%d " % k
    t = re.sub(r"a\(n(-(\d+))?\)", rep, t)
    e = parse_expr(t, local_dict={"n": n, **{str(v): v for v in syms.values()}}, transformations=TR)
    terms = {k: sp.expand(e.coeff(v)) for k, v in syms.items()}
    assert sp.expand(e - sum(terms[k] * syms[k] for k in syms)) == 0
    return terms

def parse_eq(line):
    m = re.search(r"satisf(?:ies|y)\s*:?\s*(.*?)(?:\.\s*-\s*_|\.?\s*$|\s+\[|\s+where|\s+\(personal)", line)
    if not m: return None
    t = m.group(1).strip().rstrip(".")
    if not re.fullmatch(r"[A\(\)x0-9\^\*\+\-/ =]+", t) or t.count("=") != 1: return None
    t = t.replace("A(x)", "Y").replace("^", "**")
    l, r = t.split("=")
    if not l.strip() or not r.strip(): return None
    try: P = sp.numer(sp.together(parse_expr(l, local_dict={"x": x, "Y": Y}) - parse_expr(r, local_dict={"x": x, "Y": Y})))
    except Exception: return None
    return sp.expand(P)

def prove(P, terms, data, n0):
    K = QQ.frac_field(x)
    PP = Poly(P, Y, domain=K)
    if PP.degree() < 1: return "équation sans A"
    if sp.degree(sp.gcd(Poly(P, Y), Poly(sp.diff(P, Y), Y)).as_expr(), Y) > 0: return "P non sans facteur carré"
    PY, Px = PP.diff(Y), Poly(sp.diff(P, x), Y, domain=K)
    dY = (-Px * PY.invert(PP)).rem(PP)
    def deriv(F):
        out = Poly(0, Y, domain=K)
        for (j,), c in F.terms():
            cc = K.to_sympy(c)
            out += Poly(sp.diff(cc, x) * Y**j, Y, domain=K)
            if j: out += Poly(cc * j * Y**(j - 1), Y, domain=K) * dY
        return out.rem(PP)
    L = Poly(0, Y, domain=K)
    for i, p in terms.items():
        q = Poly(sp.expand(p.subs(n, n + i)), n)
        acc, Tk = Poly(0, Y, domain=K), Poly(Y, Y, domain=K)
        for k in range(q.degree() + 1):
            acc += Poly(q.coeff_monomial(n**k), Y, domain=K) * Tk
            Tk = (Poly(x, Y, domain=K) * deriv(Tk)).rem(PP)
        L += Poly(x**i, Y, domain=K) * acc
    L = L.rem(PP)
    if L.degree() > 0: return "L(A) non constant en A"
    c = sp.cancel(K.to_sympy(L.coeff_monomial(1)))
    num, den = sp.fraction(c)
    if not den.is_number: return "L(A) rationnel non polynomial"
    deg = sp.Poly(num, x).degree() if c != 0 else -1
    return ("prouvée pour n >= %d" % (deg + 1)) if deg + 1 <= n0 else "L(A) de degré %d >= n0 = %d" % (deg, n0)

def check_data(P, data, N, off):
    A = sum(sp.Integer(v) * x**(k + off) for k, v in enumerate(data[:N]))
    r = sp.expand(P.subs(Y, A))
    ok = all(r.coeff(x, k) == 0 for k in range(N))
    PY0 = sp.diff(P, Y).subs({x: 0, Y: data[0] if off == 0 else 0})
    return ok, PY0 != 0

if __name__ == "__main__":
    E = {}
    for f in glob.glob("../crawl/raw_*.json"): E.update(json.load(open(f)))
    out = {}
    for a in json.load(open("../crawl/prec_targets.json")):
        e = E[a]; F = e.get("formula") or []
        recs = [l for l in F if re.search(r"[Cc]onjecture", l) and "a(n-1)" in l]
        eqs = [P for l in F if "A(x)" in l and "satisf" in l for P in [parse_eq(l)] if P is not None]
        try: data = [int(v) for v in e["data"].split(",")]
        except Exception: continue
        off = int(e["offset"].split(",")[0])
        if not eqs: print(a, "pas d'équation exploitable"); continue
        for P in eqs:
            ok, uniq = check_data(P, data, min(len(data), 25), off)
            if not ok: print(a, "équation ne colle pas aux données :", str(P)[:60]); continue
            for rl in recs:
                try: terms = parse_rec(rl)
                except Exception as ex: out.setdefault(a, []).append(("analyse impossible", rl[:60])); continue
                if terms is None: continue
                n0 = max(terms)
                res = prove(P, terms, data, n0 + 50)   # A(x) = Sum a(n) x^n avec l'indexation de l'entrée
                # contrôle direct sur les données (indexation de l'entrée)
                direct = all(sum(terms[k].subs(n, m) * data[m - off - k] for k in terms) == 0 for m in range(off + n0, off + len(data)))
                out.setdefault(a, []).append((res, "unicité" if uniq else "P_Y(0)=0", "données OK" if direct else "données KO", str(P)[:70], rl[:70]))
            break
    for a, v in out.items():
        for r in v: print(a, " | ".join(r))
    json.dump(out, open("results.json", "w"), indent=1, ensure_ascii=False)
