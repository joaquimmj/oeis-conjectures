# Transformées {u -> c} du mot de Thue-Morse : a(n)/n -> 1/f, avec f calculé EXACTEMENT par les fréquences des
# facteurs de TM (vecteur de Perron de la substitution induite sur les blocs de longueur l ; Queffélec).
import re
import sympy as sp
P0 = "../phase0/"
def txt(a): return open(P0 + a + ".txt").read()
def data(a): return [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(P0 + a + ".txt") if l[:2] in ("%S", "%T", "%U")))]
TM = "0"
while len(TM) < 400000: TM = "".join({"0": "01", "1": "10"}[c] for c in TM)
def factor_freqs(l):
    blocks = sorted({TM[i:i + l] for i in range(5000)})
    idx = {b: i for i, b in enumerate(blocks)}
    M = sp.zeros(len(blocks))
    for b in blocks:
        s = "".join({"0": "01", "1": "10"}[c] for c in b)
        for j in range(2): M[idx[s[j:j + l]], idx[b]] += 1        # blocs de sigma(b) commençant en 0 et 1
    v = (M - 2 * sp.eye(len(blocks))).nullspace()[0]
    v = v / sum(v)
    return {b: sp.nsimplify(v[idx[b]]) for b in blocks}
FF = {l: factor_freqs(l) for l in range(1, 5)}
def check_ff():   # contrôle numérique des fréquences exactes
    for l, F in FF.items():
        for b, f in F.items():
            emp = sum(1 for i in range(200000) if TM[i:i + l] == b) / 200000
            assert abs(emp - float(f)) < 3e-3, (b, f, emp)
check_ff()
targets = [x.strip() for x in open("limit_targets.txt")]
out = []
for a in targets:
    T = txt(a)
    nm = next(l for l in T.split("\n") if l.startswith("%N"))
    base = re.search(r"in (A\d{6})", nm)
    if not base:
        if a == "A003157": base, L = "A286044", "1"
        else: continue
    else:
        mL = re.search(r"Positions of ([01])", T)
        if not mL: continue
        base = base.group(1); L = mL.group(1)
    bn = next(l for l in txt(base).split("\n") if l.startswith("%N"))
    m = re.search(r"\{([01]+)->([01])\}-transform of the Thue-Morse word", bn)
    if not m: continue
    u, c = m.group(1), m.group(2)
    W = TM.replace(u, c)
    bd = data(base); ok_base = [int(x) for x in W[:len(bd)]] == bd
    pos = [i + 1 for i, x in enumerate(W) if x == L]; d = data(a); ok_pos = pos[:len(d)] == d
    fu = FF[len(u)][u]
    fL = (sp.Rational(1, 2) - u.count(L) * fu + (1 if c == L else 0) * fu) / (1 - (len(u) - 1) * fu)
    r = sp.nsimplify(1 / fL)
    conj = next(l[11:] for l in T.split("\n") if l.startswith("%") and re.search(r"onjecture[^.]*a\(n\)/n\s*->", l))
    mm = re.search(r"a\(n\)\s*/\s*n\s*->\s*([0-9/.]+)", conj); stated = sp.nsimplify(mm.group(1).rstrip("."))
    out.append((a, base, u, c, L, ok_base, ok_pos, r, stated, r == stated, pos[-1] / len(pos)))
for o in out:
    a, base, u, c, L, ob, op, r, st, eq, obs = o
    print(f"{a} : {{{u}->{c}}}(TM) = {base}, lettre {L}, données {'OK' if ob and op else 'ÉCART'} ; limite exacte {r} ; énoncée {st} ; {'VRAIE' if eq else 'FAUSSE'} (observé {obs:.5f})")
