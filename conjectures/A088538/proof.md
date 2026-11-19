# A088538 — conjecture d'Aktar (2007) : vraie

**Énoncé.** u(0) = 1 + i, u(n+1) = (u(n) + |u(n)|)/2. Alors lim Re u(n) = 4/π.

**Preuve.** Pour z = r·e^(iθ), r > 0, |θ| < π : (z + |z|)/2 = r(1 + e^(iθ))/2 = r·cos(θ/2)·e^(iθ/2).
Comme u(0) = √2·e^(iπ/4), par récurrence u(n) = √2·Π_{k=1..n} cos(π/2^(k+2))·e^(iπ/2^(n+2)).
Le produit de Viète Π_{k≥1} cos(θ/2^k) = sin θ/θ, avec θ = π/4, donne u(n) → √2·(√2/2)/(π/4) = 4/π (et Im u(n) → 0). ∎
**Contrôle** : `check.py` (forme close et limite, 50 chiffres).
