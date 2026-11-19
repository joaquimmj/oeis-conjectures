# Test numérique des inégalités de Kimberling, indexation de l'OEIS (n >= 0) et indexation décalée (n -> n+1).
from probe import run, SYS
C = {
 "A297291": {"a": lambda n,v: 0 <= 5*n+4-2*v <= 5, "b": lambda n,v: 0 <= 5*n+8-2*v <= 4, "c": lambda n,v: 0 <= v-5*n <= 4},
 "A297464": {"a": lambda n,v: 0 <= 10*n-6-3*v <= 2, "b": lambda n,v: 0 <= 10*n-2-3*v <= 3, "c": lambda n,v: 0 <= 10*n+1-3*v <= 3, "d": lambda n,v: 0 <= 10*n-3-v <= 2},
 "A299405": {"a": lambda n,v: 0 <= 17*n-11-4*v <= 4, "b": lambda n,v: 0 <= 17*n-7-4*v <= 4, "c": lambda n,v: 0 <= 17*n-3-4*v <= 3, "d": lambda n,v: 0 <= 17*n+1-4*v <= 3, "e": lambda n,v: 0 <= 17*n-5-v <= 3},
}
for name, cs in C.items():
    steps, init = SYS[name]
    s = run(steps, init or {"a": 1, "b": 3, "c": 2}, 200000)
    for x, f in cs.items():
        for sh in (0, 1):
            bad = [n for n in range(len(s[x])) if not f(n + sh, s[x][n])]
            print(name, x, "décalage", sh, "OK" if not bad else "faux, premier n = %d (%d échecs)" % (bad[0], len(bad)))
# compléments : récurrence de A297464, contre-exemple et borne corrigée de A299405 (c), indexation littérale
s = run(*SYS["A297464"], 200000)
a = s["a"]; assert all(a[n] == a[n-1] + a[n-3] - a[n-4] for n in range(4, len(a)))
assert s["d"] == [s["a"][n] + s["b"][n] + s["c"][n] for n in range(len(a))]
t = run(*SYS["A299405"], 200000)
c = t["c"]; assert c[26] == 113 and 17*27 - 3 - 4*113 == 4
assert all(0 <= 17*(n+1) - 3 - 4*c[n] <= 4 for n in range(len(c)))
print("compléments OK")
