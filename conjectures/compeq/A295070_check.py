# A295070 : a(n) = a(n-2) + b(n-1) + b(n-2) ; contrôle des étapes de A295070.md (solveur de compute.py).
import json, glob
from compute import parse, solve
E = {}
for f in glob.glob("../crawl/raw_*.json"): E.update(json.load(open(f)))
e = E["A295070"]; rhs, init, py = parse(e["name"])
a = solve(py, init, 3000)
assert a[:len(e["data"].split(","))] == [int(v) for v in e["data"].split(",")]
aset = set(a); comp = [x for x in range(1, a[-1]) if x not in aset]
assert all(a[n] >= 2*n + 2 for n in range(3, len(a))) and all(comp[m] <= 2*m + 1 for m in range(3, 2000))
assert all(a[n] - a[n-1] <= 4*n for n in range(2, len(a)))
print("A295070 OK ; a(n)/n^2 ->", a[-1] / (len(a) - 1)**2, "; a(N)/a(N-1) - 1 =", a[-1] / a[-2] - 1)
