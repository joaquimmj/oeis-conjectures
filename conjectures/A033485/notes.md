# A033485 (Cloitre 2003) : lim a(2n)/a(n)·log(n)/n = c = 1,64… — **non résolu** (indice contre la valeur 1,64)

`ratio.c` calcule a(n) = a(n−1) + a(⌊n/2⌋) en double précision, jusqu'à 4·10⁸ (sortie `ratio.out`). La quantité
a(2n)/a(n)·log(n)/n passe par un maximum d'environ 1,659 vers n ≈ 150. Elle décroît ensuite régulièrement :
1,639 (10⁴), 1,618 (10⁵), 1,599 (10⁶), 1,582 (10⁷), 1,568 (10⁸), 1,566 (1,5·10⁸).

Identité exacte utile : a(2n) = 2S(n) − a(n) + 1, où S(n) = a(1) + … + a(n).

Heuristique (fonction de Mahler f′(x) = f(x/2), méthode du col) : la limite, si elle existe, vaudrait √2·log 2 ≈
0,98 ou 2 log 2 ≈ 1,39 selon le traitement de la fluctuation discrète, mais pas 1,64. Une preuve demanderait
l'asymptotique précise de de Bruijn (1948) pour les partitions binaires, avec son facteur périodique ; non faite.
Statut : non compté.
