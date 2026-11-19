# Contrôle indépendant de compute.py : autre générateur (crible + pointeur, formule via sympy.sympify),
# puis vérifications numériques des étapes de la preuve (proof.md) pour chacune des 90 entrées.
import json, re
import sympy as sp
from mpmath import mp, mpf, sqrt
mp.dps = 400  # a(600) a ~125 chiffres : il faut bien plus pour e(n) = a(n) - phi a(n-1)
E = json.load(open("entries.json"))
PHI = (1 + sqrt(5)) / 2
n_, A_, B_ = sp.symbols("n"), sp.Function("a"), sp.Function("b")

def gen(name, N=600):
    rhs = re.search(r"a\(n\) = (.*?), where", name).group(1)
    rhs = re.sub(r"(\d)n", r"\1*n", rhs)
    expr = sp.sympify(rhs, locals={"a": A_, "b": B_, "n": n_})
    f = sp.lambdify([n_, A_, B_], expr, modules=[{"a": None, "b": None}])
    a = [int(v) for _, v in sorted((int(i), v) for i, v in re.findall(r"a\((\d+)\) = (\d+)", name))]
    mark = bytearray(10**6)
    for v in a: mark[v] = 1
    for n in range(len(a), N):
        bl, p = [], 0
        def b(j):
            nonlocal p
            while len(bl) <= j:
                p += 1
                if not mark[p]: bl.append(p)
            return bl[j]
        v = int(f(n, lambda i: a[int(i)], lambda j: b(int(j))))
        assert v > a[-1] and v > max(bl or [0])
        a.append(v)
        if v < len(mark): mark[v] = 1
    return a, expr

bad = 0
for A, e in sorted(E.items()):
    a, expr = gen(e["name"])
    data = [int(v) for v in e["data"].split(",")]
    ok_data = a[:len(data)] == data
    # croissance exponentielle et e(n) = a(n) - phi a(n-1) = O(n^(D+1)) ; rapport -> phi
    D = sp.Poly(expr.subs({A_(n_ - k): 0 for k in range(1, 5)}).replace(B_, lambda x: n_), n_).degree()
    en = [abs(mpf(a[n]) - PHI * a[n - 1]) for n in range(10, len(a))]
    ok_e = max(float(en[i]) / (i + 10) ** (D + 1) for i in range(len(en))) < 50
    ok_r = abs(mpf(a[-1]) / a[-2] - PHI) < mpf(10) ** -80
    if A == "A294413":   # base de la récurrence H(n): a(n) >= 4n, et d = a - 2n - 6 > 0
        assert a[5] >= 20 and a[6] >= 24 and a[5] - 16 > 0 and a[6] - 18 > 0
        assert all(a[n] >= 4 * n for n in range(5, len(a)))
    print(A, "données", ok_data, "| e(n)=O(n^%d)" % (D + 1), ok_e, "| |a(N)/a(N-1)-phi|<1e-80", ok_r)
    bad += not (ok_data and ok_e and ok_r)
print("échecs :", bad)
