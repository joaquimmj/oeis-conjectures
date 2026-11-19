# A079267 — conjecture de Callan (2012) : vraie

**Énoncé.** d(n,s) = nombre de couplages parfaits de {1, …, 2n} ayant s paires courtes. Asymptotiquement, la ligne n
suit une loi de Poisson de paramètre 1 : d(n,s)/(2n−1)!! → e^(−1)/s! pour tout s.

**Preuve.** La formule de l'entrée (inclusion-exclusion) donne
d(n,s)/(2n−1)!! = (1/s!) Σ_{h=s}^{n} (−1)^(h−s) r_h(n)/(h−s)!, avec
r_h(n) = (2n−h)!·2^h·n!/((2n)!·(n−h)!) = Π_{i<h} 2(n−i)/(2n−i).
Chaque facteur est ≤ 1, donc 0 ≤ r_h(n) ≤ 1, et r_h(n) → 1 pour h fixé. Par convergence dominée (majorant
1/(h−s)!, sommable), la limite vaut (1/s!)Σ_{j≥0} (−1)^j/j! = e^(−1)/s!. ∎
**Contrôle** : `check.py` (données de l'entrée, r_h ≤ 1, et valeurs pour n ≤ 300).
