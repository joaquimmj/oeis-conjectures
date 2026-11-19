# A368281 / A368282 : sommes partielles de la ligne n de A368281 = ligne n de A368282 (données des entrées).
import re
def rows_antidiag(f):
    d = [int(x) for x in re.findall(r"-?\d+", "".join(l[11:] for l in open(f) if l[:2] in ("%S", "%T", "%U")))]
    return d
def fixed(n, N):
    w = [1]
    while len(w) < N: w = [c for x in w for c in [1] * n + ([0] if x else [])]
    return w[:N]
def b(n, N):
    a = [0]
    for k in range(1, N + 1): a.append(k - a[a[-1] // n])
    return a
d1 = rows_antidiag("../phase0/A368281.txt"); d2 = rows_antidiag("../phase0/A368282.txt")
# tableaux lus par antidiagonales descendantes : T(n,k), n,k >= 1 (A368282 : vérifier son offset)
def table(d, k0):
    T, i, s = {}, 0, 0
    while i < len(d):
        for n in range(1, s + 2):
            if i < len(d): T[(n, s + 2 - n - 1 + k0)] = d[i]; i += 1
        s += 1
    return T
T1 = table(d1, 1)
assert all(T1[(n, k)] == fixed(n, k)[k - 1] for (n, k) in T1), "lecture de A368281"
for k0 in (0, 1):
    T2 = table(d2, k0)
    if all(T2[(n, k)] == b(n, k + 5)[k] for (n, k) in T2): print("A368282 offset k0 =", k0, ": OK, données conformes"); break
for n in range(1, 12):                       # le théorème lui-même (cf. A366860/proof.md)
    w = fixed(n, 10**5); s = 0; bb = b(n, 10**5)
    for k in range(1, 10**5 + 1): s += w[k - 1]; assert s == bb[k]
print("théorème vérifié pour n <= 11, k <= 1e5")
