# A116731 : nombre de couples distincts (échanges, passes) du tri à bulles sur les permutations de [n].
# (1) simulation directe du tri à bulles (n <= 9) ; (2) formule Sum_{P=0}^{n-1} (Sum_i min(i-1,P) - P + 1) ; (3) données.
import json, glob
from itertools import permutations
def bubble(p):
    p, flips, it = list(p), 0, 0
    while True:
        sw = False
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]: p[i], p[i + 1] = p[i + 1], p[i]; flips += 1; sw = True
        if not sw: return flips, it
        it += 1                         # passes ayant effectué au moins un échange
def formula(n): return sum(sum(min(i - 1, P) for i in range(1, n + 1)) - P + 1 for P in range(n))
E = {}
for f in glob.glob("../crawl/raw_*.json"): E.update(json.load(open(f)))
data = [int(v) for v in E["A116731"]["data"].split(",")]
for n in range(1, 10):
    pairs = {bubble(p) for p in permutations(range(n))}
    assert len(pairs) == formula(n) == data[n - 1], (n, len(pairs), formula(n), data[n - 1])
assert all(formula(n) == data[n - 1] for n in range(1, len(data) + 1))
# la table d'inversion à gauche : passes = max L_i (contrôle n <= 8)
for n in range(1, 9):
    for p in permutations(range(n)):
        L = [sum(1 for j in range(i) if p[j] > p[i]) for i in range(n)]
        assert bubble(p) == (sum(L), max(L))
print("OK : simulation (n <= 9), formule et données (%d termes) concordent" % len(data))
