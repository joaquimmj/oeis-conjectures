# A170941 — conjecture de Callan (2012) : vraie

**Énoncé.** a(n) compte les involutions de [n] sans transposition adjacente (i, i+1) (Callan, dans l'entrée).
Alors a(n)/I(n) → 1/e, où I(n) = A000085(n) est le nombre d'involutions.

**Preuve.** Par inclusion-exclusion sur les ensembles de h transpositions adjacentes disjointes (il y en a
C(n−h, h)) : a(n) = Σ_h (−1)^h C(n−h, h)·I(n−2h). Posons t_h(n) = C(n−h, h)·I(n−2h)/I(n). Comme
I(m) ≥ (m−1)·I(m−2), on a I(n) ≥ Π_{i<h}(n−1−2i)·I(n−2h). D'autre part C(n−h, h) = Π_{i<h}(n−h−i)/h!, et
n − h − i ≤ n − 1 − 2i pour i ≤ h − 1. Donc 0 ≤ t_h(n) ≤ 1/h!. Pour h fixé, C(n−h, h) ~ n^h/h! et
I(n−2h)/I(n) ~ n^(−h), puisque I(m)/I(m−1) ~ √m. Donc t_h(n) → 1/h!. Par convergence dominée,
a(n)/I(n) → Σ (−1)^h/h! = 1/e. ∎
**Contrôle** : `check.py` (inclusion-exclusion = récurrence de l'entrée pour n < 400, force brute pour n ≤ 8,
domination, et rapport 0,3858 en n = 399). La convergence est lente.
