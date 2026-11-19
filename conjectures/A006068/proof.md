# A006068 (Gray inverse) — conjecture de Kurkov (2023) : vraie

**Énoncé.** a(n) = a(A053645(A063946(n))) + A053644(n) pour n > 0 : on complémente le 2e bit de n, on retire le bit
de tête, et l'on ajoute le bit de tête de n.

**Preuve Walnut (base 2)** (`A006068.wal`, `A006068.out`). Le Gray inverse est la relation synchronisée `igray.txt`
(bit i de a = XOR des bits de n de rang ≥ i), contrôlée par sa fonctionnalité et les récurrences a(2n), a(2n+1)
(TRUE). Contrôle des définitions de A063946 et A053645 sur des valeurs (TRUE). Énoncé : TRUE. Témoin sans le
complément du 2e bit : FALSE. ∎
**Note technique.** Walnut ordonne les variables libres d'un `def` alphabétiquement ; les noms sont choisis en
conséquence (cela a été vérifié aussi pour les scripts précédents).
**Contrôle indépendant** : Python, n < 2^16.
