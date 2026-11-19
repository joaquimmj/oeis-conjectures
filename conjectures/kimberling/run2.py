# Deuxième série de conjectures de Kimberling (mots limites) : construction automatique des cas et calcul exact.
import sys, re
sys.path.insert(0, "../../python")
from fractions import Fraction as Fr
from math import isqrt
from discrepancy_exact import Q, analyse, dt_check
P0 = "../phase0/"
def txt(a): return open(P0 + a + ".txt").read()
def data(a): return [int(x) for x in re.findall(r"-?\d+", "".join(l[11:] for l in open(P0 + a + ".txt") if l[:2] in ("%S", "%T", "%U")))]
def sqfree(D):
    k = 1
    for p in range(2, isqrt(abs(D)) + 1):
        while D % (p * p) == 0: D //= p * p; k *= p
    return k, D
def exact_r(sigma, L):
    M = [[sigma[j].count(str(i)) for j in "01"] for i in "01"]            # M[i][j] = |sigma(j)|_i
    t, det = M[0][0] + M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0]
    k, d = sqfree(t * t - 4 * det)
    lam = Q(Fr(t, 2), Fr(k, 2), d)                                         # (t + sqrt(D))/2
    v = [Q(M[0][1], 0, d), lam - M[0][0]]                                  # vecteur propre (colonnes)
    return (v[0] + v[1]) / v[int(L)]
def parse_bounds(line):
    m = re.search(r"([-+]?[0-9./]*(?:\s*[-+]\s*)?(?:sqrt\(\d+(?:/\d+)?\))?)\s*<\s*n\s*\*?\s*r\s*-\s*a\(n\)\s*<\s*([-+0-9./()r* ]*(?:sqrt\(\d+(?:/\d+)?\))?[-+0-9./()r* ]*?)\s*(?:for|,|;|\.\s|$)", line)
    ev = lambda s: float(eval(s.replace("sqrt", "__import__('math').sqrt"), {}))
    nr = lambda s, v: re.sub(r"\br\b", v, s)
    return m.group(1), m.group(2), ev(m.group(1)), (ev(m.group(2)) if not re.search(r"\br\b", m.group(2)) else None)
targets = (sys.argv[1:] or "A026367 A284654 A284675 A284676 A284678 A284679 A285032 A285035 A285036 A285082 A285084 A285275 A285278 A285419".split())
for a in targets:
    T = txt(a)
    conj = next((l[11:] for l in T.split("\n") if l.startswith("%") and "onjecture" in l and re.search(r"n\s*\*?\s*r\s*-\s*a\(n\)", l)), None)
    if conj is None: print(a, ": énoncé non trouvé"); continue
    if a == "A026367":
        sigma, c, L = {'0': '11', '1': '110'}, '1', '1'
    else:
        base = re.search(r"in (A\d{6})", next(l for l in T.split("\n") if l.startswith("%N"))).group(1)
        N = next(l for l in txt(base).split("\n") if l.startswith("%N"))
        m = re.search(r"0\s*->\s*([01]+),\s*1\s*->\s*([01]+)", N); sigma = {'0': m.group(1), '1': m.group(2)}
        c = re.search(r"([01])-limiting", N).group(1) if "limiting" in N else None
        L = re.search(r"Positions of ([01])", T).group(1)
        if c is None: c = sigma['0'][0]
        if sigma[c][0] != c: sigma = {x: "".join(sigma[y] for y in sigma[x]) for x in "01"}   # sigma^2
    r = exact_r(sigma, L)
    w = c
    while len(w) < 6000: w = "".join(sigma[x] for x in w)
    pos = [i + 1 for i, x in enumerate(w) if x == L]; dd = data(a)
    ok = pos[:len(dd)] == dd
    lo_s, hi_s, lo, hi = parse_bounds(conj)
    if hi is None: hi = float(eval(re.sub(r"\br\b", str(float(r)), hi_s).replace("sqrt", "__import__('math').sqrt")))
    lam2 = (Q(Fr(sum(sigma[x].count(x) for x in '01'), 2), 0, r.d) - (Q(0, 0, r.d)))  # (contrôle Pisot ci-dessous)
    try:
        res = analyse(sigma, c, L, r, verbose=False); mn, mx = dt_check(sigma, c, L, r, res)
    except AssertionError:
        D = [float(r) * n - p for n, p in enumerate(pos, 1)]
        bad = next(((n, p, d) for n, (p, d) in enumerate(zip(pos, D), 1) if not (lo < d < hi)), None)
        print(f"{a}: NON PISOT (tau = {sigma} depuis {c}, lettre {L}, r ≈ {float(r):.6f}) ; premier contre-exemple : {bad} ; conjecture {lo_s} < D < {hi_s}")
        continue
    inf, sup = res['inf'], res['sup']
    vl = 'TRUE' if float(inf) > lo + 1e-12 else ('ÉGALITÉ' if abs(float(inf) - lo) < 1e-9 else 'FALSE')
    vh = 'TRUE' if float(sup) < hi - 1e-12 else ('ÉGALITÉ' if abs(float(sup) - hi) < 1e-9 else 'FALSE')
    print(f"{a}: tau = {sigma} depuis {c}, lettre {L}, r = {r} ≈ {float(r):.6f} ; indexation {'OK' if ok else 'À REVOIR'}")
    print(f"   inf = {inf} ≈ {float(inf):.6f}, sup = {sup} ≈ {float(sup):.6f} (observé {mn:.4f} .. {mx:.4f})")
    print(f"   conjecture {lo_s} < D < {hi_s} : inf {vl}, sup {vh}   [{conj.strip()[:90]}]")
