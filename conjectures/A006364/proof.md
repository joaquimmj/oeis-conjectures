# A006364 — formule de Yanev (2016) : vraie (élémentaire)
Les termes vont par paires {2j, 2j+1} avec j maléfique, et le i-ème maléfique (i ≥ 0) vaut 2i + t(i), où t est la
suite de Thue-Morse. Donc a(2i+1) = 4i + 2t(i) et a(2i+2) = 4i + 2t(i) + 1 (offset 1).
- Pour n = 2i+1 : s(n−1) = s(i), (−1)^(n − s(i)) = −(−1)^{t(i)} et (3 + (−1)ⁿ)/2 = 1, d'où
  2n ∓ 1 − 1 = 4i + 2t(i).
- Pour n = 2i+2 : s(n−1) = s(i) + 1, le signe est le même et (3 + (−1)ⁿ)/2 = 2, d'où
  4i + 4 ∓ 1 − 2 = 4i + 2t(i) + 1. ∎
Contrôle : `check.py`.
