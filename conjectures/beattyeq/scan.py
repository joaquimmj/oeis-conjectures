from gen import gen
from mpmath import mp, mpf, sqrt
mp.dps = 30
import sys
N = int(sys.argv[1])
F = {  # entrée : (s, c, d, qui, alpha, bas, haut) ; bornes strictes sauf indication
 "A297830": (1, 2, 0, "a", 2 + sqrt(2), None, None),
 "A297831": (1, 2, -1, "a", 2 + sqrt(2), None, mpf(5) / 2),
 "A297833": (1, 2, -3, "a", 2 + sqrt(2), -2, 1),
 "A297834": (1, 2, -4, "a", 2 + sqrt(2), -3, 1),
 "A297835": (1, 2, 1, "a", 2 + sqrt(2), None, 7),
 "A297836": (1, 3, 0, "a", (5 + sqrt(13)) / 2, None, 2),
 "A297837": (1, 4, 0, "a", 3 + sqrt(5), None, 3),
 "A298000": (0, 2, 0, "a", 2 + sqrt(2), None, 4),
 "A298001": (0, 3, 0, "a", (5 + sqrt(13)) / 2, None, 4),
 "A298002": (0, 4, 0, "a", 3 + sqrt(5), None, 4),
 "A298003": (1, 2, 0, "b", sqrt(2), mpf(3) / 5, 3),
 "A298004": (1, 3, 0, "b", (-1 + sqrt(13)) / 2, mpf(7) / 10, 3),
 "A298005": (1, 4, 0, "b", -1 + sqrt(5), mpf(7) / 10, 3),
 "A298006": (1, 2, -1, "b", sqrt(2), mpf(9) / 10, 3),
 "A298007": (1, 2, -2, "b", sqrt(2), 1, 3),
 "A298108": (1, 2, -3, "b", sqrt(2), mpf(3) / 2, 4),
 "A298109": (1, 2, -4, "b", sqrt(2), mpf(3) / 2, 4),
 "A298111": (0, 2, 0, "b", sqrt(2), mpf(1) / 5, 3),
 "A298112": (0, 3, 0, "b", sqrt(2), mpf(2) / 5, 3),
 "A298113": (0, 4, 0, "b", sqrt(2), mpf(1) / 2, 3),
}
import json, glob
E = {}
for f in glob.glob("../crawl/raw_*.json"): E.update(json.load(open(f)))
for A, (s, c, d, who, al, lo, hi) in F.items():
    a, b = gen(s, c, d, N)
    seq = a if who == "a" else b
    data = [int(v) for v in E[A]["data"].split(",")]
    off = int(E[A]["offset"].split(",")[0])
    ok = seq[off:off + len(data)] == data if off == 0 else seq[:len(data)] == data
    dev = [seq[n] - al * n for n in range(1, len(seq))]
    mn, mx = min(dev), max(dev)
    viol = [n + 1 for n, x in enumerate(dev) if (lo is not None and not x > lo) or (hi is not None and not x < hi)]
    print(A, "données", ok, "offset", off, "| min %.4f max %.4f" % (mn, mx), "| bornes", lo, hi, "| violations", viol[:4], len(viol))
