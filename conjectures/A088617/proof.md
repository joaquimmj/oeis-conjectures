# A088617 — conjecture de Callan (2008) : vraie

**Énoncé.** T(n,k) = C(n+k,n)C(n,k)/(k+1) compte les chemins de Schröder de demi-longueur n avec k pas U. Le nombre
moyen E(n) de pas U vérifie E(n) ~ n/√2.

**Preuve.** r(k) = T(n,k+1)/T(n,k) = (n+k+1)(n−k)/((k+1)(k+2)) est strictement décroissante en k. Soit ε > 0 et
k± = (1 ± ε)n/√2. Pour n grand, r(k) ≥ 1 + δ pour k ≤ k₋ et r(k) ≤ 1 − δ pour k ≥ k₊, avec δ = δ(ε) > 0 : en effet
r(xn) → (1 + x)(1 − x)/x² = (1 − x²)/x², qui vaut 1 en x = 1/√2 et est strictement décroissante. Donc
Σ_{k≥k₊+m} T(n,k) ≤ T(n,k₊)(1−δ)^m/δ, de même à gauche, alors que la somme totale est ≥ T(n,⌊n/√2⌋) ≥ T(n,k₊).
La masse hors de [k₋ − O(1/δ), k₊ + O(1/δ)] est donc O(1/δ) fois une fraction bornée, et l'espérance hors de cette
fenêtre contribue O(n/δ²)·(1−δ)^(εn/2) → 0 relativement à n. Ainsi lim inf et lim sup de E(n)/n sont dans
[(1−ε)/√2, (1+ε)/√2] pour tout ε. ∎
**Contrôle** : `check.py` (E(n)/n pour n jusqu'à 4000, et la décroissance de r).
