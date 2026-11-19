# Conjectures OEIS hors article — rapport (18/11/2026)

**Bilan : 125 entrées avec une conjecture nouvellement réglée (14 avant le crawl, 9 au lot 3, 6 au lot 4, 9 au lot 5, 69 au lot 6 Kimberling, 18 au lot 7) : 111 vraies, 13 fausses, 1 vraie seulement pour n ≥ 2 (A285078). Une (A361190) repose sur un théorème publié appliqué sans re-vérification complète de ses hypothèses. Rien n'est soumis.**

Phase 0 faite le 18/11 : entrées complètes téléchargées (`phase0/`), arXiv interrogé (Shallit depuis 2023,
Dekking depuis 2020, Letouzey, Doche, Schreier, Rudin-Shapiro). Aucune preuve antérieure trouvée pour ces
entrées. Non vérifié : les historiques OEIS (page protégée contre les robots). A366860/70/71 et A286389 ont
été modifiés le 09/11/2026 ; le texte actuel ne contient aucune preuve.

| Entrée | Conjecture | Statut | Preuve | Certitude |
|---|---|---|---|---|
| A371176 | Kotesovec 2025 : lim sup log a(n)/log n = log 2/log φ | **vraie, et la limite existe** | à la main (ensembles de Schreier, Fibonacci) | élevée ; étapes vérifiées pour m ≤ 22 |
| A366860, A366870, A366871 | Gutkovskiy 2023 : a(n) ~ c·n | **vraies, pour tout k ≥ 1** | à la main : différences = point fixe de 0 → 1^k, 1 → 1^k 0 | élevée ; k ≤ 30 vérifié numériquement ; pas de 2e preuve machine |
| A118006 | équation de Hebisch–Rubey (Somos) | **vraie** pour f = Σ a(n) x^(n−1), fausse avec x^n | lemme à la main et Walnut en base 3 | élevée |
| A007413 | Shevelev 2009 : nombres de 1 entre deux 2 de A076826 | **vraie** | réduction à la main et Walnut en base 2 | élevée |
| A005590 | Stephan 2003 : a(3n) = 0 ⇔ n fibbinaire | **vraie**, et |a(3n)| ≥ 2 sinon | à la main : représentation linéaire et invariant quadratique | élevée ; identités vérifiées par sympy, énoncé jusqu'à 2^21 |
| A347171 | Doche–Mendès France 2001 : nombre de racines réelles = A285869(n) | **vraie**, toutes les racines sont simples, avec le décompte par région | à la main : forme de Tchebychev, phase croissante ou concave sur les deux branches, analyse directe pour y > 0 | élevée ; formules vérifiées (mpmath), décompte exact par région (Sturm sur ℚ(√2)) pour n ≤ 300 ; article original non lu (hôte inaccessible) |
| A357097 | A(A019586(x), A019586(y)) = A019586(A101330(x,y)) | **vraie** | à la main : anneau ℤ[φ], θ(n) = Σ φ^{cᵢ} multiplicative pour le produit de Knuth (argument sur le conjugué) | élevée ; vérifiée en entiers pour x, y < 400 |
| A358360 | Oudra 2026 : cinq formules pour ν₃ des Delannoy centraux | **vraies** | à la main, à partir des théorèmes 4 et 6 d'Alekseyev–Amdeberhan–Shallit–Vukusic (2026) | élevée ; repose sur l'article cité (lu) |
| A161580 (et A161579, A161817, A162311) | Shevelev 2009 : alternance odieux / maléfiques, k impair | **vraie**, les deux variantes | Walnut en base 2, pour tous les k impairs à la fois | élevée ; la variante « = » est déjà dans Allouche 2015, la variante « ≠ » de A161580 n'était pas référencée |
| A070864 | Layman 2002 : formule fermée | **vraie** | récurrence forte rédigée ; équivalente aux formules de Cloitre et Curgus (données sans preuve dans l'entrée) | élevée ; apport modeste |
| A112310 | Adamson 2010 : sommes par groupes = A023610 | **vraie** à partir du 2e groupe | à la main (mots sans 00) | élevée |
| A055246 | Jeffery 2015 : deux conjectures | **vraies** | élémentaire, depuis a(n) = 1 + 6·A005836(n) | élevée ; apport modeste |

## Lot 3 (crawl du 18/11 : 1 643 entrées lues, 710 conjectures sans signe de résolution, tri à la main)

| Entrée | Conjecture | Statut | Preuve | Certitude |
|---|---|---|---|---|
| A001462 (core) | Song 2021 : Golomb a(n) ≥ n^(φ−1) | **vraie** | à la main : m^φ/φ ≤ A001463(m) ≤ m^φ par récurrence forte, base m ≤ 30 calculée | élevée |
| A006165 | Bala 2022 : sept conjectures, dont (vi) et (vii) pour tout k | **vraies** | Walnut base 2 (k paramétré par u = msb(n)/2^k) et formule des itérées | élevée ; le « 35 » de l'entrée est une coquille pour 33 |
| A000139 (nice) | Bala 2025 : a(n) impair ⇔ n ∈ A022341 | **vraie** | à la main (Legendre, retenues de n + 2n) | élevée |
| A004123, A006531 (nice) | Bala 2022 : périodicité mod k, période divisant φ(k), et forme générale G(eˣ − 1) | **vraies** | à la main (j!·S(n,j), Carmichael λ(k)) | élevée ; argument classique, référence non cherchée |
| A050446 (nice) | Rascoe 2025 : mots à sommes voisines ≤ m + 1 | **vraie** | bijection vers les mots alternés, puis récurrence de l'entrée | élevée ; dépend de la récurrence %F de l'entrée |
| A003278, A006364, A034448 (nice) | Jeffery, Yanev, Yanev | **vraies** | élémentaires | élevée ; apport modeste |
| A022558 | Burstein 2019 : |Av(2143, 415263)| = |Av(1342)| | **ouverte**, vérifiée pour n ≤ 10 (`count.py`) | TileScope (tilings 4.1.0) : pas de spécification avec point, row ou insertion placements en 300 s chacune ; la 4e stratégie sature la mémoire du conteneur | — |
| A033485 (nice) | Cloitre 2003 : lim a(2n)/a(n)·log n/n | non prouvée | a(n) = b(2n)/2 (partitions binaires) ; la limite devrait découler de de Bruijn 1948 ou Knuth 1966, non lus ; numériquement ≈ 1,60, pas 1,64 | — |

## Lot 4 (19/11, suite du crawl)

| Entrée | Conjecture | Statut | Preuve | Certitude |
|---|---|---|---|---|
| A226898 (core) | Greathouse 2026 : Δ(n) ≤ d(n)/2 pour n > 4 (Δ de Hooley) | **vraie** | à la main (chaînes d, dq, dq², … pour un premier impair q) | élevée |
| A072939 | Jovovic 2003, Kimberling 2017, Sloane 2019, limite 3 | **vraies** (quatre conjectures) | à la main (dynamique des différences) | élevée |
| A368281 / A368282 | sommes partielles du point fixe de 0 → 1ⁿ, 1 → 1ⁿ0 | **vraie** pour tout n | théorème de A366860 | élevée |
| A363308 | parité de C(x·C(x)³) | **vraie** | à la main dans GF(2)[[x]] | élevée |
| A088538 | Aktar 2007 : limite 4/π | **vraie** | à la main (produit de Viète) | élevée ; apport modeste |
| A361190 | Kotesovec 2026 : exposant 1 + π/arctan(√2) | **vraie** (et série non D-finie) | application du théorème de Denisov–Wachtel (2015) | moyenne à élevée : hypothèses non re-vérifiées ligne à ligne |
| A288997 | Dekking 2022 : mot de Pell décalé | non prouvée, vérifiée sur 248 425 lettres | réduite à un énoncé en numération de Pell | — |

## Lot 5 (19/11, second crawl : auteurs Bala, Kotesovec, Cloitre, Jovovic, Wiseman, Callan, Hasler, Greathouse…)

| Entrée | Conjecture | Statut | Preuve | Certitude |
|---|---|---|---|---|
| A005121 (nice) | Mohapatra 2026 : R(n,n) = a(n) | **vraie** | à la main : M^t triangulaire, sommes de colonnes = Stirling, récurrence de Lengyel | élevée |
| A006068 (nice) | Kurkov 2023 : Gray inverse | **vraie** | Walnut base 2 | élevée |
| A055938 (nice) | Stephan 2013 : règle +1/+3 et lien avec A080578 | **vraies** | à la main (écarts de A005187) | élevée |
| A008278 (nice) | Wiseman : diviseurs des superprimorielles | **vraie** | nombres de tours du plateau en escalier | élevée |
| A040027 (nice) | Yanev 2021 : nombres de Gould | **vraie** | séries génératrices exponentielles | élevée |
| A079267 (nice) | Callan 2012 : loi de Poisson(1) à la limite | **vraie** | convergence dominée | élevée |
| A170941 | Callan 2012 : proportion 1/e | **vraie** | inclusion-exclusion, convergence dominée | élevée |
| A088617 | Callan 2008 : ~ n/√2 pas U | **vraie** | log-concavité, concentration | élevée (rédaction un peu rapide) |
| A003959 (nice) | Stephan 2013 : produit eulérien | **vraie** | immédiate | élevée ; apport minime |

**Références à ajouter (déjà prouvé ailleurs)** : A059100 (Cloitre 2002 : la fraction continue de Σ n^(−2^k)
relève du théorème de Shallit 1979 sur Σ x^(−2^k), non relu), A001156 (Bohman–Fröberg–Riesel : l'asymptotique
exacte, donnée par Kotesovec dans l'entrée, a pour exposant 7/6, et non 1,16022).

## Lot 6 (19/11) : conjectures de discrépance de Kimberling hors article, avec la méthode exacte de l'article

`conjectures/kimberling/` : outil `python/discrepancy_exact.py` réutilisé tel quel (certificat exact dans ℚ(√d)).
- **20 conjectures vraies, avec les bornes exactes** : A026363, A026364, A026367, A026368, A284654, A284675, A284676,
  A284678, A284679, A284753, A284894, A285032, A285035, A285036, A285082, A285084, A285275, A285278, A285419, A285669.
  Plusieurs bornes conjecturées sont exactement l'infimum ou le supremum, jamais atteints (D(n) irrationnel) :
  elles sont optimales. A284753, A284894 et A285669 n'avaient que la forme faible (bornitude, Dekking).
- **2 conjectures fausses** : A285126 (n = 3) et A285127 (n = 2), contre-exemples dans les données mêmes des
  entrées ; la discrépance y est non bornée (morphisme 0 → 10, 1 → 0000 non Pisot).
- Déjà prouvées par Dekking, non comptées : A285074, A285075, A287664, A287665, A287675, A287726, A287770.
- Conséquence : la conjecture plus forte de Dekking dans A284753 (sur A026363, borne 3/2) est vraie.
- **Troisième série** (`kimberling/proof.md`) : **30 vraies** avec bornes exactes, dont 4 entrées compagnes de
  mots de l'article (A283964, A283967, A284370, A284506), formulées en positions ; **11 fausses** avec contre-exemples
  exacts (A285129, A285130, A285134, A285135, A285137, A285138, A285140, A285141, A285143, A285144, A285279 ; pour
  A285279, le r énoncé est faux) ; **A285078** vraie pour n ≥ 2, fausse en n = 1 (égalité avec la borne).
- **Transformées du mot de Fibonacci** (`fibtransform/`, Walnut en numération de Fibonacci) : A287676 (avec la
  formule de Liu), A287723, A287724 et A287727 vraies.
- **Total Kimberling** : 55 vraies (dont A284015), 13 fausses, 1 vraie pour n ≥ 2.

## Lot 7 (19/11) : Bala, Yanev

| Entrée | Conjecture | Statut | Preuve |
|---|---|---|---|
| A060973 | Bala 2022 : deux identités emboîtées | **vraies** | Walnut base 2 |
| A007226 | Bala 2023 : parité | **vraie** | via A000139 |
| A080253 | Bala : périodicité mod k | **vraie** | théorème de A004123 (cas G(eˣ − 1)) |
| A129527, A173614, A023887, A055210, A367865, A090079, A163617, A285385, A179504 | Yanev : identités | **vraies** | élémentaires (`yanev/proof.md`) ; apport modeste |
| A285503, A285517, A285567, A285623, A285627, A285663 | Kimberling : a(n)/n → φ | **vraies** | fréquences de Perron (substitutions primitives non Pisot) |

**Déjà résolues par d'autres (trouvé en Phase 0, non comptées)** : A000521 (Sun : rapports décroissants ; Li,
arXiv:2506.19292, 2025, théorème 3.1), A001462 (van Lamoen : Claes–Miyamoto, arXiv:2602.10992, 2026), A000002
(Perry : Hervé 2014), A305394 (Dekking et al.), A002083 (Finch), A001187 (probablement Konvalinka–Pak 2014), A122135,
A006012, A094913/A006697 (probablement Shallit 1993, Allouche–Shallit 2016).

**Écartées après Phase 0** : A178482 (déjà prouvée, Shallit–Vukusic 2025) ; A156253 (la récurrence de Maiga a
une note de 2025 dans l'entrée, non lue ; l'asymptotique 2n/3 équivaut à la densité de Kolakoski) ; A364648
(énoncé non exprimable directement dans Walnut : multiplication j·d) ; A285296, A356677, A370630 (suites
lexicographiques, pas d'angle) ; A001953/A001954, A022344, A070875, A133954, A189628 (non examinées en détail).

Walnut : github.com/firetto/Walnut, HEAD a4fe84e, compilé avec javac (OpenJDK 21), fastutil 8.5.13 et
automaton 1.12-4. Les lignes `#` des scripts `.wal` sont retirées avant exécution, car le REPL ne les accepte pas.
Rien n'a été soumis à l'OEIS. Pour A347171, le plan prévoit d'abord une note arXiv, et de vérifier avant dans l'article de 2001 qu'il ne contient pas déjà une preuve. Note LaTeX de A347171 (anglais, 3 pages, compilée avec pdflatex) : `A347171/paper/note.tex` et `note.pdf`. Brouillons : `*/draft.txt`. Aucune de ces preuves n'a été relue par un humain.
