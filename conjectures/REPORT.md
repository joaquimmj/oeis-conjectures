# Conjectures OEIS hors article — rapport (18/11/2026)

**Bilan : 325 entrées avec une conjecture nouvellement réglée (14 avant le crawl, 9 au lot 3, 6 au lot 4, 9 au lot 5, 140 au lot 6 Kimberling, 31 au lot 7, 65 au lot 8, 51 au lot 9) : 293 vraies, 26 fausses, 1 vraie seulement pour n ≥ 2 (A285078), 4 mixtes, 1 partielle (A101513 : 4 conjectures sur 5) (A297469, A298468 : conjecture de Sloane vraie, deux énoncés de Kimberling faux tels qu'écrits ; A304451, A304452 : limites vraies, encadrements faux en n = 1). Une (A361190) repose sur un théorème publié appliqué sans re-vérification complète de ses hypothèses. Rien n'est soumis.**

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
- **Limites a(n)/n → m** (`kimberling/limits.py`, `tm_limits.py`) : 63 vraies, 8 fausses (limite énoncée incorrecte, dont A285964, coquille 4/5 pour 5/4), par les fréquences de Perron, celles des facteurs de Thue-Morse et celles des plages ; 13 déjà réglées par d'autres (Dekking, Zabolotskii) ; restent non traitées les substitutions par blocs de 2 (A287xxx, A288xxx, A289xxx).

## Lot 7 (19/11) : Bala, Yanev

| Entrée | Conjecture | Statut | Preuve |
|---|---|---|---|
| A060973 | Bala 2022 : deux identités emboîtées | **vraies** | Walnut base 2 |
| A007226 | Bala 2023 : parité | **vraie** | via A000139 |
| A080253 | Bala : périodicité mod k | **vraie** | théorème de A004123 (cas G(eˣ − 1)) |
| A129527, A173614, A023887, A055210, A367865, A090079, A163617, A285385, A179504 | Yanev : identités | **vraies** | élémentaires (`yanev/proof.md`) ; apport modeste |
| A285503, A285517, A285567, A285623, A285627, A285663 | Kimberling : a(n)/n → φ | **vraies** | fréquences de Perron (substitutions primitives non Pisot) |
| A373308, A000918, A048881, A059906, A073089, A284388, A225132 | parité de Thue-Morse, Jeffery, Kimberling, Yanev, Beck, inverse de Thue-Morse (preuve assistée, principe de l argument certifié) | **vraies** | élémentaires (`batch8/`) |
| A026743, A027174, A027175, A103973, A190171, A385252 | Mathar (récurrences D-finies) | **vraies** (A385252 : pour n ≥ 6, fausse en n = 5) | vérification exacte de l'opérateur différentiel sur la série algébrique (`dfinite/`) ; apport minime |

## Lot 8 (19/11) : équations complémentaires de Kimberling, a(n)/a(n−1) → φ

| Entrées | Conjecture | Statut | Preuve |
|---|---|---|---|
| 65 entrées : A293057, A293058, A293076, A293316, A293317, A293349–A293351, A293357, A293358, A293406, A293765–A293767, A294365–A294368, A294413–A294426, A294532–A294551, A294553–A294565 | a(n) = a(n−1) + a(n−2) + g(b, n), avec a, b complémentaires : a(n)/a(n−1) → φ | **vraies** | élémentaire, un seul théorème (`compeq/proof.md`) : g ≥ 0, donc croissance exponentielle, donc b(n) ≤ 2n+1, donc e(n) = a(n) − φa(n−1) est à croissance polynomiale. A294413 (g = 6 − b(n−1)) se traite par une récurrence à part |
| 25 entrées (A294170, A294552, A295357, A295754, A295862, A295947–A295953, A295960, A296245…A296843) | même limite, affirmée sans preuve ni mention « Conjecture » | prouvée, **non comptée** dans le bilan | même théorème ; A295754 est d'ordre 4, avec P = (x² − x − 1)(x² + 1) |

Contrôles : `compute.py` (90/90 conformes aux données OEIS, minoration symbolique de g) et `check.py` (générateur
indépendant, 600 termes, 0 échec). Apport modeste : l'argument est standard, mais il n'était écrit nulle part dans
ces entrées.

## Lot 9 (19/11) : systèmes d'équations complémentaires (Walnut)

Non traitées : A297291–A297293 (encadrements vrais numériquement, sur 2·10⁵ termes, mais pas de structure automatique visible) et A299634–A299636 (énoncés d'oscillation non bornée, non automatiques).


| Entrée | Conjecture | Statut | Preuve |
|---|---|---|---|
| A297469, A298468 | Sloane (2019) : formules binaires de bb(2t) et aa(2t) ; Kimberling : cc = A047218, (1)–(4) | **Sloane vraie**, cc = A047218, (2) et (4) vraies ; (1) et (3) **fausses telles qu'écrites** (n = 1), versions corrigées prouvées | Walnut base 2 : candidats automatiques puis vérification des règles gloutonnes (`A297469/`) |
| A304451, A304452 | Kimberling : a(n)/n → 5/2, b(n)/n → 5/3, encadrements pour n ≥ 1 | **mixtes** : limites **vraies** ; encadrements faux en n = 1 (et n = 2 pour a), vrais pour n ≥ 3 | à la main : contraction f(x) = 3x/(3x−2) sur limsup/liminf (`A304451/`) |
| A298173, A298741 | Kimberling (« It appears ») : a(n)/a(n−1) → 3 (resp. 2) et a(n) − k·a(n−1) non borné | **vraies** | élémentaire : somme alternée de b croissante, encadrée par ⌈n/2⌉ et 2n+1 (`A298173/`) |
| A297836, A298112, A298113 | Kimberling : encadrements de a(n) − αn (famille A297830) | **fausses** : A297836 dès n = 2 (a(2) = 11) ; A298112/3 portent sur la mauvaise pente √2 (b(7) = 10). Au passage, les données de A297834/A298109 ne vérifient pas l'équation à partir de a(3). Les 16 autres entrées de la famille restent non prouvées (vraies sur 2·10⁶ termes) | calcul direct (`beattyeq/`) |
| A014664 | Shevelev (2008) : ord_{p^k}(2) = ord_p(2)·p^{k−1} si p n'est pas de Wieferich | **vraie** | classique (relèvement des exposants) ; apport nul (`A014664/`) |
| A025258, A059279, A073155, A080243, A114584, A143013, A166300, A174169, A174171, A188314, A215973, A217333, A254314, A257178, A257388, A261196, A346074 | Mathar (2011–2022) : récurrences polynomiales pour des f.g. algébriques | **vraies** (A025258 : pour n ≥ 6, fausse en n = 5) | réduction exacte de l'opérateur modulo P(x, A) = 0 (`precalg/`) ; conditionnelles à la f.g. de l'entrée ; apport modeste |
| A036766 | Mathar (2015) : récurrence polynomiale d'ordre 5 | **vraie** (n ≥ 2) | réduction exacte de l'opérateur modulo l'équation algébrique de degré 4 (`A036766/verify.py`) |
| A033485 | Cloitre (2003) : lim a(2n)/a(n)·log n/n = c = 1,64… | **fausse** : la limite existe et vaut 2 log 2 = 1,386… (β(n) = log₂ n + O((log log n)²)) | récurrence par blocs dyadiques avec erreurs explicites, base calculée jusqu'à 2²⁹ (`A033485/`) ; la seconde conjecture (a(n)/A(n) borné) n'est pas traitée | **Antériorité :** la limite 2 log 2 découle aussi de l'asymptotique de de Bruijn (1948) pour les partitions binaires, rappelée par Flajolet dans A000123 ; la preuve du dépôt en est un contrôle indépendant.
| A083207 | 12 entiers consécutifs contiennent un nombre de Zumkeller (2010) | **vraie** | à la main : 3·2^a est de Zumkeller, extension première, multiples de 6 (`A083207/`) ; corollaire d'un fait déjà noté (Ianakiev), apport modeste |
| A022344 | Ramsey (2007) : produit de deux lignes du tableau de Wythoff, caractéristique multiplicative | **vraie** | identité de norme dans ℤ[φ] et théorème de Morrison (`A022344/`) ; apport modeste |
| A155200 | Hanna (2009) : v₂(a(n)) = s₂(n) pour exp(Σ 2^{n²}xⁿ/n) | **vraie** | à la main : A = exp(2x)·R, Legendre, valuations 2-adiques (`A155200/`) |
| A123722, A123723 | nombre de carrés mod n égal à ⌈(n+1)/3⌉ ou ⌈(n+1)/4⌉ : les multiples de 3 (resp. 4) sont 3p (resp. 4p) | **vraies** | multiplicativité et formules aux puissances premières (`A123365/`) ; A123365 (cubes) vérifiée jusqu'à 3·10⁶ mais non prouvée |
| A143772 | Wilson (2008) : pgcd des k + m/k ; tout pair est atteint, les seules valeurs impaires sont 1 et 3 | **vraie** | à la main (diviseurs 1 et 2, puis m = qr avec Dirichlet et lemme chinois) (`A143772/`) |
| A101513 | Sloane (2005) : (1) repoussés = premiers, (2) tout entier apparaît, (3) premiers dans l'ordre, (4) 2p puis p ; (5) dernier terme | **(1)–(4) vraies**, (5) non traitée | récurrence sur la structure des lignes, bornes explicites (Montgomery–Vaughan, Rosser–Schoenfeld) pour n ≥ 1500, simulation en dessous (`A101513/`) |
| A100036, A100037, A100038, A100039 | Stephan (2007) : positions des copies de ℕ dans A100035 (2n²−n+3, 2n²+3n+6, 2n²+7n+13, sommes partielles) | **vraies** (coquille « n/2−7 » pour 2n−7 dans A100036) | structure explicite en blocs de A100035, par récurrence sur l'ensemble des paires adjacentes (`A100035/`) |
| A116731 | Meeussen (2008) : couples (échanges, itérations) du tri à bulles | **vraie** | table d'inversions, (Σ L, max L) (`A116731/`) ; apport modeste |
| A078841 | Wilson (2007) : a(n+1)/a(n) → 2 pour le (n+1)-ième entier à n facteurs premiers | **vraie** | à la main : a(n) = 2ⁿ·t_{n+1} avec V = {u/2^Ω(u), u impair} indépendant de n, puis théorème des nombres premiers (`A078841/`) |
| A005427 | Hadjicostas (2020) : pour tout k ≥ 2, les m dont le survivant de Josèphe (une personne sur k) est parmi les k−1 premiers sont les T(n;k) = ⌈ΣT/(k−1)⌉ ≥ k | **vraie pour tout k** | à la main : invariant J(T(n)) = r_n + 1 (reste du plafond), base par J(v) = kv + 1 − Q(v) (`A005427/`) ; nouveauté à vérifier (Burde 1987, Thériault) | **Antériorité :** corollaire court de la formule d'Odlyzko–Wilf (J_k(m) = km + 1 − D_j, aussi dans *Concrete Mathematics* §3.3) ; voir `paper/parts/part3a.tex`.
| A120160 | Hadjicostas (2020) : Josèphe pour k = 5 ; conjectures 1 et 2 en base 5/4 | **vraies** (conjecture 1 : multiples > 0 ; avec 0 compté, échec seulement en n = 2) | cas k = 5 du théorème de A005427 ; arbre des écritures en base (k+1)/k, pour tout k (`A120160/`) | **Antériorité :** la partie Josèphe relève du même corollaire d'Odlyzko–Wilf.
| A074355 | Stephan (2004) : f.g. (9x⁴+3x³)/(1−3x−3x²)² | **fausse** telle qu'écrite (x⁴ : 27 au lieu de 15) ; la f.g. corrigée (1−x−3x²)² est prouvée | récurrence sur [q¹] (`A074355/`) |
| A074356, A074357, A074358, A074359, A074360 | Mathar (2009), Wu (2016), Barker (2017) : f.g. et récurrences des coefficients de q^j dans nu(n) | **vraies** | système triangulaire exact pour les C_j(x) (`A074357/`) ; apport modeste |
| A064097 (partiel, non compté) | Cloitre (2002), Wilson (2013) : log n < a(n) < (5/2) log n | minorations **vraies**, majoration prouvée avec 2/log 2 ≈ 2,885 ; 5/2 ouverte (liée aux chaînes de Cunningham) | `A064097/` |
| A295070 | Kimberling : a(n) = a(n−2) + b(n−1) + b(n−2), a(n)/a(n−1) → 1 | **vraie** | croissance quadratique, a(n) − a(n−1) ≤ 4n+O(1) (`compeq/A295070.md`) |
| A297464, A297465, A297466 (**non comptées : déjà traitées par Bosma et al., arXiv:2503.04122, 2025, p. 8, cité dans l'entrée**) | Kimberling : quatre encadrements (système « anti-tribonacci ») ; récurrence a(n) = a(n−1) + a(n−3) − a(n−4) | **mixtes** : encadrements faux tels qu'écrits (offset 0, échec en n = 0), vrais avec n → n+1 ; récurrence **vraie** | Walnut lsd_3, candidats devinés depuis le 3-noyau puis règles gloutonnes (`A297464/`) |
| A299405, A299409, A299637, A299638, A299641 (**non comptées : traitées par Bosma et al. 2025 et Fokkink–Joshi, arXiv:2506.13337, cités dans A299409 ; articles non lus, hôtes bloqués. Point à confronter : selon les résumés trouvés, ces articles « vérifient » les bornes, alors que notre calcul, depuis la définition et par Walnut, montre que la borne de c échoue en n = 26**) | Kimberling : cinq encadrements (système « anti-tétranacci ») | **fausses** : même avec n → n+1, c(26) = 113 viole la borne de c (4 > 3) ; les autres bornes sont vraies avec le décalage, et celle de c avec 4 | Walnut lsd_2 (`A299405/`) |

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
