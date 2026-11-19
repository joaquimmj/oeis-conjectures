# A055938 : conjectures de Stephan (2013), et les étapes de proof.md.
N = 1 << 16
s = lambda m: bin(m).count("1")
V = {2 * m - s(m) for m in range(N)}                     # A005187
c = [x for x in range(1, 2 * N - 40) if x not in V]      # A055938 (offset 1 : c[0] = a(1))
# règle de Stephan : b(1) = 2, b(n+1) = b(n) + 1 si n est dans la suite, + 3 sinon
C = set(c); b = [2]
while len(b) < len(c): b.append(b[-1] + (1 if len(b) in C else 3))
assert b == c
# A080578 : a(1) = 1, a(n) = a(n-1) + 1 si n est déjà dans la suite, + 3 sinon (récurrence auto-référente)
A = [None, 1]; S = {1}
for n in range(2, len(c) + 2):
    A.append(A[-1] + (1 if n in S else 3)); S.add(A[-1])
assert all(c[n - 1] == A[n + 1] - 2 for n in range(1, len(c)))        # a(n) = A080578(n+1) - 2
assert all(c[n - 1] == (A[n + 1] - 2 * (n + 1)) + 2 * n for n in range(1, len(c)))   # = A080468(n+1) + 2n
# étapes : écarts de A005187 = 1 + t(m) ; positions des sauts de 3 = A005187 \ {0}
t = lambda m: (~m & (m + 1)).bit_length() - 1
assert all((2 * (m + 1) - s(m + 1)) - (2 * m - s(m)) == 1 + t(m) for m in range(N))
jumps = {n for n in range(1, len(c)) if c[n] - c[n - 1] == 3}
assert jumps == {x for x in V if 0 < x < len(c)}
print("OK :", len(c), "termes")
