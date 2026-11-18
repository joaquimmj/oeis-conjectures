# A358360 : les cinq conjectures d'Oudra et les identités de proof.md, depuis la définition (Delannoy centraux).
from math import comb
N = 3 ** 8
D = [1, 3]
for n in range(2, N + 1): D.append((3 * (2 * n - 1) * D[-1] - (n - 1) * D[-2]) // n)
assert all(D[n] == sum(comb(n, k) * comb(n + k, k) for k in range(n + 1)) for n in range(40))
def v3(x):
    c = 0
    while x % 3 == 0: x //= 3; c += 1
    return c
a = [v3(d) for d in D]
A000989 = lambda n: v3(comb(2 * n, n))
A168570 = lambda n: v3(2 ** n - 1)
def A254046(n): return 1 if n % 3 != 2 else 1 + A254046(n // 3 + 1)
g = lambda n: sum((n // 3 ** k) % 2 for k in range(12))
M = 2000
for m in range(M):
    assert a[2 * m] == A000989(m) and a[2 * m + 1] == 1 + v3(2 * m + 1) + A000989(m)      # Théorème 4 de AASV
    assert A254046(m + 1) == 1 + v3(2 * m + 1)                                             # lemme pour (5)
    assert A168570(2 * m + 2) == 1 + v3(m + 1) and A168570(2 * m + 1) == 0                 # lemme pour (3)
for n in range(N // 3):
    for r in range(3): assert a[3 * n + r] == a[n] + (n % 2 if r != 1 else 1 - n % 2)      # Théorème 6 de AASV
s = 0
for n in range(N):
    if n: s += (-1) ** (n + 1) * (1 + v3(n))                                               # A051064(n) = 1 + v3(n)
    assert a[n] == s == g(n)                                                               # (1), (2)
    if n < 2 * M - 1: assert a[n] == A000989((n + 1) // 2) + A168570(n + 1)                # (3)
print("OK : conjectures (1) à (5) pour n <", N, "((3) à (5) pour n <", 2 * M, ")")
