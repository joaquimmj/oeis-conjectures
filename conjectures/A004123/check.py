# A004123, A006531 : périodicité mod k (période | lambda(k) | phi(k)), et la forme générale G(e^x - 1).
from math import comb, factorial, gcd
NM = 260
S = [[1]]
for n in range(1, NM + 1):
    S.append([0] + [S[n-1][j-1] + (j * S[n-1][j] if j < n else 0) for j in range(1, n + 1)])
seq = lambda g, sg=False: [sum(g(j) * factorial(j) * S[n][j] for j in range(n + 1)) * ((-1) ** n if sg else 1) for n in range(NM + 1)]
A4123 = seq(lambda j: 2 ** j)
A6531 = seq(lambda j: (-1) ** j * comb(2 * j, j) // (j + 1), True)
assert A4123[:8] == [1, 2, 10, 74, 730, 9002, 133210, 2299754]
assert A6531[:8] == [1, 1, 3, 19, 183, 2371, 38703, 763099]
phi = lambda k: sum(1 for i in range(1, k + 1) if gcd(i, k) == 1)
def lam(k):
    L = 1
    for i in range(1, k + 1):
        if gcd(i, k) == 1:
            o, x = 1, i % k
            while x != 1 % k: x = x * i % k; o += 1
            L = L * o // gcd(L, o)
    return L
import random
random.seed(1)
G = [lambda j, c=[random.randint(-9, 9) for _ in range(NM + 1)]: c[j] for _ in range(3)]
for k in range(1, 61):
    assert phi(k) % lam(k) == 0
    for s in [A4123, A6531] + [seq(g) for g in G]:
        t = [x % k for x in s]
        assert all(t[n] == t[n + lam(k)] for n in range(k + 8, NM + 1 - lam(k)))   # périodique dès n >= k
print("OK : k <= 60, A004123, A006531 et 3 séries G aléatoires")
