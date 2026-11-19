# A298173, A298741 : génération depuis la définition et contrôle des bornes de proof.md.
def gen(k, x0, N):
    a, b, used, m = [1], [2], {1, 2}, 1
    for n in range(1, N):
        while m in used: m += 1
        b.append(m); used.add(m)
        S = sum((-1)**j * b[n - j] for j in range(n + 1))       # x(j) = (-1)^j
        v = k * a[-1] + S + (x0 - 1) * b[n]
        assert v not in used; a.append(v); used.add(v)
    return a, b
for A, k, x0, lo, hi in (("A298173", 3, 1, lambda n: (n + 1) // 2, lambda n: 2*n + 1),
                         ("A298741", 2, 2, lambda n: n + 1, lambda n: 4*n + 2)):
    a, b = gen(k, x0, 400)
    import json, glob
    E = {}
    for f in glob.glob("../crawl/raw_*.json"): E.update(json.load(open(f)))
    data = [int(v) for v in E[A]["data"].split(",")]
    assert a[:len(data)] == data, A
    assert all(b[n] <= 2*n + 1 for n in range(1, len(b)))   # n >= 1 : 2n entiers placés avant b(n)
    d = [a[n] - k * a[n-1] for n in range(1, len(a))]
    assert all(lo(n) <= d[n-1] <= hi(n) for n in range(1, len(a)))
    print(A, "données OK,", len(data), "termes ; d(n) dans les bornes ; a(399)/a(398) - k =", float(a[-1] / a[-2] - k))
