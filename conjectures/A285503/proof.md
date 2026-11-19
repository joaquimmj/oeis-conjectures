# A285503, A285517, A285567, A285623, A285627, A285663 — conjectures de Kimberling (2017) : a(n)/n → φ. Vraies

**Mots.** Mots limites ou points fixes de 0 → 11, 1 → w, avec w ∈ {0011, 0110, 1001, 1010, 1100}. A285517 lit
A285501 par paires.

**Preuve.** Les cinq morphismes ont la même matrice d'incidence M = [[0, 2], [2, 2]] (lignes : nombre de 0 et de 1 ;
colonnes : images de 0 et de 1). M² > 0, donc la substitution est primitive (σ² aussi, pour les mots limites). Pour
une substitution primitive, chaque lettre a une fréquence, qui est la composante normalisée du vecteur propre de
Perron (Queffélec, *Substitution dynamical systems*). Valeur propre λ = 1 + √5, vecteur propre (2, λ) : la
fréquence de 1 vaut λ/(2 + λ) = (√5 − 1)/2 = 1/φ. La position du n-ième 1 vérifie donc a(n)/n → φ.

Pour A285515 : toutes les images ont une longueur paire et sont faites de blocs 00 et 11, donc A285501 est une
suite de paires alignées 00 ou 11. La transformée {00 → 0, 11 → 1} est le mot des paires, où la fréquence de 1 est
la même, 1/φ. ∎

**Remarque.** La seconde valeur propre 1 − √5 est de module > 1 : ces mots ne sont pas de Pisot, et
a(n) − nφ n'est pas borné. Seule la limite est vraie, pas une borne de discrépance.
**Contrôle** : `check.py` (données des entrées ; a(n)/n ≈ 1,6180 sur ≈ 2,5·10⁵ termes).
