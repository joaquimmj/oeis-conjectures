# A298173, A298741 : « It appears that a(n)/a(n−1) → k and that a(n) − k·a(n−1) is unbounded »

**Définitions.** a(0) = 1 et b(0) = 2. Pour n ≥ 1, b(n) est le plus petit entier positif non placé, puis :
- A298173 : a(n) = 3a(n−1) + Σ_{j=0}^{n} (−1)^j b(n−j) ;
- A298741 : a(n) = 2a(n−1) + 2b(n) + Σ_{j=1}^{n} (−1)^j b(n−j).

**Théorème.** Les deux énoncés sont **vrais**. Plus précisément :
- A298173 : ⌈n/2⌉ ≤ a(n) − 3a(n−1) ≤ 2n + 1 ;
- A298741 : n + 1 ≤ a(n) − 2a(n−1) ≤ 4n + 2.

## Preuve
1. **Majoration de b.** Pour n ≥ 1, quand b(n) est choisi, exactement 2n entiers sont placés : a(0), …, a(n−1)
   et b(0), …, b(n−1). Le plus petit entier libre vérifie donc b(n) ≤ 2n + 1.
2. **Somme alternée.** Soit S(n) = Σ_{j=0}^{n} (−1)^j b(n−j). Comme b est strictement croissante, on peut
   regrouper les termes en paires b(n−2i) − b(n−2i−1) ≥ 1, plus b(0) = 2 si n est pair. D'où S(n) ≥ ⌈n/2⌉.
   Dans l'autre sens, S(n) = b(n) − [b(n−1) − b(n−2)] − …, où chaque crochet est ≥ 1 et où le dernier terme
   vaut −b(0) si n est impair. D'où S(n) ≤ b(n) ≤ 2n + 1.
3. **A298173.** a(n) − 3a(n−1) = S(n), ce qui donne l'encadrement ; la différence est donc non bornée. De plus
   a(n) ≥ 3a(n−1), d'où a(n) ≥ 3ⁿ, et a(n)/a(n−1) = 3 + S(n)/a(n−1) = 3 + O(n/3ⁿ) → 3.
4. **A298741.** a(n) − 2a(n−1) = b(n) + S(n), avec n + 1 ≤ b(n) + S(n) ≤ 4n + 2, puisque b(n) ≥ n + 1. On
   conclut de même : a(n) ≥ 2ⁿ et a(n)/a(n−1) → 2. ∎

## Contrôle
`check.py` génère les deux suites depuis la définition (400 termes) et vérifie les données OEIS, la majoration
b(n) ≤ 2n + 1 et les encadrements de a(n) − k·a(n−1).

## Limites
Énoncés présentés comme « It appears » (il n'y a pas de mot « Conjecture ») ; la preuve est élémentaire.
