# A161580 (et A161579, A161817, A162311) — conjecture de Shevelev (2009) : vraie, preuve Walnut

**Énoncé.** Pour k impair fixé, dans la suite croissante des n tels que t(n) = t(n+k) (A161579 pour k = 3,
A161817 pour k = 5, A162311 pour k = 7), les nombres odieux et maléfiques alternent. A161580 énonce la
même chose pour les n tels que t(n) + t(n+k) = 1.

**Statut.** La première variante est prouvée par Allouche (J. Théor. Nombres Bordeaux 27, 2015), cité dans
A161579, A161817 et A162311. A161580 ne cite rien. Je n'ai pas vérifié dans l'article si la seconde variante y figure.

**Preuve Walnut (base 2), pour tous les k impairs à la fois** (`A161580.wal`, `A161580.out`) : l'énoncé
« si n < m sont deux termes consécutifs, alors t(n) ≠ t(m) » est du premier ordre en (k, n, m).
shev_same : TRUE. shev_diff : TRUE. Témoin sans l'hypothèse « k impair » : FALSE. ∎
**Contrôle indépendant** : `check.py`.
