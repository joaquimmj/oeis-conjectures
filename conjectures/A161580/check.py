# Conjecture de Shevelev, deux variantes, contrôle numérique indépendant de Walnut.
t = lambda n: bin(n).count("1") % 2
for k in range(1, 400, 2):
    for f in (lambda n: t(n) == t(n + k), lambda n: t(n) != t(n + k)):
        s = [n for n in range(20000) if f(n)]
        assert all(t(x) != t(y) for x, y in zip(s, s[1:])), k
print("OK : k impair < 400, n < 20000")
