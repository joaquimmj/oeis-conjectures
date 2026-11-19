# A074355 : f.g. conjecturée par Stephan (2004) — fausse telle qu'écrite, vraie avec la correction évidente

**Définition.** nu(0) = 1, nu(1) = 1, et nu(n) = nu(n−1) + 3(1 + q + … + q^{n−2})·nu(n−2). a(n) = [q¹] nu(n).

**Conjecture de l'entrée :** G.f. (9x⁴ + 3x³)/(1 − 3x − 3x²)². **Fausse** : le coefficient de x⁴ vaut 27, alors que
a(4) = 15.

**Correction prouvée :** G.f. = (9x⁴ + 3x³)/(1 − x − 3x²)².

*Preuve.* On écrit nu(n) = c₀(n) + c₁(n)q + O(q²). Le coefficient constant de 1 + … + q^{n−2} vaut 1, et celui
de q vaut 1 si n ≥ 3, et 0 si n = 2. Donc :
- c₀(n) = c₀(n−1) + 3c₀(n−2), d'où C₀(x) = 1/(1 − x − 3x²) (c'est A006130) ;
- c₁(n) = c₁(n−1) + 3c₁(n−2) + 3c₀(n−2)·[n ≥ 3], avec c₁(0) = c₁(1) = 0.

Il en résulte C₁(x)(1 − x − 3x²) = 3x²(C₀(x) − 1) = 3x²(x + 3x²)/(1 − x − 3x²), d'où
C₁ = (3x³ + 9x⁴)/(1 − x − 3x²)². ∎

**Contrôle :** `check.py` (sympy, 40 termes, depuis la définition).
