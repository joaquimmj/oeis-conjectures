# Contrôle des définitions de fib.wal contre les données OEIS (positions dans T(F)).
import re
def data(a): return [int(x) for x in re.findall(r"\d+", "".join(l[11:] for l in open(f"../phase0/{a}.txt") if l[:2] in ("%S", "%T", "%U")))]
F = "0"
while len(F) < 20000: F = "".join({"0": "01", "1": "0"}[c] for c in F)
for T, pairs in (({"0": "1", "1": "001"}, [("1", "A287676")]), ({"0": "1", "1": "010"}, [("0", "A287723"), ("1", "A287724")]),
                 ({"0": "1", "1": "011"}, [("1", "A287727")])):
    W = "".join(T[c] for c in F)
    for L, a in pairs:
        pos = [i + 1 for i, c in enumerate(W) if c == L]; d = data(a)
        assert pos[:len(d)] == d, a
print("OK : positions conformes aux données des quatre entrées")
