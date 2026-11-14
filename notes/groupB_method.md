# Groupe B : méthode et statut

**Statut : preuve assistée par ordinateur en arithmétique exacte, PAS une preuve Walnut.**
Raison : les inégalités portent sur le réel n·r − a(n). Pour les morphismes non unimodulaires
(déterminant ±2, ±3 : tous les cas sauf √13), je ne sais pas exprimer la comparaison à un seuil réel
par un automate fini dans la numération de Dumont–Thomas, donc pas par une formule Walnut. C'est aussi
la voie de Fokkink–Joshi d'après les résumés consultés (discrépance symbolique, Adamczewski 2004) ;
leur article (lu ensuite) confirme : Walnut identifie la suite, la borne vient d une majoration numérique des sommes de chiffres (Lemme 18, Théorème 19).

## Lecture des conjectures
Écrites avec u(n) = nombre de 0 parmi les n premiers termes, elles sont fausses dès n <= 4.
On lit : a(n) = position du n-ième 0 (resp. 1), et la borne porte sur D(n) = n·r − a(n).
C'est la formulation de Kimberling lui-même dans A045671/A045672.

## Argument (détail et code : `python/discrepancy_exact.py`)
σ morphisme sur {0,1}, x = σ^ω(lettre initiale), M sa matrice, λ > 1 > |λ'| ses valeurs propres,
L une lettre, r = 1/fréquence(L).

1. f(q) = r·q_L − |q| sur les vecteurs de Parikh vérifie f(Mq) = λ'·f(q) (vérifié exactement ;
   cela certifie aussi que r est bien l'inverse de la fréquence).
2. Dumont–Thomas : tout m >= 0 correspond à un unique chemin (c_k,d_k)…(c_0,d_0) de l'automate des
   préfixes (états = lettres, c --d--> σ(c)[d]) avec x[0..m) = σ^k(p_k)…σ(p_1)p_0, p_i = préfixe de
   longueur d_i de σ(c_i), et x[m] = état final. Donc
   f(Parikh x[0..m)) = Σ_i λ'^i·g(c_i,d_i), g(c,d) = f(Parikh p), et D(n) = cette somme + r − 1
   quand m = a(n) − 1.
3. V_c = ensemble des valeurs de la somme sur les chemins finissant en c ; S_c = sup, I_c = inf.
   Un chemin vers c' est un chemin vers c suivi d'une arête, donc
   V_c' = [c' initial]{0} ∪ ⋃ (λ'·V_c + g(c,d)). Comme λ' < 0 : S_c' = max(λ'·I_c + g), I_c' = min(λ'·S_c + g).
4. Cet opérateur est une contraction de rapport |λ'| pour la norme sup : son point fixe borné est unique.
   Le programme devine le point fixe en flottants, résout le système linéaire **exactement** dans Q(√d),
   puis **vérifie exactement** toutes les égalités et inégalités max/min. D'où sup D = S_L + r − 1 et
   inf D = I_L + r − 1, valeurs optimales par construction.

## Contrôles indépendants
- Formule de Dumont–Thomas comparée exactement à la définition directe sur un échantillon de m < 2·10^5,
  et toutes les valeurs D(n) de ce préfixe sont dans [inf, sup] (arithmétique exacte).
- Balayage flottant sur 2·10^8 lettres (`results/groupB_scan_2e8_float.txt`) : les extrêmes observés
  sont à l'intérieur de [inf, sup] et s'en approchent.
- A284364 : contre-exemple explicite en entiers exacts (`python/exact_A284364.py`).

## Cas d'égalité
A284369, lettre 1 : inf = −2 exactement, la borne conjecturée. La conjecture (stricte) reste vraie car
n·√3 est irrationnel, donc D(n) ≠ −2. Je n'ai pas étudié si les autres extrêmes sont atteints ;
les énoncés sûrs sont inf <= D(n) <= sup.

## Résultats
Voir `results/groupB_table.md`.
