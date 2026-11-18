# A070864 — conjecture de Layman (2002) : vraie (preuve par récurrence rédigée)

**Énoncé.** a(1) = a(2) = 1, a(n) = 2 + a(n − a(n−1)). Layman : avec K = ⌊√(n+1)⌋ et d = n − K² + 1,
a(n) = 2K − 1 si d ∈ {0, 1, 2} ou d pair, et 2K + 1 sinon. L'entrée contient des formules équivalentes de Cloitre
(2002, « by induction ») et de Curgus (2011), sans preuve écrite.

**Théorème.** Pour k ≥ 1 : a(k²) = 2k − 1, et a(k² − i) = 2k − 2 − (−1)^i pour 1 ≤ i ≤ 2k − 2.
(Tout n ≥ 1 s'écrit ainsi de façon unique. C'est la formule de Curgus a(n) = 2⌊√n⌋ − (−1)^(n+⌈√n⌉).)

**Preuve**, par récurrence forte sur n ≥ 3 (n = 1, 2 : a = 1, conforme). Soit n = k² − i, avec 0 ≤ i ≤ 2k − 2.
- i = 0 : a(n−1) = a(k² − 1) = 2k − 1, donc n − a(n−1) = (k−1)² et a(n) = 2 + 2(k−1) − 1 = 2k − 1.
- i = 2k − 2, c'est-à-dire n = (k−1)² + 1 : a(n−1) = a((k−1)²) = 2k − 3, donc n − a(n−1) = (k−2)² + 1, où a
  vaut 2k − 5 (même cas pour k − 1, valable dès k ≥ 3 ; pour k = 2, n = 2 est un cas de base). D'où a(n) = 2k − 3.
- 1 ≤ i ≤ 2k − 3 : n − 1 = k² − (i+1), donc a(n−1) = 2k − 2 + (−1)^i et n − a(n−1) = (k−1)² − i′, avec
  i′ = i − 1 + (−1)^i.
  - i impair ≥ 3 : i′ = i − 2 est impair, dans [1, 2(k−1) − 2], donc a = 2k − 3 et a(n) = 2k − 1.
  - i = 1 : n − a(n−1) = (k−1)² + 1, où a vaut 2k − 3 (cas précédent), donc a(n) = 2k − 1.
  - i pair : i′ = i est pair, dans [2, 2(k−1) − 2], donc a = 2k − 5 et a(n) = 2k − 3.
  Dans les trois cas, a(n) = 2k − 2 − (−1)^i.

**Équivalence avec Layman.** n ∈ [K² − 1, (K+1)² − 2] et d ∈ [0, 2K]. Pour d = 0, 1, 2, n = K² − 1, K², K² + 1
et a(n) = 2K − 1. Pour d ≥ 3, n = (K+1)² − i avec i = 2K + 2 − d, donc a(n) = 2K − (−1)^d : 2K − 1 si d est pair,
2K + 1 si d est impair. ∎

**Contrôle** : `check.py` (Layman = Curgus = suite, pour n ≤ 10^6).
