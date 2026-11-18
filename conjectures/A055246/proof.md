# A055246 — conjectures de Jeffery (2015) : vraies (élémentaires)

On part de la formule de l'entrée a(n) = 1 + 6c(n), où c = A005836 (c(n) = écriture binaire de n − 1 lue en base 3).
1. **Règles 1, x ↦ 3x − 2, x ↦ 3x + 4.** A005836 est engendrée par 0, c ↦ 3c, c ↦ 3c + 1 (ajout d'un chiffre 0
   ou 1 à droite). Or 3(1 + 6c) − 2 = 1 + 6(3c) et 3(1 + 6c) + 4 = 1 + 6(3c + 1).
2. **a(n) = 2·A191107(n) − 1.** A191107 (règles 1, 3x − 2, 3x + 1) vaut 1 + 3c(n) par le même argument, et
   2(1 + 3c) − 1 = 1 + 6c.
3. **a(n) = 6·A003278(n) − 5.** A003278(n) = c(n) + 1 (définition de l'entrée), et 6(c + 1) − 5 = 1 + 6c.
4. **a(n) = (a((2n−1)·2^(k−1)) + 2)/3^k.** (2n−1)·2^(k−1) − 1 = (n−1)·2^k + 2^(k−1) − 1 s'écrit en binaire comme
   n − 1 suivi de « 0 » puis de k − 1 chiffres 1. Donc c((2n−1)·2^(k−1)) = 3^k·c(n) + (3^(k−1) − 1)/2, et
   1 + 6·c(…) + 2 = 3^k·(6c(n) + 1). ∎

**Contrôle** : `check.py`.
