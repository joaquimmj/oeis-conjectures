# A371176 : contrôle des étapes de notes/proof.md, depuis la définition A000120(k) <= A001511(k).
from math import comb, log
ok = lambda k: bin(k).count("1") <= (k & -k).bit_length()
F = [0, 1]
while len(F) < 60: F.append(F[-1] + F[-2])
M = 22
terms = [k for k in range(1, 1 << M) if ok(k)]
for m in range(1, M + 1):
    s = sum(1 for k in terms if (1 << (m - 1)) <= k < (1 << m))          # max X = m
    tight = sum(1 for k in terms if (1 << (m - 1)) <= k < (1 << m) and bin(k).count("1") == (k & -k).bit_length())
    assert s == F[m], m                                                   # étape 1
    if m >= 3: assert tight == F[m - 2] == sum(comb(m - j - 1, j - 2) for j in range(2, m)), m  # serrés
    assert sum(1 for k in terms if k < (1 << m)) == F[m + 2] - 1          # étape 2
for n, k in enumerate(terms, 1):                                          # étape 3 : encadrement
    m = k.bit_length()
    assert F[m + 1] - 1 < n <= F[m + 2] - 1
print("OK pour m <=", M, "; log a(n)/log n en n =", len(terms), ":", log(terms[-1]) / log(len(terms)))
