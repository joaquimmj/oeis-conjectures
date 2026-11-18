# A001462 (suite de Golomb) — conjecture de Song (2021) : vraie

**Énoncé.** a(n) ≥ n^(φ−1) pour tout n ≥ 1. Ici a est la suite de Golomb (n apparaît a(n) fois), φ le nombre d'or,
et α = φ − 1 = 1/φ.

**Notation.** S(m) = a(1) + … + a(m) = A001463(m) est la dernière position de la valeur m. Donc a(n) = m pour
S(m−1) < n ≤ S(m).

**Réduction.** Comme φ·α = 1 : a(n) ≥ n^α pour tout n ⇔ S(m) ≤ m^φ pour tout m. En effet, le pire n de valeur m
est n = S(m).

**Théorème.** Pour tout m ≥ 1 : m^φ/φ ≤ S(m) ≤ m^φ. En particulier, a(n) ≥ n^(φ−1) pour tout n, avec égalité
seulement en n = 1.

**Preuve**, par récurrence forte : P(m) désigne l'encadrement pour m.
- *Base.* P(m) est vérifié par calcul pour m ≤ 20 000 (`check.py`, 60 chiffres).
- *Hérédité*, pour m > 30 : on suppose P(v) pour tout v < m. Pour j ≤ m, posons v = a(j) ; alors v ≤ a(m) < m.
  - *Majoration.* On a j > S(v−1) ≥ (v−1)^φ/φ, d'où v < 1 + (φj)^α. En sommant :
    S(m) < m + φ^α Σ_{j≤m} j^α ≤ m + φ^α ∫₁^{m+1} x^α dx < m + φ^(α−1)(m+1)^φ.
    Ce dernier terme est ≤ m^φ ⇔ h(m) := φ^(α−1)(1 + 1/m)^φ + m^(1−φ) ≤ 1. Or h est décroissante (ses deux termes
    le sont) et h(30) ≈ 0,99964 < 1.
  - *Minoration.* On a j ≤ S(v) ≤ v^φ, d'où a(j) = v ≥ j^α, puis S(m) ≥ Σ_{j≤m} j^α ≥ ∫₀^m x^α dx = m^φ/φ. ∎

**Remarques.**
- La constante asymptotique S(m)/m^φ → φ^(−φ(2−φ)) ≈ 0,743 (Fine, Vardi) laisse une marge. L'argument est
  élémentaire et ne l'utilise pas.
- L'autre conjecture de l'entrée (van Lamoen 2005, sommes des lignes et suite de Levine A014644) découle de la
  relation (4) de Claes–Miyamoto, arXiv:2602.10992 (2026). Elle n'est pas comptée ici.

**Contrôle** : `check.py`.
