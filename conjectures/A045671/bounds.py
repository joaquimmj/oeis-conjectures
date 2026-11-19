# A045671 / A045672 : bornes exactes de D(n) = n r - a(n) (outil exact du lot 6, python/discrepancy_exact.py)
# pour les positions des 1 (resp. des 0) du point fixe de 0 -> 11, 1 -> 1110 commençant par 1.
import sys
sys.path.insert(0, "../../python"); sys.path.insert(0, "../kimberling")
from discrepancy_exact import analyse, dt_check
from fractions import Fraction as Fr
import importlib.util
spec = importlib.util.spec_from_file_location("r2", "../kimberling/run2.py")
src = open("../kimberling/run2.py").read().split("targets = ")[0]
ns = {}; exec(src, ns)
exact_r = ns["exact_r"]
sigma = {"0": "11", "1": "1110"}
for name, L, lo, hi in (("A045671", "1", -1, 2), ("A045672", "0", -1, 3)):
    r = exact_r(sigma, L)
    res = analyse(sigma, "1", L, r, verbose=False); mn, mx = dt_check(sigma, "1", L, r, res)
    inf, sup = res["inf"], res["sup"]
    print(f"{name}: r = {r} ≈ {float(r):.6f} ; inf = {inf} ≈ {float(inf):.6f} ; sup = {sup} ≈ {float(sup):.6f} ; "
          f"observé {mn:.4f}..{mx:.4f} ; conjecture {lo} < D < {hi} : {float(inf) > lo and float(sup) < hi}")
