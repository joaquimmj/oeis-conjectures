# A049473, A001953, A001954 : conjecture de C. Kimberling (2014) sur la queue de ζ(3) — vraie

**Énoncé** (identique dans les trois entrées). Soit s(m) = ζ(3) − Σ_{k≤m} 1/k³ = Σ_{k>m} 1/k³, et
a(n) = A049473(n), l'entier le plus proche de n/√2. Alors :
- (i) s(a(n)) < 1/n² < s(a(n)−1) pour n ≥ 1 ;
- (ii) les différences de A049473 valent 0 ou 1, les 1 étant aux positions A001953 et les 0 aux positions A001954.

(Dans (i), « a(n) » désigne A049473. Lu littéralement dans A001953 et A001954, avec la suite de l'entrée,
l'énoncé serait faux : par exemple s(⌊(n+½)√2⌋ − 1) ≈ 1/(4n²) < 1/n².)

## Deux inégalités exactes (télescopage)
- **(T1)** s(a) < 1/(2a(a+1)) pour a ≥ 1. En effet 1/k³ < 1/(k(k²−1)) = 1/(2(k−1)k) − 1/(2k(k+1)) pour k ≥ 2 ;
  on somme sur k > a.
- **(T2)** s(a−1) = Σ_{k≥a} 1/k³ > 1/(2a² − 2a + 1) pour a ≥ 1. Avec h(k) = 1/(2k² − 2k + 1), on a
  h(k) − h(k+1) = 4k/(4k⁴ + 1) < 1/k³ ; on somme sur k ≥ a (h → 0).

## Preuve de (i)
Soit a = a(n) ≥ 1 l'entier le plus proche de n/√2. On a a − ½ < n/√2 < a + ½ (n/√2 est irrationnel), c'est-à-dire
(2a−1)² < 2n² < (2a+1)².
- Les carrés impairs et 2n² sont de parités différentes, donc (2a+1)² ≥ 2n² + 1. Ainsi 2a(a+1) ≥ n², et (T1)
  donne s(a) < 1/(2a(a+1)) ≤ 1/n².
- De même, (2a−1)² ≤ 2n² − 1, donc 2a² − 2a + 1 = ((2a−1)² + 1)/2 ≤ n², et (T2) donne
  s(a−1) > 1/(2a² − 2a + 1) ≥ 1/n². ∎

Le cas le plus serré est celui des solutions de Pell 2n² − (2a−1)² = 1 (n = 5, 29, 169, 985, …). L'écart y est
d'ordre 1/(24a⁶), mais (T2) est une inégalité exacte.

## Preuve de (ii)
On pose d(m) = a(m+1) − a(m) ∈ {0, 1}, puisque 1/√2 < 1. On a d(m) = 1 si et seulement si un demi-entier j + ½
appartient à (m/√2, (m+1)/√2], c'est-à-dire m < (j+½)√2 < m + 1, soit m = ⌊(j+½)√2⌋ = A001953(j). Le complémentaire
de A001953 est A001954 : suites de Beatty non homogènes avec 1/√2 + 1/(2+√2) = 1 (théorème de Fraenkel),
vérifié ici jusqu'à 10⁶. ∎

## Contrôles
`check.py` et `scan.py` vérifient :
- les inégalités T1 et T2 (exactes pour k < 2000, en multi-précision jusqu'à 10⁵) ;
- (i) pour n ≤ 2·10⁴, plus tous les n ≤ 10⁶ proches d'un demi-entier (2064 cas, `scan.py`) ;
- (ii) pour m < 10⁶.
