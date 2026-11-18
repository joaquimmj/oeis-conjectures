from math import gcd
def fac(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
sigma = lambda n: sum(d for d in range(1, n + 1) if n % d == 0)
usig = lambda n: sum(d for d in range(1, n + 1) if n % d == 0 and gcd(d, n // d) == 1)
for n in range(1, 3000):
    r = 1
    for p in fac(n): r *= p
    assert usig(n) * sigma(n // r) == sigma(n * n // r)
print("OK")
