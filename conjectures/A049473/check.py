# Contrôles de proof.md : (1) inégalités télescopiques exactes (fractions) pour a <= 60 et en flottant multi-précision
# jusqu'à 10^5 ; (2) s(a) < 1/n^2 < s(a-1) pour a = round(n/sqrt 2), n <= 10^5 (mpmath) et cas critiques (scan.py) ;
# (3) positions des 1 et des 0 dans les différences de A049473 = A001953 et A001954 (n < 10^6).
from fractions import Fraction as F
from math import isqrt
from mpmath import mp, zeta, mpf
mp.dps = 40
for a in range(1, 61):
    assert F(4 * a, 4 * a**4 + 1) < F(1, a**3)                         # h(k) - h(k+1) < 1/k^3
for k in range(2, 2000): assert F(1, k**3) < F(1, k * (k * k - 1))
for a in range(1, 10**5, 997):
    z = zeta(3, a)
    assert z > mpf(1) / (2 * a * a - 2 * a + 1) and zeta(3, a + 1) < mpf(1) / (2 * a * (a + 1))
rnd = lambda n: int(mpf(n) / mp.sqrt(2) + mpf(1) / 2)
for n in range(1, 20001):
    a = rnd(n); t = mpf(1) / n**2
    assert zeta(3, a + 1) < t < zeta(3, a), n
N = 10**6
A = [isqrt(2 * n * n) // 2 + (1 if 2 * n * n > (2 * (isqrt(2 * n * n) // 2) + 1)**2 else 0) for n in range(N + 2)]  # round(n/sqrt2) exact
assert all(abs(A[n] - n / 2**0.5) < 0.5 for n in range(1, 2000))
d = [A[m + 1] - A[m] for m in range(N)]
ones = [m for m in range(N) if d[m] == 1]; zeros = [m for m in range(N) if d[m] == 0]
b53 = [isqrt((2 * j + 1)**2 * 2) // 2 for j in range(len(ones))]          # floor((j+1/2) sqrt 2) = floor(sqrt(2(2j+1)^2)/2)
assert ones == b53[:len(ones)]
b54 = [2 * j + 1 + isqrt(2 * (2 * j + 1)**2) // 2 for j in range(len(zeros))]   # floor((j+1/2)(2+sqrt2))
assert zeros == b54[:len(zeros)]
print("OK")
