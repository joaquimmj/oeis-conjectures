# A047863 : les cinq observations de R. Stephan (2013) — vraies

a(n) = Σ_k C(n,k)·2^{k(n−k)}. Stephan observe :
- (i) 5 ∤ a(n) ;
- (ii) a(n) est pair pour n > 0 ;
- (iii) 3 | a(2n) pour n > 0 ;
- (iv) 7 | a(6n+5) ;
- (v) 13 | a(12n+3).

**(ii).** Les termes k = 0 et k = n valent 1 chacun, et tous les autres sont pairs.

**Lemme (périodicité).** Pour p premier impair, n ↦ a(n) mod p est périodique de période p − 1 sur n ≥ 1.

*Preuve.* Soit d = ord_p(2), qui divise p − 1. Comme 2^{k(n−k)} mod p ne dépend que de k(n−k) mod d, il est de
la forme g(k mod d, n mod d). Soit ζ ∈ 𝔽_p une racine primitive d-ième de l'unité. On a
[k ≡ r (mod d)] = d⁻¹·Σ_j ζ^{j(k−r)}, d'où

  a(n) ≡ d⁻¹·Σ_{r=0}^{d−1} g(r, n mod d)·Σ_{j=0}^{d−1} ζ^{−jr}·(1 + ζ^j)ⁿ  (mod p).

Chaque (1 + ζ^j)ⁿ est périodique de période divisant p − 1 pour n ≥ 1 (il est nul pour tout n ≥ 1 si
1 + ζ^j = 0), et g(r, n mod d) est de période d | p − 1. ∎

**Conséquences** (calcul sur une période, `check.py`) :
- (i) a(1..4) ≡ 2, 1, 1, 2 (mod 5), jamais 0 ;
- (iii) modulo 3, la période est 2, et a(2) ≡ 0 ;
- (iv) modulo 7, la période est 6, et a(5) ≡ 0 ;
- (v) modulo 13, la période est 12, et a(3) ≡ 0.

**Contrôle :** `check.py` vérifie aussi la périodicité directement, en arithmétique exacte, pour n < 200 et
p = 3, 5, 7, 13. Apport modeste.
