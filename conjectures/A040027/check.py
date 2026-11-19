# A040027 : conjecture de Yanev, et les étapes de proof.md (séries formelles, en entiers exacts).
import re
from math import factorial, comb
from functools import lru_cache
@lru_cache(None)
def S(n, k):
    if n == k: return 1
    if k == 0 or k > n: return 0
    return S(n - 1, k - 1) + k * S(n - 1, k)
N = 120
c = [sum((-1) ** j * factorial(j) for j in range(k + 1)) for k in range(N + 2)]
r = [sum(c[k] * S(n + 1, k + 1) for k in range(n + 1)) for n in range(N)]           # membre de droite de Yanev
oeis = [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open("../phase0/A040027.txt") if l[:2] in ("%S", "%T", "%U")))]
assert r[:len(oeis)] == oeis
# H' = (1 + e^x) H - 1 : r(n+1) = r(n) + sum_k C(n,k) r(k) - [n = 0]
assert all(r[n + 1] == r[n] + sum(comb(n, k) * r[k] for k in range(n + 1)) - (n == 0) for n in range(N - 1))
# e.g.f. de Sloane : s(n) = a(n-1), S' = 1 + e^x S, S(0) = 0 <=> s(n+1) = [n=0] + sum_k C(n,k) s(k)
s = [0, 1]
for n in range(1, N): s.append(sum(comb(n, k) * s[k] for k in range(n + 1)))
assert s[1:N] == r[:N - 1]
# formule de Bala (partitions dont le dernier bloc est un singleton)
assert all(r[n] == sum(S(j, k) * k ** (n - j) for k in range(n + 1) for j in range(k, n + 1)) for n in range(40))
print("OK pour n <", N)
