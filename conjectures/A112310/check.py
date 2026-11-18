# A112310 : conjecture d'Adamson (sommes par groupes de F(k) termes = A023610), depuis la définition.
F = [0, 1]
while len(F) < 40: F.append(F[-1] + F[-2])
def lazy(n):   # nombre de termes de la représentation paresseuse (maximale) : glouton sur le complément
    # n = somme de F(2..L+1) moins une représentation de Zeckendorf du complément
    if n == 0: return 0
    L = 1
    while F[L + 3] - 2 < n: L += 1                     # longueur L : F(L+2)-2 < n <= F(L+3)-2
    m, cnt, k = F[L + 3] - 2 - n, L, L + 1
    while m:
        while F[k] > m: k -= 1
        m -= F[k]; cnt -= 1
    return cnt
from itertools import product
def brute(n):  # contrôle : mots binaires sans 00, chiffres F(2), F(3), ...
    for L in range(1, 12):
        for w in product((0, 1), repeat=L):
            if w[-1] == 1 and all(w[i] or w[i + 1] for i in range(L - 1)) and sum(F[i + 2] for i in range(L) if w[i]) == n:
                return sum(w)
assert all(lazy(n) == brute(n) for n in range(1, 120))
assert [lazy(n) for n in range(12)] == [0, 1, 1, 2, 2, 2, 3, 2, 3, 3, 3, 4]
A023610 = lambda n: ((n + 2) * F[n + 4] + (n - 1) * F[n + 2]) // 5
pos, sums = 1, []
for k in range(2, 26):                                 # groupe k : F(k) termes, n = F(k+1)-1 .. F(k+2)-2
    assert pos == F[k + 1] - 1
    sums.append(sum(lazy(n) for n in range(pos, pos + F[k]))); pos += F[k]
assert sums == [A023610(i) for i in range(len(sums))]
print("OK : groupes 2 à 25, sommes =", sums[:8], "...")
