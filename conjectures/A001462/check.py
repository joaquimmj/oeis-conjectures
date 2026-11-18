# A001462 (Golomb) : conjecture de Song a(n) >= n^(phi-1). Contrôle des étapes de proof.md, en précision 60 chiffres.
from mpmath import mp, mpf, sqrt, power
mp.dps = 60
phi = (1 + sqrt(5)) / 2; al = phi - 1
M = 200000
a = [0, 1]
for n in range(2, M + 1): a.append(1 + a[n - a[a[n - 1]]])
S = [0]
for m in range(1, M + 1): S.append(S[-1] + a[m])                   # S(m) = dernière position de m (A001463)
assert all(a[S[m]] == m and (S[m] + 1 > M or a[S[m] + 1] == m + 1) for m in range(1, 400))
# h(m) = phi^(al-1) (1+1/m)^phi + m^(1-phi) est décroissante ; trouver M0 avec h(M0) <= 1
h = lambda m: power(phi, al - 1) * power(1 + mpf(1) / m, phi) + power(m, 1 - phi)
M0 = next(m for m in range(1, 1000) if h(m) <= 1)
assert all(h(m) >= h(m + 1) for m in range(1, 5000))
# cas de base : P(m) pour m <= max(M0, 1000) (et bien plus loin, par prudence)
for m in range(1, 20001):
    assert power(m, phi) / phi <= S[m] <= power(m, phi), m
# l'énoncé lui-même, directement
assert all(a[n] >= power(n, al) for n in range(1, 20001))
print("M0 =", M0, "; h(M0) =", float(h(M0)), "; P(m) vérifié pour m <= 20000 ; max S(m)/m^phi =",
      float(max(S[m] / power(m, phi) for m in range(1, 20001))))
