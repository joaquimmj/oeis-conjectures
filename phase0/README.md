# Phase 0 — état des cibles (14/11/2026)

Sources lues : fichiers `.seq` de oeis/oeisdata (HEAD 49db774, données du jour), recherche web.
NON lus (bloqués par le réseau de la session) : pages oeis.org en direct et historiques, b-files,
page de Shallit, texte intégral des articles arXiv.
Calculs : `python/check_phase0.py`, `check_phase0b.py`, `scout_groupB.py`, `exact_A284364.py`.
Toutes les définitions reproduisent la section DATA de l'OEIS (86 à 105 termes) ; deux b-files
(A284929, A096268) sont vérifiés en entier par SHA-256.

## Groupe A
| Suite | Statut | Détail |
|---|---|---|
| A285383 | **déjà prouvée** | A. Ashburn, arXiv:2610.04842 (04/10/2026), lien ajouté à l'entrée le 06/10/2026 ; le résumé dit « proves a conjecture of Mathar on A285383 » (texte intégral non lu). Numériquement vraie pour 2 <= n < 2e6 ; n = 1 sort de l'offset de A035263. |
| A284948 | ouverte (rien trouvé) | a(n) = A096268(n-2) vraie pour 2 <= n < 2e6. |
| A284677 | **énoncé faux tel qu'écrit** | a(n) = A284674(n-1) échoue dès n = 6 (a(6) = 0, A284674(5) = 1). La relation vraie numériquement est a(n) = A284674(n) pour n >= 3 (les deux mots ne diffèrent qu'aux deux premiers termes : 10... / 01...). |
| A285076 | ouverte formellement, mais contenue dans un commentaire | a(n) = A285073(n), n >= 3 : vraie jusqu'à 2e6. Dekking (commentaire de 2017, arXiv:1705.08607) écrit déjà a = 10c et A285073 = 01c ; la conjecture en découle. |
| A285358 | ouverte (rien trouvé) | a(n) = A284929(n+1) vraie pour 1 <= n < 2e6. |

## Groupe B
Lu littéralement (u(n) = nombre de 0 parmi les n premiers termes), **tous les énoncés sont faux
dès n <= 4** : n*r - u(n) croît linéairement. Le sens voulu est celui de A045671 : a(n) = position
du n-ième 0 (resp. 1), et la borne porte sur n*r - a(n). Résultats sous cette lecture
(flottants sur 2e8 lettres, sauf mention) :

| Suite | Statut | 0 : min / max observés (conj.) | 1 : min / max observés (conj.) |
|---|---|---|---|
| A283963 | ouverte | -0.784 / 1.573 (-1, 2) | -0.419 / 1.574 (-1, 2) |
| A283966 | ouverte | -0.500 / 2.281 (-1, 3) | -0.719 / 1.281 (-1, 2) |
| A284364 | **FAUSSE (contre-exemple exact)** | max 2.0367 > 2 ; plus petit n : 8933313, a(n) = 20222898 | max 2.0566 > 2 ; plus petit n : 2977771, a(n) = 5334043 |
| A284386 | énoncé avec coquille | r = (5+sqrt 3)/2 est faux (échec à n = 2) ; avec r = (5+sqrt 13)/2 : 0.768 / 1.768 (0, 2) | -0.232 / 0.768 (-1, 1) |
| A284368 | ouverte | 1.535 / 2.535 (1, 3) | -0.465 / 0.535 (-1, 1) |
| A284369 | ouverte, borne serrée | -2.356 / 3.725 (-3, 4) | **-1.9947** / 2.725 (-2, 3) |
| A284505 | ouverte | -2.931 / 3.143 (-3, 4) | -1.569 / 3.146 (-2, 4) |
| A045671 | ouverte | (positions de 1) -0.410 / 1.230 (-1, 2) | |
| A045672 | ouverte | (positions de 0) -0.820 / 2.460 (-1, 3) | |

Contre-exemple A284364 : vérifié en entiers exacts (comparaison de carrés), deux générateurs
indépendants du mot, plus petit n obtenu par balayage exact.
Fokkink–Joshi (arXiv:2507.16956) traite A284753 (0->10, 1->1000), pas ces suites, d'après les
résumés ; aucun résultat de recherche ne mentionne les A-numéros du groupe B.

## Mise à jour après ouverture du réseau (14/11/2026, soir)
- Entrées en direct sur oeis.org : **identiques** aux fichiers `.seq` pour les 20 suites (`python/check_live.py`).
- b-files en direct : **tous** les termes (10000 à 65536 selon la suite) coïncident avec la génération indépendante.
- Historique OEIS de A284364 : dernier changement approuvé le 13/04/2025 (Eldar, moyenne asymptotique) ; rien sur la borne.
- Ashburn, arXiv:2610.04842, lu : Proposition 5 prouve A285383 (w = 0·d) par la conjugaison 1·μ(u) = σ(u)·1. Cible retirée.
- Fokkink–Joshi, arXiv:2507.16956, lu : ne mentionne aucune de nos suites. Leur borne pour A284753 n'est PAS obtenue par Walnut :
  Walnut sert à identifier la suite dans la numération de Dumont–Thomas, puis la borne vient d'une majoration numérique de
  Σ d_i·λ̄^i (Lemme 18, « a finite problem that we solved numerically », Théorème 19). Notre calcul exact est de la même famille.
- Page de Shallit (cs.uwaterloo.ca) : toujours inaccessible. Shallit et al., arXiv:2510.11318 : aucune de nos suites.
