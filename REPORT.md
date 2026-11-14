# REPORT (14/11/2026)

| Cible | Résultat | Niveau de certitude |
|---|---|---|
| A285383 | a(n) = A035263(n-1), n >= 2 : vraie | Walnut TRUE (échauffement). Déjà prouvée : Ashburn, arXiv:2610.04842. Rien à soumettre. |
| A284948 | a(n) = A096268(n-2), n >= 2 : vraie | **Walnut TRUE** ; automates vérifiés contre génération directe sur 3e5 termes ; énoncé vérifié sur 2e6 termes. |
| A285358 | a(n) = A284929(n+1), n >= 1 : vraie | Preuve à la main (pas Walnut) ; identités vérifiées par machine ; 2e6 termes. |
| A285076 | a(n) = A285073(n), n >= 3 : vraie | Preuve à la main ; découle aussi du commentaire de Dekking (2017). |
| A284677 | énoncé d'origine faux (n = 6) ; a(n) = A284674(n), n >= 3 : vraie | Contre-exemple exact ; preuve à la main de la forme corrigée. |
| A284364 | conjecture de Kimberling fausse (lecture « positions ») | Contre-exemple en entiers exacts : n = 2977771 (lettre 1), n = 8933313 (lettre 0). Pas encore via Walnut. |
| Reste du groupe B | non traité | Exploration flottante seulement (phase0/README.md). |

Limites : oeis.org, arxiv.org inaccessibles depuis la session ; b-files non comparés (sauf deux par SHA-256) ;
texte intégral d'Ashburn non lu. Pas de dépôt git (identité de Joaquim non configurée).
