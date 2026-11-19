# Lecture d'un DFAO Walnut à une entrée et évaluation sur la représentation de Pell (msd, glouton).
import re, sys
def load(path):
    T, out, cur = {}, {}, None
    for line in open(path).read().split("\n")[1:]:
        line = line.strip()
        if not line: continue
        m = re.match(r"^(\d+) (-?\d+)$", line)
        if m: cur = int(m[1]); out[cur] = int(m[2]); T[cur] = {}; continue
        a, b = line.split("->"); T[cur][int(a)] = int(b)
    return T, out
P = [1, 2]
while P[-1] < 10**9: P.append(2 * P[-1] + P[-2])
def rep(n):
    d = []
    for x in reversed(P):
        c = n // x; d.append(c); n -= c * x
    return d
def ev(A, n):
    T, out = A; s = 0
    for c in rep(n):
        s = T[s].get(c)
        if s is None: return None
    return out[s]
if __name__ == "__main__":
    A = load(sys.argv[1]); print([ev(A, n) for n in range(40)])
