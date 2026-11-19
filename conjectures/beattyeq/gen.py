# Famille A297830 : a(n) = 2b(n-s) - b(n-s-1) + c*n + d (s = 1 : « b(n-1), b(n-2) » ; s = 0 : « b(n), b(n-1) »),
# a(0) = 1, a(1) = 2, b complément croissant de a. Génération par marquage (a est croissante et a(n) > b utilisés).
def gen(s, c, d, N):
    a = [1, 2]; mark = bytearray(8 * N + 100); mark[1] = mark[2] = 1
    b, p = [], 0
    def bb(j):
        nonlocal p
        while len(b) <= j:
            p += 1
            if not mark[p]: b.append(p)
        return b[j]
    for n in range(2, N):
        v = 2 * bb(n - s) - bb(n - s - 1) + c * n + d
        assert v > a[-1] and v > b[-1] and not mark[v], n
        a.append(v); mark[v] = 1
    return a, b[:N - 2]
