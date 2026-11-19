# Contrôles numériques (définition directe, gen.py) : limites, inégalités de l'entrée dans les deux indexations,
# et les deux lemmes de proof.md : b(n) = n + 1 + #{k : a(k) < b(n)} et n+1 <= b(n) <= 2n+1.
from fractions import Fraction as F
from gen import gen
a, b = gen(300000)
import bisect
assert all(b[n] == n + 1 + bisect.bisect_left(a, b[n]) for n in range(len(b)))
assert all(n + 1 <= b[n] <= 2*n + 1 for n in range(len(b)))
for sh in (0, 1):
    ba = [n for n in range(1, len(a)) if not (-1 <= F(5, 2) - F(a[n], n + sh) <= 2)]
    bb = [n for n in range(1, len(b)) if not (-1 <= F(5, 3) - F(b[n], n + sh) <= 2)]
    print("décalage", sh, "échecs a :", ba[:5], len(ba), "| échecs b :", bb[:5], len(bb))
N = len(a) - 1
print("a(N)/N =", a[N] / N, " b(N)/N =", b[N] / N)
