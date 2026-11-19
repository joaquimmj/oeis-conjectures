# A123722, A123723 : nombre de carrés modulo n (Bernard, ~2006) — vraies ; A123365 (cubes) — partielle

s(n) désigne le nombre de carrés modulo n (A000224). Il est multiplicatif. Formules classiques aux puissances
premières (vérifiées par `check.py`) :
- s(2) = 2 ;
- s(2^b) = (2^{b−1} + 4)/3 pour b ≥ 2 pair, et (2^{b−1} + 5)/3 pour b ≥ 3 impair ;
- pour p impair, s(p^e) = (p^{e+1} + p + 2)/(2(p+1)) pour e pair, et (p^{e+1} + 2p + 1)/(2(p+1)) pour e impair ;
  en particulier s(p) = (p+1)/2.

**Lemme.** Pour r impair, s(r) ≤ (r+1)/2, avec égalité si et seulement si r = 1 ou r est premier.
*Preuve.* Pour p^e avec e ≥ 2, les formules donnent s(p^e) < (p^e+1)/2. Pour au moins deux facteurs, l'inégalité
(q₁+1)(q₂+1)/4 < (q₁q₂+1)/2, qui équivaut à (q₁−1)(q₂−1) > 0, donne une inégalité stricte par récurrence. ∎

## A123722 : s(n) = ⌈(n+1)/3⌉
**Conjecture :** (i) si un terme n > 3 est multiple de 3, alors n/3 est premier ; (ii) 3p est un terme pour tout
premier impair p.

(ii) Pour p ≠ 3, s(3p) = 2·(p+1)/2 = p + 1 = ⌈(3p+1)/3⌉. Pour p = 3, s(9) = 4 = ⌈10/3⌉.

(i) On écrit n = 3^a·r avec 3 ∤ r. L'équation devient s(n) = n/3 + 1.
- **a = 1.** On obtient 2s(r) = r + 1. Si r est pair, le membre de droite est impair : impossible. Si r est
  impair, le lemme impose r premier (r = 1 donne n = 3). Donc n/3 = r est premier.
- **a ≥ 2.** On a s(3^a)/3^a ≤ 4/9, alors qu'il faut s(n)/n > 1/3. Il faut donc Π_{q ∥ r} s(q)/q > 3/4. Or
  s(q)/q ≤ 3/5 pour toute puissance q d'un premier impair ≥ 5, et s(2^b)/2^b ≤ 1/2 pour b ≥ 2. D'où r ∈ {1, 2}.
  - r = 2 (n = 18) : s(18) = 8 ≠ 7.
  - r = 1 : s(3^a) = 3^{a−1} + 1. Les formules ne laissent que a = 2 (et a = 1). Donc n = 9, et 9/3 = 3 est
    premier. ∎

## A123723 : s(n) = ⌈(n+1)/4⌉
**Conjecture :** si un terme n > 4 est multiple de 4, alors n/4 est premier.

On écrit n = 2^b·r avec r impair et b ≥ 2. L'équation devient s(2^b)·s(r) = 2^{b−2}r + 1.
- **b = 2.** s(4) = 2, donc s(r) = (r+1)/2, et r est premier par le lemme (r = 1 donne n = 4, exclu).
- **b = 3.** s(8) = 3, donc s(r) = (2r+1)/3 ≤ (r+1)/2, ce qui impose r ≤ 1. Donc n = 8, et 8/4 = 2 est premier.
- **b ≥ 4.** s(2^b)/2^b ≤ 1/4, avec égalité seulement pour b = 4, et s(r)/r ≤ 1, avec égalité seulement pour
  r = 1. Comme il faut s(n)/n > 1/4, il ne reste que n = 16, et s(16) = 4 ≠ 5. ∎

## A123365 (cubes) : non prouvée
La conjecture dit que les k avec A046530(k) = (k+2)/3 sont 1 et les premiers ≡ 1 (mod 6).
- `scan.py` (`scan.out`) : aucun contre-exemple jusqu'à 3·10⁶.
- Deux faits partiels :
  - un premier p ≡ 2 (mod 3), p ≠ 2, ne peut pas diviser k exactement une fois, car c(p) = p diviserait
    (k+2)/3 ;
  - k = p·q avec p, q ≡ 1 (mod 3) est impossible, car (p−1)(q−1) = 0.
- Le cas général résiste : les rapports locaux 3c(q)/q sont tantôt > 1, tantôt < 1.
- Non comptée.
