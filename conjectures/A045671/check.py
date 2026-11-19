# A045671/A045672 : (1) mex + b = 2a + 2n == positions des 1 / des 0 du point fixe de 0->11, 1->1110 (1-indexées) ;
# (2) faits structurels : pas de « 00 », le n-ième 0 est après le n-ième 1. Contrôle contre les données OEIS.
import re
def gen(N):
    a, b, used, m = [0], [0], {0}, 0
    for n in range(1, N):
        while m in used: m += 1
        a.append(m); b.append(2 * m + 2 * n); used |= {m, b[-1]}
    return a, b
a, b = gen(50000)
w = "1"
while len(w) < b[-1] + 10: w = "".join({"0": "11", "1": "1110"}[c] for c in w)
ones = [i + 1 for i, c in enumerate(w) if c == "1"]; zeros = [i + 1 for i, c in enumerate(w) if c == "0"]
assert a[1:] == ones[:len(a) - 1] and b[1:] == zeros[:len(b) - 1]
assert "00" not in w and all(zeros[n] > ones[n] for n in range(len(zeros)))
for A, s in (("A045671", a), ("A045672", b)):
    t = open("../phase0/%s.txt" % A).read()
    d = [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in t.split("\n") if l[:2] in ("%S", "%T", "%U")))]
    assert s[:len(d)] == d, A
print("OK")
