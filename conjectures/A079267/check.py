# A079267 : conjecture de Callan (loi de Poisson de paramètre 1 à la limite).
from math import factorial, e
def dfact(n): return factorial(2 * n) // (2 ** n * factorial(n))
def d(n, s):   # formule de l'entrée : d(n,s) = (1/s!) Sum_h (-1)^(h-s) (2n-h)! / (2^(n-h) (n-h)! (h-s)!)
    return sum((-1) ** (h - s) * factorial(2 * n - h) * 2 ** h // (factorial(n - h) * factorial(h - s)) for h in range(s, n + 1)) // (2 ** n * factorial(s))
data = [1, 0, 1, 1, 1, 1, 5, 6, 3, 1, 36, 41, 21, 6, 1, 329, 365, 185, 55, 10, 1]
assert [d(n, s) for n in range(6) for s in range(n + 1)] == data
for n in range(1, 60):                                                             # r_h <= 1
    for h in range(n + 1):
        assert factorial(2 * n - h) * 2 ** h * factorial(n) <= factorial(2 * n) * factorial(n - h)
for n in (20, 100, 300):
    print(n, [round(d(n, s) / dfact(n), 6) for s in range(4)], [round(e ** -1 / factorial(s), 6) for s in range(4)])
