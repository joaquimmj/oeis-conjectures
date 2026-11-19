# A128440 : T(n,k) = floor(k r^n), r = phi. Conjecture : les lignes 2n-1 et 2n sont disjointes (n >= 1).
# Calcul exact : floor(k phi^m) = F(m-1) k + floor(F(m) k phi), floor(x phi) = (x + isqrt(5x^2)) // 2.
from math import isqrt
F = [0, 1]
for _ in range(200): F.append(F[-1] + F[-2])
fl_phi = lambda x: (x + isqrt(5 * x * x)) // 2
T = lambda m, k: F[m - 1] * k + fl_phi(F[m] * k)
import sys
LIM = int(sys.argv[1])
for n in range(1, 13):
    a, b = 2 * n - 1, 2 * n
    top = T(b, LIM)
    A = {T(a, k) for k in range(1, (top * 1) // max(1, T(a, 1)) + 3) if T(a, k) <= top}
    inter = sorted(x for x in (T(b, k) for k in range(1, LIM + 1)) if x in A)
    print("n=%d lignes %d et %d : intersection (k <= %d) :" % (n, a, b, LIM), inter[:5], len(inter))
