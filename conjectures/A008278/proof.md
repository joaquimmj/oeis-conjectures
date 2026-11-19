# A008278 — conjecture de Wiseman (2018 ou après) : vraie

**Énoncé.** T(n,k) = S(n, n−k+1) est le nombre de diviseurs de la superprimorielle A006939(n−1) = Π_{i<n} p_i^(n−i)
qui ont k − 1 facteurs premiers distincts, tous avec des multiplicités distinctes.

**Preuve.** Un tel diviseur revient à choisir r = k − 1 premiers et à leur donner des exposants distincts eᵢ, avec
1 ≤ eᵢ ≤ cᵢ, où les bornes cᵢ valent exactement 1, 2, …, n − 1. C'est un placement de r tours sans prise mutuelle
sur le plateau en escalier dont les lignes ont pour longueurs 1, …, n − 1. Soit ρ_r(n) leur nombre. Considérons la
ligne la plus longue (n − 1 cases). Ou bien elle est vide, ce qui donne ρ_r(n−1). Ou bien elle porte une tour, à
placer dans l'une des (n − 1) − (r − 1) = n − r colonnes non utilisées par les r − 1 autres tours (toutes dans les
colonnes ≤ n − 2), ce qui donne (n − r)·ρ_{r−1}(n−1). Ainsi ρ_r(n) = ρ_r(n−1) + (n − r)·ρ_{r−1}(n−1) avec ρ_0 = 1 :
c'est la récurrence S(n, n−r) = S(n−1, n−r−1) + (n−r)·S(n−1, n−r). Donc ρ_r(n) = S(n, n−r) = T(n, k). ∎
(C'est le résultat classique sur les nombres de tours du plateau triangulaire.)
**Contrôle** : `check.py` (énumération directe des diviseurs, n ≤ 8).
