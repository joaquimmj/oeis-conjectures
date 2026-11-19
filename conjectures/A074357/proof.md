# A074356–A074360 : fonctions génératrices conjecturées des coefficients de nu(n) (Mathar 2009, Wu 2016, Barker 2017)

**Définition.** nu(0) = 1, nu(1) = b et nu(n) = b·nu(n−1) + λ(1 + q + … + q^{n−2})·nu(n−2). On note
c_j(n) = [q^j] nu(n) et C_j(x) = Σ c_j(n) xⁿ. Les entrées concernées :
- (b, λ) = (1, 3) : j = 2 (A074356), j = 3 (A074357) ;
- (b, λ) = (2, 2) : j = 1 (A074358), j = 2 (A074359), j = 3 (A074360).

**Théorème.** Les cinq f.g. conjecturées sont **vraies**. Les formules annexes le sont aussi :
- la récurrence d'ordre 6 de Barker pour A074356 ;
- la forme close et la récurrence d'ordre 4 de Barker pour A074358.

## Preuve
On a [q^i](1 + … + q^{n−2}) = 1 si 0 ≤ i ≤ n−2, et 0 sinon. D'où, pour n ≥ 2 :

  c_j(n) = b·c_j(n−1) + λ·Σ_{i=0}^{min(j, n−2)} c_{j−i}(n−2).

En multipliant par xⁿ et en sommant, on obtient :

  C_j(x)·(1 − bx − λx²) = [j = 0] + λx²·Σ_{i=1}^{j} (C_{j−i}(x) − Σ_{m<i} c_{j−i}(m) x^m).

En effet, le terme i n'apparaît qu'à partir de n − 2 = m ≥ i, et c_j(0) = c_j(1) = 0 pour j ≥ 1. C'est un
système triangulaire : C₀ = 1/(1 − bx − λx²), puis chaque C_j est une fraction rationnelle explicite.
`solve.py` le résout exactement avec sympy et compare à chaque conjecture : différence nulle dans les cinq cas
(`solve.out`).

Les formules annexes en découlent :
- **A074358.** Le dénominateur (1 − 2x − 2x²)² = 1 − 4x + 8x³ + 4x⁴ donne a(n) = 4a(n−1) − 8a(n−3) − 4a(n−4)
  pour n > 4, puisque le numérateur est de degré 4. La forme close de Barker vérifie la même récurrence, dont les
  racines sont 1 ± √3, doubles. Elle coïncide avec a sur n = 1..40, donc partout.
- **A074356.** Le dénominateur (1 − x − 3x²)³ et un numérateur de degré 7 donnent la récurrence d'ordre 6 pour
  n > 7.

**Contrôle indépendant.** Chaque C_j développé est comparé à c_j(n) calculé directement depuis la récurrence
polynomiale en q (60 termes), et aux données OEIS. ∎
