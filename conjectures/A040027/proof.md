# A040027 (nombres de Gould) — conjecture de Yanev (2021) : vraie

**Énoncé.** a(n) = Σ_{k=0}^{n} A058006(k)·S(n+1, k+1), où A058006(k) = c_k = Σ_{j≤k} (−1)^j j!.

**Preuve** (séries formelles).
- Σₙ S(n+1, k+1) xⁿ/n! = d/dx[(eˣ − 1)^(k+1)/(k+1)!] = eˣ(eˣ − 1)ᵏ/k!. La série génératrice exponentielle du
  membre de droite est donc H(x) = eˣ·C(eˣ − 1), avec C(y) = Σ c_k yᵏ/k!. La composition est licite, eˣ − 1 étant
  sans terme constant.
- Comme c_{k+1} − c_k = (−1)^(k+1)(k+1)!, on a C′ − C = −Σ (−1)ᵏ(k+1)yᵏ = −1/(1+y)².
- Avec u = eˣ − 1 (u′ = 1 + u = eˣ) : H′ = eˣC(u) + e^(2x)C′(u) = H + e^(2x)C(u) − 1 = (1 + eˣ)H − 1, et H(0) = c_0 = 1.
- La caractérisation de l'entrée (« e.g.f. satisfies A′(x) = exp(x)A(x) + 1 », Sloane) porte sur la suite décalée
  s(n) = a(n−1) (S(0) = 0). H = S′ vérifie alors H = 1 + eˣ∫₀ˣ H, et en dérivant H′ = (1 + eˣ)H − 1, avec H(0) = 1.
  Les deux séries vérifient la même équation différentielle avec la même condition initiale, donc elles sont
  égales. ∎
- La formule de Bala (partitions de [n+1] dont le dernier bloc est un singleton) coïncide aussi (contrôle numérique).

**Contrôle** : `check.py` (n < 120 : données de l'entrée, équation différentielle et e.g.f. de Sloane ; formule de
Bala pour n < 40).
