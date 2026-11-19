# A373308, A000918, A048881, A059906, A073089 : contrôles des preuves de proof.md.
import re
from math import comb, gcd
def data(a): return [int(x) for x in re.findall(r"-?\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
t = lambda n: bin(n).count("1") % 2
s2 = lambda n: bin(n).count("1")
v2 = lambda n: (n & -n).bit_length() - 1
# A373308
N = 3000; P = [(-1) ** t(i) for i in range(N)]
sq = [sum(P[i] * P[k - i] for i in range(k + 1)) for k in range(N)]
cu = [sum(sq[i] * P[k - i] for i in range(k + 1)) for k in range(N)]
assert cu[:len(data("A373308"))] == data("A373308")
assert all((cu[3 * k] - (1 if t(k) == 0 else 2)) % 3 == 0 for k in range(N // 3)) and all(cu[k] % 3 == 0 for k in range(N) if k % 3)
# A000918
cat = lambda m: comb(2 * m, m) // (m + 1)
assert all(v2(cat(m)) == s2(m + 1) - 1 for m in range(1, 3000))
assert all(min(m for m in range(0, 2 ** n) if v2(cat(m)) == n - 1) == 2 ** n - 2 for n in range(1, 12))
# A048881 : n-ième mot de A076478 (mots binaires par longueur puis ordre numérique)
words = [format(v, f"0{L}b") for L in range(1, 13) for v in range(2 ** L)]
assert all(sum(map(int, words[n])) == s2(n + 2) - 1 for n in range(len(words)))   # n-ième (à partir de 0) <-> A048881(n+1)
seq = [s2(n + 1) - 1 for n in range(len(words) + 1)]
assert all(seq[n] == sum(map(int, words[n - 1])) for n in range(1, len(words)))
# A059906
j = lambda n: int("".join(b for i, b in enumerate(bin(n)[2:][::-1]) if i % 2 == 1)[::-1] or "0", 2)
assert [j(n) for n in range(len(data("A059906")))] == data("A059906")
for n in range(0, 5000):
    assert 2 * j(n) == 2 * n - sum((1 + (-1) ** v2(k)) * 2 ** (v2(k) // 2) * (1 if v2(k) % 2 == 0 else 0) for k in range(1, n + 1))  # forme 1
    assert j(n) == -sum((-1) ** k * 2 ** (k // 2) * (n // 2 ** k) for k in range(1, n.bit_length() + 1))                       # forme 2
# A073089
d = data("A073089")
A057661 = lambda m: sum(m * k // gcd(m, k) for k in range(1, m + 1)) // m
assert all(A057661(m) * 2 == 1 + sum(e * phi for e, phi in ((dd, sum(1 for i in range(1, dd + 1) if gcd(i, dd) == 1)) for dd in range(1, m + 1) if m % dd == 0)) for m in range(1, 300))
assert all(d[n - 1] == (1 + (-1) ** A057661(n - 1)) // 2 for n in range(2, len(d) + 1))
pf = lambda m: 1 if (m >> v2(m)) % 4 == 1 else 0                                         # A014577(m-1)
assert all(d[n - 1] == pf(n - 1) + [1, 0, -1, 0][n % 4] for n in range(2, len(d) + 1))
assert all((1 + (-1) ** A057661(n - 1)) // 2 == pf(n - 1) + [1, 0, -1, 0][n % 4] for n in range(2, 2000))
print("OK")
