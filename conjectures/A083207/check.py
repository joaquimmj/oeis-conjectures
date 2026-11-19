# A083207 : contrôles de proof.md.
# (1) partition explicite de D(3*2^a) ; (2) écarts entre nombres de Zumkeller <= 12 (sous-somme par bitset) jusqu'à 10^5 ;
# (3) le témoin de la preuve (multiple de 6 avec v3 = 1) est bien de Zumkeller.
from sympy import divisors
def zumkeller(n):
    d = divisors(n); s = sum(d)
    if s % 2: return False
    reach = 1
    for x in d: reach |= reach << x
    return (reach >> (s // 2)) & 1 == 1
for a in range(1, 40):
    q = 3 * 2**a; A = [q] + [2**i for i in range(1, a)]
    assert sum(A) * 2 == sum(divisors(q)) and set(A) <= set(divisors(q))
Z = [n for n in range(1, 100001) if zumkeller(n)]
gaps = max(b - a for a, b in zip(Z, Z[1:]))
print("Zumkeller <= 10^5 :", len(Z), "| écart max :", gaps)
assert gaps <= 12
for n in range(1, 200000):
    w = [m for m in range(n, n + 12) if m % 6 == 0 and (m // 3) % 3 != 0]
    assert w
for m in range(6, 30000, 6):
    if (m // 3) % 3: assert zumkeller(m), m
print("OK")
