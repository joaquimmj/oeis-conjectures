# A285590/1/3/4 : {00->0, 11->1}-transformées (gloutonnes) de A285565/A285568 (mots limites de 0 -> 11, 1 -> 0110).
# Fréquences EXACTES des facteurs (vecteur de Perron de la substitution induite sur les l-blocs), puis des plages.
import re
import sympy as sp
P0 = "../phase0/"
def data(a): return [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(P0 + a + ".txt") if l[:2] in ("%S", "%T", "%U")))]
sig = {'0': '11', '1': '0110'}
def limword(c, N=300000):
    t = {x: "".join(sig[y] for y in sig[x]) for x in "01"}; w = c
    while len(w) < N: w = "".join(t[x] for x in w)
    return w[:N]
def greedy(w):
    out, i = [], 0
    while i < len(w):
        if w[i:i + 2] in ("00", "11"): out.append(w[i]); i += 2
        else: out.append(w[i]); i += 1
    return "".join(out)
W0, W1 = limword('0'), limword('1')
assert [int(x) for x in W0[:len(data("A285565"))]] == data("A285565") and [int(x) for x in W1[:len(data("A285568"))]] == data("A285568")
G0, G1 = greedy(W0), greedy(W1)
assert [int(x) for x in G0[:len(data("A285589"))]] == data("A285589") and [int(x) for x in G1[:len(data("A285592"))]] == data("A285592")
# plage de k lettres x -> ceil(k/2) lettres x (contrôle empirique de la sémantique)
runs = lambda w: [(m.group(0)[0], len(m.group(0))) for m in re.finditer(r"0+|1+", w)]
assert "".join(x * ((k + 1) // 2) for x, k in runs(W0[:100000]))[:5000] == G0[:5000]
maxrun = max(k for _, k in runs(W0))
l = maxrun + 2
lam = (1 + sp.sqrt(5))                                  # valeur propre de Perron de M = [[0,2],[2,2]]
def factor_freqs(l, sample):
    blocks = sorted({sample[i:i + l] for i in range(len(sample) - l)})
    idx = {b: i for i, b in enumerate(blocks)}
    M = sp.zeros(len(blocks))
    for b in blocks:
        s = "".join(sig[c] for c in b)
        for j in range(len(sig[b[0]])): M[idx[s[j:j + l]], idx[b]] += 1
    v = (M - lam * sp.eye(len(blocks))).nullspace()[0]
    v = v / sum(v)
    return {b: sp.nsimplify(sp.simplify(v[idx[b]])) for b in blocks}
F = factor_freqs(l, W0[:200000])
for b, f in list(F.items())[:6]:
    emp = sum(1 for i in range(200000) if W0[i:i + l] == b) / 200000
    assert abs(emp - float(f)) < 5e-3, (b, f, emp)
def runfreq(x, k):   # fréquence d'une plage maximale x^k = somme des fréquences des facteurs y x^k y de longueur l
    y = "1" if x == "0" else "0"; core = y + x * k + y
    return sum(f for b, f in F.items() if b.startswith(core)) if len(core) <= l else 0
num = {x: sum(sp.ceiling(sp.Rational(k, 2)) * runfreq(x, k) for k in range(1, maxrun + 1)) for x in "01"}
tot = num["0"] + num["1"]
for a, x, conj in (("A285590", "0", "1+sqrt(5/4)"), ("A285591", "1", "1+sqrt(4/5)"), ("A285593", "0", "1+sqrt(5/4)"), ("A285594", "1", "1+sqrt(4/5)")):
    G = G0 if a in ("A285590", "A285591") else G1
    pos = [i + 1 for i, c in enumerate(G) if c == x]; d = data(a)
    r = sp.nsimplify(sp.simplify(tot / num[x]))
    st = sp.sympify(conj)
    print(f"{a} : données {'OK' if pos[:len(d)] == d else 'ÉCART'} ; limite exacte {r} ≈ {float(r):.6f} ; énoncée {st} ≈ {float(st):.6f} ; "
          f"{'VRAIE' if sp.simplify(r - st) == 0 else 'FAUSSE'} (observé {pos[-1] / len(pos):.5f})")
