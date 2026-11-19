# A128440 (Kimberling 2022) : les lignes 2n−1 et 2n de ⌊kφⁿ⌋ sont disjointes — **non résolue**

- **Numérique** (`scan.py`) : aucune intersection pour n ≤ 12 et k ≤ 2·10⁵.
- **Réduction (prouvée).** La conjecture « forte » de Kimberling, où les deux lignes s'entrelacent comme les lignes
  de Wythoff, équivaut à la disjonction. Avec α = φ^{2n−1}, δ = kφ − j, et les conjugués dans ℤ[φ], on obtient
  ⌊kφα⌋ − ⌊jα⌋ = δα + {j/α} + {k/(φα)} − 1. Cette quantité est donc ≥ 0 si δ > 0 et ≤ 0 si δ < 0. Une fois la
  disjonction acquise, l'ordre relatif est celui de j et kφ, c'est-à-dire celui des suites de Wythoff.
- **Ce qui manque :** exclure le cas d'égalité. Ni une caractérisation par les suffixes de Zeckendorf ni une
  application de décalage commune ne fonctionnent (l'écart avec ⌊φ²N⌋ vaut 0 à 3).

Non comptée.
