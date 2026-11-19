# A155200 : conjecture de P. D. Hanna (2009), v₂(a(n)) = s₂(n) (nombre de 1 binaires) — vraie

**Définition.** A(x) = Σ a(n)xⁿ = exp(Σ_{n≥1} 2^{n²}·xⁿ/n).

**Théorème.** Pour tout n ≥ 0, v₂(a(n)) = s₂(n) = A000120(n) : a(n)/2^{s₂(n)} est un entier impair.

## Preuve (valuations 2-adiques dans ℚ₂)
On écrit A(x) = exp(2x)·R(x), avec R(x) = exp(Σ_{n≥2} 2^{n²}xⁿ/n) = Σ r(t)x^t.
1. **Le facteur exp(2x) = Σ 2^j x^j/j!.** Par la formule de Legendre, v₂(j!) = j − s₂(j), donc
   v₂(2^j/j!) = s₂(j).
2. **Le facteur R.** Le coefficient r(t) est une somme, sur les k ≥ 1 et les décompositions t = n₁ + … + n_k avec
   n_i ≥ 2, de termes Π_i (2^{n_i²}/n_i)/k!. On a v₂(k!) ≤ k − 1, et n² − v₂(n) ≥ n + 1 pour n ≥ 2 (égalité en
   n = 2). Chaque terme a donc une valuation ≥ Σ_i (n_i + 1) − (k − 1) = t + 1. Par ultramétrie,
   v₂(r(t)) ≥ t + 1 pour t ≥ 1.
3. **Conclusion.** a(n) = Σ_{t=0}^{n} (2^{n−t}/(n−t)!)·r(t).
   - Le terme t = 0 a pour valuation s₂(n).
   - Pour t ≥ 1, la valuation est ≥ s₂(n−t) + t + 1 ≥ s₂(n−t) + s₂(t) + 1 ≥ s₂(n) + 1, par la sous-additivité
     de s₂.

   Donc v₂(a(n)) = s₂(n). ∎

## Contrôle
`check.py`, en arithmétique exacte, vérifie v₂(a(n)) = s₂(n) pour n ≤ 300, la formule de l'étape 1 pour j ≤ 300,
et v₂(r(t)) ≥ t + 1 pour t ≤ 120.
