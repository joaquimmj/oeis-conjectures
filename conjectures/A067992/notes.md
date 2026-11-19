# A067992 (Adams-Watters 2006) : deux termes voisins sont-ils premiers entre eux ? — **non résolu**

`search.c` génère la suite. Pour chaque valeur p, il garde un pointeur vers le plus petit v dont le rapport
min/max avec p n'a pas encore servi ; c'est valide parce que les rapports déjà vus le restent. Il teste ensuite
pgcd(a(n−1), a(n)) = 1. Les 40 premiers termes coïncident avec les données OEIS.

Résultat : **aucune violation sur 3·10⁷ termes** (max a(n) = 14 096, 3 min de calcul). Le passage à 3·10⁸ termes a été
interrompu par la limite de temps de la session.

Pas de preuve : la minimalité de v ne force pas d'elle-même pgcd(v, p) = 1. Il faudrait montrer que le rapport
réduit v′/p′ a déjà été utilisé, ce qui demande de contrôler toute la dynamique de la suite. Statut : non compté.
