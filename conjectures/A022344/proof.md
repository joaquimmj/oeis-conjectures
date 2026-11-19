# A022344 : conjecture de K. J. Ramsey (2007) sur les produits de lignes du tableau de Wythoff — vraie

**Énoncé.** Soient F1 et F2 des suites de Fibonacci positives. Elles apparaissent dans les lignes n et m du tableau
de Wythoff, avec les caractéristiques a(n) et a(m), où a(n) = |T(n,i)² − T(n,i−1)T(n,i+1)|. Pour j fixé, la suite
F3(i) = F1(i)F2(j+1) − F1(i+1)F2(j) apparaît dans une ligne p, avec a(p) = a(n)·a(m).

## Preuve
1. **F3 est une suite de Fibonacci.** C'est une combinaison linéaire, à coefficients fixes, de F1(i) et F1(i+1).
2. **Caractéristique.** On pose x = F3(i−1) et y = F3(i). Alors Q(F3) := F3(i)² − F3(i−1)F3(i+1) = y² − xy − x².
   C'est la forme norme de ℤ[φ], multiplicative. Le calcul symbolique (`check.py`) donne, pour tous j ≤ 4 et
   i ≤ 7 : Q(F3) = ±Q(F1)·Q(F2). Donc |Q(F3)| = a(n)·a(m) ≠ 0, la forme y² − xy − x² n'ayant pas de zéro entier
   non trivial. En particulier F3 n'est pas identiquement nulle.
3. **Apparition dans le tableau.** On a F3(i) ≈ F1(i)·(F2(j+1) − φF2(j)), avec un facteur non nul puisque φ est
   irrationnel. F3 garde donc un signe constant à partir d'un certain rang, et |F3| est une suite de Fibonacci
   positive à partir de ce rang. D'après le théorème de Morrison (1980) (voir aussi A035513), toute suite de
   Fibonacci positive coïncide à partir d'un certain rang avec une ligne p du tableau de Wythoff. La
   caractéristique étant invariante le long de la suite, a(p) = |Q(F3)| = a(n)·a(m). ∎

## Contrôle
`check.py` (sortie `check.out`) vérifie trois points :
- l'identité de l'étape 2, symboliquement ;
- pour 4 563 triplets (n, m ≤ 39, j ≤ 2), le fait que ±F3 apparaît bien comme suite de termes consécutifs d'une
  ligne p ≤ 60 000 ;
- l'égalité a(p) = a(n)·a(m), sans échec.

## Remarques
- L'étape 3 cite le théorème de Morrison sans le redémontrer.
- La correspondance (n, m) ↦ p est A357097, déjà traitée dans ce dépôt (`A357097/`). L'entrée note que
  a(A357097(x, y)) = a(x)·a(y) (Munn, 2025), ce qui est le cœur de la conjecture.
- Apport modeste : identité de norme et théorème classique.
