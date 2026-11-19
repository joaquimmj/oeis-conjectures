# A005121 : conjecture de Mohapatra, R(n,n) = a(n), et les étapes de proof.md.
from functools import lru_cache
@lru_cache(None)
def R(n, k):
    if n == 1: return 1 if k == 1 else 0
    if k < n: return k * sum(R(n - 1, j) for j in range(k, n))
    return sum(R(n, j) for j in range(1, n))
@lru_cache(None)
def S(n, k):
    if n == k: return 1
    if k == 0 or k > n: return 0
    return S(n - 1, k - 1) + k * S(n - 1, k)
@lru_cache(None)
def a(n): return 1 if n == 1 else sum(S(n, k) * a(k) for k in range(1, n))     # Lengyel
@lru_cache(None)
def c(n, k, m):                                                                # coeff. de R(m,m) dans R(n,k)
    if n <= 1: return 0
    return k * (sum(c(n - 1, j, m) for j in range(k, n - 1)) + (1 if m == n - 1 else 0))
N = 30
assert all(R(n, n) == a(n) for n in range(1, N))
for n in range(2, 18):
    for k in range(1, n):
        assert R(n, k) == sum(c(n, k, m) * R(m, m) for m in range(1, n))             # étape 1
    for m in range(1, n):
        t = n - m - 1
        v = [k if k <= m else 0 for k in range(1, n)]
        for _ in range(t): v = [k * sum(v[j - 1] for j in range(k, m + 1)) if k <= m else 0 for k in range(1, n)]
        assert v == [c(n, k, m) for k in range(1, n)]                                # étape 2 : M^t v
        assert sum(v) == S(n, m)                                                      # étape 3
W = {(0, j): 1 for j in range(0, 20)}
for t in range(1, 15):
    for j in range(0, 20): W[(t, j)] = sum(k * W[(t - 1, k)] for k in range(1, j + 1))
assert all(W[(t, j)] == S(j + t, j) for t in range(15) for j in range(1, 20))        # W_t(j) = S(j+t, j)
print("OK : R(n,n) = a(n) pour n <", N, "; étapes vérifiées pour n < 18")
