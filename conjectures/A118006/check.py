# Équation de Hebisch–Rubey (corrigée par Somos), testée sur les coefficients,
# à partir de la définition w(1)=01, w(n+1)=w(n)w(n)reverse(w(n)).
import sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
w = "01"
while len(w) < N + 10: w = w + w + w[::-1]
import re, os
oeis = [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(os.path.join(os.path.dirname(__file__), "../phase0/A118006.txt")) if l[:2] in ("%S","%T","%U")))]  # données de l'entrée, a(1), a(2), ...
assert [int(c) for c in w[:len(oeis)]] == oeis
def coeffs(shift):  # f(x) = sum_{n>=1} a(n) x^(n+shift)
    c = [0] * (N + 1)
    for n in range(1, N + 1):
        if 0 <= n + shift <= N: c[n + shift] = int(w[n - 1])
    return c
p = lambda n: 0 if n == 0 else (2 if n % 6 in (3, 4) else 1)   # x(1+x)(1+x^2)^2/(1-x^6)
for shift in (0, -1):
    f = coeffs(shift); g = lambda m: f[m] if m >= 0 else 0
    bad = [n for n in range(N) if g(n) + g(n-1) + g(n-2) - (f[(n-2)//3] if n >= 2 and (n-2) % 3 == 0 else 0) != p(n)]
    print(f"f = sum a(n) x^(n{shift:+d}):", "OK" if not bad else f"{len(bad)} échecs, premiers {bad[:8]}")
