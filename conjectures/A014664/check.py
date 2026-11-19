# A014664 : contrôle de ord_{p^k}(2) = ord_p(2) * p^(k-1) pour les premiers impairs non Wieferich p < 3000, k <= 3,
# et de l'échec pour les premiers de Wieferich 1093, 3511 (k = 2).
from sympy import primerange, n_order
for p in primerange(3, 3000):
    wief = pow(2, p - 1, p * p) == 1
    d = n_order(2, p)
    for k in (2, 3):
        if not wief: assert n_order(2, p**k) == d * p**(k - 1), (p, k)
for p in (1093, 3511): assert n_order(2, p * p) == n_order(2, p)
print("OK")
