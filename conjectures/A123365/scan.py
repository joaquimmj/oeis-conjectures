# Nombre de cubes c(n) (A046530) et de carrés s(n) (A000224) mod n, multiplicatifs ; valeurs aux puissances
# premières : formule exacte pour p premier, énumération (mise en cache) pour p^e, e >= 2. Balayage des trois conjectures jusqu'à N.
import sys
from sympy import factorint, isprime
N = int(sys.argv[1])
cache = {}
def count_pow(q, k):
    if isprime(q):   # formules exactes aux nombres premiers
        if k == 3: return (q + 2) // 3 if q % 3 == 1 else q
        return 2 if q == 2 else (q + 1) // 2
    if (q, k) not in cache: cache[q, k] = len({pow(x, k, q) for x in range(q)})
    return cache[q, k]
def mult(n, k):
    r = 1
    for p, e in factorint(n).items(): r *= count_pow(p**e, k)
    return r
bad365, bad722a, bad723 = [], [], []
seq722 = set()
for n in range(2, N + 1):
    if n % 3 == 1:
        c = mult(n, 3)
        if 3 * c == n + 2 and not (isprime(n) and n % 6 == 1): bad365.append(n)
    s = mult(n, 2)
    if s == -(-(n + 1) // 3):
        seq722.add(n)
        if n > 2 and n % 3 == 0 and not isprime(n // 3): bad722a.append(n)
    if s == -(-(n + 1) // 4) and n > 4 and n % 4 == 0 and not isprime(n // 4): bad723.append(n)
    if n % 500000 == 0: print("…", n, flush=True)
from sympy import primerange
miss = [p for p in primerange(3, N // 3 + 1) if 3 * p not in seq722]
print("A123365 contre-exemples :", bad365[:10])
print("A123722 (multiples de 3 non 3·premier) :", bad722a[:10], "| premiers impairs p sans 3p :", miss[:10])
print("A123723 :", bad723[:10])
