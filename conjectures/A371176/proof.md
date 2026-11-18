# A371176 — conjecture de Kotesovec (2025) : vraie, et la limite existe

**Énoncé.** a(n) = n-ième entier k ≥ 1 tel que A000120(k) ≤ A001511(k).
Conjecture : lim sup log a(n) / log n = log 2 / log φ.

**Théorème.** log a(n) / log n → log 2 / log φ (la limite existe).

**Preuve.**
0. (Branicky, dans l'entrée) k ↔ X = {positions des bits 1 de k, le bit de poids faible ayant la position 1}.
   A000120(k) = |X| et A001511(k) = min X. Donc k est dans la suite ⇔ X est un ensemble de Schreier
   non vide (|X| ≤ min X), et 2^(m−1) ≤ k < 2^m ⇔ max X = m.
1. Soit s(m) le nombre d'ensembles de Schreier de maximum m. Alors s(m) = F_m.
   s(1) = 1 ({1}) et s(2) = 1 ({2}). Pour m ≥ 3, on décale de −1 : X ↦ X − 1. C'est une bijection entre les ensembles
   de Schreier de maximum m vérifiant |X| < min X et tous les ensembles de Schreier de maximum m − 1 (l'inverse
   X ↦ X + 1 augmente le minimum, donc préserve la condition). Il reste les ensembles « serrés » |X| = min X = j.
   Ils sont formés de j, de m et de j − 2 éléments pris dans ]j, m[, d'où Σ_j C(m−j−1, j−2) = F_{m−2},
   par l'identité classique Σ_i C(N−i, i) = F_{N+1}. Donc s(m) = s(m−1) + F_{m−2}, d'où s(m) = F_m par récurrence.
2. N(m) = #{n : a(n) < 2^m} = Σ_{j ≤ m} F_j = F_{m+2} − 1.
3. Si a(n) a m bits, alors N(m−1) < n ≤ N(m), donc φ^m / C ≤ n ≤ C·φ^m et 2^(m−1) ≤ a(n) < 2^m pour une
   constante C, d'où log a(n) = m log 2 + O(1) et log n = m log φ + O(1). Le rapport tend vers log 2 / log φ. ∎

**Contrôle** : `check.py` (étapes 1 à 3 pour m ≤ 22, depuis la définition). La lenteur de la convergence
(1,419 en n = 46 367) vient du terme O(1)/m.
