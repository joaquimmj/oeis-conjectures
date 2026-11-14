# Groupe A, morphismes non uniformes : preuves Walnut dans une numération de Dumont–Thomas

Statut : **Walnut TRUE pour les trois égalités** (14/11/2026), sorties brutes dans `walnut/groupA_nonuniform_*.out`.
Chaque fichier contient 16 TRUE et 2 FALSE, tous conformes à l'attendu. Les preuves à la main de
`notes/groupA_handproofs.md` ne sont pas utilisées.

Rejouer (depuis la racine du dépôt, environ 3 minutes, un cœur, tas Java limité à 1 Go) :

    ../.venv/bin/python python/make_nonuniform.py        # WALNUT_DIR, défaut ../Walnut

## Les trois cas

| Cas | numération | morphisme μ, graine | mot U (DFAO écrit par le script) | mot V | morphisme ν de V | énoncé prouvé (indices à partir de 0) |
|---|---|---|---|---|---|---|
| A285358 | `msd_dtp` | σ : 0→10, 1→1101, graine 1 | `UP[i]` = A285358(i+1) | `VP[i]` = A284929(i+1) | τ : 0→01, 1→1011 | ∀n UP[n] = VP[n+1] |
| A285076 | `msd_dtq` | ψ² : 0→01010, 1→1001010, graine 1 | `UQ[i]` = A285076(i+1) | `VQ[i]` = A285073(i+1) | ψ² | ∀n≥2 UQ[n] = VQ[n] |
| A284677 | `msd_dtr` | ψ² : 0→0111, 1→1011101110111, graine 1 | `UR[i]` = A284677(i+1) | `VR[i]` = A284674(i+1) | ψ² | ∀n≥2 UR[n] = VR[n] |

Les offsets OEIS valent 1 pour les six suites (ligne %O de `phase0/seq/*.seq`, vérifiée par le script), d'où le décalage
d'indice : « a(n) = b(n) pour n ≥ 3 » s'écrit U[n] = V[n] pour n ≥ 2, et « A285358(n) = A284929(n+1) pour n ≥ 1 »
s'écrit U[n] = V[n+1] pour n ≥ 0.

## Méthode

1. **Numération.** `licofage -W dtX -D $WALNUT_DIR "1->…, 0->…"` produit l'automate du langage (`msd_dtX.txt`) et
   l'additionneur (`msd_dtX_addition.txt`, 24, 25 et 22 états) de la numération de Dumont–Thomas de μ depuis la lettre 1.
   Copies dans `walnut/`. L'additionneur n'est **pas** cru sur parole : voir « Validation de la numération ».
2. **DFAO de U.** États = lettres, état initial = graine, chiffre d : c → μ(c)[d].
3. **Longueur des images.** Automate `shdtX(n,m)` écrit par le script : « m = n suivi du chiffre 0 ». Il n'est pas cru non
   plus : Walnut prouve que c'est une fonction totale f avec f(0) = 0 et f(n+1) = f(n) + |μ(U[n])| (`f_fun`, `f_zero`,
   `f_rec`), donc f(n) = |μ(U[0..n))| par récurrence.
4. **U est le point fixe** (`u_fixed`) : U[0] = graine et, pour tout n, U[f(n)+j] = μ(U[n])[j] pour 0 ≤ j < |μ(U[n])|.
   Les blocs [f(n), f(n+1)) recouvrent ℕ, donc μ(U) = U ; μ(1) commence par 1 et est de longueur > 1, donc U = μ^ω(1).
5. **V dans la même numération.** V est défini dans Walnut à partir de U (`def` puis `combine`) :
   A285358 : V[0] = 0 et V[n] = U[n−1] ; les deux autres : V[0] = 0, V[1] = 1, V[n] = U[n] pour n ≥ 2.
   Puis g(n) = |ν(V[0..n))| est défini par cas (`gdtX`) et Walnut prouve g(0) = 0, g(n+1) = g(n) + |ν(V[n])| (`g_rec`)
   et **V[0] = 0 et ν(V) = V** (`v_fixed`). Donc V = ν^ω(0), c'est-à-dire la suite OEIS annoncée.
6. **Égalité** (`main`) et deux contrôles qui doivent être FALSE (`control1`, `control2`).

Attention à la portée logique : comme V est construit à partir de U, l'évaluation `main` est vraie presque par
construction. Le contenu mathématique est dans `v_fixed` : c'est lui qui prouve que le mot ainsi construit est bien le
point fixe de τ (resp. le second point fixe de ψ²). La preuve de chaque égalité est la conjonction
`u_fixed` + `v_fixed` + `main`, plus les axiomes de la numération. Je n'ai pas construit de DFAO de V indépendant de U.

## Validation de la numération (dans Walnut, pour chacune des trois)

Walnut (lu dans `NumberSystem.java`) compare les entiers d'une base personnalisée par l'ordre lexicographique des mots
complétés par des zéros à gauche, teste l'égalité par égalité des mots, prend 0 = 0*, 1 = 0*1 et fabrique les autres
constantes par additions. Le langage est stable par ajout et retrait de zéros à gauche (vérifié par le script), donc cet
ordre est l'ordre radix, de type ω : « n » désigne le n-ième mot du langage. On définit succ par l'ordre seul :
`succ(x,y) := x<y & ~Et (x<t & t<y)`. Walnut renvoie TRUE pour :

- `ax_total` : ∀x,y ∃z x+y=z ; `ax_fun` : z unique ;
- `ax_zero` : x+0=z ⇔ x=z ; `ax_comm` : x+y=z ⇔ y+x=z ;
- `ax_succ_total` : tout x a un successeur ; `ax_one` : la constante 1 est succ(0) ;
- `ax_succ` : x+y=z ⇒ x+succ(y) = succ(z).

Par récurrence sur y, la relation de l'additionneur est donc l'addition des rangs, et les constantes, `n+1`, `n-1`,
`m+13` utilisées ensuite sont les bonnes. Aucune propriété de la théorie de Dumont–Thomas n'est supposée.
Non fait : associativité (inutile ici) et le script `Command Files/check_dtX.txt` fourni par licofage.

## Validation des DFAO (Python, hors preuve)

Pour chaque DFAO (U écrit par le script, V tel que Walnut l'a produit, relus depuis `walnut/*.txt`) : simulation sur les
200 000 premiers mots du langage `msd_dtX` en ordre radix, comparée à l'itération directe du morphisme : identique dans
les six cas. Les termes %S/%T/%U de `phase0/seq` sont des préfixes des mots engendrés (six suites).

## Contrôles FALSE

- A285358 : U[n] = V[n] et U[n] = V[n+2].
- A285076 : la borne abaissée (n ≥ 1) et le décalage U[n] = V[n+1].
- A284677 : la borne abaissée (n ≥ 1) et l'énoncé d'origine de l'OEIS a(n) = A284674(n−1), soit U[n] = V[n−1] :
  FALSE, ce qui confirme mécaniquement qu'il est faux.

## Ce qui reste supposé

- La correction de Walnut (HEAD a4fe84e) et sa sémantique des bases personnalisées telle que lue dans le source.
- Trois arguments élémentaires faits à la main : l'ordre radix est de type ω (récurrence licite) ; les axiomes ci-dessus
  caractérisent l'addition ; un point fixe d'un morphisme est déterminé par sa première lettre a quand μ(a) commence
  par a et |μ(a)| > 1.
- L'identification des suites OEIS avec ces points fixes (définitions des entrées ; contrôlée sur les termes publiés).

## Détails pratiques

- Dans un `def`, Walnut ordonne les arguments par nom de variable : `gdtX` est écrit avec i (indice) et j (longueur).
- `ax_succ` est écrit avec des ∃ imbriqués pour ne pas dépasser 4 pistes : la forme à 5 variables épuise 1 Go de tas
  quand il y a 13 chiffres (`msd_dtr`).
- Walnut affiche « 0 states » pour une conjonction de deux formules closes ; le résultat est correct (testé sur trois
  conjonctions de valeur connue).
- Effets de bord : `pip install licofage` a rétrogradé numpy de 2.0.2 à 1.26.4 dans `../.venv` (licofage exige numpy<2).
  Dans `$WALNUT_DIR`, licofage et Walnut ont écrit `Custom Bases/msd_dt{p,q,r}*.txt`, `Word Automata Library/Dt*.txt`,
  `U*.txt`, `V*.txt`, `Command Files/check_dt*.txt`, `Automata Library/{sh,succ,v1,g}dt*.txt` et des fichiers `Result/`.
