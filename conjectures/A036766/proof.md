# A036766 : récurrence polynomiale conjecturée par R. J. Mathar (2015) — vraie (pour n ≥ 2)

La f.g. A(x) vérifie A = 1 + xA + (xA)² + (xA)³ + (xA)⁴ (Kruchinin). La conjecture est une récurrence
Σ_{i=0}^{5} p_i(n) a(n−i) = 0 de degré 5 en n.

**Preuve exacte (`verify.py`).**
1. On a Σ_n p_i(n) a(n−i) xⁿ = xⁱ p_i(θ + i)A, avec θ = x d/dx.
2. On calcule l'opérateur L = Σ_i xⁱ p_i(θ + i) appliqué à A dans ℚ(x)[Y]/(P), où P(x, Y) = Y − Σ_k (xY)^k, en
   utilisant Y′ = −P_x/P_Y, avec un inverse calculé modulo P.
3. Résultat : L(A) = 8328 + 6660x. C'est un polynôme de degré 1 : le coefficient de xⁿ du membre de gauche est
   nul pour tout n ≥ 2, et la récurrence est vraie pour tout n ≥ 2 (a(m) = 0 pour m < 0). ∎

**Contrôle :** la récurrence est vérifiée directement sur les 29 termes de l'entrée.
