# Groupe B, cas unimodulaires (Q(√13)) : bornes de Kimberling pour A284386 et A284368 par Walnut

Statut (15/11/2026) : **les quatre bornes conjecturées sont prouvées**, par une preuve en deux étages :
un lemme de quasi-additivité **prouvé par Walnut** (TRUE, sorties brutes `walnut/groupB_sqrt13_A284386.out` et
`walnut/groupB_sqrt13_A284368.out`, 22 TRUE et 4 FALSE de contrôle chacune, tous conformes à l'attendu), puis un
argument **à la main** de dix lignes (lemme de Fekete, fréquence, irrationalité de √13) qui en déduit la borne réelle.
Walnut ne manipule aucun réel et la preuve n'utilise aucun flottant.

**Non prouvé mécaniquement** : que ces mots sont sturmiens, la forme a(n) = ⌊n·r + β⌋ et les valeurs exactes de inf et
sup (elles restent au niveau « calcul exact » de `notes/groupB_method.md`). La voie Ostrowski n'a pas été essayée.

Rejouer (depuis la racine du dépôt, environ 30 secondes, un cœur, tas Java 1 Go) :

    ../.venv/bin/python python/make_sqrt13.py        # WALNUT_DIR, défaut ../Walnut

## Énoncés

x = point fixe commençant par 1, indexé à partir de 1 comme dans l'OEIS (offset 1). p_L(n) = position du n-ième L.
r = (5+√13)/2, r' = (−1+√13)/2. Lecture « positions » des conjectures, comme dans `REPORT.md`.

| Suite | morphisme | lettre | énoncé OEIS | lemme prouvé par Walnut, pour tous i, j ≥ 1 | éval |
|---|---|---|---|---|---|
| A284386 | 0→1, 1→1101 | 0 | 0 < n·r − p(n) < 2 | p(i)+p(j) ≤ p(i+j) ≤ p(i)+p(j)+2 | `A284386_main0` TRUE |
| A284386 | | 1 | −1 < n·r' − p(n) < 1 | p(i)+p(j)−1 ≤ p(i+j) ≤ p(i)+p(j)+1 | `A284386_main1` TRUE |
| A284368 | 0→1, 1→1011 | 0 | 1 < n·r − p(n) < 3 | p(i)+p(j)+1 ≤ p(i+j) ≤ p(i)+p(j)+3 | `A284368_main0` TRUE |
| A284368 | | 1 | −1 < n·r' − p(n) < 1 | p(i)+p(j)−1 ≤ p(i+j) ≤ p(i)+p(j)+1 | `A284368_main1` TRUE |

## Choix de la voie : (A) Dumont–Thomas, sans partie entière

- Dans la numération de Dumont–Thomas du morphisme μ, f(n) = |μ(x[0..n))| est « ajouter le chiffre 0 ». Ici
  |μ(0)| = 1 et |μ(1)| = 4, donc f(n) = n + 3·(nombre de 1 dans x[0..n)) : le comptage des lettres, puis la position
  du n-ième 0 ou 1, se définissent en logique du premier ordre à partir de f. Rien à deviner, et toute la chaîne
  de validation de `make_nonuniform.py` se réutilise telle quelle.
- La comparaison à n·r ne passe ni par ⌊n·r⌋ ni par un automate deviné : la quasi-additivité de p (énoncé
  purement entier, à deux variables) suffit, par Fekete. Les constantes entières qui sortent sont exactement celles
  de Kimberling, parce que sup − inf = 1 dans ces quatre cas (c'est là que sert le caractère « sturmien »).
- La voie (B) aurait demandé de deviner le mot sturmien et la fonction f dans la numération d'Ostrowski, et de
  s'appuyer sur le théorème de Schaeffer–Shallit–Zorcic pour ⌊nα+β⌋. Plus d'hypothèses externes, pas moins.
- Limite de la méthode : elle donne A < n·r − p(n) < B avec A, B entiers, pas inf et sup. Elle ne donne les bornes
  conjecturées que si sup − inf ≤ 1, donc pas pour les autres suites du groupe B.

## Chaîne logique

Notations Walnut pour A284386 (numération `msd_dts`, mot `KS`) ; pour A284368 : `msd_dtt`, `KT`, suffixe `dtt`.
Indices Walnut à partir de 0 : `KS[i]` = x(i+1).

1. **Numération** : licofage produit le langage et l'additionneur (18 états). Walnut prouve les sept axiomes
   `ax_*` (addition totale, fonctionnelle, x+0 = x, commutative, compatible avec le successeur défini par l'ordre) :
   l'additionneur est l'addition des rangs. Même argument que `notes/groupA_walnut_nonuniform.md`.
2. **Mot** : `f_fun`, `f_zero`, `f_rec` : `shdts(n,m)` est la fonction m = f(n) = |μ(KS[0..n))|.
   `u_fixed` : KS[0] = 1 et μ(KS) = KS, donc KS = μ^ω(1) = x.
3. **Comptage** : `onedts(i,j)` := ∃m f(i) = m ∧ m = i + 3j. Walnut prouve que c'est une fonction totale, nulle en 0,
   qui augmente de 1 exactement quand KS[i] = 1 (`one_fun`, `one_zero`, `one_rec`) : par récurrence c'est le nombre
   de 1 dans KS[0..i). Idem `zerdts` pour les 0 (`zer_*`). La formule f = n + 3·(nombre de 1) n'est donc pas supposée.
4. **Positions** : `pzdts(i,j)` := i ≥ 1 ∧ j ≥ 1 ∧ KS[j−1] = 0 ∧ « KS[0..j) contient i zéros ». La
   j-ième lettre x(j) est un 0 et c'est le i-ième : j = p_0(i), position comptée à partir de 1. `pos0_fun` : fonction
   totale sur i ≥ 1. Idem `podts` pour les 1 (`pos1_fun`).
5. **Quasi-additivité** (`main0`, `main1`) : pour tous i, j ≥ 1, avec u = p(i)+p(j) (`szdts`) et t = p(i+j) (`tzdts`) :
   u + A ≤ t ≤ u + B, (A,B) = (0,2), (−1,1), (1,3), (−1,1) selon la ligne du tableau.
6. **À la main, Fekete** : p + A est sur-additive et p + B sous-additive, donc p(n)/n a une limite ℓ, avec
   (p(n)+A)/n ≤ ℓ ≤ (p(n)+B)/n pour tout n ≥ 1, soit A ≤ n·ℓ − p(n) ≤ B.
7. **À la main, valeur de ℓ** : Z(m) = nombre de 0 dans x[1..m]. Z(p_0(n)) = n et p_0 est croissante, donc
   Z(m)/m → d = 1/ℓ_0. Walnut prouve (`density`) Z(f(n)) = n − Z(n), avec f(n) = n + 3(n − Z(n)) → ∞. En divisant par
   n : d = (1−d)/(4−3d), soit 3d² − 5d + 1 = 0 ; la racine (5+√13)/6 dépasse 1, donc d = (5−√13)/6 et
   ℓ_0 = 1/d = (5+√13)/2 = r. Pour les 1 : ℓ_1 = 1/(1−d) = 6/(1+√13) = (−1+√13)/2 = r'.
8. **À la main, inégalités strictes** : ℓ est irrationnel, n ≥ 1 et p(n) entier, donc n·ℓ − p(n) n'est pas entier :
   A < n·ℓ − p(n) < B. C'est l'énoncé OEIS (avec r corrigé en (5+√13)/2 pour A284386, coquille signalée dans `REPORT.md`).

## Contrôles FALSE (Walnut)

Pour chaque lettre, le lemme resserré d'une unité de chaque côté : `control*_low` (A+1 au lieu de A) et
`control*_up` (B−1 au lieu de B) : 8 FALSE, tous obtenus. Les constantes A et B du lemme sont donc optimales.
Ce contrôle porte sur le lemme entier. Pour la borne réelle resserrée d'une unité, le script vérifie en entiers exacts
(13n² comparé à un carré) qu'elle est fausse dès n ≤ 3 dans les huit cas (dernière ligne de sortie de chaque lettre).

## Validations hors preuve (Python, dans le script)

- DFAO `KS`, `KT` : simulés sur les 200 000 premiers mots du langage en ordre radix, identiques à l'itération directe
  du morphisme ; préfixes conformes aux termes %S/%T/%U et à l'offset 1 de `phase0/seq/A284386.seq`, `A284368.seq`.
- Automates de position construits par Walnut (`pz*`, `po*`, copiés dans `walnut/`) : acceptent (n, p(n)) et
  rejettent (n, p(n)+1) et (n+1, p(n)) pour tous les n tels que p(n) < 200 000 (46 481 zéros, 153 517 uns),
  p calculé par comptage direct.
- Sur la même plage, l'inégalité OEIS elle-même, en entiers exacts : vraie partout.
- Quasi-additivité vérifiée par force brute pour i, j < 750 avant de lancer Walnut (non conservé dans le script).

## Ce qui reste supposé

- La correction de Walnut (HEAD a4fe84e) et sa sémantique des bases personnalisées, comme pour le groupe A.
- Les arguments à la main : étapes 6 à 8 ci-dessus, plus les trois du groupe A (ordre radix de type ω, les axiomes
  caractérisent l'addition, unicité du point fixe commençant par 1).
- L'identification des suites OEIS avec ces points fixes, et la lecture « positions » de la conjecture.
- L'associativité de l'additionneur n'est pas vérifiée à part ; elle découle de « l'additionneur est l'addition des
  rangs » (étape 1).

## Ce qui a échoué ou n'a pas été fait

- Rien n'a échoué : tout est passé au premier lancement de Walnut (un seul bogue, d'indice, dans le contrôle Python).
- Pas de preuve mécanique du caractère sturmien ni de inf/sup exacts ; pas de numération d'Ostrowski.
- Pas encore relu par des pairs.

## Détails pratiques

- Fichiers ajoutés : `python/make_sqrt13.py`, `walnut/groupB_sqrt13_*` (commandes `.txt`, sorties `.out`, copies de la
  numération, des DFAO, de l'automate de décalage et des automates de position).
- Effets de bord dans `$WALNUT_DIR` : `Custom Bases/msd_dt{s,t}*.txt`, `Word Automata Library/{KS,KT,Dts*,Dtt*}.txt`,
  `Automata Library/*dt{s,t}.txt`, `Command Files/check_dt{s,t}.txt`, fichiers `Result/A28438*_*`.
- Les fonctions utilitaires sont recopiées de `make_nonuniform.py` : ce script n'a pas de garde `__main__`, l'importer
  relancerait les trois preuves du groupe A.
