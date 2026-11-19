# A304451, A304452 : b(n) = least new, a(n) = b(n) + b(⌊n/2⌋), b(0) = 1

**Conjectures.** a(n)/n → 5/2 et −1 ≤ 5/2 − a(n)/n ≤ 2 pour n ≥ 1 ; b(n)/n → 5/3 et −1 ≤ 5/3 − b(n)/n ≤ 2 pour
n ≥ 1.

**Statut.**
- Les deux limites sont **vraies**.
- Les inégalités sont **fausses telles qu'écrites** en petit n : b(1) = 3 donne 5/3 − 3 = −4/3 < −1 ; a(1) = 4 et
  a(2) = 8 donnent −3/2 < −1. Elles sont vraies pour n ≥ 3, et vraies pour tout n si l'on divise par n + 1 au
  lieu de n.

## Lemme 1
On a b(n) = n + 1 + #{k : a(k) < b(n)} et n + 1 ≤ b(n) ≤ 2n + 1.

*Preuve.* b et a sont strictement croissantes, et b(n) < a(n), car b(⌊n/2⌋) ≥ 1. Quand b(n) est choisi, tous les
entiers < b(n) sont déjà placés. Ce sont b(0), …, b(n−1) et les a(k) < b(n), qui ont tous un indice k < n, puisque
a(k) < b(n) entraîne b(k) < a(k) < b(n). Réciproquement, aucun entier ≥ b(n) n'a encore été placé, sauf des a(k)
qui sont > b(n). Comme #{k : a(k) < b(n)} ≤ n, l'encadrement suit.

## Théorème : b(n)/n → 5/3 et a(n)/n → 5/2
Soient β⁺ = limsup b(n)/n et β⁻ = liminf b(n)/n. Par le lemme 1, on a 1 ≤ β⁻ ≤ β⁺ ≤ 2.

**Majoration.** Soit ε > 0. Pour m ≥ M, b(m) ≥ (β⁻ − ε)m, donc
a(k) = b(k) + b(⌊k/2⌋) ≥ (β⁻ − ε)(3k/2 − 1) − C. Par conséquent #{k : a(k) < y} ≤ 2y/(3(β⁻ − ε)) + C′, et le
lemme 1 donne b(n) ≤ n + 1 + 2b(n)/(3(β⁻ − ε)) + C′. D'où b(n)/n ≤ f(β⁻ − ε) + o(1), avec f(x) = 3x/(3x − 2)
(on a 3(β⁻ − ε) > 2). Ainsi β⁺ ≤ f(β⁻).

**Minoration.** Le même argument, appliqué avec b(m) ≤ (β⁺ + ε)m, donne β⁻ ≥ f(β⁺).

**Conclusion.** f est décroissante sur (2/3, ∞). Donc β⁺ ≤ f(β⁻) ≤ f(f(β⁺)) = g(β⁺), avec g(x) = 9x/(3x + 4).
Or g(x) < x pour x > 5/3, d'où β⁺ ≤ 5/3. De même, β⁻ ≥ g(β⁻) et g(x) > x sur (0, 5/3), d'où β⁻ ≥ 5/3. Donc
b(n)/n → 5/3, puis a(n)/n → 5/3 + 5/6 = 5/2. ∎

## Inégalités
- Pour n ≥ 3, par le lemme 1 : a(n) ≤ (2n + 1) + (n + 1) = 3n + 2 et a(n) ≥ n + 2. La borne 3n + 2 ≤ 7n/2 vaut
  pour n ≥ 4 ; pour n = 3, on a a(3) = 9 ≤ 21/2. On a aussi b(n) ≤ 2n + 1 ≤ 8n/3 pour n ≥ 2, et b(n) ≥ 0. Les
  encadrements sont donc vrais pour n ≥ 3, et faux pour n = 1 (pour a et pour b) et n = 2 (pour a).
- Avec le dénominateur n + 1, les mêmes bornes donnent l'encadrement pour tout n ≥ 0.

## Contrôles
`check.py` génère les suites depuis la définition (`gen.py`, 3·10⁵ termes, sans automate). Il vérifie le lemme 1
terme à terme, la liste exacte des échecs (n = 1, 2 pour a ; n = 1 pour b), l'absence d'échec avec n + 1, et les
rapports a(N)/N ≈ 2,49995 et b(N)/N ≈ 1,66665.
