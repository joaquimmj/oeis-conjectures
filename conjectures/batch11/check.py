# A084091 (Dirichlet g.f.), A327551 (cycles du mélange parfait), A088226 (formule de Stephan) : contrôles.
from math import isqrt
from sympy import n_order, divisors, totient
# A084091 : a(n) = Sum_{2^k | n} chi3(n/2^k) ; contrôle contre le développement en série de la définition
N = 3000
chi = lambda m: (0, 1, -1)[m % 3]
ser = [0] * (N + 1)
k = 1
while k <= N:
    for m in range(1, N // k + 1): ser[m * k] += chi(m)      # y/(1+y+y^2) = Sum chi(m) y^m, y = x^(2^j)
    k *= 2
d = [0] * (N + 1)
for n in range(1, N + 1):
    v, t = 0, n
    while True:
        v += chi(t)
        if t % 2: break
        t //= 2
    d[n] = v
assert d == ser
# cohérence avec les données de l'entrée
dat = [0,1,0,0,1,-1,0,1,0,0,0,-1,0,1,0,0,1,-1,0,1,-1,0,0,-1,0,1,0,0,1,-1,0]
assert ser[:len(dat)] == dat
# A327551 : simulation du mélange parfait et formule A081844(n-1) + 1
def cycles(n):
    perm = [None] * (2 * n)
    out = [x for i in range(n) for x in (i, n + i)]          # (1, n+1, 2, n+2, ...) en 0-indexé
    seen, c = set(), 0
    for s in range(2 * n):
        if s in seen: continue
        c += 1; x = s
        while x not in seen: seen.add(x); x = out[x]
    return c
A081844 = lambda m: sum(totient(e) // n_order(2, e) if e > 1 else 1 for e in divisors(2 * m + 1))
dat327 = [2,3,3,4,4,3,3,6,4,3,7,4,4,5,3,8,6,7,3,6,4,5,9,4,6,9,3,6,6,3,3,14,8,3]
assert [cycles(n) for n in range(1, len(dat327) + 1)] == dat327
assert all(cycles(n) == A081844(n - 1) + 1 for n in range(1, 600))
# A088226 : récurrence, formule de bloc, et formule de Stephan (avec recherche du décalage)
M = 20000
a = [None, 0, 0, 1]
for n in range(4, M + 1): a.append(abs(a[n-1] - a[n-2] - a[n-3]))
blk = lambda n: next((k - m) if n == k*k + 2*m + 2 else m for k in [isqrt(n - 1)] for m in [(n - k*k - 1) // 2])
assert all(a[n] == blk(n) for n in range(1, M + 1))
def stephan(n):
    t = isqrt(n)
    return (n - t*t) // 2 if (n - t*t) % 2 == 0 else ((t + 1)**2 - n) // 2
for s in range(-3, 4):
    if all(a[n] == stephan(n + s) for n in range(max(1, 1 - s), M - 3)): print("A088226 : a(n) = stephan(n%+d)" % s)
print("A088226 stephan(n) vs a(n), n = 1..12 :", [stephan(n) for n in range(1, 13)], a[1:13])
print("OK A084091, A327551 ; A088226 formule de bloc OK")
