# A361190 : données de l'entrée (entiers exacts, petits n) et exposant alpha = 1 + pi/arctan(sqrt 2) (flottants, n grand).
import re, numpy as np
from math import pi, atan, sqrt, log
oeis = [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open("../phase0/A361190.txt") if l[:2] in ("%S", "%T", "%U")))]
STEPS = [(1, 1), (1, -1), (-1, 0)]
def exact(nmax):                       # excursions de longueur 4n dans 0 <= y <= x
    cur = {(0, 0): 1}; out = [1]
    for t in range(1, 4 * nmax + 1):
        nxt = {}
        for (x, y), c in cur.items():
            for dx, dy in STEPS:
                X, Y = x + dx, y + dy
                if 0 <= Y <= X: nxt[(X, Y)] = nxt.get((X, Y), 0) + c
        cur = nxt
        if t % 4 == 0: out.append(cur.get((0, 0), 0))
    return out
ex = exact(len(oeis) - 1); assert ex == oeis[:len(ex)], (ex[:8], oeis[:8])
# flottants : marche pondérée (poids 1/4, 1/4, 1/2 après recentrage), a(n)/64^n = proba
N = 2400; L = N // 2 + 2
p = np.zeros((L, L)); p[0, 0] = 1.0; probs = {(1, 1): .25, (1, -1): .25, (-1, 0): .5}
vals = {}
for t in range(1, N + 1):
    q = np.zeros_like(p)
    for (dx, dy), w in probs.items():
        src = p[max(0, -dx):L - max(0, dx), max(0, -dy):L - max(0, dy)]
        q[max(0, dx):max(0, dx) + src.shape[0], max(0, dy):max(0, dy) + src.shape[1]] += w * src
    iu = np.triu_indices(L, 1); q[iu] = 0           # garde y <= x (indice [x, y])
    p = q
    if t % 4 == 0: vals[t // 4] = p[0, 0]
alpha = 1 + pi / atan(sqrt(2))
ns = sorted(vals)
for n in (100, 300, 500, 599):
    est = -log(vals[n] / vals[n // 2]) / log(2)     # pente locale de log a(n)/64^n
    print(n, round(est, 4))
print("alpha prédit :", alpha)
