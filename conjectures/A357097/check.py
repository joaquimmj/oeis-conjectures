# A357097 : contrôle de la conjecture A(A019586(x), A019586(y)) = A019586(A101330(x,y)) et des étapes de proof.md.
# Tout est en entiers : un élément a + b*phi de Z[phi] est le couple (a, b).
from math import isqrt
import sys
sys.setrecursionlimit(10000)
fl_phi = lambda n: (n + isqrt(5 * n * n)) // 2            # floor(n*phi)
F = [0, 1]
while len(F) < 90: F.append(F[-1] + F[-2])
def zeck(n):                                              # indices de Zeckendorf (>= 2), décroissants
    out, k = [], 89
    while n:
        while F[k] > n: k -= 1
        out.append(k); n -= F[k]
    return out
circ = lambda x, y: sum(F[c + d] for c in zeck(x) for d in zeck(y))        # produit de Knuth (A101330)
theta = lambda n: (sum(F[c - 1] for c in zeck(n)), n)                       # sum phi^c = sum F(c-1) + F(c) phi
mul = lambda u, v: (u[0] * v[0] + u[1] * v[1], u[0] * v[1] + u[1] * v[0] + u[1] * v[1])   # phi^2 = phi + 1
def row(n):                                               # A019586 : ligne (à partir de 0) du tableau de Wythoff contenant n
    j, k = sum(F[c + 1] for c in zeck(n)), n              # (successeur de n dans sa ligne, n)
    while j != fl_phi(k + 1): j, k = k, j - k             # remonte jusqu'à (eW(z,1), eW(z,0)) = (floor((z+1)phi), z)
    return k
A019586 = [0, 0, 0, 1, 0, 2, 1, 0, 3, 2, 1, 4, 0, 5, 3, 2, 6, 1, 7, 4, 0, 8, 5, 3, 9, 2, 10, 6, 1, 11, 7, 4, 12]
assert [row(n) for n in range(1, 34)] == A019586
def A(x, y):                                              # formule de l'entrée A357097
    j1, k1 = 2 * fl_phi(x + 1) + x, fl_phi(x + 1) + x     # A035336(x+1), A003622(x+1)
    j2, k2 = 2 * fl_phi(y + 1) + y, fl_phi(y + 1) + y
    j, k = j1 * j2 + k1 * k2, j1 * k2 + k1 * j2 - k1 * k2
    while j != fl_phi(k + 1): j, k = k, j - k
    return k
data = [0,1,1,2,15,2,3,8,8,3,4,12,4,12,4,5,44,18,18,44,5,6,19,24,27,24,19,6,7,62,28,96,96,28,62,7]
assert [A(x, d - x) for d in range(8) for x in range(d + 1)] == data       # données de l'entrée, par antidiagonales
N = 400
for x in range(1, N):
    for y in range(x, N):
        assert mul(theta(x), theta(y)) == theta(circ(x, y))               # étape 3 : theta multiplicative
        assert A(row(x), row(y)) == row(circ(x, y))                        # la conjecture
print(f"OK pour 1 <= x <= y < {N}")
