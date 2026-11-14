# LOG

- 2026-11-14 : Phase 0. Téléchargement des .seq (oeisdata), génération indépendante, tests numériques, recherche web. Voir phase0/README.md. oeis.org, b-files (LFS), arxiv.org et cs.uwaterloo.ca inaccessibles depuis la session.
- 2026-11-14 : Phase 1. Walnut 6 (github.com/firetto/Walnut, HEAD a4fe84e) compilé avec javac sous OpenJDK 21 ; Gradle 7.5.1 du dépôt incompatible avec Java 21 ; fastutil 8.5.13 au lieu de 8.5.12 (absent du miroir Maven). Test `?msd_fib An Em m>n` : TRUE.
- 2026-11-14 : Phase 2. Échauffement = A285383 (résultat connu d'Ashburn) : TRUE. A284948 : TRUE. Preuves à la main pour A285358, A285076, A284677 (notes/groupA_handproofs.md). Brouillons dans drafts/.
- 2026-11-14 : Phase 3. Groupe B traité par calcul exact (Dumont–Thomas + système max/min contractant, vérifié dans Q(√d)) : `python/discrepancy_exact.py`, résultats dans `results/`. Pas de preuve Walnut pour ce groupe (voir notes/groupB_method.md). Tentative d'installation de l'outil licofage refusée par la session ; méthode reconstruite sans lui. Brouillons OEIS pour les 9 entrées, brouillon d'article `paper/draft.tex`.
- 2026-11-14 : dépôt git local initialisé (auteur : Joaquim Manji-Jung). Création du dépôt GitHub impossible depuis la session.
