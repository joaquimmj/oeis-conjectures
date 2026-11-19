# A363308 : C(x*C(x)^3) mod 2, et l'identité de proof.md dans GF(2)[[x]].
import re
from math import comb
M = 300
cat = [comb(2*k, k) // (k + 1) for k in range(M)]
def imul(a, b): return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(M)]
y = [0] + imul(imul(cat, cat), cat)[:M - 1]
res = [0] * M; p = [1] + [0] * (M - 1)
for k in range(M):
    for i in range(M): res[i] += cat[k] * p[i]
    p = imul(p, y)
oeis = [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open("phase0/A363308.txt") if l[:2] in ("%S", "%T", "%U")))]
assert res[:len(oeis)] == oeis
assert all((res[n] % 2 == 1) == (n == 0 or n & (n - 1) == 0) for n in range(M))
N = 2048                                   # identité A = 1 + y A^2 mod 2, en entiers binaires (bit i = coeff de x^i)
mask = (1 << N) - 1
def m2(a, b):
    r, i = 0, 0
    while b:
        if b & 1: r ^= a << i
        b >>= 1; i += 1
    return r & mask
P = sum(1 << (1 << k) for k in range(N.bit_length()) if (1 << k) < N)
A = P | 1
Cm = sum(1 << ((1 << k) - 1) for k in range(N.bit_length() + 1) if (1 << k) - 1 < N)
y2 = (m2(m2(Cm, Cm), Cm) << 1) & mask
assert (m2(y2, m2(A, A)) ^ 1) == A
print("OK : énoncé et données pour n <", M, "; identité mod 2 jusqu'à x^%d" % N)
