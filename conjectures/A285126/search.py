# A285126 / A285127 : 0-limiting word of 0->10, 1->0000 (non Pisot). Recherche de contre-exemples à
# 0 < n*r - a(n) < 1 (positions de 0) et -3 < n*s - b(n) < 0 (positions de 1).
import re, sys
from mpmath import mp, mpf, sqrt
mp.dps = 50
lam = (1 + sqrt(17)) / 2
r = (4 + lam - 1) / 4          # 1 / fréquence de 0  (vecteur propre (4, lam - 1))
s = (4 + lam - 1) / (lam - 1)  # 1 / fréquence de 1
sig = {'0': '10', '1': '0000'}
tau = {x: "".join(sig[y] for y in sig[x]) for x in "01"}        # sigma^2, prolongeable depuis 0
w = "0"
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 3_000_000
while len(w) < NMAX: w = "".join(tau[x] for x in w)
w = w[:NMAX]
def data(a): return [int(x) for x in re.findall(r"-?\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
p0 = [i + 1 for i, x in enumerate(w) if x == "0"]; p1 = [i + 1 for i, x in enumerate(w) if x == "1"]
assert p0[:len(data("A285126"))] == data("A285126") and p1[:len(data("A285127"))] == data("A285127")
print("r =", mp.nstr(r, 20), " s =", mp.nstr(s, 20))
for name, P, x, lo, hi in (("A285126", p0, r, 0, 1), ("A285127", p1, s, -3, 0)):
    first = None; mn = mx = None
    for n, a in enumerate(P, 1):
        D = n * x - a
        if mn is None or D < mn: mn = D
        if mx is None or D > mx: mx = D
        if first is None and not (lo < D < hi): first = (n, a, D)
    print(name, ": premier contre-exemple", (first[0], first[1], mp.nstr(first[2], 15)) if first else None,
          "; min", mp.nstr(mn, 8), "max", mp.nstr(mx, 8), "sur", len(P), "termes")
