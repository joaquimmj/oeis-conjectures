# A285126 et A285127 — conjectures de Kimberling (2017) : FAUSSES

**Mot.** A285125 = mot 0-limite de σ : 0 → 10, 1 → 0000 (point fixe de σ² issu de 0). A285126 et A285127 listent
les positions de 0 et de 1. La matrice de σ a pour valeurs propres (1 ± √17)/2. La seconde vaut ≈ −1,56, de module
> 1 : σ n'est pas de Pisot.

**Conjectures.** 0 < n·r − a(n) < 1 avec r = 1,3903… (A285126) et −3 < n·s − b(n) < 0 avec s = 3,5621… (A285127),
où r = 1/f₀ = 1,39038820… et s = 1/f₁ = 3,56155281… sont les inverses des fréquences de 0 et de 1 (vecteur de Perron (4, λ − 1), λ = (1+√17)/2 ; calcul dans `search.py`).

**Contre-exemples** (dans les données mêmes des entrées) :
- A285126 : n = 3, a(3) = 3, 3r − 3 ≈ 1,1712 > 1 ;
- A285127 : n = 2, b(2) = 11, 2s − 11 ≈ −3,8769 < −3.

**De plus**, la discrépance n'est pas bornée (|λ₂| > 1). Sur 3·10⁶ lettres, n·r − a(n) atteint 1017,3 et n·s − b(n)
descend à −2603,3. ∎
**Contrôle** : `search.py` (positions recalculées et comparées aux données des entrées).
