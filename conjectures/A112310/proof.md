# A112310 — conjecture d'Adamson (2010) : vraie (à partir du deuxième groupe)

**Énoncé.** a(n) = nombre de termes de la représentation de Fibonacci paresseuse de n. On découpe la suite en
groupes de F(k) termes : (0), (1), (1,2), (2,2,3), (2,3,3,3,4), … Conjecture : les sommes des groupes sont les
termes de A023610 (1, 3, 7, 15, 30, …).

**Théorème.** Pour k ≥ 2, la somme du k-ième groupe vaut A023610(k−2). Le premier groupe, (0), a pour somme 0.

**Preuve.** La représentation paresseuse de n ≥ 1 est l'unique écriture n = Σ wᵢ·F(i+1), où w = w₁…w_L est un
mot binaire sans « 00 » avec w_L = 1 (Brown 1965 ; c'est A104326). Les mots de longueur L représentent
exactement les entiers de ]F(L+2) − 2, F(L+3) − 2], qui sont au nombre de F(L+1). Le groupe k (k ≥ 2) est donc
l'ensemble des n dont le mot a pour longueur L = k − 1. Soit W(L) l'ensemble de ces mots et T(L) le nombre total
de 1. En lisant depuis le chiffre de poids fort, un mot de W(L), L ≥ 3, est soit « 1 » suivi d'un mot de W(L−1),
soit « 10 » suivi d'un mot de W(L−2). Donc |W(L)| = |W(L−1)| + |W(L−2)| = F(L+1) et
T(L) = T(L−1) + T(L−2) + F(L+1), avec T(1) = 1 et T(2) = 3. C'est la récurrence de A023610 décalée
(A023610(n+2) = A023610(n+1) + A023610(n) + F(n+4), valeurs initiales 1 et 3), d'où T(L) = A023610(L−1). ∎

**Contrôle** : `check.py` (groupes 2 à 25, depuis la définition).
