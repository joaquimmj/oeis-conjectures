# Conjectures OEIS hors article — rapport (18/11/2026)

**Bilan : 12 lignes de résultats, 18 entrées concernées, toutes prouvées ; rien n'est soumis.**

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

**Écartées après Phase 0** : A178482 (déjà prouvée, Shallit–Vukusic 2025) ; A156253 (la récurrence de Maiga a
une note de 2025 dans l'entrée, non lue ; l'asymptotique 2n/3 équivaut à la densité de Kolakoski) ; A364648
(énoncé non exprimable directement dans Walnut : multiplication j·d) ; A285296, A356677, A370630 (suites
lexicographiques, pas d'angle) ; A001953/A001954, A022344, A070875, A133954, A189628 (non examinées en détail).

Walnut : github.com/firetto/Walnut, HEAD a4fe84e, compilé avec javac (OpenJDK 21), fastutil 8.5.13 et
automaton 1.12-4. Les lignes `#` des scripts `.wal` sont retirées avant exécution, car le REPL ne les accepte pas.
Rien n'a été soumis à l'OEIS. Pour A347171, le plan prévoit d'abord une note arXiv, et de vérifier avant dans l'article de 2001 qu'il ne contient pas déjà une preuve. Note LaTeX de A347171 (anglais, 3 pages, compilée avec pdflatex) : `A347171/paper/note.tex` et `note.pdf`. Brouillons : `*/draft.txt`. Aucune de ces preuves n'a été relue par un humain.
