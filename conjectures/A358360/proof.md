# A358360 — les cinq conjectures d'Oudra (2026) : vraies

a(n) = ν₃(D(n)), où D(n) est le n-ième nombre de Delannoy central (D(n) = Pₙ(3), polynôme de Legendre).
**Résultats utilisés** (Alekseyev, Amdeberhan, Shallit, Vukusic, Res. Number Theory 12 (2026), arXiv:2505.08935,
lus le 18/11) :
- Théorème 4 : a(2m) = ν₃(C(2m, m)) et a(2m+1) = 1 + ν₃(2m+1) + ν₃(C(2m, m)).
- Théorème 6 (p = 3) : a(3n + r) = a(n) + (n mod 2) si r ∈ {0, 2}, et a(3n + 1) = a(n) + 1 − (n mod 2).

**(4) a(2n) = A000989(n).** C'est le théorème 4, car A000989(n) = ν₃(C(2n, n)).

**(5) a(2n+1) = A000989(n) + A254046(n+1).** Il suffit de voir que A254046(m) = 1 + ν₃(2m − 1). La suite
A254046 est définie par a(3j) = a(3j+1) = 1 et a(3j+2) = 1 + a(j+1). Or 2(3j) − 1 et 2(3j+1) − 1 ne sont pas
divisibles par 3, et 2(3j+2) − 1 = 3(2(j+1) − 1). Les deux suites vérifient donc la même récurrence.
Avec m = n + 1, on retrouve le théorème 4.

**(3) a(n) = A000989(⌊(n+1)/2⌋) + A168570(n+1).** A168570(k) = ν₃(2^k − 1) vaut 0 si k est impair, et
ν₃(4^j − 1) = 1 + ν₃(j) si k = 2j (lemme LTE). Pour n = 2m, on obtient A000989(m), qui est (4). Pour n = 2m + 1, on
obtient ν₃(C(2m+2, m+1)) + 1 + ν₃(m+1). Comme C(2m+2, m+1) = C(2m, m)·2(2m+1)/(m+1), cela vaut
ν₃(C(2m, m)) + ν₃(2m+1) + 1, qui est le théorème 4.

**(2) a(n) = Σ_{k≥0} (⌊n/3^k⌋ mod 2).** Soit g(n) le membre de droite. Alors g(0) = 0 = a(0) et
g(3n + r) = ((3n + r) mod 2) + g(n), avec (3n + r) mod 2 = n mod 2 si r est pair et 1 − (n mod 2) si r = 1.
C'est la récurrence du théorème 6, donc g = a.

**(1) a(n) = Σ_{k=1..n} (−1)^{k+1}·A051064(k).** A051064(k) = 1 + ν₃(k) = #{j ≥ 0 : 3^j | k}. En échangeant les
sommes, on obtient Σ_j Σ_{i ≤ ⌊n/3^j⌋} (−1)^{3^j·i + 1} = Σ_j Σ_{i ≤ ⌊n/3^j⌋} (−1)^{i+1}, car 3^j est impair, et
la somme intérieure vaut ⌊n/3^j⌋ mod 2. On retrouve g(n). ∎

**Contrôle** : `check.py` (les deux théorèmes cités, les lemmes et les cinq formules, depuis la définition).
