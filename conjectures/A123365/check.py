# Contrôles des faits utilisés dans proof.md (A123722, A123723) : formules de s(q) aux puissances premières,
# lemme s(r) <= (r+1)/2 pour r impair (égalité ssi r = 1 ou r premier), bornes de rapports.
from sympy import factorint, isprime
s = lambda q: len({x * x % q for x in range(q)})
for b in range(1, 18):
    f = 2 if b == 1 else ((2**(b - 1) + 5) // 3 if b % 2 else (2**(b - 1) + 4) // 3)
    assert s(2**b) == f, b
    if b >= 4: assert 4 * s(2**b) <= 2**b
for p in (3, 5, 7, 11, 13):
    for e in range(1, 6 if p < 10 else 4):
        q = p**e
        f = (p**(e + 1) + p + 2) // (2 * (p + 1)) if e % 2 == 0 else (p**(e + 1) + 2 * p + 1) // (2 * (p + 1))
        assert s(q) == f, (p, e)
        if e >= 2: assert 2 * s(q) < q + 1
def S(n):
    r = 1
    for p, e in factorint(n).items(): r *= s(p**e)
    return r
for r in range(1, 30001, 2):
    v = S(r)
    assert 2 * v <= r + 1 and ((2 * v == r + 1) == (r == 1 or isprime(r))), r
assert all(9 * S(3**a) <= 4 * 3**a for a in range(2, 9))
print("OK")
