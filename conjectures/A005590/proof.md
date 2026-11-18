# A005590 — conjecture de Stephan (2003) : vraie

**Énoncé.** a(0) = 0, a(1) = 1, a(2n) = a(n), a(2n+1) = a(n+1) − a(n). Conjecture : a(3n) = 0 ⇔ n est
fibbinaire (A003714 : pas deux bits 1 consécutifs).

**Théorème.** C'est vrai. De plus, si n n'est pas fibbinaire, a(3n) est pair et |a(3n)| ≥ 2.

**Preuve.**
1. Soit u(n) = (a(3n), a(3n+1), a(3n+2), a(3n+3)). La définition donne a(6n) = a(3n),
   a(6n+1) = a(3n+1) − a(3n), a(6n+2) = a(3n+1), a(6n+3) = a(3n+2) − a(3n+1), etc. D'où
   u(2n) = B₀ u(n) = (a₀, a₁−a₀, a₁, a₂−a₁) et u(2n+1) = B₁ u(n) = (a₂−a₁, a₂, a₃−a₂, a₃), avec
   u(0) = (0, 1, 1, 0). On calcule u(n) en lisant les bits de n depuis le poids fort.
2. Soit P_m = (0, 1, 1, −2m) et Q_m = (0, 1, −2m−1, −2m). On a B₀P_m = P₀, B₁P_m = Q_m et B₀Q_m = P_{m+1}.
   Comme u(0) = P₀, tant que les bits lus ne contiennent pas « 11 », l'état est un P_m (après un 0) ou un
   Q_m (après un 1). En particulier a(3n) = 0 si n est fibbinaire.
3. Soit I = { a₀(a₀−a₁) > 0, a₁(a₁−a₂) > 0, a₂(a₂−a₃) > 0 } (« chaque rapport consécutif est < 1 »).
   On note C₁, C₂, C₃ les trois quantités. Après B₀, elles deviennent C₁ + a₀², C₁ et C₂ + a₁² ; après B₁,
   elles deviennent C₂, C₃ + a₂² et C₃. Elles restent donc > 0 : I est stable par B₀ et B₁.
4. Au premier « 11 », l'état est B₁Q_m = (−2m−2, −2m−1, 1, −2m), qui est dans I : C₁ = 2m+2,
   C₂ = (2m+1)(2m+2) et C₃ = 2m+1. Par 3, l'état reste dans I, et I impose a₀ ≠ 0. Donc a(3n) ≠ 0 si n
   n'est pas fibbinaire.
5. Parité : le motif (pair, impair, impair, pair) est stable par B₀ et B₁ et vaut au départ (0, 1, 1, 0).
   Donc a(3n) est pair, et |a(3n)| ≥ 2 au point 4. ∎

**Contrôles** : `check_symbolic.py` (identités du point 3, sympy) et `check.py` (points 1, 2 et 4, l'énoncé, et
l'appartenance à I pour tout n < 2^21, depuis la définition).
