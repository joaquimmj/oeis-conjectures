# REPORT (14/11/2026)

| Cible | Résultat | Niveau de certitude |
|---|---|---|
| A285383 | a(n) = A035263(n-1), n >= 2 : vraie | Walnut TRUE (échauffement). Déjà prouvée : Ashburn, arXiv:2610.04842. Rien à soumettre. |
| A284948 | a(n) = A096268(n-2), n >= 2 : vraie | **Walnut TRUE** ; automates vérifiés contre génération directe sur 3e5 termes ; énoncé vérifié sur 2e6 termes. |
| A285358 | a(n) = A284929(n+1), n >= 1 : vraie | Preuve à la main (pas Walnut) ; identités vérifiées par machine ; 2e6 termes. |
| A285076 | a(n) = A285073(n), n >= 3 : vraie | Preuve à la main ; découle aussi du commentaire de Dekking (2017). |
| A284677 | énoncé d'origine faux (n = 6) ; a(n) = A284674(n), n >= 3 : vraie | Contre-exemple exact ; preuve à la main de la forme corrigée. |

## Groupe B (lecture « positions » : a(n) = position du n-ième 0 ou 1, D(n) = n·r − a(n))

Niveau de certitude : **calcul exact avec certificat vérifié** (pas Walnut) ; méthode dans notes/groupB_method.md.
Contrôles : formule comparée à la définition directe (exact, 2e5 lettres) ; balayage flottant sur 2e8 lettres cohérent.

| Suite, lettre | r | conjecture | inf exact | ~ | sup exact | ~ | conjecture |
|---|---|---|---|---|---|---|---|
| A283963 zeros | (3+sqrt(3))/2 | -1 < n·r − a(n) < 2 | (-3-sqrt(3))/6 | -0.788675 | (3+sqrt(3))/3 | 1.577350 | VRAIE |
| A283963 ones | sqrt(3) | -1 < n·r − a(n) < 2 | (-3+sqrt(3))/3 | -0.422650 | (3+sqrt(3))/3 | 1.577350 | VRAIE |
| A283966 zeros | (7+sqrt(17))/4 | -1 < n·r − a(n) < 3 | -1/2 | -0.500000 | (5+sqrt(17))/4 | 2.280776 | VRAIE |
| A283966 ones | (-1+sqrt(17))/2 | -1 < n·r − a(n) < 2 | (-7+sqrt(17))/4 | -0.719224 | (1+sqrt(17))/4 | 1.280776 | VRAIE |
| A284364 zeros | (9+sqrt(21))/6 | -2 < n·r − a(n) < 2 | (-12-2*sqrt(21))/15 | -1.411010 | (6+sqrt(21))/5 | 2.116515 | FAUSSE |
| A284364 ones | (-1+sqrt(21))/2 | -1 < n·r − a(n) < 2 | (-9+sqrt(21))/5 | -0.883485 | (6+sqrt(21))/5 | 2.116515 | FAUSSE |
| A284386 zeros [r corrected to (5+sqrt13)/2] | (5+sqrt(13))/2 | 0 < n·r − a(n) < 2 | (1+sqrt(13))/6 | 0.767592 | (7+sqrt(13))/6 | 1.767592 | VRAIE |
| A284386 ones | (-1+sqrt(13))/2 | -1 < n·r − a(n) < 1 | (-5+sqrt(13))/6 | -0.232408 | (1+sqrt(13))/6 | 0.767592 | VRAIE |
| A284368 zeros | (5+sqrt(13))/2 | 1 < n·r − a(n) < 3 | (1+sqrt(13))/3 | 1.535184 | (4+sqrt(13))/3 | 2.535184 | VRAIE |
| A284368 ones | (-1+sqrt(13))/2 | -1 < n·r − a(n) < 1 | (-5+sqrt(13))/3 | -0.464816 | (-2+sqrt(13))/3 | 0.535184 | VRAIE |
| A284369 zeros | (3+sqrt(3))/2 | -3 < n·r − a(n) < 4 | (-3-sqrt(3))/2 | -2.366025 | 2+sqrt(3) | 3.732051 | VRAIE |
| A284369 ones | sqrt(3) | -2 < n·r − a(n) < 3 | -2 | -2.000000 | 1+sqrt(3) | 2.732051 | VRAIE |
| A284505 zeros | (3+sqrt(3))/2 | -3 < n·r − a(n) < 4 | (-9-5*sqrt(3))/6 | -2.943376 | (6+2*sqrt(3))/3 | 3.154701 | VRAIE |
| A284505 ones | sqrt(3) | -2 < n·r − a(n) < 4 | (-3-sqrt(3))/3 | -1.577350 | (6+2*sqrt(3))/3 | 3.154701 | VRAIE |
| A045671 (ones of 0->11,1->1110) | (1+sqrt(17))/4 | -1 < n·r − a(n) < 2 | (-9-sqrt(17))/32 | -0.410097 | (27+3*sqrt(17))/32 | 1.230291 | VRAIE |
| A045672 (zeros of 0->11,1->1110) | (5+sqrt(17))/2 | -1 < n·r − a(n) < 3 | (-9-sqrt(17))/16 | -0.820194 | (27+3*sqrt(17))/16 | 2.460582 | VRAIE |

- A284364 : **conjecture fausse**, sup = (6+sqrt(21))/5 = 2,1165 > 2 pour les deux lettres ; plus petits contre-exemples
  n = 2977771 (lettre 1) et n = 8933313 (lettre 0), vérifiés en entiers exacts.
- A284386 : la constante r de l'entrée, (5+sqrt(3))/2, est une coquille pour (5+sqrt(13))/2.
- A284369, lettre 1 : la borne −2 est l'infimum exact, non atteint (irrationalité).
- Toutes les entrées sauf A045671/A045672 énoncent la conjecture avec u(n) = nombre de 0 <= n ; sous cette forme littérale elle est fausse.

## Limites
oeis.org et arxiv.org inaccessibles depuis la session : historiques OEIS, b-files (sauf deux par SHA-256) et textes
intégraux (Ashburn, Fokkink–Joshi) non lus. Antériorité vérifiée par recherche web seulement.
Atteinte des bornes non étudiée (énoncés sûrs : inf <= D(n) <= sup).
