# Systèmes de Kimberling : génération et test d'automaticité (taille du 2-noyau/3-noyau de a(n) - round(rn)).
from fractions import Fraction as F
def run(steps, init, N):
    used = set(); seqs = {k: [] for k, _ in steps}
    for k, v in init.items(): seqs[k].append(v); used.add(v)
    m = 1
    def least(lo=1):
        x = lo
        while x in used: x += 1
        return x
    n = 1
    while n < N:
        for k, rule in steps:
            if len(seqs[k]) > n: continue
            v = rule(seqs, n, least)
            assert v not in used, (k, n, v); seqs[k].append(v); used.add(v)
        n += 1
    return seqs
SYS = {
 "A297291": ([("a", lambda s,n,L: L()), ("b", lambda s,n,L: L(s["a"][n]+2)), ("c", lambda s,n,L: s["a"][n]+s["b"][n]-2)], None),
 "A297464": ([("a", lambda s,n,L: L()), ("b", lambda s,n,L: L()), ("c", lambda s,n,L: L()), ("d", lambda s,n,L: s["a"][n]+s["b"][n]+s["c"][n])], {"a":1,"b":2,"c":3,"d":6}),
 "A299405": ([("a", lambda s,n,L: L()), ("b", lambda s,n,L: L()), ("c", lambda s,n,L: L()), ("d", lambda s,n,L: L()), ("e", lambda s,n,L: sum(s[x][n] for x in "abcd"))], {"a":1,"b":2,"c":3,"d":4,"e":10}),
 "A299634": ([("a", lambda s,n,L: L(2*s["b"][n-1])), ("b", lambda s,n,L: L()), ("c", lambda s,n,L: s["a"][n]+s["b"][n])], {"a":1,"b":2,"c":3}),
}
def kernel(seq, k, depth=6, pref=60):
    subs = set()
    for e in range(depth):
        for r in range(k**e):
            sub = tuple(seq[k**e*i + r] for i in range(pref) if k**e*i + r < len(seq))
            if len(sub) == pref: subs.add(sub)
    return len(subs)
if __name__ == "__main__":
    import sys
    for name, (steps, init) in SYS.items():
        if init is None:   # A297291 : a(0) = 1, b(0) = 3 (least new >= a+2), c(0) = a+b-2 = 2
            init = {"a": 1, "b": 3, "c": 2}
        s = run(steps, init, 60000)
        print(name, {k: v[:12] for k, v in s.items()})
        for k, v in s.items():
            r = F(v[-1] - v[1000], len(v) - 1 - 1000)
            dev = [v[n] - (r.numerator*n)//r.denominator for n in range(len(v))]
            print("  ", k, "pente ~", float(r), "écarts", sorted(set(dev[:20000]))[:12], "noyau2", kernel(dev, 2), "noyau3", kernel(dev, 3, 5))
