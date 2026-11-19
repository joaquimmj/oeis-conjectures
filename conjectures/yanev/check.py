# Neuf conjectures de V. Yanev : contrôle numérique contre les données des entrées et les définitions.
import re
from math import gcd, prod
def data(a): return [int(x) for x in re.findall(r"-?\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
def fac(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
rad = lambda n: prod(fac(n))
def divs(n):
    ds = [1]
    for p, e in fac(n).items(): ds = [d * p ** k for d in ds for k in range(e + 1)]
    return sorted(ds)
sig = lambda k, n: prod(sum(p ** (k * i) for i in range(e + 1)) for p, e in fac(n).items())
phi = lambda n: prod(p ** (e - 1) * (p - 1) for p, e in fac(n).items())
mu = lambda n: 0 if any(e > 1 for e in fac(n).values()) else (-1) ** len(fac(n))
def lam(n):
    L = 1
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            o, x = 1, i % n
            while x != 1 % n: x = x * i % n; o += 1
            L = L * o // gcd(L, o)
    return L
odd = lambda n: n >> ((n & -n).bit_length() - 1)
core = lambda n: prod(p for p, e in fac(n).items() if e % 2)
# A129527
d = data("A129527"); A = [0]
for n in range(1, 3000): A.append(A[n // 2] + n if n % 2 == 0 else n)
assert A[:len(d)] == d and all(A[n] == 2 * n - odd(n) for n in range(1, 3000))
# A173614
d = data("A173614"); L = [__import__("math").lcm(*[p - 1 for p in fac(n)]) for n in range(2, 400)]
assert L[:len(d)] == d and all(L[n - 2] == lam(rad(n)) for n in range(2, 400))
# A023887
assert all(sig(m, n) * sig(1, rad(n) ** (m - 1)) == sig(1, n ** m * rad(n) ** (m - 1)) for n in range(1, 40) for m in range(1, 5))
# A055210
d = data("A055210"); S = [sum(phi(q) for q in divs(n) if int(q ** .5) ** 2 == q) for n in range(1, 300)]
assert S[:len(d)] == d and all(S[n - 1] * sig(1, n // core(n)) == sig(2, n // core(n)) for n in range(1, 300))
# A367865
d = data("A367865"); T = [sum(q * phi(q) * mu(q) ** 2 for q in divs(n)) for n in range(1, 200)]
assert T[:len(d)] == d and all(T[n - 1] * n == rad(n) * sum(rad(n * k) // rad(k) for k in range(1, n + 1)) for n in range(1, 200))
# A090079
d = data("A090079"); runs = lambda n: len(re.findall(r"0+|1+", bin(n)[2:])) if n else 0
V = [int(re.sub(r"0+", "0", re.sub(r"1+", "1", bin(n)[2:])), 2) for n in range(0, 4000)]
assert V[:len(d)] == d and all(3 * V[n] == 2 ** (runs(n) + 1) + (1 - (-1) ** n) // 2 - 2 for n in range(1, 4000))
# A163617
d = data("A163617"); B = [0]
for n in range(1, 4000): B.append(2 * B[n // 2] if n % 2 == 0 else 2 * B[n // 2] + 2 + (-1) ** (n // 2))
assert B[:len(d)] == d and all(4 * B[n] == 4 * (n ^ (n >> 1)) + 6 * n + 1 - (-1) ** n for n in range(4000))
# A285385 (positions de 1 dans A285384 = complément de A072939 = A036554 + 1)
d = data("A285385"); odd_z = lambda m: m > 0 and ((m & -m).bit_length() - 1) % 2 == 1
P = [m for m in range(1, 6000) if not odd_z(m - 1)]
pd = [0]
while len(pd) < 7000: pd = [c for x in pd for c in ([0, 1] if x == 0 else [0, 0])]
assert P[:len(d)] == d and all(P[i + 1] == P[i] + pd[P[i] - 1] + 1 for i in range(len(P) - 1))
# A179504
d = data("A179504"); C = [1] + [sig(n, 2 * n) for n in range(1, 40)]
assert C[:len(d)] == d
for n in range(1, 40):
    v = ((n & -n).bit_length() - 1)
    from fractions import Fraction as Fr
    assert C[n] == sig(n, n) * (Fr(2 ** n - 1, 2 ** (n * (v + 1)) - 1) + 2 ** n)
print("OK : les neuf identités")
