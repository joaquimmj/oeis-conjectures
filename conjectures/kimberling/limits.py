# Conjectures « a(n)/n -> m » de Kimberling sur des mots morphiques : limite exacte = 1/fréquence (Perron) pour
# une substitution primitive, comparée symboliquement (sympy) à la limite énoncée. Cas (a) et (b).
import re, sys
import sympy as sp
P0 = "../phase0/"
def txt(a): return open(P0 + a + ".txt").read()
def data(a): return [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(P0 + a + ".txt") if l[:2] in ("%S", "%T", "%U")))]
def morph(base):
    N = next(l for l in txt(base).split("\n") if l.startswith("%N"))
    m = re.search(r"of the morphism\s*0\s*->\s*([01]+),\s*1\s*->\s*([01]+)", N)
    if not m: return None
    sig = {'0': m.group(1), '1': m.group(2)}
    c = re.search(r"([01])-limiting", N)
    c = c.group(1) if c else sig['0'][0] if sig['0'][0] == '0' else sig['1'][0]
    if "Fixed point" in N: c = '0' if sig['0'][0] == '0' else '1'
    return sig, c
def word(sig, c, N=300000):
    if sig[c][0] != c: sig = {x: "".join(sig[y] for y in sig[x]) for x in "01"}
    w = c
    while len(w) < N: w = "".join(sig[x] for x in w)
    return w[:N]
def perron_r(sig, L):
    M = sp.Matrix([[sig[j].count(i) for j in "01"] for i in "01"])
    assert all(x > 0 for x in (M ** 2)) or all(x > 0 for x in (M ** 3)), "non primitive"
    lam = max(M.eigenvals(), key=lambda e: float(sp.re(e)))
    v = (M - lam * sp.eye(2)).nullspace()[0]
    return sp.nsimplify(sp.simplify((v[0] + v[1]) / v[int(L)]))
def parse_lim(s):
    m = re.search(r"a\(n\)\s*/\s*n\s*->\s*((?:sqrt|[0-9+\-*/(). ])+)", s)
    e = m.group(1).strip()
    num = "..." in e
    e = e.replace("...", "").rstrip(". ")
    while e.count(")") > e.count("("): e = e[:-1].rstrip()
    if num or re.fullmatch(r"\d+\.\d+", e): return None, float(e)
    return sp.sympify(e), None
rows = []
for a in [x.strip() for x in open("limit_targets.txt")]:
    T = txt(a)
    conj = next(l[11:] for l in T.split("\n") if l.startswith("%") and re.search(r"onjecture[^.]*a\(n\)/n\s*->", l))
    base = re.search(r"in (A\d{6})", next(l for l in T.split("\n") if l.startswith("%N")))
    L = re.search(r"Positions of ([01])", T)
    if not base or not L: rows.append((a, "?", "définition non reconnue")); continue
    base, L = base.group(1), L.group(1)
    N = next(l for l in txt(base).split("\n") if l.startswith("%N"))
    pairs = re.search(r"\{00->0, 11->1\}-transform of (A\d{6})", N)
    src = pairs.group(1) if pairs else base
    mc = morph(src)
    if mc is None: rows.append((a, "autre", N[11:80])); continue
    sig, c = mc; w = word(sig, c)
    if pairs:
        if not all(w[i] == w[i + 1] for i in range(0, len(w) - 1, 2)): rows.append((a, "autre", "transformée non alignée")); continue
        w = w[::2]
    pos = [i + 1 for i, x in enumerate(w) if x == L]; d = data(a)
    if pos[:len(d)] != d: rows.append((a, "INDEX", "positions ≠ données")); continue
    r = perron_r(sig, L)
    lim, num = parse_lim(conj)
    ok = (sp.simplify(r - lim) == 0) if lim is not None else abs(float(r) - num) < 10 ** -(len(str(num).split(".")[1]) - 0.5) * 5
    extra = " [+bornes]" if re.search(r"<\s*m\s*-|<\s*[\w(+\-.]+\s*-\s*a\(n\)/n", conj) else ""
    rows.append((a, "VRAIE" if ok else "FAUSSE", f"r = {r} ≈ {float(r):.6f} ; énoncé {lim if lim is not None else num} ; observé {pos[-1]/len(pos):.5f}{extra}"))
for row in rows: print(*row)
