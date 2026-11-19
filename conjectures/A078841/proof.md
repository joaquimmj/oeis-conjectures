# A078841 : conjecture de R. G. Wilson v (2007), lim a(n+1)/a(n) = 2 — vraie

**Définition.** a(n) est le (n+1)-ième entier m tel que Ω(m) = n (nombre de facteurs premiers, avec multiplicité).
Les premiers termes sont 1, 3, 9, 20, 54, 112, …

**Théorème.** On pose V = {u/2^{Ω(u)} : u impair ≥ 1}, compté avec multiplicité et rangé en ordre croissant :
t₁ ≤ t₂ ≤ …. Alors a(n) = 2ⁿ·t_{n+1} pour tout n ≥ 0, et a(n+1)/a(n) = 2·t_{n+2}/t_{n+1} → 2.

## Preuve
1. **Bijection.** Un entier m avec Ω(m) = n s'écrit de façon unique m = 2^{n−j}·u, avec u impair et Ω(u) = j ≤ n.
   L'application m ↦ m/2ⁿ = u/2^j est donc une bijection croissante entre {m : Ω(m) = n} et
   V_n = {u/2^{Ω(u)} ∈ V : Ω(u) ≤ n}.
2. **V_n et V ont les mêmes petits éléments.** Si Ω(u) = j, alors u ≥ 3^j, donc u/2^j ≥ (3/2)^j. Les éléments de V
   absents de V_n sont donc > (3/2)ⁿ. D'autre part, t_{n+1} ≤ p_{n+2}/2, car les p/2 (p premier impair) et 1 sont
   dans V. Pour n ≥ 10, p_{n+2}/2 < (3/2)ⁿ, donc les n+1 plus petits éléments de V sont dans V_n, et
   a(n) = 2ⁿ·t_{n+1}. Pour n < 10, et en fait pour les 30 termes connus, l'égalité est vérifiée directement
   (`check.py`).
3. **Rapport.** V est localement fini : u/2^j ≤ y impose (3/2)^j ≤ y et u ≤ 2^j y. Donc t_k → ∞. Soit ε > 0. Par le
   théorème des nombres premiers, il existe pour y assez grand un premier p dans (2y, 2y(1+ε)], c'est-à-dire un
   élément p/2 de V dans (y, y(1+ε)]. En prenant y = t_k, on obtient t_k ≤ t_{k+1} ≤ (1+ε)t_k pour k assez grand.
   Ainsi t_{k+1}/t_k → 1, et a(n+1)/a(n) = 2t_{n+2}/t_{n+1} → 2. ∎

## Contrôle
`check.py` calcule Ω par crible jusqu'à 2·10⁶. Il énumère V ∩ [0, 122], ensemble complet pour ce rayon, et
retrouve a(n) = 2ⁿ·t_{n+1} pour les 30 termes de l'entrée. Le rapport maximal t_{k+1}/t_k sur la seconde moitié
vaut 1,015.

## Remarques
- La preuve n'utilise que t_{k+1}/t_k → 1, qui découle du théorème des nombres premiers (et même de « p_{k+1}/p_k → 1 »).
- Preuve relue seulement par l'auteur (une IA). Nouveauté à vérifier : l'énoncé a pu être noté ailleurs, mais
  l'entrée ne cite aucune preuve.
