import sys
from probe import run, SYS
from guess import guess, walnut_file
from fractions import Fraction as F
name, k, N = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
steps, init = SYS[name]
s = run(steps, init, N)
slopes = {}; meta = {}
for x, v in s.items():
    r = F(v[-1] - v[1000], len(v) - 1 - 1000).limit_denominator(40); slopes[x] = r
    dev = [v[n] - (r.numerator * n) // r.denominator for n in range(len(v))]
    lo = min(dev)
    out, tr = guess(dev, k)
    fn = "/home/user/Walnut/Word Automata Library/K%s%s.txt" % (name[1:], x.upper())
    walnut_file(fn, k, out, tr, -lo)
    meta[x] = dict(p=r.numerator, q=r.denominator, lo=lo, outs=sorted(set(out)))
    print(x, "pente", r, "décalage", -lo, "états", len(out))
import json; json.dump(meta, open("meta_%s.json" % name, "w"))
