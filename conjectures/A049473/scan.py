# s(m) = zeta(3, m+1). Conjecture : pour n >= 1, s(a) < 1/n^2 < s(a-1) avec a = round(n/sqrt(2)) (A049473).
# On teste les n où n/sqrt(2) est proche d'un demi-entier (les seuls délicats), en haute précision.
import sys
from mpmath import mp, mpf, zeta, sqrt, floor, nint
mp.dps = 50
N = int(sys.argv[1])
s = lambda m: zeta(3, m + 1)
bad, tested = [], 0
r2 = sqrt(2)
for n in range(1, N + 1):
    x = n / r2
    frac = x - floor(x)
    if n > 2000 and abs(frac - mpf(1) / 2) > mpf(5) / n: continue      # loin d'un demi-entier : sans risque (cf. proof.md)
    a = int(nint(x))
    tested += 1
    t = mpf(1) / n**2
    if not (s(a) < t < s(a - 1)): bad.append((n, a, float(frac)))
print("testés :", tested, "| échecs :", bad[:10], len(bad))
