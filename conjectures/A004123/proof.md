# A004123 et A006531 — conjectures de Bala (2022) : vraies, avec la forme générale

**Énoncés.**
- A004123 (e.g.f. 1/(3 − 2eˣ)) : pour tout k ≥ 1, a(n) mod k est ultimement périodique, de période divisant φ(k).
- Bala, dans A004123 : il en va de même pour toute suite entière d'e.g.f. G(eˣ − 1), G ∈ ℤ[[x]].
- A006531 (semi-ordres, a(n) = Σ (−1)^(n+j) Cat(j) j! S(n,j)) : même énoncé.

**Théorème.** Si a a pour e.g.f. G(eˣ − 1) avec G = Σ gⱼ xʲ ∈ ℤ[[x]], alors pour tout k ≥ 1, (a(n) mod k) est
périodique à partir de n = ⌈log₂ k⌉, avec une période divisant λ(k) (fonction de Carmichael), donc divisant φ(k).

**Preuve.** (eˣ − 1)ʲ/j! = Σₙ S(n,j) xⁿ/n!, donc a(n) = Σⱼ gⱼ·j!·S(n,j). Comme k | j! pour j ≥ k,
a(n) ≡ Σ_{j<k} gⱼ·j!·S(n,j) = Σ_{j<k} gⱼ Σ_{i≤j} (−1)^(j−i) C(j,i) iⁿ (mod k). Donc a(n) ≡ Σ_{i<k} cᵢ·iⁿ (mod k), avec
des cᵢ entiers. Pour chaque i, écrivons k = k₁k₂, où k₁ ne contient que les premiers divisant i et pgcd(i, k₂) = 1.
Alors iⁿ ≡ 0 (mod k₁) dès que n ≥ log₂ k₁, et iⁿ mod k₂ est périodique de période l'ordre de i, qui divise
λ(k₂) | λ(k). On conclut par les restes chinois, et λ(k) | φ(k).
- A004123 : 1/(3 − 2eˣ) = 1/(1 − 2(eˣ − 1)), donc gⱼ = 2ʲ.
- A006531 : a(n) = (−1)ⁿ·b(n), où b correspond à gⱼ = (−1)ʲ·Cat(j). Le facteur (−1)ⁿ a une période 2, qui divise
  λ(k) pour k ≥ 3, et vaut 1 modulo 1 et 2. ∎

**Remarque.** L'argument est classique (comme pour les nombres de Fubini) ; je n'ai pas cherché de référence. Il
donne même une période divisant λ(k), plus fin que φ(k) (par exemple λ(8) = 2 et φ(8) = 4).
**Contrôle** : `check.py` (k ≤ 60, avec en plus 3 séries G aléatoires).
