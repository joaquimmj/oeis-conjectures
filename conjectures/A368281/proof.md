# A368281 / A368282 — conjecture (2024) : vraie pour tout n ≥ 1

**Énoncé.** La somme partielle de la ligne n de A368281 (point fixe de 0 → R(n), 1 → R(n)0, avec R(n) = 1ⁿ) est la
ligne n de A368282 (b(0) = 0, b(k) = k − b(⌊b(k−1)/n⌋)).

**Preuve.** C'est exactement le théorème de `../A366860/proof.md` (cas k = n), prouvé pour tout n ≥ 1. ∎
**Contrôle** : `check.py` (lecture des deux tableaux de l'OEIS et le théorème pour n ≤ 11, k ≤ 10^5).
