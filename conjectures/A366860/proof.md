# A366860, A366870, A366871 — conjectures de Gutkovskiy (2023) : vraies, et pour tout k

**Énoncé.** Pour k ≥ 1 : a_k(0) = 0, a_k(n) = n − a_k(⌊a_k(n−1)/k⌋). Les entrées A366860, A366870 et A366871
(k = 3, 4, 5) conjecturent a_k(n) ~ c_k·n. k = 2 est A286389 (Shallit 2023 avec Walnut) et k = 1 est la
fonction G de Hofstadter (A005206).

**Théorème.** Soit σ_k : 0 → 1^k, 1 → 1^k 0 et w = w_1 w_2 … son point fixe commençant par 1. Alors pour tout
n ≥ 0, a_k(n) = w_1 + … + w_n. En particulier a_k(n)/n → c_k = (√(k²+4k) − k)/2, racine positive de c² + kc − k.
Cela donne c_3 = (√21 − 3)/2, c_4 = 2(√2 − 1), c_5 = (3√5 − 5)/2 (les trois conjectures), c_2 = √3 − 1 et
c_1 = (√5 − 1)/2.

**Preuve.** Soit b(n) = w_1 + … + w_n. La récurrence détermine a_k, il suffit donc de montrer que
b(n) = n − b(⌊b(n−1)/k⌋) pour n ≥ 1. Comme w = σ(w), w est la concaténation des blocs σ(w_1) σ(w_2) … :
chaque bloc commence par k lettres 1 et, si w_j = 1, se termine par un 0, qui est son seul 0.
Fixons n ≥ 1 et écrivons le préfixe de longueur n − 1 comme j blocs complets suivis de r lettres du bloc j + 1
(0 ≤ r < |σ(w_{j+1})|). Alors b(n−1) = kj + r avec r ≤ k. Le nombre de 0 dans le préfixe de longueur n,
n − b(n), est le nombre de blocs complets de lettre 1 qu'il contient.
- Si r < k : ⌊b(n−1)/k⌋ = j et la lettre n est un 1 du bloc j + 1. Ce bloc n'est complet que si c'est σ(0),
  qui n'a pas de 0. Donc n − b(n) = #{i ≤ j : w_i = 1} = b(j).
- Si r = k : le bloc j + 1 est σ(1) et la lettre n est son 0 final. Donc ⌊b(n−1)/k⌋ = j + 1 et
  n − b(n) = b(j + 1).
Dans les deux cas, n − b(n) = b(⌊b(n−1)/k⌋). La matrice de σ_k, [[0, 1], [k, k]], est primitive. Par
Perron–Frobenius, la fréquence de 1 dans w existe et vaut λ/(1 + λ), où λ = (k + √(k²+4k))/2, ce qui donne
c_k = (√(k²+4k) − k)/2. ∎

**Remarques.**
- Le second conjugué λ' = −k/λ vérifie |λ'| < 1 (σ_k est de Pisot), donc a_k(n) − c_k·n est même borné.
  Je ne l'ai pas rédigé en détail.
- Pour k = 2, cela redonne la conjecture d'Irvine (A286389 = sommes partielles de A285431) que Shallit a prouvée
  avec Walnut. Ici la preuve est courte, à la main, et vaut pour tout k.
- Pas de preuve Walnut indépendante (il faudrait une numération de Dumont–Thomas pour chaque k).

**Contrôle** : `guess.py` (k = 2 à 7 sur 10^6 termes, k = 8 à 30 sur 10^5, depuis la définition).
