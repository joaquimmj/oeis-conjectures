# A078841 : a(n) = (n+1)-ième entier avec Omega = n. Contrôle de a(n) = 2^n * t_{n+1}, où t_1 <= t_2 <= ... est
# l'énumération croissante (avec multiplicité) de V = {u / 2^Omega(u) : u impair >= 1} (proof.md).
from fractions import Fraction as F
import json, sympy
U = 2_000_000
Om = [0] * (U + 1)
for p in sympy.primerange(2, U + 1):
    pk = p
    while pk <= U:
        for m in range(pk, U + 1, pk): Om[m] += 1
        pk *= p
# éléments de V <= Y : u <= 2^Omega(u) * Y ; on se limite à u <= U, ce qui est complet pour Y <= U / 2^Omega max ;
# on garde Y = 1000 et on vérifie la complétude : u/2^j <= 1000 avec u > U impose 2^j > 2000, j >= 11, u >= 3^11 = 177147 :
# pas complet a priori, donc on teste explicitement u jusqu'à U et on ne compare que les t <= Y0 tels que 2^j Y0 <= U pour tout j possible.
vals = sorted(F(u, 2**Om[u]) for u in range(1, U + 1, 2) if F(u, 2**Om[u]) <= 400)
# complétude : un u impair avec u/2^j <= 400 vérifie 3^j <= 400 * 2^j, donc j <= 14, d'où u <= 400 * 2^14 = 6 553 600 > U ;
# on ne garde donc que les valeurs <= U / 2^14 = 122 (complètes).
Ymax = F(U, 2**14)
vals = [v for v in vals if v <= Ymax]
E = json.load(open("A078841.json"))
data = [int(x) for x in E["data"].split(",")]
ok = all(data[n] == 2**n * vals[n] for n in range(len(data)) if n < len(vals) and vals[n] <= Ymax)
print("a(n) = 2^n t_{n+1} pour les", sum(1 for n in range(len(data)) if n < len(vals)), "premiers termes :", ok)
r = [float(vals[i+1] / vals[i]) for i in range(len(vals) - 1)]
print("nombre d'éléments de V <= %s : %d ; max t_{k+1}/t_k sur la seconde moitié : %.5f" % (Ymax, len(vals), max(r[len(r)//2:])))
