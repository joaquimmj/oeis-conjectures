# A057194 et A216151 : conjecture de J. Perry (2012), A057194(n) < A216151(n) pour n > 1 — vraie (immédiate)

Les deux suites vérifient x(n+1) = (Π_{k≤n} x(k))·(Σ_{k≤n} x(k)), avec x(1) = 1, et x(2) = 1 pour A057194
(puisque 1·1 = 1) mais x(2) = 2 pour A216151.

Tous les termes sont positifs. Supposons a(k) ≤ b(k) pour tout k ≤ n, avec a(2) < b(2) et n ≥ 2. Alors le
produit et la somme des n premiers termes sont strictement plus grands pour b, donc a(n+1) < b(n+1). Par
récurrence, a(n) < b(n) pour tout n > 1. ∎

Contrôle : `check.py` (12 termes). Apport nul : l'argument tient en une ligne.
