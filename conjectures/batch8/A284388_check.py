# A284388 : conjecture de Beck. Vérifie la conjugaison 01 sigma^2(a) = rho'(a) 01 et l'énoncé.
import re
def data(a): return [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
s2 = {"0": "001", "1": "11001"}; rho = {"0": "010", "1": "01110"}
assert all("01" + s2[a] == rho[a] + "01" for a in "01")
X = "0"
while len(X) < 200000: X = "".join(s2[c] for c in X)
assert [int(c) for c in X[:len(data("A284388"))]] == data("A284388")
TM = "0"
while len(TM) < 600000: TM = "".join({"0": "01", "1": "10"}[c] for c in TM)
R = [len(m.group(0)) for m in re.finditer(r"0+|1+", TM)][:-1]
assert R[:len(data("A026465"))] == data("A026465")
Y = X[1:]
assert all(int(Y[i]) == R[i] - 1 for i in range(min(len(Y), len(R)) - 10))
print("OK")
