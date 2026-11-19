# A080253 : périodicité mod k (période | lambda(k) | phi(k)), cas particulier du théorème de ../A004123/proof.md.
from math import comb, factorial, gcd
N = 300
a = [1]
for n in range(1, N): a.append(1 + sum(2 ** r * comb(n, r) * a[n - r] for r in range(1, n + 1)))
assert a[:6] == [1, 3, 17, 147, 1697, 24483]
g = [1, 3]                                                     # G(u) = (1+u)/(1-2u-u^2)
while len(g) < N: g.append(2 * g[-1] + g[-2])
S = [[1]]
for n in range(1, N): S.append([0] + [S[n-1][j-1] + (j * S[n-1][j] if j < n else 0) for j in range(1, n + 1)])
assert all(a[n] == sum(g[j] * factorial(j) * S[n][j] for j in range(n + 1)) for n in range(60))
def lam(k):
    L = 1
    for i in range(1, k + 1):
        if gcd(i, k) == 1:
            o, x = 1, i % k
            while x != 1 % k: x = x * i % k; o += 1
            L = L * o // gcd(L, o)
    return L
for k in range(1, 80):
    t = [x % k for x in a]
    assert all(t[n] == t[n + lam(k)] for n in range(k, N - lam(k)))
print("OK : forme G(e^x - 1) et période | lambda(k) pour k < 80")
