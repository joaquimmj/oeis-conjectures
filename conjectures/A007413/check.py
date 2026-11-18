# Conjecture de Shevelev, testée depuis les définitions OEIS (sans Walnut).
N = 10**6
t = [bin(k).count("1") % 2 for k in range(N)]
a076826, s = [], 0
for n in range(N):
    s += t[n]; a076826.append(2 * s - n)          # a(n) = 2 * sum_{k<=n} t(k) - n
w = [1]                                           # A007413 : 1->123, 2->13, 3->2
mu = {1: [1, 2, 3], 2: [1, 3], 3: [2]}
while len(w) < N: w = [c for x in w for c in mu[x]]
twos = [n for n, v in enumerate(a076826) if v == 2]
ones = [a076826[p+1:q].count(1) for p, q in zip(twos, twos[1:])]
assert ones == w[:len(ones)], "échec"
print(f"OK : {len(ones)} termes de A007413 retrouvés")
