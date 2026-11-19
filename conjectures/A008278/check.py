# A008278 : conjecture de Wiseman, par énumération des diviseurs des superprimorielles (exposants).
from itertools import product
from functools import lru_cache
@lru_cache(None)
def S(n, k):
    if n == k: return 1
    if k == 0 or k > n: return 0
    return S(n - 1, k - 1) + k * S(n - 1, k)
for n in range(1, 9):
    caps = [n - i for i in range(1, n)]                  # exposants de A006939(n-1) : n-1, ..., 1
    cnt = [0] * (n + 1)
    for e in product(*[range(c + 1) for c in caps]):
        nz = [x for x in e if x]
        if len(nz) == len(set(nz)): cnt[len(nz) + 1] += 1
    assert cnt[1:] == [S(n, n - k + 1) for k in range(1, n + 1)], (n, cnt)
print("OK pour n <= 8")
