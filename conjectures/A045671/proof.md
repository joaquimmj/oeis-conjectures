# A045671, A045672 : conjectures de C. Kimberling (2017) — vraies

**Définition** (Fraenkel, suites (s,t) avec s = t = 2). a(0) = b(0) = 0, a(n) = mex{a(i), b(i) : i < n},
b(n) = 2a(n) + 2n.

**Conjectures.**
1. Pour n ≥ 1, a(n) (resp. b(n)) est la position du n-ième 1 (resp. 0) dans le point fixe w = 1110 1110 1110 11 …
   de σ : 0 → 11, 1 → 1110. Kimberling marque lui-même cette identification « conjectured ».
2. −1 < n·r − a(n) < 2 avec r = (1+√17)/4, et −1 < n·r − b(n) < 3 avec r = (5+√17)/2.

## 1. Identification morphique
Soient a′(n) et b′(n) les positions des n-ièmes 1 et 0 de w = σ(w).
- Chaque 1 de w engendre « 1110 » et chaque 0 engendre « 11 ». Les 0 de w sont donc les dernières lettres des
  blocs issus des 1 : le n-ième 0 est dans le bloc du n-ième 1, d'où b′(n) > a′(n). Il n'y a jamais « 00 ».
- Deux 1 consécutifs de w sont à distance d ∈ {1, 2}. Les 0 correspondants sont à distance 4 (« 1110 », « 1110 »)
  ou 6 (« 1110 », « 11 », « 1110 »), soit 2d + 2. Avec a′(0) = b′(0) = 0 et b′(1) = 4, on obtient par télescopage
  b′(n) = 2a′(n) + 2n.
- Les deux suites sont complémentaires, et b′(j) < a′(n) entraîne j < n. Donc a′(n) = mex{a′(i), b′(i) : i < n}.

Les règles de définition déterminent les suites de façon unique, donc a = a′ et b = b′. ∎

## 2. Bornes exactes
La matrice d'incidence [[0, 1], [2, 3]] a pour valeurs propres (3 ± √17)/2, dont une de module < 1 : le morphisme
est de Pisot. L'outil exact du lot 6 (`python/discrepancy_exact.py`, formule de Dumont–Thomas dans ℚ(√17))
donne (`bounds.py`, `bounds.out`) :
- pour a = A045671 : inf D = −(9 + √17)/32 ≈ −0,4101 et sup D = (27 + 3√17)/32 ≈ 1,2303, compris dans (−1, 2) ;
- pour b = A045672 : inf D = −(9 + √17)/16 ≈ −0,8202 et sup D = (27 + 3√17)/16 ≈ 2,4606, compris dans (−1, 3).

Pour n = 0, D = 0. Les deux encadrements sont donc vrais, avec des bornes optimales plus fines.

## Contrôles
- `check.py` : égalité avec le mot et avec les données OEIS sur 5·10⁴ termes, et les faits structurels.
- `dt_check` (dans `bounds.py`) : la formule de Dumont–Thomas est vérifiée sur 2·10⁵ lettres, avec les valeurs
  observées −0,4048…1,2265 et −0,8065…2,4418.

## Remarque
Artstein-Avidan, Fraenkel et Sós (2008) étudient cette famille. Nous n'avons pas vérifié si leur article contient
déjà ces énoncés.
