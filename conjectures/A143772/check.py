# A143772 : g(m) = gcd_{k | m} (k + m/k) pour m composé. Contrôles de proof.md :
# (1) valeurs impaires de g sur m <= 3*10^5 : {1, 3} ; (2) pour chaque e pair <= 300, témoin m = q r construit comme dans la preuve.
from math import gcd
from sympy import divisors, isprime, primerange, factorint
def g(m):
    r = 0
    for k in divisors(m): r = gcd(r, k + m // k)
    return r
odd = {g(m) for m in range(4, 300001) if not isprime(m) and g(m) % 2}
print("valeurs impaires :", sorted(odd)); assert odd == {1, 3}
def witness(e):
    q = next(p for p in primerange(3, 10**7) if p % e == 1)
    M1 = (q * q - 1) // e
    # t0 : t0 premier à M1, et e*t0 - q premier à e*M1 (CRT résolu par recherche directe)
    for t0 in range(1, 10**6):
        if gcd(t0, M1) == 1 and gcd(e * t0 - q, e * M1) == 1: break
    mod = e * M1
    r = e * t0 - q
    while not (r > q and isprime(r)): r += mod
    m = q * r
    assert g(m) == e == gcd(q + r, q * q - 1), (e, q, r)
    return m
W = {e: witness(e) for e in range(2, 301, 2)}
print("témoins construits pour e = 2..300 pairs ; exemples :", {e: W[e] for e in (2, 10, 14, 30, 100, 298)})
