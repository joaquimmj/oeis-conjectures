# Neuf conjectures de Velin Yanev (2016-2025) : toutes vraies (preuves élémentaires)

1. **A129527** : a(n) = 2n − A000265(n) (partie impaire). f(n) = 2n − odd(n) vérifie f(2n+1) = 2n + 1 et
   f(2n) = 4n − odd(n) = f(n) + 2n, f(0) = 0 : c'est la définition.
2. **A173614** : lcm_{p|n}(p − 1) = λ(rad n). rad n est sans facteur carré, donc λ(rad n) = lcm λ(p) = lcm(p − 1)
   (λ(2) = 1 = 2 − 1).
3. **A023887** : σ_m(n) = σ(n^m rad(n)^(m−1))/σ(rad(n)^(m−1)). Les deux membres sont multiplicatifs ; en pᵉ :
   σ(p^(me+m−1))/σ(p^(m−1)) = (p^(m(e+1)) − 1)/(p^m − 1) = σ_m(pᵉ).
4. **A055210** : Σ_{d²|n} φ(d²) = σ₂(n/core n)/σ₁(n/core n). Multiplicatif ; en pᵉ avec t = ⌊e/2⌋ :
   1 + (p − 1)Σ_{j=1..t} p^(2j−1) = (p^(2t+1) + 1)/(p + 1) = σ₂(p^(2t))/σ₁(p^(2t)).
5. **A367865** : Σ_{d|n} d·φ(d)·μ(d)² = (rad n/n)·Σ_{k=1..n} rad(nk)/rad(k). rad(nk)/rad(k) = Π_{p|n, p∤k} p dépend de
   k mod rad n. Sur n/rad n périodes complètes, et par les restes chinois, la somme vaut (n/rad n)·Π_{p|n}((p−1)p + 1).
   Le membre de droite vaut donc Π_{p|n}(p² − p + 1), qui est aussi le membre de gauche (seuls les d sans facteur
   carré comptent : Π(1 + p(p−1))).
6. **A090079** : a(n) = (2^(r+1) + [n impair] − 2)/3 avec r = A005811(n), le nombre de blocs. a(n) est le mot
   alterné 1010… de longueur r ; il vaut (2^(r+1) − 1)/3 s'il finit par 1 (n impair) et (2^(r+1) − 2)/3 sinon.
7. **A163617** : a(n) = g(n) + (6n + 1 − (−1)ⁿ)/4, g = code de Gray. Avec g(2n) = 2g(n) + (n mod 2) et
   g(2n+1) = 2g(n) + 1 − (n mod 2), le membre de droite R vérifie R(2n) = 2R(n) et R(2n+1) = 2R(n) + 2 + (−1)ⁿ
   (car 1 − 2(n mod 2) = (−1)ⁿ), avec R(0) = 0.
8. **A285385** : a(n+1) = a(n) + A096268(a(n) − 1) + 1. Par `../A072939/proof.md`, a liste les m ≥ 1 tels que
   m − 1 a un nombre pair de zéros finaux (ou m = 1). Si v₂(m) est pair, m + 1 est le suivant. Sinon m est pair, m + 1
   est exclu, et m + 2 convient (m + 1 impair). Or A096268(m − 1) = v₂(m) mod 2 (mot de doublement de période).
9. **A179504** : σ_n(2n) = σ_n(n)·((2ⁿ − 1)/(2^(n(v+1)) − 1) + 2ⁿ), v = v₂(n). Le rapport σ_n(2n)/σ_n(n) vaut
   σ_n(2^(v+1))/σ_n(2^v) = (2^(n(v+2)) − 1)/(2^(n(v+1)) − 1), égal au facteur annoncé. ∎

**Contrôle** : `check.py` (données des entrées et identités, sur des milliers de valeurs).
