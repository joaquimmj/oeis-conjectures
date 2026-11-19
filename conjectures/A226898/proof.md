# A226898 (Δ de Hooley) — conjecture de Greathouse (2026) : vraie

**Énoncé.** Pour n > 4, Δ(n) ≤ d(n)/2, où Δ(n) est le maximum, sur u > 0, du nombre de diviseurs de n dans
[u, e·u].

**Preuve.**
- *Si un premier impair q divise n.* On range les diviseurs de n en chaînes d₀, d₀q, …, d₀q^v (avec q ∤ d₀ et
  v = v_q(n) ≥ 1). Elles sont au nombre de d(n)/(v+1) et ont chacune au moins deux éléments. Deux éléments d'une même
  chaîne ont un rapport ≥ q ≥ 3 > e, donc un intervalle [u, e·u] contient au plus un élément par chaîne. Ainsi
  Δ(n) ≤ d(n)/(v+1) ≤ d(n)/2.
- *Si n = 2^v.* Un intervalle de rapport e < 4 contient au plus deux puissances de 2. Donc Δ(n) ≤ 2 ≤ (v+1)/2 dès
  v ≥ 3, c'est-à-dire n ≥ 8.

Les seuls n > 4 restants n'existent pas (5, 6 et 7 ont un facteur impair). Les exceptions n = 1, 2, 4 sont bien des
contre-exemples pour n ≤ 4. ∎
**Contrôle** : `check.py` (données de l'entrée, et l'énoncé pour 4 < n ≤ 200 000).
