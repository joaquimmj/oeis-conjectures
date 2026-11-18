# Tests numériques des conjectures de la sélection (lot 3), depuis les définitions.
from math import comb, factorial, isqrt, log, gcd
res = {}
# A000139 : a(n) impair <=> n = 4*f+1 avec f fibbinaire (A022341)
fib = lambda m: m & (m >> 1) == 0
a139 = lambda n: 2 * factorial(3*n) // (factorial(2*n+1) * factorial(n+1))
res["A000139"] = all((a139(n) % 2 == 1) == (n % 4 == 1 and fib((n-1)//4)) for n in range(0, 3000))
# A006165 : identités (i)-(vi) et (vii)
def A6165(n): return 1 if n <= 2 else A6165(n//2) + A6165((n+1)//2)
N = 1 << 14; a = [0] + [A6165(n) for n in range(1, N + 1)]
it = lambda k, n: n if k == 0 else it(k - 1, a[n])
ok = True
for n in range(2, N + 1):
    A = lambda m: a[m]
    ok &= A(n) + A(n - A(n - A(n - A(n - A(n))))) == n
    ok &= A(n - A(n - A(n - A(n)))) == A(n - A(n - A(n - A(n - A(n - A(n))))))
    ok &= it(2, n) == A(n - A(n - A(n - A(n))))
    ok &= n - A(n) == A(n - it(2, n))
    ok &= A(n - A(n)) == it(2, n - it(2, n - it(2, n - it(2, n))))
    for k in range(2, 7):
        I = lambda m: it(k, m)
        ok &= I(n - I(n)) == I(n - I(n - I(n - I(n))))
res["A006165 (i)-(vi)"] = ok
ok7 = True
for k in range(1, 8):
    s = [n - it(k, n) for n in range(1, N + 1)]
    d = [y - x for x, y in zip(s, s[1:])]
    ok7 &= set(d) <= {0, 1}
    rep = sorted({s[i] for i in range(len(d)) if d[i] == 0})
    ok7 &= all(v % (2**k - 1) == 0 and ((v // (2**k - 1)) & (v // (2**k - 1) - 1)) == 0 for v in rep)
res["A006165 (vii)"] = ok7
# A006364 : formule de Yanev
evenrest = lambda k: bin(k >> 1).count("1") % 2 == 0
seq = [k for k in range(0, 50000) if evenrest(k)]
off = [n for n in (0, 1) if all(seq[i] == 2*(i+n) + (-1)**((i+n) - bin(i+n-1).count("1") if i+n >= 1 else 0) - (3 + (-1)**(i+n))//2 for i in range(1, 2000))]
res["A006364 (offset ok)"] = off
# A004123, A006531 : périodicité mod k, période | phi(k)
def stir_seq(coef, n_max, sign=False):
    S = [[1]]
    for n in range(1, n_max + 1):
        row = [0] * (n + 1)
        for j in range(1, n + 1): row[j] = (S[n-1][j-1] if j-1 < len(S[n-1]) else 0) + j * (S[n-1][j] if j < len(S[n-1]) else 0)
        S.append(row)
    return [sum(coef(j) * factorial(j) * S[n][j] * ((-1)**(n+j) if sign else 1) for j in range(n + 1)) for n in range(n_max + 1)]
cat = lambda j: comb(2*j, j) // (j + 1)
A4123 = stir_seq(lambda j: 2**j // 2 if j else 1, 220)              # e.g.f. 1/(3-2e^x) : g_j = 2^j ... à valider
A6531 = stir_seq(cat, 220, sign=True)
def phi(k): return sum(1 for i in range(1, k + 1) if gcd(i, k) == 1)
def per_ok(s, k):
    t = [x % k for x in s]; P = phi(k)
    return all(t[n] == t[n + P] for n in range(100, len(t) - P))
res["A004123 data"] = A4123[:8]
res["A006531 data"] = A6531[:8]
res["A006531 période | phi(k), k<=60"] = all(per_ok(A6531, k) for k in range(1, 61))
# A033485 : a(2n)/a(n)*log(n)/n
M = 1 << 21; b = [0, 1]
for n in range(2, M + 1): b.append(b[-1] + b[n // 2])
res["A033485 ratio"] = [round(b[2*n] / b[n] * log(n) / n, 5) for n in (1 << 12, 1 << 16, 1 << 20, 3 << 18, 5 << 17)]
# A001462 Golomb : a(n) >= n^(phi-1)
G = [0, 1]
for n in range(2, 10**6 + 1): G.append(1 + G[n - G[G[n - 1]]])
assert G[1:12] == [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]
ph = (1 + 5 ** 0.5) / 2
res["A001462 a(n)>=n^(phi-1), n<1e6"] = all(G[n] >= n ** (ph - 1) for n in range(1, 10**6))
res["A001462 min ratio"] = min(G[n] / n ** (ph - 1) for n in range(1, 10**6))
for k, v in res.items(): print(k, ":", v)
