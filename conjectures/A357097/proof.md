# A357097 — A(A019586(x), A019586(y)) = A019586(A101330(x,y)) : vraie

**Énoncé.** A(·,·) est la multiplication des lignes du tableau de Wythoff étendu définie dans l'entrée,
A019586(n) est la ligne (à partir de 0) du tableau de Wythoff qui contient n, et A101330(x,y) = x∘y est le produit
de Fibonacci de Knuth : si x = Σ F(cᵢ) et y = Σ F(dⱼ) sont les représentations de Zeckendorf (indices ≥ 2),
x∘y = Σ F(cᵢ + dⱼ).

**Preuve.**
1. **L'anneau.** Soit ω = 1/φ = φ − 1, de sorte que ω² = 1 − ω. La loi de l'entrée
   (j₁,k₁)∘(j₂,k₂) = (j₁j₂ + k₁k₂, j₁k₂ + k₁j₂ − k₁k₂) est la multiplication de j + kω dans ℤ[φ]. Comme
   (j + kω)·φ = (j + k) + jω, passer de (eW(n,m+1), eW(n,m)) à (eW(n,m+2), eW(n,m+1)) revient à multiplier par φ.
   Donc S_n = {β_n·φ^m : m ∈ ℤ} pour un β_n ∈ ℤ[φ], et les S_n sont deux à deux disjoints (une paire de termes
   consécutifs détermine sa ligne).
2. **L'élément d'un entier.** Pour n ≥ 1, de Zeckendorf n = Σ F(cᵢ), soit θ(n) = Σ φ^{cᵢ}. Comme
   φ^c = F(c−1) + F(c)·φ, on a θ(n) = a + nφ avec a = Σ F(cᵢ − 1). Dans le tableau de Wythoff, le successeur de n
   dans sa ligne est s(n) = Σ F(cᵢ + 1) (Kimberling 1995 : le tableau de Zeckendorf est le tableau de Wythoff).
   La paire (s(n), n) est dans S_{A019586(n)}, et son élément est s(n) + nω = (s(n) − n) + nφ = θ(n).
3. **θ est multiplicative : θ(x)·θ(y) = θ(x∘y).** Le coefficient de φ dans θ(x)θ(y) = Σ φ^{cᵢ+dⱼ} est
   Σ F(cᵢ + dⱼ) = x∘y. Reste le terme entier. Soit ψ = −1/φ le conjugué. Le conjugué de θ(n) est Σ ψ^{cᵢ}, somme finie
   d'exposants ≥ 2 non adjacents, donc strictement compris entre ψ³ + ψ⁵ + … = −1/φ² et ψ² + ψ⁴ + … = 1/φ.
   L'intervalle I = (−1/φ², 1/φ) est de longueur 1 : pour N donné, il y a donc au plus un entier a tel que le
   conjugué a + Nψ soit dans I, et θ(N) est cet élément. Or le conjugué de θ(x)θ(y) est le produit de deux
   nombres de I, donc compris entre −1/φ³ et 1/φ², donc dans I. Ainsi θ(x)θ(y) = θ(x∘y).
4. **Conclusion.** Soit u = A019586(x), v = A019586(y). Par 2, θ(x) ∈ S_u et θ(y) ∈ S_v. Par définition de A,
   le produit est dans S_{A(u,v)}. Par 3, ce produit est θ(x∘y), qui est dans S_{A019586(x∘y)}. Les S_n étant
   disjoints, A(u, v) = A019586(x∘y). ∎

**Remarque.** Le point 3 est la remarque d'Arnoux (1989) sur la multiplication de Fibonacci, citée dans l'entrée ;
je ne l'ai pas lue, l'argument ci-dessus est autonome.

**Contrôle** : `check.py` (formule de l'entrée pour A, données de l'entrée, multiplicativité de θ en entiers et
conjecture pour 1 ≤ x ≤ y < 400).
