# A101513 : simulation du triangle et test des conjectures (1)-(4) de Sloane.
# Ligne n : les n plus petits entiers non utilisés ayant un facteur premier commun avec un élément de la ligne n-1.
import sys
from sympy import isprime, primefactors
R = int(sys.argv[1])
used, rows = set([1, 2, 3]), [[1], [2, 3]]
row_of = {1: 1, 2: 2, 3: 2}
postponed = set()
spf_cache = {}
def pf(x):
    if x not in spf_cache: spf_cache[x] = primefactors(x)
    return spf_cache[x]
low = 4
for n in range(3, R + 1):
    prev = rows[-1]
    P = set()
    for y in prev: P.update(pf(y))
    cur, x = [], low
    first_unused_seen = None
    while len(cur) < n:
        if x not in used:
            if any(p in P for p in pf(x)): cur.append(x)
            else: postponed.add(x)          # candidat sauté (n'a pas pu être placé tout de suite)
        x += 1
    for y in cur: used.add(y); row_of[y] = n
    while low in used: low += 1
    rows.append(cur)
maxv = low  # tous les entiers < low sont placés
print("lignes :", R, "| entiers < %d tous placés" % low)
bad1 = [x for x in range(4, low) if (x in postponed) != isprime(x)]
print("(1) repoussé <=> premier (x < low) :", "OK" if not bad1 else bad1[:10])
primes = [p for p in range(2, low) if isprime(p)]
rws = [row_of[p] for p in primes]
print("(3) premiers dans l'ordre (lignes croissantes, et ordre dans la ligne) :",
      all(rws[i] <= rws[i+1] for i in range(len(rws) - 1)))
bad4 = [p for p in primes if p > 3 and 2 * p in row_of and row_of[p] != row_of[2 * p] + 1]
print("(4) 2p dans une ligne, p dans la suivante :", "OK" if not bad4 else bad4[:10])
# Hypothèse de récurrence H(n) de proof.md, vérifiée pour 3 <= n <= R :
# ligne n = {p premier : 2p dans la ligne n-1} (hors p <= 3) ∪ {les composés suivants, dans l'ordre}.
comp_next = 4
ok = True
for n in range(3, R + 1):
    row = rows[n - 1]
    primes_expected = sorted(p for p in (y // 2 for y in rows[n - 2] if y % 2 == 0) if isprime(p) and p > 3)
    pr = sorted(y for y in row if isprime(y))
    co = [y for y in row if not isprime(y)]
    exp_co = []
    c = comp_next
    while len(exp_co) < len(co):
        if not isprime(c) and c not in (1,): exp_co.append(c)
        c += 1
    if pr != primes_expected or co != exp_co or row != sorted(row): ok = False; print("H échoue en", n); break
    comp_next = c
print("H(n) pour 3 <= n <=", R, ":", ok)
