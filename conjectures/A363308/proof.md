# A363308 — conjecture (2023) : a(n) impair ⇔ n = 0 ou n est une puissance de 2. Vraie.

**Preuve**, dans GF(2)[[x]]. Soit P = Σ_{k≥0} x^(2^k). On sait que Cat(m) est impair ⇔ m = 2^k − 1, donc C ≡ P/x.
De plus P² = P + x (Frobenius). Soit y = x·C(x)³ (de valuation 1) et A = 1 + P. Alors A² = 1 + P² = A + x, et
y ≡ C²·(xC) ≡ ((P + x)/x²)·P = (P² + xP)/x² = (P + x + xP)/x².
Un calcul direct donne (P + x + xP)(1 + x + P) = x²P, d'où y·A² = P = A + 1, c'est-à-dire A = 1 + y·A².
Or F = C(y) est l'unique série telle que F = 1 + y·F² (y étant de valuation ≥ 1, l'équation détermine les
coefficients un par un), et cette identité passe à la réduction modulo 2. Donc C(y) ≡ A = 1 + Σ x^(2^k) (mod 2). ∎
**Contrôle** : `check.py` (données de l'entrée, énoncé pour n < 300, identité modulo 2 jusqu'à x^2048).
