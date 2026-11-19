# A226898 : Delta(n) <= d(n)/2 pour n > 4 (conjecture de Greathouse), et le lemme des chaînes de proof.md.
from math import e, log
N = 200000
divs = [[] for _ in range(N + 1)]
for d in range(1, N + 1):
    for m in range(d, N + 1, d): divs[m].append(d)
def Delta(n):                       # max sur u de #{d | n : u <= d <= e*u} ; il suffit de prendre u parmi les diviseurs
    D = divs[n]; best, j = 0, 0
    for i in range(len(D)):
        while j < len(D) and D[j] <= e * D[i]: j += 1
        best = max(best, j - i)
    return best
import re
oeis = [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open("phase0/A226898.txt") if l[:2] in ("%S","%T","%U")))]
assert [Delta(n) for n in range(1, len(oeis) + 1)] == oeis, "données"
assert all(2 * Delta(n) <= len(divs[n]) for n in range(5, N + 1))
assert [n for n in range(1, 5) if 2 * Delta(n) > len(divs[n])] == [1, 2, 4]
print("OK pour 4 < n <=", N)
