# Équations complémentaires de Kimberling : a(n)/a(n−1) → φ (90 entrées, dont 65 étiquetées « Conjecture »)

**Entrées.** A293057, A293058, A293076, A293316, A293317, A293349–A293351, A293357, A293358, A293406,
A293765–A293767, A294365–A294368, A294413–A294426, A294532–A294551, A294553–A294565 : la conjecture
« a(n)/a(n−1) → (1+√5)/2 » y est écrite explicitement (65 entrées). A294170, A294552, A295357, A295754, A295862,
A295947–A295953, A295960, A296245, A296251, A296257, A296266, A296272, A296278, A296284, A296288, A296292,
A296555, A296776, A296843 : la même limite y est affirmée sans preuve ni mention de conjecture (25 entrées).
Liste et formules : `results.json` (sortie de `compute.py`).

**Cadre.** a et b sont deux suites strictement croissantes d'entiers positifs, complémentaires (chaque entier
≥ 1 est dans exactement une des deux). Pour n ≥ n₀ (n₀ = nombre de valeurs initiales de a) :

  a(n) = Σᵢ cᵢ a(n−i) + g(n),

où g est un polynôme, de degré D, en n et en un nombre fini de b(n+j) (j ∈ {−4,…,1}). Pour 89 entrées,
Σ cᵢ a(n−i) = a(n−1) + a(n−2), de polynôme caractéristique P = x² − x − 1. Pour A295754, c'est
a(n−1) + a(n−3) + a(n−4), avec P = (x² − x − 1)(x² + 1).

**Théorème.** Pour chacune des 90 entrées, a(n)/a(n−1) → φ. Plus précisément,
a(n)/a(n−1) − φ = O(n^{D+1}·r⁻ⁿ), avec r = φ (r = 1,4655… pour A295754).

## Preuve

**Lemme 1 (comptage).** Si a(m) ≥ 2m + 2, alors b(m) ≤ 2m + 1.
En effet, les valeurs de a dans [1, 2m+1] sont parmi a(0), …, a(m−1), puisque a(m) > 2m+1. Il y en a donc au plus
m, et au moins m+1 entiers de [1, 2m+1] sont dans b. Le (m+1)-ième élément de b, b(m), est donc ≤ 2m+1.

**Étape 1 : g(n) ≥ 0 (toutes les entrées sauf A294413).** On a b(k) ≥ k+1, puisque b(0) ≥ 1 et que b est
strictement croissante, et b(k+1) ≥ b(k) + 1. On pose b(n+j) = n + j + 1 + u_j, où u est positive et croissante, et
on écrit u en sommes partielles de variables tᵢ ≥ 0, avec n = n₀ + m. g devient alors un polynôme en (m, t) dont
tous les coefficients non constants sont ≥ 0 (vérifié par `compute.py`, qui utilise sympy). Donc g(n) ≥ g_min,
avec g_min ≥ 0 dans chaque cas (colonne « g>= » de la sortie ; exemple : 2b(n−1) − b(n−2) − 2 ≥ b(n−1) − 1 ≥ 0).

**Étape 2 : croissance exponentielle.** Comme g ≥ 0, on a a(n) ≥ a(n−1) + a(n−2), avec a(0), a(1) ≥ 1, donc
a(n) ≥ F(n+1) ≥ φ^{n−1}. Pour A295754, a(n) ≥ a(n−1) + a(n−3), d'où a(n) ≥ c·rⁿ, avec r la racine réelle de
x³ = x² + 1.

**Étape 3 : b est linéaire.** Par l'étape 2, a(m) ≥ 2m + 2 pour m assez grand, donc b(m) ≤ 2m + 1 par le lemme 1.
Ainsi |g(n)| ≤ K·n^D pour n ≥ 1.

**Étape 4 : l'erreur e(n) = a(n) − φ a(n−1).** On écrit P = (x − φ)Q. Alors e vérifie la récurrence de polynôme
caractéristique Q avec le même second membre g. Pour x² − x − 1 : comme φ + ψ = 1 et φψ = −1, avec ψ = −1/φ,
on obtient e(n) = ψ e(n−1) + g(n). Pour A295754 : Q = (x − ψ)(x² + 1), dont les racines ψ, i et −i sont simples et
de module ≤ 1. Dans les deux cas, la réponse impulsionnelle h de Q est bornée, d'où
|e(n)| ≤ H + ‖h‖_∞ Σ_{k≤n} |g(k)| = O(n^{D+1}).

**Conclusion.** a(n)/a(n−1) − φ = e(n)/a(n−1) = O(n^{D+1}/r^{n}) → 0. ∎

**Cas A294413 : a(n) = a(n−1) + a(n−2) − b(n−1) + 6.** Ici g n'est pas minoré a priori. On montre par récurrence
H(n) : a(n) ≥ 4n pour n ≥ 5. La base est a(5) = 23 et a(6) = 35. Pour l'hérédité, supposons H(n−1) et H(n−2),
avec n ≥ 7. Alors a(n−1) ≥ 4n − 4 ≥ 2n, donc b(n−1) ≤ 2n − 1 par le lemme 1 (indice m = n−1). D'où
a(n) ≥ (4n − 4) + (4n − 8) + 6 − (2n − 1) = 6n − 5 ≥ 4n. On a donc g(n) ≥ 7 − 2n pour n ≥ 7, ce qui donne
a(n) ≥ a(n−1) + a(n−2) − 2n. Avec d(n) = a(n) − 2n − 6, on obtient d(n) ≥ d(n−1) + d(n−2), et d(5) = 7,
d(6) = 17 > 0. Donc d, et a avec elle, croît au moins comme φⁿ. Les étapes 3 et 4 s'appliquent ensuite sans
changement (D = 1).

## Contrôles

- `compute.py` : calcule chaque suite depuis sa définition (400 termes). Il vérifie que chaque a(n) dépasse les
  b provisoires utilisés, ce qui garantit la cohérence du calcul avec la complémentarité, et que les b initiaux
  donnés sont bien ceux du complément. Il compare le résultat aux données OEIS (90/90 identiques) et établit la
  minoration de g de l'étape 1, ainsi que le polynôme P. Sortie : `results.json`.
- `check.py` : second générateur, indépendant (formule lue par sympy.sympify, crible sur un tableau). Il recalcule
  600 termes et vérifie de nouveau les données, |e(n)| ≤ 50·n^{D+1}, |a(599)/a(598) − φ| < 10⁻⁸⁰ et la base de
  récurrence de A294413. Résultat : 0 échec (`check.out`).

## Limites

- La preuve est élémentaire et vaut pour toute équation de cette forme dont le second membre g est minoré.
  Kimberling ne l'a probablement pas jugée difficile ; l'apport est d'avoir réglé, avec une preuve écrite, les
  65 entrées où elle est notée « Conjecture ».
- Le théorème suppose l'existence du couple (a, b) complémentaire, que les entrées affirment (« uniquely
  determined ») ; le calcul ne la vérifie que sur un nombre fini de termes. Pour la preuve elle-même, c'est sans
  importance : elle s'applique à tout couple complémentaire qui satisfait l'équation et les valeurs initiales.
  Celles-ci fixent en effet les premiers termes, qui servent de base.
- Preuve relue seulement par l'auteur (une IA).
