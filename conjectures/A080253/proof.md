# A080253 — conjecture de Bala : a(n) mod k est ultimement périodique, de période divisant φ(k). Vraie
E.g.f. eˣ/(2 − e^(2x)). Avec u = eˣ − 1 : e^(2x) − 1 = u² + 2u, donc eˣ/(2 − e^(2x)) = (1 + u)/(1 − 2u − u²) = G(u),
avec G à coefficients entiers (g₀ = 1, g₁ = 3, g_j = 2g_{j−1} + g_{j−2}). Par le théorème de `../A004123/proof.md`,
a(n) mod k est périodique dès n ≥ log₂ k, avec une période divisant λ(k), qui divise φ(k). ∎
**Contrôle** : `check.py` (identité a(n) = Σ gⱼ j! S(n,j), et période pour k < 80).
