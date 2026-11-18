# Conjectures OEIS hors article — rapport (18/11/2026)

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
| A347171 | Doche–Mendès France 2001 : racines réelles | en cours | — | — |

Walnut : github.com/firetto/Walnut, HEAD a4fe84e, compilé avec javac (OpenJDK 21), fastutil 8.5.13 et
automaton 1.12-4. Les lignes `#` des scripts `.wal` sont retirées avant exécution, car le REPL ne les accepte pas.
Rien n'a été soumis à l'OEIS. Brouillons : `*/draft.txt`. Aucune de ces preuves n'a été relue par un humain.
