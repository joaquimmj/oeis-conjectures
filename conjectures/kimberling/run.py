# Conjectures de discrépance de Kimberling (hors article), avec l'outil exact du dépôt (python/discrepancy_exact.py).
import sys, re
sys.path.insert(0, "../../python")
from fractions import Fraction as Fr
from discrepancy_exact import Q, analyse, dt_check
def data(a): return [int(x) for x in re.findall(r"-?\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
CASES = [  # entrée, morphisme, départ, lettre, r = (p + q sqrt d)/den, bornes conjecturées
 ("A026363", {'0': '11', '1': '101'}, '1', '1', (1, 1, 3, 2), (-1, 2)),
 ("A026364", {'0': '11', '1': '101'}, '1', '0', (2, 1, 3, 1), (-1, 4)),
 ("A026368", {'0': '11', '1': '110'}, '1', '0', (2, 1, 3, 1), (-2, 4)),
 ("A284753", {'0': '01', '1': '0001'}, '0', '1', (1, 1, 3, 1), (-2, 3)),
 ("A284894", {'0': '01', '1': '0111'}, '0', '0', (2, 1, 2, 1), (2, 6)),
 ("A285669", {'0': '11', '1': '1101'}, '1', '0', (5, 1, 17, 2), (-1, 4)),
]
for a, sigma, start, L, (p, q, d, den), (lo, hi) in CASES:
    w = start
    while len(w) < 5000: w = "".join(sigma[c] for c in w)
    pos = [i + 1 for i, c in enumerate(w) if c == L]
    dd = data(a); off = next((s for s in range(-2, 3) if pos[:len(dd) - 2] == [x + s for x in dd[:len(dd) - 2]] or pos[:len(dd)] == [x + s for x in dd]), None)
    print(f"{a}: positions 1-indexées = données de l'entrée {'(décalage %+d)' % off if off else ''}" if off is not None else f"{a}: INDEXATION À REVOIR {pos[:10]} vs {dd[:10]}")
    r = Q(Fr(p, den), Fr(q, den), d)
    res = analyse(sigma, start, L, r, verbose=False)
    mn, mx = dt_check(sigma, start, L, r, res)
    sup, inf = res['sup'], res['inf']
    up = 'TRUE' if sup < hi else ('FALSE' if sup > hi else 'ÉGALITÉ')
    dn = 'TRUE' if inf > lo else ('FALSE' if inf < lo else 'ÉGALITÉ')
    print(f"   r = {r} ; inf = {inf} ≈ {float(inf):.6f} ; sup = {sup} ≈ {float(sup):.6f} ; observé {mn:.5f} .. {mx:.5f}")
    print(f"   conjecture {lo} < n r - a(n) < {hi} : borne inf {dn}, borne sup {up}")
