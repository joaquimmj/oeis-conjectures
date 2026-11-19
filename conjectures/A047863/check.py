# A047863 : a(n) = Sum_k C(n,k) 2^(k(n-k)). Lemme (proof.md) : pour p premier impair, a(n) mod p est de période p-1 (n >= 1).
# On vérifie la périodicité sur plusieurs périodes (calcul exact) puis les cinq énoncés sur une période.
from math import comb
def a(n): return sum(comb(n, k) * 2**(k * (n - k)) for k in range(n + 1))
A = [a(n) for n in range(0, 200)]
for p in (3, 5, 7, 13):
    assert all(A[n] % p == A[n + p - 1] % p for n in range(1, 200 - (p - 1)))
assert all(A[n] % 2 == 0 for n in range(1, 200))                         # pair (k = 0 et k = n donnent 2)
assert all(A[n] % 5 for n in range(1, 5))                                # 5 ne divise jamais : une période (n = 1..4)
assert all(A[2 * n] % 3 == 0 for n in range(1, 3))                       # 3 | a(2n) : période 2
assert A[5] % 7 == 0                                                     # 7 | a(6n+5) : période 6
assert A[3] % 13 == 0                                                    # 13 | a(12n+3) : période 12
print("a(n) mod 5, n = 1..4 :", [A[n] % 5 for n in range(1, 5)], "| a(5) mod 7 =", A[5] % 7, "| a(3) mod 13 =", A[3] % 13)
print("OK : périodicité vérifiée sur n < 200 pour p = 3, 5, 7, 13 ; énoncés vérifiés sur une période")
