# oeis-walnut

Preuves et réfutations de quatorze conjectures de l'OEIS sur des mots morphiques binaires (conjectures de
R. J. Mathar et de C. Kimberling), avec le prouveur Walnut, des preuves à la main et un calcul exact certifié.

**Soumis à l'OEIS le 15/11/2026, en relecture :** le contre-exemple de A284364, A284365 et A284366 (un commentaire
par entrée). Rien d'autre n'est soumis ni publié. Les preuves ne sont
pas encore relues par des pairs : chaque résultat porte son niveau de certitude dans `REPORT.md`.

## Résultats en bref

| Entrées | Résultat | Preuve |
|---|---|---|
| A284948 | conjecture vraie | Walnut (`walnut/groupA_uniform.txt`) |
| A285358, A285076 | conjectures vraies | à la main (`notes/groupA_handproofs.md`) et Walnut (`python/make_nonuniform.py`) |
| A284677 | énoncé d'origine faux (n = 6) ; forme corrigée vraie | à la main et Walnut |
| A285383 | déjà prouvée par A. Ashburn (arXiv:2610.04842) | rien à revendiquer |
| A283963, A283966, A284386, A284368, A284369, A284505, A045671, A045672 | bornes de Kimberling vraies ; inf et sup exacts, jamais atteints | calcul exact (`python/discrepancy_exact.py`, `python/attainment.py`) |
| A284386, A284368 | en plus : les quatre bornes prouvées par Walnut + un argument à la main | `python/make_sqrt13.py`, `notes/groupB_walnut_sqrt13.md` |
| A284364 | borne de Kimberling **fausse** ; plus petit contre-exemple n = 2977771 | calcul exact + entiers exacts (`python/exact_A284364.py`) |

Les bornes de Kimberling sont lues avec a(n) = position du n-ième 0 (ou 1) ; écrites littéralement avec un
compteur, elles sont fausses. Dans A284386 la constante r doit être (5+sqrt 13)/2.

## Contenu

- `REPORT.md` : résultats détaillés, niveau de certitude, limites. `LOG.md` : journal.
- `notes/` : preuves à la main (groupe A) et méthode du calcul exact (groupe B).
- `python/` : générations indépendantes des suites, vérifications, calcul exact.
- `walnut/` : automates, scripts Walnut et sorties brutes.
- `results/` : tables et sorties des calculs.
- `phase0/` : copies des entrées OEIS, b-files, historiques et pages lues (antériorité).
- `drafts/` : un brouillon de commentaire OEIS par entrée. `paper/` : brouillon d'article (`draft.tex`, `draft.pdf`).

## Rejouer

Python 3.9+ avec `numpy` ; Java 17+ pour Walnut ; un LaTeX (par exemple `tectonic`) pour l'article.

```bash
python3 python/check_phase0.py        # définitions contre les données OEIS
python3 python/check_live.py          # entrées et b-files (copies dans phase0/live)
python3 python/check_handproofs.py    # identités des preuves à la main
python3 python/discrepancy_exact.py   # bornes exactes du groupe B (~45 s)
python3 python/discrepancy_bracket.py # contrôle par un second algorithme
python3 python/attainment.py          # bornes atteintes ou non
python3 python/exact_A284364.py       # contre-exemple en entiers exacts
python3 python/scout_groupB.py        # balayage flottant, 2e8 lettres (~3 Go de RAM)
```

Walnut : cloner https://github.com/firetto/Walnut dans `../Walnut` (ou définir `WALNUT_DIR`), le compiler, puis
`python3 python/make_uniform.py` écrit les automates et `walnut/groupA_uniform.txt` se passe à Walnut sur
l'entrée standard. `python3 python/make_nonuniform.py` (avec `pip install licofage`, qui exige numpy < 2) refait les trois preuves non uniformes (~3 min). Le détail de la compilation est dans `LOG.md`.
