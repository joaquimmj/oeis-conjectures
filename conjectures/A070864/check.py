# A070864 : la formule conjecturée par Layman (2002) coïncide avec celles de Cloitre et de Curgus.
from math import isqrt
N = 10 ** 6
a = [0, 1, 1]
for n in range(3, N + 1): a.append(2 + a[n - a[n - 1]])
for n in range(3, N + 1):
    k = isqrt(n + 1) - 1; d = n - k * (k + 2)
    layman = 2 * k + 1 if d in (0, 1, 2) or d % 2 == 0 else 2 * k + 3
    r = isqrt(n); c = r if r * r == n else r + 1
    curgus = 2 * r - (-1) ** (n + c)
    assert a[n] == layman == curgus, n
print("OK jusqu'à n =", N)
