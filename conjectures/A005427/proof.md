# A005427 : conjecture générale de Hadjicostas (2020) sur le problème de Josèphe — vraie pour tout k ≥ 2

**Énoncé** (commentaire de P. Hadjicostas, 22 juillet 2020, « I do not have a general proof »). On place m
personnes en cercle, numérotées de 1 à m, et on retire une personne sur k en commençant à compter en 1. Soit
J_k(m) le survivant. On pose T(1) = 1 et T(n) = ⌈(T(1) + … + T(n−1))/(k−1)⌉. Alors les m ≥ k pour lesquels
J_k(m) ∈ {1, …, k−1} sont exactement les valeurs T(n) ≥ k.

Cas particuliers dans l'OEIS :
- k = 2 : puissances de 2 ;
- k = 3 : A073941/A005428 ;
- k = 4 : A072493/A005427 ;
- k = 5 à 9 : A120160, A120170, A120178, A120186, A120194.

**Théorème.** La conjecture est vraie pour tout k ≥ 2. De plus, pour T(n) ≥ k, on a J_k(T(n)) = r_n + 1, où
r_n = (k−1)T(n) − S(n−1) ∈ {0, …, k−2} et S(n) = T(1) + … + T(n).

## Notations
- La récurrence de Josèphe s'écrit J(1) = 1 et J(m) = ((J(m−1) + k − 1) mod m) + 1.
- r_n ∈ [0, k−2] est le « reste du plafond », d'où T(n+1) = T(n) + t_n avec t_n = ⌈(T(n) − r_n)/(k−1)⌉.
- On a r_{n+1} = r_n + (k−1)t_n − T(n).

## Étape 1 : les petites valeurs (v ≤ k−1), et la base m = k
Tant que T(n) ≤ k−1, on a t_n ∈ {0, 1}, car T(n) − r_n ≤ k−1. Donc T prend chacune des valeurs 1, …, k−1, une
ou plusieurs fois. Pour v ≤ k−1, soit Q(v) la somme partielle S à la dernière occurrence de v. Le terme suivant
vaut v + 1 exactement quand la somme dépasse (k−1)v. Comme les pas valent v ≤ k−1 :

  Q(v) ≡ Q(v−1) (mod v), et Q(v) est le plus petit entier > (k−1)v dans cette classe ; donc (k−1)v < Q(v) ≤ kv.
  On a Q(0) = 0, puis Q(1) = k.

**Lemme 1.** Pour 1 ≤ v ≤ k−1, J(v) = kv + 1 − Q(v).
*Preuve.* Pour v = 1 : J(1) = 1 = k + 1 − Q(1). Pour l'hérédité, on part de J(v−1) + k − 1 = kv − Q(v−1). Comme
Q(v) ≡ Q(v−1) (mod v) et que 0 ≤ kv − Q(v) ≤ v − 1, on obtient
(J(v−1) + k − 1) mod v = (kv − Q(v−1)) mod v = kv − Q(v). D'où J(v) = kv − Q(v) + 1. ∎

**Base.** Après la dernière occurrence de k−1, le terme suivant est T(n₀) = k, car (k−1)² < Q(k−1) ≤ k(k−1). Alors :
- r_{n₀} = k(k−1) − Q(k−1) ∈ [0, k−2] ;
- par le lemme 1, J(k−1) + k − 1 = k(k−1) − Q(k−1) = r_{n₀} < k ;
- donc J(k) = r_{n₀} + 1 ≤ k−1.

T(n₀) = k est la première valeur ≥ k, et k est bien dans l'ensemble de Josèphe.

## Étape 2 : de T(n) à T(n+1), pour T(n) ≥ k
Pour m ≥ k−1, comme J(m−1) ≤ m − 1, on a J(m−1) + k − 1 < 2m : il y a au plus un tour par étape. Supposons
J(m₀) = j = r_n + 1, avec m₀ = T(n) ≥ k. Alors :
- tant que j + (k−1)s ≤ m₀, c'est-à-dire pour s ≤ t_n − 1 = ⌊(m₀ − j)/(k−1)⌋, on a J(m₀ + s) = j + ks ≥ k + 1 : aucun
  de ces m n'est dans l'ensemble ;
- pour s = t_n, on a j + kt_n − 1 ≥ m₀ + t_n, d'où un tour :
  J(m₀ + t_n) = j + kt_n − (m₀ + t_n) = r_n + 1 + (k−1)t_n − T(n) = r_{n+1} + 1 ∈ [1, k−1].

Comme m₀ + t_n = T(n+1) et t_n ≥ 1 (car T(n) ≥ k > r_n), la suite est strictement croissante à partir de là. Par
récurrence, les m ≥ k avec J(m) ≤ k−1 sont exactement les T(n) ≥ k. ∎

## Contrôles
`check.py` vérifie trois choses, depuis les définitions :
- l'égalité des ensembles pour k = 2..30 et m ≤ 10⁶ ;
- le lemme 1, pour k = 2..60 ;
- l'invariant J(T(n)) = r_n + 1 pour k ≤ T(n) ≤ 2000 et k = 2..60.

## Remarques
- Hadjicostas pensait que la méthode de Schuh (1968) pour k = 3 donnerait des indices. La preuve ci-dessus est
  directe : la récurrence de Josèphe, regardée aux instants où le survivant est petit, coïncide exactement avec
  la récurrence du plafond de T. C'est le principe de l'algorithme de Burde–Thériault, mais avec l'identification
  explicite j = r + 1, qui ferme la preuve.
- **Nouveauté non vérifiée hors de l'OEIS.** Il faut vérifier que Burde (1987), Thériault ou Odlyzko–Wilf (1991)
  ne contiennent pas déjà l'énoncé général.
- Preuve relue seulement par l'auteur (une IA).

## Antériorité (ajoutée après coup)
Voir `paper/parts/part3a.tex`. Le résultat découle d'un théorème classique : la formule d'Odlyzko–Wilf pour Josèphe, et l'asymptotique de de Bruijn (1948) pour A033485. La preuve ci-dessus est indépendante, mais elle n'est pas la première.
