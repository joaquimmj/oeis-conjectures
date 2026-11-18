# A050446 : conjecture de Rascoe. Bijection, récurrence et table de l'entrée (n <= 8, m <= 6).
from itertools import product
from functools import lru_cache
@lru_cache(None)
def T(n, m):                      # récurrence de l'entrée, T(0,m) = 1, T(n,0) = [n = 0]
    if n == 0: return 1
    if m == 0: return 0
    return T(n, m - 1) + sum(T(2 * k, m - 1) * T(n - 1 - 2 * k, m) for k in range((n - 1) // 2 + 1))
table = [[1]*10, list(range(1, 11)), [1,3,6,10,15,21,28,36,45,55], [1,5,14,30,55,91,140,204,285,385],
         [1,8,31,85,190,371,658,1086,1695,2530], [1,13,70,246,671,1547,3164,5916,10317,17017]]
assert all(T(n, m + 1) == v for n, r in enumerate(table) for m, v in enumerate(r))
for n in range(0, 9):
    for m in range(1, 7):
        W = [w for w in product(range(1, m + 1), repeat=n) if all(w[i] + w[i+1] <= m + 1 for i in range(n - 1))]
        V = {tuple(x if i % 2 == 0 else m + 1 - x for i, x in enumerate(w)) for w in W}       # bijection
        assert len(V) == len(W) and all(all((v[i] <= v[i+1]) if i % 2 == 0 else (v[i] >= v[i+1]) for i in range(n - 1)) for v in V)
        UD = [w for w in product(range(1, m + 1), repeat=n) if all((w[i] <= w[i+1]) if i % 2 == 0 else (w[i] >= w[i+1]) for i in range(n - 1))]
        assert set(UD) == V and len(W) == T(n, m)
print("OK : n <= 8, m <= 6")
