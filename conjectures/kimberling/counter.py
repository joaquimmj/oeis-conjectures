# Contre-exemples explicites (arithmétique exacte dans Q(sqrt d)) pour les conjectures de Kimberling fausses,
# avec le r ÉNONCÉ dans l'entrée ; et contrôle d'atteinte en n = 1 pour A285078.
import sys, re
sys.path.insert(0, "../../python")
from fractions import Fraction as Fr
from discrepancy_exact import Q
def data(a): return [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
def word(sig, c, N=200000):
    if sig[c][0] != c: sig = {x: "".join(sig[y] for y in sig[x]) for x in "01"}
    w = c
    while len(w) < N: w = "".join(sig[x] for x in w)
    return w
CASES = [  # entrée, sigma, lettre limite, lettre comptée, r énoncé (p, q, d, den), bornes (lo, hi) avec sqrt éventuel
 ("A285134", {'0': '10', '1': '0001'}, '0', '0', (3, 1, 3, 3), (Q(-1, 0, 3), Q(1, 0, 3))),
 ("A285135", {'0': '10', '1': '0001'}, '0', '1', (1, 1, 3, 1), (Q(-1, 0, 3), Q(1, 0, 3))),
 ("A285137", {'0': '10', '1': '0001'}, '1', '0', (3, 1, 3, 3), (Q(-1, 0, 3), Q(1, 0, 3))),
 ("A285138", {'0': '10', '1': '0001'}, '1', '1', (1, 1, 3, 1), (Q(-1, 0, 3), Q(0, 1, 3))),
 ("A285140", {'0': '10', '1': '0010'}, '0', '0', (3, 1, 3, 3), (Q(-1, 0, 3), Q(1, 0, 3))),
 ("A285141", {'0': '10', '1': '0010'}, '0', '1', (1, 1, 3, 1), (Q(-1, 0, 3), Q(1, 0, 3))),
 ("A285143", {'0': '10', '1': '0010'}, '1', '0', (3, 1, 3, 3), (Q(-1, 0, 3), Q(1, 0, 3))),
 ("A285144", {'0': '10', '1': '0010'}, '1', '1', (1, 1, 3, 1), (Q(-1, 0, 3), Q(0, 1, 3))),
 ("A285279", {'0': '10', '1': '0111'}, '1', '1', (2, 1, 2, 1), (Q(0, 0, 2), Q(6, 0, 2))),
 ("A285078", {'0': '10', '1': '010'}, '1', '1', (1, 1, 2, 1), (Q(-1, 1, 2), Q(0, 1, 2))),
]
for a, sig, c, L, (p, q, d, den), (lo, hi) in CASES:
    w = word(sig, c); pos = [i + 1 for i, x in enumerate(w) if x == L]; dd = data(a)
    assert pos[:len(dd)] == dd, a
    r = Q(Fr(p, den), Fr(q, den), d)
    bad = None
    for n, x in enumerate(pos, 1):
        D = r * n - x
        if not (lo < D and D < hi): bad = (n, x, D, float(D)); break
    print(f"{a}: r = {r} ; premier n avec D hors de ({lo}, {hi}) : " + (f"n = {bad[0]}, a(n) = {bad[1]}, D = {bad[2]} ≈ {bad[3]:.6f}" if bad else "aucun"))
