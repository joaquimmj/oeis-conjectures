# A010048 (Stephan 2004) : P_n(x) = Σ_k C_F(n,k)·x^k est réductible si et seulement si n est impair > 1 — **partiel, non compté**

- **Sens « si » (n impair ⇒ réductible) : prouvé.** Comme C_F(n,k) = C_F(n,n−k), le polynôme est palindromique :
  P_n(x) = xⁿ·P_n(1/x). Pour n impair, P_n(−1) = −P_n(−1) = 0, donc (x+1) | P_n.
- **Sens « seulement si » (n pair ⇒ irréductible) : vérifié pour n ≤ 60** (`factor.py`, `factor.out`), ainsi que
  l'irréductibilité de P_n/(x+1) pour n impair ≤ 59. Pas de preuve générale : aucun critère d'irréductibilité
  standard ne s'applique, faute de nombre premier pour Eisenstein puisque les coefficients extrêmes valent 1.
