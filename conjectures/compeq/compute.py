# Équations complémentaires de Kimberling a(n) = Σ c_i a(n-i) + g(b(...), n) : calcul depuis la définition,
# comparaison aux données OEIS, et vérification des hypothèses du théorème de proof.md pour chaque entrée.
import json, re, sys
import sympy as sp

E = json.load(open("entries.json"))
N_TERMS = 400

def parse(name):
    rhs = re.search(r"a\(n\) = (.*?), where", name).group(1)
    init = {(m[0], int(m[1])): int(m[2]) for m in re.findall(r"([ab])\((\d+)\) = (\d+)", name)}
    py = re.sub(r"(\d)n", r"\1*n", rhs).replace("^", "**").replace(" n*", " n*")
    return rhs, init, py

def solve(py, init, nterms=N_TERMS):
    a = [init[("a", i)] for i in range(10) if ("a", i) in init]
    n0 = len(a)
    used_b = []
    for n in range(n0, nterms):
        aset = set(a)
        bl, k = [], 0
        def b(j):
            # j-ième entier positif hors de {a(0..n-1)} (provisoire : validé ensuite par a(n) > b(j))
            nonlocal k
            while len(bl) <= j:
                k += 1
                if k not in aset: bl.append(k)
            used_b.append((n, j, bl[j]))
            return bl[j]
        an = eval(py, {"n": n, "a": lambda i: a[i], "b": b})
        assert an > a[-1], (n, an)
        assert all(an > v for (m, j, v) in used_b if m == n), "a(n) <= b provisoire"
        a.append(an)
    for (key, v) in init.items():           # les b initiaux doivent être ceux du complément
        if key[0] == "b":
            comp = [x for x in range(1, 100) if x not in set(a)]
            assert comp[key[1]] == v, (key, v, comp[:6])
    return a

def gsym(py):
    # g(n) symbolique : b(n+j) = n + j + 1 + u_j, u croissante (b(k+1) >= b(k)+1, b(0) >= 1)
    n = sp.Symbol("n")
    shifts = sorted({int(s or 0) for s in re.findall(r"b\(n([+-]\d+)?\)", py.replace(" ", ""))})
    t = sp.symbols("t0:%d" % max(1, len(shifts)), nonnegative=True)
    u = {}
    acc = 0
    for i, s in enumerate(shifts):
        acc = acc + t[i]; u[s] = acc
    arec = re.sub(r"a\(n-\d\)", "0", py)
    g = eval(arec, {"n": n, "a": None, "b": lambda e: (lambda s: n + s + 1 + u[s])(sp.simplify(e - n))})
    return sp.expand(g), n, t

def lower_const(py, n0):
    # si, après n = n0 + m, tous les coefficients non constants sont >= 0 : g(n) >= constante pour n >= n0
    g, n, t = gsym(py)
    m = sp.Symbol("m", nonnegative=True)
    P = sp.Poly(sp.expand(g.subs(n, m + n0)), m, *t)
    const = P.coeff_monomial(1)
    ok = all(c >= 0 for mon, c in P.terms() if any(mon))
    return ok, const

def charpoly(py):
    x = sp.Symbol("x")
    shifts = [int(s) for s in re.findall(r"a\(n-(\d)\)", py)]
    coef = {}
    for s in shifts: coef[s] = coef.get(s, 0) + 1
    for m in re.finditer(r"(\d)\*a\(n-(\d)\)", py): coef[int(m[2])] += int(m[1]) - 1
    k = max(coef)
    return sp.expand(x**k - sum(c * x**(k - s) for s, c in coef.items())), coef

if __name__ == "__main__":
    phi = (1 + sp.sqrt(5)) / 2
    rows = []
    for A, e in sorted(E.items()):
        rhs, init, py = parse(e["name"])
        a = solve(py, init)
        data = [int(v) for v in e["data"].split(",")]
        assert a[:len(data)] == data, A
        P, coef = charpoly(py)
        n0 = len([1 for k in init if k[0] == "a"])
        ok, C = lower_const(py, n0)
        # croissance : a(n) - K >= Σ c_i (a(n-i) - K) dès que g >= -C, avec K = C/(Σc_i - 1) ; certificat : k termes consécutifs > K
        S = sum(coef.values())
        K = sp.Rational(max(0, -C), S - 1) if ok else None
        k = max(coef)
        Nc = next((i for i in range(k, len(a)) if ok and all(a[j] > K for j in range(i - k, i))), None)
        r = float(a[-1]) / float(a[-2])
        rows.append(dict(A=A, rhs=rhs, P=str(sp.factor(P)), lower_ok=bool(ok), C=int(C), base=Nc, ratio=r,
                         conj=any("onjectur" in l for l in e.get("comment") or [])))
        print(A, rhs, "| P =", sp.factor(P), "| g>=", C if ok else "NON", "| base", Nc, "| ratio-phi %.1e" % (r - float(phi)))
    json.dump(rows, open("results.json", "w"), indent=1)
    print(len(rows), "entrées ;", sum(r["conj"] for r in rows), "étiquetées « Conjecture »")
