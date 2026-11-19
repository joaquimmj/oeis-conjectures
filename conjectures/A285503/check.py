# A285503, A285517, A285567, A285623, A285627, A285663 : a(n)/n -> phi (positions de 1).
import re
from math import sqrt
phi = (1 + sqrt(5)) / 2
def data(a): return [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
def word(sig, c, N=400000):
    if sig[c][0] != c: sig = {x: "".join(sig[y] for y in sig[x]) for x in "01"}
    w = c
    while len(w) < N: w = "".join(sig[x] for x in w)
    return w[:N]
W = {"A285503": word({'0': '11', '1': '0011'}, '0'), "A285567": word({'0': '11', '1': '0110'}, '0'),
     "A285623": word({'0': '11', '1': '1001'}, '1'), "A285627": word({'0': '11', '1': '1010'}, '1'),
     "A285663": word({'0': '11', '1': '1100'}, '1')}
w = W["A285503"]; assert all(w[i] == w[i + 1] for i in range(0, len(w) - 1, 2))      # paires alignées 00 / 11
W["A285517"] = w[::2]                                                                  # transformée {00->0, 11->1}
for a, x in W.items():
    pos = [i + 1 for i, c in enumerate(x) if c == "1"]; d = data(a)
    assert pos[:len(d)] == d, a
    print(a, "a(n)/n en n =", len(pos), ":", round(pos[-1] / len(pos), 6), " phi =", round(phi, 6))
