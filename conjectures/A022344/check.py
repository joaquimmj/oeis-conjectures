# A022344 : conjecture de K. J. Ramsey (2007). (1) identité Q(F3) = ± Q(F1) Q(F2), symbolique ;
# (2) F3 (ou -F3) finit par coïncider avec une ligne p du tableau de Wythoff, avec a(p) = a(n) a(m).
import sympy as sp
from math import isqrt
g0, g1, h0, h1 = sp.symbols("g0 g1 h0 h1")
def fibseq(a, b, N):
    s = [a, b]
    for _ in range(N): s.append(s[-1] + s[-2])
    return s
Q = lambda s, i: s[i]**2 - s[i-1] * s[i+1]
G, H = fibseq(g0, g1, 12), fibseq(h0, h1, 12)
for j in range(0, 5):
    F3 = [sp.expand(G[i] * H[j+1] - G[i+1] * H[j]) for i in range(10)]
    assert all(sp.expand(F3[i+1] - F3[i] - F3[i-1]) == 0 for i in range(1, 8))
    for i in range(1, 8):
        r = sp.expand(Q(F3, i) - (-1)**(i + j) * Q(G, 1) * Q(H, 1))      # signe (-1)^(i+j) (à un signe global près)
        r2 = sp.expand(Q(F3, i) + (-1)**(i + j) * Q(G, 1) * Q(H, 1))
        assert r == 0 or r2 == 0, (i, j)
print("identité : |Q(F3)| = |Q(F1)| |Q(F2)| (symbolique)")
# tableau de Wythoff
def isq(n): return isqrt(5 * n * n)
def lower(n): return (n + isq(n)) // 2          # floor(n phi)
R, C = 60000, 30
row_of = {}
rows = []
for n in range(1, R + 1):
    t1 = lower(lower(n)); t2 = lower(n) + t1     # floor(floor(n phi) phi) et floor(floor(n phi) phi^2)
    r = [t1, t2]
    for _ in range(C): r.append(r[-1] + r[-2])
    rows.append(r)
    for c in range(len(r) - 1): row_of[(r[c], r[c+1])] = n
a = lambda n: abs(Q(rows[n-1], 2))
bad = tested = 0
for n in range(1, 40):
    for m in range(1, 40):
        for j in range(0, 3):
            F3 = [rows[n-1][i] * rows[m-1][j+1] - rows[n-1][i+1] * rows[m-1][j] for i in range(C)]
            if F3[10] < 0: F3 = [-v for v in F3]
            p = next((row_of.get((F3[i], F3[i+1])) for i in range(4, C - 1) if (F3[i], F3[i+1]) in row_of), None)
            tested += 1
            if p is None or a(p) != a(n) * a(m): bad += 1
print("paires testées :", tested, "| échecs :", bad)
