# A100036, A100037, A100038, A100039 : formules conjecturées par R. Stephan (2007) — vraies

**Suite de base A100035.** a(1) = 1. a(n+1) est le plus grand y < a(n) jamais adjacent à a(n) jusqu'ici, ou à
défaut le plus petit y > a(n) jamais adjacent. A100036 à A100039 donnent les positions de la 1ʳᵉ, 2ᵉ, 3ᵉ et 4ᵉ
« copie » gloutonne de 1, 2, 3, … dans A100035.

## Théorème 1 (structure explicite)
A100035 est la concaténation des blocs B₁ = (1, 2, 3) et, pour k ≥ 2 avec m = 2k :

  B_k = (1, m, m−1, m+1, m, m−2, m+1, m−3, m, m−4, …, m+1, 2, m+1).

Après les quatre premiers termes viennent les paires (h_j, m−j) pour j = 2, …, m−2, avec h_j = m si j est pair
et m+1 sinon. Le bloc B_k a une longueur de 4k − 1 et commence à la position s_k = 2k² − 3k + 2.

*Preuve, par récurrence sur k.* **Invariant :** juste après le dernier terme de B_k, les paires {x, y} déjà
adjacentes sont exactement toutes les paires avec 1 ≤ x < y ≤ 2k+1, et la transition vers le 1 suivant ajoute
{2k+1, 1}. En effet, B_k ajoute {1, m} (et {m−1, 1} à son entrée), {m, x} pour x ≤ m−1, {m+1, x} pour 2 ≤ x ≤ m−1,
et {m, m+1}. Cela fait 2m − 1 paires nouvelles, autant que de transitions.

Sous cet invariant, avec M = m + 2 pour le bloc suivant, chaque pas est le choix glouton :
- en 1, toutes les valeurs de 2 à M−1 sont déjà voisines, donc on monte en M ;
- en M (nouveau), le plus grand candidat inférieur est M−1 ;
- en M−1 (ancien), tout ce qui est plus petit est déjà voisin, et M aussi, donc on monte en M+1 ;
- en M+1, on descend en M ;
- en une valeur haute h ∈ {M, M+1}, on descend vers la plus grande valeur basse non encore voisine de h, qui
  est la suivante dans la liste décroissante ;
- en une valeur basse x ≤ M−2, toutes les plus petites sont déjà voisines (invariant). Comme x vient d'être
  adjacent à une valeur haute, on monte vers l'autre valeur haute ;
- enfin, en M+1 après la valeur basse 2, le seul candidat inférieur restant est 1 : le bloc suivant commence.

Le bloc B₂ = (1, 4, 3, 5, 4, 2, 5) se vérifie à la main. ∎

## Conséquences : formules de Stephan
Dans B_k, la valeur basse n (2 ≤ n ≤ 2k−2) est à la position s_k + 4k − 2n + 1. Les valeurs hautes de B_k sont
2k et 2k+1, et les valeurs basses décroissent. Pour la r-ième copie gloutonne (r = 2, 3, 4), après la valeur n−1
située dans le bloc B_{n−1+r−1}, la prochaine occurrence de n est donc la valeur basse n du bloc suivant.
- **A100037** (bloc n) : s_n + 2n + 1 = **2n² − n + 3**.
- **A100038** (bloc n+1) : **2n² + 3n + 6**.
- **A100039** (bloc n+2) : **2n² + 7n + 13**.
- **A100036** (premières occurrences) : 2k apparaît d'abord en position s_k + 1 = 2k² − 3k + 3 = A096376(k−1),
  et 2k+1 en position s_k + 3 = A096376(k−1) + 2. Les différences successives valent donc 2 (n impair) et
  2n − 7 (n pair), après le début 1, 1, 1, 2, 2. C'est la conjecture de Stephan : les « partial sums of
  [1,1,1,2,2,5,2,9,2,13,…] ». Le terme général imprimé « n/2−7 » est vraisemblablement une coquille pour 2n−7.

## Contrôle
`check.py` vérifie trois choses :
- la description des blocs coïncide avec la définition gloutonne (`sim.py`) sur 2·10⁵ termes ;
- les trois formules quadratiques, pour n < 200 ;
- les différences de A100036, pour n < 400.
