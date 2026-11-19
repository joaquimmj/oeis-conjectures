# A057194 < A216151 (n > 1) : contrôle direct sur 12 termes ; la preuve (proof.md) est une récurrence immédiate.
def seq(a1, a2, N):
    a = [a1, a2]
    while len(a) < N:
        p = 1
        for v in a: p *= v
        a.append(p * sum(a))
    return a
A, B = seq(1, 1, 12), seq(1, 2, 12)
assert A[:8] == [1, 1, 2, 8, 192, 626688, 1206883411034112, 2804162815248299020572908137501717168128]
assert all(A[n] < B[n] for n in range(1, 12))
print("OK")
