# A170941 : conjecture de Callan, a(n)/A000085(n) -> 1/e, et les étapes de proof.md.
from math import comb, e
from itertools import permutations
N = 400
a = [1, 1, 1, 2]
for n in range(3, N): a.append(a[n] + n * a[n - 1] - a[n - 2] + a[n - 3])        # a(n+1)
I = [1, 1]
for n in range(2, N + 1): I.append(I[-1] + (n - 1) * I[-2])
ie = lambda n: sum((-1) ** h * comb(n - h, h) * I[n - 2 * h] for h in range(n // 2 + 1))
assert all(a[n] == ie(n) for n in range(N))                                       # inclusion-exclusion = récurrence
for n in range(1, 9):                                                             # force brute
    cnt = sum(1 for p in permutations(range(n)) if all(p[p[i]] == i for i in range(n)) and all(p[i] != i + 1 or p[i + 1] != i for i in range(n - 1)))
    assert cnt == a[n]
for n in range(2, N):                                                             # domination : terme_h <= 1/h!
    for h in range(n // 2 + 1):
        assert comb(n - h, h) * I[n - 2 * h] * __import__("math").factorial(h) <= I[n]
print("a(n)/I(n) :", [round(a[n] / I[n], 6) for n in (10, 50, 100, 399)], " 1/e =", round(1 / e, 6))
