# REPORT (14/11/2026)

| Cible | Résultat | Niveau de certitude |
|---|---|---|
| A285383 | a(n) = A035263(n-1), n >= 2 : vraie | Walnut TRUE (échauffement). Déjà prouvée : Ashburn, arXiv:2610.04842. Rien à soumettre. |
| A284948 | a(n) = A096268(n-2), n >= 2 : vraie | **Walnut TRUE** ; automates vérifiés contre génération directe sur 3e5 termes ; énoncé vérifié sur 2e6 termes. |
| A285358 | a(n) = A284929(n+1), n >= 1 : vraie | Preuve à la main **et Walnut TRUE** (numération de Dumont–Thomas, voir plus bas) ; 2e6 termes. |
| A285076 | a(n) = A285073(n), n >= 3 : vraie | Preuve à la main **et Walnut TRUE** ; découle aussi du commentaire de Dekking (2017). |
| A284677 | énoncé d'origine faux (n = 6) ; a(n) = A284674(n), n >= 3 : vraie | Contre-exemple exact ; forme corrigée : preuve à la main **et Walnut TRUE** ; Walnut renvoie FALSE pour l'énoncé d'origine. |

### Preuves Walnut des trois égalités non uniformes (ajout du 14/11 au soir, en local)
`python/make_nonuniform.py`, note `notes/groupA_walnut_nonuniform.md`, sorties `walnut/groupA_nonuniform_*.out` (17 TRUE et 2 FALSE de contrôle chacune ;
rejoué deux fois). Numération de Dumont–Thomas et additionneur produits par l'outil licofage, **validés dans Walnut** par des axiomes
(addition totale, fonctionnelle, 0 minimal, x+0 = x, commutative, compatible avec le successeur défini par l'ordre). Walnut prouve que chaque mot est le
point fixe de son morphisme. Limites : le second mot de chaque paire est défini à partir du premier, donc l'égalité finale est vraie par
construction et tout le contenu est dans les deux preuves de point fixe ; l'associativité de l'addition n'a pas été vérifiée (non utilisée) ;
on suppose Walnut correct. Pas encore relu par des pairs.

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

- A284386 et A284368 (les deux cas en sqrt 13, ajout du 15/11) : les quatre bornes ont aussi une **preuve par Walnut complétée par un argument à la main**
  (`python/make_sqrt13.py`, `notes/groupB_walnut_sqrt13.md`, sorties `walnut/groupB_sqrt13_*.out` : 23 TRUE et 4 FALSE de contrôle chacune, rejoué
  deux fois). Walnut prouve la quasi-additivité p(i)+p(j)+A <= p(i+j) <= p(i)+p(j)+B des positions ; le passage à A < n·r − p(n) < B se fait à la main
  (lemme de Fekete, fréquence, irrationalité de sqrt 13). Les valeurs exactes de inf et sup ne sont pas prouvées par Walnut, seulement par le calcul exact.
  La méthode ne s'étend pas telle quelle aux autres suites du groupe (elle exige sup − inf = 1).
- A284364 : **conjecture fausse**, sup = (6+sqrt(21))/5 = 2,1165 > 2 pour les deux lettres ; plus petits contre-exemples
  n = 2977771 (lettre 1) et n = 8933313 (lettre 0), vérifiés en entiers exacts.
- A284386 : la constante r de l'entrée, (5+sqrt(3))/2, est une coquille pour (5+sqrt(13))/2.
- A284369, lettre 1 : la borne −2 est l'infimum exact, non atteint (irrationalité).
- Toutes les entrées sauf A045671/A045672 énoncent la conjecture avec u(n) = nombre de 0 <= n ; sous cette forme littérale elle est fausse.

## Vérifications en direct (réseau ouvert le 14/11 au soir)
- Les 20 entrées OEIS en direct sont identiques aux fichiers du dépôt oeisdata ; tous les termes de tous les b-files
  coïncident avec la génération indépendante (python/check_live.py).
- Vérification croisée du groupe B par un second algorithme (énumération à profondeur 80 + queue géométrique) :
  encadrements à 1e-8 près, tous cohérents avec les valeurs exactes (results/groupB_bracket_check.txt).
- Ashburn (arXiv:2610.04842) lu : prouve A285383. Fokkink–Joshi (arXiv:2507.16956) lu : aucune de nos suites ; leur borne
  vient aussi d'une majoration des sommes de chiffres, pas de Walnut.

## Limites
Rejeu local du 14/11 au soir : Walnut recompilé et script du groupe A rejoué à l'identique ; article compilé (paper/draft.pdf).
Page de Shallit et historiques OEIS des 14 entrées lus depuis : rien sur ces suites (détail dans LOG.md). Google Scholar non consulté.
Ce qui suit date du 15/11/2026 :
Page de publications de Shallit inaccessible ; antériorité vérifiée par recherche web, lecture des entrées OEIS et des
deux articles ci-dessus. Seul l'historique OEIS de A284364 a été lu en détail.
Atteinte des bornes (ajout du 14/11 au soir, en local) : **aucune des 32 bornes n'est atteinte**, donc inf < D(n) < sup pour tout n >= 1
(python/attainment.py, results/groupB_attainment.txt ; deux méthodes exactes concordantes). Les brouillons de drafts/ disent encore « inf/sup ».
