# A100035 : (1) la description explicite des blocs coïncide avec la définition gloutonne sur 2*10^5 termes ;
# (2) formules de Stephan : A100037(n) = 2n^2-n+3, A100038(n) = 2n^2+3n+6, A100039(n) = 2n^2+7n+13 ;
#     A100036 : différences 2 et 4k-7 en alternance (premières occurrences 2k^2-3k+3 et 2k^2-3k+5).
from sim import gen
N = 200000
a = gen(N)
def block(k):
    if k == 1: return [1, 2, 3]
    m = 2 * k
    b = [1, m, m - 1, m + 1]
    for j in range(2, m - 1):            # valeur haute (m si j pair, m+1 sinon) puis valeur basse m-j
        b += [m if j % 2 == 0 else m + 1, m - j]
    b.append(m + 1)
    return b
f = []
k = 1
while len(f) < N: f += block(k); k += 1
assert f[:N] == a, next(i for i in range(N) if f[i] != a[i])
s = lambda k: 2 * k * k - 3 * k + 2                     # position (1-indexée) du début du bloc k
assert all(a[s(k) - 1] == 1 for k in range(1, 300))
pos = {}
for i, v in enumerate(a, 1): pos.setdefault(v, []).append(i)
def chain(start):    # sous-suite gloutonne 1, 2, 3, ... à partir de la position start (valeur 1)
    out, p = [start], start
    for n in range(2, 200):
        p = next(q for q in pos[n] if q > p); out.append(p)
    return out
c2, c3, c4 = chain(pos[1][1]), chain(pos[1][2]), chain(pos[1][3])
assert all(c2[n - 1] == 2*n*n - n + 3 for n in range(1, 200))
assert all(c3[n - 1] == 2*n*n + 3*n + 6 for n in range(1, 200))
assert all(c4[n - 1] == 2*n*n + 7*n + 13 for n in range(1, 200))
first = [pos[n][0] for n in range(1, 400)]
d = [first[i] - first[i - 1] for i in range(1, len(first))]
assert d[:5] == [1, 1, 2, 2, 5] and all(d[n - 2] == (2 if n % 2 else 2 * n - 7) for n in range(6, 399))
print("OK : description des blocs (2e5 termes), A100036-A100039 vérifiées")
