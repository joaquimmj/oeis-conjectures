# A171947 : équivalence des descriptions (Hofstadter, Zumkeller, Beauchamp x2, Kimberling x2), contrôlée jusqu'à N.
import re
N = 200000
txt = open("../phase0/A171947.txt").read()
data = [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in txt.split("\n") if l[:2] in ("%S", "%T", "%U")))]
# Hofstadter : 1, puis 2k-1 avec k le plus petit non-membre non encore utilisé
S, used, mem = [1], set(), {1}
c = 1
while S[-1] < N:
    c += 1
    while c in mem: c += 1
    S.append(2 * c - 1); mem.add(2 * c - 1)
H = [x for x in S if x <= N]
v2 = lambda x: (x & -x).bit_length() - 1
C = [1] + [n for n in range(2, N + 1) if v2(n - 1) % 2 == 1]                       # caractérisation
assert H == C, "Hofstadter != v2(n-1) impair"
assert data == H[:len(data)], "données"
A003159 = [m for m in range(1, N) if v2(m) % 2 == 0]
assert C[1:] == [2 * m + 1 for m in A003159 if 2 * m + 1 <= N]                   # Zumkeller (hors le terme 1)
assert all(any((n - (2**k + 1)) % 2**(k + 1) == 0 for k in range(1, 40, 2)) == (v2(n - 1) % 2 == 1) for n in range(2, N))  # Beauchamp 1
setC = set(C)
bad = [i for i in range(len(C) - 1) if C[i] + C[i + 1] - 1 <= N and C[i] + C[i + 1] - 1 not in setC]
print("Beauchamp 2 (a(n)+a(n+1)-1 dans la suite) : échecs", bad[:5], len(bad))
# Kimberling 1 : positions (1-indexées) de 1 dans le mot 1-limite de 0->10, 1->00 (point fixe de sigma^2 commençant par 1)
s2 = {"0": "0010", "1": "1010"}
w = "1"
while len(w) < N: w = "".join(s2[ch] for ch in w)
K1 = [i + 1 for i, ch in enumerate(w[:N]) if ch == "1"]
print("Kimberling 1 :", K1[:12] == C[:12], K1 == [x for x in C if x <= len(w[:N])][:len(K1)])
# Kimberling 2 : positions de 0 dans le mot 0-limite de 0->11, 1->01 (point fixe de son carré commençant par 0)
t = {"0": "11", "1": "01"}; t2 = {ch: "".join(t[c] for c in t[ch]) for ch in "01"}
u = "0"
while len(u) < N: u = "".join(t2[ch] for ch in u)
K2 = [i + 1 for i, ch in enumerate(u[:N]) if ch == "0"]
print("Kimberling 2 :", K2[:12], "vs", C[:12], K2 == [x for x in C if x <= N][:len(K2)])
