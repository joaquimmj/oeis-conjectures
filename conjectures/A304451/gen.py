# A304451/A304452 : b(n) = least new, a(n) = b(n) + b(floor(n/2)), b(0) = 1 (définition de l'entrée).
def gen(N):
    used, a, b = set(), [], []
    m = 1
    for n in range(N):
        while m in used: m += 1
        b.append(m); used.add(m)
        v = b[n] + b[n // 2]; assert v not in used, n
        a.append(v); used.add(v)
    return a, b
