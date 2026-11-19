# Génère le script Walnut : définitions des candidats (pente·n + automate), partition, règles gloutonnes, énoncés.
import sys, json
from fractions import Fraction as F
def gen(name, k, order, rules, lo, slopes, outvals, extra):
    B = "lsd_%d" % k
    L = []
    for x in order:
        r = slopes[x]; p, q = r.numerator, r.denominator
        W = "K%s%s" % (name[1:], x.upper())   # nom sans « A » initial (quantificateur Walnut)
        alts = " | ".join("(%s[n]=@%d & z=t+%d)" % (W, o, o + lo[x]) for o in outvals[x])
        L.append('def %s "?%s Et (%d*t<=%d*n & %d*n<%d*t+%d & (%s))":' % (x, B, q, p, p, q, q, alts))
    L.append('eval fun "?%s An %s":' % (B, " & ".join("(Ez $%s(n,z)) & (Ay,z ($%s(n,y) & $%s(n,z)) => y=z)" % (x, x, x) for x in order)))
    L.append('eval incr "?%s An,y,z %s":' % (B, " & ".join("(($%s(n,y) & $%s(n+1,z)) => y<z)" % (x, x) for x in order)))
    for x in order: L.append('def in%s "?%s En $%s(n,x)":' % (x, B, x))
    one = " | ".join("$in%s(x)" % x for x in order)
    pairs = " & ".join("~($in%s(x) & $in%s(x))" % (x, y) for i, x in enumerate(order) for y in order[i+1:])
    L.append('eval part "?%s (Ax (x>=1) => ((%s) & %s)) & ~(%s)":' % (B, one, pairs, one.replace("(x)", "(0)")))
    for i, x in enumerate(order):
        if rules[x] == "least":
            before = " | ".join("$%s(k,x)" % y for y in order)
            same = "".join(" | $%s(n,x)" % y for y in order[:i])
            L.append('eval greedy_%s "?%s An,x,z ($%s(n,z) & x>=1 & x<z) => ((Ek (k<n & (%s)))%s)":' % (x, B, x, before, same))
        else:
            L.append('eval rule_%s "?%s An,%s,z (%s & $%s(n,z)) => z=%s":' % (x, B, ",".join("v" + y for y in rules[x]), " & ".join("$%s(n,v%s)" % (y, y) for y in rules[x]), x, "+".join("v" + y for y in rules[x])))
    L += extra
    L.append("exit;")
    return "\n".join(L) + "\n"
