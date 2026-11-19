# A088617 : nombre moyen de pas U dans un chemin de Schröder de demi-longueur n, divisé par n, -> 1/sqrt(2).
from math import comb, sqrt
for n in (10, 100, 1000, 4000):
    T = [comb(n + k, n) * comb(n, k) // (k + 1) for k in range(n + 1)]
    E = sum(k * t for k, t in enumerate(T)) / sum(T)
    r = [(n + k + 1) * (n - k) / ((k + 1) * (k + 2)) for k in range(n)]
    assert all(r[k] > r[k + 1] for k in range(n - 1))                     # rapport décroissant
    print(n, round(E / n, 5), "écart à 1/sqrt2 :", round(E / n - 1 / sqrt(2), 5))
