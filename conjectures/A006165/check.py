# A006165 : contrôle numérique des conjectures (i)-(vii) de Bala et de la formule des itérées (proof.md).
def A6165(n): return 1 if n <= 2 else A6165(n // 2) + A6165((n + 1) // 2)
N = 1 << 15
a = [0] + [A6165(n) for n in range(1, N + 1)]
def it(k, n):
    for _ in range(k): n = a[n]
    return n
for k in range(1, 12):                                     # formule des itérées
    for n in range(1, N + 1):
        m = n.bit_length() - 1
        assert it(k, n) == (min(n - (2**k - 1) * 2**(m - k), 2**(m - k + 1)) if k <= m else 1)
A = lambda m: a[m]
for n in range(2, N + 1):
    assert A(n) + A(n - A(n - A(n - A(n - A(n))))) == n                                   # (i)
    assert A(n - A(n - A(n - A(n)))) == A(n - A(n - A(n - A(n - A(n - A(n))))))           # (ii)
    assert it(2, n) == A(n - A(n - A(n - A(n))))                                          # (iii)
    assert n - A(n) == A(n - it(2, n))                                                    # (iv)
    assert A(n - A(n)) == it(2, n - it(2, n - it(2, n - it(2, n))))                       # (v)
    for k in range(2, 12):                                                                # (vi)
        I = lambda x: it(k, x)
        assert I(n - I(n)) == I(n - I(n - I(n - I(n))))
for k in range(1, 12):                                                                    # (vii)
    s = [n - it(k, n) for n in range(1, N + 1)]
    assert all(y - x in (0, 1) for x, y in zip(s, s[1:]))
    from collections import Counter
    for v, c in Counter(s).items():
        if c > 1:
            j = (v // (2**k - 1)).bit_length() - 1
            assert v == (2**k - 1) * 2**j and (c == 2**j + 1 or v + 2**(k+j) > N)  # multiplicité 2^j + 1 (A000051)
print("OK pour n <=", N, "et k <= 11")
