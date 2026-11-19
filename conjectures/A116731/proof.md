# A116731 : conjecture de W. Meeussen (2008) — vraie

**Énoncé.** Le nombre de couples distincts (échanges, itérations) produits par le tri à bulles sur les n!
permutations de [n] est égal à a(n) = (n³ − 3n² + 5n)/3. C'est le nombre de permutations évitant
{321, 2143, 3124}, d'après la formule établie de l'entrée.

## Preuve
1. **Table d'inversions.** Soit L_i le nombre d'éléments plus grands que π_i situés à sa gauche. L'application
   π ↦ (L₁, …, L_n) est une bijection sur Π_i [0, i−1]. Le tri à bulles effectue Σ L_i échanges, et le nombre de
   passes avec échange vaut max L_i (Knuth, TAOCP 5.2.2 : chaque passe diminue de 1 chaque entrée positive de la
   table). Si le programme compte aussi la passe finale sans échange, le nombre d'itérations est une fonction
   injective de max L_i, ce qui ne change pas le nombre de couples.
2. **Couples atteignables.** Pour max L = P (0 ≤ P ≤ n−1) :
   - la somme minimale est P (une seule entrée égale à P) ;
   - la somme maximale est Σ_i min(i−1, P) = P(P+1)/2 + P(n−1−P) ;
   - toute valeur intermédiaire est atteinte, en diminuant une entrée de 1 à la fois sans toucher au maximum.
3. **Total.** Σ_{P=0}^{n−1} (Σ_i min(i−1, P) − P + 1) = n(n² − 3n + 5)/3 = a(n). ∎

## Contrôle
`check.py` vérifie trois choses :
- une simulation directe du tri à bulles pour n ≤ 9 ;
- l'identité (échanges, passes) = (Σ L, max L) pour n ≤ 8 ;
- la formule, sur les 44 termes de l'entrée.
