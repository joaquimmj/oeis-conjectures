# A155200 : A(x) = exp(Sum 2^(n^2) x^n/n). Contrôle de v2(a(n)) = s2(n) (n <= 300) et des deux lemmes de proof.md :
# v2(2^j/j!) = s2(j), et v2(r(t)) >= t+1 pour R = exp(Sum_{n>=2} 2^(n^2) x^n / n) (calcul exact dans Q).
from fractions import Fraction as Fr
from math import factorial
N = 300
c = [0] + [2**(n*n) for n in range(1, N + 1)]
a = [1]
for n in range(1, N + 1):
    s = sum(c[k] * a[n - k] for k in range(1, n + 1)); assert s % n == 0; a.append(s // n)
v2i = lambda x: (x & -x).bit_length() - 1
v2 = lambda q: v2i(q.numerator) - v2i(q.denominator)
s2 = lambda n: bin(n).count("1")
assert all(v2i(a[n]) == s2(n) for n in range(1, N + 1))
assert all(v2(Fr(2**j, factorial(j))) == s2(j) for j in range(1, N + 1))
r = [Fr(1)] + [Fr(0)] * 120                     # R' = R * Sum_{n>=2} 2^(n^2) x^(n-1)
for t in range(1, 121):
    r[t] = sum(Fr(2**(n*n)) * r[t - n] for n in range(2, t + 1)) / t
assert all(r[t] == 0 or v2(r[t]) >= t + 1 for t in range(1, 121))
print("OK : v2(a(n)) = s2(n) pour n <= 300 ; lemmes vérifiés")
