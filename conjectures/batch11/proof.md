# Lot 11 : A084091, A327551 (vraies), A088226 (vraie seulement avec n−1)

## A084091 : f.g. de Dirichlet L(χ₃, s)/(1 − 2^{−s}) (Stephan 2015) — vraie
On a y/(1 + y + y²) = y(1 − y)/(1 − y³) = Σ_m χ₃(m)y^m, où χ₃ est le caractère non trivial modulo 3. Avec
y = x^{2^k}, cela donne a(n) = Σ_{2^k | n} χ₃(n/2^k), d'où
Σ_n a(n)n^{−s} = Σ_k 2^{−ks}·Σ_m χ₃(m)m^{−s} = L(χ₃, s)/(1 − 2^{−s}). ∎

## A327551 : a(n) = A006694(n−1) + 2 = A081844(n−1) + 1 (Sloane 2019) — vraie
On numérote les positions 0, …, 2n−1. Le mélange (1, n+1, 2, n+2, …) envoie la carte de la position x sur la
position 2x mod (2n−1) pour x < 2n−1, et laisse la position 2n−1 fixe. Les cycles sont donc :
- les deux points fixes 0 et 2n−1 ;
- les orbites du doublement sur (ℤ/(2n−1)) ∖ {0}.

Les orbites du doublement sur ℤ/(2n−1) sont au nombre de A081844(n−1), en comptant l'orbite {0}, et
A006694 = A081844 − 1. D'où a(n) = A081844(n−1) − 1 + 2. ∎ (Pour n = 1, a(1) = 2.)

## A088226 : « a(n) = m/2, où m est la plus petite distance paire de n à un carré » (Stephan 2013) — fausse telle qu'écrite, vraie pour n−1
**Formule par blocs.** Pour k ≥ 1 et 0 ≤ m ≤ k : a(k² + 2m + 1) = m et a(k² + 2m + 2) = k − m (cette seconde formule
pour m ≤ k−1).

*Preuve par récurrence sur n,* avec a(n) = |a(n−1) − a(n−2) − a(n−3)| :
- **Intérieur d'un bloc (j ≥ 4).** Si n = k² + 2m + 1, on obtient |(k−m+1) − (m−1) − (k−m+2)| = m. Si
  n = k² + 2m + 2, on obtient |m − (k−m+1) − (m−1)| = k − m.
- **Bords**, où les trois valeurs précédentes sont prises dans le bloc k−1 :
  - j = 1 : |(k−1) − 1 − (k−2)| = 0 ;
  - j = 2 : |0 − (k−1) − 1| = k ;
  - j = 3 : |k − 0 − (k−1)| = 1.
- **Base.** Les premiers termes se vérifient directement. ∎

**Conséquence.** Soit N = n − 1 et t = ⌊√N⌋. Si N − t² est pair, a(n) = (N − t²)/2 ; sinon
a(n) = ((t+1)² − N)/2. C'est exactement le programme PARI de Stephan, appliqué à n − 1 et non à n. Avec l'offset 1
de l'entrée, l'énoncé littéral est faux dès n = 2 : la plus petite distance paire de 2 à un carré vaut 2, ce qui
donnerait 1, alors que a(2) = 0.

## Contrôles
`check.py` vérifie trois choses :
- A084091 sur 3000 termes, contre le développement en série de la définition ;
- A327551 par simulation du mélange jusqu'à n = 600, et contre les données ;
- A088226 : la formule par blocs jusqu'à n = 2·10⁴, et le décalage n−1, seul décalage qui convient.

Apport modeste pour les trois.
